# Reforger Game Data Indexer Design

This document is the detailed contract for the future game-data indexer. It is for Codex and future tooling implementation, not for human browsing. The indexer exists so Codex can write accurate Arma Reforger scripts without loading huge raw files or guessing APIs.

Do not implement the indexer inside `scripts/update-reforger-data.py`. The updater only checks and pulls raw game data. The future indexer must be a single Python script named `scripts/index-reforger-data.py`.

## Purpose

The indexer will parse `raw/game-data/scripts/` and generate compact lookup artifacts that later scripts can query.

Primary uses:

- Verify exact API signatures before Codex writes code.
- Route Codex to relevant raw source files and bounded snippets.
- Find implementation examples for common Reforger tasks.
- Generate runtime references and curated docs from source-grounded data.
- Separate generated signature truth from handwritten usage examples.

The indexer should do heavy lifting once, then let later query scripts use small JSONL files instead of repeatedly scanning thousands of `.c` files.

## Raw Data Review

Current raw game data at `raw/game-data` contains:

- `manifest.json`: local source commit and upstream repo metadata.
- `scripts/`: sparse checkout of BohemiaInteractive/Arma-Reforger-Script-Diff `scripts/`.

Observed corpus shape:

- `6495` `.c` files.
- Modules:
  - `Game`: largest module and broadest gameplay implementation surface.
  - `GameLib`: generated engine/game library APIs plus useful docs such as replication examples.
  - `Core`: low-level generated/proto APIs such as network attributes.
  - `WorkbenchGame`, `WorkbenchCommon`, `Workbench`, `WorkbenchGameCommon`: editor and Workbench APIs/examples.
  - `GameCode`: compact handwritten examples for user actions, world systems, components, and gameplay glue.
  - `Autotest`: test/support patterns, lower priority for ordinary scripting examples.
- About `1637` files are under `generated/`.

Interpretation for Codex:

- Generated files are strongest for exact signatures, inheritance, attributes, and available methods.
- Handwritten files outside `generated/` are strongest for implementation examples and real usage patterns.
- Documentation-style raw files such as `GameLib/replication/RplDocs.c` are high-value examples and should be indexed as example sources, not treated only as ordinary API files.

High-value anchors found in raw data:

- Entity/component APIs: `IEntity`, `GenericEntity`, `GenericComponent`, `ScriptComponent`, `ScriptComponentClass`.
- Replication APIs: `BaseRplComponent`, `RplComponent`, `RplProp`, `RplRpc`, `OnRpl`.
- User actions: `ScriptedUserAction`, `BaseUserAction`, `CanBeShownScript`, `PerformAction`.
- Workbench APIs: `WorkbenchPlugin`, `WorkbenchPluginAttribute`, Workbench module files.

## Ownership Boundary

`scripts/update-reforger-data.py` owns only:

- checking the remote upstream commit,
- pulling sparse `scripts/`,
- writing `raw/game-data/manifest.json`,
- deleting checkout artifacts.

`scripts/index-reforger-data.py` will own:

- parsing `.c` files,
- writing `raw/game-data/api-schema.json`,
- writing `raw/game-data/api-index.md`,
- writing compact JSONL lookup indexes,
- writing `raw/game-data/indexes/manifest.json`,
- deciding whether derived indexes are current.

Do not duplicate upstream freshness checks in the indexer. The indexer checks whether local derived files are stale relative to `raw/game-data/manifest.json`, the indexer version, and the index configuration.

## Output Files

The future indexer should write these files:

```text
raw/game-data/
  api-schema.json
  api-index.md
  indexes/
    symbols.jsonl
    files.jsonl
    examples.jsonl
    inheritance.jsonl
    manifest.json
```

`api-schema.json` is the complete structured parse. It can be large and should be treated as a build artifact for index generation and exhaustive fallback.

`api-index.md` is a broad fallback for manual or emergency search. Codex should not load it during normal work.

`indexes/*.jsonl` are the normal Codex lookup layer.

## Indexer Manifest

Write `raw/game-data/indexes/manifest.json`.

Required fields:

```json
{
  "generatedAt": "2026-07-08T00:00:00Z",
  "indexer": {
    "name": "index-reforger-data.py",
    "version": 1,
    "configVersion": 1
  },
  "gameData": {
    "repo": "https://github.com/BohemiaInteractive/Arma-Reforger-Script-Diff.git",
    "ref": "main",
    "commit": "full-commit",
    "sparsePath": "scripts"
  },
  "outputs": {
    "symbols": 0,
    "files": 0,
    "examples": 0,
    "inheritance": 0
  }
}
```

