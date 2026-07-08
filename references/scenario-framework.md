# Scenario Framework

## When To Read

Read this reference when a task involves building, wiring, debugging, updating, or validating Scenario Framework content.

Use this as the primary owner for:

- Scenario Framework world setup;
- Scenario Framework hierarchy design;
- GameMode manager settings for Scenario Framework;
- areas, layers, layer tasks, slots, logic, plugins, actions, getters, and conditions;
- task chains built from Scenario Framework entities;
- dynamic spawn/despawn in Scenario Framework;
- Scenario Framework debug menu, inspectors, debug actions, and log messages;
- Scenario Framework setup tutorial workflows;
- Scenario Framework update plugin usage.

Do not use this as the owner for generic Game Master authoring, faction creation, Conflict, Capture and Hold, generic entity/component lifecycle, terrain creation, World Editor tools, Workbench plugin authoring, replication, or server hosting. Route those tasks to their owning references after using this file for Scenario Framework-specific behavior.

## Source Inventory

Wiki ownership:

- Primary wiki topics/categories: Scenario Framework, Scenario Framework Setup Tutorial, Scenario Framework Update Plugin.
- Secondary/cross-reference topics: Game Mode Setup plugin, World Editor setup, Game Master/game mode/task systems, entity/component lifecycle, prefabs/configs/resources, Workbench debugging, terrain/world setup, multiplayer/server validation.

Wiki pages reviewed:

- Scenario Framework - https://community.bistudio.com/wiki/Arma_Reforger:Scenario_Framework - status: covered - reason: primary source for framework purpose, prerequisites, GameMode manager settings, hierarchy, components, shared attributes, activation, tasks, slots, plugins, logic, getters, actions, debug menu, samples, structural changes, and logs.
- Scenario Framework Setup Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Scenario_Framework_Setup_Tutorial - status: covered - reason: primary ordered workflow for creating a small Scenario Framework scenario from a world setup through spawn, move task, random destroy task, and game over.
- Scenario Framework Update Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Scenario_Framework_Update_Plugin - status: covered - reason: primary source for update plugin usage and migration warning for older Scenario Framework worlds.

Wiki sections covered:

- Scenario Framework: Prerequisites; Basics; GameMode Manager Settings; Tasks; Debug; Dynamic Spawn/Despawn; Basic Hierarchy Components; Area; Layer; LayerTask; Slot; Logic; Example; Tutorial; Debug Menu; Tasks; Registered Areas; Debug Areas; Layer Inspector; Action Inspector; Logic Inspector; Plugin Inspector; Condition Inspector; Debug Actions; Log Messages; Components; Shared Attributes; Children; Asset; Debug; Activation; Activation Type; Activation Conditions; Activation Condition Logic; OnActivation; Plugins; Area; Layer; LayerTask task variants; Slot variants; Logic variants; Plugins; Conditions; Getters; Actions; Nested Subtasks; QRF System; Faction Aliases; Samples; Compositions; 1.1.0 Structural Changes.
- Scenario Framework Setup Tutorial: World Setup; Scenario Framework Setup; Spawn Area Creation; Add a Move Task; Add a Random Destroy Task; Add a Game Over.
- Scenario Framework Update Plugin: Page context and Usage.

Structured wiki records:

- Tables reviewed/included: Scenario Framework page table of contents record, used as coverage check rather than copied as a runtime table.
- Procedures reviewed/included: setup tutorial workflow, spawn area workflow, move task workflow, random destroy task workflow, update plugin workflow, LayerTaskDefend parameter sequence, Trigger plugin count setup, Change Task Icon, End Mission, Set Signal, Set Grenade Live, Spawn Objects Based On Distance, Wait And Execute, QRF System configuration, Faction Aliases configuration.
- Admonitions reviewed/included: setup tutorial requirement to keep the main documentation available, Game Mode Setup skip/create-entities notes, update plugin backup/reload/warning notes, `GameModeSF.et` recommendation, required supporting prefabs, `SCR_GameModeSFManager` importance, hierarchy notes, slot spawn note, log warning/error severity, activation condition caveats, defend trigger requirement, defender/attacker layer constraints, slot asset requirements, dynamic spawn/despawn range guidance, delete/kill/remove-item irreversible action warnings, QRF naming/snap guidance, sample caveats, structural change warnings.
- Code blocks reviewed/included: no primary code blocks were required for this reference; API-sensitive implementation routes are delegated to query commands and bounded snippets.
- Media reviewed: setup tutorial images, Scenario Framework hierarchy/debug images, inspector screenshots, component screenshots, and sample media; used as UI/workflow evidence, not copied.

Game-data/API evidence:

