# Start Here: Source Authority

## When To Read

Read this first when a Reforger task is broad, ambiguous, or touches more than one surface. Use it to route into the smallest relevant reference before writing code, editing data, changing prefabs/configs, or answering API-sensitive questions.

This reference is a router and source-authority guide. It intentionally does not own detailed workflow bodies for scripting, Workbench, prefabs, terrain, assets, vehicles, weapons, animation, audio, UI, AI, server runtime, or Scenario Framework. It points to the reference that owns each workflow.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: overview, source authority, modding entry points, project/source identity, data-modification concepts.
- Secondary/cross-reference topics: resource workflows, Workbench metadata, Workbench links, samples, scripting, packaging.

Wiki pages reviewed:
- Arma Reforger - Category - https://community.bistudio.com/wiki/Category:Arma_Reforger - status: covered - reason: top-level product/source orientation.
- Modding - Arma Reforger Category - https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding - status: covered - reason: official modding source hierarchy.
- Getting Started - Arma Reforger - https://community.bistudio.com/wiki/Arma_Reforger:Getting_Started - status: covered - reason: product/game entry points and official channels.
- Data Modding Basics - Arma Reforger - https://community.bistudio.com/wiki/Arma_Reforger:Data_Modding_Basics - status: covered - reason: core data modification, override, inherit, duplicate, replace concepts.
- Directory Structure - Arma Reforger - https://community.bistudio.com/wiki/Arma_Reforger:Directory_Structure - status: covered - reason: top-level addon/source folder meanings.
- Game Identity - Arma Reforger - https://community.bistudio.com/wiki/Arma_Reforger:Game_Identity - status: covered - reason: account/player identity terminology.
- Dictionary - Arma Reforger - https://community.bistudio.com/wiki/Arma_Reforger:Dictionary - status: covered - reason: Conflict mode glossary routing.
- Workbench Metadata - Arma Reforger - https://community.bistudio.com/wiki/Arma_Reforger:Workbench_Metadata - status: covered - reason: GUID and `.meta` source identity.
- Workbench Links - Arma Reforger - https://community.bistudio.com/wiki/Arma_Reforger:Workbench_Links - status: covered - reason: `enfusion://` links and editor deep-linking.
- Resource Manager: Getting Started Tutorial - Arma Reforger - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Getting_Started_Tutorial - status: partial - reason: supports first-launch and `enfusion://` setup; detailed Resource Manager ownership belongs to `resource-manager-file-types-and-editors.md`.

Wiki sections covered:
- Arma Reforger category: Introduction, Features, Getting Started, Subcategories.
- Modding category: modding page table, subcategories, pages in modding category.
- Getting Started: buy/start/play/mods/community/communication orientation.
- Data Modding Basics: moddability overview, moddability table, footnotes, basics, overriding, navigation, scripts, duplicate, inherit, transfer, replace, GUID, replacing scripts.
- Directory Structure: top-level directory table and folder purposes.
- Game Identity: definitions and scripting context.
- Dictionary: Conflict glossary routing.
- Workbench Metadata: `.meta`, GUID, GUID changes, `resourceDatabase.rdb`.
- Workbench Links: format, Resource Manager links, Script Editor links, World Editor links.
- Resource Manager getting started: first launch, new project routing, `enfusion://` protocol registration.

