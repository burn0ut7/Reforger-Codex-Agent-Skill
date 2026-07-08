# Game Master, Factions, Tasks, And Modes

## When To Read

Read this reference when a task involves Game Master operation, in-game editor content registration, faction creation, task system setup, general game-mode setup, Conflict, Capture & Hold, notifications, hints, editable entity properties, toolbar/context actions, tooltips, or preview/image generation for in-game editor assets.

Use this as the primary owner for:

- Game Master controls, interface, toolbar, scenario menu, entity browser, placement, budgets, and waypoints;
- Game Master tutorial operations such as placing assets, moving assets, changing status, healing, resupplying, fire/lightning/bleeding/refuel operations, duplication, neutralisation, removal, and group operations;
- registering placeable prefabs, editable entities, editable properties, entity tooltips, context actions, toolbar actions, and compositions;
- creating factions, faction configs, character/group/vehicle variants, faction editor integration, Conflict-specific faction data, and spawn point registration;
- Task System setup, task executors, assignment, ownership/visibility, group tasks, progression, nesting, Workbench/runtime behavior, and debug menu use;
- General Game Mode Setup for free-for-all and faction-based modes;
- Conflict concepts and Capture & Hold setup/repair/testing;
- notification and hint config/script workflows.

Do not use this reference as the owner for Scenario Framework internals, generic entity/component lifecycle, asset import, weapon creation, vehicle simulation, UI layout implementation, server hosting, or Workbench plugin authoring. Route those tasks to their domain references and return here only for Game Master, faction, task, or game-mode integration.

## Source Inventory

Wiki ownership:

- Primary wiki topics/categories: Game Master, Game Master tutorials, Faction Creation, Task System Usage, General Game Mode Setup, Conflict, Capture & Hold Setup, Notification Creation, Hint Usage, editable entity/property/action/tooltip workflows.
- Secondary/cross-reference topics: Scenario Framework, asset import, character gear/inventory, weapons, vehicles, UI layouts, server runtime, Workbench plugin authoring, Resource Manager/config/prefab workflows.

Wiki pages reviewed:

- Game Master - https://community.bistudio.com/wiki/Arma_Reforger:Game_Master - status: covered - reason: primary source for Game Master description, controls, interface, scenario menu, playable factions, entity browser, placement, budgets, gamepad menu, and waypoints.
- Game Master Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Game_Master_Tutorial - status: covered - reason: primary source for operating Game Master, placing assets, changing statuses, asset operations, and group operations.
- Game Master: Composition Configuration Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Game_Master:_Composition_Configuration_Tutorial - status: covered - reason: primary source for composition prefab creation, editable variants, registration, and in-game editor testing.
- Game Master: Editable Entities Configuration - https://community.bistudio.com/wiki/Arma_Reforger:Game_Master:_Editable_Entities_Configuration - status: covered - reason: primary source for creating placeable prefabs, registry config, edit mode registration, and entity registration.
- Game Master: Context Action Creation - https://community.bistudio.com/wiki/Arma_Reforger:Game_Master:_Context_Action_Creation - status: covered - reason: primary source for context action script/config/UI info workflow.
- Game Master: Toolbar Action Creation - https://community.bistudio.com/wiki/Arma_Reforger:Game_Master:_Toolbar_Action_Creation - status: covered - reason: primary source for toolbar action script/config/UI info workflow.
- Game Master: Entity Property Creation - https://community.bistudio.com/wiki/Arma_Reforger:Game_Master:_Entity_Property_Creation - status: covered - reason: primary source for editor property scripts, layouts, config, UI info, slider/dropdown/selection/dynamic description fields, variables, and classes.
- Game Master: Entity Tooltip Creation - https://community.bistudio.com/wiki/Arma_Reforger:Game_Master:_Entity_Tooltip_Creation - status: covered - reason: primary source for tooltip script/config workflow.
- Game Master: Image Generation Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Game_Master:_Image_Generation_Tutorial - status: covered - reason: primary source for generating editor preview images, custom preview worlds, positions, cameras, and tests.
- Faction Creation - https://community.bistudio.com/wiki/Arma_Reforger:Faction_Creation - status: covered - reason: primary dense source for faction file structure, characters, vehicles, groups, faction configs, editor registration, spawn points, Conflict integration, and testing.
- Task System Usage - https://community.bistudio.com/wiki/Arma_Reforger:Task_System_Usage - status: covered - reason: primary source for task setup, debug menu, extended tasks, task API/control flow, executors, assignment, ownership, visibility, progression, nesting, Workbench, and runtime behavior.
- General Game Mode Setup - https://community.bistudio.com/wiki/Arma_Reforger:General_Game_Mode_Setup - status: covered - reason: primary source for free-for-all/faction-based game-mode examples, requirements, instances, game state, game-mode end, and troubleshooting.
- Conflict - https://community.bistudio.com/wiki/Arma_Reforger:Conflict - status: covered - reason: primary source for Conflict gameplay concepts and design surfaces.
- Capture & Hold Setup - https://community.bistudio.com/wiki/Arma_Reforger:Capture_&_Hold_Setup - status: covered - reason: primary source for Capture & Hold scenario creation, tests, header, publishing, settings, common issues, and repair notes.
- Notification Creation - https://community.bistudio.com/wiki/Arma_Reforger:Notification_Creation - status: covered - reason: primary source for notification enum/config/info/color/editor position/send/localisation workflow.
- Hint Usage - https://community.bistudio.com/wiki/Arma_Reforger:Hint_Usage - status: covered - reason: primary source for hint config/script/sequence workflow and hint fields.
- Modding/Game Master category pages - official category URLs - status: partial - reason: used as source inventory/routing evidence only; content-heavy tutorials are covered individually above.