- Queries run:
  - `py -3 scripts\query-reforger-data.py files ScenarioFramework --limit 8`
  - `py -3 scripts\query-reforger-data.py files SCR_ScenarioFramework --limit 8`
  - `py -3 scripts\query-reforger-data.py examples scenario-framework --limit 8`
  - `py -3 scripts\query-reforger-data.py files SCR_ScenarioFrameworkSystem --limit 8`
  - `py -3 scripts\query-reforger-data.py files SCR_ScenarioFrameworkLayer --limit 8`
  - `py -3 scripts\query-reforger-data.py files SCR_ScenarioFrameworkTask --limit 8`
- Symbols/methods/attributes verified: `SCR_ScenarioFrameworkSystem`, `SCR_ScenarioFrameworkSystemSerializer`, `SCR_ScenarioFrameworkArea`, `SCR_ScenarioFrameworkDebug`, `SCR_ScenarioFrameworkLayerBase`, `SCR_ScenarioFrameworkLayerTask`, `SCR_ScenarioFrameworkLayerTaskDefend`, `SCR_ScenarioFrameworkTask`, `SCR_ScenarioFrameworkTaskArea`, `SCR_ScenarioFrameworkTaskData`, `SCR_TaskDefend`, `SCR_TaskDeliver`.
- Examples/snippets reviewed: Scenario Framework system, area, layer base, layer task, task, debug, persistence serializer, action getter, tutorial stage, and mission header routes.

Samples and source examples:

- Official sample folders reviewed as layout signals: `SampleMod_Main`, `SampleMod_NewFaction`.
- Game-source example families reviewed: Scenario Framework component files, task files, action getters, debug system, persistence serializers, tutorial game-mode stages, and `SCR_MissionHeaderScenarioFramework`-derived routes.

Coverage gaps:

- Game Master, faction creation, Conflict, Capture and Hold, notifications, hints, editable entities, and generic game-mode setup are intentionally deferred to `game-master-factions-tasks-and-modes.md`.
- Generic entity/component lifecycle rules are intentionally deferred to `entities-components-and-lifecycle.md`; this reference owns Scenario Framework component meaning and workflow.
- Terrain setup and World Editor tools are intentionally deferred to terrain/world-editor references; this reference only covers World Editor use needed by Scenario Framework setup.
- Workbench plugin authoring is intentionally deferred to `workbench-plugins-and-editor-tools.md`; the update plugin is covered only as a Scenario Framework workflow.
- Replication and server hosting are intentionally deferred to their dedicated references; Scenario Framework scenarios still require runtime/server validation when used in multiplayer or hosted contexts.

## Wiki Source Coverage

Scenario Framework purpose:

- Scenario Framework is a World Editor-driven system for building scenarios without requiring scripting for every behavior.
- The expected author already knows basic World Editor operation.
- Most work is done by placing framework entities, arranging hierarchy, and editing attributes.
- Scripting knowledge helps when extending the framework, but normal scenario assembly should start from the documented component/action/condition workflow.

Prerequisites:

- Use the Game Mode Setup plugin to prepare a functional world for Scenario Framework.
- The Scenario Framework template route is `ScenarioFramework.conf`.
- `GameModeSF.et` is the recommended prefab for Scenario Framework scenarios.
- If not using `GameModeSF.et`, the wiki lists required supporting prefabs for optimal scenario functionality, including AI world, faction/loadout/radio/communication managers, weather, time, and related game mode support surfaces.
- Treat missing prerequisite entities as setup defects before debugging task logic.

GameMode manager settings:

- The core scenario entity is the GameMode entity.
- `GameModeSF.et` contains many components already and is the recommended starting point.
- The key component is `SCR_GameModeSFManager`; it exposes Scenario Framework properties and should be reviewed before assuming task, debug, or spawn behavior is broken.
- Task-related manager settings include available task types, maximum spawned tasks, and actions after tasks initialize.
- Debug settings allow targeted debugging of areas and layer tasks in complex or randomized scenarios.
- Dynamic Spawn/Despawn manager settings control whether dynamic despawn is enabled and how frequently it checks for spawn/despawn.

Hierarchy:

- Area is the top framework unit. Use areas to divide the scenario into functional regions.
- Layer sits under an Area and organizes child layers or slots. Layers can be basic hierarchy nodes or specialized task layers.
- LayerTask creates and drives task workflows. Different LayerTask types expect matching slot types.
- Slot is the lowest normal hierarchy element. Basic slots can spawn prefabs or carry components without spawning a prefab.
- Logic entities receive inputs and activate actions for more complex workflows.
- The normal authoring model is Area -> Layer or LayerTask -> Slot or Logic, with actions, conditions, plugins, and getters wired through attributes.

Debug menu and logs:

- Scenario Framework provides a dedicated debug menu suite.
- The debug menu can inspect tasks, registered areas, debug areas, layers, actions, logic, plugins, conditions, and debug actions.
- The Task debug view shows active tasks and their parent Area, LayerTask, and SlotTask relationships.
- Registered Areas lets you inspect valid areas and open layer inspectors.
- Debug Areas can add or inspect named debug area entries, optionally tied to LayerTask and SlotTask names.
- Layer, Action, Logic, Plugin, and Condition inspectors show the relevant runtime information for named entities or components.
- Debug Actions are predefined actions that can be selected and run from the debug menu.
- Scenario Framework log messages always include the Scenario Framework term.
- Informational log messages may not require action, but warnings identify improper usage and errors identify more serious failures.

