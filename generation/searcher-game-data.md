# Reforger Game Data Searcher Design

This document is the detailed contract for `scripts/query-reforger-data.py`. It is generation-facing and tooling-facing. The searcher exists so Codex can verify Reforger APIs and inspect examples without loading large schema files, API dumps, or broad raw source.

## Purpose

Codex must not guess Reforger APIs. The searcher is the mandatory low-context lookup helper over generated game-data indexes.

Primary uses:

- Verify exact class, method, property, enum, function, and attribute records.
- Find valid method signatures before writing API-sensitive code.
- Find base and derived classes for inheritance-sensitive work.
- Find handwritten implementation examples by task topic.
- Find narrower implementation patterns by indexed subtopic.
- Return task-oriented lookup bundles for common Reforger scripting work.
- Locate source files by symbol, base class, topic, module, or path text.
- Return bounded raw source snippets only after a query identifies exact files and lines.

The searcher must never parse or read `raw/game-data/api-schema.json` during ordinary lookup. The JSONL indexes are the normal query surface.

## Inputs

The searcher reads only:

- `raw/game-data/indexes/symbols.jsonl`
- `raw/game-data/indexes/files.jsonl`
- `raw/game-data/indexes/examples.jsonl`
- `raw/game-data/indexes/inheritance.jsonl`
- `raw/game-data/indexes/manifest.json`
- `raw/game-data/scripts/**` only for explicit bounded snippet requests

It does not update raw game data or regenerate indexes.

## Commands

Use:

```powershell
py -3 scripts/query-reforger-data.py symbol ResourceName
py -3 scripts/query-reforger-data.py symbol ScriptComponent --kind class
py -3 scripts/query-reforger-data.py method IEntity FindComponent
py -3 scripts/query-reforger-data.py method Resource Load
py -3 scripts/query-reforger-data.py attribute RplProp
py -3 scripts/query-reforger-data.py inherits ScriptedUserAction
py -3 scripts/query-reforger-data.py examples replication
py -3 scripts/query-reforger-data.py examples resource-loading --subtopic spawn-prefab --with-snippets
py -3 scripts/query-reforger-data.py files WorkbenchPlugin
py -3 scripts/query-reforger-data.py snippet scripts/Game/CombatOps/SCR_FastTravelAction.c --line 1 --context 20
py -3 scripts/query-reforger-data.py lookup "replicated component"
```

Common options:

- `--json`: emit machine-readable JSON.
- `--limit N`: bound returned results.
- `--kind KIND`: filter symbol kind.
- `--module MODULE`: filter source module.
- `--topic TOPIC`: filter topic-tagged records.
- `--subtopic SUBTOPIC`: filter records that contain a narrower topic family.
- `--generated-only`: return only generated API records.
- `--handwritten-only`: return only handwritten source records.
- `--exact`: require exact case-sensitive matches where supported.

`examples` additionally supports `--with-snippets`. This attaches hard-bounded snippets to only the top example records. It is for situations where Codex needs immediate source shape after examples have already been ranked.

`lookup "<task phrase>"` is a deterministic, rule-based task router. It does not use embeddings. It returns a compact bundle of exact API symbols, method records, inheritance candidates, examples, suggested snippet commands, and residual Workbench/runtime/server verification notes. Current task families are user actions, replicated components, prefab spawning, resource loading, Workbench plugins, weapons, vehicles, inventory, UI/HUD, audio, and animation.

When no task rule matches, `lookup` must return an explicit unmatched result with `matchedTask: null`, no unrelated APIs/examples, and suggested next searches. It must not fall back to an unrelated task bundle.

## Ranking Rules

For symbol, method, and file searches:

1. exact match,
2. qualified-name exact match,
3. prefix match,
4. contains match.

For API lookup, generated records sort before handwritten records. For examples, handwritten records sort before generated records and higher `priority` sorts first.

For subtopic-aware example lookup, records with matching subtopics and stronger evidence should rank above incidental broad-topic matches. Example records may include compact `subtopics` and `evidence` fields so Codex can see why a file matched without opening the raw source first.

Use `--exact` when Codex is verifying a known API name and should not receive prefix or contains matches. For example, `method IEntity FindComponent --exact` returns `IEntity.FindComponent` without related methods such as `FindComponents`.

Use `attribute <name>` for annotation APIs such as `RplProp`, `RplRpc`, and other classes extending `UniqueAttribute`. Attribute lookup returns the attribute class plus constructor/properties when available.

Examples are not signature authority. Codex must verify signatures with `symbol` or `method`.