Wiki sections covered:

- Game Master: Description; Controls; Interface; Mode; Toolbar; Map; Flashlight; Toggle Interface; Guided Tour; Clear Destroyed Entities; Scenario Menu; playable factions; game/time/weather; Entity Browser; filters; budgets; entity placement; gamepad-specific menu; waypoints.
- Game Master Tutorial: Start Game Master; Place Assets; Place an Asset; Place a Player Unit; Select/Move Assets; Change Status; Heal; Resupply; Set On Fire; Extinguish; Cast Lightning; Start Bleeding; Refuel; Edit Advanced Settings; Duplicate; Neutralise; Remove; Group Operations.
- Game Master composition/editable tutorials: composition prefab creation, flexible/static naming, configuring and editing composition, technical rules, editable variant creation, registry config, testing in in-game editor, placeable prefab creation, maintaining existing prefabs, custom prefab directory choice, registration.
- Game Master action/property/tooltip tutorials: script creation, config modding, UI info, additional variables, base classes, methods, layout selection, layout creation, layout scripting, slider/dropdown/selection/multiselection/dynamic description, add-to-config workflow.
- Faction Creation: goals, file structure, character configuration, retextures, character variants, radio protocol, identity, faction, outfit, storage items, weapons/magazines, vehicle variants, groups, faction config, faction identity, in-game editor integration, labels, Editable Entity Core, register characters/groups/vehicles, generator config, editable prefab adjustments, Faction Manager, spawn points, previews, Conflict integration, loadouts, in-game testing.
- Task System Usage: setup, World Editor, Game UI, debug menu, tasks and extended tasks, API/control flow, executor, assignment, ownership/visibility, group tasks, progression, state-progress behavior, nesting, Workbench/runtime behavior.
- General Game Mode Setup: examples, basic setup, free-for-all, faction-based, requirements, instances, game state, game-mode end, troubleshooting.
- Conflict: seizing, respawn, supplies, construction interface, service depots, vehicle maintenance, fuel, ammunition, field hospital, radio relay, living quarters, mobile command unit, ranks.
- Capture & Hold Setup: creation steps, initial setup, scenario setup, system test, scenario header, in-game test, publishing, score/time endings, scoring multipliers, kill feed, unconsciousness, spawn/no-go/death zones, garbage manager note, common issues, repair notes.
- Notification Creation and Hint Usage: enum/config/script/send workflows, info fields, UI/editor placement, localisation, hint sequence.

Structured wiki records:

- Tables reviewed/included: Faction Creation character component table, faction config table, editable entity table, group localised strings, Conflict faction/vehicle config tables, Game Master controls/entity placement/gamepad/waypoint tables, action/property/tooltip UI/config tables, General Game Mode setup tables, Hint fields, Notification info fields, Task System tables.
- Procedures reviewed/included: Capture & Hold creation/score/time/repair workflows, Faction Creation vehicle/editor/faction-manager/spawn/conflict/loadout procedures, Game Master tutorial placement procedure, composition flexible/static/config/register/test procedures, editable entity maintain/register procedure, property layout creation procedure, image generation procedures, hint sequence workflow, task executor/assignment/nesting procedures.
- Admonitions reviewed/included: Capture & Hold scenario/header/publish/private-test/garbage/repair warnings, Conflict concept requirements, Faction Creation recommendations and material override warnings, respawn localised string requirement, editable label and registry warnings, Workbench restart/save notes, Game Master role/budget/waypoint caveats, composition technical rules, editable prefab directory/auto-generation warnings, context action shortcut-only note, property/layout cautions, image generation camera/position warnings, General Game Mode requirements, Notification and Hint warnings, Task System state/progression/runtime warnings.
- Code blocks reviewed/included: action/property/tooltip/notification/hint/task pages contain API-sensitive script routes; exact code is not copied and must be queried before implementation.
- Media reviewed: Game Master interface/tutorial images, faction setup images, Capture & Hold setup images, composition/editable entity/property/image generation screenshots; used as UI evidence, not copied.

Game-data/API evidence:

- Queries run:
  - `py -3 scripts\query-reforger-data.py files GameMaster --limit 8`
  - `py -3 scripts\query-reforger-data.py files EditableEntity --limit 8`
  - `py -3 scripts\query-reforger-data.py files SCR_TaskSystem --limit 8`
  - `py -3 scripts\query-reforger-data.py files SCR_Faction --limit 8`
  - `py -3 scripts\query-reforger-data.py files GameMode --limit 8`
  - `py -3 scripts\query-reforger-data.py examples game-mode --limit 8`
  - `py -3 scripts\query-reforger-data.py files Notification --limit 8`
  - `py -3 scripts\query-reforger-data.py files Hint --limit 8`
