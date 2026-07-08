#!/usr/bin/env python3
"""Validate Reforger game-data search quality with high-value Codex lookup cases."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
QUERY_SCRIPT = ROOT / "scripts" / "query-reforger-data.py"
DEFAULT_HUMAN_LOG_DIR = ROOT / "generation" / "search-exports"


class Failure(Exception):
    pass


def run_query(args: list[str], human_log: bool, human_log_dir: Path | None, expect_success: bool = True) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, str(QUERY_SCRIPT), *args]
    if human_log and expect_success:
        command.append("--human-log")
        if human_log_dir:
            command.extend(["--human-log-dir", str(human_log_dir)])
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if expect_success and result.returncode != 0:
        raise Failure(f"query failed: {' '.join(args)}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}")
    if not expect_success and result.returncode == 0:
        raise Failure(f"query unexpectedly succeeded: {' '.join(args)}\nSTDOUT:\n{result.stdout}")
    return result


def run_json(args: list[str], human_log: bool, human_log_dir: Path | None) -> dict[str, Any]:
    result = run_query([*args, "--json"], human_log, human_log_dir)
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise Failure(f"invalid JSON for {' '.join(args)}: {exc}\n{result.stdout}") from exc
    if not isinstance(payload, dict) or not isinstance(payload.get("records"), list):
        raise Failure(f"unexpected JSON shape for {' '.join(args)}")
    return payload


def first_record(payload: dict[str, Any], label: str) -> dict[str, Any]:
    records = payload.get("records") or []
    if not records:
        raise Failure(f"no records returned for {label}")
    if not isinstance(records[0], dict):
        raise Failure(f"first record is not an object for {label}")
    return records[0]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Failure(message)


def validate_symbol(human_log: bool, human_log_dir: Path | None) -> None:
    payload = run_json(["symbol", "ResourceName", "--exact"], human_log, human_log_dir)
    record = first_record(payload, "symbol ResourceName")
    require(record.get("name") == "ResourceName", "ResourceName exact lookup did not return ResourceName first")
    require(bool(record.get("generated")), "ResourceName exact lookup should prefer generated API truth")
    require(bool(record.get("file")) and bool(record.get("line")), "ResourceName record lacks source reference")

    payload = run_json(["symbol", "ScriptComponent", "--kind", "class", "--exact"], human_log, human_log_dir)
    record = first_record(payload, "symbol ScriptComponent")
    require(record.get("name") == "ScriptComponent" and record.get("kind") == "class", "ScriptComponent class lookup failed")


def validate_method_and_attributes(human_log: bool, human_log_dir: Path | None) -> None:
    payload = run_json(["method", "IEntity", "FindComponent", "--exact"], human_log, human_log_dir)
    record = first_record(payload, "method IEntity FindComponent")
    require(record.get("owner") == "IEntity" and record.get("name") == "FindComponent", "IEntity.FindComponent was not the first exact method match")
    require("FindComponent" in str(record.get("signature") or ""), "IEntity.FindComponent record lacks signature")

    for attribute in ("RplProp", "RplRpc"):
        payload = run_json(["attribute", attribute, "--exact"], human_log, human_log_dir)
        records = payload.get("records") or []
        require(any(item.get("name") == attribute for item in records), f"{attribute} attribute class not returned")
        require(all(item.get("file") and item.get("line") for item in records), f"{attribute} records lack source references")


def validate_inheritance(human_log: bool, human_log_dir: Path | None) -> None:
    payload = run_json(["inherits", "ScriptedUserAction"], human_log, human_log_dir)
    records = payload.get("records") or []
    require(any(item.get("extends") == "ScriptedUserAction" for item in records), "ScriptedUserAction derived classes were not found")
    require(all(item.get("file") and item.get("line") for item in records[:5]), "inheritance records lack source references")


def validate_examples_and_files(human_log: bool, human_log_dir: Path | None) -> None:
    examples = {
        "replication": lambda item: item.get("file") == "scripts/GameLib/replication/RplDocs.c",
        "user-action": lambda item: "ScriptedUserAction" in (item.get("baseClasses") or []) or "scripted-user-action" in (item.get("subtopics") or []),
        "resource-loading": lambda item: bool({"resource-load", "spawn-prefab", "resource-picker-config"} & set(item.get("subtopics") or [])),
        "workbench-plugin": lambda item: "WorkbenchPlugin" in (item.get("baseClasses") or []) or "workbench-plugin" in (item.get("subtopics") or []),
    }
    for topic, predicate in examples.items():
        payload = run_json(["examples", topic], human_log, human_log_dir)
        records = payload.get("records") or []
        require(records, f"examples {topic} returned no records")
        require(any(predicate(item) for item in records[:8]), f"examples {topic} did not return expected anchors near the top")
        require(all(item.get("file") and item.get("suggestedLines") for item in records[:5]), f"examples {topic} records lack source ranges")

    payload = run_json(["examples", "resource-loading", "--subtopic", "spawn-prefab"], human_log, human_log_dir)
    records = payload.get("records") or []
    require(records and all("spawn-prefab" in (item.get("subtopics") or []) for item in records), "spawn-prefab subtopic filter failed")

    payload = run_json(["examples", "replication", "--with-snippets", "--limit", "2"], human_log, human_log_dir)
    records = payload.get("records") or []
    require(records and any(item.get("snippet") for item in records), "--with-snippets did not attach a bounded snippet")

    payload = run_json(["files", "WorkbenchPlugin"], human_log, human_log_dir)
    records = payload.get("records") or []
    require(records, "files WorkbenchPlugin returned no records")
    require(any("WorkbenchPlugin" in " ".join(item.get("declaredSymbols") or item.get("baseClasses") or []) or "workbench-plugin" in (item.get("subtopics") or []) for item in records[:10]), "files WorkbenchPlugin lacks expected Workbench anchors")

    subtopic_cases = [
        ("weapon", "magazine"),
        ("vehicle", "compartment"),
        ("inventory", "character-inventory"),
        ("ui", "hud"),
        ("audio", "sound-event"),
        ("animation", "anim-graph"),
    ]
    for topic, subtopic in subtopic_cases:
        payload = run_json(["examples", topic, "--subtopic", subtopic, "--limit", "8"], human_log, human_log_dir)
        records = payload.get("records") or []
        require(records, f"examples {topic} --subtopic {subtopic} returned no records")
        require(any(subtopic in (item.get("subtopics") or []) for item in records[:5]), f"examples {topic} did not rank {subtopic} records near the top")


def validate_snippet_and_lookup(human_log: bool, human_log_dir: Path | None) -> None:
    payload = run_json(["snippet", "scripts/GameLib/replication/RplDocs.c", "--line", "1", "--context", "20"], human_log, human_log_dir)
    record = first_record(payload, "snippet RplDocs")
    require(record.get("file") == "scripts/GameLib/replication/RplDocs.c", "snippet returned the wrong file")
    require(1 <= len(record.get("excerpt") or []) <= 100, "snippet is not bounded")

    run_query(["snippet", "..\\README.md", "--line", "1", "--context", "20"], human_log, human_log_dir, expect_success=False)

    payload = run_json(["lookup", "replicated component"], human_log, human_log_dir)
    record = first_record(payload, "lookup replicated component")
    require(record.get("matchedTask") == "replicated-component", "lookup did not classify replicated component task")
    require(record.get("apiSymbols") and record.get("examples"), "lookup did not return API symbols and examples")

    expected_tasks = {
        "make a user action": "user-action",
        "create weapon script": "weapon",
        "vehicle compartment": "vehicle",
        "use CharacterInventory": "inventory",
        "create HUD widget": "ui",
        "play a sound event": "audio",
        "find animation graph examples": "animation",
    }
    for query, expected in expected_tasks.items():
        payload = run_json(["lookup", query], human_log, human_log_dir)
        record = first_record(payload, f"lookup {query}")
        require(record.get("matchedTask") == expected, f"lookup {query!r} returned {record.get('matchedTask')!r}, expected {expected!r}")
        require(record.get("apiSymbols") or record.get("methods"), f"lookup {query!r} did not return API anchors")
        require(record.get("examples"), f"lookup {query!r} did not return examples")

    payload = run_json(["lookup", "unknown made-up task"], human_log, human_log_dir)
    record = first_record(payload, "lookup unknown made-up task")
    require(record.get("matchedTask") is None, "unknown lookup should return explicit unmatched state")
    require(record.get("suggestedSearches"), "unknown lookup should return suggested searches")
    require(not record.get("apiSymbols") and not record.get("examples"), "unknown lookup should not return unrelated API/examples")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Reforger search quality against known Codex lookup anchors.")
    parser.add_argument("--human-log", action="store_true", help="Write human-only query logs for each successful validation query")
    parser.add_argument("--human-log-dir", type=Path, default=DEFAULT_HUMAN_LOG_DIR, help="Human log output directory")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    checks = [
        ("symbols", validate_symbol),
        ("methods and attributes", validate_method_and_attributes),
        ("inheritance", validate_inheritance),
        ("examples and files", validate_examples_and_files),
        ("snippets and lookup", validate_snippet_and_lookup),
    ]
    for name, check in checks:
        check(args.human_log, args.human_log_dir if args.human_log else None)
        print(f"[reforger-validate] ok: {name}")
    print("[reforger-validate] search quality checks passed")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Failure as exc:
        print(f"[reforger-validate] FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
    except Exception as exc:
        print(f"[reforger-validate] ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