Structured wiki records:
- Tables reviewed/included: Data Modding Basics moddability table, data manipulation comparison table, Directory Structure table, Game Identity table, Dictionary glossary table, Modding category table, Workbench Links format table.
- Procedures reviewed/included: Getting Started settings checklist, Data Modding Basics footnotes, Workbench Metadata GUID warning bullets.
- Admonitions reviewed/included: Data Modding notes/warnings for override/replace/inherit behavior, GUID warnings, Workbench Links protocol warning, Resource Manager read-only base project note.
- Code blocks reviewed/included: Data Modding Basics replacing-script path example was reviewed but not copied; this reference records the rule and routes scripting details elsewhere.
- Media reviewed: screenshots and GIFs were reviewed as workflow evidence only; no media copied.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts\query-reforger-data.py symbol ResourceName --exact --limit 3`
  - `py -3 scripts\query-reforger-data.py symbol ScriptComponent --kind class --exact --limit 3`
  - `py -3 scripts\query-reforger-data.py attribute RplProp --exact --limit 3`
  - `py -3 scripts\query-reforger-data.py files WorkbenchPlugin --limit 3`
- Symbols/methods/attributes verified for routing evidence: `ResourceName`, `ScriptComponent`, `RplProp`, `WorkbenchPlugin` file examples.
- Examples/snippets reviewed: no snippets needed for this orientation reference.

Samples and source examples:
- Official sample folders reviewed as routing signals: `SampleMod_Main`, `SampleMod_ModdedScript`, `SampleMod_WorkbenchPlugin`, `SampleMod_NewWeapon`, `SampleMod_ModdedWeapon`, `SampleMod_NewCar`, `SampleMod_ModdedCar`, `SampleMod_NewCharacter`, `SampleMod_NewFaction`, `SampleMod_NewProp`, `SampleMod_AnimationWorkshop`, `SampleMod_CinematicTutorial`, `SampleMod_Replacement`.
- Raw game-source example families reviewed through query output: Workbench plugin file matches, generated API anchors, replication attribute anchor.

Coverage gaps:
- Detailed Resource Manager, scripting, addon setup, assets, terrain, server, and domain workflows are intentionally excluded here and owned by narrower references.
- This file does not copy full wiki tables. It preserves operational rules and routes detailed table-heavy work to the owning reference.

## Wiki Source Coverage

Arma Reforger is both a game and a modding platform built on Enfusion. Official wiki orientation describes it as a moddable platform with Game Master curation, multiplayer play, official tools, and a source hierarchy split between game content, modding, support, and Workbench/editor workflows.

The official modding category separates these high-level work areas:
- official tools and Resource Manager,
- project creation and Workshop publishing,
- content/data workflows,
- scripting,
- assets,
- audio,
- Game Master and Scenario work,
- terrains,
- tutorials and guidelines.

For Codex, this means most Reforger tasks are not pure scripting tasks. A correct answer often needs to identify whether the task is script-first, data-first, editor-first, asset-first, server-first, or mixed.

Data Modding Basics is the key orientation page for how Reforger content is changed. It distinguishes:
- replacement: a resource is fully replaced, usually by preserving or recreating the same GUID;
- modification/override: selected parts of a resource are changed while the original remains the base;
- inheritance: a new resource inherits from an existing file and gets its own identity;
- duplication: a copied resource becomes the active copied data for that GUID and does not inherit later parent changes;
- transfer: partially overridden data can be moved/merged into a parent addon when the parent is unpacked.

The wiki moddability table is important source authority. In practical terms:
- prefabs (`.et`), configs (`.conf`), layout definitions, material definitions, worlds, behaviors, audio projects, animations, particles, signals, materials, font configs, animation graphs, and similar metadata-backed resources are data/modding surfaces;
- models (`.xob`) and textures (`.edds`) are replacement-oriented assets rather than inherited data surfaces;
- script source (`.c`) has special rules: a script can be replaced by same relative path/name, but normal script extension should prefer Enfusion script mechanisms such as `modded`, `override`, and `super` when appropriate;
- files without metadata need different handling than resources with `.meta` and GUID identity.

Directory Structure is the source for top-level content family routing. Important folder families:
- `AI`: AI behavior and related data.
- `Anims`: animation configuration and actual character/procedural animations.
- `Assets`: source and imported game assets.
- `Configs`: configuration data.
- `Language`: localization.
- `Missions`: mission/scenario-related data.
- `Particles`: particle data.
- `PrefabLibrary`, `Prefabs`, `PrefabsEditable`: prefab families and editor/game prefab content.
- `Scripts`: Enfusion Script source.
- `Sounds`: audio data.
- `Terrains`, `Worlds`: terrain/world data.
- `UI`: UI resources.
- `WBData`: Workbench data.

Workbench Metadata defines resource identity. `.meta` files are created when resources are registered or created in Workbench. They carry GUID and build/import metadata. The engine tracks resource identity by GUID, not just by the visible file name or path. Moving or renaming through Workbench should preserve metadata behavior; manual GUID edits are dangerous because duplicate GUIDs across addons can overwrite each other or make one file fail.

Workbench Links define shareable editor links. They use `enfusion://` and can target Resource Manager, Script Editor, or World Editor. To use these links on Windows, the protocol must be registered through Workbench Options. These links are useful for humans and Workbench workflows, but Codex should not rely on live Workbench links as API truth.

