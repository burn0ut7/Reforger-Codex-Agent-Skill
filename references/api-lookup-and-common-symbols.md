# API Lookup And Common Symbols

## When To Read

Read this when a Reforger task needs exact API names, signatures, inheritance, attributes, examples, file routes, or source snippets.

Use this reference for:

- choosing the right `scripts\query-reforger-data.py` command;
- verifying exact classes, methods, attributes, properties, return types, parameters, inheritance, files, and examples;
- finding bounded source snippets after query output gives a concrete file and line;
- routing common API anchors such as entities, components, resources, replication, and Workbench plugins;
- avoiding broad context loads and API guessing.

Do not use this as a workflow reference. Read the source-owning reference first for the task, then use this file for exact lookup. This reference intentionally does not own scripting patterns, entity/component lifecycle, prefab/config/resource workflows, replication behavior, Workbench plugin authoring, domain setup, or verification workflows.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: none. This is a utility reference for query behavior and common API routing.
- Secondary/cross-reference topics: language/editor, scripting patterns, entity/component lifecycle, resources/prefabs/configs, replication, Workbench plugins, and examples only as lookup-route context.

Wiki pages reviewed:
- No primary wiki pages are owned by this reference - status: excluded - reason: exact API truth comes from current game-data query output; workflow truth belongs to source-owning references.
- Start-here/source authority reference - status: covered - reason: confirms lookup-first behavior and reference routing boundary.
- Enfusion language and Script Editor reference - status: covered - reason: confirms language/API claims must be verified rather than guessed.
- Script events/actions reference - status: covered - reason: confirms script-pattern tasks use query output for exact methods and snippets.

Wiki sections covered:
- No wiki source sections are owned here. This utility reference routes to source-owning references instead of copying wiki workflow sections.

