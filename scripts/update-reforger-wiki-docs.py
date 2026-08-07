#!/usr/bin/env python3
"""Crawl Arma Reforger BIKI docs into a generation-only raw cache.

The output under raw/wiki-docs is source material for reference generation.
Runtime references and future SKILL.md files must not depend on this cache.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
import urllib.request
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urldefrag, urljoin, urlparse


START_URL = "https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding"
WIKI_UPDATER_VERSION = 2
OUTPUT_CONTRACT = "raw-wiki-cache-v1"
REQUIREMENTS = ["selenium>=4.45.0", "beautifulsoup4>=4.12.0", "markdownify>=0.12.0"]
EXCLUDED_PATHS = {
    "/wiki/Arma_Reforger:Known_Issues",
}


def ensure_requirements() -> None:
    missing = []
    for module in ["selenium", "bs4", "markdownify"]:
        try:
            __import__(module)
        except ImportError:
            missing.append(module)

    if missing:
        subprocess.check_call([sys.executable, "-m", "pip", "install", *REQUIREMENTS])


def find_chrome() -> Path:
    candidates = [
        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
        Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("Google Chrome was not found. Install Chrome before running this script.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Crawl Arma Reforger BIKI docs through Chrome.")
    parser.add_argument("--start-url", default=START_URL, help="Wiki URL to start crawling from.")
    parser.add_argument("--max-pages", type=int, default=0, help="Safety cap. 0 means no cap.")
    parser.add_argument("--manual-first", action="store_true", help="Pause after first page for manual verification.")
    parser.add_argument("--no-manual-security", action="store_true", help="Do not pause for manual security verification.")
    parser.add_argument("--keep-browser-open", action="store_true")
    parser.add_argument(
        "--rebuild-markdown",
        action="store_true",
        help="Rebuild Markdown files and markdown/wiki-index.md from raw/wiki-docs without opening Chrome or fetching wiki pages.",
    )
    parser.add_argument("--settle-seconds", type=float, default=0.25, help="Extra wait after wiki content appears.")
    parser.add_argument("--page-timeout", type=float, default=30.0, help="Seconds before a page load is considered stuck.")
    parser.add_argument("--ready-timeout", type=float, default=30.0, help="Seconds to wait for wiki content after navigation.")
    parser.add_argument("--retry-delay", type=float, default=2.0, help="Seconds to wait before retrying a stuck page.")
    parser.add_argument("--max-page-retries", type=int, default=0, help="Retries per page. 0 means keep trying until saved or skipped.")
    parser.add_argument(
        "--browser-mode",
        choices=["attach", "webdriver"],
        default="attach",
        help="attach launches normal Chrome with remote debugging, then Selenium attaches. webdriver starts Chrome through Selenium directly.",
    )
    parser.add_argument("--debug-port", type=int, default=9223, help="Chrome remote debugging port used by --browser-mode attach.")
    return parser.parse_args()


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_text(value: str) -> str:
    replacements = {
        "â€“": "-",
        "â€”": "-",
        "â€˜": "'",
        "â€™": "'",
        "â€œ": '"',
        "â€": '"',
        "â€“": "-",
        "â€”": "-",
        "â€˜": "'",
        "â€™": "'",
        "â€œ": '"',
        "â€�": '"',
        "â€¦": "...",
        "â€Ž": "",
        "Â ": " ",
        "Â": "",
    }
    for bad, good in replacements.items():
        value = value.replace(bad, good)
    return value


def safe_name(url: str) -> str:
    parsed = urlparse(url)
    name = unquote(parsed.path.removeprefix("/wiki/").strip("/"))
    name = re.sub(r"[^A-Za-z0-9._-]+", "_", name)
    return name or "page"


def safe_file_name(value: str) -> str:
    """Return a readable Windows-safe Markdown filename."""
    name = re.sub(r'[<>:"/\\|?*]+', " ", value)
    name = re.sub(r"\s+", " ", name).strip(" .")
    return name or "page"


def document_title(title: str, fallback: str) -> str:
    """Remove the wiki's product namespace from a document title.

    The product is already implicit in this cache.  Repeating it in every
    filename and Markdown H1 makes the corpus noisier without adding context.
    """
    title = normalize_text(title).strip() or fallback
    title = re.sub(r"^Category:\s*Arma Reforger\s*/\s*", "", title, flags=re.IGNORECASE)
    title = re.sub(r"^Arma Reforger\s*[:/-]\s*", "", title, flags=re.IGNORECASE)
    title = re.sub(r"^Arma Reforger\s+[–-]\s+", "", title, flags=re.IGNORECASE)
    title = re.sub(r"\s+[–-]\s+Arma Reforger\s+Category$", " Category", title, flags=re.IGNORECASE)
    title = re.sub(r"\s+[–-]\s+Arma Reforger$", "", title, flags=re.IGNORECASE)
    return title.strip() or fallback


def category_path_from_url(url: str) -> list[str]:
    """Map an official category URL to its useful, relative folder path."""
    path = unquote(urlparse(url).path).lstrip("/")
    marker = "wiki/Category:Arma_Reforger"
    if not path.startswith(marker):
        return []
    suffix = path[len(marker):].strip("/")
    return [safe_file_name(part.replace("_", " ")) for part in suffix.split("/") if part]


def category_paths_from_soup(soup) -> list[list[str]]:
    """Read the page's official category memberships from MediaWiki markup."""
    paths: set[tuple[str, ...]] = set()
    for link in soup.select("#mw-normal-catlinks a[href], #catlinks a[href]"):
        category_path = category_path_from_url(link.get("href") or "")
        if category_path:
            paths.add(tuple(category_path))
    return [list(path) for path in sorted(paths, key=lambda path: (-len(path), path))]