## Output Limits

Defaults:

- `symbol`: 20 records.
- `method`: 20 records.
- `inherits`: 40 records.
- `examples`: 12 records.
- `files`: 30 records.
- `snippet`: one bounded source excerpt.
- `lookup`: one task bundle.

Snippet behavior:

- Default context is 20 lines.
- Hard cap is 100 total lines.
- `--with-snippets` uses a smaller internal cap and only attaches snippets to a few top-ranked examples.
- Snippet paths must resolve under `raw/game-data/scripts/`.
- Paths outside raw game scripts must fail cleanly.

## Human Log Export

Every command supports optional human-only Markdown export:

```powershell
py -3 scripts/query-reforger-data.py method IEntity FindComponent --human-log
py -3 scripts/query-reforger-data.py examples replication --human-log --human-log-dir generation/search-exports
```

Default output directory:

```text
generation/search-exports/
```

Each export records:

- command line,
- parsed command and filters,
- working directory,
- game-data commit from the index manifest,
- indexes scanned,
- total matches before limiting,
- returned result count,
- warnings or no-match notes,
- readable returned output.

Human logs are output-only audit artifacts:

- The query script must never read them.
- Index generation must never depend on them.
- Runtime `SKILL.md` must not route Codex to use them as source truth.
- They exist only so a human can review what the searcher returned.

## Codex Usage Model

For API-sensitive Reforger work, Codex should:

1. Use `symbol` or `method` for exact API details.
2. Use `inherits` when choosing base classes or searching derived implementations.
3. Use `examples` for implementation patterns.
4. Use `--subtopic` when broad examples are too noisy.
5. Use `lookup` for common task-oriented bundles, then verify exact APIs from the returned symbol/method records.
6. Use `files` when exact symbol or topic is unclear.
7. Use `snippet` only after a query result provides a specific file and line.

Codex should not load `api-schema.json`, broad raw source directories, or human search exports during normal work.

## Validation Scenarios

The searcher is ready when these pass:

- `symbol ResourceName` returns the generated sealed class.
- `symbol ScriptComponent --kind class` returns generated class metadata.
- `method IEntity FindComponent` returns `proto external Managed FindComponent(typename typeName);`.
- `method Resource Load` returns `static proto ref Resource Load(ResourceName name);`.
- `method IEntity FindComponent --exact` returns only `IEntity.FindComponent`.
- `attribute RplProp --exact` returns the `RplProp` attribute API and members.
- `inherits ScriptedUserAction` returns handwritten user-action classes.
- `examples replication` returns `scripts/GameLib/replication/RplDocs.c` near the top.
- `examples workbench-plugin` returns Workbench plugin files.
- `examples resource-loading --subtopic spawn-prefab` returns records whose `subtopics` include `spawn-prefab`.
- `examples replication --with-snippets --limit 2` attaches bounded snippets to top results.
- `lookup "replicated component"` returns API symbols, inheritance candidates, examples, snippet commands, and verification notes.
- `lookup "create weapon script"` returns the weapon task, not user-action.
- `lookup "unknown made-up task"` returns an unmatched result and suggested searches.
- `examples weapon --subtopic magazine` returns handwritten weapon/magazine examples near the top.
- `examples vehicle --subtopic compartment` returns vehicle compartment examples near the top.
- `examples inventory --subtopic character-inventory` returns inventory examples near the top.
- `examples ui --subtopic hud` returns HUD/widget examples near the top.
- `files WorkbenchPlugin` returns generated and handwritten Workbench-related files.
- `snippet scripts/Game/CombatOps/SCR_FastTravelAction.c --line 1 --context 20` returns bounded numbered source.
- `--json` emits valid JSON for every command.
- `--human-log` writes readable Markdown and does not affect query results.
- Missing indexes fail cleanly.
- Broad queries remain bounded.
- Snippet rejects paths outside `raw/game-data/scripts/`.

The search quality validator is `scripts/tests/validate-reforger-search.py`. It should be run after searcher or indexer changes. It checks exact API anchors, attributes, inheritance, examples, subtopic filtering, bounded snippets, task lookup, JSON validity, and snippet path rejection. It can also pass `--human-log` through successful query cases for human review exports.

The usefulness benchmark is `scripts/tests/measure-reforger-search-usefulness.py`. It runs realistic task lookups, scores each task across API precision, example relevance, source grounding, context efficiency, routing safety, snippet usefulness, and verification guidance, then writes a human-review Markdown report. The report is an audit artifact only and must not become Codex source truth.

