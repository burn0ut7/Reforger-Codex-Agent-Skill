# Low-Context Game Data Lookup Tooling

This document is the detailed tooling contract for making the Reforger skill useful to Codex without bloating context. It is written for future skill generation and tooling implementation, not for human browsing. Future `SKILL.md` and runtime references must be generated from this model instead of routing Codex toward large API dumps.

## Goal

Codex needs accurate Reforger scripts, not broad prose. The skill should route Codex to the smallest useful context, then force exact lookup against generated indexes or raw game source before Codex writes API-sensitive code.

The game data exists to answer specifics:

- Which class exists?
- Which method signature is valid?
- Which base class or generated class pair is required?
- Which attributes, callbacks, enums, and resource types are present?
- Which official or game-source file shows a real pattern?
- Which exact source file and line should Codex inspect before answering?

The game data must not be turned into one huge always-read markdown reference. That creates context bloat and encourages Codex to skim or guess.

## Layered Context Model

Use four layers. Codex should stop at the first layer that contains enough information for the current decision, then move deeper only for specifics.

### Layer 1: Router

The router is the future `SKILL.md` or agent entrypoint. It must be compact.

Responsibilities:

- Classify the task as script-first, data-first, editor-first, server-first, asset-first, or mixed.
- Select the smallest relevant topical reference.
- Require exact API lookup before writing Reforger code.
- Require raw example lookup when examples or implementation patterns matter.
- Tell Codex to state residual Workbench, runtime, multiplayer, dedicated-server, or packaging verification.

The router must not contain topic detail, API dumps, raw paths, provenance tables, or long examples.

### Layer 2: Topical Runtime Docs

Topical docs provide the general understanding Codex needs to choose the right implementation surface.

They should answer:

- Which Reforger system is involved?
- Is the work script-first, data-first, editor-first, server-first, asset-first, or mixed?
- Which Workbench/resource/config/prefab/server steps may be required?
- Which exact search terms should Codex use next?
- Which classes, methods, file names, or example families are likely relevant?
- Which common traps should Codex avoid?

Topical docs should guide lookup instead of embedding exhaustive source data. They may include short, curated examples, but they should not copy large raw game-source bodies or generated API dumps.

Each topical doc should include a small lookup section with:

- API search terms.
- Class names.
- Method names.
- Attribute names.
- File-name patterns.
- Example family names.
- Expected raw-data locations at the conceptual level, such as `Game`, `GameCode`, `Workbench`, or `GameLib`.

Runtime references must avoid local machine-specific raw paths. Generation docs and review docs may mention raw paths.

### Layer 3: Generated Lookup Indexes

Generated indexes are the normal exact-lookup layer for Codex. They should be compact, deterministic, and queryable without loading full `api-schema.json`.

Recommended generated files under `raw/game-data/indexes/`:

- `symbols.jsonl`: one record per class, enum, function, method, and property.
- `files.jsonl`: one record per source file with module, declared symbols, likely topic tags, and path.
- `examples.jsonl`: one record per likely example file or source pattern.
- `inheritance.jsonl`: optional class-to-base and base-to-derived lookup if `symbols.jsonl` is not enough.

Indexes should be regenerated from:

- `raw/game-data/scripts/`
- `raw/game-data/api-schema.json`
- optional sample cache under `raw/samples/`
- optional wiki/doc inventory under `raw/wiki-docs/`

Indexes must prefer exact file and line references over copied text. They should be small enough for a lookup tool to return bounded matches directly into context.

### Layer 4: Raw Script And Source Layer

Raw source is the final specificity layer.

Primary source:

- `raw/game-data/scripts/`, sparse-checked-out from `BohemiaInteractive/Arma-Reforger-Script-Diff`.

Optional source:

- `raw/samples/`, official sample mods.
- `raw/wiki-docs/`, official docs cache.

Codex should open raw files only after a targeted lookup identifies relevant candidates. It should inspect bounded snippets around exact lines, not load broad directories or entire large files unless the file is already small and directly relevant.

## Mandatory API Rule

Codex must not guess Reforger APIs.

Before writing, modifying, or reviewing API-sensitive Reforger code, Codex must verify exact API details using at least one of:

