#!/usr/bin/env python3
"""Query compact Arma Reforger game-data indexes for Codex lookup."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
GAME_DATA_ROOT = ROOT / "raw" / "game-data"
INDEXES_DIR = GAME_DATA_ROOT / "indexes"
SCRIPTS_ROOT = GAME_DATA_ROOT / "scripts"
DEFAULT_HUMAN_LOG_DIR = ROOT / "generation" / "search-exports"

INDEX_FILES = {
    "symbols": INDEXES_DIR / "symbols.jsonl",
    "files": INDEXES_DIR / "files.jsonl",
    "examples": INDEXES_DIR / "examples.jsonl",
    "inheritance": INDEXES_DIR / "inheritance.jsonl",
    "manifest": INDEXES_DIR / "manifest.json",
}

DEFAULT_LIMITS = {
    "symbol": 20,
    "method": 20,
    "attribute": 20,
    "inherits": 40,
    "examples": 12,
    "files": 30,
    "snippet": 1,
    "lookup": 1,
}

KIND_ORDER = {
    "class": 0,
    "modded class": 1,
    "enum": 2,
    "function": 3,
    "method": 4,
    "property": 5,
}

TASK_RULES = [
    {
        "name": "user-action",
        "keywords": ["user action", "scripteduseraction", "action", "perform action", "can be shown"],
        "symbols": ["ScriptedUserAction", "BaseUserAction"],
        "methods": [("ScriptedUserAction", "PerformAction"), ("ScriptedUserAction", "CanBeShownScript"), ("ScriptedUserAction", "CanBePerformedScript")],
        "inherits": ["ScriptedUserAction"],
        "examples": [("user-action", "scripted-user-action"), ("user-action", "perform-action")],
        "verification": "Verify action registration and dedicated-server behavior in Workbench/runtime; user-action visibility can depend on entity and player context.",
    },
    {
        "name": "replicated-component",
        "keywords": ["replicated component", "replication", "rpl component", "rplprop", "rpc", "network"],
        "symbols": ["RplComponent", "BaseRplComponent", "RplProp", "RplRpc", "ScriptComponent"],
        "methods": [("BaseRplComponent", "RplLoad"), ("BaseRplComponent", "RplSave")],
        "inherits": ["RplComponent", "BaseRplComponent", "ScriptComponent"],
        "examples": [("replication", "rpl-component"), ("replication", "rpl-prop"), ("replication", "rpc")],
        "verification": "Verify authority/proxy paths in multiplayer and dedicated server; API lookup does not prove replication behavior is correct at runtime.",
    },
    {
        "name": "spawn-prefab",
        "keywords": ["spawn prefab", "spawn entity", "prefab", "entityspawnparams", "spawnentityprefab"],
        "symbols": ["PrefabResource", "EntitySpawnParams", "ResourceName"],
        "methods": [("Game", "SpawnEntityPrefab"), ("Resource", "Load")],
        "inherits": [],
        "examples": [("resource-loading", "spawn-prefab"), ("prefab", None)],
        "verification": "Verify resource paths and prefab dependencies in Workbench; spawning behavior can differ by world, authority, and server context.",
    },
    {
        "name": "load-resource",
        "keywords": ["load resource", "resource load", "resourcename", "resource.load", "config resource"],
        "symbols": ["Resource", "ResourceName"],
        "methods": [("Resource", "Load")],
        "inherits": [],
        "examples": [("resource-loading", "resource-load"), ("resource-loading", "resource-picker-config")],
        "verification": "Verify the resource type and path in Workbench; index lookup confirms API names but not asset existence.",
    },
    {
        "name": "workbench-plugin",
        "keywords": ["workbench plugin", "editor plugin", "workbenchplugin", "tool plugin"],
        "symbols": ["WorkbenchPlugin", "WorkbenchPluginAttribute"],
        "methods": [("WorkbenchPlugin", "Run")],
        "inherits": ["WorkbenchPlugin"],
        "examples": [("workbench-plugin", "workbench-plugin"), ("workbench-plugin", "editor-ui")],
        "verification": "Verify plugin menu/command registration in Workbench; generated API signatures do not prove editor integration is visible.",
    },
]


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise RuntimeError(f"Missing required file: {path}")
    value = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(value, dict):
        raise RuntimeError(f"Expected JSON object: {path}")
    return value


def iter_jsonl(path: Path) -> Any:
    if not path.exists():
        raise RuntimeError(f"Missing required index: {path}")
    with path.open("r", encoding="utf-8-sig") as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(line)


def validate_indexes(required: list[str]) -> None:
    missing = [str(INDEX_FILES[name]) for name in required if not INDEX_FILES[name].exists()]
    if missing:
        raise RuntimeError("Missing required indexes: " + ", ".join(missing))


def as_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return " ".join(as_text(item) for item in value)
    return str(value)


def one_line(value: Any, max_len: int = 220) -> str:
    text = re.sub(r"\s+", " ", as_text(value)).strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 3].rstrip() + "..."


def match_score(query: str, values: list[Any]) -> int | None:
    q = query.lower()
    best: int | None = None
    for value in values:
        text = as_text(value).strip()
        if not text:
            continue
        t = text.lower()
        if t == q:
            score = 0
        elif "." in t and t.split(".")[-1] == q:
            score = 1
        elif t.startswith(q):
            score = 2
        elif q in t:
            score = 3
        else:
            continue
        best = score if best is None else min(best, score)
    return best


def exact_value_match(query: str, values: list[Any]) -> bool:
    for value in values:
        if isinstance(value, list):
            if exact_value_match(query, value):
                return True
            continue
        text = as_text(value).strip()
        if text == query:
            return True
    return False


def generated_filter(record: dict[str, Any], args: argparse.Namespace) -> bool:
    generated = bool(record.get("generated"))
    if getattr(args, "generated_only", False) and not generated:
        return False
    if getattr(args, "handwritten_only", False) and generated:
        return False
    return True


def common_record_filter(record: dict[str, Any], args: argparse.Namespace) -> bool:
    if getattr(args, "kind", None) and record.get("kind") != args.kind:
        return False
    if getattr(args, "module", None) and record.get("module") != args.module:
        return False
    if getattr(args, "topic", None):
        topics = record.get("topicTags") or [record.get("topic")]
        if args.topic not in topics:
            return False
    if getattr(args, "subtopic", None):
        subtopics = record.get("subtopics") or []
        if args.subtopic not in subtopics:
            return False
    return generated_filter(record, args)


def limit_for(args: argparse.Namespace) -> int:
    return max(0, int(args.limit if args.limit is not None else DEFAULT_LIMITS[args.command]))


def source_ref(record: dict[str, Any]) -> str:
    file_name = record.get("file") or "unknown"
    line = record.get("line")
    return f"{file_name}:{line}" if line else str(file_name)


def record_title(record: dict[str, Any]) -> str:
    if record.get("qualifiedName"):
        return str(record["qualifiedName"])
    if record.get("class") and record.get("extends"):
        return f"{record['class']} -> {record['extends']}"
    if record.get("file"):
        return str(record["file"])
    return str(record.get("name") or record.get("topic") or "record")


def compact_symbol(record: dict[str, Any]) -> dict[str, Any]:
    keys = [
        "kind",
        "name",
        "owner",
        "qualifiedName",
        "signature",
        "returnType",
        "type",
        "extends",
        "modifiers",
        "attributes",
        "docs",
        "file",
        "line",
        "module",
        "generated",
    ]
    return {key: record[key] for key in keys if key in record and record[key] not in (None, "", [])}


def command_symbol(args: argparse.Namespace) -> tuple[list[dict[str, Any]], int, list[str], list[str]]:
    validate_indexes(["symbols", "manifest"])
    matches: list[tuple[tuple[Any, ...], dict[str, Any]]] = []
    total = 0
    for record in iter_jsonl(INDEX_FILES["symbols"]):
        if not common_record_filter(record, args):
            continue
        if getattr(args, "exact", False) and not exact_value_match(args.name, [record.get("name"), record.get("qualifiedName")]):
            continue
        score = match_score(args.name, [record.get("name"), record.get("qualifiedName"), record.get("owner")])
        if score is None:
            continue
        total += 1
        sort_key = (
            score,
            0 if record.get("generated") else 1,
            KIND_ORDER.get(str(record.get("kind")), 99),
            str(record.get("qualifiedName") or record.get("name")).lower(),
            str(record.get("file")).lower(),
            int(record.get("line") or 0),
        )
        matches.append((sort_key, compact_symbol(record)))
    matches.sort(key=lambda item: item[0])
    return [record for _, record in matches[: limit_for(args)]], total, ["symbols"], []


def command_attribute(args: argparse.Namespace) -> tuple[list[dict[str, Any]], int, list[str], list[str]]:
    validate_indexes(["symbols", "manifest"])
    matches: list[tuple[tuple[Any, ...], dict[str, Any]]] = []
    total = 0
    for record in iter_jsonl(INDEX_FILES["symbols"]):
        if not generated_filter(record, args):
            continue
        is_attribute_class = record.get("kind") in {"class", "modded class"} and record.get("extends") == "UniqueAttribute"
        is_attribute_member = record.get("owner") and exact_value_match(args.name, [record.get("owner")])
        if not (is_attribute_class or is_attribute_member):
            continue
        if getattr(args, "exact", False):
            if not exact_value_match(args.name, [record.get("name"), record.get("qualifiedName"), record.get("owner")]):
                continue
            score = 0
        else:
            score = match_score(args.name, [record.get("name"), record.get("qualifiedName"), record.get("owner")])
            if score is None:
                continue
        total += 1
        sort_key = (
            score,
            KIND_ORDER.get(str(record.get("kind")), 99),
            str(record.get("qualifiedName") or record.get("name")).lower(),
            int(record.get("line") or 0),
        )
        matches.append((sort_key, compact_symbol(record)))
    matches.sort(key=lambda item: item[0])
    return [record for _, record in matches[: limit_for(args)]], total, ["symbols"], []


def command_method(args: argparse.Namespace) -> tuple[list[dict[str, Any]], int, list[str], list[str]]:
    validate_indexes(["symbols", "manifest"])
    owner = args.terms[0] if len(args.terms) == 2 else None
    name = args.terms[-1]
    matches: list[tuple[tuple[Any, ...], dict[str, Any]]] = []
    total = 0
    for record in iter_jsonl(INDEX_FILES["symbols"]):
        if record.get("kind") not in {"method", "function"}:
            continue
        if not common_record_filter(record, args):
            continue
        if owner and str(record.get("owner", "")).lower() != owner.lower():
            continue
        if getattr(args, "exact", False) and not exact_value_match(name, [record.get("name")]):
            continue
        score = match_score(name, [record.get("name"), record.get("qualifiedName")])
        if score is None:
            continue
        total += 1
        sort_key = (
            0 if owner else score,
            score,
            0 if record.get("generated") else 1,
            str(record.get("owner") or "").lower(),
            str(record.get("name") or "").lower(),
            str(record.get("file") or "").lower(),
            int(record.get("line") or 0),
        )
        matches.append((sort_key, compact_symbol(record)))
    matches.sort(key=lambda item: item[0])
    return [record for _, record in matches[: limit_for(args)]], total, ["symbols"], []


def command_inherits(args: argparse.Namespace) -> tuple[list[dict[str, Any]], int, list[str], list[str]]:
    validate_indexes(["inheritance", "manifest"])
    matches: list[tuple[tuple[Any, ...], dict[str, Any]]] = []
    total = 0
    query = args.class_name
    for record in iter_jsonl(INDEX_FILES["inheritance"]):
        if not generated_filter(record, args):
            continue
        class_score = match_score(query, [record.get("class")])
        extends_score = match_score(query, [record.get("extends")])
        if class_score is None and extends_score is None:
            continue
        relation = "base" if class_score is not None and class_score <= (extends_score or 99) else "derived"
        score = class_score if relation == "base" else extends_score
        total += 1
        item = dict(record)
        item["relation"] = relation
        sort_key = (
            score,
            0 if relation == "base" else 1,
            0 if not record.get("generated") else 1,
            str(record.get("class") or "").lower(),
            str(record.get("file") or "").lower(),
        )
        matches.append((sort_key, item))
    matches.sort(key=lambda item: item[0])
    return [record for _, record in matches[: limit_for(args)]], total, ["inheritance"], []


def command_examples(args: argparse.Namespace) -> tuple[list[dict[str, Any]], int, list[str], list[str]]:
    validate_indexes(["examples", "manifest"])
    matches: list[tuple[tuple[Any, ...], dict[str, Any]]] = []
    total = 0
    for record in iter_jsonl(INDEX_FILES["examples"]):
        if not common_record_filter(record, args):
            continue
        score = match_score(args.topic_name, [record.get("topic"), record.get("subtopics"), record.get("file"), record.get("symbols"), record.get("baseClasses"), record.get("evidence")])
        if score is None:
            continue
        total += 1
        sort_key = (
            score,
            -int(record.get("priority") or 0),
            0 if not record.get("generated") else 1,
            str(record.get("file") or "").lower(),
        )
        matches.append((sort_key, record))
    matches.sort(key=lambda item: item[0])
    records = [record for _, record in matches[: limit_for(args)]]
    if getattr(args, "with_snippets", False):
        attach_example_snippets(records, max_records=3, max_lines=60)
    return records, total, ["examples"], []


def command_files(args: argparse.Namespace) -> tuple[list[dict[str, Any]], int, list[str], list[str]]:
    validate_indexes(["files", "manifest"])
    matches: list[tuple[tuple[Any, ...], dict[str, Any]]] = []
    total = 0
    for record in iter_jsonl(INDEX_FILES["files"]):
        if not common_record_filter(record, args):
            continue
        exact_values = [
            record.get("file"),
            Path(str(record.get("file") or "")).name,
            record.get("module"),
            record.get("declaredSymbols"),
            record.get("baseClasses"),
            record.get("topicTags"),
            record.get("subtopics"),
            record.get("evidence"),
        ]
        if getattr(args, "exact", False) and not exact_value_match(args.query, exact_values):
            continue
        score = match_score(
            args.query,
            [
                *exact_values,
                record.get("searchText"),
            ],
        )
        if score is None:
            continue
        total += 1
        sort_key = (
            score,
            0 if not record.get("generated") else 1,
            str(record.get("file") or "").lower(),
        )
        matches.append((sort_key, record))
    matches.sort(key=lambda item: item[0])
    return [record for _, record in matches[: limit_for(args)]], total, ["files"], []


def normalize_snippet_path(user_path: str) -> Path:
    raw = Path(user_path)
    text = user_path.replace("\\", "/")
    if text.startswith("raw/game-data/scripts/"):
        rel = text[len("raw/game-data/") :]
    elif text.startswith("scripts/"):
        rel = text
    else:
        rel = raw.as_posix()
    candidate = (GAME_DATA_ROOT / rel).resolve()
    scripts_root = SCRIPTS_ROOT.resolve()
    try:
        candidate.relative_to(scripts_root)
    except ValueError as exc:
        raise RuntimeError(f"Snippet path must be under raw/game-data/scripts: {user_path}") from exc
    if not candidate.exists() or not candidate.is_file():
        raise RuntimeError(f"Snippet file does not exist: {user_path}")
    return candidate


def command_snippet(args: argparse.Namespace) -> tuple[list[dict[str, Any]], int, list[str], list[str]]:
    validate_indexes(["manifest"])
    path = normalize_snippet_path(args.file)
    lines = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    if args.line < 1 or args.line > len(lines):
        raise RuntimeError(f"Line {args.line} is outside file range 1-{len(lines)}")
    context = max(0, int(args.context))
    start = max(1, args.line - context)
    end = min(len(lines), args.line + context)
    if end - start + 1 > 100:
        half = 49
        start = max(1, args.line - half)
        end = min(len(lines), start + 99)
    normalized = path.relative_to(GAME_DATA_ROOT).as_posix()
    excerpt = [{"line": number, "text": lines[number - 1]} for number in range(start, end + 1)]
    record = {
        "file": normalized,
        "requestedLine": args.line,
        "startLine": start,
        "endLine": end,
        "totalLines": len(lines),
        "excerpt": excerpt,
    }
    return [record], 1, ["raw-source"], []


def bounded_source_excerpt(file_name: str, line_range: list[int] | tuple[int, int] | None, max_lines: int) -> dict[str, Any] | None:
    if not file_name:
        return None
    path = normalize_snippet_path(file_name)
    lines = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    if line_range and len(line_range) == 2:
        start = max(1, int(line_range[0]))
        end = min(len(lines), int(line_range[1]))
    else:
        start = 1
        end = min(len(lines), max_lines)
    if end < start:
        return None
    if end - start + 1 > max_lines:
        end = start + max_lines - 1
    excerpt = [{"line": number, "text": lines[number - 1]} for number in range(start, end + 1)]
    return {
        "file": file_name,
        "startLine": start,
        "endLine": end,
        "excerpt": excerpt,
    }


def attach_example_snippets(records: list[dict[str, Any]], max_records: int, max_lines: int) -> None:
    for record in records[:max_records]:
        try:
            snippet = bounded_source_excerpt(str(record.get("file") or ""), record.get("suggestedLines"), max_lines)
        except RuntimeError:
            snippet = None
        if snippet:
            record["snippet"] = snippet


def make_query_args(command: str, **values: Any) -> argparse.Namespace:
    defaults = {
        "command": command,
        "json": False,
        "limit": None,
        "kind": None,
        "module": None,
        "topic": None,
        "subtopic": None,
        "generated_only": False,
        "handwritten_only": False,
        "exact": False,
        "human_log": False,
        "human_log_dir": None,
        "with_snippets": False,
    }
    defaults.update(values)
    return argparse.Namespace(**defaults)


def unique_records(records: list[dict[str, Any]], keys: list[str], limit: int) -> list[dict[str, Any]]:
    seen: set[tuple[Any, ...]] = set()
    unique: list[dict[str, Any]] = []
    for record in records:
        identity = tuple(record.get(key) for key in keys)
        if identity in seen:
            continue
        seen.add(identity)
        unique.append(record)
        if len(unique) >= limit:
            break
    return unique


def task_score(query: str, rule: dict[str, Any]) -> int:
    lowered = query.lower()
    score = 0
    for keyword in rule["keywords"]:
        key = keyword.lower()
        if key == lowered:
            score += 100
        elif key in lowered:
            score += 25 + len(key)
        else:
            parts = [part for part in re.split(r"[^a-z0-9]+", key) if part]
            if parts and all(part in lowered for part in parts):
                score += 10 + len(parts)
    return score


def select_task_rule(query: str) -> tuple[dict[str, Any], list[str]]:
    ranked = sorted(((task_score(query, rule), rule) for rule in TASK_RULES), key=lambda item: (-item[0], item[1]["name"]))
    warnings: list[str] = []
    if not ranked or ranked[0][0] <= 0:
        warnings.append("no task rule matched exactly; using broad resource/API lookup")
        return TASK_RULES[0], warnings
    return ranked[0][1], warnings


def command_lookup(args: argparse.Namespace) -> tuple[list[dict[str, Any]], int, list[str], list[str]]:
    validate_indexes(["symbols", "inheritance", "examples", "manifest"])
    rule, warnings = select_task_rule(args.query)
    api: list[dict[str, Any]] = []
    methods: list[dict[str, Any]] = []
    inheritance: list[dict[str, Any]] = []
    examples: list[dict[str, Any]] = []

    for symbol in rule["symbols"]:
        found, _total, _indexes, _warnings = command_symbol(make_query_args("symbol", name=symbol, exact=True, limit=3))
        api.extend(found)
    for owner, method in rule["methods"]:
        found, _total, _indexes, _warnings = command_method(make_query_args("method", terms=[owner, method], exact=True, limit=3))
        methods.extend(found)
    for class_name in rule["inherits"]:
        found, _total, _indexes, _warnings = command_inherits(make_query_args("inherits", class_name=class_name, limit=8))
        inheritance.extend(found)
    for topic, subtopic in rule["examples"]:
        found, _total, _indexes, _warnings = command_examples(
            make_query_args("examples", topic_name=topic, subtopic=subtopic, handwritten_only=True, limit=4, with_snippets=False)
        )
        examples.extend(found)

    api = unique_records(api, ["kind", "qualifiedName", "name", "owner"], 10)
    methods = unique_records(methods, ["kind", "qualifiedName", "name", "owner"], 10)
    inheritance = unique_records(inheritance, ["class", "extends"], 12)
    dedup_examples: dict[str, dict[str, Any]] = {}
    for example in examples:
        key = f"{example.get('topic')}:{example.get('file')}"
        current = dedup_examples.get(key)
        if current is None or int(example.get("priority") or 0) > int(current.get("priority") or 0):
            dedup_examples[key] = example
    examples = sorted(dedup_examples.values(), key=lambda record: (-int(record.get("priority") or 0), str(record.get("file") or "").lower()))[: limit_for(make_query_args("examples", limit=8))]
    if getattr(args, "with_snippets", False):
        attach_example_snippets(examples, max_records=3, max_lines=60)

    snippet_commands = []
    for example in examples[:5]:
        lines = example.get("suggestedLines") or [1, 1]
        line = lines[0] if isinstance(lines, list) and lines else 1
        snippet_commands.append(f"py -3 scripts/query-reforger-data.py snippet {example.get('file')} --line {line} --context 30")

    record = {
        "query": args.query,
        "matchedTask": rule["name"],
        "apiSymbols": api,
        "methods": methods,
        "inheritance": inheritance,
        "examples": examples,
        "suggestedSnippetCommands": snippet_commands,
        "verification": rule["verification"],
    }
    return [record], 1, ["symbols", "inheritance", "examples"], warnings


def text_symbol(record: dict[str, Any]) -> list[str]:
    lines = [f"{record.get('kind', 'symbol')} {record_title(record)}"]
    detail = record.get("signature") or (f"type: {record.get('type')}" if record.get("type") else "")
    if detail:
        lines.append(f"  signature: {detail}")
    if record.get("extends"):
        lines.append(f"  extends: {record['extends']}")
    if record.get("modifiers"):
        lines.append(f"  modifiers: {', '.join(record['modifiers'])}")
    if record.get("attributes"):
        lines.append(f"  attributes: {one_line(record['attributes'])}")
    if record.get("docs"):
        lines.append(f"  docs: {one_line(record['docs'])}")
    lines.append(f"  source: {source_ref(record)}")
    lines.append(f"  generated: {str(bool(record.get('generated'))).lower()}")
    return lines


def text_example(record: dict[str, Any]) -> list[str]:
    lines = [
        f"example {record.get('topic')} priority={record.get('priority')}",
        f"  file: {record.get('file')}",
        f"  lines: {record.get('suggestedLines')}",
        f"  subtopics: {', '.join(record.get('subtopics') or [])}",
        f"  evidence: {', '.join(record.get('evidence') or [])}",
        f"  symbols: {', '.join(record.get('symbols') or [])}",
        f"  bases: {', '.join(record.get('baseClasses') or [])}",
        f"  reason: {record.get('reason')}",
        f"  generated: {str(bool(record.get('generated'))).lower()}",
    ]
    if record.get("snippet"):
        snippet = record["snippet"]
        lines.append(f"  snippet: {snippet['file']}:{snippet['startLine']}-{snippet['endLine']}")
    return lines


def text_file(record: dict[str, Any]) -> list[str]:
    return [
        f"file {record.get('file')}",
        f"  module: {record.get('module')} generated: {str(bool(record.get('generated'))).lower()} lines: {record.get('lineCount')}",
        f"  symbols: {', '.join((record.get('declaredSymbols') or [])[:12])}",
        f"  bases: {', '.join((record.get('baseClasses') or [])[:12])}",
        f"  topics: {', '.join(record.get('topicTags') or [])}",
        f"  subtopics: {', '.join(record.get('subtopics') or [])}",
        f"  evidence: {', '.join((record.get('evidence') or [])[:12])}",
    ]


def text_inheritance(record: dict[str, Any]) -> list[str]:
    return [
        f"{record.get('class')} -> {record.get('extends')} ({record.get('relation')})",
        f"  source: {source_ref(record)}",
        f"  generated: {str(bool(record.get('generated'))).lower()}",
    ]


def text_snippet(record: dict[str, Any]) -> list[str]:
    lines = [f"snippet {record['file']}:{record['startLine']}-{record['endLine']}"]
    width = len(str(record["endLine"]))
    for item in record["excerpt"]:
        lines.append(f"{item['line']:>{width}} | {item['text']}")
    return lines


def text_lookup(record: dict[str, Any]) -> list[str]:
    lines = [
        f"lookup {record.get('matchedTask')} for: {record.get('query')}",
        f"  verification: {record.get('verification')}",
        "  api symbols:",
    ]
    for item in record.get("apiSymbols") or []:
        lines.append(f"    - {record_title(item)} :: {item.get('signature') or item.get('extends') or item.get('type') or source_ref(item)}")
    lines.append("  methods:")
    for item in record.get("methods") or []:
        lines.append(f"    - {record_title(item)} :: {item.get('signature') or source_ref(item)}")
    lines.append("  inheritance:")
    for item in record.get("inheritance") or []:
        lines.append(f"    - {item.get('class')} -> {item.get('extends')} ({source_ref(item)})")
    lines.append("  examples:")
    for item in record.get("examples") or []:
        subtopics = ", ".join(item.get("subtopics") or [])
        lines.append(f"    - {item.get('file')} lines {item.get('suggestedLines')} topic={item.get('topic')} subtopics={subtopics}")
    lines.append("  suggested snippets:")
    for command in record.get("suggestedSnippetCommands") or []:
        lines.append(f"    - {command}")
    return lines


def render_text(command: str, records: list[dict[str, Any]], total: int, warnings: list[str]) -> str:
    lines = [f"[reforger-query] matches: {len(records)} returned / {total} total"]
    for warning in warnings:
        lines.append(f"[reforger-query] warning: {warning}")
    if not records:
        lines.append("[reforger-query] no matches")
        return "\n".join(lines) + "\n"
    for index, record in enumerate(records, start=1):
        lines.append("")
        lines.append(f"{index}.")
        if command in {"symbol", "method", "attribute"}:
            lines.extend(text_symbol(record))
        elif command == "inherits":
            lines.extend(text_inheritance(record))
        elif command == "examples":
            lines.extend(text_example(record))
        elif command == "files":
            lines.extend(text_file(record))
        elif command == "snippet":
            lines.extend(text_snippet(record))
        elif command == "lookup":
            lines.extend(text_lookup(record))
    return "\n".join(lines) + "\n"


def metadata(args: argparse.Namespace, indexes_scanned: list[str], total: int, warnings: list[str]) -> dict[str, Any]:
    manifest = load_json(INDEX_FILES["manifest"]) if INDEX_FILES["manifest"].exists() else {}
    game_data = manifest.get("gameData") if isinstance(manifest.get("gameData"), dict) else {}
    return {
        "command": args.command,
        "argv": sys.argv[1:],
        "cwd": str(Path.cwd()),
        "gameDataCommit": game_data.get("commit"),
        "indexesScanned": indexes_scanned,
        "totalMatches": total,
        "returned": None,
        "limit": getattr(args, "limit", None) if getattr(args, "limit", None) is not None else DEFAULT_LIMITS.get(args.command),
        "filters": {
            "kind": getattr(args, "kind", None),
            "module": getattr(args, "module", None),
            "topic": getattr(args, "topic", None),
            "subtopic": getattr(args, "subtopic", None),
            "exact": getattr(args, "exact", False),
            "generatedOnly": getattr(args, "generated_only", False),
            "handwrittenOnly": getattr(args, "handwritten_only", False),
            "withSnippets": getattr(args, "with_snippets", False),
        },
        "warnings": warnings,
    }


def render_json(args: argparse.Namespace, records: list[dict[str, Any]], total: int, indexes_scanned: list[str], warnings: list[str]) -> str:
    meta = metadata(args, indexes_scanned, total, warnings)
    meta["returned"] = len(records)
    return json.dumps({"meta": meta, "records": records}, ensure_ascii=False, indent=2) + "\n"


def sanitize_filename_part(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip())[:80].strip("-")
    return value or "query"


def write_human_log(args: argparse.Namespace, records: list[dict[str, Any]], total: int, indexes_scanned: list[str], warnings: list[str], text_output: str) -> Path:
    out_dir = Path(args.human_log_dir or DEFAULT_HUMAN_LOG_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    query_parts = []
    for attr in ("name", "terms", "class_name", "topic_name", "query", "file"):
        value = getattr(args, attr, None)
        if value:
            query_parts.append("-".join(value) if isinstance(value, list) else str(value))
    filename = f"{stamp}-{args.command}-{sanitize_filename_part('-'.join(query_parts))}.md"
    path = out_dir / filename

    meta = metadata(args, indexes_scanned, total, warnings)
    meta["returned"] = len(records)
    lines = [
        "# Reforger Search Export",
        "",
        "Human review artifact only. The query script does not read this file, indexes do not depend on it, and Codex must not use it as source truth.",
        "",
        "## Inputs",
        "",
        f"- Command: `{args.command}`",
        f"- Command line: `py -3 scripts/query-reforger-data.py {' '.join(sys.argv[1:])}`",
        f"- Working directory: `{Path.cwd()}`",
        f"- Game-data commit: `{meta.get('gameDataCommit') or 'unknown'}`",
        f"- Indexes scanned: `{', '.join(indexes_scanned)}`",
        f"- Limit: `{meta.get('limit')}`",
        f"- Filters: `{json.dumps(meta['filters'], sort_keys=True)}`",
        "",
        "## Results",
        "",
        f"- Total matches before limit: `{total}`",
        f"- Returned results: `{len(records)}`",
    ]
    if warnings:
        lines.extend(["", "## Warnings", ""])
        lines.extend(f"- {warning}" for warning in warnings)
    lines.extend(["", "## Output", "", "```text", text_output.rstrip(), "```", ""])
    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return path


def add_common_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    parser.add_argument("--limit", type=int, default=None, help="Maximum returned records")
    parser.add_argument("--kind", help="Filter symbol kind")
    parser.add_argument("--module", help="Filter module")
    parser.add_argument("--topic", help="Filter topic")
    parser.add_argument("--subtopic", help="Filter subtopic")
    parser.add_argument("--generated-only", action="store_true", help="Only generated records")
    parser.add_argument("--handwritten-only", action="store_true", help="Only handwritten records")
    parser.add_argument("--exact", action="store_true", help="Require exact name/owner/path matches where supported")
    parser.add_argument("--human-log", action="store_true", help="Write a human-only Markdown query export")
    parser.add_argument("--human-log-dir", type=Path, default=None, help="Human log output directory")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Query compact Arma Reforger game-data indexes.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    symbol = subparsers.add_parser("symbol", help="Find classes, enums, functions, methods, and properties")
    symbol.add_argument("name")
    add_common_options(symbol)

    method = subparsers.add_parser("method", help="Find method/function signatures")
    method.add_argument("terms", nargs="+", help="Either <method> or <owner> <method>")
    add_common_options(method)

    attribute = subparsers.add_parser("attribute", help="Find attribute classes and members")
    attribute.add_argument("name")
    add_common_options(attribute)

    inherits = subparsers.add_parser("inherits", help="Find base/derived class relationships")
    inherits.add_argument("class_name")
    add_common_options(inherits)

    examples = subparsers.add_parser("examples", help="Find implementation examples by topic")
    examples.add_argument("topic_name")
    add_common_options(examples)
    examples.add_argument("--with-snippets", action="store_true", help="Attach hard-bounded snippets to top example results")

    files = subparsers.add_parser("files", help="Find source files by symbol, topic, module, or path text")
    files.add_argument("query")
    add_common_options(files)

    snippet = subparsers.add_parser("snippet", help="Show bounded line-numbered raw source")
    snippet.add_argument("file")
    snippet.add_argument("--line", type=int, required=True)
    snippet.add_argument("--context", type=int, default=20)
    snippet.add_argument("--json", action="store_true", help="Emit JSON output")
    snippet.add_argument("--limit", type=int, default=None, help=argparse.SUPPRESS)
    snippet.add_argument("--human-log", action="store_true", help="Write a human-only Markdown query export")
    snippet.add_argument("--human-log-dir", type=Path, default=None, help="Human log output directory")

    lookup = subparsers.add_parser("lookup", help="Return a bounded task-oriented API/example lookup bundle")
    lookup.add_argument("query")
    lookup.add_argument("--json", action="store_true", help="Emit JSON output")
    lookup.add_argument("--limit", type=int, default=None, help=argparse.SUPPRESS)
    lookup.add_argument("--with-snippets", action="store_true", help="Attach hard-bounded snippets to top example results")
    lookup.add_argument("--human-log", action="store_true", help="Write a human-only Markdown query export")
    lookup.add_argument("--human-log-dir", type=Path, default=None, help="Human log output directory")

    args = parser.parse_args()
    if getattr(args, "generated_only", False) and getattr(args, "handwritten_only", False):
        raise RuntimeError("--generated-only and --handwritten-only cannot be combined")
    if args.command == "method" and len(args.terms) not in {1, 2}:
        raise RuntimeError("method expects either <method> or <owner> <method>")
    return args


def dispatch(args: argparse.Namespace) -> tuple[list[dict[str, Any]], int, list[str], list[str]]:
    if args.command == "symbol":
        return command_symbol(args)
    if args.command == "method":
        return command_method(args)
    if args.command == "attribute":
        return command_attribute(args)
    if args.command == "inherits":
        return command_inherits(args)
    if args.command == "examples":
        return command_examples(args)
    if args.command == "files":
        return command_files(args)
    if args.command == "snippet":
        return command_snippet(args)
    if args.command == "lookup":
        return command_lookup(args)
    raise RuntimeError(f"Unknown command: {args.command}")


def main() -> int:
    args = parse_args()
    records, total, indexes_scanned, warnings = dispatch(args)
    text_output = render_text(args.command, records, total, warnings)
    if args.human_log:
        log_path = write_human_log(args, records, total, indexes_scanned, warnings, text_output)
        warnings.append(f"human log written: {log_path}")
        text_output = render_text(args.command, records, total, warnings)
    if args.json:
        print(render_json(args, records, total, indexes_scanned, warnings), end="")
    else:
        print(text_output, end="")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"[reforger-query] ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