Shared component attributes:

- Children controls child layer spawning. Spawn modes include all children, one random child, one selected random child family, or repeated spawn patterns depending on component type.
- Asset handles faction and prefab/resource relationships. Faction keys must correspond to configured faction data, and object/prefab attributes must point to valid resources.
- Debug handles runtime and Workbench debug shapes, including sphere/range visualizations for layers, triggers, or dynamic spawn/despawn.
- Activation handles activation type, activation conditions, condition logic, and dynamic spawn/despawn exclusion.
- OnActivation executes actions after a layer is fully spawned and activated.
- Plugins attach Scenario Framework plugins in listed order.

Activation:

- Activation Type controls when a layer activates and spawns.
- `SAME_AS_PARENT` follows the parent activation.
- `ON_TRIGGER_ACTIVATION` activates from a trigger or action using trigger activation.
- `ON_AREA_TRIGGER_ACTIVATION` activates when the parent area trigger activates.
- `ON_INIT` activates immediately after layer creation, which can still be after its parent is created.
- Activation Conditions are evaluated in inserted order.
- Activation Condition Logic supports boolean combinations such as AND, OR, NOT, and XOR.
- Exclude From Dynamic Despawn keeps a layer and its children out of dynamic despawn even when the surrounding system despawns other content.

Task and slot families:

- Generic LayerTask can be controlled by actions when specialized logic is not enough.
- LayerTaskMove expects SlotMoveTo.
- LayerTaskDestroy expects SlotDestroy.
- LayerTaskKill expects SlotKill.
- LayerTaskDefend expects SlotDefend.
- LayerTaskClearArea expects SlotClearArea.
- LayerTaskDeliver expects SlotPick and SlotDelivery for full behavior.
- SlotDefend can spawn a trigger, spawn a defend target entity, or combine an entity and external trigger.
- Task UI settings include icon set/name, progress bar, progress calculation, and task state changed actions.
- Subtask settings let a task become a subtask and route under a parent task.
- Nested subtasks can be managed by parent and child tasks, with parent task completion rules controlling how many subtasks must finish.

LayerTaskDefend:

- Defend tasks require a trigger if defending an area or an entity plus area.
- Defend parameters include countdown title text, defend time, countdown HUD, defender and attacker faction settings, and percentage/ratio checks.
- Attacker layer names must identify layers that contain only AI units/groups and nothing else.
- Defender/attacker calculations must be validated in the scenario, not assumed from attribute names.

Plugins, conditions, getters, and actions:

- Trigger plugin supports class/prefab filtering and count-based checks.
- Activation countdown timers reset when trigger conditions become false.
- Conditions are used for activation and action gating; some conditions are versioned and some source notes identify mistakes or caveats in class names.
- Getters return Scenario Framework entities, closest players, entity counts in triggers, named entities, layer entities, prefab-spawned children, tasks, and similar runtime targets.
- Actions perform scenario behavior such as changing task state, changing task icon, ending mission, changing activation type, spawning objects, waiting and executing, setting signals, deleting or killing entities, removing inventory items, and running debug actions.
- Destructive actions such as delete entity, kill entity, or remove item from inventory are dangerous because the effect cannot be reversed.

Dynamic spawn/despawn:

- Dynamic Spawn/Despawn works on Areas and manages their hierarchy to keep only needed content spawned.
- The wiki describes a continuous check, defaulting to a four-second cadence in the documented manager route.
- Dynamic despawn ranges are based on nearby observer/player cameras depending on the setting.
- Exclusions prevent specific layers from being despawned with their parent area.
- Dynamic spawn/despawn should be validated with debug shapes and runtime observation because incorrect range or activation settings can make content appear missing.

Setup tutorial:

- Start by opening the intended world in World Editor.
- Create a new world as a sub-scene of the current world, then choose where to save it.
- Open Plugins > Game Mode Setup.
- Select `ScenarioFramework.conf` in the Template field.
- Skip World Scan for a clean copy when appropriate.
- Use Create entities on World Configuration to generate required entities.
- Save after setup before building tasks.
- Create a Start layer, make it active, add a Scenario Framework Area, add a Slot, and set slot/player spawn attributes.
- Add a Move task by creating a task layer, adding an Area, adding the relevant move task hierarchy, setting task attributes, and linking completion flow.
- Add a Random Destroy task by creating a second task layer, using a destroy task, setting spawn children to random one, using trigger activation, adding child layers/slots, and wiring activation from previous task completion.
- Add game over by adding an EndMission action to `OnTaskFinished`, enabling override, and selecting the intended game-over type.