- generated lookup indexes,
- the query helper over those indexes,
- direct `rg` search under `raw/game-data/scripts/`,
- direct inspection of specific raw source files,
- curated `api-main.md` only when it was built from the same raw data and contains the exact signature needed.

API-sensitive details include:

- class names,
- method names,
- method parameters,
- return types,
- class inheritance,
- component class pairs,
- event callback names,
- attributes and annotations,
- enum names and values,
- resource/config types,
- replication/RPC declarations,
- Workbench plugin APIs.

If lookup cannot verify a detail, Codex must label the uncertainty and avoid presenting the code as final exact Reforger API code.

## Intended Data Flow

The extractor should pull game script data from Git and generate progressively smaller lookup products.

Flow:

1. Pull or update `BohemiaInteractive/Arma-Reforger-Script-Diff`.
2. Use `raw/game-data` as the single local game-data directory and temporary Git checkout location.
3. Sparse-checkout only upstream `scripts/` into `raw/game-data/scripts/`.
4. Write `raw/game-data/manifest.json` with the source repo, ref, commit, sparse path, and cleanup behavior.
5. Delete only `.git`, `README.md`, and `LICENSE` inside `raw/game-data`.
6. Later, a dedicated indexer reads `raw/game-data/scripts/` and generates schema, compact JSONL lookup indexes, and any markdown fallback artifacts according to `generation/indexer-game-data.md`.
7. Query indexes for symbols, methods, files, examples, and snippets.
8. Inspect raw snippets for implementation-specific patterns.

Do not maintain a second raw source cache such as `raw/source-cache`. During refresh, the updater may initialize sparse Git metadata inside `raw/game-data`, but after data is pulled it must delete only these checkout artifacts inside `raw/game-data`: `.git`, `README.md`, and `LICENSE`. Freshness checks must rely on `raw/game-data/manifest.json`, not a persistent local Git checkout.

The game-data updater must also support cheap freshness checks:

- `py -3 scripts/update-reforger-data.py --check` compares the local manifest or checkout commit with the remote Git ref and does not fetch, checkout, parse, or write files.
- `py -3 scripts/update-reforger-data.py --if-needed` performs the same check first, skips all work when local game data is current, and pulls raw scripts only when local data is missing or remote data changed.
- Exit code `0` means game data is current or the requested update completed successfully.
- Exit code `10` from `--check` means local game data is missing or remote data is newer.
- Exit code `2` from `--check` means status could not be determined.

Game-data freshness and index freshness are separate responsibilities. `update-reforger-data.py` owns upstream game-data freshness. A later indexer should follow `generation/indexer-game-data.md`, compare its own index manifest against `raw/game-data/manifest.json`, and rebuild indexes only when the game-data commit, indexer version, or index configuration changes.

The raw schema may be large. It must be produced by the future indexer, not by `update-reforger-data.py`. Codex should not load it directly during ordinary work; it is an intermediate artifact for deterministic index generation and exhaustive fallback.

## Proposed Lookup Surfaces

Provide a deterministic command-line helper, `scripts/query-reforger-data.py`. `generation/searcher-game-data.md` is the detailed contract for this searcher, including command behavior, ranking, output limits, and human-only search export rules.

### Symbol Lookup

Purpose: find classes, enums, functions, properties, and methods by exact or fuzzy name.

Example shape:

```powershell
py -3 scripts\query-reforger-data.py symbol ScriptComponent
py -3 scripts\query-reforger-data.py symbol SCR_BaseGameMode
py -3 scripts\query-reforger-data.py symbol ResourceName --exact
```

Output should include:

- symbol kind,
- name,
- owner class for methods/properties,
- signature when available,
- inheritance when available,
- file path,
- line number,
- short doc/attribute summary when available.

Default output should be bounded. Prefer top exact matches first, then prefix matches, then contains matches.

### Method Lookup

Purpose: verify callable signatures and owner classes.

Example shape:

```powershell
py -3 scripts\query-reforger-data.py method IEntity SetOrigin
py -3 scripts\query-reforger-data.py method GetOwner
py -3 scripts\query-reforger-data.py method IEntity FindComponent --exact
```

Output should include:

- owner class,
- method name,
- full signature,
- modifiers,
- source file and line,
- inherited/derived context if indexed.