def markdown_path_for_document(
    markdown_root: Path,
    title: str,
    url: str,
    kind: str,
    category_paths: list[list[str]],
    used_paths: dict[Path, str],
) -> Path:
    """Place a document below its deepest official category, without collisions."""
    category_path = category_paths[0] if category_paths else []
    if kind == "category":
        own_path = category_path_from_url(url)
        directory = markdown_root.joinpath(*own_path)
        candidate = directory / "index.md"
    else:
        directory = markdown_root.joinpath(*category_path)
        candidate = directory / f"{safe_file_name(title)}.md"

    if candidate not in used_paths or used_paths[candidate] == url:
        used_paths[candidate] = url
        return candidate

    # Same-title pages can exist in one category. Keep their readable title and
    # add a stable URL-derived suffix rather than silently overwriting content.
    candidate = candidate.with_name(f"{candidate.stem} -- {safe_name(url)}.md")
    used_paths[candidate] = url
    return candidate


def normalize_document_heading_levels(markdown: str) -> str:
    """Reserve H1 for the generated page title while preserving code blocks."""
    lines = []
    in_fence = False
    for line in markdown.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
        elif not in_fence and re.match(r"^#(?!#)\s+", line):
            line = f"#{line}"
        lines.append(line)
    return "\n".join(lines).strip()


def normalize_url(base_url: str, href: str | None) -> str | None:
    if not href:
        return None

    url, _fragment = urldefrag(urljoin(base_url, href))
    parsed = urlparse(url)
    if parsed.netloc != "community.bistudio.com":
        return None
    if not parsed.path.startswith("/wiki/"):
        return None

    path = unquote(parsed.path)
    if path in EXCLUDED_PATHS:
        return None
    if path.startswith("/wiki/Category:Arma_Reforger"):
        return url
    if path.startswith("/wiki/Arma_Reforger:"):
        return url
    if path.startswith("/wiki/Arma_Reforger/"):
        return url
    return None


def page_kind(url: str) -> str:
    path = unquote(urlparse(url).path)
    if "/wiki/Category:" in path:
        return "category"
    return "page"


def is_excluded_url(url: str) -> bool:
    return unquote(urlparse(url).path) in EXCLUDED_PATHS


