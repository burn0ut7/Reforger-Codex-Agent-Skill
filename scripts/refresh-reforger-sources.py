#!/usr/bin/env python3
"""Refresh and index Reforger source data by orchestrating existing scripts."""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]

EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EXIT_CANNOT_DETERMINE = 2
EXIT_STALE = 10


@dataclass(frozen=True)
class Command:
    args: list[str]
    display: str


@dataclass(frozen=True)
class Stage:
    name: str
    command: Command | None = None
    check: Callable[[], tuple[int, str]] | None = None
    stale_is_failure: bool = False


@dataclass
class StageResult:
    name: str
    status: str
    exit_code: int
    elapsed: float
    display: str


def py_script(script: str, *args: str) -> Command:
    display_parts = ["py", "-3", script.replace("/", "\\"), *args]
    return Command([sys.executable, str(ROOT / script), *args], " ".join(display_parts))


def powershell_script(script: str, *args: str) -> Command:
    display_parts = ["powershell", "-ExecutionPolicy", "Bypass", "-File", script.replace("/", "\\"), *args]
    return Command(
        ["powershell", "-ExecutionPolicy", "Bypass", "-File", str(ROOT / script), *args],
        " ".join(display_parts),
    )


def has_scope(args: argparse.Namespace) -> bool:
    return bool(args.all or args.game_data or args.wiki or args.samples or args.validate)


def selected_scopes(args: argparse.Namespace) -> dict[str, bool]:
    run_all = args.all or not has_scope(args)
    return {
        "game_data": run_all or args.game_data,
        "wiki": run_all or args.wiki,
        "samples": run_all or args.samples,
        "validate": args.validate or (run_all and not args.no_validate and not args.check),
    }


def check_path_exists(path: Path, label: str) -> tuple[int, str]:
    if path.exists():
        return EXIT_SUCCESS, f"{label} exists: {path}"
    return EXIT_STALE, f"{label} missing: {path}"