Staleness checks compare:

- `gameData.commit` against `raw/game-data/manifest.json.source.commit`.
- `indexer.version` against the current script constant.
- `indexer.configVersion` against the current index config constant.
- required output files exist.

## `symbols.jsonl`

Purpose: exact API lookup before Codex writes code.

One JSON object per class, enum, global function, method, and property.

Required fields:

```json
{
  "kind": "method",
  "name": "SetOrigin",
  "owner": "IEntity",
  "qualifiedName": "IEntity.SetOrigin",
  "signature": "proto external void SetOrigin(vector origin);",
  "returnType": "void",
  "parameters": [{"name": "origin", "type": "vector", "modifiers": [], "raw": "vector origin"}],
  "modifiers": ["proto", "external"],
  "attributes": [],
  "docs": [],
  "file": "scripts/Core/generated/Entities/IEntity.c",
  "line": 123,
  "module": "Core",
  "generated": true
}
```

For class records include:

- `kind: "class"` or `kind: "modded class"`,
- `name`,
- `extends`,
- `modifiers`,
- `attributes`,
- `docs`,
- `file`,
- `line`,
- `module`,
- `generated`.

For enum records include:

- `kind: "enum"`,
- `name`,
- `values` if practical,
- `file`,
- `line`,
- `module`,
- `generated`.

Keep docs bounded. Preserve enough doc text to disambiguate symbols, but do not dump long comments into JSONL.

## `files.jsonl`

Purpose: route Codex to relevant raw files without broad directory scans.

One JSON object per `.c` file.

Required fields:

```json
{
  "file": "scripts/GameCode/UserAction/LightUserAction.c",
  "module": "GameCode",
  "generated": false,
  "lineCount": 91,
  "declaredSymbols": ["LightUserAction"],
  "baseClasses": ["BaseLightUserAction"],
  "attributes": [],
  "topicTags": ["user-action"],
  "subtopics": ["scripted-user-action", "perform-action"],
  "evidence": ["ScriptedUserAction", "PerformAction"],
  "searchText": "LightUserAction BaseLightUserAction CanBeShownScript PerformAction"
}
```

`subtopics` are narrower, queryable task families under broad topics. `evidence` is a compact list of tokens that explain why the file matched. `searchText` should be compact and built from names, base classes, attributes, topic tags, subtopics, and evidence. It is not a full source dump.

## `examples.jsonl`

Purpose: find useful real implementation patterns.

One JSON object per example candidate. A file can produce multiple example records if it covers multiple task families.

Required fields:

```json
{
  "topic": "user-action",
  "subtopics": ["scripted-user-action", "perform-action"],
  "evidence": ["ScriptedUserAction", "PerformAction"],
  "file": "scripts/GameCode/UserAction/LightUserAction.c",
  "module": "GameCode",
  "generated": false,
  "symbols": ["LightUserAction"],
  "baseClasses": ["BaseLightUserAction"],
  "reason": "defines a user action override with CanBeShownScript and PerformAction",
  "suggestedLines": [1, 91],
  "priority": 80
}
```

Topic tags to support in the first version:

- `component`
- `entity-lifecycle`
- `transform`
- `user-action`
- `replication`
- `rpc`
- `rpl-prop`
- `workbench-plugin`
- `resource-loading`
- `prefab`
- `game-mode`
- `scenario-framework`
- `weapon`
- `vehicle`
- `inventory`
- `ui`
- `audio`
- `animation`

Subtopics should be compact and deterministic. Initial high-value subtopics:

- replication: `rpl-prop`, `rpc`, `authority`, `rpl-component`
- resources: `resource-load`, `spawn-prefab`, `resource-picker-config`, `ui-layout-resource`
- components: `script-component`, `game-component`, `lifecycle`
- user actions: `scripted-user-action`, `perform-action`, `can-be-shown`
- Workbench: `workbench-plugin`, `editor-ui`, `resource-browser`

Prioritization rules:

- Prefer handwritten files over generated files for examples.
- Prefer smaller files with direct patterns over large systems when both match.
- Prefer `GameCode`, `Game`, and Workbench handwritten files for implementation examples.
- Include documentation/example raw files such as replication docs when they contain explicit snippets.
- Penalize incidental broad-topic matches when a file is primarily about another system and better direct examples exist.
- Use generated files for signature examples only when no handwritten example exists.