Structured wiki records:
- Tables reviewed/included: none as owned content; command tables below are generated from query tool behavior and verified anchors.
- Procedures reviewed/included: no wiki procedures owned; lookup procedures are tool-operation guidance.
- Admonitions reviewed/included: source-authority and no-guessing rules are represented as runtime warnings.
- Code blocks reviewed/included: query command examples only.
- Media reviewed: not applicable.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts\query-reforger-data.py symbol IEntity --kind class --exact`
  - `py -3 scripts\query-reforger-data.py method IEntity FindComponent --exact`
  - `py -3 scripts\query-reforger-data.py symbol GenericEntity --kind class --exact`
  - `py -3 scripts\query-reforger-data.py symbol GenericComponent --kind class --exact`
  - `py -3 scripts\query-reforger-data.py symbol ScriptComponent --kind class --exact`
  - `py -3 scripts\query-reforger-data.py symbol ScriptComponentClass --kind class --exact`
  - `py -3 scripts\query-reforger-data.py symbol ResourceName --exact`
  - `py -3 scripts\query-reforger-data.py method Resource Load --exact`
  - `py -3 scripts\query-reforger-data.py attribute RplProp --exact`
  - `py -3 scripts\query-reforger-data.py attribute RplRpc --exact`
  - `py -3 scripts\query-reforger-data.py symbol RplComponent --kind class --exact`
  - `py -3 scripts\query-reforger-data.py symbol BaseRplComponent --kind class --exact`
  - `py -3 scripts\query-reforger-data.py symbol WorkbenchPlugin --kind class --exact`
  - `py -3 scripts\query-reforger-data.py examples workbench-plugin --limit 10`
  - `py -3 scripts\query-reforger-data.py lookup "make a user action"`
  - `py -3 scripts\query-reforger-data.py lookup "make a replicated component"`
  - `py -3 scripts\query-reforger-data.py lookup "spawn prefab"`
  - `py -3 scripts\query-reforger-data.py lookup "load resource"`
  - `py -3 scripts\query-reforger-data.py lookup "workbench plugin"`
- Symbols/methods/attributes verified: `IEntity`, `IEntity.FindComponent`, `GenericEntity`, `GenericComponent`, `ScriptComponent`, `ScriptComponentClass`, `ResourceName`, `Resource.Load`, `RplProp`, `RplRpc`, `RplComponent`, `BaseRplComponent`, `WorkbenchPlugin`, and task lookup bundles.
- Examples/snippets reviewed: Workbench plugin example output and task lookup suggested snippets. No source bodies are copied.

Samples and source examples:
- Official sample folders reviewed: none directly required for this utility reference.
- Game-source example families reviewed through query output: Workbench plugin examples, user-action examples, replication examples, resource-loading examples.

Coverage gaps:
- Missing, excluded, or intentionally deferred source: workflow wiki pages, full API schema, large API indexes, full sample trees, and broad source files.
- Reason and impact: this reference exists to prevent context bloat. It points Codex to exact query commands and source-owning references instead of embedding workflow or API dumps.

## Wiki Source Coverage

This utility reference owns no primary wiki pages. That is intentional.

Workflow source authority remains with the source-owning references. Use this file only after the relevant workflow reference has established what kind of Reforger work is being performed.

Source authority split:

| Need | Source |
| --- | --- |
| Workflow, editor steps, warnings, data surfaces | Relevant runtime reference |
| Exact class/method/attribute/property signature | `scripts\query-reforger-data.py` output |
| Inheritance and correct base class | `inherits` query output |
| Implementation pattern | `examples`, `lookup`, then bounded `snippet` |
| Resource/prefab existence or editor wiring | Workbench/runtime verification |
| Multiplayer/authority behavior | Networking reference plus runtime/server verification |

Do not turn this file into a copied API reference. The useful output is a small set of command patterns and common lookup keys.

## Terms And Concepts

- Exact lookup: a query with `--exact` when the symbol/method/attribute name is known and false positives would be harmful.
- Symbol lookup: search for classes, enums, functions, methods, and properties by name.
- Method lookup: search for a method by optional owner and method name.
- Attribute lookup: search for annotation attributes and their constructor/properties.
- Inheritance lookup: find base and derived classes for choosing correct extension points and examples.
- File lookup: find source files by symbol, topic, module, or path text.
- Example lookup: find handwritten implementation files tagged by topic and subtopic.
- Task lookup: deterministic bundle of likely APIs, inheritance, examples, snippets, and verification notes for common tasks.
- Bounded snippet: line-numbered source excerpt from a known file and line, used only after query output points there.
- Generated API truth: generated records are usually best for exact signatures.
- Handwritten example truth: handwritten game/workbench files are usually best for implementation shape.
- Residual verification: Workbench, runtime, dedicated-server, multiplayer, packaging, or editor validation that query output cannot prove.

## Workbench / Resource / Data Surfaces

This reference has no Workbench editor surface of its own.

Use these routing rules:

| Task surface | Read first | Then query |
| --- | --- | --- |
| Broad source authority | `start-here-source-authority.md` | `lookup "<task phrase>"` |
| Language/syntax/API decorators | `enfusion-language-and-script-editor.md` | `symbol`, `method`, `attribute` |
| Gameplay script/user action | `script-events-actions-and-patterns.md` | `lookup`, `method`, `examples`, `snippet` |
| Entity/component lifecycle | `entities-components-and-lifecycle.md` | `symbol`, `inherits`, `examples component` |
| Resource/prefab/config | `resource-manager-file-types-and-editors.md` and `prefabs-configs-containers-and-catalogs.md` | `symbol ResourceName`, `method Resource Load`, `lookup "spawn prefab"` |
| Replication/multiplayer | `multiplayer-replication-and-authority.md` | `attribute RplProp`, `attribute RplRpc`, `lookup "make a replicated component"` |
| Workbench plugin | `workbench-plugins-and-editor-tools.md` | `symbol WorkbenchPlugin`, `examples workbench-plugin` |
| Domain workflow | narrow domain reference | `examples <topic>`, `files <query>`, `snippet` |

Query output can prove current API names and source locations. It cannot prove that a resource exists in the user's addon, that a prefab is wired correctly, that Workbench registration appears in UI, or that server/client behavior is correct.

## Required Workflows

### API-Sensitive Code Workflow

1. Read the relevant source-owning reference in full.
2. Identify every uncertain class, method, attribute, enum, property, callback, or base class.
3. Query exact symbols and methods before writing code.
4. Use generated records for signatures.
5. Use handwritten examples for implementation patterns.
6. Open bounded snippets only for files and lines returned by query output.
7. Write the smallest local change that preserves current behavior.
8. State any Workbench/runtime/server verification that remains.

### Choosing The Right Query

1. If the task is broad, use `lookup "<task phrase>"`.
2. If the exact class/type name is known, use `symbol <name> --exact`.
3. If the exact method owner is known, use `method <Owner> <Name> --exact`.
4. If the target is an annotation/decorator, use `attribute <Name> --exact`.
5. If choosing a base class or finding implementations, use `inherits <Class>`.
6. If looking for implementation patterns, use `examples <topic>` with `--subtopic` where possible.
7. If looking for source locations by name/path/topic, use `files <query>`.
8. If more context is needed, use `snippet <file> --line <n> --context <n>`.

### Avoiding Context Bloat

1. Do not load full schema files for normal work.
2. Do not open broad source files before query output identifies a target.
3. Prefer exact queries over broad contains searches.
4. Prefer `--limit` on exploratory commands.
5. Prefer snippets of 20-40 lines for examples; increase only when the returned pattern requires it.
6. Query again with a better term instead of opening many unrelated files.
7. Keep human log exports out of Codex source reasoning unless the user explicitly asks to review logs as audit artifacts.

## Configuration Fields And Tables

Command selection table:

| Need | Command shape |
| --- | --- |
| Exact class/type/function/property | `py -3 scripts\query-reforger-data.py symbol <Name> --exact` |
| Class only | `py -3 scripts\query-reforger-data.py symbol <Name> --kind class --exact` |
| Exact owner method | `py -3 scripts\query-reforger-data.py method <Owner> <Method> --exact` |
| Attribute/decorator API | `py -3 scripts\query-reforger-data.py attribute <Name> --exact` |
| Base and derived classes | `py -3 scripts\query-reforger-data.py inherits <Class>` |
| Implementation examples | `py -3 scripts\query-reforger-data.py examples <topic> --limit 10` |
| Narrow example family | `py -3 scripts\query-reforger-data.py examples <topic> --subtopic <subtopic> --limit 10` |
| File discovery | `py -3 scripts\query-reforger-data.py files <query> --limit 20` |
| Bounded source excerpt | `py -3 scripts\query-reforger-data.py snippet <scripts/...file.c> --line <n> --context 30` |
| Common task bundle | `py -3 scripts\query-reforger-data.py lookup "<task phrase>"` |
| Machine-readable result | add `--json` where supported by the command |

Filter table:

| Filter | Use |
| --- | --- |
| `--exact` | Known name; prevent prefix/contains noise. |
| `--limit <n>` | Keep output bounded. |
| `--kind class` | Restrict symbol lookup to classes. |
| `--module <name>` | Narrow by script module when needed. |
| `--topic <topic>` | Narrow examples/files by topic when available. |
| `--subtopic <subtopic>` | Narrow example families after tags exist. |
| `--generated-only` | Prefer generated API signatures. |
| `--handwritten-only` | Prefer implementation examples. |
| `--json` | Use for script-readable or validation output. |

Common topic names:

| Topic | Typical use |
| --- | --- |
| `component` | script/game component examples. |
| `user-action` | `ScriptedUserAction` examples. |
| `replication` | `RplProp`, `RplRpc`, replicated component examples. |
| `resource-loading` | `ResourceName`, `Resource.Load`, prefab/resource load examples. |
| `workbench-plugin` | Workbench plugin examples. |
| `prefab` | prefab-related source examples. |
| `game-mode` | game mode and scenario logic examples. |
| `weapon`, `vehicle`, `inventory`, `ui`, `audio`, `animation`, `ai` | domain examples. |

## Procedures And Ordered Steps

Exact API lookup procedure:

1. Extract the exact candidate name from the task/reference/local code.
2. Run an exact `symbol`, `method`, or `attribute` query.
3. Prefer generated results for signatures.
4. Record the file and line from query output.
5. If multiple valid results exist, pick the one matching the module/workflow reference.
6. If no exact match exists, search with `files` or broader `symbol` and revise the candidate name.
7. Do not write API-sensitive code until the exact lookup succeeds or the uncertainty is explicitly stated.

Example lookup procedure:

1. Identify the topic and subtopic from the owning reference.
2. Run `examples <topic>` with a low limit.
3. Prefer handwritten files for implementation patterns.
4. Inspect the returned `reason`, `evidence`, `symbols`, `bases`, and file/line.
5. Open one bounded snippet near the returned line.
6. Do not copy the example blindly; verify exact APIs separately.

Task lookup procedure:

1. Use `lookup "<task phrase>"` for common tasks.
2. Read returned verification notes first.
3. Verify returned symbols/methods separately when writing code.
4. Inspect one or two suggested snippets.
5. Read the owning workflow reference when the lookup indicates a workflow surface.
6. If lookup returns unmatched or irrelevant results, fall back to exact `symbol`, `files`, or `examples` queries instead of trusting the bundle.

Snippet procedure:

1. Use only file paths returned by query output.
2. Keep context around 20-40 lines by default.
3. Increase context only when the pattern crosses more lines.
4. Do not use snippets as a replacement for exact symbol/method lookup.
5. Do not infer unrelated lifecycle, authority, or Workbench behavior from one snippet.

## Warnings And Failure Modes

- Do not guess Reforger APIs.
- Do not assume Unity, Unreal, C#, or Arma 3 API names apply.
- Do not use this utility reference instead of the workflow-owning reference.
- Do not turn broad `files` matches into API truth.
- Do not treat examples as signature truth.
- Do not paste large snippets or source bodies into runtime references or answers.
- Do not load broad API schema/index files for normal work.
- Do not trust an unbounded search when an exact query is available.
- Do not assume generated and handwritten records have the same purpose: generated is signature truth, handwritten is pattern truth.
- Do not assume a successful lookup proves Workbench wiring, prefab registration, resource existence, multiplayer authority, or dedicated-server behavior.
- Do not use `--json` output as a reason to attach more context than needed.
- Do not read human-log exports as source truth; they are audit artifacts only.

## API Lookup Keys

Use these common anchors to start exact lookup. This is a key list, not an API dump.

Entity/component anchors:

- `IEntity`
- `GenericEntity`
- `GenericComponent`
- `ScriptComponent`
- `ScriptComponentClass`
- `GenericComponentClass`
- `FindComponent`
- `FindComponents`
- `OnPostInit`
- `EOnInit`
- `EOnFrame`
- `SetEventMask`

Resource/prefab/config anchors:

- `ResourceName`
- `Resource`
- `Resource.Load`
- `PrefabResource`
- `EntitySpawnParams`
- `SpawnEntityPrefab`
- `BaseContainer`
- `BaseContainerProps`
- `Attribute`
- `UIWidgets`
- `EntityCatalog`

Replication anchors:

- `BaseRplComponent`
- `RplComponent`
- `RplProp`
- `RplRpc`
- `RplGroup`
- `RplChannel`
- `RplRcver`
- `RplCondition`
- `RplSession`
- `RplMode`

Script pattern anchors:

- `ScriptedUserAction`
- `BaseUserAction`
- `PerformAction`
- `CanBeShownScript`
- `CanBePerformedScript`
- `ScriptInvoker`
- `Print`
- `DbgUI`

Workbench anchors:

- `WorkbenchPlugin`
- `WorkbenchPluginAttribute`
- `Workbench`
- `ResourceManager`
- `WorldEditor`
- `WorldEditorPlugin`
- `WorldEditorTool`
- `ScriptEditor`

Domain anchors should be taken from the owning reference and verified with query output before use.

## Game-Data Query Commands

Entity and component anchors:

```powershell
py -3 scripts\query-reforger-data.py symbol IEntity --kind class --exact
py -3 scripts\query-reforger-data.py method IEntity FindComponent --exact
py -3 scripts\query-reforger-data.py symbol GenericEntity --kind class --exact
py -3 scripts\query-reforger-data.py symbol GenericComponent --kind class --exact
py -3 scripts\query-reforger-data.py symbol ScriptComponent --kind class --exact
py -3 scripts\query-reforger-data.py symbol ScriptComponentClass --kind class --exact
py -3 scripts\query-reforger-data.py inherits ScriptComponent
py -3 scripts\query-reforger-data.py examples component --subtopic script-component --limit 10
```

Resource and prefab anchors:

```powershell
py -3 scripts\query-reforger-data.py symbol ResourceName --exact
py -3 scripts\query-reforger-data.py symbol Resource --kind class --exact
py -3 scripts\query-reforger-data.py method Resource Load --exact
py -3 scripts\query-reforger-data.py lookup "load resource"
py -3 scripts\query-reforger-data.py lookup "spawn prefab"
py -3 scripts\query-reforger-data.py examples resource-loading --limit 10
```

Replication anchors:

```powershell
py -3 scripts\query-reforger-data.py attribute RplProp --exact
py -3 scripts\query-reforger-data.py attribute RplRpc --exact
py -3 scripts\query-reforger-data.py symbol RplComponent --kind class --exact
py -3 scripts\query-reforger-data.py symbol BaseRplComponent --kind class --exact
py -3 scripts\query-reforger-data.py lookup "make a replicated component"
py -3 scripts\query-reforger-data.py examples replication --limit 10
```

Script actions and patterns:

```powershell
py -3 scripts\query-reforger-data.py lookup "make a user action"
py -3 scripts\query-reforger-data.py inherits ScriptedUserAction
py -3 scripts\query-reforger-data.py method ScriptedUserAction PerformAction --exact
py -3 scripts\query-reforger-data.py method ScriptedUserAction CanBeShownScript --exact
py -3 scripts\query-reforger-data.py method ScriptedUserAction CanBePerformedScript --exact
py -3 scripts\query-reforger-data.py examples user-action --limit 10
```

Workbench anchors:

```powershell
py -3 scripts\query-reforger-data.py symbol WorkbenchPlugin --kind class --exact
py -3 scripts\query-reforger-data.py files WorkbenchPlugin --limit 20
py -3 scripts\query-reforger-data.py examples workbench-plugin --limit 10
py -3 scripts\query-reforger-data.py lookup "workbench plugin"
```

File and snippet routes:

```powershell
py -3 scripts\query-reforger-data.py files <query> --limit 20
py -3 scripts\query-reforger-data.py examples <topic> --limit 10
py -3 scripts\query-reforger-data.py snippet <scripts/...file.c> --line <line> --context 30
```

JSON output:

```powershell
py -3 scripts\query-reforger-data.py symbol ResourceName --exact --json
py -3 scripts\query-reforger-data.py method IEntity FindComponent --exact --json
py -3 scripts\query-reforger-data.py lookup "load resource" --json
```

## Examples And Samples

This utility reference does not own official sample layout. It routes example lookup to query output and the future `examples-and-sample-patterns.md` reference.

Useful example commands:

```powershell
py -3 scripts\query-reforger-data.py examples component --subtopic script-component --limit 10
py -3 scripts\query-reforger-data.py examples user-action --limit 10
py -3 scripts\query-reforger-data.py examples replication --limit 10
py -3 scripts\query-reforger-data.py examples resource-loading --limit 10
py -3 scripts\query-reforger-data.py examples workbench-plugin --limit 10
```

Representative evidence from query output:

- Workbench plugin examples returned handwritten files such as Workbench and WorkbenchCommon plugin/tool scripts.
- User-action lookup returned `ScriptedUserAction` methods plus suggested snippets for concrete user-action files.
- Replicated-component lookup returned `RplProp`, `RplRpc`, `RplComponent`, `BaseRplComponent`, and replication examples.
- Resource/prefab lookup returned `ResourceName`, `Resource.Load`, `EntitySpawnParams`, `SpawnEntityPrefab`, and resource-loading examples.

Do not paste sample or game-source bodies into the reference. Use `snippet` when a bounded source view is needed for a concrete task.

## Follow-Up Keywords

Use these as query terms when the owning reference gives no narrower key:

- `IEntity`
- `GenericEntity`
- `GenericComponent`
- `ScriptComponent`
- `ScriptComponentClass`
- `FindComponent`
- `ResourceName`
- `Resource`
- `Resource.Load`
- `PrefabResource`
- `EntitySpawnParams`
- `SpawnEntityPrefab`
- `BaseContainer`
- `Attribute`
- `UIWidgets`
- `RplProp`
- `RplRpc`
- `RplComponent`
- `BaseRplComponent`
- `ScriptedUserAction`
- `PerformAction`
- `CanBeShownScript`
- `CanBePerformedScript`
- `WorkbenchPlugin`
- `WorkbenchPluginAttribute`
- `WorldEditorPlugin`
- `ScriptInvoker`
- `Print`
- `DbgUI`

## Verification

Before finalizing API-sensitive work:

- Confirm the relevant source-owning reference was read.
- Confirm exact symbols/methods/attributes were queried with `--exact` when names were known.
- Confirm generated records were used for signatures.
- Confirm handwritten examples were used only for implementation shape.
- Confirm snippets were bounded and came from query-returned files/lines.
- Confirm no broad schema/API dump was loaded as normal workflow.
- Confirm unresolved API uncertainty is stated rather than guessed.
- Confirm Workbench/runtime verification remains for resources, prefabs, plugin visibility, entity wiring, multiplayer/authority, and dedicated-server behavior.

Residual uncertainty to state in final answers:

- API lookup confirms current extracted source signatures, not successful Workbench compilation in the user's project.
- Query output does not prove resource path validity, prefab dependencies, or editor registration.
- Query output does not prove replication, authority, client/server, or JIP behavior.
- Runtime, Workbench, dedicated-server, packaging, and editor validation should be named when they remain.

## Official Wiki Links

No primary wiki page is owned by this utility reference. Use these human provenance links only for the workflow context they own:

- Scripting Modding: https://community.bistudio.com/wiki/Arma_Reforger:Scripting_Modding
- Scripting Example: https://community.bistudio.com/wiki/Arma_Reforger:Scripting_Example
- Enforce Script Syntax: https://community.bistudio.com/wiki/Arma_Reforger:Enforce_Script_Syntax
- Resource Manager: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager
- Workbench Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Workbench_Plugin
- Multiplayer Scripting: https://community.bistudio.com/wiki/Arma_Reforger:Multiplayer_Scripting

## Usefulness Score

Score: 90/100

- Wiki coverage: 26/30. This utility reference owns no primary wiki pages by design. The no-primary-owner case is explicit, relevant workflow owners are routed, official links are included for provenance, and no wiki workflow content is duplicated.
- Operational detail: 13/15. The reference gives concrete query-selection rules, command forms, filters, task bundles, snippet workflow, and verification boundaries.
- API lookup usefulness: 15/15. Exact commands cover symbol, method, attribute, inheritance, examples, files, snippets, JSON output, and common high-value anchors.
- Example grounding: 8/10. Query-surfaced example families are included without copying source bodies. Official sample layout is intentionally routed to the future examples reference.
- Codex task usefulness: 14/15. Codex can move from a task to exact API lookup and bounded snippets without broad dumps or guessing.
- Context efficiency: 10/10. The reference is compact, query-focused, and avoids workflow/source/API duplication.
- Verification guidance: 4/5. It clearly states what lookup proves and what still requires Workbench/runtime/server/editor validation.

Category-fit check:

- Source family complete: pass. This file owns query behavior, not wiki workflow source families.
- No owned page missing: pass. There are no owned primary wiki pages; this is stated in Source Inventory and Official Wiki Links.
- Split boundary justified: pass. Workflow authority is routed to source-owning references; this file owns only lookup behavior and common anchors.
- Cross-links present: pass. Adjacent workflow references are named in When To Read and Workbench / Resource / Data Surfaces.
- Task route clear: pass. Common tasks route to one workflow reference plus exact query commands or `lookup` bundles.

Missed coverage/cap review:

- No owned primary wiki page was skipped.
- No workflow category is silently owned by this utility reference.
- No full wiki page, source body, broad API dump, machine-specific filesystem path, or live wiki-fetch instruction is included.
- API-sensitive guidance is paired with query commands.
- No automatic failure condition applies.