def clean_soup(soup) -> object:
    for selector in [
        "script",
        "style",
        "noscript",
        "nav",
        "footer",
        ".printfooter",
        ".mw-editsection",
        "#mw-navigation",
        "#mw-panel",
        "#footer",
        "#siteNotice",
    ]:
        for tag in soup.select(selector):
            tag.decompose()
    return soup


def table_rows(table) -> list:
    """Return rows owned by this table, excluding rows nested in detail tables."""
    return [row for row in table.find_all("tr") if row.find_parent("table") == table]


def append_asset_detail_lists(catalog, detail_cell, soup) -> bool:
    """Flatten nested detail lists into labeled, searchable asset facts."""
    detail_lists = [item for item in detail_cell.select("table ul") if not item.find_parent("ul")]
    if not detail_lists:
        return False
    for detail_list in detail_lists:
        for item in detail_list.find_all("li", recursive=False):
            nested_list = item.find("ul", recursive=False)
            label_parts = []
            for child in item.contents:
                if child == nested_list:
                    continue
                label_parts.append(child.get_text(" ", strip=True) if hasattr(child, "get_text") else str(child))
            label = " ".join(part.strip() for part in label_parts if part.strip())
            values = []
            if nested_list:
                values = [value.get_text(" ", strip=True) for value in nested_list.find_all("li", recursive=False)]

            details = soup.new_tag("p")
            if label:
                strong = soup.new_tag("strong")
                strong.string = label
                details.append(strong)
            if values:
                details.append(" " if label else "")
                details.append("; ".join(values))
            catalog.append(details)
    return True


def unwrap_asset_catalog_tables(soup) -> None:
    """Turn the wiki's nested asset catalog tables into readable asset records."""
    for table in list(soup.select("table")):
        rows = table_rows(table)
        if len(rows) < 2:
            continue
        headers = [cell.get_text(" ", strip=True).casefold() for cell in rows[0].find_all("th", recursive=False)]
        if headers != ["name", "prefab", "details"] or not table.select_one(".biki-spoiler"):
            continue

        catalog = soup.new_tag("div", attrs={"class": "wiki-asset-catalog"})
        for row in rows[1:]:
            cells = row.find_all("td", recursive=False)
            if len(cells) != 3:
                continue
            heading = soup.new_tag("h4")
            for child in list(cells[0].contents):
                heading.append(child.extract())
            catalog.append(heading)

            prefab = soup.new_tag("p")
            label = soup.new_tag("strong")
            label.string = "Prefab:"
            prefab.append(label)
            prefab.append(" ")
            for child in list(cells[1].contents):
                prefab.append(child.extract())
            catalog.append(prefab)

            if not append_asset_detail_lists(catalog, cells[2], soup):
                detail_text = cells[2].get_text(" ", strip=True).replace("Show details", "").strip()
                if detail_text:
                    details = soup.new_tag("p")
                    details.string = detail_text
                    catalog.append(details)
        table.replace_with(catalog)


def is_enforce_comparison_table(table) -> bool:
    """Identify the wiki's two-column Don't/Do code comparison tables."""
    rows = table.find_all("tr")
    if len(rows) < 2:
        return False
    headers = [cell.get_text(" ", strip=True).casefold() for cell in rows[0].find_all("th", recursive=False)]
    if headers != ["don't", "do"]:
        return False
    return any(row.select_one(".enforcescripthighlighter-block") for row in rows[1:])


def unwrap_enforce_comparison_tables(soup) -> None:
    """Turn comparison tables into sequential Markdown-friendly sections."""
    for table in list(soup.select("table")):
        if not is_enforce_comparison_table(table):
            continue
        rows = table.find_all("tr")
        labels = [cell.get_text(" ", strip=True) for cell in rows[0].find_all("th", recursive=False)]
        container = soup.new_tag("div", attrs={"class": "wiki-enforce-comparison"})
        for row in rows[1:]:
            cells = row.find_all("td", recursive=False)
            if len(cells) != 2:
                continue
            for label, cell in zip(labels, cells):
                heading = soup.new_tag("h3")
                heading.string = label
                container.append(heading)
                for child in list(cell.contents):
                    container.append(child.extract())
        table.replace_with(container)