Game Identity is account/player identity terminology. It matters for backend/player identity discussions, not for ordinary class/method signature lookup.

Dictionary currently contains Conflict mode terminology. Route deep Conflict, factions, tasks, and Game Master work to `game-master-factions-tasks-and-modes.md`.

## Terms And Concepts

- API truth: exact class, method, attribute, enum, parameter, return type, inheritance, and source line from current game data.
- Workflow truth: official wiki guidance about Workbench, data, editor procedures, server/runtime behavior, packaging, assets, terrain, audio, animation, and other non-code workflows.
- Example truth: official samples and raw game source patterns. Examples show implementation shape but do not override current API signatures.
- Project/local truth: existing user project code and local conventions. Preserve them unless they conflict with source authority.
- Resource: an Enfusion-managed file with resource identity, often tracked by metadata and GUID.
- GUID: resource identity used by the engine. GUID conflicts or manual edits can break or override content.
- `.meta`: Workbench-generated metadata for registered/created resources. Scripts are handled differently from metadata-backed resources.
- Override/modify: edit selected data in an addon while retaining an original resource relationship.
- Replace: substitute a resource by identity. Use extreme care because this can affect every reference to that GUID.
- Inherit: create a new resource that inherits parent data and can override selected attributes.
- Duplicate: copy a resource into the working addon. Treat it as a separate copied source of data, not a live inherited child.
- `modded`: Enfusion script mechanism for extending existing script classes.
- `override`: Enfusion script mechanism for overriding an inherited method.
- `super`: call into the overridden/inherited method behavior.
- `enfusion://`: Workbench link protocol for Resource Manager, Script Editor, and World Editor.

## Workbench / Resource / Data Surfaces

Use this routing when the user asks for a Reforger task:

| User task shape | First reference to read |
| --- | --- |
| Source authority, broad orientation, or unclear task | `start-here-source-authority.md` |
| Addon/project setup, `.gproj`, Workshop, packaging | `mod-projects-addons-workshop.md` |
| Enforce syntax, language rules, Script Editor usage | `enfusion-language-and-script-editor.md` |
| Gameplay script events, user actions, modded script patterns | `script-events-actions-and-patterns.md` |
| Generic entity/component lifecycle and prefab component wiring | `entities-components-and-lifecycle.md` |
| Exact API anchors and common query commands | `api-lookup-and-common-symbols.md` |
| Resource Manager tools, file types, editor panels | `resource-manager-file-types-and-editors.md` |
| Prefabs, configs, containers, catalogs, `ResourceName` | `prefabs-configs-containers-and-catalogs.md` |
| Multiplayer authority, replication, RPC | `multiplayer-replication-and-authority.md` |
| Server config, startup parameters, hosting/runtime | `server-hosting-startup-and-runtime.md` |
| Workbench plugins and editor extension tools | `workbench-plugins-and-editor-tools.md` |
| Diag Menu, performance, autotests, profiling | `diagnostics-testing-and-performance.md` |
| Scenario Framework hierarchy and setup | `scenario-framework.md` |
| Game Master, factions, tasks, game modes | `game-master-factions-tasks-and-modes.md` |
| Terrain creation and world foundation setup | `terrain-creation-and-world-setup.md` |
| World Editor tools, generators, navmesh | `world-editor-tools-generators-and-navmesh.md` |
| Asset import, models, props, materials, LOD/collision | `asset-import-models-materials-and-props.md` |
| Weapons, firearm prefabs, attachments, muzzle/ammo/magazine links | `weapons-prefabs-attachments-and-firearms.md` |
| Character gear, inventory, arsenal, wearable equipment | `character-gear-inventory-and-arsenal.md` |
| Vehicles, simulation, compartments, controls | `vehicles-creation-simulation-and-compartments.md` |
| Animation graphs, export, weapon animation | `animation-graphs-weapon-animation-and-export.md` |
| Audio Editor, signals, sound events/components | `audio-editor-signals-and-sound-systems.md` |
| UI layouts, dialogs, menus, widgets, HUD | `ui-layouts-dialogs-and-menus.md` |
| AI behavior, commanding, AI debug | `ai-behavior-commanding-and-debug.md` |
| Official sample and raw game-source example families | `examples-and-sample-patterns.md` |
| Common task recipes | `common-task-recipes.md` |