When method lookup is ambiguous, Codex should inspect the likely owner class and related examples before writing code.

Use `--exact` when Codex already knows the API name it needs to verify and must avoid prefix or contains matches.

### Attribute Lookup

Purpose: verify annotation classes and constructor signatures.

Example shape:

```powershell
py -3 scripts\query-reforger-data.py attribute RplProp --exact
py -3 scripts\query-reforger-data.py attribute RplRpc --exact
```

Output should include the attribute class, constructor signature, fields/properties, source file and line, and docs when available.

### File Lookup

Purpose: find raw source files by topic, class, keyword, or file-name pattern.

Example shape:

```powershell
py -3 scripts\query-reforger-data.py file WorkbenchPlugin
py -3 scripts\query-reforger-data.py file UserAction
```

Output should include:

- file path,
- module or top-level script folder,
- declared classes/enums/functions,
- topic tags if generated,
- match reason.

### Example Lookup

Purpose: identify useful real implementation patterns without loading whole sample or game directories.

Example shape:

```powershell
py -3 scripts\query-reforger-data.py example component
py -3 scripts\query-reforger-data.py example replication
py -3 scripts\query-reforger-data.py example workbench-plugin
py -3 scripts\query-reforger-data.py example user-action
```

Example records should be generated from game source, official samples, or both.

Output should include:

- example topic,
- file path,
- relevant symbols,
- why it matched,
- suggested snippet lines when available.

Examples are not authority over signatures by themselves. Codex must still verify current API symbols from the generated game data.

### Bounded Source Snippet Lookup

Purpose: inspect exact raw source context without loading large files.

Example shape:

```powershell
py -3 scripts\query-reforger-data.py snippet raw/game-data/scripts/GameCode/UserAction/ActionsManagerComponent.c --line 5 --context 20
```

Output should include:

- normalized file path,
- requested line range,
- source excerpt with line numbers.

The helper must prevent huge accidental output by enforcing a default maximum context window and a hard maximum line count.

## Context-Bloat Controls

The tooling must be designed around bounded output.

Rules:

- Do not load full `raw/game-data/api-schema.json` during normal Codex work.
- Do not route normal work to `references/api-extended.md`.
- Do not ask Codex to read all of `raw/game-data/api-index.md`.
- Prefer query output with file and line references over copied source.
- Return bounded matches by default.
- Return bounded snippets by default.
- Prefer exact class/method/file searches over broad topic searches.
- Use subtopic filters or task lookup when broad example topics return too many mixed-system matches.
- Read one topical reference at a time unless the task is clearly cross-system.
- Use `rg` when query tooling is missing or insufficient.
- Use raw source inspection only after narrowing candidates.

Suggested defaults:

- Symbol lookup: return at most 20 matches.
- Method lookup: return at most 20 matches.
- File lookup: return at most 30 matches.
- Example lookup: return at most 12 examples.
- Task lookup: return one bounded task bundle.
- Snippet lookup: default 20 context lines, hard cap 100 total lines.

When a lookup returns too many candidates, Codex should refine the query rather than dump more context.

## How Topical Docs Should Point Into Raw Data

Topical docs should contain lookup keys, not large copied code blocks.

Each topical reference should include a section like `## Lookup Keys` with:

- key classes,
- key methods,
- key attributes,
- key enums,
- file-name patterns,
- example topics,
- example subtopics,
- source modules,
- useful `rg` fallback patterns.

Example for entity/component work:

```text
Lookup keys:
- Classes: ScriptComponent, ScriptComponentClass, GenericComponent, GenericEntity, IEntity
- Methods: GetOwner, EOnInit, OnPostInit, SetEventMask, GetOrigin, SetOrigin, GetTransform, SetTransform
- Attributes: ComponentEditorProps, Attribute
- Example topics: component, entity-lifecycle, transform
- Example subtopics: script-component, game-component, lifecycle
- Source modules: Game, GameCode
```

Example for replication:

```text
Lookup keys:
- Classes: BaseRplComponent, RplComponent
- Attributes: RplProp, RplRpc, OnRpl
- Terms: authority, proxy, owner, reliable, broadcast, JIP
- Example topics: replication, rpc, rpl-prop
- Example subtopics: rpl-component, rpl-prop, rpc, authority
```