def convert_enforce_highlighter_blocks(soup) -> None:
    """Replace BIKI's span-based Enforce highlighter with real code blocks."""
    for block in list(soup.select(".enforcescripthighlighter-block")):
        scroller = block.select_one(".enforcescripthighlighter-scroller")
        if not scroller:
            continue
        code = format_enforce_code(scroller.get_text().strip("\n"))
        marker = soup.new_tag("p")
        marker.string = "ENFORCECODEMARKER"
        pre = soup.new_tag("pre")
        code_tag = soup.new_tag("code")
        code_tag.string = code
        pre.append(code_tag)
        block.replace_with(marker)
        marker.insert_after(pre)


def format_enforce_code(code: str) -> str:
    """Restore readable indentation lost when Chromium serializes highlighted spans."""
    lines = []
    indent = 0
    for raw_line in code.splitlines():
        line = raw_line.strip()
        if not line:
            lines.append("")
            continue
        leading_closes = len(re.match(r"^}+", line).group(0)) if line.startswith("}") else 0
        lines.append(f"{'\t' * max(0, indent - leading_closes)}{line}")
        indent = max(0, indent + line.count("{") - line.count("}"))
    return "\n".join(lines).strip()


def mark_enforce_fences(markdown: str) -> str:
    """Apply a language tag only to code fences originating from the wiki highlighter."""
    return re.sub(r"ENFORCECODEMARKER\s*\n+```", "```enforce", markdown)


def extract_document(html: str):
    from bs4 import BeautifulSoup
    from markdownify import markdownify

    soup = BeautifulSoup(html, "html.parser")
    clean_soup(soup)

    content = soup.select_one("#mw-content-text") or soup.select_one("main") or soup.body or soup
    title_tag = soup.select_one("#firstHeading") or soup.title
    title = title_tag.get_text(" ", strip=True) if title_tag else ""
    unwrap_asset_catalog_tables(content)
    unwrap_enforce_comparison_tables(content)
    convert_enforce_highlighter_blocks(content)
    headings = [heading.get_text(" ", strip=True) for heading in content.find_all(re.compile("^h[1-6]$"))]
    text = content.get_text("\n", strip=True)
    markdown = markdownify(str(content), heading_style="ATX").strip()
    markdown = mark_enforce_fences(markdown)
    title = normalize_text(title)
    headings = [normalize_text(heading) for heading in headings]
    text = normalize_text(text)
    markdown = normalize_text(markdown)
    markdown = normalize_document_heading_levels(markdown)
    return title, headings, text, markdown, category_paths_from_soup(soup), soup


def is_empty_wiki_page(text: str) -> bool:
    empty_page_markers = [
        "There is currently no text in this page.",
        "you do not have permission to create this page.",
        "This category currently contains no pages or media.",
        "TODO): placeholder",
        "TODO: placeholder",
    ]
    return any(marker in text for marker in empty_page_markers)


def is_security_page(driver) -> bool:
    title = ""
    body = ""
    try:
        title = driver.title or ""
    except Exception:
        pass
    try:
        body = driver.execute_script("return document.body ? document.body.innerText : ''") or ""
    except Exception:
        pass

    combined = f"{title}\n{body}".lower()
    markers = [
        "just a moment",
        "performing security verification",
        "security service",
        "verify you are not a bot",
        "checking your browser",
        "cloudflare",
    ]
    return any(marker in combined for marker in markers)


def make_driver(profile_dir: Path):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.binary_location = str(find_chrome())
    options.add_argument(f"--user-data-dir={profile_dir}")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.page_load_strategy = "eager"
    return webdriver.Chrome(options=options)


def wait_for_debugger(port: int, timeout: float = 20.0) -> None:
    deadline = time.time() + timeout
    url = f"http://127.0.0.1:{port}/json/version"
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=1):
                return
        except Exception:
            time.sleep(0.2)
    raise RuntimeError(f"Chrome remote debugger did not open on port {port}.")


