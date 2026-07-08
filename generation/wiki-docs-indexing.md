# Wiki Docs Collection And Indexing

This document defines the current wiki tooling scope. The wiki pipeline only collects official wiki data and indexes it into generation-only lookup artifacts. It does not decide runtime reference files and does not build references.

## Scope

In scope now:

- Pull official Arma Reforger wiki pages into `raw/wiki-docs`.
- Keep the web scraper focused on fetching and storing raw cache data.
- Index cached wiki pages into complete generation artifacts.
- Preserve page URLs, headings, full section content, chunks, links, media, tables, code blocks, procedures, admonitions, terms, topic hints, and workflow signals for later use.
- Make the indexed data useful to later reference-generation workflows.

Out of scope now:

- Choosing the final runtime reference file set.
- Writing `references/*.md`.
- Writing `SKILL.md`.
- Auditing final runtime references.
- Depending on live wiki access during runtime Codex work.

## Scripts

### `scripts/update-reforger-wiki-docs.py`

This is the scraper. Keep it focused on fetching official wiki data into `raw/wiki-docs`.

Expected outputs:

- `raw/wiki-docs/html/*.html`
- `raw/wiki-docs/markdown/*.md`
- `raw/wiki-docs/pages/*.json`
- `raw/wiki-docs/schema.json`
- `raw/wiki-docs/manifest.json`
- `raw/wiki-docs/router.md`

The raw cache is generation input only. End users and future runtime Codex runs should not be expected to run this script.

### `scripts/index-reforger-wiki-docs.py`

This is the wiki indexer. It reads `raw/wiki-docs` and writes generation-only indexes.

Expected outputs under `generation/wiki-index/`:

- `pages.jsonl`: one canonical record per wiki page, including aliases for duplicate final URLs.
- `sections.jsonl`: every headed section with full normalized markdown and text.
- `chunks.jsonl`: bounded ordered chunks derived from sections for later low-context consumption.
- `tables.jsonl`: full markdown tables with page and section context.
- `code-blocks.jsonl`: fenced code blocks with page and section context.
- `procedures.jsonl`: ordered or checklist-like workflow steps.
- `admonitions.jsonl`: notes, warnings, important guidance, and required/must guidance.
- `media.jsonl`: image/media references with labels, source page, section, and URLs.
- `links.jsonl`: non-media links extracted with source page and section context.
- `topics.json`: uncapped topic-to-page and topic-to-section routing hints.
- `taxonomy.json`: category and page-family grouping from official wiki structure.
- `quality-report.json`: coverage and usefulness checks for future reference generation.
- `manifest.json`: indexer version, config version, source counts, output hashes.

The indexer does not scrape, build references, or write runtime files.

## Useful Indexed Data

The wiki index should preserve:

- Official page title and URL.
- Page kind, category path, family, aliases, and cache-relative paths.
- Full heading list.
- Headed section paths and full section content.
- Bounded chunks as derived convenience records, not replacements for sections.
- Chunk character ranges: `startChar`, `endChar`, and `overlapPrevious`.
- Full markdown tables.
- Full fenced code blocks.
- Image/media references.
- Procedures and checklist-like workflows with `procedureType`.
- Notes, warnings, important guidance, and required/must guidance with `admonitionType`.
- Matched terms.
- Token-aware topic scores plus `primaryTopics` and `relatedTopics`.
- Links between wiki pages.
- Link kinds: `wiki`, `image`, `enfusion`, `external`, `anchor`, or `other`.
- Stable output hashes for review.

This gives later generation scripts enough structure to build high-quality references without rereading every raw page or relying on old conversation context.

## Topic Hints

Topic hints are routing aids, not final reference decisions.

Topic matching must be token/phrase-aware. Short terms such as `ai` and `ui` must not match substrings inside unrelated words. Generic page-wide text such as `Arma Reforger` should not drive topic scoring.

Current topic families:

- overview
- scripting
- entity-component
- networking
- resources-prefabs-configs
- workbench-debugging
- scenario-game-master
- terrain-world-editor
- assets
- weapons
- vehicles
- animation
- audio
- ai
- ui
- configs
- prefabs
- packaging
- server-runtime
- samples-examples

Later reference generation may merge, split, or ignore these topics.

## Runtime Boundary

Runtime references and future `SKILL.md` should be built later from:

- wiki indexes for workflow/editor knowledge,
- game-data query/indexes for exact APIs,
- official samples for layout and examples,
- human review of coverage and usefulness.

The wiki raw cache and wiki index are generation artifacts. They are not runtime source truth for Codex by themselves.

## Validation

Current validation for this stage:

```powershell
py -3 -m py_compile scripts\update-reforger-wiki-docs.py scripts\index-reforger-wiki-docs.py
py -3 scripts\index-reforger-wiki-docs.py
```

If `raw/wiki-docs` is missing, the indexer should fail cleanly with exit code `2` and explain that the scraper must be run first.

Coverage checks should confirm that every raw page JSON file appears through a canonical page or alias, every section has full markdown, extracted structured records are non-empty when the corpus contains those structures, and output hashes remain stable across repeated index runs.

Quality checks should confirm that:

- `links.jsonl` has no malformed image labels such as `![`.
- `media.jsonl` retains image/media records.
- markdown tables are not captured as admonitions.
- chunks include character ranges.
- high-value pages route to expected primary topics.
