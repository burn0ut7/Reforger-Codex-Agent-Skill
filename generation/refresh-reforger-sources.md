# Refresh Reforger Sources Runner

This document defines the purpose and command interface for `scripts/refresh-reforger-sources.py`.

The refresh runner is a convenience orchestration script. It should call the existing source-specific scripts in the correct order, print a clear stage summary, and make it easy to refresh or check all generated Reforger source data from one command.

It must not replace the existing updater, indexer, query, scraper, or validation scripts. Each source-specific script remains the owner of its own data.

## What It Refreshes

The runner coordinates these data areas:

- Game data:
  - updates raw scripts with `scripts/update-reforger-data.py`,
  - indexes raw scripts with `scripts/index-reforger-data.py`.
- Wiki data:
  - optionally refreshes the raw wiki cache with `scripts/update-reforger-wiki-docs.py`,
  - indexes the existing raw wiki cache with `scripts/index-reforger-wiki-docs.py`.
- Official samples:
  - refreshes `raw/samples/` with `scripts/update-reforger-samples.ps1`.
- Search quality:
  - validates query behavior with `scripts/tests/validate-reforger-search.py`,
  - measures search usefulness with `scripts/tests/measure-reforger-search-usefulness.py`.

The runner is for generation/tooling maintenance. It is not a runtime reference source and should not be used by future `SKILL.md` as source truth.

## Default Behavior

Run from the repository root:

```powershell
py -3 scripts\refresh-reforger-sources.py
```

Default behavior should be a safe full refresh:

- update game data only if needed,
- rebuild game-data indexes only if stale,
- refresh official samples,
- rebuild the wiki index from the existing `raw/wiki-docs` cache,
- run search validation and usefulness checks,
- do not scrape the live wiki.

Live wiki scraping must be explicit. The wiki scraper uses a browser and can be affected by Cloudflare/security prompts, so the runner must only call it when `--fetch-wiki` is passed.

## Common Commands

Check status without refreshing data where supported:

```powershell
py -3 scripts\refresh-reforger-sources.py --check
```

Refresh only game data and game-data indexes:

```powershell
py -3 scripts\refresh-reforger-sources.py --game-data
```

Rebuild the wiki index from the existing raw wiki cache:

```powershell
py -3 scripts\refresh-reforger-sources.py --wiki
```

Fetch the live wiki first, then rebuild the wiki index:

```powershell
py -3 scripts\refresh-reforger-sources.py --wiki --fetch-wiki
```

Refresh official samples:

```powershell
py -3 scripts\refresh-reforger-sources.py --samples
```

Run only search validation and usefulness checks:

```powershell
py -3 scripts\refresh-reforger-sources.py --validate
```

Print the planned commands without running them:

```powershell
py -3 scripts\refresh-reforger-sources.py --dry-run
```

## Options

### Scope

- `--all`: run the safe full refresh. This is the default when no scope flags are provided.
- `--game-data`: update `raw/game-data/` and rebuild game-data lookup indexes as needed.
- `--wiki`: index the cached wiki data under `raw/wiki-docs/`.
- `--fetch-wiki`: run the live wiki scraper before wiki indexing. This only applies with `--wiki` or `--all`.
- `--samples`: refresh official samples under `raw/samples/`.
- `--validate`: run search quality validation and usefulness measurement.
- `--no-validate`: skip validation during the default or `--all` run.

### Execution

- `--if-needed`: use freshness checks where supported. This should be the default for game data and game-data indexes.
- `--force`: force game-data refresh and rebuild game-data indexes.
- `--check`: report status without mutating source data where supported.
- `--dry-run`: print every command in order without running it.
- `--keep-going`: continue after a failed stage, then exit nonzero if any required stage failed.

### Wiki Scraper Pass-Through

These options apply only when `--fetch-wiki` is used:

- `--wiki-manual-first`
- `--wiki-no-manual-security`
- `--wiki-keep-browser-open`
- `--wiki-browser-mode attach`
- `--wiki-browser-mode webdriver`
- `--wiki-max-pages <number>`

Example:

```powershell
py -3 scripts\refresh-reforger-sources.py --wiki --fetch-wiki --wiki-manual-first
```

## Stage Order

When selected, stages should run in this order:

1. Game data update:

   ```powershell
   py -3 scripts\update-reforger-data.py --if-needed
   ```

2. Game data index:

   ```powershell
   py -3 scripts\index-reforger-data.py --if-needed
   ```

3. Official samples:

   ```powershell
   powershell -ExecutionPolicy Bypass -File scripts\update-reforger-samples.ps1
   ```

4. Optional live wiki fetch:

   ```powershell
   py -3 scripts\update-reforger-wiki-docs.py
   ```

5. Wiki index:

   ```powershell
   py -3 scripts\index-reforger-wiki-docs.py
   ```

6. Search validation:

   ```powershell
   py -3 scripts\tests\validate-reforger-search.py
   py -3 scripts\tests\measure-reforger-search-usefulness.py
   ```

## Check Mode

`--check` should avoid mutating source data.

Expected behavior:

- Game data: run `scripts/update-reforger-data.py --check`.
- Game-data indexes: run `scripts/index-reforger-data.py --check`.
- Samples: report whether `raw/samples/.git` exists and can resolve `HEAD`; do not fetch.
- Wiki cache: report whether `raw/wiki-docs/manifest.json` exists; do not scrape.
- Wiki index: report whether `generation/wiki-index/manifest.json` exists; do not rebuild.
- Validation: skip unless `--validate` is explicitly selected.

## Exit Codes

- `0`: all selected stages succeeded, or selected checks are current.
- `10`: check mode found stale or missing data/indexes.
- `2`: status cannot be determined, or required source data is missing.
- `1`: a selected command failed.

With `--keep-going`, the runner should continue through later stages but still return a nonzero exit code if any selected stage failed.

## Human Review Output

Validation may write human-review artifacts such as search usefulness reports. These reports are audit artifacts only. They must not be used by the query script, indexes, runtime references, or future `SKILL.md` as source truth.

## Implementation Notes

- Keep orchestration logic thin.
- Do not duplicate fetch, parse, indexing, scraping, query, or validation logic from the source-specific scripts.
- Prefer clear subprocess command lines over importing and calling script internals.
- Print a final summary with each stage name, status, exit code, and elapsed time.
- In `--dry-run`, print exactly what would run and exit `0`.