def make_attached_driver(profile_dir: Path, port: int, start_url: str):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    chrome = find_chrome()
    profile_dir.mkdir(parents=True, exist_ok=True)
    args = [
        str(chrome),
        f"--remote-debugging-port={port}",
        f"--user-data-dir={profile_dir}",
        "--new-window",
        start_url,
    ]
    subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    wait_for_debugger(port)

    options = Options()
    options.debugger_address = f"127.0.0.1:{port}"
    options.page_load_strategy = "eager"
    return webdriver.Chrome(options=options)


def wait_ready(driver, timeout: float = 30.0, settle_seconds: float = 1.0) -> bool:
    from selenium.webdriver.common.by import By

    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            state = driver.execute_script("return document.readyState")
            content = driver.find_elements(By.CSS_SELECTOR, "#mw-content-text, main, body")
            if state in {"interactive", "complete"} and content and not is_security_page(driver):
                time.sleep(settle_seconds)
                return True
        except Exception:
            pass
        time.sleep(0.1)
    return False


def wait_past_security(driver, manual: bool, settle_seconds: float, ready_timeout: float) -> bool:
    wait_ready(driver, timeout=ready_timeout, settle_seconds=settle_seconds)
    if not is_security_page(driver):
        return True

    print("[wiki-docs] browser security verification is showing.")
    if manual:
        try:
            input("Complete it in Chrome, wait for the real page, then press Enter here...")
        except EOFError:
            print("[wiki-docs] stdin is unavailable; waiting for verification to clear automatically.")
        return wait_ready(driver, timeout=ready_timeout, settle_seconds=settle_seconds)

    deadline = time.time() + 60
    while is_security_page(driver) and time.time() < deadline:
        time.sleep(1)
    return not is_security_page(driver)


def stop_loading(driver) -> None:
    try:
        driver.execute_script("window.stop();")
    except Exception:
        pass


def add_links_from_page(driver, queue: deque[str], queued: set[str], visited: set[str]) -> int:
    from selenium.webdriver.common.by import By

    added = 0
    current_url = driver.current_url
    elements = driver.find_elements(By.CSS_SELECTOR, "#mw-content-text a[href], main a[href]")
    if not elements:
        elements = driver.find_elements(By.CSS_SELECTOR, "a[href]")

    for element in elements:
        next_url = normalize_url(current_url, element.get_attribute("href"))
        if not next_url or next_url in visited or next_url in queued:
            continue
        queue.append(next_url)
        queued.add(next_url)
        added += 1
    return added


def write_router(path: Path, records: list[dict]) -> None:
    lines = [
        "# Wiki Markdown Index",
        "",
        "Generation-only raw wiki cache index. Each title links to its local Markdown file; the `wiki` link opens the official source page.",
        "",
        "For MCP/Codex search, use the exact category names, page titles, and heading phrases listed as keywords below. The linked Markdown file contains the full page content.",
        "",
        "Do not ship this file as a runtime reference, and do not route future Codex runs to depend on `raw/wiki-docs`.",
        "",
        "## Categories",
    ]

    def local_link(record: dict) -> str:
        title = record.get("displayTitle") or record["title"]
        title = title.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")
        markdown_path = Path(record["markdownPath"]).as_posix()
        if markdown_path.startswith("markdown/"):
            markdown_path = markdown_path.removeprefix("markdown/")
        return f"[{title}](<{markdown_path}>)"

    def search_terms(record: dict) -> str:
        terms = [record.get("displayTitle") or record["title"]]
        terms.extend(" > ".join(category) for category in record.get("categoryPaths") or [])
        terms.extend(record.get("headings") or [])
        unique_terms = []
        seen = set()
        for term in terms:
            normalized = normalize_text(str(term)).strip()
            key = normalized.casefold()
            if normalized and key not in seen:
                unique_terms.append(normalized)
                seen.add(key)
        return "; ".join(unique_terms)

    for record in sorted(records, key=lambda item: (item["kind"], item.get("displayTitle") or item["title"])):
        if record["kind"] == "category":
            lines.append(f"- {local_link(record)} ([wiki]({record['url']}))")

    lines.append("")
    lines.append("## All Documents")
    for record in sorted(records, key=lambda item: ((item.get("displayTitle") or item["title"]).casefold(), item["url"])):
        lines.append(f"- {local_link(record)} ([wiki]({record['url']}))")
        lines.append(f"  - keywords: {search_terms(record)}")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def remove_generated_title(markdown: str) -> str:
    """Make the Markdown-only rebuild mode idempotent."""
    return re.sub(r"\A\s*#\s+\[[^\]]+\]\([^\n]+\)\s*\n{1,2}", "", markdown).strip()