Update plugin:

- The update plugin exists because the 1.1.0 update changed how AIs and waypoints are handled by Scenario Framework.
- Older scenarios may not be backward compatible without running the update workflow.
- The source instructs backing up work first.
- Load the Scenario Framework world to update.
- Run the Scenario Framework update plugin from the documented plugin route.
- Save, unload, and load the world again as instructed.
- Running the plugin on an already compatible scenario is not recommended; behavior is undocumented.

Samples and compositions:

- The Scenario Framework page includes many samples and compositions.
- TaskMove is recommended as a simple learning task.
- TaskKill requires the target entity to be killed.
- TaskDeliverIntel requires a specific item and cannot interchange arbitrary same-prefab items in that documented case.
- DynamicDespawn samples use shorter check timing for samples, but the wiki recommends a slower rate for real scenarios to save performance.
- DeliverWeaponsToCrate and DeliverWeaponsInVehicle show action-driven and trigger/filter-driven delivery patterns.
- Composition examples are intended to be adjusted and reused, but still require validation in the target scenario.

## Terms And Concepts

- Scenario Framework: World Editor scenario-building system based on hierarchy, attributes, actions, conditions, plugins, and tasks.
- GameMode entity: core entity for a Scenario Framework scenario.
- `GameModeSF.et`: recommended Scenario Framework game mode prefab.
- `SCR_GameModeSFManager`: key manager component for Scenario Framework behavior.
- Area: top-level scenario region.
- Layer: hierarchy organizer under an Area.
- LayerTask: layer specialized for task creation and task workflow.
- Slot: lower-level spawn or component holder.
- Logic: entity that receives inputs and activates actions.
- Action: operation executed by activation, task events, logic, debug action, or other framework flow.
- Condition: check used to decide activation or action flow.
- Getter: helper that resolves entities, tasks, layers, players, counts, or named framework objects.
- Plugin: framework extension attached to layer/slot behavior through attributes.
- Dynamic Spawn/Despawn: system that spawns/despawns Area hierarchy based on distance and settings.
- Debug Area: named debug scope used by Scenario Framework debug menu.
- Layer Inspector: debug view for a specific layer.
- Action Inspector: debug view for layer actions.
- Condition Inspector: debug view for activation/action conditions.
- SlotDefend: slot type used with defend tasks.
- LayerTaskMove, LayerTaskDestroy, LayerTaskKill, LayerTaskDefend, LayerTaskClearArea, LayerTaskDeliver: specialized layer task families.
- QRF: quick reaction force system documented as Scenario Framework configuration.
- Faction Alias: mapping support for faction references in Scenario Framework.

## Workbench / Resource / Data Surfaces

Workbench and editor surfaces:

- World Editor.
- File > Load World.
- File > New World.
- Sub-scene world creation.
- Hierarchy panel.
- Active layer selection.
- Object Properties panel.
- Plugins > Game Mode Setup.
- Scenario Framework update plugin.
- Scenario Framework debug menu.
- Debug inspectors for tasks, areas, layers, actions, logic, plugins, and conditions.

Resource and prefab surfaces:

- `ScenarioFramework.conf`.
- `GameModeSF.et`.
- Scenario Framework component prefabs under the engine's Scenario Framework component resource family.
- Area prefabs.
- Layer and LayerTask prefabs.
- Slot and SlotTask prefabs.
- Trigger resources.
- Task prefab resources.
- Faction keys.
- Object-to-spawn prefab names.
- Layout resources for task UI/countdown HUD where used.

Script/source surfaces:

- `SCR_ScenarioFrameworkSystem`
- `SCR_ScenarioFrameworkArea`
- `SCR_ScenarioFrameworkLayerBase`
- `SCR_ScenarioFrameworkLayerTask`
- `SCR_ScenarioFrameworkTask`
- `SCR_ScenarioFrameworkDebug`
- `SCR_ScenarioFrameworkSystemSerializer`
- `SCR_ScenarioFrameworkGet`
- `SCR_ScenarioFrameworkActivationConditionBase`
- `SCR_EScenarioFrameworkComparisonOperator`

Cross-reference surfaces:

- Generic component lifecycle belongs to `entities-components-and-lifecycle.md`.
- Prefab/config/resource modeling belongs to `prefabs-configs-containers-and-catalogs.md`.
- World Editor terrain and tool operation belongs to terrain/world-editor references.
- Workbench plugin authoring belongs to `workbench-plugins-and-editor-tools.md`.
- Game Master/factions/tasks outside Scenario Framework belong to `game-master-factions-tasks-and-modes.md`.

## Required Workflows

Scenario Framework setup workflow:

1. Open the base world in World Editor.
2. Create a new sub-scene world for the scenario.
3. Open Plugins > Game Mode Setup.
4. Select `ScenarioFramework.conf` as the template.
5. Decide whether World Scan is needed; for a clean copy, the tutorial skips it.
6. Use Create entities on World Configuration to generate required entities.
7. Save before adding task content.
8. Confirm the GameMode entity uses Scenario Framework setup, preferably `GameModeSF.et`.
9. Inspect `SCR_GameModeSFManager` before changing task/debug/dynamic spawn behavior.

Basic hierarchy workflow:

1. Create an Area for the scenario region.
2. Add Layer or LayerTask children under the Area.
3. Add Slots or Logic under the layer/task.
4. Configure shared attributes first: children, asset, debug, activation, on-activation actions, and plugins.
5. Configure task-specific attributes next.
6. Wire actions, getters, conditions, and plugins only after the hierarchy names are stable.
7. Use debug menu and log messages to verify registration and activation.

Task chain workflow:

1. Start with TaskMove or another simple documented task.
2. Use a dedicated layer for each task stage.
3. Use matching LayerTask and Slot types.
4. Set activation type according to the expected flow.
5. Use task state changed actions to spawn or activate the next stage.
6. Use `OnTaskFinished` or related task event action slots for completion flow.
7. Add EndMission only after the final task condition is proven.

Randomized destroy workflow:

1. Create a new task layer.
2. Place an Area for the destroy task.
3. Use a LayerTaskDestroy hierarchy.
4. Set Spawn Children to `RANDOM_ONE` when selecting one child from alternatives.
5. Set Activation Type to `ON_TRIGGER_ACTIVATION` if previous task completion should spawn it.
6. Add child layers/slots for candidate targets.
7. Wire previous task completion to the destroy task activation.
8. Validate with debug inspectors because randomized hierarchy can hide incorrect names or activation paths.

Dynamic spawn/despawn workflow:

1. Enable dynamic despawn only on areas that should stream their hierarchy.
2. Set update rate deliberately; avoid overly frequent checks unless there is a measured need.
3. Set range based on player/observer camera behavior in the target scenario.
4. Exclude layers that must remain spawned.
5. Turn on debug shapes or relevant debug inspectors.
6. Test movement into and out of range.
7. Confirm child layers and slots return to the expected state.

Debug workflow:

1. Open Scenario Framework debug menu.
2. Check Tasks for active task relationships.
3. Check Registered Areas before assuming an Area failed.
4. Use Debug Areas to inspect named areas/layers/tasks.
5. Use Layer Inspector for activation and child state.
6. Use Action, Logic, Plugin, and Condition inspectors for flow failures.
7. Trigger Debug Actions only when the action is safe for the current scenario state.
8. Check logs for Scenario Framework warnings and errors.

Update plugin workflow:

1. Back up the world before opening it for update.
2. Load the Scenario Framework world to be updated.
3. Run the Scenario Framework update plugin from the documented plugin route.
4. Save after update.
5. Unload and load the world again.
6. Re-test AI, waypoint, task, and spawn behavior.
7. Do not run the update plugin casually on already compatible worlds.

## Configuration Fields And Tables

GameMode manager fields:

- task types available;
- maximum number of spawned tasks;
- after-tasks-init actions;
- debug area/task selection;
- predefined debug actions;
- dynamic despawn enabled;
- dynamic spawn/despawn update rate.

Shared attribute groups:

- Children:
  - Spawn Children;
  - all/random/selected/repeated spawn behavior where supported.
- Asset:
  - Faction Key;
  - object/prefab resource references;
  - task-specific asset overrides.
- Debug:
  - debug shapes during runtime;
  - debug shapes in Workbench;
  - range or trigger visualizations.
- Activation:
  - Activation Type;
  - Activation Conditions;
  - Activation Condition Logic;
  - Exclude From Dynamic Despawn.
- OnActivation:
  - Activation Actions.
- Plugins:
  - ordered plugin list.

Activation Type values:

- `SAME_AS_PARENT`: follows parent activation.
- `ON_TRIGGER_ACTIVATION`: waits for trigger/action activation.
- `ON_AREA_TRIGGER_ACTIVATION`: waits for parent area trigger activation.
- `ON_INIT`: activates after creation/init.

Activation Condition Logic values:

- AND.
- OR.
- NOT.
- XOR.

LayerTask fields:

- Type Of Task.
- Task Ownership.
- Task Title.
- Task Description.
- Task Prefab.
- Override Object Display Name.
- Subtasks Description.
- Is Subtask.
- Parent Task Name.
- Task Icon Set.
- Task Icon Name.
- Progress Bar.
- Calculate Progress Bar On Completed Tasks.
- Trigger Actions On Finish.
- Actions On Created.
- Actions On Failed.
- Actions On Cancelled.

LayerTaskDefend fields:

- Trigger Name.
- Countdown Title Text.
- Defend Time.
- Display Countdown HUD.
- Countdown HUD.
- Faction Settings.
- Defender/attacker faction keys.
- Count Only Players.
- Min Defender Percentage Ratio.
- Attacker Layer Names.

Slot fields:

- Object To Spawn.
- Faction Key.
- Randomization labels.
- Included editable entity labels.
- excluded labels.
- repeated spawn settings where supported.
- SlotTask task links.
- SlotDefend target/trigger behavior.

Plugin and trigger fields:

- Specific Class Name Count.
- Specific Prefab Count.
- Activation Countdown Timer.
- trigger filters.
- prefab filters.
- class filters.

Action fields:

- End Mission: override game over type, overridden game over type.
- Change Task Icon: task icon set, task icon name.
- Set Signal: getter, signal, value.
- Set Grenade Live: getter, enable simulation.
- Spawn Objects: names of objects to spawn on activation.
- Spawn Objects Based On Distance: getter, min distance, max distance, list of objects.
- Wait And Execute: delay, max delay, looped state, actions.
- Delete/Kill/Remove Item: getter and target filters.

Debug and log fields:

- task list entries;
- parent Area, LayerTask, SlotTask names;
- layer name;
- logic entity name;
- debug action name;
- warning messages;
- error messages.

## Procedures And Ordered Steps

Before creating Scenario Framework content:

1. Confirm the world has been prepared with Game Mode Setup.
2. Confirm `ScenarioFramework.conf` was used or that equivalent required entities exist.
3. Confirm the GameMode entity is the Scenario Framework GameMode or has equivalent required components.
4. Confirm the scenario has a clear Area/Layer/Slot naming plan.
5. Confirm task flow before adding randomized or dynamic spawn behavior.

To create a spawn area:

1. Create an organizing layer in the world hierarchy.
2. Set it as active.
3. Add a Scenario Framework Area.
4. Add a Slot under the correct hierarchy.
5. Configure the slot's Scenario Framework slot component.
6. Set the needed spawn/player attributes.
7. Validate through World Editor hierarchy and runtime spawn behavior.

To add a move task:

1. Create and activate a task layer.
2. Add an Area in the target task location.
3. Use the move task layer/slot family.
4. Configure task title, description, ownership, prefab, and task UI as needed.
5. Wire completion behavior.
6. Test the task from scenario start and through any previous task chain.

To add a random destroy task:

1. Create and activate a second task layer.
2. Add an Area and LayerTaskDestroy hierarchy.
3. Set Spawn Children to `RANDOM_ONE`.
4. Set Activation Type to `ON_TRIGGER_ACTIVATION`.
5. Add child layers/slots for possible destroy targets.
6. Link previous task completion to this layer activation.
7. Validate that exactly the intended random child appears and the destroy task completes.

To add game over:

1. Add an EndMission action to the final task's `OnTaskFinished` action list.
2. Enable override when the final task should set the game-over type explicitly.
3. Set the intended game-over type.
4. Run the task chain to completion.
5. Confirm the mission ends with the expected state.

To update an older Scenario Framework world:

1. Back up the world.
2. Load the world.
3. Run the update plugin.
4. Save.
5. Unload and load the world again.
6. Re-test AI/waypoint behavior, tasks, dynamic spawn/despawn, debug menu, and logs.

## Warnings And Failure Modes

- Do not skip Game Mode Setup and then debug task components as if the framework is fully initialized.
- Do not ignore required supporting prefabs if not using `GameModeSF.et`.
- Do not treat Scenario Framework as generic Game Master authoring; it has its own hierarchy and component expectations.
- Do not mix up Area, Layer, LayerTask, Slot, and Logic responsibilities.
- Do not use a specialized LayerTask without the matching slot family.
- Do not rename entities after wiring getters/actions/conditions unless every name reference is updated.
- Do not assume randomized child spawning works until the debug menu confirms the active child.
- Do not enable dynamic despawn without range/debug validation.
- Do not use overly frequent dynamic spawn/despawn checks without a performance reason.
- Do not run the update plugin on compatible worlds as routine maintenance; the source warns behavior is undocumented.
- Do not skip the post-update reload step.
- Do not ignore Scenario Framework warnings and errors in logs.
- Do not use delete, kill, or remove-item actions casually; the source marks these actions as dangerous or irreversible.
- Do not assume `examples scenario-framework` query output is precise enough by itself; it can return incidental task/faction matches. Prefer file lookups for exact Scenario Framework source routes.
- Do not validate only in editor when the scenario is intended for runtime, hosted, or multiplayer use.

## API Lookup Keys

Core framework:

- `SCR_ScenarioFrameworkSystem`
- `SCR_ScenarioFrameworkDebug`
- `SCR_ScenarioFrameworkSystemSerializer`
- `SCR_EScenarioFrameworkComparisonOperator`

Components and hierarchy:

- `SCR_ScenarioFrameworkArea`
- `SCR_ScenarioFrameworkLayerBase`
- `SCR_ScenarioFrameworkLayerTask`
- `SCR_ScenarioFrameworkLayerTaskDefend`
- `SCR_ScenarioFrameworkSlotBase`
- `SCR_ScenarioFrameworkGet`

