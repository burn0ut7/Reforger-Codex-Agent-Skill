#!/usr/bin/env python3
"""Index cached Arma Reforger wiki docs for complete doc generation.

This script does not scrape the web and does not build runtime references. It
reads raw/wiki-docs produced by update-reforger-wiki-docs.py and writes a
generation-only source pack that preserves all useful wiki content.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse


INDEXER_VERSION = 3
INDEX_CONFIG_VERSION = 3
DEFAULT_RAW_DIR = "raw/wiki-docs"
DEFAULT_OUT_DIR = "generation/wiki-index"
CHUNK_TARGET_CHARS = 2200
CHUNK_OVERLAP_CHARS = 180

TOPIC_RULES: dict[str, tuple[str, ...]] = {
    "overview": ("modding", "getting started", "directory structure", "data modding", "game identity", "addon", "workbench"),
    "scripting": ("scripting", "script", "enfusion", "enforce", "class", "modded", "component", "attribute", "event", "callback"),
    "entity-component": ("entity", "component", "prefab", "lifecycle", "event mask", "transform", "activeness"),
    "networking": ("multiplayer", "replication", "rpl", "rpc", "authority", "proxy", "owner", "jip", "network"),
    "resources-prefabs-configs": ("resource manager", "resource", "prefab", "config", "catalog", "resourcename", "layout", "basecontainer"),
    "workbench-debugging": ("workbench", "plugin", "debug", "diag", "profiler", "resource manager", "script editor", "world editor"),
    "scenario-game-master": ("scenario framework", "scenario", "game master", "faction", "task", "layer", "gamemode", "conflict"),
    "terrain-world-editor": ("terrain", "world editor", "road", "river", "navmesh", "heightmap", "world", "generator"),
    "assets": ("asset", "assets", "import", "material", "lod", "collision", "model", "texture", "blender"),
    "weapons": ("weapon", "muzzle", "magazine", "ammo", "ballistic", "reload", "optic", "suppressor"),
    "vehicles": ("vehicle", "car", "compartment", "turret", "wheel", "physics", "driver"),
    "animation": ("animation", "anim", "animgraph", "graph", "character command", "state machine"),
    "audio": ("audio", "sound", "soundevent", "signal", "voiceover", "music", "occlusion"),
    "ai": ("ai", "behavior", "navmesh", "waypoint", "perception", "commanding"),
    "ui": ("ui", "hud", "dialog", "menu", "layout", "widget", "interface"),
    "configs": ("config", "configs", "basecontainer", "json", "parameters", "template"),
    "prefabs": ("prefab", "prefabs", "component", "inherit", "override", "entity catalog"),
    "packaging": ("workshop", "publishing", "package", "addon", "gproj", "mod project", "build"),
    "server-runtime": ("server", "dedicated", "startup", "hosting", "rcon", "a2s", "config", "maxfps"),
    "samples-examples": ("sample", "samples", "example", "tutorial", "walkthrough", "template"),
}

TERM_RULES: tuple[str, ...] = tuple(sorted({term for terms in TOPIC_RULES.values() for term in terms}))
TOKEN_BOUNDARY = r"(?<![a-z0-9]){}(?![a-z0-9])"

ADMONITION_WORDS = (
    "warning",
    "important",
    "caution",
    "attention",
    "note",
    "must",
    "required",
    "requires",
    "recommended",
    "do not",
    "cannot",
)

PROCEDURE_WORDS = (
    "open",
    "select",
    "click",
    "create",
    "add",
    "set",
    "configure",
    "save",
    "export",
    "import",
    "build",
    "run",
    "enable",
    "disable",
)

WIKI_BASE_URL = "https://community.bistudio.com"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def normalize_match_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def term_pattern(term: str) -> re.Pattern:
    pieces = [re.escape(piece) for piece in normalize_match_text(term).split()]
    body = r"[\s_-]+".join(pieces)
    return re.compile(TOKEN_BOUNDARY.format(body))


TERM_PATTERNS: dict[str, re.Pattern] = {term: term_pattern(term) for term in TERM_RULES}


def term_count(text: str, term: str) -> int:
    normalized = normalize_match_text(text)
    return len(TERM_PATTERNS[term].findall(normalized))


def term_present(text: str, term: str) -> bool:
    return term_count(text, term) > 0


def stable_id(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:10]
    if slug:
        return f"{slug[:80]}-{digest}"
    return digest


def text_hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def json_dump_line(record: dict) -> str:
    return json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.write_text("\n".join(json_dump_line(record) for record in records) + ("\n" if records else ""), encoding="utf-8")


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON: {path}") from exc


def normalize_url(url: str, base_url: str = "", keep_fragment: bool = True) -> str:
    if not url:
        return ""
    if base_url:
        url = urljoin(base_url, url)
    parsed = urlparse(url)
    if not parsed.scheme:
        url = urljoin(WIKI_BASE_URL, url)
        parsed = urlparse(url)
    path = unquote(parsed.path).replace(" ", "_")
    fragment = parsed.fragment if keep_fragment else ""
    return parsed._replace(path=path, fragment=fragment).geturl()


def load_raw_cache(raw_dir: Path) -> tuple[dict, dict, list[dict]]:
    schema_path = raw_dir / "schema.json"
    pages_dir = raw_dir / "pages"
    manifest_path = raw_dir / "manifest.json"
    if not schema_path.exists():
        raise FileNotFoundError(f"Missing wiki schema: {schema_path}")
    if not pages_dir.exists():
        raise FileNotFoundError(f"Missing wiki pages directory: {pages_dir}")

    schema = read_json(schema_path)
    manifest = read_json(manifest_path) if manifest_path.exists() else {}
    pages = []
    for page_path in sorted(pages_dir.glob("*.json")):
        page = read_json(page_path)
        page["_pageJson"] = page_path.name
        pages.append(page)
    return schema, manifest, pages


def canonicalize_pages(raw_pages: list[dict]) -> tuple[list[dict], dict[str, str]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for page in raw_pages:
        key = normalize_url(page.get("url") or page.get("_pageJson", ""), keep_fragment=False)
        grouped[key].append(page)

    canonical_pages = []
    alias_map: dict[str, str] = {}
    for url, group in sorted(grouped.items(), key=lambda item: item[0]):
        group.sort(key=lambda page: (-(len(page.get("markdown") or "")), page.get("title") or "", page.get("_pageJson") or ""))
        primary = group[0]
        page_id = stable_id(url or primary.get("_pageJson", "page"))
        aliases = []
        for page in group:
            alias_map[page.get("_pageJson", "")] = page_id
            aliases.append(
                {
                    "title": page.get("title") or "",
                    "url": normalize_url(page.get("url") or "", keep_fragment=False),
                    "jsonPath": page.get("jsonPath"),
                    "jsonFile": page.get("_pageJson"),
                    "markdownPath": page.get("markdownPath"),
                    "htmlPath": page.get("htmlPath"),
                    "textLength": page.get("textLength") or len(page.get("text") or ""),
                    "contentHash": text_hash(page.get("markdown") or page.get("text") or ""),
                }
            )
        canonical = dict(primary)
        canonical["_canonicalId"] = page_id
        canonical["_canonicalUrl"] = url
        canonical["_aliases"] = aliases
        canonical_pages.append(canonical)
    return canonical_pages, alias_map


def split_sections(markdown: str) -> list[dict]:
    sections: list[dict] = []
    stack: list[tuple[int, str]] = []
    current_heading = "Page"
    current_level = 1
    current_lines: list[str] = []
    current_start_line = 1
    line_number = 0

    def flush(end_line: int) -> None:
        markdown_text = "\n".join(current_lines).strip()
        if not markdown_text:
            return
        heading_path = [heading for _level, heading in stack] or [current_heading]
        sections.append(
            {
                "heading": current_heading,
                "headingPath": heading_path,
                "level": current_level,
                "startLine": current_start_line,
                "endLine": end_line,
                "markdown": markdown_text,
                "text": markdown_to_text(markdown_text),
            }
        )

    for line in markdown.splitlines():
        line_number += 1
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not match:
            current_lines.append(line)
            continue

        flush(line_number - 1)
        current_lines = []
        current_level = len(match.group(1))
        current_heading = normalize_space(match.group(2).strip("# "))
        current_start_line = line_number + 1
        stack = [(level, heading) for level, heading in stack if level < current_level]
        stack.append((current_level, current_heading))

    flush(line_number)
    return sections


def markdown_to_text(markdown: str) -> str:
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", markdown)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"[*_~#>|]+", " ", text)
    return normalize_space(text)


def matched_terms(text: str, terms: tuple[str, ...] = TERM_RULES) -> list[str]:
    return [term for term in terms if term_present(text, term)]


def page_family(page: dict) -> str:
    title = (page.get("title") or "").replace(" – Arma Reforger", "").replace(" â€“ Arma Reforger", "")
    if "/" in title:
        return title.split("/", 1)[0].strip()
    if ":" in title:
        return title.split(":", 1)[0].strip()
    path = unquote(urlparse(page.get("_canonicalUrl") or page.get("url") or "").path)
    if ":" in path:
        name = path.rsplit(":", 1)[-1]
        return name.split("/", 1)[0].replace("_", " ")
    return title


def category_path(page: dict) -> list[str]:
    # The scraper records the actual MediaWiki category memberships for pages,
    # which is more useful than inferring a hierarchy from a page's own URL.
    recorded_paths = page.get("categoryPaths") or []
    if recorded_paths:
        return list(recorded_paths[0])

    url = page.get("_canonicalUrl") or page.get("url") or ""
    path = unquote(urlparse(url).path)
    if "/Category:" not in path:
        return []
    category = path.split("/Category:", 1)[1].replace("_", " ")
    return [part for part in category.split("/") if part]


def topic_scores(text: str, page: dict | None = None, heading_weight: int = 1) -> dict[str, int]:
    scores: dict[str, int] = {}
    title_boost = ""
    category_boost = ""
    if page:
        title_boost = f"{page.get('title','')} {page_family(page)}"
        category_boost = " ".join(category_path(page))
    for topic, terms in TOPIC_RULES.items():
        score = 0
        for term in terms:
            count = term_count(text, term)
            if count:
                score += 1 + min(count, 12)
            if title_boost and term_present(title_boost, term):
                score += 14 * heading_weight
            if category_boost and term_present(category_boost, term):
                score += 8 * heading_weight
        if score:
            scores[topic] = score
    return dict(sorted(scores.items(), key=lambda item: (-item[1], item[0])))


def split_topics(scores: dict[str, int]) -> tuple[list[str], list[str]]:
    if not scores:
        return [], []
    top_score = max(scores.values())
    primary_floor = max(12, int(top_score * 0.45))
    primary = [topic for topic, score in scores.items() if score >= primary_floor]
    related = [topic for topic in scores if topic not in primary]
    return primary, related


def extract_links(markdown: str, page: dict, section: dict | None = None) -> list[dict]:
    records = []
    seen = set()
    base_url = page.get("_canonicalUrl") or page.get("url") or ""

    def add_link(label: str, raw_url: str, position: int) -> None:
        label = normalize_space(label)
        if not label:
            label = "image link"
        url = normalize_url(raw_url.strip(), base_url)
        key = (label, url, position)
        if key in seen:
            return
        seen.add(key)
        base = context_record(page, section)
        base.update(
            {
                "label": label,
                "url": url,
                "rawUrl": raw_url.strip(),
                "isInternalWiki": "community.bistudio.com/wiki/" in url,
                "kind": "link",
                "linkKind": link_kind(raw_url.strip(), url),
                "terms": matched_terms(f"{label} {url}")[:20],
            }
        )
        records.append(base)

    for match in re.finditer(r"\[(!\[[^\]]*\]\([^)]+\))\]\(([^)]+)\)", markdown):
        media_label = re.search(r"!\[([^\]]*)\]", match.group(1))
        add_link(media_label.group(1) if media_label else "image link", match.group(2), match.start())

    markdown_without_media = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", markdown)
    for match in re.finditer(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)", markdown_without_media):
        label = normalize_space(match.group(1))
        if not label:
            continue
        url = normalize_url(match.group(2).strip(), page.get("_canonicalUrl") or page.get("url") or "")
        key = (label, url, match.start())
        if key in seen:
            continue
        seen.add(key)
        base = context_record(page, section)
        base.update(
            {
                "label": label,
                "url": url,
                "rawUrl": match.group(2).strip(),
                "isInternalWiki": "community.bistudio.com/wiki/" in url,
                "kind": "link",
                "linkKind": link_kind(match.group(2).strip(), url),
                "terms": matched_terms(f"{label} {url}")[:20],
            }
        )
        records.append(base)
    return records


def link_kind(raw_url: str, normalized_url: str) -> str:
    if raw_url.startswith("#") or normalized_url.startswith("#"):
        return "anchor"
    if raw_url.startswith("enfusion://") or normalized_url.startswith("enfusion://"):
        return "enfusion"
    if "/wikidata/images/" in normalized_url or re.search(r"\.(png|jpg|jpeg|gif|webp|svg)(\?|#|$)", normalized_url, re.IGNORECASE):
        return "image"
    if "community.bistudio.com/wiki/" in normalized_url:
        return "wiki"
    if urlparse(normalized_url).scheme in {"http", "https"}:
        return "external"
    return "other"


def context_record(page: dict, section: dict | None = None) -> dict:
    record = {
        "pageId": page["_canonicalId"],
        "pageTitle": page.get("title") or "",
        "pageUrl": page.get("_canonicalUrl") or normalize_url(page.get("url") or "", keep_fragment=False),
    }
    if section:
        record.update(
            {
                "sectionId": section["id"],
                "sectionOrder": section["order"],
                "headingPath": section["headingPath"],
                "heading": section["heading"],
            }
        )
    return record


def extract_tables(section: dict, page: dict) -> list[dict]:
    tables = []
    lines = section["markdown"].splitlines()
    i = 0
    table_index = 0
    while i < len(lines):
        if "|" not in lines[i]:
            i += 1
            continue
        block = [lines[i]]
        j = i + 1
        while j < len(lines) and "|" in lines[j]:
            block.append(lines[j])
            j += 1
        if len(block) >= 2 and re.search(r"\|\s*:?-{3,}:?\s*(\||$)", "\n".join(block)):
            table_index += 1
            markdown = "\n".join(block).strip()
            record = context_record(page, section)
            record.update(
                {
                    "id": f"{section['id']}:table:{table_index}",
                    "order": table_index,
                    "markdown": markdown,
                    "rowCount": len(block),
                    "contentHash": text_hash(markdown),
                }
            )
            tables.append(record)
        i = max(j, i + 1)
    return tables


def extract_code_blocks(section: dict, page: dict) -> list[dict]:
    records = []
    pattern = re.compile(r"```([^\n`]*)\n(.*?)```", re.DOTALL)
    for index, match in enumerate(pattern.finditer(section["markdown"]), start=1):
        code = match.group(2).rstrip()
        record = context_record(page, section)
        record.update(
            {
                "id": f"{section['id']}:code:{index}",
                "order": index,
                "language": normalize_space(match.group(1)),
                "code": code,
                "lineCount": code.count("\n") + (1 if code else 0),
                "contentHash": text_hash(code),
            }
        )
        records.append(record)
    return records


def extract_media(section: dict, page: dict) -> list[dict]:
    records = []
    for index, match in enumerate(re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", section["markdown"]), start=1):
        record = context_record(page, section)
        url = normalize_url(match.group(2).strip(), page.get("_canonicalUrl") or page.get("url") or "")
        record.update(
            {
                "id": f"{section['id']}:media:{index}",
                "order": index,
                "label": normalize_space(match.group(1)),
                "url": url,
                "rawUrl": match.group(2).strip(),
                "isInternalWiki": "community.bistudio.com/wiki/" in url,
                "kind": "media",
                "linkKind": "image",
            }
        )
        records.append(record)
    return records


def extract_procedures(section: dict, page: dict) -> list[dict]:
    records = []
    lines = section["markdown"].splitlines()
    block: list[str] = []
    block_start = 0
    order = 0

    def is_step(line: str) -> bool:
        stripped = line.strip()
        if re.match(r"^(\d+[.)]|[-*+])\s+", stripped):
            lower = stripped.lower()
            return any(word in lower for word in PROCEDURE_WORDS) or bool(re.match(r"^\d+[.)]\s+", stripped))
        return False

    def procedure_type(lines: list[str]) -> str:
        has_numbered = any(re.match(r"^\s*\d+[.)]\s+", line) for line in lines)
        has_bullet = any(re.match(r"^\s*[-*+]\s+", line) for line in lines)
        if has_numbered and has_bullet:
            return "mixed"
        if has_numbered:
            return "numbered"
        return "bullet"

    def flush(end_line: int) -> None:
        nonlocal order, block
        if len(block) < 2:
            block = []
            return
        order += 1
        markdown = "\n".join(block).strip()
        record = context_record(page, section)
        record.update(
            {
                "id": f"{section['id']}:procedure:{order}",
                "order": order,
                "startLine": block_start,
                "endLine": end_line,
                "procedureType": procedure_type(block),
                "markdown": markdown,
                "steps": [normalize_space(re.sub(r"^(\d+[.)]|[-*+])\s+", "", line.strip())) for line in block],
                "contentHash": text_hash(markdown),
            }
        )
        records.append(record)
        block = []

    for index, line in enumerate(lines, start=section["startLine"]):
        if is_step(line):
            if not block:
                block_start = index
            block.append(line)
        else:
            flush(index - 1)
    flush(section["endLine"])
    return records


def extract_admonitions(section: dict, page: dict) -> list[dict]:
    records = []
    lines = section["markdown"].splitlines()
    current: list[str] = []
    current_start = 0
    order = 0

    def is_table_line(line: str) -> bool:
        stripped = line.strip()
        return stripped.startswith("|") and stripped.endswith("|")

    def admonition_type(line: str) -> str:
        stripped = line.strip()
        lower = stripped.lower()
        if stripped.startswith("⚠") or any(word in lower for word in ("warning", "caution", "attention")):
            return "warning"
        if any(word in lower for word in ("important", "recommended")):
            return "important"
        if stripped.startswith("ⓘ") or re.search(r"(?<![a-z0-9])note(?![a-z0-9])", lower):
            return "note"
        if any(word in lower for word in ("must", "required", "requires", "do not", "cannot")):
            return "requirement"
        return "candidate"

    def is_admonition(line: str) -> bool:
        if is_table_line(line):
            return False
        lower = line.lower()
        return any(word in lower for word in ADMONITION_WORDS) or line.strip().startswith(("ⓘ", "⚠"))

    def flush(end_line: int) -> None:
        nonlocal current, order
        if not current:
            return
        order += 1
        markdown = "\n".join(current).strip()
        record = context_record(page, section)
        record.update(
            {
                "id": f"{section['id']}:admonition:{order}",
                "order": order,
                "startLine": current_start,
                "endLine": end_line,
                "admonitionType": admonition_type(current[0]),
                "markdown": markdown,
                "text": markdown_to_text(markdown),
                "terms": matched_terms(markdown)[:20],
                "contentHash": text_hash(markdown),
            }
        )
        records.append(record)
        current = []

    for index, line in enumerate(lines, start=section["startLine"]):
        if is_admonition(line):
            flush(index - 1)
            current_start = index
            current = [line]
        elif current and (line.startswith((" ", "\t", "-", "*", "+")) or not line.strip()):
            current.append(line)
        else:
            flush(index - 1)
    flush(section["endLine"])
    return records


def chunk_section(section: dict, page: dict) -> list[dict]:
    markdown = section["markdown"]
    if len(markdown) <= CHUNK_TARGET_CHARS:
        chunks = [(0, len(markdown))]
    else:
        chunks = []
        start = 0
        while start < len(markdown):
            end = min(len(markdown), start + CHUNK_TARGET_CHARS)
            if end < len(markdown):
                boundary = max(markdown.rfind("\n\n", start, end), markdown.rfind("\n", start, end), markdown.rfind(" ", start, end))
                if boundary > start + 600:
                    end = boundary
            chunks.append((start, end))
            if end >= len(markdown):
                break
            start = max(end - CHUNK_OVERLAP_CHARS, start + 1)

    records = []
    total = len(chunks)
    for index, (start, end) in enumerate(chunks, start=1):
        raw_chunk = markdown[start:end]
        chunk = raw_chunk.strip()
        leading_trim = len(raw_chunk) - len(raw_chunk.lstrip())
        start_char = start + leading_trim
        end_char = start_char + len(chunk)
        record = context_record(page, section)
        record.update(
            {
                "id": f"{section['id']}:chunk:{index}",
                "chunkOrder": index,
                "chunkCount": total,
                "startChar": start_char,
                "endChar": end_char,
                "overlapPrevious": index > 1,
                "markdown": chunk,
                "text": markdown_to_text(chunk),
                "charCount": len(chunk),
                "contentHash": text_hash(chunk),
            }
        )
        records.append(record)
    return records


def build_page_record(page: dict, raw_index: int) -> dict:
    markdown = page.get("markdown") or ""
    text = page.get("text") or markdown_to_text(markdown)
    headings = [heading for heading in (page.get("headings") or []) if heading.strip()]
    search_text = "\n".join(
        [
            page.get("title") or "",
            page.get("_canonicalUrl") or "",
            page_family(page),
            " ".join(category_path(page)),
            " ".join(headings),
            text,
        ]
    )
    scores = topic_scores(search_text, page, heading_weight=2)
    primary_topics, related_topics = split_topics(scores)
    return {
        "id": page["_canonicalId"],
        "rawOrder": raw_index,
        "title": page.get("title") or "",
        "url": page.get("_canonicalUrl") or normalize_url(page.get("url") or "", keep_fragment=False),
        "kind": page.get("kind") or "page",
        "family": page_family(page),
        "categoryPath": category_path(page),
        "markdownPath": page.get("markdownPath"),
        "htmlPath": page.get("htmlPath"),
        "jsonPath": page.get("jsonPath"),
        "aliasCount": len(page.get("_aliases") or []),
        "aliases": page.get("_aliases") or [],
        "textLength": page.get("textLength") or len(text),
        "markdownLength": len(markdown),
        "headingCount": len(headings),
        "headings": headings,
        "terms": matched_terms(search_text),
        "topics": list(scores.keys()),
        "primaryTopics": primary_topics,
        "relatedTopics": related_topics,
        "topicScores": scores,
        "contentHash": text_hash(markdown or text),
    }


def build_section_record(page: dict, section: dict, order: int) -> dict:
    section_id = stable_id(f"{page['_canonicalId']}:{order}:{' > '.join(section['headingPath'])}")
    search_text = "\n".join(
        [
            page.get("title") or "",
            page.get("_canonicalUrl") or "",
            page_family(page),
            " ".join(category_path(page)),
            " > ".join(section["headingPath"]),
            section["text"],
        ]
    )
    scores = topic_scores(search_text, page)
    primary_topics, related_topics = split_topics(scores)
    section.update({"id": section_id, "order": order})
    record = context_record(page, section)
    record.update(
        {
            "id": section_id,
            "order": order,
            "level": section["level"],
            "startLine": section["startLine"],
            "endLine": section["endLine"],
            "markdown": section["markdown"],
            "text": section["text"],
            "charCount": len(section["markdown"]),
            "terms": matched_terms(search_text),
            "topics": list(scores.keys()),
            "primaryTopics": primary_topics,
            "relatedTopics": related_topics,
            "topicScores": scores,
            "contentHash": text_hash(section["markdown"]),
        }
    )
    return record


def build_topic_index(pages: list[dict], sections: list[dict]) -> dict:
    topic_index: dict[str, dict] = {}
    for topic, terms in TOPIC_RULES.items():
        page_matches = []
        section_matches = []
        for page in pages:
            score = page.get("topicScores", {}).get(topic, 0)
            if score:
                page_matches.append(
                    {
                        "pageId": page["id"],
                        "title": page["title"],
                        "url": page["url"],
                        "score": score,
                        "family": page["family"],
                        "categoryPath": page["categoryPath"],
                        "confidence": "primary" if topic in page.get("primaryTopics", []) else "related",
                        "terms": [term for term in page["terms"] if term in terms],
                    }
                )
        for section in sections:
            score = section.get("topicScores", {}).get(topic, 0)
            if score:
                section_matches.append(
                    {
                        "sectionId": section["id"],
                        "pageId": section["pageId"],
                        "title": section["pageTitle"],
                        "url": section["pageUrl"],
                        "headingPath": section["headingPath"],
                        "score": score,
                        "confidence": "primary" if topic in section.get("primaryTopics", []) else "related",
                        "terms": [term for term in section["terms"] if term in terms],
                    }
                )
        page_matches.sort(key=lambda item: (-item["score"], item["title"], item["url"]))
        section_matches.sort(key=lambda item: (-item["score"], item["title"], item["headingPath"]))
        topic_index[topic] = {
            "terms": list(terms),
            "pageCount": len(page_matches),
            "sectionCount": len(section_matches),
            "primaryPageCount": sum(1 for item in page_matches if item["confidence"] == "primary"),
            "primarySectionCount": sum(1 for item in section_matches if item["confidence"] == "primary"),
            "pages": page_matches,
            "sections": section_matches,
        }
    return dict(sorted(topic_index.items()))


def build_taxonomy(pages: list[dict]) -> dict:
    categories: dict[str, dict] = {}
    families: dict[str, dict] = {}
    for page in pages:
        family = page.get("family") or "Unclassified"
        families.setdefault(family, {"pageCount": 0, "pages": []})
        families[family]["pageCount"] += 1
        families[family]["pages"].append({"pageId": page["id"], "title": page["title"], "url": page["url"]})

        category_parts = page.get("categoryPath") or []
        for index in range(1, len(category_parts) + 1):
            path = "/".join(category_parts[:index])
            categories.setdefault(path, {"depth": index, "pageCount": 0, "pages": []})
        if category_parts:
            path = "/".join(category_parts)
            categories[path]["pageCount"] += 1
            categories[path]["pages"].append({"pageId": page["id"], "title": page["title"], "url": page["url"]})

    return {
        "categories": dict(sorted(categories.items())),
        "families": dict(sorted(families.items())),
    }


def build_quality_report(
    pages: list[dict],
    sections: list[dict],
    chunks: list[dict],
    tables: list[dict],
    code_blocks: list[dict],
    procedures: list[dict],
    admonitions: list[dict],
    media: list[dict],
    links: list[dict],
    canonical_pages: list[dict],
    raw_pages: list[dict],
) -> dict:
    high_value = {
        "scenario-framework": ("scenario-game-master", "Scenario Framework"),
        "server-config": ("server-runtime", "Server Config"),
        "multiplayer-scripting": ("networking", "Multiplayer Scripting"),
        "workbench-plugin-tutorial": ("workbench-debugging", "Workbench Plugin Tutorial"),
        "weapon-prefab-configuration": ("weapons", "Weapon Creation/Prefab Configuration"),
        "assets": ("assets", "Assets"),
        "terrain-tutorial": ("terrain-world-editor", "Terrain Tutorial"),
        "animation-editor": ("animation", "Animation Editor"),
        "audio-editor": ("audio", "Audio Editor"),
    }
    routing_checks = {}
    for name, (topic, title_part) in high_value.items():
        matches = [page for page in pages if title_part in page["title"]]
        routing_checks[name] = {
            "expectedTopic": topic,
            "matchedPages": len(matches),
            "hasPrimaryTopic": any(topic in page.get("primaryTopics", []) for page in matches),
            "titles": [page["title"] for page in matches[:8]],
        }

    return {
        "counts": {
            "rawPages": len(raw_pages),
            "canonicalPages": len(canonical_pages),
            "pages": len(pages),
            "sections": len(sections),
            "chunks": len(chunks),
            "tables": len(tables),
            "codeBlocks": len(code_blocks),
            "procedures": len(procedures),
            "admonitions": len(admonitions),
            "media": len(media),
            "links": len(links),
        },
        "quality": {
            "pagesWithoutPrimaryTopics": [page["title"] for page in pages if not page.get("primaryTopics")],
            "sectionsWithoutPrimaryTopics": sum(1 for section in sections if not section.get("primaryTopics")),
            "noisyLinkCount": sum(1 for link in links if link.get("label", "").startswith("![")),
            "tableAdmonitionCount": sum(1 for item in admonitions if item.get("markdown", "").strip().startswith("|")),
            "chunkRangeMissingCount": sum(1 for chunk in chunks if "startChar" not in chunk or "endChar" not in chunk),
            "duplicateAliasPages": sum(1 for page in pages if page.get("aliasCount", 0) > 1),
            "admonitionTypes": sorted({item.get("admonitionType") for item in admonitions}),
            "procedureTypes": sorted({item.get("procedureType") for item in procedures}),
        },
        "highValueRouting": routing_checks,
    }


def output_hashes(out_dir: Path, names: tuple[str, ...]) -> dict[str, str]:
    hashes = {}
    for name in names:
        path = out_dir / name
        if path.exists():
            hashes[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return hashes


def build_index(raw_dir: Path, out_dir: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    schema, raw_manifest, raw_pages = load_raw_cache(raw_dir)
    canonical_pages, alias_map = canonicalize_pages(raw_pages)
    out_dir.mkdir(parents=True, exist_ok=True)

    pages: list[dict] = []
    sections: list[dict] = []
    chunks: list[dict] = []
    tables: list[dict] = []
    code_blocks: list[dict] = []
    procedures: list[dict] = []
    admonitions: list[dict] = []
    media: list[dict] = []
    links: list[dict] = []

    for raw_index, page in enumerate(canonical_pages, start=1):
        page_record = build_page_record(page, raw_index)
        pages.append(page_record)
        for section_order, section in enumerate(split_sections(page.get("markdown") or ""), start=1):
            section_record = build_section_record(page, section, section_order)
            sections.append(section_record)
            chunks.extend(chunk_section(section, page))
            tables.extend(extract_tables(section, page))
            code_blocks.extend(extract_code_blocks(section, page))
            procedures.extend(extract_procedures(section, page))
            admonitions.extend(extract_admonitions(section, page))
            media.extend(extract_media(section, page))
            links.extend(extract_links(section["markdown"], page, section))

    pages.sort(key=lambda item: (item["title"], item["url"], item["id"]))
    sections.sort(key=lambda item: (item["pageTitle"], item["order"], item["id"]))
    chunks.sort(key=lambda item: (item["pageTitle"], item["sectionOrder"], item["chunkOrder"], item["id"]))
    tables.sort(key=lambda item: (item["pageTitle"], item["sectionOrder"], item["order"], item["id"]))
    code_blocks.sort(key=lambda item: (item["pageTitle"], item["sectionOrder"], item["order"], item["id"]))
    procedures.sort(key=lambda item: (item["pageTitle"], item["sectionOrder"], item["order"], item["id"]))
    admonitions.sort(key=lambda item: (item["pageTitle"], item["sectionOrder"], item["order"], item["id"]))
    media.sort(key=lambda item: (item["pageTitle"], item["sectionOrder"], item["order"], item["id"]))
    links.sort(key=lambda item: (item["pageTitle"], item.get("sectionOrder", 0), item["label"], item["url"]))

    topic_index = build_topic_index(pages, sections)
    taxonomy = build_taxonomy(pages)
    quality_report = build_quality_report(
        pages,
        sections,
        chunks,
        tables,
        code_blocks,
        procedures,
        admonitions,
        media,
        links,
        canonical_pages,
        raw_pages,
    )

    outputs = (
        "pages.jsonl",
        "sections.jsonl",
        "chunks.jsonl",
        "tables.jsonl",
        "code-blocks.jsonl",
        "procedures.jsonl",
        "admonitions.jsonl",
        "media.jsonl",
        "links.jsonl",
        "topics.json",
        "taxonomy.json",
        "quality-report.json",
    )
    write_jsonl(out_dir / "pages.jsonl", pages)
    write_jsonl(out_dir / "sections.jsonl", sections)
    write_jsonl(out_dir / "chunks.jsonl", chunks)
    write_jsonl(out_dir / "tables.jsonl", tables)
    write_jsonl(out_dir / "code-blocks.jsonl", code_blocks)
    write_jsonl(out_dir / "procedures.jsonl", procedures)
    write_jsonl(out_dir / "admonitions.jsonl", admonitions)
    write_jsonl(out_dir / "media.jsonl", media)
    write_jsonl(out_dir / "links.jsonl", links)
    (out_dir / "topics.json").write_text(json.dumps(topic_index, indent=2, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    (out_dir / "taxonomy.json").write_text(json.dumps(taxonomy, indent=2, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    (out_dir / "quality-report.json").write_text(json.dumps(quality_report, indent=2, ensure_ascii=False, sort_keys=True), encoding="utf-8")

    manifest = {
        "generatedAt": now_iso(),
        "tool": {
            "name": "index-reforger-wiki-docs.py",
            "version": INDEXER_VERSION,
            "configVersion": INDEX_CONFIG_VERSION,
        },
        "runtimeUse": "generation-only",
        "source": {
            "rawWikiDir": raw_dir.relative_to(root).as_posix() if raw_dir.is_relative_to(root) else raw_dir.as_posix(),
            "schemaGeneratedAt": schema.get("generatedAt"),
            "schemaDocumentCount": len(schema.get("documents") or []),
            "rawManifest": raw_manifest,
            "startUrl": schema.get("startUrl"),
            "rawPageJsonCount": len(raw_pages),
            "canonicalPageCount": len(canonical_pages),
            "duplicateAliasCount": sum(max(0, len(page.get("_aliases") or []) - 1) for page in canonical_pages),
        },
        "counts": {
            "pages": len(pages),
            "sections": len(sections),
            "chunks": len(chunks),
            "tables": len(tables),
            "codeBlocks": len(code_blocks),
            "procedures": len(procedures),
            "admonitions": len(admonitions),
            "media": len(media),
            "links": len(links),
            "topics": len(topic_index),
            "taxonomyCategories": len(taxonomy["categories"]),
            "taxonomyFamilies": len(taxonomy["families"]),
            "rawAliases": len(alias_map),
        },
        "outputs": list(outputs),
        "preservation": {
            "sectionsContainFullMarkdown": True,
            "chunksAreDerivedFromSections": True,
            "topicMembershipIsUncapped": True,
            "referencesAreNotGenerated": True,
        },
    }
    manifest["outputHashes"] = output_hashes(out_dir, outputs)
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Index cached Arma Reforger wiki docs for generation workflows.")
    parser.add_argument("--raw-wiki-dir", default=DEFAULT_RAW_DIR, help="Raw wiki cache produced by update-reforger-wiki-docs.py.")
    parser.add_argument("--out-dir", default=DEFAULT_OUT_DIR, help="Generation-only wiki index output directory.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    raw_dir = (root / args.raw_wiki_dir).resolve()
    out_dir = root / args.out_dir
    try:
        build_index(raw_dir, out_dir)
    except (FileNotFoundError, ValueError) as exc:
        print(f"[wiki-index] {exc}", file=sys.stderr)
        return 2
    print(f"[wiki-index] wrote {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
