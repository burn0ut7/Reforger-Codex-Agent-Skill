#!/usr/bin/env python3
"""Build compact Codex lookup indexes from raw Arma Reforger game scripts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
GAME_DATA_ROOT = ROOT / "raw" / "game-data"
SCRIPTS_ROOT = GAME_DATA_ROOT / "scripts"
INDEXES_DIR = GAME_DATA_ROOT / "indexes"

INDEXER_NAME = "index-reforger-data.py"
INDEXER_VERSION = 3
INDEX_CONFIG_VERSION = 3

EXIT_CURRENT = 0
EXIT_STALE = 10
EXIT_CANNOT_DETERMINE = 2

REQUIRED_OUTPUTS = [
    GAME_DATA_ROOT / "api-schema.json",
    GAME_DATA_ROOT / "api-index.md",
    INDEXES_DIR / "symbols.jsonl",
    INDEXES_DIR / "files.jsonl",
    INDEXES_DIR / "examples.jsonl",
    INDEXES_DIR / "inheritance.jsonl",
    INDEXES_DIR / "manifest.json",
]

DECL_PREFIXES = {
    "static",
    "proto",
    "external",
    "native",
    "event",
    "override",
    "protected",
    "private",
    "public",
    "owned",
    "ref",
    "out",
    "const",
    "typename",
    "autoptr",
    "notnull",
    "abstract",
    "sealed",
    "volatile",
    "localized",
}

CONTROL_WORDS = {
    "if",
    "for",
    "while",
    "switch",
    "foreach",
    "return",
    "else",
    "case",
    "catch",
}

TOPIC_RULES: list[tuple[str, list[str]]] = [
    ("component", ["Component", "ScriptComponent", "GenericComponent", "FindComponent", "OnComponentInsert"]),
    ("entity-lifecycle", ["EOnInit", "EOnFrame", "EOnDelete", "EOnActivate", "EOnDeactivate", "EventMask"]),
    ("transform", ["SetOrigin", "GetOrigin", "SetTransform", "GetTransform", "CoordTo", "vector"]),
    ("user-action", ["UserAction", "ScriptedUserAction", "BaseUserAction", "CanBeShownScript", "PerformAction"]),
    ("replication", ["Replication", "RplComponent", "BaseRplComponent", "RplSession", "RplLoad", "RplSave"]),
    ("rpc", ["RplRpc", "Rpc(", "RPC", "RplRcver", "RplChannel"]),
    ("rpl-prop", ["RplProp", "OnRpl", "RplGroup", "RplCondition"]),
    ("workbench-plugin", ["WorkbenchPlugin", "WorkbenchPluginAttribute", "Workbench", "RunCommandline"]),
    ("resource-loading", ["ResourceName", "Resource.Load", "LoadResource", "ResourceNamePicker", "SpawnEntityPrefab", "PrefabResource"]),
    ("prefab", ["Prefab", "EntitySpawnParams", "SpawnEntityPrefab", "PrefabResource"]),
    ("game-mode", ["GameMode", "BaseGameMode", "SCR_BaseGameMode"]),
    ("scenario-framework", ["ScenarioFramework", "SCR_ScenarioFramework", "GameMaster", "Task", "Faction"]),
    ("weapon", ["Weapon", "Muzzle", "Magazine", "Firearm", "Turret"]),
    ("vehicle", ["Vehicle", "Compartment", "Wheeled", "Pilot", "BaseLightManagerComponent"]),
    ("inventory", ["Inventory", "InventoryStorage", "Item", "CharacterInventory"]),
    ("ui", ["UI", "Widget", "Menu", "HUD", "Layout", "LocalizedString"]),
    ("audio", ["Audio", "Sound", "SoundComponent", "SoundEvent", "Ak"]),
    ("animation", ["Animation", "Anim", "AnimGraph", "AnimationComponent"]),
]

SUBTOPIC_RULES: list[tuple[str, str, list[str]]] = [
    ("rpl-prop", "replication", ["RplProp", "OnRpl", "RplCondition", "RplGroup"]),
    ("rpc", "replication", ["RplRpc", "Rpc(", "RplRcver", "RplChannel"]),
    ("authority", "replication", ["HasAuthority", "IsMaster", "Authority", "Proxy", "RplRole"]),
    ("rpl-component", "replication", ["RplComponent", "BaseRplComponent", "RplLoad", "RplSave"]),
    ("resource-load", "resource-loading", ["Resource.Load", "LoadResource", "ResourceManager"]),
    ("spawn-prefab", "resource-loading", ["SpawnEntityPrefab", "EntitySpawnParams", "PrefabResource"]),
    ("resource-picker-config", "resource-loading", ["ResourceNamePicker", "UIWidgets.ResourceNamePicker"]),
    ("ui-layout-resource", "resource-loading", [".layout", "CreateWidgets"]),
    ("script-component", "component", ["ScriptComponent", "ScriptComponentClass"]),
    ("game-component", "component", ["GameComponent", "GenericComponent", "FindComponent"]),
    ("lifecycle", "component", ["EOnInit", "OnPostInit", "EOnFrame", "OnComponentInsert", "EventMask"]),
    ("scripted-user-action", "user-action", ["ScriptedUserAction", "BaseUserAction"]),
    ("perform-action", "user-action", ["PerformAction", "CanBePerformedScript"]),
    ("can-be-shown", "user-action", ["CanBeShownScript", "CanBeShown"]),
    ("workbench-plugin", "workbench-plugin", ["WorkbenchPlugin", "WorkbenchPluginAttribute"]),
    ("editor-ui", "workbench-plugin", ["Workbench", "Widget", "UIWidgets", "MenuItem"]),
    ("resource-browser", "workbench-plugin", ["ResourceBrowser", "ResourceNamePicker", "ResourceManager"]),
    ("weapon-component", "weapon", ["WeaponComponent", "BaseWeaponComponent", "BaseMuzzleComponent", "MuzzleComponent"]),
    ("muzzle", "weapon", ["MuzzleComponent", "BaseMuzzleComponent", "Muzzle", "MortarMuzzleComponent"]),
    ("magazine", "weapon", ["MagazineComponent", "BaseMagazineComponent", "Magazine", "MagazineWell"]),
    ("fire-mode", "weapon", ["FireMode", "Firearm", "SCR_EFireModeChange"]),
    ("turret", "weapon", ["Turret", "TurretControllerComponent"]),
    ("vehicle-component", "vehicle", ["VehicleControllerComponent", "BaseVehicleControllerComponent", "VehicleComponent"]),
    ("compartment", "vehicle", ["Compartment", "CompartmentManagerComponent", "BaseCompartmentManagerComponent"]),
    ("vehicle-controls", "vehicle", ["VehicleControllerComponent", "Pilot", "Wheeled", "Throttle", "Brake"]),
    ("vehicle-damage", "vehicle", ["DamageManagerComponent", "HitZone", "VehicleDamage"]),
    ("vehicle-lights", "vehicle", ["BaseLightManagerComponent", "LightManagerComponent", "VehicleLight"]),
    ("character-inventory", "inventory", ["CharacterInventory", "InventoryStorageManagerComponent"]),
    ("storage", "inventory", ["InventoryStorage", "InventoryStorageManagerComponent", "InventoryStorageSlot"]),
    ("item-equip", "inventory", ["Equip", "CanStoreItem", "TryInsertItem", "Pickup", "Item"],
    ),
    ("magazine-ammo", "inventory", ["Magazine", "Ammo", "Ammunition", "InventoryStorage"]),
    ("hud", "ui", ["HUD", "InfoDisplay", "SCR_InfoDisplay", "SCR_HUD"]),
    ("widget", "ui", ["Widget", "WorkspaceWidget", "TextWidget", "ImageWidget"]),
    ("menu", "ui", ["Menu", "MenuBase", "GetMenuManager"]),
    ("layout", "ui", [".layout", "CreateWidgets", "Layout"]),
    ("map-marker", "ui", ["MapMarker", "SCR_MapMarker", "MapEntity"]),
    ("sound-component", "audio", ["SoundComponent", "SimpleSoundComponent"]),
    ("sound-event", "audio", ["SoundEvent", "AudioSystem", "SoundEventName"]),
    ("voice", "audio", ["Voice", "Voiceover", "RadioProtocol"]),
    ("music", "audio", ["Music", "MusicManager", "SoundEvent"]),
    ("anim-graph", "animation", ["AnimGraph", "AnimationGraph"]),
    ("character-animation", "animation", ["CharacterAnimationComponent", "CharacterCommand", "AnimationComponent"]),
    ("procedural-animation", "animation", ["AnimPhys", "BaseAnimPhysComponent", "ProceduralAnimation"]),
]


@dataclass
class Context:
    file: str
    module: str
    generated: bool


@dataclass
class ClassScope:
    name: str
    start_depth: int


@dataclass
class ParsedFile:
    file: str
    module: str
    generated: bool
    line_count: int
    symbols: list[dict[str, Any]] = field(default_factory=list)
    classes: list[dict[str, Any]] = field(default_factory=list)
    enums: list[dict[str, Any]] = field(default_factory=list)
    functions: list[dict[str, Any]] = field(default_factory=list)
    inheritance: list[dict[str, Any]] = field(default_factory=list)
    attributes: list[str] = field(default_factory=list)
    text_tokens: set[str] = field(default_factory=set)
    topic_lines: dict[str, list[int]] = field(default_factory=dict)
    subtopic_lines: dict[str, list[int]] = field(default_factory=dict)
    evidence: dict[str, set[str]] = field(default_factory=dict)


def log(message: str) -> None:
    print(f"[reforger-index] {message}", flush=True)


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except FileNotFoundError as exc:
        raise RuntimeError(f"Missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise RuntimeError(f"Expected JSON object in {path}")
    return data


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")) for record in records]
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8", newline="\n")


def game_source(manifest: dict[str, Any]) -> dict[str, Any]:
    source = manifest.get("source")
    if not isinstance(source, dict):
        raise RuntimeError("raw/game-data/manifest.json is missing source metadata")
    commit = source.get("commit")
    if not isinstance(commit, str) or not commit.strip():
        raise RuntimeError("raw/game-data/manifest.json is missing source.commit")
    return source


def validate_inputs(game_data_root: Path) -> dict[str, Any]:
    manifest = load_json(game_data_root / "manifest.json")
    game_source(manifest)
    scripts_root = game_data_root / "scripts"
    if not scripts_root.exists() or not scripts_root.is_dir():
        raise RuntimeError(f"Missing required scripts directory: {scripts_root}")
    return manifest


def expected_game_data(manifest: dict[str, Any]) -> dict[str, Any]:
    source = game_source(manifest)
    return {
        "repo": source.get("repo"),
        "ref": source.get("ref"),
        "commit": source.get("commit"),
        "sparsePath": source.get("sparsePath"),
    }


def deterministic_generated_at(manifest: dict[str, Any]) -> str:
    generated_at = manifest.get("generatedAt")
    if isinstance(generated_at, str) and generated_at:
        return generated_at
    return str(expected_game_data(manifest).get("commit") or "unknown")


def index_status(game_data_root: Path) -> tuple[int, dict[str, Any]]:
    manifest = validate_inputs(game_data_root)
    expected = expected_game_data(manifest)
    index_manifest_path = game_data_root / "indexes" / "manifest.json"
    missing = [str(path.relative_to(game_data_root)) for path in REQUIRED_OUTPUTS if not path.exists()]
    status: dict[str, Any] = {
        "gameDataCommit": expected["commit"],
        "missingOutputs": missing,
        "needsIndex": False,
        "status": "current",
    }
    if missing:
        status["status"] = "missing-indexes"
        status["needsIndex"] = True
        return EXIT_STALE, status

    index_manifest = load_json(index_manifest_path)
    indexer = index_manifest.get("indexer")
    game_data = index_manifest.get("gameData")
    if not isinstance(indexer, dict) or not isinstance(game_data, dict):
        status["status"] = "invalid-index-manifest"
        status["needsIndex"] = True
        return EXIT_STALE, status

    if game_data.get("commit") != expected["commit"]:
        status["status"] = "stale-game-data"
        status["indexCommit"] = game_data.get("commit")
        status["needsIndex"] = True
        return EXIT_STALE, status
    if indexer.get("version") != INDEXER_VERSION or indexer.get("configVersion") != INDEX_CONFIG_VERSION:
        status["status"] = "stale-indexer"
        status["indexer"] = indexer
        status["needsIndex"] = True
        return EXIT_STALE, status

    return EXIT_CURRENT, status


def print_status(status: dict[str, Any]) -> None:
    print(f"[reforger-index] status: {status['status']}")
    print(f"[reforger-index] game-data commit: {status.get('gameDataCommit') or 'unknown'}")
    if status.get("missingOutputs"):
        print(f"[reforger-index] missing outputs: {', '.join(status['missingOutputs'])}")
    if status.get("indexCommit"):
        print(f"[reforger-index] index commit: {status['indexCommit']}")


def normalize_path(path: Path, scripts_root: Path) -> str:
    relative = path.relative_to(scripts_root.parent)
    return relative.as_posix()


def module_from_path(normalized: str) -> str:
    parts = normalized.split("/")
    return parts[1] if len(parts) > 1 and parts[0] == "scripts" else ""


def is_generated_path(normalized: str) -> bool:
    return "/generated/" in f"/{normalized}/"


def strip_line_comment(line: str) -> str:
    in_string = False
    escaped = False
    for index, char in enumerate(line):
        if char == "\\" and in_string:
            escaped = not escaped
            continue
        if char == '"' and not escaped:
            in_string = not in_string
        escaped = False
        if not in_string and line[index : index + 2] == "//":
            return line[:index]
    return line


def code_part(line: str, in_block_comment: bool) -> tuple[str, bool]:
    output: list[str] = []
    index = 0
    while index < len(line):
        if in_block_comment:
            end = line.find("*/", index)
            if end == -1:
                return "".join(output), True
            index = end + 2
            in_block_comment = False
            continue
        start = line.find("/*", index)
        slash = line.find("//", index)
        if slash != -1 and (start == -1 or slash < start):
            output.append(line[index:slash])
            return "".join(output), False
        if start == -1:
            output.append(line[index:])
            return "".join(output), False
        output.append(line[index:start])
        index = start + 2
        in_block_comment = True
    return "".join(output), in_block_comment


def brace_delta(code: str) -> int:
    delta = 0
    in_string = False
    escaped = False
    for char in code:
        if char == "\\" and in_string:
            escaped = not escaped
            continue
        if char == '"' and not escaped:
            in_string = not in_string
        escaped = False
        if in_string:
            continue
        if char == "{":
            delta += 1
        elif char == "}":
            delta -= 1
    return delta


def clean_doc_lines(lines: list[str]) -> list[str]:
    cleaned: list[str] = []
    for raw in lines:
        line = raw.strip()
        line = re.sub(r"^/\*!?", "", line).strip()
        line = re.sub(r"^\*/$", "", line).strip()
        line = re.sub(r"^\* ?", "", line).strip()
        line = re.sub(r"^//! ?", "", line).strip()
        line = re.sub(r"^// ?", "", line).strip()
        if not line or line in {"{", "}", "\\{", "\\}"}:
            continue
        if line.startswith("\\addtogroup"):
            continue
        cleaned.append(line)
    return cleaned[:8]


def bounded_docs(lines: list[str]) -> list[str]:
    docs = clean_doc_lines(lines)
    text = "\n".join(docs)
    if len(text) <= 800:
        return docs
    shortened = text[:797].rstrip() + "..."
    return shortened.splitlines()


def declaration_signature(lines: list[str]) -> str:
    signature = " ".join(part.strip() for part in lines if part.strip())
    signature = re.sub(r"\s+", " ", signature).strip()
    signature = signature.rstrip("{").strip()
    if signature and not signature.endswith(";") and "(" in signature and ")" in signature:
        signature += ";"
    return signature


def strip_default(value: str) -> str:
    depth = 0
    in_string = False
    escaped = False
    for index, char in enumerate(value):
        if char == "\\" and in_string:
            escaped = not escaped
            continue
        if char == '"' and not escaped:
            in_string = not in_string
        escaped = False
        if in_string:
            continue
        if char in "([{":
            depth += 1
        elif char in ")]}":
            depth -= 1
        elif char == "=" and depth == 0:
            return value[:index].strip()
    return value.strip()


def split_top_level(value: str, separator: str = ",") -> list[str]:
    parts: list[str] = []
    start = 0
    depth = 0
    in_string = False
    escaped = False
    for index, char in enumerate(value):
        if char == "\\" and in_string:
            escaped = not escaped
            continue
        if char == '"' and not escaped:
            in_string = not in_string
        escaped = False
        if in_string:
            continue
        if char in "([{":
            depth += 1
        elif char in ")]}":
            depth -= 1
        elif char == separator and depth == 0:
            parts.append(value[start:index].strip())
            start = index + 1
    tail = value[start:].strip()
    if tail:
        parts.append(tail)
    return parts


def parse_parameters(text: str) -> list[dict[str, Any]]:
    text = text.strip()
    if not text:
        return []
    parameters: list[dict[str, Any]] = []
    for raw in split_top_level(text):
        clean = strip_default(raw)
        tokens = clean.split()
        if not tokens:
            continue
        name = tokens[-1]
        array_suffix = ""
        array_match = re.match(r"^(.+?)(\[[^\]]*\])+$", name)
        if array_match:
            name = array_match.group(1)
            array_suffix = clean[len(clean) - len(array_match.group(2)) :]
        type_tokens = tokens[:-1]
        modifiers = [token for token in type_tokens if token in DECL_PREFIXES]
        type_parts = [token for token in type_tokens if token not in DECL_PREFIXES]
        param_type = " ".join(type_parts).strip()
        if array_suffix:
            param_type = f"{param_type}{array_suffix}".strip()
        parameters.append({"name": name, "type": param_type, "modifiers": modifiers, "raw": raw})
    return parameters


def parse_callable(signature: str) -> dict[str, Any] | None:
    if "(" not in signature or ")" not in signature:
        return None
    prefix = signature[: signature.find("(")].strip()
    params = signature[signature.find("(") + 1 : signature.rfind(")")]
    tokens = prefix.split()
    if not tokens:
        return None
    name = tokens[-1]
    if name in CONTROL_WORDS:
        return None
    before_name = tokens[:-1]
    modifiers = [token for token in before_name if token in DECL_PREFIXES]
    return_tokens = [token for token in before_name if token not in DECL_PREFIXES]
    return_type = " ".join(return_tokens).strip()
    return {"name": name, "returnType": return_type, "modifiers": modifiers, "parameters": parse_parameters(params)}


def parse_property(signature: str) -> dict[str, Any] | None:
    if not signature.endswith(";"):
        return None
    clean = strip_default(signature.rstrip(";").strip())
    if "(" in clean:
        return None
    if not clean or clean.startswith(("typedef ", "class ", "enum ")):
        return None
    tokens = clean.split()
    if len(tokens) < 2:
        return None
    name = tokens[-1]
    if name in CONTROL_WORDS or name.startswith("#"):
        return None
    modifiers = [token for token in tokens[:-1] if token in DECL_PREFIXES]
    type_tokens = [token for token in tokens[:-1] if token not in DECL_PREFIXES]
    if not type_tokens:
        return None
    return {"name": name, "type": " ".join(type_tokens), "modifiers": modifiers}


def base_symbol_record(kind: str, name: str, ctx: Context, line: int, attrs: list[str], docs: list[str]) -> dict[str, Any]:
    return {
        "kind": kind,
        "name": name,
        "qualifiedName": name,
        "attributes": attrs,
        "docs": docs,
        "file": ctx.file,
        "line": line,
        "module": ctx.module,
        "generated": ctx.generated,
    }


def class_record(match: re.Match[str], ctx: Context, line: int, attrs: list[str], docs: list[str]) -> dict[str, Any]:
    modifiers = [token for token in (match.group("modifiers") or "").split() if token]
    kind = "modded class" if "modded" in modifiers else "class"
    name = match.group("name")
    extends = match.group("extends") or ""
    record = base_symbol_record(kind, name, ctx, line, attrs, docs)
    record["extends"] = extends
    record["modifiers"] = modifiers
    return record


def enum_record(name: str, ctx: Context, line: int, attrs: list[str], docs: list[str]) -> dict[str, Any]:
    record = base_symbol_record("enum", name, ctx, line, attrs, docs)
    record["values"] = []
    return record


def method_record(owner: str, parsed: dict[str, Any], signature: str, ctx: Context, line: int, attrs: list[str], docs: list[str]) -> dict[str, Any]:
    name = parsed["name"]
    return {
        "kind": "method",
        "name": name,
        "owner": owner,
        "qualifiedName": f"{owner}.{name}",
        "signature": signature,
        "returnType": parsed["returnType"],
        "parameters": parsed["parameters"],
        "modifiers": parsed["modifiers"],
        "attributes": attrs,
        "docs": docs,
        "file": ctx.file,
        "line": line,
        "module": ctx.module,
        "generated": ctx.generated,
    }


def function_record(parsed: dict[str, Any], signature: str, ctx: Context, line: int, attrs: list[str], docs: list[str]) -> dict[str, Any]:
    name = parsed["name"]
    return {
        "kind": "function",
        "name": name,
        "qualifiedName": name,
        "signature": signature,
        "returnType": parsed["returnType"],
        "parameters": parsed["parameters"],
        "modifiers": parsed["modifiers"],
        "attributes": attrs,
        "docs": docs,
        "file": ctx.file,
        "line": line,
        "module": ctx.module,
        "generated": ctx.generated,
    }


def property_record(owner: str, parsed: dict[str, Any], signature: str, ctx: Context, line: int, attrs: list[str], docs: list[str]) -> dict[str, Any]:
    name = parsed["name"]
    return {
        "kind": "property",
        "name": name,
        "owner": owner,
        "qualifiedName": f"{owner}.{name}",
        "signature": signature,
        "type": parsed["type"],
        "modifiers": parsed["modifiers"],
        "attributes": attrs,
        "docs": docs,
        "file": ctx.file,
        "line": line,
        "module": ctx.module,
        "generated": ctx.generated,
    }


def token_text(value: str) -> list[str]:
    return re.findall(r"[A-Za-z_][A-Za-z0-9_]*", value)


def class_decl_match(signature: str) -> re.Match[str] | None:
    return re.match(
        r"^(?P<modifiers>(?:(?:sealed|abstract|modded)\s+)*)class\s+"
        r"(?P<name>[A-Za-z_][A-Za-z0-9_]*)"
        r"(?:\s*:\s*(?P<extends>[A-Za-z_][A-Za-z0-9_]*))?",
        signature,
    )


def enum_decl_match(signature: str) -> re.Match[str] | None:
    return re.match(r"^enum\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)", signature)


def pending_complete(lines: list[str]) -> bool:
    signature = declaration_signature(lines)
    if not signature:
        return False
    if class_decl_match(signature) or enum_decl_match(signature):
        return True
    return signature.endswith(";") or "{" in " ".join(lines)


def add_topic_evidence(parsed: ParsedFile, text: str, line_number: int) -> None:
    lowered = text.lower()
    if "resource.load" in lowered:
        parsed.text_tokens.add("Resource.Load")
    if "spawnentityprefab" in lowered:
        parsed.text_tokens.add("SpawnEntityPrefab")
    if "uiwidgets.resourcenamepicker" in lowered:
        parsed.text_tokens.add("UIWidgets.ResourceNamePicker")
    for topic, needles in TOPIC_RULES:
        hits = [needle for needle in needles if needle.lower() in lowered]
        if hits:
            parsed.topic_lines.setdefault(topic, []).append(line_number)
            parsed.evidence.setdefault(topic, set()).update(hits)
    for subtopic, topic, needles in SUBTOPIC_RULES:
        hits = [needle for needle in needles if needle.lower() in lowered]
        if hits:
            parsed.topic_lines.setdefault(topic, []).append(line_number)
            parsed.subtopic_lines.setdefault(subtopic, []).append(line_number)
            parsed.evidence.setdefault(topic, set()).update(hits)
            parsed.evidence.setdefault(subtopic, set()).update(hits)


def in_body_context(scopes: list[ClassScope], depth: int) -> bool:
    if scopes:
        return depth > scopes[-1].start_depth
    return depth > 0


def parse_file(path: Path, scripts_root: Path) -> ParsedFile:
    normalized = normalize_path(path, scripts_root)
    ctx = Context(normalized, module_from_path(normalized), is_generated_path(normalized))
    lines = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    parsed = ParsedFile(ctx.file, ctx.module, ctx.generated, len(lines))

    pending_docs: list[str] = []
    pending_attrs: list[str] = []
    pending_decl: list[str] = []
    pending_line = 0
    scopes: list[ClassScope] = []
    depth = 0
    in_block_comment = False
    collecting_doc_block = False
    enum_body_depth: int | None = None
    awaiting_class_scope: str | None = None
    awaiting_enum_body = False

    for line_number, raw_line in enumerate(lines, start=1):
        stripped = raw_line.strip()
        add_topic_evidence(parsed, raw_line, line_number)

        if in_body_context(scopes, depth):
            code, in_block_comment = code_part(raw_line, in_block_comment)
            depth += brace_delta(code)
            while scopes and depth < scopes[-1].start_depth:
                scopes.pop()
            continue

        if collecting_doc_block:
            pending_docs.append(stripped)
            if "*/" in stripped:
                collecting_doc_block = False
            continue
        if stripped.startswith("/*!") or stripped.startswith("/**"):
            pending_docs.append(stripped)
            if "*/" not in stripped:
                collecting_doc_block = True
            continue
        if stripped.startswith("//!"):
            pending_docs.append(stripped)
            continue
        if stripped.startswith("[") and not pending_decl:
            pending_attrs.append(stripped)
            parsed.attributes.append(stripped)
            if "]" not in stripped:
                pending_decl.append(stripped)
                pending_line = line_number
            continue
        if pending_decl and pending_decl[0].startswith("[") and not stripped.endswith("]"):
            pending_decl.append(stripped)
            continue
        if pending_decl and pending_decl[0].startswith("[") and stripped.endswith("]"):
            pending_decl.append(stripped)
            pending_attrs[-1] = declaration_signature(pending_decl)
            pending_decl = []
            continue

        code, in_block_comment = code_part(raw_line, in_block_comment)
        code = code.strip()
        before_delta_depth = depth

        while scopes and before_delta_depth < scopes[-1].start_depth:
            scopes.pop()

        if awaiting_class_scope and code.startswith("{"):
            scopes.append(ClassScope(awaiting_class_scope, before_delta_depth + 1))
            awaiting_class_scope = None
            depth += brace_delta(code)
            continue

        if awaiting_enum_body and code.startswith("{"):
            awaiting_enum_body = False
            enum_body_depth = before_delta_depth + 1
            depth += brace_delta(code)
            if depth < enum_body_depth:
                enum_body_depth = None
            continue

        if enum_body_depth is not None:
            depth += brace_delta(code)
            if depth < enum_body_depth:
                enum_body_depth = None
            continue

        if code and re.fullmatch(r"[{};]+", code):
            depth += brace_delta(code)
            while scopes and depth < scopes[-1].start_depth:
                scopes.pop()
            continue

        if code and not code.startswith("#"):
            if pending_decl and "(" in code and "(" not in " ".join(pending_decl) and not pending_decl[0].startswith("["):
                pending_decl = []
                pending_docs = []
                pending_attrs = []
                pending_line = line_number
            if not pending_decl:
                pending_line = line_number
            pending_decl.append(code)

            if pending_complete(pending_decl):
                signature = declaration_signature(pending_decl)
                docs = bounded_docs(pending_docs)
                attrs = list(pending_attrs)
                owner = scopes[-1].name if scopes and before_delta_depth == scopes[-1].start_depth else ""

                match = class_decl_match(signature)
                if match:
                    record = class_record(match, ctx, pending_line, attrs, docs)
                    parsed.symbols.append(record)
                    parsed.classes.append(record)
                    parsed.text_tokens.update(token_text(record["name"]))
                    if record.get("extends"):
                        parsed.text_tokens.add(record["extends"])
                        parsed.inheritance.append(
                            {
                                "class": record["name"],
                                "extends": record["extends"],
                                "file": ctx.file,
                                "line": pending_line,
                                "module": ctx.module,
                                "generated": ctx.generated,
                            }
                        )
                    if "{" in " ".join(pending_decl):
                        scopes.append(ClassScope(record["name"], before_delta_depth + 1))
                    else:
                        awaiting_class_scope = record["name"]
                else:
                    enum_match = enum_decl_match(signature)
                    if enum_match:
                        record = enum_record(enum_match.group("name"), ctx, pending_line, attrs, docs)
                        parsed.symbols.append(record)
                        parsed.enums.append(record)
                        parsed.text_tokens.add(record["name"])
                        if "{" in " ".join(pending_decl):
                            enum_body_depth = before_delta_depth + 1
                        else:
                            awaiting_enum_body = True
                    else:
                        property_info = parse_property(signature) if owner else None
                        if property_info:
                            record = property_record(owner, property_info, signature, ctx, pending_line, attrs, docs)
                            parsed.symbols.append(record)
                            parsed.text_tokens.update(token_text(record["qualifiedName"]))
                            parsed.text_tokens.update(token_text(signature))
                        else:
                            callable_info = parse_callable(signature)
                            if callable_info:
                                if owner:
                                    record = method_record(owner, callable_info, signature, ctx, pending_line, attrs, docs)
                                else:
                                    record = function_record(callable_info, signature, ctx, pending_line, attrs, docs)
                                    parsed.functions.append(record)
                                parsed.symbols.append(record)
                                parsed.text_tokens.update(token_text(record["qualifiedName"]))
                                parsed.text_tokens.update(token_text(signature))

                pending_decl = []
                pending_docs = []
                pending_attrs = []

        depth += brace_delta(code)
        while scopes and depth < scopes[-1].start_depth:
            scopes.pop()

    parsed.text_tokens.update(token_text(parsed.file))
    return parsed


def topic_tags(parsed: ParsedFile) -> list[str]:
    haystack = " ".join(sorted(parsed.text_tokens)) + " " + parsed.file
    lowered = haystack.lower()
    tags = set(parsed.topic_lines)
    for topic, needles in TOPIC_RULES:
        if any(needle.lower() in lowered for needle in needles):
            tags.add(topic)
    for _subtopic, topic, needles in SUBTOPIC_RULES:
        if any(needle.lower() in lowered for needle in needles):
            tags.add(topic)
    return sorted(tags)


def subtopic_tags(parsed: ParsedFile, topic: str | None = None) -> list[str]:
    tags = set(parsed.subtopic_lines)
    haystack = " ".join(sorted(parsed.text_tokens)) + " " + parsed.file
    lowered = haystack.lower()
    for subtopic, parent_topic, needles in SUBTOPIC_RULES:
        if topic and parent_topic != topic:
            continue
        if any(needle.lower() in lowered for needle in needles):
            tags.add(subtopic)
    if topic:
        allowed = {subtopic for subtopic, parent, _needles in SUBTOPIC_RULES if parent == topic}
        tags &= allowed
    return sorted(tags)


def file_record(parsed: ParsedFile, tags: list[str]) -> dict[str, Any]:
    declared = sorted({record["name"] for record in parsed.symbols if record["kind"] in {"class", "modded class", "enum", "function"}})
    bases = sorted({record["extends"] for record in parsed.classes if record.get("extends")})
    attributes = sorted(set(parsed.attributes))[:20]
    subtopics = subtopic_tags(parsed)
    evidence = sorted({item for tag in tags + subtopics for item in parsed.evidence.get(tag, set())})[:24]
    search_terms = sorted(set(declared + bases + attributes + tags + subtopics + evidence + sorted(parsed.text_tokens)))[:100]
    return {
        "file": parsed.file,
        "module": parsed.module,
        "generated": parsed.generated,
        "lineCount": parsed.line_count,
        "declaredSymbols": declared,
        "baseClasses": bases,
        "attributes": attributes,
        "topicTags": tags,
        "subtopics": subtopics,
        "evidence": evidence,
        "searchText": " ".join(search_terms),
    }


def symbol_names(parsed: ParsedFile, kind: str | None = None) -> set[str]:
    return {record["name"] for record in parsed.symbols if kind is None or record["kind"] == kind}


def owner_method_names(parsed: ParsedFile) -> set[str]:
    return {record["name"] for record in parsed.symbols if record["kind"] == "method"}


def class_bases(parsed: ParsedFile) -> set[str]:
    return {record["extends"] for record in parsed.classes if record.get("extends")}


def attr_text(parsed: ParsedFile) -> str:
    return " ".join(parsed.attributes)


def topic_strength(parsed: ParsedFile, topic: str) -> int:
    bases = class_bases(parsed)
    methods = owner_method_names(parsed)
    attrs = attr_text(parsed)
    classes = symbol_names(parsed, "class") | symbol_names(parsed, "modded class")
    file_lower = parsed.file.lower()
    subtopics = set(subtopic_tags(parsed, topic))
    strength = 0

    if topic == "user-action":
        if bases & {"ScriptedUserAction", "BaseUserAction"}:
            strength += 30
        if {"CanBeShownScript", "CanBePerformedScript", "PerformAction"} & methods:
            strength += 25
        if any(name.endswith("UserAction") for name in classes):
            strength += 10
        if "performaction" in file_lower and "useraction" not in file_lower:
            strength -= 20
    elif topic == "component":
        if bases & {"ScriptComponent", "GenericComponent", "GameComponent"}:
            strength += 25
        if any(name.endswith("Component") for name in classes):
            strength += 15
        if {"EOnInit", "OnPostInit", "OnComponentInsert"} & methods:
            strength += 10
    elif topic == "replication":
        strength += len(subtopics & {"rpl-prop", "rpc", "authority", "rpl-component"}) * 10
        if bases & {"RplComponent", "BaseRplComponent"}:
            strength += 30
        if {"RplLoad", "RplSave", "OnPostInit"} & methods:
            strength += 15
        if any(token in attrs for token in ["RplProp", "RplRpc"]):
            strength += 15
    elif topic == "rpc":
        if "RplRpc" in attrs:
            strength += 35
        if "rpc" in file_lower:
            strength += 10
    elif topic == "rpl-prop":
        if "RplProp" in attrs:
            strength += 35
        if "rplprop" in file_lower:
            strength += 10
    elif topic == "workbench-plugin":
        strength += len(subtopics & {"workbench-plugin", "editor-ui", "resource-browser"}) * 8
        if bases & {"WorkbenchPlugin"}:
            strength += 35
        if "WorkbenchPluginAttribute" in attrs:
            strength += 30
        if parsed.module.startswith("Workbench"):
            strength += 15
        elif "workbench" not in file_lower:
            strength -= 20
    elif topic == "resource-loading":
        strength += len(subtopics & {"resource-load", "spawn-prefab", "resource-picker-config", "ui-layout-resource"}) * 12
        direct_resource = bool({"Resource.Load", "SpawnEntityPrefab", "UIWidgets.ResourceNamePicker"} & parsed.text_tokens)
        if direct_resource:
            strength += 30
        if "SpawnEntityPrefab" in parsed.text_tokens:
            strength += 12
        if "Resource.Load" in parsed.text_tokens:
            strength += 12
        if "ResourceName" in symbol_names(parsed, "property") or "ResourceName" in " ".join(parsed.text_tokens):
            strength += 15
        if parsed.topic_lines.get(topic):
            strength += 10
        if "tests/test" in file_lower and not direct_resource:
            strength -= 35
        if "replication/" in file_lower or "rpldocs" in file_lower:
            strength -= 45
        if any(path_part in file_lower for path_part in ["/worldeditor/", "/editor/", "/building/", "/gamemode/"]):
            strength += 8
    elif topic == "weapon":
        strength += len(subtopics & {"weapon-component", "muzzle", "magazine", "fire-mode", "turret"}) * 14
        if bases & {"BaseWeaponComponent", "WeaponComponent", "BaseMuzzleComponent", "MuzzleComponent", "MagazineComponent", "TurretControllerComponent"}:
            strength += 30
        if any(name.endswith(("WeaponComponent", "MuzzleComponent", "MagazineComponent")) for name in classes):
            strength += 20
        if any(path_part in file_lower for path_part in ["/weapon/", "/weapons/", "/muzzle", "/magazine", "/turret"]):
            strength += 16
        if parsed.evidence.get(topic) and parsed.evidence.get(topic) <= {"Weapon", "Muzzle", "Magazine", "Turret"}:
            strength -= 15
    elif topic == "vehicle":
        strength += len(subtopics & {"vehicle-component", "compartment", "vehicle-controls", "vehicle-damage", "vehicle-lights"}) * 14
        if bases & {"BaseVehicleControllerComponent", "VehicleControllerComponent", "BaseCompartmentManagerComponent", "BaseLightManagerComponent"}:
            strength += 30
        if any("Vehicle" in name or "Compartment" in name for name in classes):
            strength += 16
        if any(path_part in file_lower for path_part in ["/vehicle/", "/vehicles/", "/compartment", "/wheeled"]):
            strength += 16
        if parsed.evidence.get(topic) and parsed.evidence.get(topic) <= {"Vehicle", "Compartment", "Pilot"}:
            strength -= 12
    elif topic == "inventory":
        strength += len(subtopics & {"character-inventory", "storage", "item-equip", "magazine-ammo"}) * 14
        if bases & {"InventoryStorageManagerComponent", "InventoryItemComponent", "BaseInventoryStorageComponent"}:
            strength += 25
        if any("Inventory" in name or "Storage" in name for name in classes):
            strength += 18
        if any(path_part in file_lower for path_part in ["/inventory/", "/inventorysystem/", "/arsenal/"]):
            strength += 16
        if parsed.evidence.get(topic) and parsed.evidence.get(topic) <= {"Item", "Inventory"}:
            strength -= 18
    elif topic == "ui":
        strength += len(subtopics & {"hud", "widget", "menu", "layout", "map-marker"}) * 14
        if any("Widget" in name or "Menu" in name or "HUD" in name or "InfoDisplay" in name for name in classes):
            strength += 22
        if any(path_part in file_lower for path_part in ["/ui/", "/hud/", "/menu/", "/map/markers/"]):
            strength += 16
        if parsed.evidence.get(topic) and parsed.evidence.get(topic) <= {"UI", "Layout", "Widget"}:
            strength -= 12
        if parsed.module == "Autotest":
            strength -= 25
    elif topic == "audio":
        strength += len(subtopics & {"sound-component", "sound-event", "voice", "music"}) * 14
        if bases & {"SoundComponent", "SimpleSoundComponent"}:
            strength += 25
        if any("Sound" in name or "Audio" in name or "Voice" in name for name in classes):
            strength += 20
        if any(path_part in file_lower for path_part in ["/audio/", "/sound/", "/voice", "/music"]):
            strength += 16
        if parsed.evidence.get(topic) and parsed.evidence.get(topic) <= {"Sound", "Audio", "Ak"}:
            strength -= 12
    elif topic == "animation":
        strength += len(subtopics & {"anim-graph", "character-animation", "procedural-animation"}) * 14
        if bases & {"BaseAnimPhysComponent", "CharacterAnimationComponent"}:
            strength += 25
        if any("Animation" in name or "Anim" in name or "CharacterCommand" in name for name in classes):
            strength += 20
        if any(path_part in file_lower for path_part in ["/animation/", "/anim", "/character/commands/", "/cinematics/"]):
            strength += 16
        if parsed.evidence.get(topic) and parsed.evidence.get(topic) <= {"Anim", "Animation"}:
            strength -= 12
    else:
        if parsed.topic_lines.get(topic):
            strength += 10

    if "Docs" in parsed.file or "Example" in parsed.file:
        strength += 12
    if topic in {"replication", "rpc", "rpl-prop"} and "RplDocs" in parsed.file:
        strength += 35
    return strength


def example_priority(parsed: ParsedFile, topic: str) -> int:
    priority = 20
    if not parsed.generated:
        priority += 25
    else:
        priority -= 25
    if parsed.module in {"GameCode", "Game"} or parsed.module.startswith("Workbench"):
        priority += 5
    if parsed.module == "Autotest":
        priority -= 20
    if parsed.line_count <= 180:
        priority += 5
    elif parsed.line_count <= 500:
        priority += 2
    if "Docs" in parsed.file or "Example" in parsed.file:
        priority += 12
    if topic in {"replication", "rpc", "rpl-prop"} and "RplDocs" in parsed.file:
        priority += 25
    priority += topic_strength(parsed, topic)
    return priority


def example_reason(parsed: ParsedFile, topic: str) -> str:
    names = ", ".join(sorted({record["name"] for record in parsed.classes})[:3])
    subject = f"defines {names}" if names else "contains source patterns"
    subtopics = ", ".join(subtopic_tags(parsed, topic)[:4])
    suffix = f" ({subtopics})" if subtopics else ""
    return f"{subject} for {topic}{suffix}"


def relevant_symbol_lines(parsed: ParsedFile, topic: str) -> list[int]:
    lines: list[int] = []
    for record in parsed.symbols:
        kind = record.get("kind")
        name = str(record.get("name") or "")
        extends = str(record.get("extends") or "")
        attrs = " ".join(str(item) for item in record.get("attributes", []))
        line = record.get("line")
        if not isinstance(line, int):
            continue

        if topic == "user-action" and (
            extends in {"ScriptedUserAction", "BaseUserAction"}
            or name in {"CanBeShownScript", "CanBePerformedScript", "PerformAction"}
            or name.endswith("UserAction")
        ):
            lines.append(line)
        elif topic == "component" and (
            extends in {"ScriptComponent", "GenericComponent", "GameComponent"} or name.endswith("Component") or name in {"EOnInit", "OnPostInit", "OnComponentInsert"}
        ):
            lines.append(line)
        elif topic in {"replication", "rpc", "rpl-prop"} and (
            "Rpl" in name or "Rpl" in extends or "Rpl" in attrs or name in {"RplLoad", "RplSave"}
        ):
            lines.append(line)
        elif topic == "workbench-plugin" and ("Workbench" in name or "Workbench" in extends or "Workbench" in attrs):
            lines.append(line)
        elif topic == "resource-loading" and (
            "ResourceName" in name or "ResourceName" in attrs or name in {"Load", "SpawnEntityPrefab"} or "ResourceName" in str(record.get("type") or "")
        ):
            lines.append(line)
        elif kind in {"class", "modded class"}:
            lines.append(line)
    return lines


def suggested_lines(parsed: ParsedFile, topic: str) -> list[int]:
    subtopic_lines = [line for subtopic in subtopic_tags(parsed, topic) for line in parsed.subtopic_lines.get(subtopic, [])]
    evidence = sorted(set(parsed.topic_lines.get(topic, []) + subtopic_lines + relevant_symbol_lines(parsed, topic)))
    if evidence:
        start = max(1, evidence[0] - 20)
        end = min(parsed.line_count, evidence[min(len(evidence) - 1, 4)] + 80)
        if end - start > 180:
            end = min(parsed.line_count, start + 180)
        return [start, end]
    return [1, min(parsed.line_count, 140)]


def example_records(parsed: ParsedFile, tags: list[str]) -> list[dict[str, Any]]:
    if not tags:
        return []
    symbols = sorted({record["name"] for record in parsed.symbols if record["kind"] in {"class", "modded class", "function"}})[:20]
    bases = sorted({record["extends"] for record in parsed.classes if record.get("extends")})[:20]
    records: list[dict[str, Any]] = []
    for topic in tags:
        priority = example_priority(parsed, topic)
        if parsed.generated and priority < 70:
            continue
        if priority < 55:
            continue
        suggested = suggested_lines(parsed, topic)
        subtopics = subtopic_tags(parsed, topic)
        evidence = sorted({item for tag in [topic] + subtopics for item in parsed.evidence.get(tag, set())})[:16]
        records.append(
            {
                "topic": topic,
                "subtopics": subtopics,
                "evidence": evidence,
                "file": parsed.file,
                "module": parsed.module,
                "generated": parsed.generated,
                "symbols": symbols,
                "baseClasses": bases,
                "reason": example_reason(parsed, topic),
                "suggestedLines": suggested,
                "priority": priority,
            }
        )
    return records


def sort_record(record: dict[str, Any]) -> tuple[Any, ...]:
    return (
        record.get("file", ""),
        record.get("line", 0),
        record.get("kind", ""),
        record.get("qualifiedName", record.get("name", record.get("class", ""))),
        record.get("topic", ""),
    )


def build_schema(manifest: dict[str, Any], parsed_files: list[ParsedFile]) -> dict[str, Any]:
    classes = [record for parsed in parsed_files for record in parsed.classes]
    enums = [record for parsed in parsed_files for record in parsed.enums]
    functions = [record for parsed in parsed_files for record in parsed.functions]
    methods = [record for parsed in parsed_files for record in parsed.symbols if record["kind"] == "method"]
    properties = [record for parsed in parsed_files for record in parsed.symbols if record["kind"] == "property"]
    source = game_source(manifest)
    return {
        "generatedAt": deterministic_generated_at(manifest),
        "gameVersion": manifest.get("gameVersion"),
        "buildId": manifest.get("buildId"),
        "source": expected_game_data(manifest),
        "stats": {
            "files": len(parsed_files),
            "classes": len(classes),
            "enums": len(enums),
            "functions": len(functions),
            "methods": len(methods),
            "properties": len(properties),
            "commit": source.get("commit"),
        },
        "classes": sorted(classes, key=sort_record),
        "enums": sorted(enums, key=sort_record),
        "functions": sorted(functions, key=sort_record),
        "methods": sorted(methods, key=sort_record),
        "properties": sorted(properties, key=sort_record),
    }


def build_api_index(schema: dict[str, Any], outputs: dict[str, int]) -> str:
    stats = schema["stats"]
    lines = [
        "# Arma Reforger Game Data Index",
        "",
        "Generated from raw game scripts. Use JSONL indexes for normal Codex lookup; this file is a compact fallback summary.",
        "",
        f"- Build id: `{schema.get('buildId') or 'unknown'}`",
        f"- Commit: `{schema['source'].get('commit') or 'unknown'}`",
        f"- Files: `{stats['files']}`",
        f"- Classes: `{stats['classes']}`",
        f"- Enums: `{stats['enums']}`",
        f"- Functions: `{stats['functions']}`",
        f"- Methods: `{stats['methods']}`",
        f"- Properties: `{stats['properties']}`",
        f"- Symbol records: `{outputs['symbols']}`",
        f"- File records: `{outputs['files']}`",
        f"- Example records: `{outputs['examples']}`",
        f"- Inheritance records: `{outputs['inheritance']}`",
        "",
        "Normal lookup order: `indexes/symbols.jsonl`, `indexes/inheritance.jsonl`, `indexes/examples.jsonl`, `indexes/files.jsonl`, then bounded raw source snippets.",
        "",
    ]
    return "\n".join(lines)


def build_indexes(game_data_root: Path) -> dict[str, int]:
    manifest = validate_inputs(game_data_root)
    scripts_root = game_data_root / "scripts"
    source_files = sorted(scripts_root.rglob("*.c"), key=lambda path: path.relative_to(scripts_root).as_posix().lower())
    if not source_files:
        raise RuntimeError(f"No .c files found under {scripts_root}")

    parsed_files = [parse_file(path, scripts_root) for path in source_files]
    symbols = sorted([record for parsed in parsed_files for record in parsed.symbols], key=sort_record)
    inheritance = sorted([record for parsed in parsed_files for record in parsed.inheritance], key=sort_record)

    file_records: list[dict[str, Any]] = []
    examples: list[dict[str, Any]] = []
    for parsed in parsed_files:
        tags = topic_tags(parsed)
        file_records.append(file_record(parsed, tags))
        examples.extend(example_records(parsed, tags))

    file_records = sorted(file_records, key=lambda record: record["file"].lower())
    examples = sorted(examples, key=lambda record: (-record["priority"], record["topic"], record["file"].lower()))

    outputs = {
        "symbols": len(symbols),
        "files": len(file_records),
        "examples": len(examples),
        "inheritance": len(inheritance),
    }
    schema = build_schema(manifest, parsed_files)
    manifest_out = {
        "generatedAt": deterministic_generated_at(manifest),
        "indexer": {
            "name": INDEXER_NAME,
            "version": INDEXER_VERSION,
            "configVersion": INDEX_CONFIG_VERSION,
        },
        "gameData": expected_game_data(manifest),
        "outputs": outputs,
    }

    write_json(game_data_root / "api-schema.json", schema)
    write_jsonl(game_data_root / "indexes" / "symbols.jsonl", symbols)
    write_jsonl(game_data_root / "indexes" / "files.jsonl", file_records)
    write_jsonl(game_data_root / "indexes" / "examples.jsonl", examples)
    write_jsonl(game_data_root / "indexes" / "inheritance.jsonl", inheritance)
    write_json(game_data_root / "indexes" / "manifest.json", manifest_out)
    (game_data_root / "api-index.md").write_text(build_api_index(schema, outputs), encoding="utf-8", newline="\n")
    return outputs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Index raw Arma Reforger scripts into compact lookup artifacts.")
    parser.add_argument("--skill-root", type=Path, default=ROOT, help="Skill repository root")
    parser.add_argument("--check", action="store_true", help="Check index freshness without writing files")
    parser.add_argument("--if-needed", action="store_true", help="Rebuild only when indexes are missing or stale")
    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> None:
    if args.check and args.if_needed:
        raise RuntimeError("--check and --if-needed cannot be used together")


def main() -> int:
    args = parse_args()
    validate_args(args)
    game_data_root = args.skill_root.resolve() / "raw" / "game-data"

    if args.check:
        try:
            exit_code, status = index_status(game_data_root)
        except Exception as exc:
            print("[reforger-index] status: cannot-determine", file=sys.stderr)
            print(f"[reforger-index] reason: {exc}", file=sys.stderr)
            return EXIT_CANNOT_DETERMINE
        print_status(status)
        return exit_code

    if args.if_needed:
        try:
            exit_code, status = index_status(game_data_root)
        except Exception as exc:
            print("[reforger-index] status: cannot-determine")
            print(f"[reforger-index] reason: {exc}")
            print("[reforger-index] continuing with rebuild")
        else:
            print_status(status)
            if exit_code == EXIT_CURRENT:
                log("Indexes are current; skipping rebuild")
                return EXIT_CURRENT

    log("Building indexes")
    outputs = build_indexes(game_data_root)
    log(
        "Wrote indexes: "
        f"{outputs['symbols']} symbols, {outputs['files']} files, "
        f"{outputs['examples']} examples, {outputs['inheritance']} inheritance records"
    )
    return EXIT_CURRENT


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"[reforger-index] ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
