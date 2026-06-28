#!/usr/bin/env python3
"""Crawl Arma Reforger BIKI docs through Chrome and build a local doc schema."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urldefrag, urljoin, urlparse


START_URL = "https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding"
REQUIREMENTS = ["selenium>=4.45.0", "beautifulsoup4>=4.12.0", "markdownify>=0.12.0"]


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
    parser.add_argument("--max-pages", type=int, default=0, help="Safety cap. 0 means no cap.")
    parser.add_argument("--manual-first", action="store_true", help="Pause after first page for manual verification.")
    parser.add_argument("--keep-browser-open", action="store_true")
    parser.add_argument("--settle-seconds", type=float, default=0.25, help="Extra wait after wiki content appears.")
    return parser.parse_args()


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def safe_name(url: str) -> str:
    parsed = urlparse(url)
    name = unquote(parsed.path.removeprefix("/wiki/").strip("/"))
    name = re.sub(r"[^A-Za-z0-9._-]+", "_", name)
    return name or "page"


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


def extract_document(html: str):
    from bs4 import BeautifulSoup
    from markdownify import markdownify

    soup = BeautifulSoup(html, "html.parser")
    clean_soup(soup)

    content = soup.select_one("#mw-content-text") or soup.select_one("main") or soup.body or soup
    title_tag = soup.select_one("#firstHeading") or soup.title
    title = title_tag.get_text(" ", strip=True) if title_tag else ""
    headings = [heading.get_text(" ", strip=True) for heading in content.find_all(re.compile("^h[1-6]$"))]
    text = content.get_text("\n", strip=True)
    markdown = markdownify(str(content), heading_style="ATX").strip()
    return title, headings, text, markdown, soup


def is_empty_wiki_page(text: str) -> bool:
    empty_page_markers = [
        "There is currently no text in this page.",
        "you do not have permission to create this page.",
        "This category currently contains no pages or media.",
    ]
    return any(marker in text for marker in empty_page_markers)


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
    options.page_load_strategy = "normal"
    return webdriver.Chrome(options=options)


def wait_ready(driver, timeout: float = 30.0, settle_seconds: float = 1.0) -> None:
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait

    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            state = driver.execute_script("return document.readyState")
            title = driver.title
            if state == "complete" and "Just a moment" not in title:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#mw-content-text, main, body"))
                )
                time.sleep(settle_seconds)
                return
        except Exception:
            pass
        time.sleep(0.1)


def wait_past_security(driver, manual: bool, settle_seconds: float) -> None:
    wait_ready(driver, settle_seconds=settle_seconds)
    if "Just a moment" not in driver.title:
        return

    print("[wiki-docs] browser security verification is showing.")
    if manual:
        input("Complete it in Chrome, wait for the real page, then press Enter...")
        wait_ready(driver, settle_seconds=settle_seconds)
        return

    deadline = time.time() + 60
    while "Just a moment" in driver.title and time.time() < deadline:
        time.sleep(1)


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
        "# Arma Reforger Wiki Docs Router",
        "",
        "Use this file to choose which local wiki document to inspect.",
        "",
        "## Categories",
    ]

    for record in records:
        if record["kind"] == "category":
            lines.append(f"- {record['title']} - `{record['markdownPath']}` - {record['url']}")

    lines.append("")
    lines.append("## All Documents")
    for record in records:
        headings = "; ".join(record["headings"][:5])
        suffix = f" - headings: {headings}" if headings else ""
        lines.append(f"- {record['title']} - `{record['markdownPath']}`{suffix}")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    ensure_requirements()

    root = Path(__file__).resolve().parents[1]
    out_root = root / "raw" / "wiki-docs"
    html_root = out_root / "html"
    markdown_root = out_root / "markdown"
    json_root = out_root / "pages"
    profile_dir = root / "raw" / "tools" / "selenium-wiki-profile"
    if out_root.exists():
        shutil.rmtree(out_root)
    for directory in [html_root, markdown_root, json_root, profile_dir]:
        directory.mkdir(parents=True, exist_ok=True)

    driver = make_driver(profile_dir)
    queue: deque[str] = deque([START_URL])
    queued = {START_URL}
    visited: set[str] = set()
    records: list[dict] = []

    try:
        while queue:
            if args.max_pages and len(records) >= args.max_pages:
                break

            url = queue.popleft()
            if url in visited:
                continue
            visited.add(url)

            print(f"[wiki-docs] opening {url}")
            driver.get(url)

            if not records and args.manual_first:
                print("Complete browser verification if it appears, then press Enter.")
                input("Press Enter after the real page has loaded...")
                wait_past_security(driver, manual=True, settle_seconds=args.settle_seconds)
            else:
                wait_past_security(driver, manual=False, settle_seconds=args.settle_seconds)

            if "Just a moment" in driver.title:
                raise RuntimeError("Chrome is still on the security verification page. Re-run with --manual-first.")

            html = driver.page_source
            title, headings, text, markdown, _soup = extract_document(html)
            if is_empty_wiki_page(text):
                print(f"[wiki-docs] skipped empty page/category: {title or url}")
                add_links_from_page(driver, queue, queued, visited)
                continue

            name = safe_name(url)

            html_path = html_root / f"{name}.html"
            markdown_path = markdown_root / f"{name}.md"
            json_path = json_root / f"{name}.json"

            html_path.write_text(html, encoding="utf-8")
            markdown_path.write_text(markdown + "\n", encoding="utf-8")

            added = add_links_from_page(driver, queue, queued, visited)
            record = {
                "title": title or name,
                "url": driver.current_url,
                "kind": page_kind(driver.current_url),
                "headings": headings,
                "textLength": len(text),
                "markdownPath": str(markdown_path.relative_to(out_root)),
                "htmlPath": str(html_path.relative_to(out_root)),
                "jsonPath": str(json_path.relative_to(out_root)),
                "discoveredCategoryLinks": added,
            }
            page_data = {**record, "text": text, "markdown": markdown}
            json_path.write_text(json.dumps(page_data, indent=2, ensure_ascii=False), encoding="utf-8")
            records.append(record)

            print(f"[wiki-docs] saved {title or name}; queued +{added}; total saved {len(records)}")

        schema = {
            "generatedAt": now_iso(),
            "startUrl": START_URL,
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
            },
            "documents": records,
        }
        (out_root / "schema.json").write_text(json.dumps(schema, indent=2, ensure_ascii=False), encoding="utf-8")
        write_router(out_root / "router.md", records)
        print(f"[wiki-docs] wrote {out_root / 'schema.json'}")
        print(f"[wiki-docs] wrote {out_root / 'router.md'}")
    finally:
        if args.keep_browser_open:
            print("[wiki-docs] leaving Chrome open")
        else:
            driver.quit()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