Read the chosen reference in full. Do not search inside references as a replacement for reading the relevant reference. Search and query tools are for exact API/source lookup after the relevant reference has established the correct workflow surface.

## Required Workflows

General action loop for Codex:

1. Classify the task surface: script, data/prefab/config, Workbench/editor, asset, terrain/world, audio, animation, UI, AI, server/runtime, packaging, or mixed.
2. Read the smallest owning reference in full.
3. Identify required data/editor steps before writing code.
4. Query exact APIs with `scripts\query-reforger-data.py` before writing or changing API-sensitive code.
5. Query examples or task lookup for implementation patterns.
6. Inspect bounded source snippets only when the query output identifies a concrete file and line.
7. Preserve local project style and current behavior.
8. Make the smallest correct change.
9. State what was verified and what still requires Workbench, runtime, multiplayer, server, packaging, or editor validation.

For data changes:

1. Decide whether the task needs override, inherit, duplicate, transfer, replacement, or script extension.
2. Prefer inherited or overridden data when the goal is targeted change.
3. Treat replacement and GUID changes as high-risk.
4. Check the owning data/resource reference before editing.
5. Verify with Workbench/Resource Manager where possible.

For script changes:

1. Do not infer an API from memory.
2. Use the topical reference to find lookup keys.
3. Use `symbol`, `method`, `attribute`, `inherits`, `examples`, `files`, or `lookup` query commands.
4. Use generated API records for signatures and handwritten examples for patterns.
5. Avoid introducing broad abstractions unless the user request or proven defect requires them.

## Configuration Fields And Tables

The reviewed wiki tables establish these orientation-level rules:

- Moddability is file-type dependent. Do not assume every resource can be replaced, modified, or inherited in the same way.
- `.et` prefabs and `.conf` configs are data surfaces that usually route to prefab/config references before code.
- `.c` scripts are code surfaces with same-path replacement behavior and `modded`/`override`/`super` extension patterns.
- `.meta` and GUID behavior define resource identity. GUID conflict risk must be considered before replacement or manual metadata changes.
- Workbench links use different modules and parameters:
  - Resource Manager: resource links.
  - Script Editor: script file and optional line number.
  - World Editor: world file, coordinates, camera orientation, and view parameters.
- Directory names are meaningful routing hints. `Scripts`, `Prefabs`, `Configs`, `UI`, `Sounds`, `Anims`, `Terrains`, `Worlds`, `Assets`, and `WBData` indicate likely owning references.

Do not copy the full official tables into this router reference. Use the owning reference for full table-heavy workflows.

## Procedures And Ordered Steps

Workbench/resource orientation:

1. If Resource Manager first launch cannot find game data, use Add Existing to point it at the Arma Reforger game project.
2. Treat the base Arma Reforger project as read-only viewing of game data/scripts.
3. Create or open a working addon/project before changing data.
4. Register the `enfusion://` protocol in Workbench Options when Workbench links are needed.
5. Use Resource Browser context actions for override, duplicate, inherit, navigation, GUID copy, and related data operations.
6. Verify resource metadata and GUID consequences before replacing or manually editing resource identity.

Data-modification orientation:

1. For a small targeted change, first consider override/modify.
2. For reusable variation, consider inherit.
3. For independent copied data, consider duplicate.
4. For replacing all references to a resource identity, use replacement only when intended and reviewed.
5. For existing scripts, prefer `modded`, `override`, and `super` patterns when the goal is script extension.
6. For same-path script replacement, understand load-order and replacement consequences before recommending it.

