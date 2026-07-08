# Common Task Recipes

## When To Read

Read this when a user asks for a Reforger scripting/modding task and Codex needs a compact route to the right reference, exact API query commands, examples, snippets, and verification checks.

This is a router, not a workflow source. For any non-trivial task, read the listed primary reference in full before coding or answering. Do not use this file to replace source-owning references, exact API lookup, or example review.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: none. This utility reference owns task routing only.
- Secondary/cross-reference topics: every source-owning runtime reference listed below.

Wiki pages reviewed:
- No primary wiki pages are owned by this reference. Workflow wiki content remains in topical references.

Wiki sections covered:
- Not applicable. Each recipe routes to the reference that owns section coverage.

Structured wiki records:
- Tables reviewed/included: not applicable.
- Procedures reviewed/included: not applicable.
- Admonitions reviewed/included: not applicable.
- Code blocks reviewed/included: none copied.
- Media reviewed: not applicable.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts\query-reforger-data.py lookup "make a user action" --limit 8`
  - `py -3 scripts\query-reforger-data.py lookup "make a replicated component" --limit 8`
  - `py -3 scripts\query-reforger-data.py lookup "spawn prefab" --limit 8`
  - `py -3 scripts\query-reforger-data.py lookup "workbench plugin" --limit 8`
  - `py -3 scripts\query-reforger-data.py lookup "vehicle compartment" --limit 8`
  - `py -3 scripts\query-reforger-data.py lookup "unknown made-up task" --limit 8`
- Symbols/methods/attributes verified through lookup routes: `ScriptedUserAction`, `BaseUserAction`, `RplComponent`, `BaseRplComponent`, `RplProp`, `RplRpc`, `ScriptComponent`, `EntitySpawnParams`, `ResourceName`, `Resource.Load`, `Game.SpawnEntityPrefab`, `WorkbenchPlugin`, `WorkbenchPluginAttribute`, `VehicleControllerComponent`, `BaseCompartmentManagerComponent`.
- Examples/snippets reviewed through lookup routes: user action examples, `RplDocs.c`, replication test components, resource/prefab spawn examples, Workbench plugin examples, vehicle controller/compartment examples, and unmatched lookup behavior.

Samples and source examples:
- Official sample folders reviewed indirectly through `references/examples-and-sample-patterns.md`.
- Raw game-source example families reviewed indirectly through lookup and example routes listed in each recipe.

Coverage gaps:
- Missing, excluded, or intentionally deferred source: no workflow wiki sections, sample map detail, source bodies, or API dumps are repeated here.
- Reason and impact: this file must stay a compact action router. Opening the primary reference and query results remains mandatory for correctness.

## Wiki Source Coverage

This reference has no primary wiki ownership. It points to the runtime reference that owns the relevant wiki pages and workflow detail. If a recipe seems too short, read the primary reference rather than expanding this file.

## Terms And Concepts

- Primary reference: the one runtime reference Codex must read in full before acting on the recipe.
- Lookup command: deterministic task bundle from `scripts\query-reforger-data.py lookup`.
- Exact API command: `symbol`, `method`, `attribute`, or `inherits` query for signatures and class relationships.
- Example command: `examples` or `files` query for implementation patterns.
- Snippet command: bounded source inspection after a file and line are known.
- Residual verification: Workbench, runtime, multiplayer, dedicated server, asset, editor, or packaging checks that query output cannot prove.
- Unmatched lookup: a lookup response that explicitly says no task rule matched. Do not infer an unrelated task from it.

## Workbench / Resource / Data Surfaces

Recipes commonly cross these surfaces:

- Workbench resources, prefabs, configs, editors, and plugin registration.
- Enfusion Script source files and generated API files.
- Entity/component prefab wiring and lifecycle.
- Runtime world, game mode, server, multiplayer, and dedicated server contexts.
- Domain editors such as Resource Manager, World Editor, Animation Editor, Audio Editor, and UI Layout Editor.

Use the recipe to find the owning surface, then use the owning reference to preserve workflow detail.

## Required Workflows

Default task loop:
1. Identify the task family.
2. Read the primary reference listed in the recipe.
3. Run the task lookup command if one exists.
4. Run exact API commands for every uncertain class, method, attribute, enum, inheritance relationship, and callback.
5. Run example or file commands for implementation patterns.
6. Open only bounded snippets from selected query results.
7. Make the smallest correct change that preserves current behavior.
8. Perform residual verification and state anything not verified.

Unknown or ambiguous task loop:
1. Run `py -3 scripts\query-reforger-data.py lookup "<task phrase>" --limit 8`.
2. If the result is `lookup unmatched`, do not choose a confident recipe.
3. Refine with targeted searches:
   - `py -3 scripts\query-reforger-data.py files <keyword> --limit 8`
   - `py -3 scripts\query-reforger-data.py examples <topic> --limit 8`
   - `py -3 scripts\query-reforger-data.py symbol <name> --limit 8`
   - `py -3 scripts\query-reforger-data.py method <name> --limit 8`
4. Read the closest topical reference after evidence points to one.
5. If no confident owner emerges, answer with the uncertainty and ask for a more specific Reforger task.

## Configuration Fields And Tables

Task routing table:

| Task | Primary reference | Query route | Example route | Residual verification |
| --- | --- | --- | --- | --- |
| Make a script component | `entities-components-and-lifecycle.md` | `symbol ScriptComponent --kind class --exact`; `symbol ScriptComponentClass --kind class --exact` | `examples component --subtopic script-component --limit 8` | Workbench prefab/component wiring and runtime lifecycle |
| Make a user action | `script-events-actions-and-patterns.md` | `lookup "make a user action" --limit 8` | Snippets suggested by lookup; `inherits ScriptedUserAction` | Entity/player context, visibility, performability, dedicated server |
| Create a replicated component | `multiplayer-replication-and-authority.md` | `lookup "make a replicated component" --limit 8`; `attribute RplProp --exact`; `attribute RplRpc --exact` | `examples replication --subtopic rpl-prop --limit 8`; `examples replication --subtopic rpc --limit 8` | Authority/proxy paths, JIP, dedicated server |
| Spawn a prefab | `prefabs-configs-containers-and-catalogs.md` | `lookup "spawn prefab" --limit 8`; `symbol ResourceName --exact`; `method Resource Load --exact` | `examples resource-loading --subtopic spawn-prefab --limit 8` | Resource path, prefab dependencies, world/authority context |
| Load a resource | `prefabs-configs-containers-and-catalogs.md` | `lookup "load resource" --limit 8`; `method Resource Load --exact` | `examples resource-loading --subtopic resource-load --limit 8` | Resource exists, dependencies load, Workbench validation |
| Create a Workbench plugin | `workbench-plugins-and-editor-tools.md` | `lookup "workbench plugin" --limit 8`; `symbol WorkbenchPlugin --kind class --exact` | `examples workbench-plugin --limit 8`; `files WorkbenchPlugin --limit 8` | Plugin menu visibility, module registration, Workbench runtime |
| Build Scenario Framework content | `scenario-framework.md` | `files SCR_ScenarioFramework --limit 8`; `files SCR_ScenarioFrameworkTask --limit 8` | `examples scenario-framework --limit 8` as secondary because it can be noisy | Scenario hierarchy, debug tools, runtime task behavior |
| Game Master/faction/task/game mode | `game-master-factions-tasks-and-modes.md` | `files SCR_TaskSystem --limit 8`; `files SCR_Faction --limit 8`; `files GameMode --limit 8` | `examples game-mode --limit 8` | Workbench config, runtime, multiplayer/game-mode behavior |
| Configure a server | `server-hosting-startup-and-runtime.md` | `files server --limit 8`; `files GameMode --limit 8` | `examples game-mode --limit 8` | Config JSON, startup params, ports, mods, dedicated server |
| Import an asset or prop | `asset-import-models-materials-and-props.md` | `files ResourceImport --limit 8`; `files ValidateFBX --limit 8`; `files Particle --limit 8` | `examples resource-loading --limit 8` | Import settings, materials, LOD/collision, Workbench asset validation |
| Create weapon behavior | `weapons-prefabs-attachments-and-firearms.md` | `lookup "create weapon script" --limit 8`; `files BaseWeaponComponent --limit 8` | `examples weapon --limit 8` | Weapon prefab/config setup, attachments, runtime firing/animation/audio |
| Add magazine or ammo behavior | `weapons-prefabs-attachments-and-firearms.md` | `lookup "add magazine or ammo behavior" --limit 8`; `files BaseMagazineComponent --limit 8` | `examples weapon --subtopic magazine --limit 8` | Magazine/muzzle/ammo config, inventory, firing runtime |
| Use CharacterInventory | `character-gear-inventory-and-arsenal.md` | `lookup "use CharacterInventory" --limit 8`; `files CharacterInventory --limit 8` | `examples inventory --subtopic character-inventory --limit 8` | Gear prefab, arsenal/catalog visibility, runtime equip/storage |
| Configure a vehicle compartment | `vehicles-creation-simulation-and-compartments.md` | `lookup "vehicle compartment" --limit 8`; `files BaseCompartmentManagerComponent --limit 8` | `examples vehicle --subtopic compartment --limit 8` | Vehicle prefab seats/actions, Workbench wiring, runtime entry/exit |
| Find animation graph examples | `animation-graphs-weapon-animation-and-export.md` | `lookup "find animation graph examples" --limit 8`; `files CharacterAnimationComponent --limit 8` | `examples animation --subtopic anim-graph --limit 8` | Animation Editor graph/export/runtime validation |
| Play a sound event | `audio-editor-signals-and-sound-systems.md` | `lookup "play a sound event" --limit 8`; `files SoundEvent --limit 8` | `examples audio --subtopic sound-event --limit 8` | Audio resource/event exists, signals/variables, runtime playback |
| Create HUD widget | `ui-layouts-dialogs-and-menus.md` | `lookup "create HUD widget" --limit 8`; `files HUD --limit 8`; `files Widget --limit 8` | `examples ui --subtopic hud --limit 8`; `examples ui --subtopic layout --limit 8` | Layout resource, widget names, runtime menu/HUD display |
| AI behavior/debug | `ai-behavior-commanding-and-debug.md` | `files AI --limit 8`; `files Behavior --limit 8`; `files AITask --limit 8` | `examples ai --limit 8` as secondary because it can be noisy | Behavior Editor graph, navmesh, AI debug panel, runtime behavior |
| Terrain/world/navmesh | `terrain-creation-and-world-setup.md` or `world-editor-tools-generators-and-navmesh.md` | `files Terrain --limit 8`; `files WorldEditor --limit 8`; `files Navmesh --limit 8` | `examples workbench-plugin --subtopic editor-ui --limit 8` only for editor tooling patterns | Terrain data, world setup, navmesh build/validation |

## Procedures And Ordered Steps

Recipe use procedure:
1. Match the user's task to one row in the task routing table.
2. Read the primary reference in full.
3. Run the lookup or exact query commands from the row.
4. If the query result suggests snippets, inspect at most the relevant bounded snippets.
5. If examples are needed, read `references/examples-and-sample-patterns.md` and use the example route.
6. If a task crosses domains, read the one owning the changed workflow first, then the secondary reference only for the crossed surface.
7. Do not implement from this recipe alone.

Cross-domain examples:
- A replicated vehicle compartment change starts with `vehicles-creation-simulation-and-compartments.md`, then checks `multiplayer-replication-and-authority.md` for replication behavior.
- A weapon UI/HUD change starts with `weapons-prefabs-attachments-and-firearms.md` if weapon behavior is primary, or `ui-layouts-dialogs-and-menus.md` if UI display is primary.
- AI movement failure starts with `ai-behavior-commanding-and-debug.md`, then routes to `world-editor-tools-generators-and-navmesh.md` if navmesh is implicated.
- Server-side replicated prefab spawning starts with `prefabs-configs-containers-and-catalogs.md`, then checks `multiplayer-replication-and-authority.md` and `server-hosting-startup-and-runtime.md`.

Snippet procedure:
1. Run a lookup/examples/files command.
2. Choose a returned file and line.
3. Run:
   ```powershell
   py -3 scripts\query-reforger-data.py snippet <scripts/path/from/query.c> --line <line> --context 40
   ```
4. Do not guess snippet paths or line numbers.

## Warnings And Failure Modes

- Do not use a recipe as API truth.
- Do not skip the primary reference.
- Do not use broad examples when a lookup or exact file route exists.
- Do not let an unmatched lookup fall back to an unrelated confident recipe.
- Do not turn this file into a duplicate of workflow references.
- Do not copy source bodies or sample bodies.
- Do not load large API dumps for normal tasks; query exact symbols/methods/attributes instead.
- If lookup output and a topical reference seem to disagree, verify with exact symbol/method/attribute query and inspect bounded source snippets.

## API Lookup Keys

Common exact lookup keys:
- Script components: `ScriptComponent`, `ScriptComponentClass`, `GenericComponent`, `IEntity`, `FindComponent`.
- User actions: `ScriptedUserAction`, `BaseUserAction`, `PerformAction`, `CanBeShownScript`, `CanBePerformedScript`.
- Replication: `RplComponent`, `BaseRplComponent`, `RplProp`, `RplRpc`, `RplSave`, `RplLoad`.
- Resources/prefabs: `ResourceName`, `Resource.Load`, `EntitySpawnParams`, `SpawnEntityPrefab`.
- Workbench plugins: `WorkbenchPlugin`, `WorkbenchPluginAttribute`, `Run`, `RunCommandline`.
- Scenario/game mode: `SCR_ScenarioFramework`, `SCR_TaskSystem`, `SCR_Faction`, `GameMode`, `SCR_BaseGameMode`.
- Assets/import: `ResourceImport`, `ValidateFBX`, `ParticleEffectEntity`.
- Weapons: `BaseWeaponComponent`, `WeaponComponent`, `BaseMuzzleComponent`, `BaseMagazineComponent`.
- Inventory: `CharacterInventory`, `InventoryStorageManagerComponent`, `InventoryItemComponent`.
- Vehicles: `VehicleControllerComponent`, `BaseCompartmentManagerComponent`, `CompartmentManagerComponent`.
- Animation: `CharacterAnimationComponent`, `BaseAnimPhysComponent`, `AnimPhysCommand`.
- Audio: `SoundComponent`, `SoundEvent`, `SoundEventName`, `SCR_SoundManagerModule`.
- UI: `Widget`, `TextWidget`, `ImageWidget`, `SCR_HUD`, `MenuBase`.
- AI: `AITask`, `AITaskScripted`, `DecoratorScripted`, `ENodeResult`, `AIControlComponent`.

## Game-Data Query Commands

Task lookup commands:

```powershell
py -3 scripts\query-reforger-data.py lookup "make a user action" --limit 8
py -3 scripts\query-reforger-data.py lookup "make a replicated component" --limit 8
py -3 scripts\query-reforger-data.py lookup "spawn prefab" --limit 8
py -3 scripts\query-reforger-data.py lookup "load resource" --limit 8
py -3 scripts\query-reforger-data.py lookup "workbench plugin" --limit 8
py -3 scripts\query-reforger-data.py lookup "create weapon script" --limit 8
py -3 scripts\query-reforger-data.py lookup "add magazine or ammo behavior" --limit 8
py -3 scripts\query-reforger-data.py lookup "use CharacterInventory" --limit 8
py -3 scripts\query-reforger-data.py lookup "vehicle compartment" --limit 8
py -3 scripts\query-reforger-data.py lookup "find animation graph examples" --limit 8
py -3 scripts\query-reforger-data.py lookup "play a sound event" --limit 8
py -3 scripts\query-reforger-data.py lookup "create HUD widget" --limit 8
```

Exact API commands:

```powershell
py -3 scripts\query-reforger-data.py symbol ScriptComponent --kind class --exact
py -3 scripts\query-reforger-data.py symbol ScriptedUserAction --kind class --exact
py -3 scripts\query-reforger-data.py attribute RplProp --exact
py -3 scripts\query-reforger-data.py attribute RplRpc --exact
py -3 scripts\query-reforger-data.py symbol ResourceName --exact
py -3 scripts\query-reforger-data.py method Resource Load --exact
py -3 scripts\query-reforger-data.py symbol WorkbenchPlugin --kind class --exact
py -3 scripts\query-reforger-data.py files BaseCompartmentManagerComponent --limit 8
```

Example routes:

```powershell
py -3 scripts\query-reforger-data.py examples component --subtopic script-component --limit 8
py -3 scripts\query-reforger-data.py examples replication --subtopic rpc --limit 8
py -3 scripts\query-reforger-data.py examples resource-loading --subtopic spawn-prefab --limit 8
py -3 scripts\query-reforger-data.py examples workbench-plugin --limit 8
py -3 scripts\query-reforger-data.py examples weapon --subtopic magazine --limit 8
py -3 scripts\query-reforger-data.py examples inventory --subtopic character-inventory --limit 8
py -3 scripts\query-reforger-data.py examples vehicle --subtopic compartment --limit 8
py -3 scripts\query-reforger-data.py examples animation --subtopic anim-graph --limit 8
py -3 scripts\query-reforger-data.py examples audio --subtopic sound-event --limit 8
py -3 scripts\query-reforger-data.py examples ui --subtopic hud --limit 8
```

Unmatched fallback:

```powershell
py -3 scripts\query-reforger-data.py lookup "<task phrase>" --limit 8
py -3 scripts\query-reforger-data.py files <keyword> --limit 8
py -3 scripts\query-reforger-data.py examples <topic> --limit 8
py -3 scripts\query-reforger-data.py symbol <name> --limit 8
py -3 scripts\query-reforger-data.py method <name> --limit 8
```

## Examples And Samples

Use `references/examples-and-sample-patterns.md` for the sample map and example-family routes. This file only points to it to avoid duplicating the sample inventory.

Recipe-level example guidance:
- Prefer lookup-suggested snippets when the `lookup` command returns a matched task.
- Prefer subtopic `examples` commands when the task family is known.
- Prefer `files` commands when broad `examples` routes are noisy.
- Prefer generated API files for signatures and handwritten files for patterns.

## Follow-Up Keywords

- make a user action
- make a replicated component
- spawn prefab
- load resource
- workbench plugin
- create weapon script
- magazine
- CharacterInventory
- vehicle compartment
- animation graph
- sound event
- HUD widget
- AI behavior
- ScenarioFramework
- GameMode
- server config
- navmesh
- ResourceName
- ScriptComponent
- RplProp
- RplRpc
- WorkbenchPlugin

## Verification

Every recipe still requires verification outside the recipe:

1. Primary reference read in full.
2. Exact API lookup completed for uncertain classes/methods/attributes.
3. Examples/snippets inspected only after query output identifies a file and line.
4. Smallest correct change applied.
5. Workbench/editor validation performed when the task touches resources, prefabs, configs, editors, plugins, assets, animation, audio, UI, terrain, or navmesh.
6. Runtime validation performed for gameplay behavior.
7. Multiplayer/dedicated server validation performed for replication, authority, server config, commands, actions, and server-side spawning.
8. Any unverified Workbench/runtime/server behavior stated explicitly.

## Official Wiki Links

This utility reference owns no primary wiki pages. Use official links in the source-owning topical references for workflow provenance.

High-level official wiki entry points for human follow-up:
- Arma Reforger Modding: https://community.bistudio.com/wiki/Arma_Reforger:Modding
- Enfusion Script Syntax: https://community.bistudio.com/wiki/Arma_Reforger:Enforce_Script_Syntax
- Multiplayer Scripting: https://community.bistudio.com/wiki/Arma_Reforger:Multiplayer_Scripting
- Workbench: https://community.bistudio.com/wiki/Arma_Reforger:Workbench
- Resource Manager: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager

## Usefulness Score

Score: 93/100

- Wiki coverage: 26/30. This utility reference owns no primary wiki pages and explicitly routes to source-owning references. Points are reserved because workflow details are intentionally not duplicated.
- Operational detail: 14/15. Recipes include primary reference, query route, example route, and verification note. Detailed workflows remain in topical references by design.
- API lookup usefulness: 15/15. Recipes include exact lookup, symbol, method, attribute, example, files, and snippet route patterns.
- Example grounding: 9/10. Example routes point to `examples-and-sample-patterns.md` and query commands. One point is reserved because this file intentionally does not repeat the full sample map.
- Codex task usefulness: 15/15. Common task families route to one primary reference plus query commands and verification.
- Context efficiency: 9/10. The file is compact for the breadth it covers. One point is reserved because the routing table is necessarily broad.
- Verification guidance: 5/5. Workbench, runtime, multiplayer, dedicated server, editor, asset, and uncertainty checks are explicit.

Category-fit check:
- Source family complete: pass. This reference owns routing recipes only.
- No owned page missing: pass. No primary wiki pages are owned.
- Split boundary justified: pass. Workflow, API lookup, and sample maps are routed to their owners.
- Cross-links present: pass.
- Task route clear: pass. Each recipe has one primary reference plus query commands.

Missed coverage and cap review:
- No owned primary wiki page was skipped.
- No workflow wiki section is omitted because this file owns no workflow wiki source.
- No API-sensitive claim is made without query routes.
- Unknown/unmatched task behavior is explicit.
- No automatic failure condition applies.