Tasks:

- `SCR_ScenarioFrameworkTask`
- `SCR_ScenarioFrameworkTaskArea`
- `SCR_ScenarioFrameworkTaskData`
- `SCR_TaskDefend`
- `SCR_TaskDeliver`
- `SCR_TaskDestroyObject`

Conditions/actions/plugins:

- `SCR_ScenarioFrameworkActivationConditionBase`
- `SCR_ScenarioFrameworkTaskStatusCondition`
- `SCR_ScenarioFrameworkGetArea`
- `SCR_ScenarioFrameworkGetArrayOfEntities`
- `SCR_ScenarioFrameworkGetArrayOfLayerBases`
- `ScenarioFrameworkActionCinematicTrack`

Follow-up lookup terms:

- ScenarioFramework.
- SCR_ScenarioFramework.
- Scenario Framework System.
- Scenario Framework Layer.
- Scenario Framework Task.
- Scenario Framework Debug.
- Scenario Framework Condition.
- Scenario Framework Action.
- Scenario Framework Getter.
- Scenario Framework Plugin.
- Dynamic Despawn.
- LayerTaskMove.
- LayerTaskDestroy.
- LayerTaskDefend.
- SlotDefend.
- QRF.
- Faction Alias.

## Game-Data Query Commands

Use file lookup as the primary Scenario Framework source route:

```powershell
py -3 scripts\query-reforger-data.py files ScenarioFramework --limit 8
py -3 scripts\query-reforger-data.py files SCR_ScenarioFramework --limit 8
py -3 scripts\query-reforger-data.py files SCR_ScenarioFrameworkSystem --limit 8
py -3 scripts\query-reforger-data.py files SCR_ScenarioFrameworkLayer --limit 8
py -3 scripts\query-reforger-data.py files SCR_ScenarioFrameworkTask --limit 8
```

Use examples as a secondary route because broad Scenario Framework example search can be noisy:

```powershell
py -3 scripts\query-reforger-data.py examples scenario-framework --limit 8
```

Use bounded snippets after choosing an exact file:

```powershell
py -3 scripts\query-reforger-data.py snippet scripts/Game/ScenarioFramework/SCR_ScenarioFrameworkSystem.c --line 1 --context 40
py -3 scripts\query-reforger-data.py snippet scripts/Game/ScenarioFramework/Components/SCR_ScenarioFrameworkArea.c --line 1 --context 40
py -3 scripts\query-reforger-data.py snippet scripts/Game/ScenarioFramework/Components/SCR_ScenarioFrameworkLayerBase.c --line 1 --context 40
py -3 scripts\query-reforger-data.py snippet scripts/Game/ScenarioFramework/Components/SCR_ScenarioFrameworkLayerTask.c --line 1 --context 40
py -3 scripts\query-reforger-data.py snippet scripts/Game/ScenarioFramework/Tasks/SCR_ScenarioFrameworkTask.c --line 1 --context 40
py -3 scripts\query-reforger-data.py snippet scripts/Game/ScenarioFramework/SCR_ScenarioFrameworkDebug.c --line 1 --context 40
```

Use JSON output only for scripted review or audit:

```powershell
py -3 scripts\query-reforger-data.py files SCR_ScenarioFramework --limit 8 --json
```

## Examples And Samples

Best game-source routes:

- `scripts/Game/ScenarioFramework/SCR_ScenarioFrameworkSystem.c`: central Scenario Framework system route.
- `scripts/Game/ScenarioFramework/Components/SCR_ScenarioFrameworkArea.c`: Area component route.
- `scripts/Game/ScenarioFramework/Components/SCR_ScenarioFrameworkLayerBase.c`: Layer base route.
- `scripts/Game/ScenarioFramework/Components/SCR_ScenarioFrameworkLayerTask.c`: LayerTask route.
- `scripts/Game/ScenarioFramework/Components/SCR_ScenarioFrameworkLayerTaskDefend.c`: Defend task route.
- `scripts/Game/ScenarioFramework/Tasks/SCR_ScenarioFrameworkTask.c`: task base route.
- `scripts/Game/ScenarioFramework/Tasks/SCR_ScenarioFrameworkTaskDeliver.c`: deliver task route.
- `scripts/Game/ScenarioFramework/SCR_ScenarioFrameworkDebug.c`: debug menu/system route.
- `scripts/Game/Plugins/Persistence/System/Serializers/States/SCR_ScenarioFrameworkSystemSerializer.c`: persistence/save-load route.
- `scripts/Game/Mission/SCR_MissionHeaderCombatOps.c`: mission header route derived from Scenario Framework mission header behavior.

Official sample status:

- `SampleMod_Main` is useful as a general project/layout signal, but wiki Scenario Framework workflows remain the authority.
- `SampleMod_NewFaction` is useful for faction-adjacent layout signals when Scenario Framework content references faction keys.
- No official sample should be copied into this reference as source body text.

