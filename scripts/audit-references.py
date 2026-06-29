#!/usr/bin/env python3
"""Audit generated Arma Reforger skill references against generation/design.md.

This is a gate, not a generator. It verifies structure, markdown hygiene,
required recipes/samples/API terms, design concept coverage, and review-table
line counts. A passing quick_validate.py is not enough for this skill.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references"
SKILL = ROOT / "SKILL.md"
DESIGN = ROOT / "generation" / "design.md"
REVIEW = ROOT / "generation" / "review.md"


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

TARGET_RANGES = {
    "overview.md": (120, 300),
    "scripting-core.md": (500, 1000),
    "scripting-language.md": (450, 900),
    "entity-component-lifecycle.md": (500, 900),
    "networking-multiplayer-replication.md": (500, 900),
    "resources-prefabs-configs.md": (500, 1000),
    "workbench-tools-debugging.md": (450, 850),
    "scenario-framework-game-master.md": (450, 850),
    "terrain-world-editor.md": (450, 850),
    "assets-weapons-vehicles-animation-audio.md": (500, 1000),
    "server-runtime-packaging.md": (350, 750),
    "examples-patterns.md": (500, 1000),
    "common-task-recipes.md": (450, 900),
    "api-main.md": (500, 1200),
}

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

TOPIC_REQUIRED_TERMS = {
    "overview.md": ["script-first", "data-first", "Workbench", "api-main.md", "api-extended.md"],
    "scripting-core.md": ["ScriptInvoker", "PrintFormat", "modded", "super", "profiling"],
    "scripting-language.md": ["ref", "Attribute", "JSON", "config", "preprocessor"],
    "entity-component-lifecycle.md": ["ScriptComponentClass", "ScriptComponent", "ComponentEditorProps", "EOnInit", "GetOwner", "SetOrigin"],
    "networking-multiplayer-replication.md": ["authority", "proxy", "owner", "BaseRplComponent", "RplRpc", "RplProp"],
    "resources-prefabs-configs.md": ["ResourceName", "Resource.Load", "prefab", "config", "BaseContainer", "entity catalog", "layout"],
    "workbench-tools-debugging.md": ["WorkbenchPlugin", "WorkbenchPluginAttribute", "ResourceManager", "ScriptEditor", "WorldEditor", "profiling"],
    "scenario-framework-game-master.md": ["Scenario", "Game Master", "faction", "task", "entity catalog", "Conflict"],
    "terrain-world-editor.md": ["World Editor", "terrain", "navmesh", "road", "river", "generator"],
    "assets-weapons-vehicles-animation-audio.md": ["weapon", "vehicle", "animation", "audio", "FBX", "texture"],
    "server-runtime-packaging.md": ["server", "startup", "Workshop", ".gproj", "dedicated"],
}

MARKDOWN_FORBIDDEN = [
    "[image omitted]",
    "Official Wiki Sources",
    "High-Signal Doc Notes",
    "Official Sample Sources",
    "Relevant APIs",
    "Headings:",
    "Source family:",
    "Source: `markdown/",
    "Show details",
    "TODO:",
    "Example Marker",
    "Audit Marker",
    "Coverage Marker",
    "Operational Detail Retention",
    "Expanded Source-Grounded Review Notes",
    "Retention note",
    "Preserve documented workflow",
    "Retain the official workflow step",
]

RAW_FORBIDDEN = [
    "raw/",
    "raw\\",
    "Sources Used",
    "Source files",
    "Raw source",
    "official sample corpus/",
    "extracted game API/",
    "markdown/Arma_Reforger_",
]

MOJIBAKE_MARKERS = ["Ã", "Â", "â", "ðŸ", "�"]

GENERIC_EVIDENCE_WORDS = {
    "workflow",
    "check",
    "checks",
    "system",
    "verify",
    "example",
    "reference",
    "guidance",
}


@dataclass(frozen=True)
class Concept:
    reference: str
    concept_id: str
    description: str
    evidence: tuple[str, ...]


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


def target_range(name: str) -> str:
    if name == "api-extended.md":
        return "exempt"
    low, high = TARGET_RANGES.get(name, (300, 900))
    return f"{low}-{high}"


def has_intentionally_short(text: str) -> bool:
    return "INTENTIONALLY SHORT" in text and "sparse" in text.lower()


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


def parse_required_concepts() -> list[Concept]:
    if not DESIGN.exists():
        return []

    text = read_text(DESIGN)
    concepts: list[Concept] = []
    current_ref: str | None = None

    ref_heading = re.compile(r"^### `([^`]+\.md)`\s*$")
    concept_line = re.compile(r"^-\s+`([A-Z]+-[A-Z0-9-]+)`:\s+(.+)$")

    for line in text.splitlines():
        heading_match = ref_heading.match(line)
        if heading_match:
            current_ref = heading_match.group(1)
            continue
        concept_match = concept_line.match(line)
        if concept_match and current_ref:
            concept_id = concept_match.group(1)
            description = concept_match.group(2)
            evidence = evidence_terms_from_concept(concept_id, description)
            concepts.append(Concept(current_ref, concept_id, description, tuple(evidence)))
    return concepts


def evidence_terms_from_concept(concept_id: str, description: str) -> list[str]:
    candidates = re.findall(r"`([^`]{2,80})`", description)
    candidates.extend(re.findall(r"\b[A-Z][A-Za-z0-9_]{3,}\b", description))
    candidates.extend(re.findall(r"\b[A-Za-z]+/[A-Za-z/]+\b", description))

    # Add stable terms from the concept id itself for domain concepts.
    for part in concept_id.split("-", 1)[1].split("-"):
        if len(part) >= 4:
            candidates.append(part.title())

    cleaned: list[str] = []
    for term in candidates:
        term = term.strip(" .,:;()[]")
        if len(term) < 3:
            continue
        if term.lower() in GENERIC_EVIDENCE_WORDS:
            continue
        if term not in cleaned:
            cleaned.append(term)
    return cleaned[:8]


def review_declared_lines() -> dict[str, int]:
    if not REVIEW.exists():
        return {}
    text = read_text(REVIEW)
    rows: dict[str, int] = {}
    for match in re.finditer(r"\|\s*`references/([^`]+\.md)`\s*\|\s*(\d+)\s*\|", text):
        rows[match.group(1)] = int(match.group(2))
    return rows


def review_concept_rows() -> set[str]:
    if not REVIEW.exists():
        return set()
    return set(re.findall(r"\|\s*`?([A-Z]+-[A-Z0-9-]+)`?\s*\|", read_text(REVIEW)))


def formatting_problems(name: str, text: str) -> list[str]:
    problems: list[str] = []
    for marker in MARKDOWN_FORBIDDEN:
        if marker in text:
            problems.append(f"markdown/crawler artifact: {marker}")
    for marker in MOJIBAKE_MARKERS:
        if marker in text:
            problems.append(f"encoding artifact: {marker}")
    for idx, line in enumerate(text.splitlines(), 1):
        if re.match(r"^#{1,6}\s+.*#{1,6}\s+", line):
            problems.append(f"collapsed heading at line {idx}")
            break
    inline_table_lines = [idx for idx, line in enumerate(text.splitlines(), 1) if line.count("|") >= 8 and not line.lstrip().startswith("|")]
    if inline_table_lines:
        problems.append(f"flattened inline table dump near line {inline_table_lines[0]}")
    return problems


def runtime_path_problems(name: str, text: str) -> list[str]:
    problems: list[str] = []
    forbidden = list(RAW_FORBIDDEN)
    if name != "api-extended.md":
        forbidden.append("addons_core\\scripts")
    for marker in forbidden:
        if marker in text:
            problems.append(f"runtime reference contains forbidden provenance marker: {marker}")
    return problems


def generic_padding_problems(name: str, text: str) -> list[str]:
    if name == "api-extended.md":
        return []
    lines = [line.strip() for line in text.splitlines() if line.strip().startswith("-")]
    if not lines:
        return []
    confirm_lines = [line for line in lines if line.startswith("- Confirm ")]
    if len(confirm_lines) >= 25 or (len(confirm_lines) / max(len(lines), 1)) > 0.45:
        return [f"too much generic checklist padding: {len(confirm_lines)} Confirm bullets"]
    duplicate_count = len(lines) - len(set(lines))
    if duplicate_count > 5:
        return [f"repeated bullet lines: {duplicate_count} duplicates"]
    return []


def concept_problems(name: str, text: str, concepts: list[Concept], review_ids: set[str], require_review_rows: bool) -> list[str]:
    if name == "api-extended.md":
        return []
    problems: list[str] = []
    relevant = [concept for concept in concepts if concept.reference == name]
    if not relevant:
        problems.append("no required concepts parsed from design for this reference")
        return problems

    for concept in relevant:
        if require_review_rows and concept.concept_id not in review_ids:
            problems.append(f"review missing required concept row: {concept.concept_id}")
        if concept.evidence and not any(term in text for term in concept.evidence):
            sample = ", ".join(concept.evidence[:4])
            problems.append(f"missing runtime evidence for concept {concept.concept_id}: expected one of {sample}")

    return problems


def topic_term_problems(name: str, text: str) -> list[str]:
    problems: list[str] = []
    for term in TOPIC_REQUIRED_TERMS.get(name, []):
        if term not in text:
            problems.append(f"missing topic term: {term}")
    return problems


def audit_skill_links() -> dict[str, object]:
    if not SKILL.exists():
        return {"name": "SKILL.md", "status": "FAIL", "lines": "", "target": "", "problems": ["missing SKILL.md"]}
    text = read_text(SKILL)
    refs = sorted(set(re.findall(r"references/[A-Za-z0-9_.-]+\.md", text)))
    problems = [f"missing linked reference: {ref}" for ref in refs if not (ROOT / ref).exists()]
    problems.extend(runtime_path_problems("SKILL.md", text))
    problems.extend(formatting_problems("SKILL.md", text))
    return {"name": "SKILL.md", "status": "PASS" if not problems else "FAIL", "lines": "", "target": "", "problems": problems}


def audit_review_counts(actual_counts: dict[str, int]) -> dict[str, object]:
    problems: list[str] = []
    if not REVIEW.exists():
        problems.append("missing generation/review.md")
        return {"name": "generation/review.md", "status": "FAIL", "lines": "", "target": "", "problems": problems}
    declared = review_declared_lines()
    for name in REQUIRED_REFERENCES:
        if name not in declared:
            problems.append(f"review missing line-count row for {name}")
            continue
        if declared[name] != actual_counts.get(name):
            problems.append(f"stale line count for {name}: review {declared[name]} != actual {actual_counts.get(name)}")
    if "Required concept coverage matrix" not in read_text(REVIEW):
        problems.append("review missing Required concept coverage matrix section")
    return {"name": "generation/review.md", "status": "PASS" if not problems else "FAIL", "lines": "", "target": "", "problems": problems}


def audit_reference(name: str, concepts: list[Concept], review_ids: set[str], require_review_rows: bool) -> dict[str, object]:
    path = REFERENCES / name
    problems: list[str] = []
    warnings: list[str] = []
    if not path.exists():
        return {"name": name, "status": "FAIL", "lines": 0, "target": target_range(name), "problems": ["missing file"], "warnings": []}

    text = read_text(path)
    lines = nonblank_lines(text)
    target = line_target(name)
    if target and lines < target and not has_intentionally_short(text):
        problems.append(f"minimum nonblank line target not met: {lines} < {target}")

    if name in TARGET_RANGES:
        ideal_low, _ = TARGET_RANGES[name]
        if lines < ideal_low and not has_intentionally_short(text):
            warnings.append(f"below useful detail range: {lines} < {ideal_low}")

    problems.extend(runtime_path_problems(name, text))
    problems.extend(formatting_problems(name, text))
    problems.extend(generic_padding_problems(name, text))

    if name != "api-extended.md":
        if not has_example(text):
            problems.append("missing direct example marker or no-example rationale")
        if not has_traps_or_checklist(text):
            problems.append("missing Common Traps or Review Checklist")
        if not has_api_notes(name, text):
            problems.append("missing API Notes")
        problems.extend(topic_term_problems(name, text))
        problems.extend(concept_problems(name, text, concepts, review_ids, require_review_rows))

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

    return {
        "name": name,
        "status": "PASS" if not problems else "FAIL",
        "lines": lines,
        "target": target_range(name),
        "problems": problems,
        "warnings": warnings,
    }


def main() -> int:
    skip_review = "--skip-review" in sys.argv[1:]
    concepts = parse_required_concepts()
    review_ids = set() if skip_review else review_concept_rows()
    rows: list[dict[str, object]] = []
    actual_counts: dict[str, int] = {}

    for name in REQUIRED_REFERENCES:
        row = audit_reference(name, concepts, review_ids, not skip_review)
        rows.append(row)
        if isinstance(row.get("lines"), int):
            actual_counts[name] = int(row["lines"])

    rows.append(audit_skill_links())
    if not skip_review:
        rows.append(audit_review_counts(actual_counts))

    failed = [row for row in rows if row["status"] != "PASS"]

    print("| File | Status | Nonblank lines | Useful detail range | Problems / warnings |")
    print("| --- | --- | ---: | --- | --- |")
    for row in rows:
        problems = row.get("problems", [])
        warnings = [f"WARNING: {warning}" for warning in row.get("warnings", [])]
        shown = [str(problem) for problem in problems[:18]]
        remaining_slots = max(0, 18 - len(shown))
        shown.extend(warnings[:remaining_slots])
        total_items = len(problems) + len(warnings)
        if total_items > len(shown):
            shown.append(f"... {total_items - len(shown)} more")
        problem_text = "<br>".join(shown) if shown else ""
        print(f"| `{row['name']}` | {row['status']} | {row.get('lines', '')} | {row.get('target', '')} | {problem_text} |")

    if failed:
        print(f"\nAudit failed: {len(failed)} file(s) need work.")
        return 1

    print("\nAudit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