Example for Workbench plugins:

```text
Lookup keys:
- Classes: WorkbenchPlugin, WorkbenchPluginAttribute, WorldEditor, ResourceManager, ScriptEditor
- Methods: Run, RunCommandline
- Example topics: workbench-plugin
- Example subtopics: workbench-plugin, editor-ui, resource-browser
- Source modules: Workbench, WorkbenchCommon, WorkbenchGame, WorkbenchGameCommon
```

Docs should also say which raw examples are useful by family, not by local absolute path.

## Expected Future `SKILL.md` Behavior

Future `SKILL.md` should be generated after the tooling and references are designed. It should be compact.

It should instruct Codex to:

1. Classify the task surface.
2. Read the smallest relevant topical reference.
3. Query exact game data for API-sensitive symbols.
4. Use task lookup or subtopic filters when a common workflow needs a compact API/example bundle.
5. Query examples when pattern or layout matters.
6. Inspect bounded raw snippets before writing final code.
7. Include data/prefab/config/Workbench/server steps alongside script code when relevant.
8. State residual verification needed.

It should not:

- embed the full tooling design,
- embed large API lists,
- point Codex to read `api-extended.md` by default,
- include raw provenance tables,
- include local absolute paths,
- treat examples as signature truth.

## Accuracy Policy

Codex should treat source authority this way:

1. Official docs and wiki define workflows, rules, and editor procedures.
2. Current extracted game API data defines exact signatures, classes, inheritance, and attributes.
3. Official samples and raw game scripts define implementation patterns.
4. Existing project code defines local conventions.

If sources conflict:

- API data wins for signatures.
- Docs win for workflows.
- Samples provide examples, not universal rules.
- Project code wins for local style unless it is incompatible with current API data.

## Failure Modes This Tooling Must Prevent

Avoid these failure modes:

- Codex reads a huge generated file and misses the one relevant signature.
- Codex guesses Unity, Unreal, Arma 3, or C# behavior.
- Codex writes plausible Enfusion-like code with nonexistent callbacks.
- Codex copies an old sample pattern without checking current API data.
- Codex solves a data-first prefab/config problem with unnecessary script.
- Codex omits Workbench, Resource Manager, server, or packaging verification.
- Codex loads so much raw source that useful context is displaced.

## Implementation Notes For Future Tooling

`generation/indexer-game-data.md` is the source of truth for the future indexer script. The notes below are retained as compact examples of the intended JSONL record shapes.

Index generation should be deterministic and fast.

Recommended symbol record fields:

```json
{
  "kind": "method",
  "name": "SetOrigin",
  "owner": "IEntity",
  "signature": "proto external void SetOrigin(vector origin);",
  "returnType": "void",
  "parameters": [{"name": "origin", "type": "vector"}],
  "modifiers": ["proto", "external"],
  "file": "scripts/Game/generated/Entities/IEntity.c",
  "line": 123,
  "docs": [],
  "attributes": []
}
```

Recommended file record fields:

```json
{
  "file": "scripts/GameCode/UserAction/ActionsManagerComponent.c",
  "module": "GameCode",
  "symbols": ["ActionsManagerComponent", "ActionsManagerComponentClass"],
  "topics": ["user-action", "component"],
  "lineCount": 42
}
```

Recommended example record fields:

```json
{
  "topic": "workbench-plugin",
  "file": "scripts/WorkbenchCommon/AddonBuildInfoTool.c",
  "symbols": ["AddonBuildInfoTool"],
  "reason": "extends WorkbenchPlugin",
  "suggestedLines": [1, 80]
}
```

The query helper should read JSONL indexes, not parse the full raw schema on every query.

## Validation For Future Implementation

A later tooling implementation should pass these checks:

- `symbol ScriptComponent` returns class metadata and source line.
- `method IEntity SetOrigin` returns exact signature candidates.
- `example user-action` returns bounded relevant files.
- `example workbench-plugin` returns Workbench plugin examples.
- `snippet <file> --line <n>` returns line-numbered bounded source.
- Normal Codex workflows do not require opening `api-extended.md`.
- Lookup output is small enough to include in a single answer context.
