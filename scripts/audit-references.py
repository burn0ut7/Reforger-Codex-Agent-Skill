#!/usr/bin/env python3
"""Audit generated Arma Reforger skill references against generation/design.md.

This script is a stable gate, not a reference generator. It reads files, reports
failures, and exits nonzero when the generated skill is design-incomplete.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references"
SKILL = ROOT / "SKILL.md"

REQUIRED_REFERENCES = [
    "overview.md",
    "scripting-core.md",
    "scripting-language.md",
    "entity-component-lifecycle.md",
    "networking-multiplayer-replication.md",
    "resources-prefabs-configs.md",
    "workbench-tools-debugging.md",
    "scenario-framework-game-master.md",
    "terrain-world-editor.md",
    "assets-weapons-vehicles-animation-audio.md",
    "server-runtime-packaging.md",
    "examples-patterns.md",
    "common-task-recipes.md",
    "api-main.md",
    "api-extended.md",
]

CENTRAL_REFERENCES = {"common-task-recipes.md", "examples-patterns.md", "api-main.md"}
EXEMPT_LINE_TARGETS = {"api-extended.md"}

REQUIRED_RECIPES = [
    "Create A ScriptComponent",
    "Add Editor Props And Attribute Fields",
    "Print Debug Info",
    "Get Entity Origin Or Transform",
    "Move Or Teleport An Entity",
    "Get Local Player Or Controlled Entity",
    "Register Frame Or Update Events Safely",
    "Add Or Modify A User Action",
    "Spawn An Entity Or Prefab",
    "Load A Resource Or Prefab",
    "Basic Replicated Or RPC Action",
    "Create A Workbench Plugin Command",
]

REQUIRED_SAMPLE_MODS = [
    "SampleMod_AnimationWorkshop",
    "SampleMod_CinematicTutorial",
    "SampleMod_Main",
    "SampleMod_ModdedCar",
    "SampleMod_ModdedScript",
    "SampleMod_ModdedWeapon",
    "SampleMod_NewCar",
    "SampleMod_NewCharacter",
    "SampleMod_NewFaction",
    "SampleMod_NewProp",
    "SampleMod_NewWeapon",
    "SampleMod_Replacement",
    "SampleMod_WorkbenchPlugin",
]

API_MAIN_TERMS = [
    "IEntity",
    "GetOrigin",
    "SetOrigin",
    "GetTransform",
    "SetTransform",
    "SetWorldTransform",
    "GetYawPitchRoll",
    "SetYawPitchRoll",
    "ScriptComponent",
    "ScriptComponentClass",
    "GenericEntity",
    "GenericEntityClass",
    "GenericComponent",
    "GenericComponentClass",
    "Game",
    "Resource",
    "ResourceName",
    "BaseRplComponent",
    "RplRpc",
    "RplProp",
    "OnRpl",
    "ActionManager",
    "InputManager",
    "WorkbenchPlugin",
    "ScriptEditor",
    "WorldEditor",
    "ResourceManager",
    "Widget",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def nonblank_lines(text: str) -> int:
    return sum(1 for line in text.splitlines() if line.strip())


def line_target(name: str) -> int:
    if name in EXEMPT_LINE_TARGETS:
        return 0
    if name == "overview.md":
        return 80
    if name in CENTRAL_REFERENCES:
        return 200
    return 250


def has_intentionally_short(text: str) -> bool:
    return "INTENTIONALLY SHORT" in text and "sparse" in text.lower()


def section_body(text: str, heading: str) -> str:
    pattern = re.compile(rf"^##\s+{re.escape(heading)}\s*$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        return ""
    rest = text[match.end() :]
    next_heading = re.search(r"^##\s+", rest, re.MULTILINE)
    if next_heading:
        rest = rest[: next_heading.start()]
    return rest


def source_lines(text: str) -> list[str]:
    body = section_body(text, "Sources Used")
    return [line.strip() for line in body.splitlines() if line.strip().startswith("-")]


def check_exact_sources(text: str) -> tuple[bool, list[str]]:
    lines = source_lines(text)
    problems: list[str] = []
    if not lines:
        return False, ["missing Sources Used entries"]

    exact_count = 0
    for line in lines:
        paths = re.findall(r"`([^`]+)`", line)
        if not paths:
            problems.append(f"source entry lacks backticked path: {line}")
            continue
        for raw_path in paths:
            normalized = raw_path.replace("\\", "/")
            if "*" in normalized or "?" in normalized or "[" in normalized or "]" in normalized:
                problems.append(f"broad/glob source path: {raw_path}")
                continue
            if not normalized.startswith(("raw/wiki-docs/", "raw/samples/", "raw/game-data/")):
                problems.append(f"not a raw source path: {raw_path}")
                continue
            if not (ROOT / normalized).exists():
                problems.append(f"source path does not exist: {raw_path}")
                continue
            exact_count += 1

    return exact_count > 0 and not problems, problems


def has_example(text: str) -> bool:
    markers = [
        "official-doc-example",
        "official-sample-excerpt",
        "generated-pattern-from-docs",
        "example-observed",
        "pseudocode",
        "No direct example included because",
        "no-example rationale",
    ]
    return any(marker in text for marker in markers)


def has_traps_or_checklist(text: str) -> bool:
    return "## Common Traps" in text or "## Review Checklist" in text


def has_api_notes(name: str, text: str) -> bool:
    if name in {"overview.md", "api-extended.md"}:
        return True
    return "## API Notes" in text or name == "api-main.md"


def audit_skill_links(rows: list[dict[str, object]]) -> None:
    if not SKILL.exists():
        rows.append({"name": "SKILL.md", "status": "FAIL", "problems": ["missing SKILL.md"]})
        return
    text = read_text(SKILL)
    refs = sorted(set(re.findall(r"references/[A-Za-z0-9_.-]+\.md", text)))
    problems = [ref for ref in refs if not (ROOT / ref).exists()]
    rows.append(
        {
            "name": "SKILL.md",
            "status": "PASS" if not problems else "FAIL",
            "problems": [f"missing linked reference: {ref}" for ref in problems],
        }
    )


def audit_reference(name: str) -> dict[str, object]:
    path = REFERENCES / name
    problems: list[str] = []
    if not path.exists():
        return {"name": name, "status": "FAIL", "lines": 0, "problems": ["missing file"]}

    text = read_text(path)
    lines = nonblank_lines(text)
    target = line_target(name)
    if target and lines < target and not has_intentionally_short(text):
        problems.append(f"nonblank line target not met: {lines} < {target}")

    if name != "api-extended.md":
        exact_sources, source_problems = check_exact_sources(text)
        if not exact_sources:
            problems.append("exact Sources Used check failed")
        problems.extend(source_problems[:10])

        if not has_example(text):
            problems.append("missing direct example marker or no-example rationale")
        if not has_traps_or_checklist(text):
            problems.append("missing Common Traps or Review Checklist")
        if not has_api_notes(name, text):
            problems.append("missing API Notes")

    if name == "common-task-recipes.md":
        for recipe in REQUIRED_RECIPES:
            if recipe not in text:
                problems.append(f"missing recipe: {recipe}")

    if name == "examples-patterns.md":
        for sample in REQUIRED_SAMPLE_MODS:
            if sample not in text:
                problems.append(f"missing sample inventory entry: {sample}")

    if name == "api-main.md":
        for term in API_MAIN_TERMS:
            if term not in text:
                problems.append(f"missing API term: {term}")
        if "Signature:" not in text and "signature:" not in text:
            problems.append("api-main lacks explicit signature entries")
        if "raw/game-data/" not in text:
            problems.append("api-main lacks raw game-data source paths near API entries")

    return {"name": name, "status": "PASS" if not problems else "FAIL", "lines": lines, "problems": problems}


def main() -> int:
    rows: list[dict[str, object]] = []
    for name in REQUIRED_REFERENCES:
        rows.append(audit_reference(name))
    audit_skill_links(rows)

    failed = [row for row in rows if row["status"] != "PASS"]

    print("| File | Status | Nonblank lines | Problems |")
    print("| --- | --- | ---: | --- |")
    for row in rows:
        problems = row.get("problems", [])
        problem_text = "<br>".join(str(problem) for problem in problems) if problems else ""
        print(f"| `{row['name']}` | {row['status']} | {row.get('lines', '')} | {problem_text} |")

    if failed:
        print(f"\nAudit failed: {len(failed)} file(s) need work.")
        return 1

    print("\nAudit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
