#!/usr/bin/env python3
"""Build the exhaustive Arma Reforger API fallback reference.

This script is deterministic and uses only raw game API data. It writes:
  references/api-extended.md

api-main.md is intentionally not generated here. It should be curated by Codex
while building the topical references, using official docs plus raw API data.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
API_SCHEMA = ROOT / "raw" / "game-data" / "api-schema.json"
GAME_MANIFEST = ROOT / "raw" / "game-data" / "manifest.json"
REFERENCES_DIR = ROOT / "references"


def load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")
    return json.loads(path.read_text(encoding="utf-8-sig"))


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def clean_doc_lines(lines: Any) -> list[str]:
    cleaned: list[str] = []
    for raw in as_list(lines):
        line = str(raw).strip()
        if not line:
            continue
        line = re.sub(r"^/\*!+", "", line).strip()
        line = re.sub(r"^\*/$", "", line).strip()
        line = re.sub(r"^\* ?", "", line).strip()
        line = re.sub(r"^//! ?", "", line).strip()
        line = re.sub(r"^// ?", "", line).strip()
        if not line or line in {"{", "}", "\\{", "\\}"}:
            continue
        if line.startswith("\\addtogroup"):
            continue
        cleaned.append(line)
    return cleaned


def doc_text(item: dict[str, Any]) -> str:
    text = " ".join(clean_doc_lines(item.get("docs")))
    return re.sub(r"\s+", " ", text).strip()


def modifiers_text(item: dict[str, Any]) -> str:
    return " ".join(str(x) for x in as_list(item.get("modifiers")) if str(x).strip())


def item_signature(item: dict[str, Any]) -> str:
    signature = str(item.get("signature") or "").strip()
    if signature:
        return signature
    name = str(item.get("name") or "").strip()
    return_type = str(item.get("returnType") or "").strip()
    return f"{return_type} {name}".strip()


def source_ref(item: dict[str, Any]) -> str:
    file_name = str(item.get("file") or "").strip()
    line = item.get("line")
    if file_name and line:
        return f"`{file_name}:{line}`"
    if file_name:
        return f"`{file_name}`"
    return "unknown"


def sort_key(item: dict[str, Any]) -> tuple[str, str]:
    return (str(item.get("name") or "").lower(), str(item.get("file") or "").lower())


def write_member(lines: list[str], member: dict[str, Any]) -> None:
    signature = item_signature(member)
    doc = doc_text(member)
    source = source_ref(member)
    parts = []
    if doc:
        parts.append(doc)
    parts.append(source)
    lines.append(f"- `{signature}` - {'; '.join(parts)}")


def write_class(lines: list[str], cls: dict[str, Any]) -> None:
    name = str(cls.get("name") or "Unnamed")
    extends = str(cls.get("extends") or "").strip()
    modifiers = modifiers_text(cls)
    doc = doc_text(cls)
    attributes = [str(x).strip() for x in as_list(cls.get("attributes")) if str(x).strip()]
    properties = sorted(as_list(cls.get("properties")), key=sort_key)
    methods = sorted(as_list(cls.get("methods")), key=sort_key)

    lines.append(f"## {name}")
    lines.append("")
    if doc:
        lines.append(doc)
        lines.append("")
    lines.append(f"- Source: {source_ref(cls)}")
    if extends:
        lines.append(f"- Extends: `{extends}`")
    if modifiers:
        lines.append(f"- Modifiers: `{modifiers}`")
    if attributes:
        lines.append("- Attributes:")
        for attr in attributes:
            lines.append(f"  - `{attr}`")

    if properties:
        lines.append("")
        lines.append("Properties:")
        for prop in properties:
            write_member(lines, prop)

    if methods:
        lines.append("")
        lines.append("Methods:")
        for method in methods:
            write_member(lines, method)

    lines.append("")


def write_enum(lines: list[str], enum: dict[str, Any]) -> None:
    name = str(enum.get("name") or "Unnamed")
    modifiers = modifiers_text(enum)
    attributes = [str(x).strip() for x in as_list(enum.get("attributes")) if str(x).strip()]
    doc = doc_text(enum)

    lines.append(f"## {name}")
    lines.append("")
    if doc:
        lines.append(doc)
        lines.append("")
    lines.append(f"- Source: {source_ref(enum)}")
    if modifiers:
        lines.append(f"- Modifiers: `{modifiers}`")
    if attributes:
        lines.append("- Attributes:")
        for attr in attributes:
            lines.append(f"  - `{attr}`")
    lines.append("")


def write_function(lines: list[str], fn: dict[str, Any]) -> None:
    name = str(fn.get("name") or "Unnamed")
    lines.append(f"## {name}")
    lines.append("")
    write_member(lines, fn)
    lines.append("")


def api_stats(api: dict[str, Any]) -> dict[str, int]:
    classes = as_list(api.get("classes"))
    enums = as_list(api.get("enums"))
    functions = as_list(api.get("functions"))
    return {
        "classes": len(classes),
        "enums": len(enums),
        "functions": len(functions),
        "methods": sum(len(as_list(cls.get("methods"))) for cls in classes),
        "properties": sum(len(as_list(cls.get("properties"))) for cls in classes),
    }


def build_extended_reference(api: dict[str, Any], manifest: dict[str, Any]) -> tuple[str, dict[str, int]]:
    stats = api_stats(api)
    lines: list[str] = [
        "# Arma Reforger API Extended Reference",
        "",
        "This is the exhaustive API fallback generated from raw game script schema. Search this file only when topical references and `api-main.md` do not answer an API question.",
        "",
        "Generated deterministically from `raw/game-data/api-schema.json`.",
        "",
        f"- Game version: `{manifest.get('gameVersion', api.get('gameVersion', 'unknown'))}`",
        f"- Build id: `{manifest.get('buildId', 'unknown')}`",
        f"- Classes: `{stats['classes']}`",
        f"- Enums: `{stats['enums']}`",
        f"- Functions: `{stats['functions']}`",
        f"- Methods: `{stats['methods']}`",
        f"- Properties: `{stats['properties']}`",
        "",
        "# Classes",
        "",
    ]

    for cls in sorted(as_list(api.get("classes")), key=sort_key):
        write_class(lines, cls)

    lines.extend(["# Enums", ""])
    for enum in sorted(as_list(api.get("enums")), key=sort_key):
        write_enum(lines, enum)

    functions = sorted(as_list(api.get("functions")), key=sort_key)
    if functions:
        lines.extend(["# Global Functions", ""])
        for fn in functions:
            write_function(lines, fn)

    return "\n".join(lines).rstrip() + "\n", stats


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the exhaustive Arma Reforger API fallback reference.")
    parser.add_argument("--api-schema", type=Path, default=API_SCHEMA, help="Path to raw/game-data/api-schema.json")
    parser.add_argument("--manifest", type=Path, default=GAME_MANIFEST, help="Path to raw/game-data/manifest.json")
    parser.add_argument("--out-dir", type=Path, default=REFERENCES_DIR, help="Reference output directory")
    parser.add_argument("--dry-run", action="store_true", help="Print output summary without writing files")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    api = load_json(args.api_schema)
    manifest = load_json(args.manifest) if args.manifest.exists() else {}
    text, stats = build_extended_reference(api, manifest)

    if args.dry_run:
        print("Dry run: no files written")
    else:
        args.out_dir.mkdir(parents=True, exist_ok=True)
        output = args.out_dir / "api-extended.md"
        output.write_text(text, encoding="utf-8", newline="\n")
        print(f"Wrote {output}")

    print(f"classes: {stats['classes']}")
    print(f"enums: {stats['enums']}")
    print(f"functions: {stats['functions']}")
    print(f"methods: {stats['methods']}")
    print(f"properties: {stats['properties']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
