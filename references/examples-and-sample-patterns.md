# Examples And Sample Patterns

## When To Read

Read this when Codex needs a fast route from a Reforger task to official sample layouts, raw game-source examples surfaced by the query tool, and bounded snippet commands.

This is a utility reference. It does not own workflow truth for any modding topic. Always read the source-owning topical reference for the task first, then use this file to choose examples and query routes. Exact APIs still come from `scripts\query-reforger-data.py`, not from memory or from copied sample code.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: none. Tutorial and workflow wiki pages remain owned by their topical references.
- Secondary/cross-reference topics: official wiki pages are represented through topical reference routes only.

Wiki pages reviewed:
- No primary wiki pages are owned by this reference. This is intentional because this file routes examples and samples instead of preserving workflow source detail.

Wiki sections covered:
- Not applicable. Use the source-owning topical reference for full wiki section coverage.

Structured wiki records:
- Tables reviewed/included: not applicable for this utility reference.
- Procedures reviewed/included: not applicable; procedures remain in topic references.
- Admonitions reviewed/included: not applicable; warnings are summarized here only as example-use safety rules.
- Code blocks reviewed/included: none copied.
- Media reviewed: not applicable.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts\query-reforger-data.py examples component --limit 8`
  - `py -3 scripts\query-reforger-data.py examples replication --limit 8`
  - `py -3 scripts\query-reforger-data.py examples resource-loading --limit 8`
  - `py -3 scripts\query-reforger-data.py examples workbench-plugin --limit 8`
  - `py -3 scripts\query-reforger-data.py examples scenario-framework --limit 8`
  - `py -3 scripts\query-reforger-data.py examples game-mode --limit 8`
  - `py -3 scripts\query-reforger-data.py examples weapon --limit 8`
  - `py -3 scripts\query-reforger-data.py examples inventory --limit 8`
  - `py -3 scripts\query-reforger-data.py examples vehicle --limit 8`
  - `py -3 scripts\query-reforger-data.py examples animation --limit 8`
  - `py -3 scripts\query-reforger-data.py examples audio --limit 8`
  - `py -3 scripts\query-reforger-data.py examples ui --limit 8`
  - `py -3 scripts\query-reforger-data.py examples ai --limit 8`
  - targeted subtopic checks for `magazine`, `character-inventory`, `compartment`, `anim-graph`, and `hud`.
- Symbols/methods/attributes verified: none directly. This reference routes examples; exact symbols must be verified with the API/search reference and query commands.
- Examples/snippets reviewed: component lifecycle/script-component examples, replication docs/examples, resource loading/spawn examples, Workbench plugin examples, scenario/game-mode example routes, weapon and magazine examples, inventory examples, vehicle compartment examples, animation graph examples, audio sound-event examples, UI/HUD examples, and AI scripted-node examples.

Samples and source examples:
- Official sample folders reviewed: `SampleMod_Main`, `SampleMod_ModdedScript`, `SampleMod_WorkbenchPlugin`, `SampleMod_NewWeapon`, `SampleMod_ModdedWeapon`, `SampleMod_NewCar`, `SampleMod_ModdedCar`, `SampleMod_NewCharacter`, `SampleMod_NewFaction`, `SampleMod_NewProp`, `SampleMod_AnimationWorkshop`, `SampleMod_CinematicTutorial`, `SampleMod_Replacement`.
- Raw game-source example families reviewed: component, replication, resource loading, Workbench plugin, scenario framework, game mode, weapon, inventory, vehicle, animation, audio, UI, and AI.

Coverage gaps:
- Missing, excluded, or intentionally deferred source: full sample file bodies, wiki workflow steps, API signatures, and domain-specific setup details are intentionally deferred.
- Reason and impact: this file is a router. Copying bodies or workflow detail here would duplicate topical references and increase context bloat.

## Wiki Source Coverage

This reference intentionally has no primary wiki ownership. Wiki-heavy workflow detail belongs in the topical references:

- Project/sample layout and publishing context: `references/mod-projects-addons-workshop.md`
- Language and script editor basics: `references/enfusion-language-and-script-editor.md`
- Script patterns and user actions: `references/script-events-actions-and-patterns.md`
- API lookup behavior: `references/api-lookup-and-common-symbols.md`
- Resource Manager/editor surfaces: `references/resource-manager-file-types-and-editors.md`
- Prefabs/configs/catalogs/resources: `references/prefabs-configs-containers-and-catalogs.md`
- Entity/component lifecycle: `references/entities-components-and-lifecycle.md`
- Replication: `references/multiplayer-replication-and-authority.md`
- Server/runtime: `references/server-hosting-startup-and-runtime.md`
- Workbench plugins: `references/workbench-plugins-and-editor-tools.md`
- Diagnostics/testing: `references/diagnostics-testing-and-performance.md`
- Scenario Framework: `references/scenario-framework.md`
- Game Master/factions/tasks/modes: `references/game-master-factions-tasks-and-modes.md`
- Terrain/world setup: `references/terrain-creation-and-world-setup.md`
- World Editor tools/navmesh: `references/world-editor-tools-generators-and-navmesh.md`
- Assets/props/materials: `references/asset-import-models-materials-and-props.md`
- Weapons: `references/weapons-prefabs-attachments-and-firearms.md`
- Gear/inventory: `references/character-gear-inventory-and-arsenal.md`
- Vehicles: `references/vehicles-creation-simulation-and-compartments.md`
- Animation: `references/animation-graphs-weapon-animation-and-export.md`
- Audio: `references/audio-editor-signals-and-sound-systems.md`
- UI: `references/ui-layouts-dialogs-and-menus.md`
- AI: `references/ai-behavior-commanding-and-debug.md`

## Terms And Concepts

- Official samples: Bohemia-provided mod projects that show addon layout, resource organization, and complete example project structure.
- Game-source examples: current game scripts surfaced by `scripts\query-reforger-data.py examples`, `files`, and `snippet` commands.
- Generated API files: exact signature truth when query output marks a record as generated.
- Handwritten files: better implementation-pattern examples when query output marks a record as not generated.
- Example route: a command and follow-up snippet path that gets Codex close to relevant source without loading broad dumps.
- Sample signal: a sample root that suggests layout, resource families, or project structure but does not override wiki or current API lookup.
- Subtopic: query filter that narrows broad example families, such as `script-component`, `rpl-prop`, `spawn-prefab`, `magazine`, `compartment`, or `hud`.

## Workbench / Resource / Data Surfaces

Use official samples to inspect project shape and data placement, not to infer API signatures. Common sample signals:

- `SampleMod_Main`: broad resource, terrain/world, UI, config, entity catalog, arsenal, mission thumbnail, and baseline project structure signals.
- `SampleMod_ModdedScript`: script override/modded-script layout signal.
- `SampleMod_WorkbenchPlugin`: Workbench plugin project and editor-extension layout signal.
- `SampleMod_NewWeapon`: new weapon asset/resource/prefab/config layout signal.
- `SampleMod_ModdedWeapon`: weapon modification/replacement layout signal.
- `SampleMod_NewCar`: new vehicle asset/prefab/simulation layout signal.
- `SampleMod_ModdedCar`: vehicle modification layout signal.
- `SampleMod_NewCharacter`: character gear/loadout/inventory layout signal.
- `SampleMod_NewFaction`: faction, campaign, group, and game-mode integration layout signal.
- `SampleMod_NewProp`: prop/model/material/prefab layout signal.
- `SampleMod_AnimationWorkshop`: animation graph/export/workshop sample signal.
- `SampleMod_CinematicTutorial`: cinematic/animation/tutorial sample signal.
- `SampleMod_Replacement`: replacement mod structure signal.

Use game-source examples to inspect current implementation patterns:

- Query generated files when the question is "what is the exact class, method, enum, or attribute?"
- Query handwritten files when the question is "how does existing game code use this?"
- Use bounded snippets after selecting a file and line from query output.

## Required Workflows

Find an example for a task:
1. Read the source-owning topical reference for the task.
2. Run the topical `examples` command listed in this reference.
3. If results are broad or noisy, add `--subtopic`, use a targeted `files` command, or search exact symbols from the topical reference.
4. Pick one or two best candidate files from query output.
5. Open only bounded snippets around the returned lines.
6. Verify every API-sensitive class, method, attribute, enum, and callback through exact symbol/method/attribute query commands.
7. Use samples only for layout/resource organization and final project-shape comparison.

Use an official sample:
1. Identify the nearest sample root from the sample map below.
2. Compare folder/resource organization and naming patterns.
3. Do not copy source bodies or assume API signatures are current.
4. Cross-check the source-owning topical reference for workflow rules.
5. Query exact APIs and game-source examples before writing code.

Use a game-source example:
1. Prefer `examples <topic> --subtopic <subtopic>` for implementation patterns.
2. Prefer `files <exact-ish name>` for noisy domains like AI, Scenario Framework, GameMode, weapon, and UI.
3. Use generated records for signatures and handwritten records for patterns.
4. Use `snippet <file> --line <n> --context <n>` only after the file is selected.
5. Keep snippets bounded and do not load a full source file unless the task truly requires it.

## Configuration Fields And Tables

Sample-to-task routing table:

| Task family | Read first | Official sample signal | Query route |
| --- | --- | --- | --- |
| Script component or script pattern | `script-events-actions-and-patterns.md`; `entities-components-and-lifecycle.md` | `SampleMod_ModdedScript` | `examples component --subtopic script-component` |
| Component lifecycle | `entities-components-and-lifecycle.md` | `SampleMod_Main` | `examples component --subtopic lifecycle` |
| Replication/RPC/RplProp | `multiplayer-replication-and-authority.md` | Use game-source examples first | `examples replication --subtopic rpl-prop`; `examples replication --subtopic rpc` |
| Resource loading or prefab spawn | `prefabs-configs-containers-and-catalogs.md` | `SampleMod_Main`; domain sample roots | `examples resource-loading --subtopic resource-load`; `examples resource-loading --subtopic spawn-prefab` |
| Workbench plugin | `workbench-plugins-and-editor-tools.md` | `SampleMod_WorkbenchPlugin` | `examples workbench-plugin --limit 8` |
| Scenario Framework | `scenario-framework.md` | `SampleMod_Main` | prefer `files ScenarioFramework`; broad `examples scenario-framework` can be noisy |
| Game mode/faction/task | `game-master-factions-tasks-and-modes.md` | `SampleMod_NewFaction`; `SampleMod_Main` | prefer `files SCR_TaskSystem`, `files SCR_Faction`, `files GameMode` |
| Terrain/world/navmesh | terrain and world-editor references | `SampleMod_Main` | prefer `files Terrain`, `files WorldEditor`, `files Navmesh` |
| Asset/prop import | `asset-import-models-materials-and-props.md` | `SampleMod_NewProp`; `SampleMod_Main` | `files Asset`; `files ResourceImport`; `examples resource-loading` |
| Weapon or magazine behavior | `weapons-prefabs-attachments-and-firearms.md` | `SampleMod_NewWeapon`; `SampleMod_ModdedWeapon` | `examples weapon`; `examples weapon --subtopic magazine` |
| Gear/inventory/arsenal | `character-gear-inventory-and-arsenal.md` | `SampleMod_NewCharacter`; `SampleMod_Main` | `examples inventory --subtopic character-inventory` |
| Vehicle compartment or controller | `vehicles-creation-simulation-and-compartments.md` | `SampleMod_NewCar`; `SampleMod_ModdedCar` | `examples vehicle --subtopic compartment`; `examples vehicle --subtopic vehicle-component` |
| Animation graph/command | `animation-graphs-weapon-animation-and-export.md` | `SampleMod_AnimationWorkshop`; `SampleMod_CinematicTutorial` | `examples animation --subtopic anim-graph` |
| Audio/sound event | `audio-editor-signals-and-sound-systems.md` | weapon/vehicle/main sample audio resources where present | `examples audio --subtopic sound-event`; `files SoundEvent` |
| UI/HUD/layout | `ui-layouts-dialogs-and-menus.md` | `SampleMod_Main` | `examples ui --subtopic hud`; `examples ui --subtopic layout` |
| AI behavior/debug | `ai-behavior-commanding-and-debug.md` | `SampleMod_Main`; `SampleMod_NewFaction` | prefer `files AI`, `files Behavior`, `files AITask`; broad `examples ai` can be noisy |
| Server/game-mode context | `server-hosting-startup-and-runtime.md`; game-mode reference | `SampleMod_Main`; `SampleMod_NewFaction` | `examples game-mode`; `files GameMode` |

Subtopic routing table:

| Subtopic | Use for |
| --- | --- |
| `script-component` | script component class examples |
| `lifecycle` | init/post-init/event-mask patterns |
| `rpl-prop` | replicated property examples |
| `rpc` | RPC examples |
| `authority` | server/authority/proxy examples |
| `spawn-prefab` | prefab spawn patterns |
| `resource-load` | `Resource.Load` patterns |
| `resource-picker-config` | Workbench resource picker attributes/config surfaces |
| `magazine` | weapon magazine/ammo behavior |
| `character-inventory` | inventory/gear/arsenal patterns |
| `compartment` | vehicle compartment access and setup |
| `vehicle-component` | vehicle controller/component patterns |
| `anim-graph` | animation graph/command patterns |
| `sound-event` | sound event/component patterns |
| `hud` | HUD widget/script patterns |
| `layout` | UI layout resource patterns |
| `workbench-plugin` | Workbench plugin classes and attributes |

## Procedures And Ordered Steps

Example-first coding loop:
1. Route task to exactly one source-owning topical reference.
2. Read that reference in full.
3. Use this reference to choose sample roots and example queries.
4. Run one exact or subtopic query first.
5. If top results are noisy, switch to a targeted `files` command using class, subsystem, or path family names from the topical reference.
6. Use a bounded snippet command for the best candidate file.
7. Verify APIs through exact symbol/method/attribute lookup.
8. Apply the smallest correct project change.
9. Validate in Workbench/runtime/server/multiplayer/editor context appropriate to the topic.

Broad-search recovery loop:
1. If `examples <topic>` returns unrelated domains, do not use the top result blindly.
2. Add `--subtopic` if the task has a known subtopic.
3. If subtopic still returns mixed results, use `files <class-or-family>`.
4. If a source-owning reference names a class, use exact `symbol`, `method`, or `attribute` lookup.
5. Only then open snippets.

Official sample review loop:
1. Choose the closest sample root from the table.
2. Inspect folder/resource shape and project structure.
3. Compare layout against the topical reference.
4. Treat missing sample coverage as normal; many runtime patterns are better represented in game-source examples.
5. Do not use sample code to override official wiki workflow detail or current query output.

## Warnings And Failure Modes

- Do not use this reference as workflow authority. It routes examples only.
- Do not copy sample source bodies into answers or generated references.
- Do not assume sample API signatures are current. Always query exact APIs.
- Do not assume broad `examples` output is precise. Some domains return cross-topic examples because real game systems overlap.
- Broad `examples scenario-framework` can return unrelated task/faction/replication/AI-adjacent results; prefer targeted `files ScenarioFramework` and class-family searches.
- Broad `examples game-mode` can return generic GameMode mentions; prefer task/faction/game-mode class families from the topical reference.
- Broad `examples ai` can return resource, inventory, UI, and vehicle examples because AI scripted nodes interact with those systems; prefer `files AI`, `files Behavior`, and `files AITask`.
- UI, weapon, vehicle, inventory, and audio examples often cross domains. Route workflow ownership to the domain reference before using the file as an implementation pattern.
- Generated files are signature truth, not usually good implementation examples.
- Handwritten files are implementation-pattern truth, but may be domain-specific; do not generalize without checking the owning reference.
- Bounded snippets are preferred. Loading large source files defeats the low-context tooling model.

## API Lookup Keys

Use examples to discover candidate names, then verify exact APIs through `references/api-lookup-and-common-symbols.md` and query commands.

High-value lookup keys surfaced by example routing:
- Components: `ScriptComponent`, `ScriptComponentClass`, `GenericComponent`, `IEntity`, `FindComponent`, `EventMask`, `EOnInit`, `OnPostInit`.
- Replication: `RplComponent`, `BaseRplComponent`, `RplProp`, `RplRpc`, `RplSave`, `RplLoad`, `RplRole`.
- Resources/prefabs: `ResourceName`, `Resource.Load`, `EntitySpawnParams`, `SpawnEntityPrefab`, `ResourceNamePicker`.
- Workbench: `WorkbenchPlugin`, `WorkbenchPluginAttribute`, `RunCommandline`, `ResourceManager`.
- Scenario/game mode: `SCR_ScenarioFramework`, `SCR_BaseGameMode`, `GameMode`, `SCR_TaskSystem`, `SCR_Faction`.
- Weapons: `BaseWeaponComponent`, `WeaponComponent`, `BaseMuzzleComponent`, `BaseMagazineComponent`, `MagazineComponent`.
- Inventory: `CharacterInventory`, `InventoryStorageManagerComponent`, `InventoryItemComponent`, `ScriptedInventoryOperationCallback`.
- Vehicles: `VehicleControllerComponent`, `BaseCompartmentManagerComponent`, `CompartmentManagerComponent`, `BaseVehicleControllerComponent`.
- Animation: `CharacterAnimationComponent`, `BaseAnimPhysComponent`, `AnimPhysCommand`, `CharacterCommand`.
- Audio: `SoundComponent`, `SoundEvent`, `SoundEventName`, `SCR_SoundManagerModule`, `AudioSystem`.
- UI: `Widget`, `TextWidget`, `ImageWidget`, `SCR_HUD`, `MenuBase`, `CreateWidgets`.
- AI: `AITask`, `AITaskScripted`, `DecoratorScripted`, `ENodeResult`, `AIControlComponent`, `SCR_AIAgentDebugPanel`.

## Game-Data Query Commands

Core example families:

```powershell
py -3 scripts\query-reforger-data.py examples component --limit 8
py -3 scripts\query-reforger-data.py examples replication --limit 8
py -3 scripts\query-reforger-data.py examples resource-loading --limit 8
py -3 scripts\query-reforger-data.py examples workbench-plugin --limit 8
py -3 scripts\query-reforger-data.py examples scenario-framework --limit 8
py -3 scripts\query-reforger-data.py examples game-mode --limit 8
py -3 scripts\query-reforger-data.py examples weapon --limit 8
py -3 scripts\query-reforger-data.py examples inventory --limit 8
py -3 scripts\query-reforger-data.py examples vehicle --limit 8
py -3 scripts\query-reforger-data.py examples animation --limit 8
py -3 scripts\query-reforger-data.py examples audio --limit 8
py -3 scripts\query-reforger-data.py examples ui --limit 8
py -3 scripts\query-reforger-data.py examples ai --limit 8
```

Targeted subtopic routes:

```powershell
py -3 scripts\query-reforger-data.py examples component --subtopic script-component --limit 8
py -3 scripts\query-reforger-data.py examples component --subtopic lifecycle --limit 8
py -3 scripts\query-reforger-data.py examples replication --subtopic rpl-prop --limit 8
py -3 scripts\query-reforger-data.py examples replication --subtopic rpc --limit 8
py -3 scripts\query-reforger-data.py examples resource-loading --subtopic spawn-prefab --limit 8
py -3 scripts\query-reforger-data.py examples resource-loading --subtopic resource-load --limit 8
py -3 scripts\query-reforger-data.py examples weapon --subtopic magazine --limit 8
py -3 scripts\query-reforger-data.py examples inventory --subtopic character-inventory --limit 8
py -3 scripts\query-reforger-data.py examples vehicle --subtopic compartment --limit 8
py -3 scripts\query-reforger-data.py examples animation --subtopic anim-graph --limit 8
py -3 scripts\query-reforger-data.py examples audio --subtopic sound-event --limit 8
py -3 scripts\query-reforger-data.py examples ui --subtopic hud --limit 8
py -3 scripts\query-reforger-data.py examples ui --subtopic layout --limit 8
```

Fallback file routes for noisy families:

```powershell
py -3 scripts\query-reforger-data.py files ScenarioFramework --limit 8
py -3 scripts\query-reforger-data.py files SCR_ScenarioFramework --limit 8
py -3 scripts\query-reforger-data.py files SCR_TaskSystem --limit 8
py -3 scripts\query-reforger-data.py files SCR_Faction --limit 8
py -3 scripts\query-reforger-data.py files GameMode --limit 8
py -3 scripts\query-reforger-data.py files AI --limit 8
py -3 scripts\query-reforger-data.py files Behavior --limit 8
py -3 scripts\query-reforger-data.py files AITask --limit 8
py -3 scripts\query-reforger-data.py files Weapon --limit 8
py -3 scripts\query-reforger-data.py files Vehicle --limit 8
py -3 scripts\query-reforger-data.py files HUD --limit 8
```

Bounded snippets after selecting a file:

```powershell
py -3 scripts\query-reforger-data.py snippet <scripts/path/from/query.c> --line <line> --context 40
```

Replace `<scripts/path/from/query.c>` and `<line>` with the file and line returned by query output. Do not guess paths.

## Examples And Samples

Official sample map:
- `SampleMod_Main`: broad project structure, resources, configs, terrain/worlds, UI, catalogs, arsenal, mission thumbnails, and baseline sample layout.
- `SampleMod_ModdedScript`: modded script and script override layout.
- `SampleMod_WorkbenchPlugin`: Workbench plugin and editor-extension layout.
- `SampleMod_NewWeapon`: new weapon asset, prefab, and config layout.
- `SampleMod_ModdedWeapon`: weapon modification/replacement layout.
- `SampleMod_NewCar`: new vehicle asset, prefab, and simulation layout.
- `SampleMod_ModdedCar`: vehicle modification/replacement layout.
- `SampleMod_NewCharacter`: character gear, clothing, inventory, and loadout layout.
- `SampleMod_NewFaction`: faction, campaign, group, and game-mode integration layout.
- `SampleMod_NewProp`: prop, model, material, texture, and prefab layout.
- `SampleMod_AnimationWorkshop`: animation graph/export/workshop layout.
- `SampleMod_CinematicTutorial`: cinematic and animation tutorial layout.
- `SampleMod_Replacement`: replacement mod layout.

Game-source example anchors observed through query:
- Component examples: `SCR_AISettingsComponent`, `SCR_CacheNoteComponent`, `SCR_CallsignBaseComponent`, `SCR_HybridPhysicsComponent`.
- Replication examples: `RplDocs.c`, `SCR_RplTestComponent`, deployable item replication, firing range replication, respawn timer replication.
- Resource loading examples: game modes and editor components that combine `ResourceName`, `Resource.Load`, `EntitySpawnParams`, and prefab spawning.
- Workbench plugin examples: `SCR_TracyPlugin`, resave tools, resource test tools, world test tools, editable entity maintenance plugin.
- Weapon examples: mine weapon component, HUD weapon info, BIKI weapon helper, muzzle/magazine/turret examples, AI weapon scripted nodes.
- Inventory examples: scripted inventory storage manager, headgear inventory component, AI inventory scripted nodes, arsenal storage manager.
- Vehicle examples: vehicle controller, compartment manager, vehicle entity, vehicle debug, AI vehicle utility/scripted nodes.
- Animation examples: character command swim/fly/loiter, animation command handler, anim phys command, Scenario Framework animation action.
- Audio examples: voiceover data/system, bell/trigger/building/communication sound components, sound manager module.
- UI examples: HUD menu component, selection menu entries, deploy/debriefing menu, map marker menu entries.
- AI examples: AI scripted nodes often surface as inventory/resource/vehicle examples; use AI reference plus `files AI`, `files Behavior`, and `files AITask`.

## Follow-Up Keywords

- SampleMod_Main
- SampleMod_ModdedScript
- SampleMod_WorkbenchPlugin
- SampleMod_NewWeapon
- SampleMod_ModdedWeapon
- SampleMod_NewCar
- SampleMod_ModdedCar
- SampleMod_NewCharacter
- SampleMod_NewFaction
- SampleMod_NewProp
- SampleMod_AnimationWorkshop
- SampleMod_CinematicTutorial
- SampleMod_Replacement
- script-component
- lifecycle
- rpl-prop
- rpc
- authority
- spawn-prefab
- resource-load
- resource-picker-config
- magazine
- character-inventory
- compartment
- anim-graph
- sound-event
- hud
- layout
- workbench-plugin
- ScenarioFramework
- GameMode
- AI
- Behavior

## Verification

Before using an example as implementation guidance:

1. Confirm the source-owning topical reference was read.
2. Confirm the chosen example came from query output or an official sample root.
3. Confirm every API-sensitive symbol is verified by exact query command.
4. Confirm generated records are used for signatures and handwritten records for patterns.
5. Confirm broad/noisy example routes were narrowed with subtopics or `files` commands where needed.
6. Confirm snippets are bounded and directly tied to returned file/line references.
7. Confirm sample layout is treated as a signal, not as current API truth.
8. Run the validation appropriate to the domain: Workbench import/editor checks, runtime checks, multiplayer/dedicated server checks, asset validation, or UI/audio/animation editor checks.

## Official Wiki Links

This utility reference owns no primary wiki pages. Use the official links in the source-owning topical reference for workflow provenance.

High-level official wiki entry points for human follow-up:
- Arma Reforger Modding: https://community.bistudio.com/wiki/Arma_Reforger:Modding
- Workbench: https://community.bistudio.com/wiki/Arma_Reforger:Workbench
- Resource Manager: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager
- Enfusion Script: https://community.bistudio.com/wiki/Arma_Reforger:Enforce_Script_Syntax
- Multiplayer Scripting: https://community.bistudio.com/wiki/Arma_Reforger:Multiplayer_Scripting

## Usefulness Score

Score: 92/100

- Wiki coverage: 26/30. This utility reference owns no primary wiki pages and explicitly routes workflow provenance to topical references. Points are reserved because wiki detail is intentionally not duplicated here.
- Operational detail: 13/15. The reference gives concrete routing workflows, sample roles, subtopic routes, and noisy-search recovery. It intentionally avoids domain workflow steps owned elsewhere.
- API lookup usefulness: 15/15. Example-sensitive guidance routes to exact query commands, subtopics, file searches, and bounded snippets.
- Example grounding: 10/10. All official sample roots are listed and major game-source example families are mapped to query routes.
- Codex task usefulness: 14/15. Common task families route to one topical reference plus sample/query commands. One point is reserved because some broad query routes remain inherently noisy.
- Context efficiency: 9/10. The file is dense and navigable without copying source bodies or API dumps. The routing table is broad by design.
- Verification guidance: 5/5. The reference requires topical reference reading, exact API verification, bounded snippets, and domain validation.

Category-fit check:
- Source family complete: pass. Utility ownership is sample/example routing only.
- No owned page missing: pass. No primary wiki pages are owned.
- Split boundary justified: pass. Topical references own workflow detail; this file owns example routes.
- Cross-links present: pass.
- Task route clear: pass. Each common task family routes to one topical reference plus query/sample routes.

Missed coverage and cap review:
- No owned primary wiki page was skipped.
- No workflow sections are omitted because this reference owns no workflow wiki pages.
- No API-sensitive claims are made without query commands.
- No automatic failure condition applies.