- Symbols/methods/attributes verified: `SCR_TaskSystem`, `SCR_TaskSystemNetworkComponent`, `SCR_TaskSystemSerializer`, `SCR_CampaignFaction`, `SCR_FreeForAllFaction`, `SCR_FactionAffiliationComponent`, `SCR_GMMenuConfiguration`, `SCR_VoteGameMasterCondition`, `NotificationsSystem`, `NotificationInfo`, `SCR_CampaignHintEntry`, `SCR_CampaignHintStorage`, `SCR_CampaignFeedbackComponent`, `SCR_EGameModeState`, `SCR_GameModeCombatOpsManager`, `GamemodeStorage`.
- Examples/snippets reviewed: game-mode examples are noisy and should be treated as route suggestions; exact routes should prefer targeted task/faction/editable/notification/hint file searches.

Samples and source examples:

- Official sample folders reviewed as layout signals: `SampleMod_NewFaction`, `SampleMod_Main`.
- Game-source example families reviewed: task system, faction, game mode, editable entity/editor, notification, hint, Game Master menu, and campaign feedback routes.

Coverage gaps:

- Scenario Framework internals are intentionally excluded and owned by `scenario-framework.md`.
- Generic component lifecycle, event masks, and prefab component wiring are intentionally excluded and owned by `entities-components-and-lifecycle.md`.
- Asset import, weapon creation, vehicle simulation, character gear details, UI layout implementation, server hosting, and Workbench plugin authoring are intentionally excluded and owned by their domain references.
- Game Master category pages are included only as routing/category evidence because their concrete pages are covered individually.

## Wiki Source Coverage

Game Master coverage:

- Game Master is a mode and in-game editor surface for live scenario control, asset placement, waypointing, and scenario state manipulation.
- The Game Master interface includes mode, toolbar, map, flashlight, interface toggle, guided tour, clear-destroyed-entities control, scenario menu, entity browser, and gamepad-specific menu surfaces.
- Scenario menu coverage includes move, seize, defend, custom flows, playable factions, game settings, time/date, and weather controls.
- Entity Browser coverage includes controls, filters, budgets, entity placement, and the consequence that budget limits can prevent additional AI placement.
- Waypoints include move, forced move, relaxed move, search and destroy, defend, get in, get out, and suppressive fire.
- Game Master Tutorial covers starting Game Master, placing assets and player units, selecting and moving assets, changing status, healing, resupplying, fire/extinguish/lightning/bleeding/refuel operations, advanced settings, duplication, neutralisation, removal, and group operations.

Game Master editable content coverage:

- Composition configuration covers creating flexible/static composition prefabs, naming rules, composition configuration, editing, prefab editing, technical rules, tips, editable variant creation, selection, registration, and in-game editor testing.
- Editable Entities Configuration covers using existing prefabs, preparing and selecting source prefabs, creating and maintaining editable variants, choosing correct directories for custom prefabs, creating registry config, adding registry to edit mode, and registering entities.
- Editable entity custom prefabs must use the documented editable prefab path family and must not be created inside the auto-generated folder.
- Entity Property Creation covers script creation, base classes, methods, layout selection and creation, layout scripting, config modding, UI info, additional property types, sliders, dropdown/spinboxes, selection buttons, multiselection buttons, dynamic descriptions, variables, and classes.
- Entity Tooltip Creation covers script creation, config modding, and adding tooltip config.
- Context Action Creation covers script creation, config modding, UI info, and variables, including shortcut-only context actions when UI info is omitted but shortcut and shortcut logic are set.
- Toolbar Action Creation covers script creation, methods, config modding, add-to-config, UI info, and other variables.
- Image Generation Tutorial covers generating preview images, loading a world, adjusting screen resolution, selecting prefabs, playing the preview workflow, configuring custom worlds, creating managers, positions, cameras, testing positions, and repeating for coverage.

Faction Creation coverage:

- The faction tutorial covers character configuration, unit group preparation, faction creation, Game Master integration, and Conflict integration.
- New factions require an elaborate file structure; keep faction work organized before editing configs.
- Character setup includes retexturing existing equipment, prefabs versus material overrides, creating base character prefabs, configuring character components, radio protocol, identity, faction affiliation, outfit, storage items, variants, weapons, and magazines.
- Material overrides are less reliable than prefab-based retextures; prefer prefab routes when the wiki recommends them.
- Vehicle variants can be created by inherited variants and faction affiliation changes; faction-specific vehicle prefabs matter for AI and game-mode behavior.
- Groups should inherit from the documented base group prefab so required components are already present.
- Faction config creation should duplicate or inherit from existing faction configs.
- Respawn depends on a localised string in the faction Name field; missing it can produce no-spawn-point style failures.
- In-game editor integration requires adding labels, adding labels to Editable Entity Core, registering characters/groups/vehicles, adjusting generator configs, saving changes, and sometimes restarting Workbench.
- Conflict integration requires additional faction configs, vehicle lists, player and AI character prefabs, groups, new Conflict world setup, Faction Manager adjustment, game-mode tweaking, loadouts, and in-game testing.

Task System coverage:

- Task System setup includes World Editor, game UI, and debug menu surfaces.
- The debug menu route is Systems > Task System.
- Tasks and extended tasks support complex missions, task nesting, progression monitoring, ownership/visibility behavior, group tasks, assignment, and runtime behavior.
- Task executor workflows include creating a task executor, assigning tasks, unassigning tasks, and passing the correct task reference and executor.
- Group task assignment can use group ownership or executor ownership with group ID fields.
- Progression has state-progress behavior; manually setting completed state and progress updates has specific caveats.
- Nesting can be configured in Workbench, affects runtime behavior, and has assignment/ownership/progression implications.

General Game Mode Setup coverage:

- General setup distinguishes free-for-all and faction-based examples.
- Requirements, instances, game state, and game-mode end behavior must be configured before treating a game-mode issue as script failure.
- Troubleshooting belongs with this reference when it affects game-mode setup rather than server runtime or Scenario Framework internals.

Conflict coverage:

- Conflict is about two groups of players fighting for strategic positions.
- Seizing requires enemy positions to be within faction radio range.
- Respawn routes include Main Operating Base and fully operational Mobile Command Units.
- Supplies are stored at bases and support construction, transport, and base development.
- Construction interface uses supply materials for defenses and support structures.
- Service depots include vehicle maintenance, fuel, ammunition, field hospital, radio relay, living quarters, and Mobile Command Unit support.
- Ranks are earned through objectives and support actions.

Capture & Hold coverage:

- Capture & Hold setup starts from Reforger Tools/project creation and Workbench/World Editor setup.
- Initial setup uses existing Capture & Hold base worlds and sub-world workflow.
- Scenario setup requires placing the required elements.
- System test requires disabling play-from-camera-position and verifying the scenario.
- Scenario Header config is required so the scenario can launch in-game.
- In-game test validates scenario selection and launch from the game.
- Publishing should wait until multiplayer testing confirms spawn points and gameplay details; use private/test visibility until verified.
- Additional settings include score ending, time ending, score multipliers, kill feed, unconsciousness, spawn/no-go/death zones, and garbage manager notes.
- Common issues include World Editor initialization failures, garbage collector crashes, and repair steps after major game updates.

Notifications and hints coverage:

- Notification Creation covers enum declaration, config modding, adding a notification, setting a key, filling info class, notification colour, editor set position data, sending notification, creating a new notification class, and localisation.
- Hint Usage covers config creation, name, description, icon, icon set name, description blocks, type, show limit, priority, duration, highlighted widget names, timer visibility, field manual link, script creation, config modification, script modification, hint sequence creation, and showing the sequence.
- API-sensitive notification/hint implementation must query exact classes and current signatures before scripting.

## Terms And Concepts

- Game Master: live/in-game editor mode for scenario control, asset placement, waypoints, and operations.
- Entity Browser: Game Master browser for placeable entities with filters, budgets, and placement controls.
- Budget: placement limit category, especially important for AI.
- Playable Faction: faction configured for player selection and Game Master scenario menu behavior.
- Editable Entity: prefab/entity registered so the in-game editor can place or edit it.
- Editable Entity Core: config surface where labels and editable entity metadata are integrated.
- Placeable Entities Registry: config used to register editable placeable entities.
- Context Action: in-game editor action available from entity context.
- Toolbar Action: in-game editor action exposed through toolbar UI.
- Entity Property: editable property exposed for editor manipulation.
- Entity Tooltip: in-game editor tooltip information for an entity.
- Composition: reusable configured collection/prefab for in-game editor placement.
- Task System: framework for tasks, task ownership, visibility, assignment, progression, and nesting.
- Task Executor: runtime target/owner used when assigning or unassigning tasks.
- Extended Task: task type with nesting and advanced progression behavior.
- Faction Config: faction data config for identity, editor, respawn, game-mode, and Conflict integration.
- Conflict: strategic faction game mode with bases, radio range, supplies, construction, respawn, and ranks.
- Capture & Hold: game mode workflow built around capture areas, scenario header, testing, publishing, and repair steps.
- Notification: configured/sent UI notification.
- Hint: configured instructional UI guidance, optionally sequenced.

## Workbench / Resource / Data Surfaces

Editor and runtime surfaces:

- Game Master mode.
- Game Master toolbar.
- Game Master map.
- Scenario menu.
- Entity Browser.
- Gamepad-specific menu.
- Waypoint menu.
- Systems > Task System debug menu.
- World Editor.
- Resource Browser.
- In-game editor.
- Register Placeable Entities plugin.
- preview/image generation world.
- Conflict world/scenario setup.
- Capture & Hold base world/sub-world setup.

Config/resource surfaces:

- faction configs;
- faction identity configs;
- callsign configs;
- loadout configs;
- character, group, vehicle, and spawn point prefabs;
- editable entity labels;
- Editable Entity Core config;
- editable prefabs configuration;
- placeable entity registry configs;
- Game Master context action configs;
- Game Master toolbar action configs;
- editable property configs;
- tooltip configs;
- composition prefabs and editable variants;
- scenario header configs;
- notification configs;
- hint configs and hint sequence lists;
- task configs and task prefab/data resources.

Script/source surfaces:

- `SCR_TaskSystem`
- `SCR_TaskSystemNetworkComponent`
- `SCR_TaskSystemSerializer`
- `SCR_CampaignFaction`
- `SCR_FreeForAllFaction`
- `SCR_FactionAffiliationComponent`
- `SCR_GMMenuConfiguration`
- `SCR_VoteGameMasterCondition`
- `NotificationsSystem`
- `NotificationInfo`
- `SCR_CampaignHintEntry`
- `SCR_CampaignHintStorage`
- `SCR_CampaignFeedbackComponent`
- `SCR_EGameModeState`

Cross-reference surfaces:

- Scenario Framework internals belong to `scenario-framework.md`.
- Generic component lifecycle belongs to `entities-components-and-lifecycle.md`.
- Prefab/config mechanics belong to `prefabs-configs-containers-and-catalogs.md`.
- Character gear/inventory, weapons, vehicles, UI layouts, server runtime, Workbench plugin authoring, and asset import belong to their domain references.

## Required Workflows

Game Master operation workflow:

1. Start Game Master in the intended scenario.
2. Use the interface and toolbar to choose the operation type.
3. Use Scenario Menu for global scenario operations, playable factions, game state, time/date, and weather.
4. Use Entity Browser filters before placing content.
5. Check budgets before placing AI-heavy content.
6. Place, select, move, duplicate, neutralise, remove, or group assets through documented operations.
7. Use waypoints for AI behavior and validate the waypoint type in play.
8. Treat Game Master runtime behavior as evidence; route authoring defects to editable entity, faction, task, or domain references.

Editable entity registration workflow:

1. Decide whether the source is an existing prefab or custom prefab.
2. Prepare the editable variant.
3. For custom prefabs, choose the correct editable prefab directory and avoid auto-generated folders.
4. Create or update the registry config.
5. Add the registry to edit mode.
6. Register entities.
7. Test in the in-game editor.
8. Generate previews if the workflow requires visible browser content.

Faction creation workflow:

1. Establish faction folder/file structure.
2. Create or inherit character base prefabs.
3. Configure radio protocol, identity, faction, outfit, storage items, weapons, and magazines.
4. Create vehicle variants and group prefabs as needed.
5. Create faction config by duplicating or inheriting from an existing config.
6. Fill faction identity and localised name fields.
7. Add labels for in-game editor integration.
8. Add labels to Editable Entity Core.
9. Register characters, groups, vehicles, and spawn points.
10. Generate editor previews.
11. Add faction to Faction Manager.
12. Add Conflict-specific configs/prefabs/groups/loadouts when needed.
13. Test in Workbench and in game.

Task System workflow:

1. Set up task system surfaces in World Editor and Game UI.
2. Use Systems > Task System debug menu to inspect task runtime state.
3. Choose normal task or extended task.
4. Create task executors deliberately.
5. Assign or unassign tasks through current API lookup.
6. Configure ownership and visibility.
7. Configure group task assignment if needed.
8. Configure progression and state behavior.
9. Configure nesting in Workbench when tasks need parent/child relationships.
10. Validate assignment, ownership, visibility, and progression at runtime.

General game-mode workflow:

1. Choose free-for-all or faction-based pattern.
2. Confirm requirements and required instances.
3. Configure game state.
4. Configure game-mode end behavior.
5. Troubleshoot setup before editing unrelated scripts.
6. Validate mode start, player flow, win/end condition, and runtime state.

Capture & Hold workflow:

1. Create the project in Reforger Tools.
2. Open Workbench and World Editor.
3. Open an existing Capture & Hold base world.
4. Create a sub-world and place required elements.
5. Run system test with play-from-camera-position disabled.
6. Create scenario header config.
7. Run in-game scenario test.
8. Test multiplayer spawn points and gameplay details.
9. Publish only after validation, using private or test visibility until ready.
10. Configure score/time ending, multipliers, kill feed, unconsciousness, zones, and related settings as needed.
11. Apply repair notes after affected game updates.

Notification and hint workflow:

1. Create enum/config entries.
2. Fill key and info class.
3. Set color, icon, priority, duration, and editor position data as applicable.
4. Add localisation.
5. Query exact classes and send/show APIs before scripting.
6. Test in runtime UI.
7. For hint sequences, create the sequence list and trigger the sequence through exact API lookup.

## Configuration Fields And Tables

Game Master fields:

- mode;
- toolbar;
- map;
- flashlight;
- toggle interface;
- guided tour;
- clear destroyed entities;
- playable factions;
- game settings;
- time and date;
- weather;
- entity browser filters;
- entity budgets;
- entity placement controls;
- waypoints.

Faction Creation fields:

- character radio protocol;
- character identity;
- character faction;
- character outfit;
- character storage items;
- character weapon slots;
- magazines/loadout;
- vehicle faction affiliation;
- group base prefab inheritance;
- faction config;
- faction identity;
- callsign info;
- localised faction name;
- editable entity labels;
- Editable Entity Core labels array;
- placeable entity registry config;
- authored labels;
- military symbols;
- Faction Manager playable factions;
- spawn point prefab and registration;
- Conflict faction config;
- Conflict vehicle list;
- Conflict player and AI character prefabs;
- Conflict loadouts.

Task System fields:

- task ownership;
- task visibility;
- executor;
- executor group ID;
- owner group array;
- owner executor array;
- progression;
- state-progress behavior;
- parent task;
- child tasks;
- Workbench nesting fields;
- runtime assignment state.

Capture & Hold fields:

- base world;
- required scenario elements;
- Scenario Header;
- score limit;
- end game duration;
- scoring multipliers;
- kill feed settings;
- unconsciousness toggle;
- spawn areas;
- no-go zones;
- death zones;
- garbage manager note.

Editable entity and Game Master extension fields:

- editable prefab source;
- editable prefab directory;
- registry config;
- edit mode registry entry;
- UI info;
- shortcut;
- enable shortcut logics;
- property layout;
- slider/dropdown/selection/multiselection settings;
- tooltip config;
- composition naming fields;
- preview world position/camera/labels/time/weather.

Notification fields:

- enum key;
- notification key;
- info class;
- colour;
- editor set position data;
- localisation.

Hint fields:

- name;
- description;
- icon;
- icon set name;
- description blocks;
- type;
- show limit;
- priority;
- duration;
- highlighted widget names;
- timer visibility;
- field manual link;
- sequence list.

## Procedures And Ordered Steps

Before changing Game Master/editor content:

1. Identify whether the task is runtime operation, editable registration, faction data, task system, game mode, notification, or hint.
2. Read this reference and only cross-link to domain references for asset/component/UI/server details.
3. Query exact API/source routes before scripting.
4. Keep prefab/config changes local to the content being registered.
5. Validate in Workbench and in the in-game editor.

Before adding a new faction:

1. Set up faction file structure.
2. Create base character prefab and variants.
3. Configure character components, loadouts, weapons, magazines, radio, identity, and faction affiliation.
4. Create vehicle and group variants.
5. Create faction config and identity.
6. Add editor labels and Editable Entity Core registration.
7. Register characters, groups, vehicles, and spawn points.
8. Generate previews.
9. Add faction to Faction Manager.
10. Add Conflict-specific data only if Conflict support is required.
11. Test in editor, in game, and Conflict if applicable.

Before adding editable Game Master content:

1. Create or select the source prefab.
2. Create editable variant.
3. Create registry config.
4. Add registry to edit mode.
5. Register entities.
6. Generate preview images if required.
7. Test placement from Entity Browser.
8. Check budget, filters, labels, tooltip, and editable properties.

Before adding a task:

1. Choose task or extended task.
2. Configure ownership and visibility.
3. Create required executor.
4. Assign task through exact API lookup or config workflow.
5. Configure progression and nesting when needed.
6. Test assignment, visibility, progression, completion/failure/cancel behavior, and runtime UI.
7. Inspect Systems > Task System debug menu.

Before creating a Capture & Hold scenario:

1. Create project.
2. Open the Capture & Hold base world.
3. Create sub-world.
4. Place required elements.
5. Run system test.
6. Create Scenario Header.
7. Run in-game test.
8. Test multiplayer.
9. Publish with private/test visibility until verified.

Before adding a notification or hint:

1. Create enum/config entry.
2. Fill UI/info fields.
3. Add localisation.
4. Query exact send/show API.
5. Trigger it in runtime.
6. Confirm display, priority, duration, icon, and sequence behavior.

## Warnings And Failure Modes

- Do not treat Game Master placement as proof that a prefab is correctly registered for all editor/game-mode contexts.
- Do not exceed budgets and then debug AI placement as if the prefab failed.
- Do not skip editable entity registry config; unregistered entities will not appear correctly.
- Do not create custom editable prefabs in auto-generated folders; they can be removed by generation.
- Do not assume material override retextures are as reliable as prefab-based retextures; the faction tutorial warns about override fragility.
- Do not omit a localised faction Name field; respawn can fail with no-spawn-point style errors.
- Do not add editor labels without adding matching Editable Entity Core entries.
- Do not forget to save generator/config changes; some changes may need Workbench restart.
- Do not copy Conflict faction data without configuring required Conflict-specific prefabs, groups, vehicles, loadouts, and world settings.
- Do not use GameMode, Faction, or Task broad search results as exact API proof; these queries are noisy.
- Do not assume task progress updates automatically when manually forcing completed state; the Task System wiki documents state-progress caveats.
- Do not publish Capture & Hold publicly before multiplayer testing.
- Do not ignore Capture & Hold repair notes after major game updates.
- Do not use notifications or hints without localisation and runtime UI verification.
- Do not route Scenario Framework hierarchy/component defects here; use `scenario-framework.md`.
- Do not solve asset, weapon, vehicle, UI layout, server, or Workbench plugin defects inside this reference unless the task is specifically editor/game-mode registration.

## API Lookup Keys

Game Master/editor:

- `GameMaster`
- `SCR_GMMenuConfiguration`
- `SCR_VoteGameMasterCondition`
- `EditableEntity`
- `EditablePrefabsConfig`
- `EntityCatalog`
- `SCR_BaseEntityCatalogData`

Tasks:

- `SCR_TaskSystem`
- `SCR_TaskSystemNetworkComponent`
- `SCR_TaskSystemSerializer`
- `SCR_ExtendedTask`
- `SCR_TaskSave`
- `SCR_ExtendedTaskSave`
- `SCR_CampaignMilitaryTaskSave`

Factions and game modes:

- `SCR_Faction`
- `SCR_CampaignFaction`
- `SCR_FreeForAllFaction`
- `SCR_FactionAffiliationComponent`
- `SCR_EGameModeState`
- `SCR_GameModeCombatOpsManager`
- `BaseGameMode`
- `SCR_BaseGameMode`