## Warnings And Failure Modes

- Do not guess Reforger APIs. Always query exact game data before writing API-sensitive code.
- Do not assume Unity, Unreal, C#, or Arma 3 patterns apply.
- Do not treat a code change as the default solution when a prefab/config/resource/editor workflow is the right surface.
- Do not use examples as signature truth; examples show shape, current generated API data gives exact signatures.
- Do not edit or recommend manual GUID changes casually.
- Duplicate GUIDs across addons can overwrite each other; duplicate GUIDs within one addon can make one resource fail.
- Resource replacement can affect every place that refers to that GUID.
- Scripts and metadata-backed resources are modified differently.
- Same-path script replacement is load-order sensitive.
- Base game data opened through Resource Manager is for viewing; work should happen in the addon/project.
- Workbench links require registered `enfusion://` protocol and are human/editor conveniences, not runtime API proof.
- Keep local work local. Do not introduce managers, services, registries, wrappers, broad validation, or extra settings unless required by the user request or demonstrated defect.

## API Lookup Keys

Use these common anchors to enter the exact API lookup layer:

- Resource/data: `ResourceName`, `Resource`, `BaseContainer`, `EntityCatalog`.
- Entity/component: `IEntity`, `GenericEntity`, `GenericComponent`, `ScriptComponent`, `ScriptComponentClass`.
- Replication: `BaseRplComponent`, `RplComponent`, `RplProp`, `RplRpc`.
- Workbench: `WorkbenchPlugin`, `WorkbenchPluginAttribute`.
- User actions: `ScriptedUserAction`, `BaseUserAction`, `CanBeShownScript`, `PerformAction`.
- UI: `Widget`, `SCR_HUDMenuComponent`, `layout`.
- Audio: `Sound`, `SoundComponent`, `sound event`.
- Animation: `Animation`, `Anim`, `AnimGraph`, `AnimationEditor`.
- Vehicles: `Vehicle`, `Compartment`, `WheeledSimulation`.
- AI: `AI`, `Behavior`, `Navmesh`.

Refine these keys in the owning reference before broad searching.

## Game-Data Query Commands

Use query commands for exact API details and examples:

```powershell
py -3 scripts\query-reforger-data.py lookup "make a user action"
py -3 scripts\query-reforger-data.py lookup "make a replicated component"
py -3 scripts\query-reforger-data.py lookup "spawn prefab"
py -3 scripts\query-reforger-data.py lookup "load resource"
py -3 scripts\query-reforger-data.py lookup "workbench plugin"
py -3 scripts\query-reforger-data.py symbol ResourceName --exact
py -3 scripts\query-reforger-data.py symbol ScriptComponent --kind class --exact
py -3 scripts\query-reforger-data.py attribute RplProp --exact
py -3 scripts\query-reforger-data.py method IEntity FindComponent --exact
py -3 scripts\query-reforger-data.py examples replication --subtopic rpc
py -3 scripts\query-reforger-data.py files WorkbenchPlugin
```

Use `--exact` when verifying a known API name. Use `lookup "<task>"` when the user request is a common task and Codex needs a compact API/example bundle. Use `examples` for implementation patterns, then verify signatures separately with `symbol`, `method`, or `attribute`.

## Examples And Samples

Official samples are routing signals for likely layouts and examples:

- General/reference mod layout: `SampleMod_Main`, `SampleMod_Replacement`.
- Script patterns: `SampleMod_ModdedScript`.
- Workbench plugin: `SampleMod_WorkbenchPlugin`.
- Weapons: `SampleMod_NewWeapon`, `SampleMod_ModdedWeapon`.
- Vehicles: `SampleMod_NewCar`, `SampleMod_ModdedCar`.
- Character/faction: `SampleMod_NewCharacter`, `SampleMod_NewFaction`.
- Props/assets: `SampleMod_NewProp`.
- Animation/cinematics: `SampleMod_AnimationWorkshop`, `SampleMod_CinematicTutorial`.

Do not use samples as runtime source truth by themselves. Use them to find layout and pattern candidates, then verify exact APIs with game-data query output.