def rebuild_markdown_from_cache(cache_root: Path) -> int:
    """Recreate Markdown output from cached source files without web access."""
    schema_path = cache_root / "schema.json"
    pages_root = cache_root / "pages"
    if not schema_path.exists() or not pages_root.exists():
        raise FileNotFoundError(
            f"Missing cached wiki data under {cache_root}. Run a full scrape once before using --rebuild-markdown."
        )

    page_paths = sorted(pages_root.glob("*.json"))
    if not page_paths:
        raise FileNotFoundError(f"No cached page JSON files found under {pages_root}.")

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    markdown_root = cache_root / "markdown"
    if markdown_root.exists():
        shutil.rmtree(markdown_root)
    markdown_root.mkdir(parents=True, exist_ok=True)

    used_markdown_paths: dict[Path, str] = {}
    records: list[dict] = []
    for page_path in page_paths:
        page_data = json.loads(page_path.read_text(encoding="utf-8"))
        page_url = page_data.get("url") or ""
        if not page_url:
            raise ValueError(f"Cached page has no URL: {page_path}")

        name = safe_name(page_url)
        title = page_data.get("title") or name
        display_title = document_title(title, name)
        kind = page_data.get("kind") or page_kind(page_url)
        html_relative_path = page_data.get("htmlPath") or f"html/{name}.html"
        html_path = cache_root / html_relative_path
        category_paths: list[list[str]] = []
        source_markdown = page_data.get("markdown") or ""
        source_headings = page_data.get("headings") or []
        source_text = page_data.get("text") or ""
        if html_path.exists():
            _title, source_headings, source_text, source_markdown, category_paths, _soup = extract_document(
                html_path.read_text(encoding="utf-8")
            )

        markdown_path = markdown_path_for_document(
            markdown_root,
            display_title,
            page_url,
            kind,
            category_paths,
            used_markdown_paths,
        )
        source_markdown = normalize_document_heading_levels(remove_generated_title(source_markdown))
        markdown = f"# [{display_title}]({page_url})\n\n{source_markdown}".strip()
        markdown_path.parent.mkdir(parents=True, exist_ok=True)
        markdown_path.write_text(markdown + "\n", encoding="utf-8")

        existing_headings = [heading for heading in source_headings if heading != display_title]
        record = {
            **{key: value for key, value in page_data.items() if key not in {"text", "markdown"}},
            "title": title,
            "displayTitle": display_title,
            "url": page_url,
            "kind": kind,
            "headings": [display_title, *existing_headings],
            "categoryPaths": category_paths,
            "markdownPath": str(markdown_path.relative_to(cache_root)),
            "htmlPath": html_relative_path,
            "jsonPath": str(page_path.relative_to(cache_root)),
        }
        page_data.update(record)
        page_data["text"] = source_text
        page_data["textLength"] = len(source_text)
        page_data["markdown"] = markdown
        page_path.write_text(json.dumps(page_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        records.append(record)

    schema["documents"] = records
    schema.setdefault("counts", {})["documents"] = len(records)
    schema["markdownRebuiltAt"] = now_iso()
    schema_path.write_text(json.dumps(schema, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    manifest_path = cache_root / "manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["markdownRebuiltAt"] = schema["markdownRebuiltAt"]
        manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_router(markdown_root / "wiki-index.md", records)
    legacy_router = cache_root / "router.md"
    if legacy_router.exists():
        legacy_router.unlink()
    return len(records)


def main() -> int:
    args = parse_args()
    ensure_requirements()

    root = Path(__file__).resolve().parents[1]
    if args.rebuild_markdown:
        try:
            count = rebuild_markdown_from_cache(root / "raw" / "wiki-docs")
        except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
            print(f"[wiki-docs] {exc}", file=sys.stderr)
            return 2
        print(f"[wiki-docs] rebuilt Markdown for {count} cached documents without scraping")
        return 0

    out_root = root / "raw" / "wiki-docs"
    stage_root = root / "raw" / "wiki-docs.tmp"
    html_root = stage_root / "html"
    markdown_root = stage_root / "markdown"
    json_root = stage_root / "pages"
    profile_dir = root / "raw" / "tools" / "chrome-wiki-profile"
    if stage_root.exists():
        shutil.rmtree(stage_root)
    for directory in [html_root, markdown_root, json_root, profile_dir]:
        directory.mkdir(parents=True, exist_ok=True)

    if args.browser_mode == "attach":
        driver = make_attached_driver(profile_dir, args.debug_port, args.start_url)
    else:
        driver = make_driver(profile_dir)
    driver.set_page_load_timeout(args.page_timeout)

    queue: deque[str] = deque([args.start_url])
    queued = {args.start_url}
    visited: set[str] = set()
    records: list[dict] = []
    skipped_urls: list[dict] = []
    used_markdown_paths: dict[Path, str] = {}

    try:
        while queue:
            if args.max_pages and len(records) >= args.max_pages:
                break

            url = queue.popleft()
            if url in visited:
                continue
            if is_excluded_url(url):
                print(f"[wiki-docs] skipped excluded URL: {url}")
                skipped_urls.append({"url": url, "reason": "excluded"})
                visited.add(url)
                continue

            attempt = 0
            while True:
                attempt += 1
                try:
                    suffix = f" (attempt {attempt})" if attempt > 1 else ""
                    print(f"[wiki-docs] opening {url}{suffix}")
                    try:
                        driver.get(url)
                    except Exception as exc:
                        print(f"[wiki-docs] page load did not finish within {args.page_timeout}s: {exc}")
                        stop_loading(driver)

                    if not records and args.manual_first:
                        print("Complete browser verification if it appears, then press Enter.")
                        try:
                            input("Press Enter after the real page has loaded...")
                        except EOFError:
                            print("[wiki-docs] stdin is unavailable; continuing with automatic wait.")
                        ready = wait_past_security(driver, manual=True, settle_seconds=args.settle_seconds, ready_timeout=args.ready_timeout)
                    else:
                        ready = wait_past_security(
                            driver,
                            manual=not args.no_manual_security,
                            settle_seconds=args.settle_seconds,
                            ready_timeout=args.ready_timeout,
                        )

                    if is_security_page(driver):
                        raise RuntimeError("Chrome is still on the security verification page.")
                    if not ready:
                        wait_ready(driver, timeout=args.ready_timeout, settle_seconds=args.settle_seconds)

                    html = driver.page_source
                    title, headings, text, markdown, category_paths, _soup = extract_document(html)
                    if is_security_page(driver):
                        raise RuntimeError("Chrome returned to the security verification page.")
                    if is_empty_wiki_page(text):
                        print(f"[wiki-docs] skipped empty page/category: {title or url}")
                        add_links_from_page(driver, queue, queued, visited)
                        visited.add(url)
                        break

                    has_wiki_container = "#mw-content-text" in html or 'id="mw-content-text"' in html
                    if len(text.strip()) < 80 and not has_wiki_container:
                        raise RuntimeError("loaded page did not contain useful wiki content")
                    if not ready:
                        print("[wiki-docs] saving from partially loaded page content")

                    page_url = driver.current_url
                    name = safe_name(page_url)
                    display_title = document_title(title, name)
                    kind = page_kind(page_url)

                    html_path = html_root / f"{name}.html"
                    json_path = json_root / f"{name}.json"
                    markdown_path = markdown_path_for_document(
                        markdown_root,
                        display_title,
                        page_url,
                        kind,
                        category_paths,
                        used_markdown_paths,
                    )
                    markdown = f"# [{display_title}]({page_url})\n\n{markdown}".strip()

                    html_path.write_text(html, encoding="utf-8")
                    markdown_path.parent.mkdir(parents=True, exist_ok=True)
                    markdown_path.write_text(markdown + "\n", encoding="utf-8")

                    added = add_links_from_page(driver, queue, queued, visited)
                    record = {
                        "title": title or name,
                        "displayTitle": display_title,
                        "url": page_url,
                        "kind": kind,
                        "headings": [display_title, *headings],
                        "categoryPaths": category_paths,
                        "textLength": len(text),
                        "markdownPath": str(markdown_path.relative_to(stage_root)),
                        "htmlPath": str(html_path.relative_to(stage_root)),
                        "jsonPath": str(json_path.relative_to(stage_root)),
                        "discoveredCategoryLinks": added,
                    }
                    page_data = {**record, "text": text, "markdown": markdown}
                    json_path.write_text(json.dumps(page_data, indent=2, ensure_ascii=False), encoding="utf-8")
                    records.append(record)
                    visited.add(url)

                    print(f"[wiki-docs] saved {title or name}; queued +{added}; total saved {len(records)}")
                    break
                except Exception as exc:
                    stop_loading(driver)
                    print(f"[wiki-docs] retrying {url}: {exc}")
                    if args.max_page_retries and attempt >= args.max_page_retries:
                        raise
                    time.sleep(args.retry_delay)

        schema = {
            "generatedAt": now_iso(),
            "tool": {
                "name": "update-reforger-wiki-docs.py",
                "version": WIKI_UPDATER_VERSION,
                "contract": OUTPUT_CONTRACT,
            },
            "runtimeUse": "generation-only",
            "startUrl": args.start_url,
            "boundary": {
                "allowedPathPrefixes": [
                    "/wiki/Category:Arma_Reforger",
                    "/wiki/Arma_Reforger:",
                    "/wiki/Arma_Reforger/",
                ],
                "visitedOnce": True,
            },
            "counts": {
                "documents": len(records),
                "remainingQueued": len(queue),
                "skipped": len(skipped_urls),
            },
            "documents": records,
            "skipped": skipped_urls,
        }
        (stage_root / "schema.json").write_text(json.dumps(schema, indent=2, ensure_ascii=False), encoding="utf-8")
        manifest = {
            "generatedAt": schema["generatedAt"],
            "tool": schema["tool"],
            "runtimeUse": "generation-only",
            "source": {
                "startUrl": args.start_url,
                "allowedPathPrefixes": schema["boundary"]["allowedPathPrefixes"],
                "excludedPaths": sorted(EXCLUDED_PATHS),
            },
            "counts": schema["counts"],
            "outputs": {
                "schema": "schema.json",
                "wikiIndex": "markdown/wiki-index.md",
                "htmlDir": "html",
                "markdownDir": "markdown",
                "pagesDir": "pages",
            },
        }
        (stage_root / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
        write_router(markdown_root / "wiki-index.md", records)

        if out_root.exists():
            shutil.rmtree(out_root)
        stage_root.rename(out_root)
        print(f"[wiki-docs] wrote {out_root / 'schema.json'}")
        print(f"[wiki-docs] wrote {out_root / 'manifest.json'}")
        print(f"[wiki-docs] wrote {out_root / 'markdown' / 'wiki-index.md'}")
    finally:
        if args.keep_browser_open:
            print("[wiki-docs] leaving Chrome open")
        else:
            driver.quit()
        if stage_root.exists():
            shutil.rmtree(stage_root)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