Notifications and hints:

- `NotificationsSystem`
- `NotificationInfo`
- `NotificationTestGeneratorEntity`
- `SCR_CampaignFeedbackComponent`
- `SCR_CampaignHintEntry`
- `SCR_CampaignHintStorage`
- `SCR_VoteHintCondition`

Follow-up terms:

- Game Master.
- Editable Entity.
- Editable Entity Core.
- Placeable Entities Registry.
- Faction Manager.
- Task System.
- Task Executor.
- Extended Task.
- Conflict.
- Capture & Hold.
- Scenario Header.
- Notification.
- Hint.
- Entity Property.
- Entity Tooltip.
- Context Action.
- Toolbar Action.
- Composition.

## Game-Data Query Commands

Use targeted file searches first:

```powershell
py -3 scripts\query-reforger-data.py files GameMaster --limit 8
py -3 scripts\query-reforger-data.py files EditableEntity --limit 8
py -3 scripts\query-reforger-data.py files SCR_TaskSystem --limit 8
py -3 scripts\query-reforger-data.py files SCR_Faction --limit 8
py -3 scripts\query-reforger-data.py files Notification --limit 8
py -3 scripts\query-reforger-data.py files Hint --limit 8
```

Use broad routes only as secondary discovery because they can be noisy:

```powershell
py -3 scripts\query-reforger-data.py files GameMode --limit 8
py -3 scripts\query-reforger-data.py examples game-mode --limit 8
```

Use bounded snippets after choosing exact files:

```powershell
py -3 scripts\query-reforger-data.py snippet scripts/Game/Tasks/SCR_TaskSystem.c --line 1 --context 40
py -3 scripts\query-reforger-data.py snippet scripts/Game/Tasks/SCR_TaskSystemNetworkComponent.c --line 1 --context 40
py -3 scripts\query-reforger-data.py snippet scripts/Game/Faction/SCR_CampaignFaction.c --line 1 --context 40
py -3 scripts\query-reforger-data.py snippet scripts/Game/Faction/SCR_FreeForAllFaction.c --line 1 --context 30
py -3 scripts\query-reforger-data.py snippet scripts/Game/Systems/NotificationsSystem.c --line 1 --context 40
py -3 scripts\query-reforger-data.py snippet scripts/Game/Campaign/SCR_CampaignHintStorage.c --line 1 --context 40
py -3 scripts\query-reforger-data.py snippet scripts/Game/UI/Menu/SCR_GMMenuConfiguration.c --line 1 --context 30
```

Use JSON for scripted review only:

```powershell
py -3 scripts\query-reforger-data.py files SCR_TaskSystem --limit 8 --json
```

## Examples And Samples

Best game-source routes:

- `scripts/Game/Tasks/SCR_TaskSystem.c`: task system source route.
- `scripts/Game/Tasks/SCR_TaskSystemNetworkComponent.c`: task networking/source route.
- `scripts/Game/Plugins/Persistence/System/Serializers/States/SCR_TaskSystemSerializer.c`: task persistence route.
- `scripts/Game/Faction/SCR_CampaignFaction.c`: campaign faction route.
- `scripts/Game/Faction/SCR_FreeForAllFaction.c`: free-for-all faction route.
- `scripts/Game/Components/SCR_FactionAffiliationComponent.c`: faction affiliation component route.
- `scripts/Game/UI/Menu/SCR_GMMenuConfiguration.c`: Game Master menu configuration route.
- `scripts/Game/Systems/NotificationsSystem.c`: notification system route.
- `scripts/Game/Campaign/SCR_CampaignFeedbackComponent.c`: campaign feedback/notification/hint-adjacent route.
- `scripts/Game/Campaign/SCR_CampaignHintStorage.c`: campaign hint storage route.

Official sample status:

- `SampleMod_NewFaction` is the main sample layout signal for faction work.
- `SampleMod_Main` is a general layout signal for mod structure and editor-visible content.
- Use samples to confirm layout patterns only. Wiki workflows and current game-data query results remain authority.

How to use examples:

1. Start with the wiki workflow for the specific area.
2. Use targeted query commands for exact source routes.
3. Open only bounded snippets from exact files.
4. Make the smallest config/script/prefab change needed.
5. Validate in Workbench, in-game editor, runtime UI, and multiplayer when applicable.

## Follow-Up Keywords

- Game Master
- Entity Browser
- playable factions
- budgets
- waypoints
- editable entity
- editable prefab
- Placeable Entities Registry
- Editable Entity Core
- context action
- toolbar action
- entity property
- entity tooltip
- composition prefab
- preview image generation
- faction creation
- faction config
- faction identity
- Faction Manager
- editable entity labels
- Conflict integration
- Capture & Hold
- Scenario Header
- Task System
- extended task
- task executor
- ownership and visibility
- group task
- task progression
- task nesting
- notification creation
- hint sequence

## Verification

Minimum Game Master verification:

- Open Game Master in the target scenario.
- Confirm Entity Browser labels, filters, budgets, and placement.
- Place the edited entity and test operations or waypoints.
- Confirm Game Master UI/actions/tooltips/properties appear where expected.

