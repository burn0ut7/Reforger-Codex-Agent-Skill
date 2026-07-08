#!/usr/bin/env python3
"""Refresh raw Arma Reforger game scripts from Bohemia's script-diff repo.

This script only owns raw game-data freshness:
  - check the remote Git commit,
  - pull sparse scripts/ from BohemiaInteractive/Arma-Reforger-Script-Diff,
  - write raw/game-data/manifest.json,
  - delete raw/game-data/.git, README.md, and LICENSE.

Parsing, schema generation, and indexing belong in a separate indexer script.

Exit codes:
  0   success or --check reports up to date
  10  --check reports missing or outdated local game data
  2   --check cannot determine status
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPO_URL = "https://github.com/BohemiaInteractive/Arma-Reforger-Script-Diff.git"
DEFAULT_REF = "main"
EXIT_UP_TO_DATE = 0
EXIT_UPDATE_NEEDED = 10
EXIT_CANNOT_DETERMINE = 2
CHECKOUT_ARTIFACTS = [".git", "README.md", "LICENSE"]
PRESERVED_GENERATED_ARTIFACTS = ["api-schema.json", "api-index.md", "indexes"]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def log(message: str) -> None:
    print(f"[reforger] {message}", flush=True)


def run_git(args: list[str], cwd: Path | None = None, check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=str(cwd) if cwd else None,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if check and result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed:\n{result.stdout}")
    return result.stdout.strip()


def load_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def local_game_data_commit(game_data_root: Path) -> str | None:
    manifest = load_json(game_data_root / "manifest.json")
    if not manifest:
        return None

    source = manifest.get("source")
    if isinstance(source, dict):
        commit = source.get("commit")
        if isinstance(commit, str) and commit.strip():
            return commit.strip()

    build_id = manifest.get("buildId")
    if isinstance(build_id, str) and build_id.strip():
        return build_id.strip()
    return None


def ls_remote(repo_url: str, pattern: str) -> list[tuple[str, str]]:
    output = run_git(["ls-remote", repo_url, pattern])
    refs: list[tuple[str, str]] = []
    for line in output.splitlines():
        parts = line.split()
        if len(parts) >= 2:
            refs.append((parts[0], parts[1]))
    return refs


def remote_commit(repo_url: str, ref: str) -> tuple[str, str]:
    patterns = [ref]
    if not ref.startswith("refs/") and ref != "HEAD":
        patterns.extend([f"refs/heads/{ref}", f"refs/tags/{ref}"])

    seen: set[str] = set()
    matches: list[tuple[str, str]] = []
    for pattern in patterns:
        if pattern in seen:
            continue
        seen.add(pattern)
        matches.extend(ls_remote(repo_url, pattern))
        if matches:
            break

    if not matches:
        raise RuntimeError(f"Could not resolve remote ref {ref!r} from {repo_url}")

    def rank(match: tuple[str, str]) -> tuple[int, str]:
        _, name = match
        preferred = (
            name == ref
            or name == f"refs/heads/{ref}"
            or name == f"refs/tags/{ref}"
            or (ref == "HEAD" and name == "HEAD")
        )
        return (0 if preferred else 1, name)

    commit, resolved_ref = sorted(matches, key=rank)[0]
    return commit, resolved_ref


def check_game_data_status(game_data_root: Path, repo_url: str, ref: str) -> tuple[int, dict[str, Any]]:
    remote, resolved_ref = remote_commit(repo_url, ref)
    local = local_game_data_commit(game_data_root)
    scripts_exists = (game_data_root / "scripts").exists()

    status: dict[str, Any] = {
        "repo": repo_url,
        "requestedRef": ref,
        "resolvedRef": resolved_ref,
        "localCommit": local,
        "remoteCommit": remote,
        "scriptsExists": scripts_exists,
    }

    if not local or not scripts_exists:
        status["status"] = "missing-local-data"
        status["needsUpdate"] = True
        return EXIT_UPDATE_NEEDED, status

    if local != remote:
        status["status"] = "update-available"
        status["needsUpdate"] = True
        return EXIT_UPDATE_NEEDED, status

    status["status"] = "up-to-date"
    status["needsUpdate"] = False
    return EXIT_UP_TO_DATE, status


def print_status(status: dict[str, Any]) -> None:
    print(f"[reforger] status: {status['status']}")
    print(f"[reforger] repo: {status['repo']}")
    print(f"[reforger] ref: {status['requestedRef']} ({status['resolvedRef']})")
    print(f"[reforger] local commit: {status.get('localCommit') or 'none'}")
    print(f"[reforger] remote commit: {status['remoteCommit']}")
    print(f"[reforger] scripts present: {str(status['scriptsExists']).lower()}")


def remove_readonly(function: Any, path: str, _: Any) -> None:
    os.chmod(path, stat.S_IWRITE)
    function(path)


def remove_path(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path, onerror=remove_readonly)
    elif path.exists():
        path.chmod(stat.S_IWRITE)
        path.unlink()


def remove_legacy_source_cache(raw_root: Path) -> None:
    legacy = raw_root / "source-cache"
    if legacy.exists():
        log(f"Removing legacy source cache: {legacy}")
        shutil.rmtree(legacy, onerror=remove_readonly)


def remove_game_data_checkout_artifacts(game_data_root: Path) -> None:
    root = game_data_root.resolve()
    for name in CHECKOUT_ARTIFACTS:
        target = (game_data_root / name).resolve()
        if target.parent != root:
            raise RuntimeError(f"Refusing to delete outside raw/game-data: {target}")
        if target.exists():
            log(f"Deleting checkout artifact: {target}")
            remove_path(target)


@contextmanager
def preserve_generated_artifacts(game_data_root: Path) -> Iterable[None]:
    """Keep existing generated artifacts out of Git checkout cleanup.

    This updater does not create these files. They are preserved only so a raw
    refresh does not delete output from the future indexer.
    """

    with tempfile.TemporaryDirectory(prefix="reforger-generated-") as temp_dir:
        temp_root = Path(temp_dir)
        preserved: list[tuple[Path, Path]] = []
        for name in PRESERVED_GENERATED_ARTIFACTS:
            source = game_data_root / name
            if source.exists():
                target = temp_root / name
                shutil.move(str(source), str(target))
                preserved.append((source, target))

        try:
            yield
        finally:
            for source, target in preserved:
                if not target.exists():
                    continue
                if source.exists():
                    remove_path(source)
                shutil.move(str(target), str(source))


def materialize_sparse_scripts(game_data_root: Path, repo_url: str, ref: str) -> str:
    if shutil.which("git") is None:
        raise RuntimeError("git is required to refresh Reforger script data")

    game_data_root.mkdir(parents=True, exist_ok=True)
    with preserve_generated_artifacts(game_data_root):
        for name in ["scripts", *CHECKOUT_ARTIFACTS]:
            stale = game_data_root / name
            if stale.exists():
                log(f"Removing previous game data artifact: {stale}")
                remove_path(stale)

        run_git(["init"], cwd=game_data_root)
        run_git(["remote", "add", "origin", repo_url], cwd=game_data_root)
        run_git(["sparse-checkout", "init", "--cone"], cwd=game_data_root)
        run_git(["sparse-checkout", "set", "scripts"], cwd=game_data_root)
        run_git(["fetch", "--depth", "1", "origin", ref], cwd=game_data_root)
        run_git(["checkout", "--detach", "FETCH_HEAD"], cwd=game_data_root)
        commit = run_git(["rev-parse", "HEAD"], cwd=game_data_root)

        if not (game_data_root / "scripts").exists():
            raise RuntimeError(f"Upstream checkout does not contain scripts/: {game_data_root / 'scripts'}")

        remove_game_data_checkout_artifacts(game_data_root)
        return commit


def build_manifest(repo_url: str, ref: str, commit: str, game_data_root: Path) -> dict[str, Any]:
    return {
        "generatedAt": utc_now(),
        "gamePath": repo_url,
        "gameVersion": commit[:12],
        "buildId": commit,
        "appManifest": None,
        "source": {
            "kind": "git",
            "repo": repo_url,
            "ref": ref,
            "commit": commit,
            "sparsePath": "scripts",
            "scriptsPath": str(game_data_root / "scripts"),
            "checkoutArtifactsRemoved": CHECKOUT_ARTIFACTS,
        },
    }


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Refresh raw Arma Reforger scripts from git.")
    parser.add_argument("--skill-root", type=Path, default=ROOT, help="Skill repository root")
    parser.add_argument("--repo-url", default=DEFAULT_REPO_URL, help="Script diff git repository URL")
    parser.add_argument("--ref", default=DEFAULT_REF, help="Git branch, tag, or ref to fetch")
    parser.add_argument("--check", action="store_true", help="Check remote status without fetching or writing files")
    parser.add_argument("--if-needed", action="store_true", help="Skip refresh when local game data already matches the remote ref")
    parser.add_argument("--force", action="store_true", help="Delete raw/game-data before refreshing scripts")
    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> None:
    if args.check and args.if_needed:
        raise RuntimeError("--check and --if-needed cannot be used together")
    if args.check and args.force:
        raise RuntimeError("--check cannot be combined with --force")
    if args.if_needed and args.force:
        raise RuntimeError("--if-needed cannot be combined with --force")


def main() -> int:
    args = parse_args()
    validate_args(args)

    skill_root = args.skill_root.resolve()
    raw_root = skill_root / "raw"
    game_data_root = raw_root / "game-data"

    if args.check:
        try:
            exit_code, status = check_game_data_status(game_data_root, args.repo_url, args.ref)
        except Exception as exc:
            print("[reforger] status: cannot-determine", file=sys.stderr)
            print(f"[reforger] reason: {exc}", file=sys.stderr)
            return EXIT_CANNOT_DETERMINE
        print_status(status)
        return exit_code

    if args.if_needed:
        try:
            exit_code, status = check_game_data_status(game_data_root, args.repo_url, args.ref)
        except Exception as exc:
            print("[reforger] status: cannot-determine")
            print(f"[reforger] reason: {exc}")
            print("[reforger] continuing with refresh")
        else:
            print_status(status)
            if exit_code == EXIT_UP_TO_DATE:
                log("Game data is current; skipping refresh")
                return EXIT_UP_TO_DATE

    if args.force and game_data_root.exists():
        log(f"Deleting existing game data: {game_data_root}")
        shutil.rmtree(game_data_root, onerror=remove_readonly)

    raw_root.mkdir(parents=True, exist_ok=True)
    remove_legacy_source_cache(raw_root)
    commit = materialize_sparse_scripts(game_data_root, args.repo_url, args.ref)
    manifest = build_manifest(args.repo_url, args.ref, commit, game_data_root)
    write_json(game_data_root / "manifest.json", manifest)
    log(f"Source commit: {commit}")
    log(f"Wrote manifest: {game_data_root / 'manifest.json'}")
    return EXIT_UP_TO_DATE


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"[reforger] ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
