#!/usr/bin/env python3
"""Measure Reforger search usefulness with a curated task benchmark."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
QUERY_SCRIPT = ROOT / "scripts" / "query-reforger-data.py"
DEFAULT_REPORT_DIR = ROOT / "generation" / "search-exports"
METRICS = [
    "api_precision",
    "example_relevance",
    "source_grounding",
    "context_efficiency",
    "routing_safety",
    "snippet_usefulness",
    "verification_guidance",
]

BENCHMARKS = [
    {
        "query": "make a user action",
        "matchedTask": "user-action",
        "api": ["ScriptedUserAction", "PerformAction"],
        "subtopics": ["scripted-user-action", "perform-action"],
    },
    {
        "query": "make a replicated component",
        "matchedTask": "replicated-component",
        "api": ["RplComponent", "RplProp", "RplRpc", "ScriptComponent"],
        "subtopics": ["rpl-component", "rpl-prop", "rpc"],
    },
    {
        "query": "spawn a prefab",
        "matchedTask": "spawn-prefab",
        "api": ["SpawnEntityPrefab", "Resource.Load", "EntitySpawnParams"],
        "subtopics": ["spawn-prefab", "resource-load"],
    },
    {
        "query": "load a resource",
        "matchedTask": "load-resource",
        "api": ["Resource", "ResourceName", "Load"],
        "subtopics": ["resource-load"],
    },
    {
        "query": "make a Workbench plugin",
        "matchedTask": "workbench-plugin",
        "api": ["WorkbenchPlugin", "WorkbenchPluginAttribute"],
        "subtopics": ["workbench-plugin", "editor-ui"],
    },
    {
        "query": "create weapon script",
        "matchedTask": "weapon",
        "api": ["WeaponComponent", "BaseWeaponComponent"],
        "subtopics": ["weapon-component", "magazine", "muzzle"],
    },
    {
        "query": "add magazine or ammo behavior",
        "matchedTask": "weapon",
        "api": ["MagazineComponent"],
        "subtopics": ["magazine"],
    },
    {
        "query": "find vehicle compartment example",
        "matchedTask": "vehicle",
        "api": ["BaseCompartmentManagerComponent"],
        "subtopics": ["compartment"],
    },
    {
        "query": "use CharacterInventory",
        "matchedTask": "inventory",
        "api": ["InventoryStorageManagerComponent"],
        "subtopics": ["character-inventory", "storage"],
    },
    {
        "query": "create HUD widget",
        "matchedTask": "ui",
        "api": ["Widget", "WorkspaceWidget"],
        "subtopics": ["hud", "widget"],
    },
    {
        "query": "play a sound event",
        "matchedTask": "audio",
        "api": ["SoundComponent", "AudioSystem"],
        "subtopics": ["sound-event", "sound-component"],
    },
    {
        "query": "find animation graph examples",
        "matchedTask": "animation",
        "api": ["CharacterAnimationComponent", "BaseAnimPhysComponent"],
        "subtopics": ["anim-graph", "character-animation"],
    },
    {
        "query": "unknown made-up task",
        "matchedTask": None,
        "api": [],
        "subtopics": [],
    },
]


class Failure(Exception):
    pass


def run_lookup(query: str) -> dict[str, Any]:
    command = [sys.executable, str(QUERY_SCRIPT), "lookup", query, "--json"]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode != 0:
        raise Failure(f"lookup failed for {query!r}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}")
    payload = json.loads(result.stdout)
    records = payload.get("records") or []
    if not records or not isinstance(records[0], dict):
        raise Failure(f"lookup returned no record for {query!r}")
    return records[0]


def flatten_record_text(value: Any) -> str:
    if isinstance(value, dict):
        return " ".join(flatten_record_text(item) for item in value.values())
    if isinstance(value, list):
        return " ".join(flatten_record_text(item) for item in value)
    if value is None:
        return ""
    return str(value)


def has_source_refs(records: list[dict[str, Any]]) -> bool:
    for record in records:
        if not record.get("file"):
            return False
        if not (record.get("line") or record.get("suggestedLines")):
            return False
    return bool(records)


def score_case(case: dict[str, Any], record: dict[str, Any]) -> dict[str, Any]:
    expected_task = case["matchedTask"]
    matched_task = record.get("matchedTask")
    is_unknown = expected_task is None
    api_records = list(record.get("apiSymbols") or []) + list(record.get("methods") or [])
    examples = list(record.get("examples") or [])
    record_text = flatten_record_text(api_records)
    example_subtopics = {subtopic for item in examples for subtopic in (item.get("subtopics") or [])}
    snippets = list(record.get("suggestedSnippetCommands") or [])
    suggested_searches = list(record.get("suggestedSearches") or [])

    scores: dict[str, int] = {}
    notes: list[str] = []

    if is_unknown:
        scores["routing_safety"] = 2 if matched_task is None and suggested_searches and not api_records and not examples else 0
        scores["api_precision"] = 2 if not api_records else 0
        scores["example_relevance"] = 2 if not examples else 0
        scores["source_grounding"] = 2 if suggested_searches else 1
        scores["context_efficiency"] = 2 if len(suggested_searches) <= 4 else 1
        scores["snippet_usefulness"] = 2 if not snippets else 0
        scores["verification_guidance"] = 2 if "No task rule matched" in str(record.get("verification") or "") else 1
    else:
        scores["routing_safety"] = 2 if matched_task == expected_task else 0
        required_api = case.get("api") or []
        api_hits = sum(1 for token in required_api if token in record_text)
        scores["api_precision"] = 2 if required_api and api_hits == len(required_api) else (1 if api_hits else 0)
        expected_subtopics = set(case.get("subtopics") or [])
        subtopic_hits = expected_subtopics & example_subtopics
        scores["example_relevance"] = 2 if examples and subtopic_hits else (1 if examples else 0)
        scores["source_grounding"] = 2 if has_source_refs(api_records[:5]) and has_source_refs(examples[:3]) else (1 if examples or api_records else 0)
        bounded = len(api_records) <= 20 and len(examples) <= 8 and len(snippets) <= 5
        scores["context_efficiency"] = 2 if bounded else 1
        scores["snippet_usefulness"] = 2 if snippets and examples else (1 if examples else 0)
        verification = str(record.get("verification") or "")
        scores["verification_guidance"] = 2 if any(term in verification.lower() for term in ["verify", "workbench", "runtime", "server"]) else 0

    if scores["routing_safety"] == 0:
        notes.append(f"routing expected {expected_task!r}, got {matched_task!r}")
    if scores["api_precision"] == 0 and not is_unknown:
        notes.append("missing required API anchors")
    if scores["example_relevance"] == 0 and not is_unknown:
        notes.append("missing relevant example subtopics")

    total = sum(scores[metric] for metric in METRICS)
    useful = total >= 10 and scores["api_precision"] > 0 and scores["routing_safety"] > 0
    return {
        "query": case["query"],
        "expectedTask": expected_task,
        "matchedTask": matched_task,
        "scores": scores,
        "total": total,
        "useful": useful,
        "notes": notes,
        "apiAnchors": [item.get("qualifiedName") or item.get("name") for item in api_records[:8]],
        "exampleFiles": [item.get("file") for item in examples[:5]],
        "exampleSubtopics": sorted(example_subtopics),
        "suggestedSearches": suggested_searches,
        "suggestedSnippetCommands": snippets,
    }


def write_markdown(report: dict[str, Any], path: Path) -> None:
    lines = [
        "# Reforger Search Usefulness Report",
        "",
        "Human review artifact only. This report is not source truth and must not be used by Codex as API documentation.",
        "",
        f"- Generated at: `{report['generatedAt']}`",
        f"- Average score: `{report['averageScore']:.2f}/14`",
        f"- Useful cases: `{report['usefulCases']}/{report['totalCases']}`",
        f"- Passed acceptance: `{str(report['passed']).lower()}`",
        "",
        "## Cases",
        "",
    ]
    for case in report["cases"]:
        lines.extend(
            [
                f"### {case['query']}",
                "",
                f"- Expected task: `{case['expectedTask']}`",
                f"- Matched task: `{case['matchedTask']}`",
                f"- Score: `{case['total']}/14`",
                f"- Useful: `{str(case['useful']).lower()}`",
                f"- Scores: `{json.dumps(case['scores'], sort_keys=True)}`",
                f"- API anchors: `{', '.join(item for item in case['apiAnchors'] if item)}`",
                f"- Example subtopics: `{', '.join(case['exampleSubtopics'])}`",
                f"- Example files: `{', '.join(item for item in case['exampleFiles'] if item)}`",
            ]
        )
        if case["notes"]:
            lines.append(f"- Notes: `{'; '.join(case['notes'])}`")
        if case["suggestedSearches"]:
            lines.append(f"- Suggested searches: `{'; '.join(case['suggestedSearches'])}`")
        lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Measure Reforger search usefulness across realistic Codex tasks.")
    parser.add_argument("--report-dir", type=Path, default=DEFAULT_REPORT_DIR, help="Directory for human-review report artifacts")
    parser.add_argument("--json-out", type=Path, default=None, help="Optional JSON report path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cases = [score_case(case, run_lookup(case["query"])) for case in BENCHMARKS]
    average = sum(case["total"] for case in cases) / len(cases)
    useful_cases = sum(1 for case in cases if case["useful"])
    passed = average >= 10 and all(case["useful"] for case in cases)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report = {
        "generatedAt": stamp,
        "averageScore": average,
        "usefulCases": useful_cases,
        "totalCases": len(cases),
        "passed": passed,
        "cases": cases,
    }

    args.report_dir.mkdir(parents=True, exist_ok=True)
    markdown_path = args.report_dir / f"{stamp}-search-usefulness.md"
    write_markdown(report, markdown_path)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    print(f"[reforger-usefulness] average: {average:.2f}/14")
    print(f"[reforger-usefulness] useful cases: {useful_cases}/{len(cases)}")
    print(f"[reforger-usefulness] report: {markdown_path}")
    if not passed:
        for case in cases:
            if not case["useful"]:
                print(f"[reforger-usefulness] not useful: {case['query']} ({case['total']}/14) {'; '.join(case['notes'])}")
        return 1
    print("[reforger-usefulness] usefulness benchmark passed")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"[reforger-usefulness] ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