Minimum faction verification:

- Confirm faction config and localised name.
- Confirm characters, groups, vehicles, and spawn points are registered.
- Confirm faction appears in in-game editor and Faction Manager.
- Confirm editor previews if required.
- Confirm Conflict-specific data only when Conflict support is intended.
- Test in game, not only in Resource Browser.

Minimum task verification:

- Run the task flow.
- Inspect Systems > Task System debug menu.
- Confirm executor, assignment, ownership, visibility, progression, and nesting.
- Confirm runtime UI state and completion/failure/cancel behavior.

Minimum game-mode verification:

- Validate game state and end condition.
- Test free-for-all or faction-based flow with expected player/faction setup.
- For Capture & Hold, test system start, scenario header, in-game launch, spawn points, scoring/time ending, and multiplayer behavior.
- For Conflict, validate radio range, respawn, supplies, construction, service depots, Mobile Command Unit, and ranks in the intended scenario.

Minimum notification/hint verification:

- Trigger the notification or hint in runtime.
- Confirm localisation, icon, priority, duration, colour, position, highlighted widgets, sequence order, and timer behavior.

Residual verification note:

- Wiki and query output identify source-backed workflows and API routes. They do not prove the final mode/faction/editor content works in a packaged mod, hosted server, multiplayer session, or all player roles. State remaining Workbench/runtime/multiplayer/server uncertainty after changes.

## Official Wiki Links

- Game Master: https://community.bistudio.com/wiki/Arma_Reforger:Game_Master
- Game Master Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Game_Master_Tutorial
- Game Master: Composition Configuration Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Game_Master:_Composition_Configuration_Tutorial
- Game Master: Editable Entities Configuration: https://community.bistudio.com/wiki/Arma_Reforger:Game_Master:_Editable_Entities_Configuration
- Game Master: Context Action Creation: https://community.bistudio.com/wiki/Arma_Reforger:Game_Master:_Context_Action_Creation
- Game Master: Toolbar Action Creation: https://community.bistudio.com/wiki/Arma_Reforger:Game_Master:_Toolbar_Action_Creation
- Game Master: Entity Property Creation: https://community.bistudio.com/wiki/Arma_Reforger:Game_Master:_Entity_Property_Creation
- Game Master: Entity Tooltip Creation: https://community.bistudio.com/wiki/Arma_Reforger:Game_Master:_Entity_Tooltip_Creation
- Game Master: Image Generation Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Game_Master:_Image_Generation_Tutorial
- Faction Creation: https://community.bistudio.com/wiki/Arma_Reforger:Faction_Creation
- Task System Usage: https://community.bistudio.com/wiki/Arma_Reforger:Task_System_Usage
- General Game Mode Setup: https://community.bistudio.com/wiki/Arma_Reforger:General_Game_Mode_Setup
- Conflict: https://community.bistudio.com/wiki/Arma_Reforger:Conflict
- Capture & Hold Setup: https://community.bistudio.com/wiki/Arma_Reforger:Capture_&_Hold_Setup
- Notification Creation: https://community.bistudio.com/wiki/Arma_Reforger:Notification_Creation
- Hint Usage: https://community.bistudio.com/wiki/Arma_Reforger:Hint_Usage

## Usefulness Score

Score: 93/100

Scoring breakdown:

- Wiki coverage: 29/30. All owned primary pages are represented, including dense Faction Creation, Game Master workflows, editable entity/action/property pages, Task System Usage, General Game Mode Setup, Conflict, Capture & Hold, notifications, and hints. Category pages are explicitly handled as routing evidence.
- Operational detail: 15/15. The reference includes concrete editor, registration, faction, task, game-mode, Capture & Hold, notification, and hint workflows with field groups and ordered steps.
- API lookup usefulness: 14/15. Query commands cover targeted Game Master, editable entity, task system, faction, game mode, notification, hint, examples, and snippets. Broad search noise is documented.
- Example grounding: 8/10. Official sample signals and game-source routes are included, with `SampleMod_NewFaction` as the main faction layout signal. Some Game Master-specific samples are not dedicated standalone samples, so game-source routes carry more of the example grounding.
- Codex task usefulness: 15/15. Codex can route likely tasks to one primary reference, preserve source boundaries, query exact APIs, and validate editor/game-mode behavior.
- Context efficiency: 7/10. The owned source family is broad and dense; this reference compresses many wiki pages into a navigable operating guide while preserving required details and routing domain authoring elsewhere.
- Verification guidance: 5/5. Workbench, in-game editor, runtime UI, game-mode, multiplayer, faction, task, and residual validation are explicit.

Missed coverage and cap review:

- No owned primary wiki page is omitted.
- Game Master category pages are included as routing/source inventory evidence; their content-heavy pages are covered individually.
- Faction Creation is preserved as a dense workflow family rather than a shallow summary.
- Task System ownership includes setup, executor, ownership/visibility, progression, nesting, Workbench, runtime, and debug menu details.
- Scenario Framework, component lifecycle, assets, weapons, vehicles, UI layout implementation, server hosting, and Workbench plugin authoring are intentionally cross-linked to owning references.
- No automatic failure applies: official wiki links are present, query commands are present, examples/sample rationale is present, split boundaries are explicit, and no broad API dump is embedded.