def check_samples() -> tuple[int, str]:
    samples_root = ROOT / "raw" / "samples"
    git_dir = samples_root / ".git"
    if not git_dir.exists():
        return EXIT_STALE, f"samples git checkout missing: {git_dir}"

    try:
        completed = subprocess.run(
            ["git", "-C", str(samples_root), "rev-parse", "HEAD"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except OSError as exc:
        return EXIT_CANNOT_DETERMINE, f"cannot check samples git HEAD: {exc}"

    if completed.returncode != 0:
        reason = (completed.stderr or completed.stdout).strip()
        return EXIT_CANNOT_DETERMINE, f"cannot resolve samples HEAD: {reason}"
    return EXIT_SUCCESS, f"samples checkout exists at {completed.stdout.strip()}"


def build_wiki_fetch_args(args: argparse.Namespace) -> list[str]:
    fetch_args: list[str] = []
    if args.wiki_manual_first:
        fetch_args.append("--manual-first")
    if args.wiki_no_manual_security:
        fetch_args.append("--no-manual-security")
    if args.wiki_keep_browser_open:
        fetch_args.append("--keep-browser-open")
    if args.wiki_browser_mode:
        fetch_args.extend(["--browser-mode", args.wiki_browser_mode])
    if args.wiki_max_pages is not None:
        fetch_args.extend(["--max-pages", str(args.wiki_max_pages)])
    return fetch_args


def build_stages(args: argparse.Namespace) -> list[Stage]:
    scopes = selected_scopes(args)
    stages: list[Stage] = []

    if scopes["game_data"]:
        if args.check:
            stages.append(Stage("game-data status", py_script("scripts/update-reforger-data.py", "--check")))
            stages.append(Stage("game-data index status", py_script("scripts/index-reforger-data.py", "--check")))
        elif args.force:
            stages.append(Stage("game-data refresh", py_script("scripts/update-reforger-data.py", "--force")))
            stages.append(Stage("game-data index", py_script("scripts/index-reforger-data.py")))
        else:
            stages.append(Stage("game-data refresh", py_script("scripts/update-reforger-data.py", "--if-needed")))
            stages.append(Stage("game-data index", py_script("scripts/index-reforger-data.py", "--if-needed")))

    if scopes["samples"]:
        if args.check:
            stages.append(Stage("samples status", check=check_samples))
        else:
            stages.append(Stage("samples refresh", powershell_script("scripts/update-reforger-samples.ps1")))

    if scopes["wiki"]:
        if args.check:
            stages.append(
                Stage(
                    "wiki cache status",
                    check=lambda: check_path_exists(ROOT / "raw" / "wiki-docs" / "manifest.json", "wiki cache manifest"),
                )
            )
            stages.append(
                Stage(
                    "wiki index status",
                    check=lambda: check_path_exists(
                        ROOT / "generation" / "wiki-index" / "manifest.json", "wiki index manifest"
                    ),
                )
            )
        else:
            if args.fetch_wiki:
                stages.append(
                    Stage(
                        "wiki fetch",
                        py_script("scripts/update-reforger-wiki-docs.py", *build_wiki_fetch_args(args)),
                    )
                )
            stages.append(Stage("wiki index", py_script("scripts/index-reforger-wiki-docs.py")))

    if scopes["validate"]:
        stages.append(Stage("search validation", py_script("scripts/tests/validate-reforger-search.py")))
        stages.append(Stage("search usefulness", py_script("scripts/tests/measure-reforger-search-usefulness.py")))

    return stages


def validate_args(args: argparse.Namespace) -> None:
    if args.force and args.check:
        raise ValueError("--force cannot be combined with --check")
    if args.force and args.if_needed:
        raise ValueError("--force cannot be combined with --if-needed")
    if args.no_validate and args.validate:
        raise ValueError("--no-validate cannot be combined with --validate")
    if args.fetch_wiki and not (args.wiki or args.all or not has_scope(args)):
        raise ValueError("--fetch-wiki requires --wiki, --all, or default full refresh")


def run_stage(stage: Stage, *, dry_run: bool) -> StageResult:
    start = time.monotonic()

    if stage.check is not None:
        if dry_run:
            return StageResult(stage.name, "dry-run", EXIT_SUCCESS, 0.0, "<internal check>")
        exit_code, message = stage.check()
        status = "ok" if exit_code == EXIT_SUCCESS else "stale" if exit_code == EXIT_STALE else "cannot-determine"
        print(f"[refresh] {stage.name}: {message}", flush=True)
        return StageResult(stage.name, status, exit_code, time.monotonic() - start, "<internal check>")

    if stage.command is None:
        return StageResult(stage.name, "skipped", EXIT_SUCCESS, 0.0, "")

    print(f"[refresh] {stage.name}: {stage.command.display}", flush=True)
    if dry_run:
        return StageResult(stage.name, "dry-run", EXIT_SUCCESS, 0.0, stage.command.display)

    completed = subprocess.run(stage.command.args, cwd=ROOT, check=False)
    elapsed = time.monotonic() - start
    if completed.returncode == EXIT_SUCCESS:
        status = "ok"
    elif completed.returncode == EXIT_STALE:
        status = "stale"
    elif completed.returncode == EXIT_CANNOT_DETERMINE:
        status = "cannot-determine"
    else:
        status = "failed"
    return StageResult(stage.name, status, completed.returncode, elapsed, stage.command.display)


def final_exit_code(results: list[StageResult], *, check_mode: bool) -> int:
    codes = [result.exit_code for result in results if result.exit_code != EXIT_SUCCESS]
    if not codes:
        return EXIT_SUCCESS
    if any(code not in (EXIT_STALE, EXIT_CANNOT_DETERMINE) for code in codes):
        return EXIT_FAILURE
    if any(code == EXIT_CANNOT_DETERMINE for code in codes):
        return EXIT_CANNOT_DETERMINE
    if check_mode and any(code == EXIT_STALE for code in codes):
        return EXIT_STALE
    return EXIT_FAILURE


def print_summary(results: list[StageResult]) -> None:
    print()
    print("[refresh] summary")
    if not results:
        print("[refresh] no stages selected")
        return
    for result in results:
        print(
            f"[refresh] {result.name}: {result.status} "
            f"(exit {result.exit_code}, {result.elapsed:.1f}s)"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Refresh and index Reforger source data.")

    scope = parser.add_argument_group("scope")
    scope.add_argument("--all", action="store_true", help="Run safe full refresh")
    scope.add_argument("--game-data", action="store_true", help="Refresh game data and game-data indexes")
    scope.add_argument("--wiki", action="store_true", help="Index cached wiki data")
    scope.add_argument("--fetch-wiki", action="store_true", help="Fetch live wiki data before wiki indexing")
    scope.add_argument("--samples", action="store_true", help="Refresh official samples")
    scope.add_argument("--validate", action="store_true", help="Run search validation and usefulness checks")
    scope.add_argument("--no-validate", action="store_true", help="Skip validation in default or --all runs")

    execution = parser.add_argument_group("execution")
    execution.add_argument("--if-needed", action="store_true", help="Use freshness checks where supported")
    execution.add_argument("--force", action="store_true", help="Force game-data refresh and index rebuild")
    execution.add_argument("--check", action="store_true", help="Check status without refreshing data where supported")
    execution.add_argument("--dry-run", action="store_true", help="Print planned commands without running them")
    execution.add_argument("--keep-going", action="store_true", help="Continue after failed stages")

    wiki = parser.add_argument_group("wiki scraper pass-through")
    wiki.add_argument("--wiki-manual-first", action="store_true", help="Pass --manual-first to wiki scraper")
    wiki.add_argument(
        "--wiki-no-manual-security",
        action="store_true",
        help="Pass --no-manual-security to wiki scraper",
    )
    wiki.add_argument("--wiki-keep-browser-open", action="store_true", help="Pass --keep-browser-open to wiki scraper")
    wiki.add_argument("--wiki-browser-mode", choices=("attach", "webdriver"), help="Wiki scraper browser mode")
    wiki.add_argument("--wiki-max-pages", type=int, help="Pass --max-pages to wiki scraper")

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    validate_args(args)
    stages = build_stages(args)

    results: list[StageResult] = []
    for stage in stages:
        result = run_stage(stage, dry_run=args.dry_run)
        results.append(result)
        if result.exit_code != EXIT_SUCCESS and not args.keep_going:
            if args.check and result.exit_code == EXIT_STALE:
                continue
            break

    print_summary(results)
    return final_exit_code(results, check_mode=args.check)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(f"[refresh] ERROR: {exc}", file=sys.stderr)
        raise SystemExit(EXIT_FAILURE)