## Follow-Up Keywords

Use these keywords to choose the next reference or query:

- `addon`, `gproj`, `Workshop`, `publishing`, `project setup`
- `Resource Manager`, `Workbench`, `Script Editor`, `World Editor`
- `override`, `inherit`, `duplicate`, `replace`, `transfer`, `GUID`, `.meta`
- `prefab`, `config`, `BaseContainer`, `ResourceName`, `EntityCatalog`
- `script`, `modded`, `override`, `super`, `ScriptComponent`
- `replication`, `authority`, `proxy`, `owner`, `RplProp`, `RplRpc`
- `server config`, `startup parameters`, `dedicated`
- `terrain`, `world`, `navmesh`
- `weapon`, `vehicle`, `inventory`, `gear`
- `animation`, `audio`, `UI`, `AI`, `Scenario Framework`, `Game Master`

## Verification

For any final answer or code change, state which of these remain:

- API verification: exact symbols/methods/attributes checked with `scripts\query-reforger-data.py`.
- Reference verification: owning runtime reference read in full.
- Workbench verification: Resource Manager, Script Editor, World Editor, Audio Editor, Animation Editor, or other editor workflow still needs manual validation.
- Runtime verification: game launch, scenario run, UI/menu behavior, audio/animation playback, or in-game behavior still needs testing.
- Multiplayer verification: authority/proxy/owner, JIP, replication, RPC, dedicated-server behavior.
- Packaging verification: addon project, `.gproj`, Workshop publishing, dependency, server config, or startup parameters.
- Asset verification: import settings, `.meta`/GUID, resource links, LOD/collision/materials/textures.

If a required verification cannot be performed in Codex, say so explicitly.

## Official Wiki Links

- Arma Reforger category: https://community.bistudio.com/wiki/Category:Arma_Reforger
- Modding category: https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding
- Getting Started: https://community.bistudio.com/wiki/Arma_Reforger:Getting_Started
- Data Modding Basics: https://community.bistudio.com/wiki/Arma_Reforger:Data_Modding_Basics
- Directory Structure: https://community.bistudio.com/wiki/Arma_Reforger:Directory_Structure
- Game Identity: https://community.bistudio.com/wiki/Arma_Reforger:Game_Identity
- Dictionary: https://community.bistudio.com/wiki/Arma_Reforger:Dictionary
- Workbench Metadata: https://community.bistudio.com/wiki/Arma_Reforger:Workbench_Metadata
- Workbench Links: https://community.bistudio.com/wiki/Arma_Reforger:Workbench_Links
- Resource Manager Getting Started Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Getting_Started_Tutorial

## Usefulness Score

Score: `94/100`

- Wiki coverage: `28/30`
  - All owned primary pages were reviewed and represented.
  - Core sections, tables, procedures, warnings, and official URLs are represented.
  - Full tables are not copied because this router intentionally preserves orientation rules and routes detailed table-heavy work to owning references.
- Operational detail: `14/15`
  - Preserves concrete Workbench/resource/data surfaces, override/inherit/duplicate/replace distinctions, GUID/meta warnings, and routing behavior.
- API lookup usefulness: `15/15`
  - API-sensitive guidance routes to exact `scripts\query-reforger-data.py` commands.
- Example grounding: `9/10`
  - Official sample families are mapped as routing signals. No source snippets are included because this orientation file does not need implementation bodies.
- Codex task usefulness: `14/15`
  - Gives a task classifier, routing table, action loop, and verification loop for common Reforger tasks.
- Context efficiency: `10/10`
  - Dense router reference; no broad API dump, raw wiki dump, raw HTML, or copied source body.
- Verification guidance: `4/5`
  - Includes clear residual verification categories; detailed validation steps live in owning references.

Category fit:
- Source family complete: pass.
- No owned page missing: pass.
- Split boundary justified: pass.
- Cross-links present: pass.
- Task route clear: pass.

Missed coverage review:
- No unreviewed owned primary wiki page.
- No missing primary orientation section.
- No omitted correctness warning from reviewed orientation pages.
- No automatic failure condition applies.