## `inheritance.jsonl`

Purpose: help Codex choose correct base classes and find examples by inheritance.

One JSON object per class with an `extends` relationship.

Required fields:

```json
{
  "class": "ScriptComponent",
  "extends": "GenericComponent",
  "file": "scripts/GameLib/generated/Components/ScriptComponent.c",
  "line": 23,
  "module": "GameLib",
  "generated": true
}
```

The indexer may also include derived-class arrays if this can be done deterministically without making records too large. If included, keep the derived list sorted.

## Parsing Scope

The first version should parse enough Enfusion Script structure for Codex lookup:

- class declarations,
- modded class declarations,
- enum declarations,
- global functions,
- class methods,
- class properties,
- attributes immediately preceding declarations,
- doc comments immediately preceding declarations,
- inheritance,
- signatures,
- parameter names/types/modifiers.

Do not try to fully compile or semantically interpret Enfusion Script. The goal is robust indexing, not language-server correctness.

## Parsing Heuristics

Use line-oriented parsing with brace-depth tracking.

Rules:

- Only parse `.c` files under `raw/game-data/scripts/`.
- Normalize paths to forward slash form beginning with `scripts/`.
- `module` is the first path segment after `scripts/`.
- `generated` is true when `/generated/` appears in the normalized path.
- Capture pending doc comments and attributes, then attach them to the next declaration.
- Class member methods/properties should be captured only at direct class-member depth.
- Avoid treating control statements such as `if`, `for`, `while`, `switch`, and `foreach` as methods.
- Keep unresolved declarations as raw signatures rather than inventing missing types.

## Staleness Behavior

The indexer should support:

```powershell
py -3 scripts/index-reforger-data.py --check
py -3 scripts/index-reforger-data.py --if-needed
py -3 scripts/index-reforger-data.py
```

Exit codes:

- `0`: indexes current, or indexing completed successfully.
- `10`: indexes missing or stale when using `--check`.
- `2`: status cannot be determined.

`--check` must not write files.

`--if-needed` must skip all parsing when indexes are current.

Plain invocation rebuilds all index artifacts unconditionally.

## Codex Usage Model

Codex should use these outputs in this order:

1. Read topical runtime docs for system understanding and lookup keys.
2. Query `symbols.jsonl` for exact class/method/property/enum signatures.
3. Query `inheritance.jsonl` when choosing a base class or finding derived examples.
4. Query `examples.jsonl` for implementation patterns.
5. Query `files.jsonl` to locate raw files by module/topic/symbol.
6. Open bounded snippets from raw source only after indexes identify exact files and lines.

Codex must not use examples as signature authority. It must verify signatures in `symbols.jsonl` or generated source.

## Validation Requirements

A future implementation must validate:

- `symbols.jsonl` includes `IEntity`, `ScriptComponent`, `ScriptComponentClass`, `BaseRplComponent`, `RplProp`, `RplRpc`, and `WorkbenchPlugin`.
- `files.jsonl` includes module, generated/non-generated classification, topic tags, subtopics, and compact evidence.
- `examples.jsonl` includes example records for `user-action`, `replication`, `component`, and `workbench-plugin`.
- `examples.jsonl` includes subtopics and evidence for high-value task families such as `spawn-prefab`, `rpl-prop`, `rpc`, `scripted-user-action`, and `workbench-plugin`.
- `inheritance.jsonl` includes:
  - `ScriptComponent -> GenericComponent`,
  - `GenericEntity -> IEntity`,
  - `RplComponent -> BaseRplComponent`.
- `--check` reports stale when `raw/game-data/manifest.json.source.commit` differs from the index manifest.
- `--check` reports stale when indexer version or config version changes.
- `--if-needed` skips work when all versions and outputs are current.
- `scripts/validate-reforger-search.py` passes after rebuilding indexes.

## Failure Modes To Avoid

- Loading full `api-schema.json` during ordinary Codex work.
- Treating generated API files as implementation examples when better handwritten examples exist.
- Treating handwritten examples as signature truth.
- Returning source dumps instead of compact file/line references.
- Creating many small scripts with overlapping responsibilities.
- Duplicating upstream game-data freshness logic from `update-reforger-data.py`.
- Inventing APIs when parsing fails.

## Non-Goals

Do not include these in the first indexer:

- Interactive query UI.
- Embeddings or vector search.
- Full Enfusion semantic analysis.
- Rewriting runtime references.
- Updating `SKILL.md`.
- Fetching upstream game data.
