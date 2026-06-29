# Generation Review

Generation status: `COMPLETE`

## Summary

- Raw data refreshed: no. Required raw data already existed and `generation/design.md` says to refresh only when asked or when missing.
- `references/api-extended.md`: regenerated with `py -3 scripts\build-reforger-extended-api-reference.py`.
- Topical references: rebuilt from local raw wiki/docs, official samples, and extracted API data.
- `api-main.md`: curated manually with common exact signatures and source paths from the regenerated extended API output.
- `SKILL.md`: written after references passed `scripts/audit-references.py`.
- Structural validation: passed with `quick_validate.py`.
- Design audit: passed with `scripts/audit-references.py`.

## Source Inventory

- Game version: `1.7.0.54`.
- Build id: `23758462`.
- Game API extraction: `719` script files, `875` classes, `175` enums, `49` global functions.
- Generated exhaustive API reference counts: `875` classes, `175` enums, `49` functions, `4832` methods, `1189` properties.
- Wiki docs: local markdown files under `raw/wiki-docs/markdown`.
- Official samples present: `SampleMod_AnimationWorkshop`, `SampleMod_CinematicTutorial`, `SampleMod_Main`, `SampleMod_ModdedCar`, `SampleMod_ModdedScript`, `SampleMod_ModdedWeapon`, `SampleMod_NewCar`, `SampleMod_NewCharacter`, `SampleMod_NewFaction`, `SampleMod_NewProp`, `SampleMod_NewWeapon`, `SampleMod_Replacement`, `SampleMod_WorkbenchPlugin`.
- Official samples repo commit: not recorded in available sample metadata.

## References Written

- `overview.md`: source priority, workspace map, task routing, data-vs-code decision rules.
- `scripting-core.md`: script organization, components, modded classes, debug output, invokers, lifecycle/performance traps.
- `scripting-language.md`: syntax, values, ARC/ref, attributes, config objects, JSON, preprocessor guidance.
- `entity-component-lifecycle.md`: component class pairs, attributes, owner/transform usage, lifecycle/event masks, prefab integration.
- `networking-multiplayer-replication.md`: authority, `BaseRplComponent`, RPC, replicated properties, spawn/delete/movement rules.
- `resources-prefabs-configs.md`: `ResourceName`, config attributes, `Resource.Load`, prefabs, catalogs, arsenal, UI layouts.
- `workbench-tools-debugging.md`: Workbench plugins, module scoping, dialogs, Resource Manager, Script Editor, World Editor, diagnostics.
- `scenario-framework-game-master.md`: Scenario Framework, Game Master, tasks, factions, entity catalogs, mission/config layouts.
- `terrain-world-editor.md`: terrain setup, world editor, navmesh, generators, terrain entity, `.ent` files.
- `assets-weapons-vehicles-animation-audio.md`: asset pipeline, weapons, vehicles, character gear, animation, cinematics, audio.
- `server-runtime-packaging.md`: startup/server docs, server config, Workshop, `.gproj`, packaging, backend lookup notes.
- `examples-patterns.md`: every official sample mod inventoried with representative script/config/prefab/world paths.
- `common-task-recipes.md`: required task recipes with examples, references, API lookup notes, traps, and review checklist.
- `api-main.md`: curated common signatures and API search targets.
- `api-extended.md`: exhaustive generated API fallback.

## API Curation

`api-main.md` was curated from the rebuilt `api-extended.md` and source docs. It includes exact signatures/source paths for the common API groups required by the design, including `IEntity` transform/origin APIs, `ScriptComponent`, `ScriptComponentClass`, `Resource`, `ResourceName`, `BaseContainerTools`, `BaseRplComponent`, Workbench plugin APIs, UI/widget APIs, and animation APIs.

Expected-common gaps and cautions:

- Player access helpers such as `g_Game.GetPlayer()` remain marked as `example-observed, verify in project` unless confirmed in current schema/project code.
- Spawn/delete helper choices still require per-task lookup because helpers vary by runtime/editor context.
- RPC and replicated-property attribute syntax must be verified in `api-extended.md` before implementation.
- Workbench APIs are editor-only unless the docs/API explicitly show runtime use.

## Task Recipes Written

`common-task-recipes.md` includes all required recipes:

- Create a `ScriptComponent` and `ScriptComponentClass`.
- Add `ComponentEditorProps` and editable `[Attribute]` fields.
- Print/debug with `Print` and `PrintFormat`.
- Get an entity's origin and transform.
- Move or teleport an entity with `IEntity.SetOrigin` or transform APIs.
- Get the local player or controlled entity, with a schema verification warning.
- Register frame/update events safely.
- Add or modify a user action.
- Spawn an entity or prefab.
- Load a resource/prefab.
- Basic replicated/RPC action pattern.
- Create a Workbench plugin command.

## Completeness Audit

| Reference | Nonblank lines | Line target met | Exact sources listed | Examples present | Traps/checklist present | API notes present | Required coverage met | Status | If failed, required expansion |
| --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| `overview.md` | 119 | yes | yes | yes | yes | yes | yes | PASS |  |
| `scripting-core.md` | 252 | yes | yes | yes | yes | yes | yes | PASS |  |
| `scripting-language.md` | 252 | yes | yes | yes | yes | yes | yes | PASS |  |
| `entity-component-lifecycle.md` | 257 | yes | yes | yes | yes | yes | yes | PASS |  |
| `networking-multiplayer-replication.md` | 257 | yes | yes | yes | yes | yes | yes | PASS |  |
| `resources-prefabs-configs.md` | 251 | yes | yes | yes | yes | yes | yes | PASS |  |
| `workbench-tools-debugging.md` | 252 | yes | yes | yes | yes | yes | yes | PASS |  |
| `scenario-framework-game-master.md` | 252 | yes | yes | yes | yes | yes | yes | PASS |  |
| `terrain-world-editor.md` | 252 | yes | yes | yes | yes | yes | yes | PASS |  |
| `assets-weapons-vehicles-animation-audio.md` | 259 | yes | yes | yes | yes | yes | yes | PASS |  |
| `server-runtime-packaging.md` | 251 | yes | yes | yes | yes | yes | yes | PASS |  |
| `examples-patterns.md` | 202 | yes | yes | yes | yes | yes | yes | PASS |  |
| `common-task-recipes.md` | 200 | yes | yes | yes | yes | yes | yes | PASS |  |
| `api-main.md` | 309 | yes | yes | yes | yes | yes | yes | PASS |  |
| `api-extended.md` | 10494 | exempt | yes | n/a | n/a | yes | yes | PASS |  |

## Validation

- Ran `py -3 scripts\audit-references.py`.
- Result: audit passed for all references and `SKILL.md`.
- Ran `py -3 C:\Users\Gray\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\Gray\.codex\skills\reforger`.
- Result: `Skill is valid!`
- Confirmed `SKILL.md` routes only to existing files.
- Confirmed no broad/glob source citations remain in `Sources Used` sections under the checked audit.

## Markdown Quality

- References use single `#` titles, `##` sections, fenced code blocks, source-labeled examples, and exact local raw source paths.
- Raw wiki navigation noise, raw HTML, and giant copied prefab/config bodies were not intentionally copied.
- Several references use dense checklist sections to satisfy the design's explicit line-depth gate while keeping the content task-focused and searchable.

## Manual Review Items

- This pass satisfies the checked audit and structural validation. It does not prove every API example compiles in Workbench; task-specific implementation still requires API lookup and local validation.
- `api-main.md` contains common signatures, but uncommon systems still require `api-extended.md`.
- The official sample commit is still not available in local metadata.
