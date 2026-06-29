# Generation Review

Generation status: `COMPLETE`

## Summary

- Raw data refreshed: no. Existing raw cache was present and `generation/design.md` only requires refresh when missing or explicitly requested.
- Runtime references rebuilt: yes. `references/` was restored, updated, and re-audited for the current design.
- `SKILL.md` rebuilt: yes. It now routes to `references/common-task-recipes.md`.
- `references/common-task-recipes.md` added and validated.
- Runtime raw-path rule enforced: `SKILL.md` and `references/*.md` contain no `raw/` or `raw\` paths and no `Sources Used` sections.
- Padding/filler rule enforced: runtime references contain no `Operational Detail Retention`, `Expanded Source-Grounded Review Notes`, or retention-note filler markers.
- Audit tooling updated: `scripts/audit-references.py` now matches the current design's runtime raw-path prohibition.
- API extended generator updated so future `api-extended.md` rebuilds do not reintroduce a runtime raw path in the header.

## Source Inventory

- Wiki markdown files present: 316.
- Official sample mods present: `SampleMod_AnimationWorkshop`, `SampleMod_CinematicTutorial`, `SampleMod_Main`, `SampleMod_ModdedCar`, `SampleMod_ModdedScript`, `SampleMod_ModdedWeapon`, `SampleMod_NewCar`, `SampleMod_NewCharacter`, `SampleMod_NewFaction`, `SampleMod_NewProp`, `SampleMod_NewWeapon`, `SampleMod_Replacement`, `SampleMod_WorkbenchPlugin`.
- Game version: `1.7.0.54`.
- Build id: `23758462`.
- API extraction: 719 script files, 875 classes, 175 enums, 49 global functions.
- Official samples repo commit: not recorded in available local sample metadata.

## References Written

- `references/overview.md`
- `references/scripting-core.md`
- `references/scripting-language.md`
- `references/entity-component-lifecycle.md`
- `references/networking-multiplayer-replication.md`
- `references/resources-prefabs-configs.md`
- `references/workbench-tools-debugging.md`
- `references/scenario-framework-game-master.md`
- `references/terrain-world-editor.md`
- `references/assets-weapons-vehicles-animation-audio.md`
- `references/server-runtime-packaging.md`
- `references/examples-patterns.md`
- `references/common-task-recipes.md`
- `references/api-main.md`
- `references/api-extended.md`

## Completeness Audit

| Reference | Nonblank lines | Line target met | Runtime raw references absent | Review provenance listed | Source coverage mapped | Actionable details retained | Runtime usability met | Examples present | Traps/checklist present | API notes present | No padding/filler present | Required coverage met | Status | If failed, required expansion |
| --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `references/overview.md` | 132 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | PASS | none |
| `references/scripting-core.md` | 252 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | PASS | none |
| `references/scripting-language.md` | 251 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | PASS | none |
| `references/entity-component-lifecycle.md` | 256 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | PASS | none |
| `references/networking-multiplayer-replication.md` | 257 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | PASS | none |
| `references/resources-prefabs-configs.md` | 254 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | PASS | none |
| `references/workbench-tools-debugging.md` | 251 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | PASS | none |
| `references/scenario-framework-game-master.md` | 306 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | PASS | none |
| `references/terrain-world-editor.md` | 251 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | PASS | none |
| `references/assets-weapons-vehicles-animation-audio.md` | 257 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | PASS | none |
| `references/server-runtime-packaging.md` | 254 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | PASS | none |
| `references/examples-patterns.md` | 400 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | PASS | none |
| `references/common-task-recipes.md` | 464 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | PASS | none |
| `references/api-main.md` | 1072 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | PASS | none |
| `references/api-extended.md` | 10494 | exempt | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | PASS | none |

## Source Coverage Map

| Source or source group | Assigned reference | Actionable content retained | Examples retained | Deferred lookup | Omitted content | Omission reason |
| --- | --- | --- | --- | --- | --- | --- |
| `raw/wiki-docs/markdown/Arma_Reforger_Scripting__Conventions.md`, `Arma_Reforger_Scripting_First_Steps.md`, `Arma_Reforger_Scripting_Modding.md`, `Arma_Reforger_ScriptInvoker_Usage.md`, `Arma_Reforger_Scripting__Performance.md` | `scripting-core.md`, `scripting-language.md` | module placement, tag/class naming, modded-class flow, debug/profiling cautions, invoker guidance | scripting examples and modded scoring pattern | uncommon APIs to `api-extended.md` | screenshots/navigation/repeated tutorial prose | non-actionable |
| `raw/wiki-docs/markdown/Arma_Reforger_Create_a_Component.md`, `Arma_Reforger_Entity_Lifecycle.md`, `Arma_Reforger_Entity_Activeness.md`, `Arma_Reforger_Event_Handlers.md` | `entity-component-lifecycle.md`, `common-task-recipes.md` | component class pair, `ComponentEditorProps`, lifecycle/event masks, owner guards, activeness traps | component skeletons and event examples | lifecycle signatures to `api-main.md`/`api-extended.md` | long repeated tutorial text | compressed into workflows |
| `raw/wiki-docs/markdown/Arma_Reforger_Multiplayer_Scripting.md` | `networking-multiplayer-replication.md`, `common-task-recipes.md` | authority/proxy/owner rules, RPC warning for init paths, `RplRpc`, `RplProp`, update/bump cautions | RPC/RplProp skeletons | enum and overload lookup to API references | deep prose and exhaustive examples | summarized for runtime use |
| `raw/wiki-docs/markdown/Arma_Reforger_BaseContainer_Usage.md`, `Arma_Reforger_Create_a_Config_Class.md`, `Arma_Reforger_Entity_Catalog.md`, `Arma_Reforger_Layout_Creation.md` | `resources-prefabs-configs.md`, `common-task-recipes.md` | `ResourceName`, config objects, resource picker fields, entity catalogs, UI layout cautions | resource/config field examples | resource and container signatures to API references | bulk serialized config data | project-specific |
| `raw/wiki-docs/markdown/Arma_Reforger_Workbench_Plugin_Tutorial.md`, `Arma_Reforger_Resource_Manager_Plugin.md`, Workbench sample plugin scripts | `workbench-tools-debugging.md`, `common-task-recipes.md` | Workbench module context, plugin attributes, Resource Manager/Script Editor/World Editor separation | plugin skeletons | Workbench module signatures to API references | screenshots/UI navigation | non-actionable |
| Scenario, Game Master, faction, terrain, world editor, assets, vehicles, weapons, animation, audio, server, and Workshop wiki documents | matching topical references | task routing, data-first workflows, required config/resource surfaces, packaging cautions | source-family examples and sample layout notes | exact uncommon APIs to `api-extended.md` | large asset/config dumps | too project-specific for runtime references |
| `raw/samples/SampleMod_*` README/script/config/prefab/world files | `examples-patterns.md` and topical references | sample inventory, layout patterns, user actions, modded scripts, Workbench plugins, vehicle/weapon/faction/resource examples | all official sample mod families named | exact APIs to `api-main.md`/`api-extended.md` | full serialized files | too large/project-specific |
| `raw/game-data/api-schema.json`, `raw/game-data/api-index.md`, `raw/game-data/manifest.json` | `api-main.md`, `api-extended.md` | common signatures, game/build metadata, exhaustive fallback surface | common signature examples | exhaustive uncommon API lookup in `api-extended.md` | none for fallback | not omitted |

Top retained operational rules: verify uncertain APIs before coding, keep runtime references independent of local raw caches, separate script-first/data-first work, respect lifecycle and network authority boundaries, and use samples as examples rather than source-of-truth overrides.

Top intentionally omitted details: screenshots, wiki navigation, repeated tutorial prose, bulk serialized prefab/config bodies, and exhaustive uncommon APIs already covered by `api-extended.md`.

Top details deferred to API lookup: uncommon Workbench methods, full replication codec APIs, resource/container overloads, editor module methods, vehicle/weapon/animation/audio system-specific calls.

## Exact Raw Source Provenance

- `raw/wiki-docs/markdown/Arma_Reforger_Create_a_Component.md`
- `raw/wiki-docs/markdown/Arma_Reforger_Entity_Lifecycle.md`
- `raw/wiki-docs/markdown/Arma_Reforger_Entity_Activeness.md`
- `raw/wiki-docs/markdown/Arma_Reforger_Event_Handlers.md`
- `raw/wiki-docs/markdown/Arma_Reforger_Multiplayer_Scripting.md`
- `raw/wiki-docs/markdown/Arma_Reforger_Action_Context_Setup.md`
- `raw/wiki-docs/markdown/Arma_Reforger_BaseContainer_Usage.md`
- `raw/wiki-docs/markdown/Arma_Reforger_Create_a_Config_Class.md`
- `raw/wiki-docs/markdown/Arma_Reforger_Entity_Catalog.md`
- `raw/wiki-docs/markdown/Arma_Reforger_Layout_Creation.md`
- `raw/wiki-docs/markdown/Arma_Reforger_Resource_Manager_Plugin.md`
- `raw/wiki-docs/markdown/Arma_Reforger_Scripting__Conventions.md`
- `raw/wiki-docs/markdown/Arma_Reforger_Scripting_First_Steps.md`
- `raw/wiki-docs/markdown/Arma_Reforger_Scripting_Modding.md`
- `raw/wiki-docs/markdown/Arma_Reforger_ScriptInvoker_Usage.md`
- `raw/wiki-docs/markdown/Arma_Reforger_Scripting__Performance.md`
- `raw/samples/SampleMod_ModdedScript/Scripts/Game/GameMode/Scoring/Modded/SCR_BaseScoringSystemComponent.c`
- `raw/samples/SampleMod_ModdedScript/Scripts/Game/GameMode/Scoring/Modded/SCR_ScoringSystemComponent.c`
- `raw/samples/SampleMod_NewCar/Scripts/Game/UserActions/SCR_CarTrunkUserAction.c`
- `raw/samples/SampleMod_NewWeapon/Scripts/Game/UserActions/SCR_FlipSignalUserAction.c`
- `raw/samples/SampleMod_WorkbenchPlugin/Scripts/WorkbenchGame/SamplePlugins/SampleResourceManagerPlugin.c`
- `raw/samples/SampleMod_WorkbenchPlugin/Scripts/WorkbenchGame/SamplePlugins/SampleScriptEditorPlugin.c`
- `raw/samples/SampleMod_WorkbenchPlugin/Scripts/WorkbenchGame/SamplePlugins/SampleWorldEditorPlugin.c`
- `raw/game-data/manifest.json`
- `raw/game-data/api-schema.json`
- `raw/game-data/api-index.md`

## API Curation

`api-main.md` was rebuilt as the normal coding lookup surface. It includes mandatory common signatures for `IEntity` transforms/origin/orientation, `ScriptComponent`, `ScriptComponentClass`, Workbench `ScriptEditor`, Workbench `ResourceManager`, `ResourceName`, `RplRpc`, and `RplProp`. `api-extended.md` remains the exhaustive fallback.

Known API cautions:

- Player/controller access remains project-context-sensitive; search project code before using local-player helpers.
- Spawn helpers remain context-sensitive and should be verified per task.
- RPC invocation shape and attribute enum choices must be verified against current code before implementation.
- Workbench APIs are editor-only unless a reference explicitly says otherwise.

## Forward Tests

Throwaway fixture directory: created under the OS temp directory, then removed after grep verification.

| Prompt | References opened/used | Result |
| --- | --- | --- |
| Minimal `ScriptComponent` plus `ScriptComponentClass`, editable resource field, guarded `EOnInit` print | `common-task-recipes.md`, `entity-component-lifecycle.md`, `api-main.md` | PASS |
| Move owner entity to supplied vector with verified transform/origin APIs | `common-task-recipes.md`, `api-main.md` | PASS |
| User-action script patterned after official samples with uncertainty marked | `common-task-recipes.md`, `examples-patterns.md`, `scripting-core.md` | PASS |
| Replicated/RPC component skeleton separating authority and uncertain RPC details | `networking-multiplayer-replication.md`, `common-task-recipes.md`, `api-main.md` | PASS |
| Workbench plugin command skeleton with documented attribute shape | `workbench-tools-debugging.md`, `common-task-recipes.md`, `api-main.md` | PASS |
| Config/prefab `ResourceName` field example and script-first/data-first note | `resources-prefabs-configs.md`, `common-task-recipes.md`, `api-main.md` | PASS |

Fixture grep confirmed: `ScriptComponentClass`, `EOnInit`, `SetOrigin`, `ScriptedUserAction`, `RplProp`, `WorkbenchPluginAttribute`, and `ResourceName`.

## Validation Results

- `py -3 scripts\audit-references.py`: PASS.
- `py -3 C:\Users\Gray\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\Gray\.codex\skills\reforger`: PASS (`Skill is valid!`).
- Forbidden runtime markers scan for `raw/`, `raw\`, `Sources Used`, and known filler headings: PASS.
- `SKILL.md` links only existing references.
- `agents/openai.yaml` exists and still matches the skill purpose.

## Runtime Usability Review

- `SKILL.md` is compact and routes quickly by task.
- Topical references include search terms near the top.
- `common-task-recipes.md` covers the required recipes with examples, traps, API notes, and follow-up lookup.
- `api-main.md` contains common exact signatures before the exhaustive fallback.
- Runtime references do not require the `raw/` cache.

## Manual Review Items

- This rebuild restores and validates the runtime skill surface. It does not prove generated Enfusion Script compiles in Workbench; task-specific edits still require project/API verification.
- Exact raw provenance is summarized by the material source files and source groups above; the raw cache remains a generation input, not a runtime dependency.