How to use examples:

1. Start with the wiki workflow and decide whether the task is setup, hierarchy, task flow, debug, update, or extension.
2. Use file lookup for exact Scenario Framework source routes.
3. Use snippets only around the chosen exact file and line.
4. Verify exact APIs before writing script-side extensions.
5. Validate the scenario in Workbench and runtime after changes.

## Follow-Up Keywords

- Scenario Framework
- ScenarioFramework.conf
- GameModeSF.et
- Game Mode Setup
- SCR_GameModeSFManager
- Area
- Layer
- LayerTask
- Slot
- Logic
- SlotDefend
- LayerTaskMove
- LayerTaskDestroy
- LayerTaskKill
- LayerTaskDefend
- LayerTaskClearArea
- LayerTaskDeliver
- Activation Type
- Activation Conditions
- Activation Condition Logic
- OnActivation
- Spawn Children
- Dynamic Spawn/Despawn
- Debug Areas
- Layer Inspector
- Action Inspector
- Logic Inspector
- Plugin Inspector
- Condition Inspector
- Debug Actions
- Scenario Framework warnings
- QRF
- Faction Aliases
- EndMission
- Wait And Execute
- Spawn Objects
- Getters
- Trigger plugin

## Verification

Minimum setup verification:

- Confirm the world was created as the intended sub-scene or target world.
- Confirm Game Mode Setup used the Scenario Framework template or equivalent required setup.
- Confirm required entities were created.
- Confirm the GameMode entity and `SCR_GameModeSFManager` are present.
- Save and reload before diagnosing later behavior.

Minimum hierarchy verification:

- Confirm Area/Layer/LayerTask/Slot/Logic hierarchy names.
- Confirm specialized LayerTasks have matching slot types.
- Confirm all name references used by getters/actions/conditions still match entity names.
- Confirm activation type and activation condition logic.
- Confirm task UI and state changed actions.

Minimum runtime verification:

- Run the scenario from start.
- Check player spawn before task logic.
- Complete each task stage in order.
- Observe dynamic spawn/despawn in and out of range when used.
- Open Scenario Framework debug menu and inspect registered areas, tasks, layers, actions, plugins, and conditions.
- Check logs for Scenario Framework warnings and errors.

Minimum update verification:

- Back up before update.
- Run the update plugin only for worlds that need it.
- Save, unload, and reload after update.
- Re-test AI/waypoints, tasks, dynamic spawn/despawn, and debug menu behavior.

Residual verification note:

- Wiki and query output identify the correct Scenario Framework workflow and source routes. They do not prove a specific scenario works in runtime, hosted play, multiplayer, or dedicated server conditions. State remaining Workbench/runtime/server uncertainty after any Scenario Framework change.

## Official Wiki Links

- Scenario Framework: https://community.bistudio.com/wiki/Arma_Reforger:Scenario_Framework
- Scenario Framework Setup Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Scenario_Framework_Setup_Tutorial
- Scenario Framework Update Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Scenario_Framework_Update_Plugin

## Usefulness Score

Score: 94/100

Scoring breakdown:

- Wiki coverage: 29/30. All owned primary pages are represented, including the large Scenario Framework source, setup tutorial, and update plugin. The reference preserves hierarchy, setup, debug, task flow, attributes, procedures, warnings, and official links without copying the full page.
- Operational detail: 15/15. Workflows cover setup, hierarchy, task chains, random destroy task, dynamic spawn/despawn, debug, update, fields, and ordered steps.
- API lookup usefulness: 15/15. Query commands cover Scenario Framework files, `SCR_ScenarioFramework` files, system, layer, task, examples, and bounded snippets.
- Example grounding: 8/10. Game-source routes are strong and official samples are identified as layout signals. Broad `examples scenario-framework` output is explicitly treated as secondary because it can be noisy.
- Codex task usefulness: 15/15. Codex can use this reference to set up Scenario Framework content, route exact APIs, choose source examples, debug hierarchy/task flow, and validate changes without guessing.
- Context efficiency: 7/10. Scenario Framework is very large; this reference compresses it into a dense operating guide while preserving key concepts, fields, warnings, procedures, and lookup routes.
- Verification guidance: 5/5. Workbench setup, hierarchy, runtime, update, log, debug menu, and residual runtime/server checks are explicit.

Missed coverage and cap review:

- No owned primary wiki page is omitted.
- Scenario Framework main page sections are represented by workflow families instead of copied one-for-one.
- The setup tutorial ordered workflows and update plugin warning/reload flow are preserved.
- Game Master, factions, generic game modes, entity lifecycle, terrain/world editing, Workbench plugin authoring, replication, and server runtime are intentionally cross-linked to owning references.
- No automatic failure applies: official wiki links are present, query commands are present, examples and no-copy sample rationale are present, split boundaries are explicit, and no broad API dump is embedded.
