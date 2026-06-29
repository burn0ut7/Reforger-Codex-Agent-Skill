# Scenario Framework Game Master

## When to read this reference

Read for Scenario Framework, Game Master, editable/placeable prefabs, factions, tasks, waypoints, entity catalogs, game mode content, and scenario setup.

## Search terms

`Game Master`, `Scenario Framework`, `Editable Prefabs`, `PrefabsEditable`, `SCR_PlaceableEntitiesRegistry`, `EditorModeEdit`, `SCR_PlacingEditorComponent`, `Entity Browser`, `Faction`, `Task System`, `Waypoint`, `Conflict`, `Game Mode`, `E_`

## Source authority summary

Game Master docs define what the mode can do and what runtime/editor features it exposes. Editable Entities Configuration defines the Workbench pipeline for making prefabs placeable/editable. Faction/task/scenario docs define content setup. Samples show folder layouts for new factions, entity catalogs, and editable arsenal content.

## Game Master runtime behavior

Game Master is a real-time curator game mode equivalent in role to Arma 3 Zeus. It lets the curator create, edit, move, and kill AI units/vehicles, edit/move/kill players, provide groups with waypoints, create/move/delete prefabs on the fly, and spawn into the game.

It cannot modify base terrain.

Role rules:

- Server host or declared server admin always has access to Game Master interface.
- If no Game Master is present, the first player to connect obtains the role.
- The role cannot be transferred unless the player disconnects.

## Game Master scenario settings

Scenario menu supports:

- Playable faction setup. Removing a playable faction kills players assigned to it.
- Faction spawn points.
- Faction objectives for players; AI ignores objectives.
- Respawn settings: enable respawn, spawn near radio operators, respawn time.
- Server-wide ambient music.
- Time of day quick selections and 15-minute slider.
- Date fields, default documented as 8 August 1989.
- Time progression and multiplier range.
- Weather automation, weather type, wind automation, wind speed, and wind direction.

## Entity Browser and budgets

Entity Browser can sort by faction, entity type, role, trait, and modded/unmodded content. Budgets appear in the lower right:

- Object Budget: props/compositions.
- AI Budget: non-player characters.
- Vehicle Budget: vehicles.
- System Budget: respawn points, objectives, arsenals, and similar systems.

If a budget reaches 100%, more items of that budget category cannot be placed until earlier items are removed. Removing killed/destroyed entities can free budget.

## Waypoints and objectives

Docs distinguish waypoints from objectives:

- Waypoints are orders for AI groups.
- Objectives are similar directional markers but addressed to factions/players.

Waypoint examples preserved from docs:

- Move: completes when group leader reaches waypoint radius.
- Forced Move: move ignoring autonomous behavior.
- Move Relaxed / Patrol: slower/different movement.
- Search and Destroy: timed waypoint; enemy in radius resets timer.
- Defend: AI stands guard; default never completes.
- Get In: AI checks for available functional vehicle within radius; completes after mounting or timeout.
- Get Out: AI moves to waypoint radius and disembarks.
- Suppressive Fire: units shoot at waypoint position; does not complete.

## Editable prefab pipeline

Making an entity editable in Game Master is data/editor-first. Several components must be added and the entity needs replication. Because this affects performance, do not make every tree/rock editable; create inherited editable variants only for content that must be edited/placed.

Existing prefab automated workflow:

1. Prepare editable prefab config. Override the editable prefab config in the addon when needed.
2. Set Image Placeholder to a registered PNG source. Packed data lacks source PNG files, so placeholder generation fails if this points to a packed-only texture.
3. Select prefab `.et` files in Resource Browser. Default config ignores `_base`, `_Base`, `_dst`, `_Dst`, and `_DST` suffixes.
4. Run Plugins > In-game Editor > Create/Update Selected Editable Prefabs, or use `Ctrl+Shift+U`.
5. Check logs for processed prefabs.
6. Interpret results:
   - Created/Updated: success.
   - Failed: commonly because child entity has `RplComponent`.
   - Non-editable: child entities without editable variants were detected; review whether children should also be editable.
7. Generated editable prefabs get `E_` prefix and are created under `PrefabsEditable/Auto` except vehicles/characters where config controls output.
8. Preview images are generated under `UI/Textures/EditorPreviews/Auto`.
9. Display names follow config rules, defaulting to localized string pattern using prefab filename. Change the string prefix from `AR` to a personal tag to avoid clashes.
10. Editable component types are assigned based on entity type, such as editable entity, character, vehicle, or group components.
11. Labels are assigned by editable prefab config rules.
12. Generate proper preview images using the image generation workflow.

Maintenance:

- Regenerate editable prefabs every time source prefab changes.
- Use Plugins > In-game Editor > Update All Editable Prefabs to update auto-generated editable prefabs and handle renamed/moved/deleted sources.
- Or select source/editable prefab and run Create/Update Selected Editable Prefabs.

## Custom editable prefab workflow

For custom editor-only prefabs such as slots/comments:

1. Add replication and editable component prefabs, commonly default RplComponent and editable entity component prefabs.
2. Only add components manually if you understand their configuration.
3. Choose a directory under `PrefabsEditable`.
4. Do not create anything manually under `PrefabsEditable/Auto`; it can be removed during auto-generation.
5. Drag the configured entity from World Editor into the chosen directory to create a prefab.
6. Name with `E_` prefix, e.g. `E_MyEntity.et`, to distinguish editable prefabs.

## Register placeable prefabs

Editable entities must be registered to appear in the content browser.

1. Create a config under `Configs/Editor/PlaceableEntities` of type `SCR_PlaceableEntitiesRegistry`.
2. Set Source Directory to the folder containing editable entity prefabs.
3. Prefer specialized registries such as Vehicles or Props instead of one giant registry.
4. Open `EditorModeEdit.et` in prefab edit mode.
5. Select `SCR_PlacingEditorComponent`.
6. Add the registry config to the Registries array.
7. If needed, override `EditorModeEdit.et` in the addon first.
8. In Resource Manager, run Plugins > In-game Editor > Register Placeable Entities.
9. Choose the registry config and confirm.
10. Repeat registration whenever prefabs in the folder are added, removed, or renamed.

## Factions, catalogs, and scenarios

Faction/Game Master/scenario work is usually data-first:

- Faction configs define playable groups, characters, gear, identities, and scenario integration.
- Entity catalogs determine what content systems can discover.
- Editable/placeable prefabs determine what Game Master can place.
- World/layer/game mode setup determines where scenarios run.
- Task system integration needs ownership, completion, cleanup, and multiplayer behavior.

Sample layout patterns:

```text
Configs/Factions/...
Configs/EntityCatalog/...
Configs/Editor/PlaceableEntities/...
PrefabsEditable/...
Prefabs/Characters/...
Prefabs/Weapons/...
UI/Textures/EditorPreviews/...
Language/...
Worlds/...
Missions/...
```

## Task and script integration cautions

Use script only after identifying the data/config surface. For task system or Game Master extensions:

- Search for existing project `SCR_` task/faction/editor classes.
- Verify callback signatures in `api-extended.md`.
- Keep server/authority ownership explicit for task state.
- Ensure cleanup when task/composition is deleted by Game Master.
- Validate in an actual scenario, not just by compiling scripts.

## API Notes

Use `api-extended.md` for `SCR_EditableEntityComponent`, `SCR_EditableCharacterComponent`, `SCR_EditableVehicleComponent`, `SCR_EditableGroupComponent`, `SCR_PlaceableEntitiesRegistry`, `SCR_PlacingEditorComponent`, task systems, faction systems, and Game Master editor APIs. Use `api-main.md` only for generic resource/entity/component/spawn APIs.

## Common Traps

- Adding a prefab file but not creating/registering an editable prefab.
- Putting manual files in `PrefabsEditable/Auto`.
- Forgetting preview image/localization/catalog updates.
- Ignoring editable-prefab performance/replication cost.
- Treating objectives as AI waypoints.
- Removing playable faction without accounting for assigned players.
- Forgetting to re-register placeable entities after add/remove/rename.

## Review Checklist

- Is the work data-first unless script integration is clearly needed?
- Are editable prefab generation, registry, and `EditorModeEdit` wiring covered?
- Are catalogs/factions/scenario/game mode consumers identified?
- Are budget/performance/replication implications stated?
- Are runtime scenario verification steps listed?

## API Notes

- Scenario and Game Master work is usually data-first, but script appears through game mode logic, task behavior, components, and editable entity behavior.
- Verify exact scenario/game mode APIs in `api-extended.md` because project-specific `SCR_` classes are common.
- Use `ResourceName` for placeable prefab references and catalog resources.
- Use replication APIs only for state that must synchronize between server and clients.
- Use Workbench editor APIs only for tools that edit scenario resources, not for runtime Game Master behavior.

## generated-pattern-from-docs: Editable Prefab Registration

```text
Create or inherit prefab.
Add/configure components expected by the editable entity system.
Generate or update editable entity configuration.
Register the prefab where Game Master can discover it.
Test placement, deletion, visibility, and replication in a scenario.
```

This is intentionally a data workflow rather than a code snippet because the official Game Master documentation emphasizes prefab/config registration and editor wiring.

## Scenario Detail

- A scenario is not only a world; it includes game mode, faction, player, objective, and system configuration.
- Scenario behavior can depend on catalog entries and faction definitions.
- Removing a faction can affect assigned players and existing scenario logic.
- Adding placeable content requires the correct discovery path, not only adding a prefab to the addon.
- Conflict mode content often has additional assumptions about factions, objectives, resources, and game mode systems.
- Mission testing should include fresh start, player join, restart, and server/client role checks.
- Scenario failures often come from missing data registration rather than script exceptions.

## Game Master Detail

- Game Master placement depends on editable entities and registered content.
- Editable entity setup should consider replication and performance budgets.
- Entity Browser contents are not a raw list of every prefab in the addon.
- Custom placeable objects need the right config path to appear.
- Editor-only previews do not prove runtime Game Master placement works.
- Placed entities should be tested for interaction, ownership, deletion, and persistence expectations.
- Expensive scripted components can multiply quickly when Game Master spawns many entities.

## Task And Objective Detail

- Tasks/objectives are gameplay goals, not AI waypoints.
- Waypoints direct AI movement; objectives represent player-facing or game-mode-facing tasks.
- Task state must be synchronized if clients need to observe it.
- Server authority should own task progression.
- UI task presentation should react to replicated or game-mode state.
- Joining players need correct task state after join.
- Do not use local-only variables for objective state in multiplayer scenarios.

## Faction And Catalog Detail

- Faction data connects units, loadouts, catalogs, and scenario systems.
- A new faction sample is the right reference for faction-facing content.
- Entity catalogs make content discoverable by systems such as arsenal or placement.
- Catalog omissions can make correct prefabs invisible to scenario tools.
- Faction edits should be tested in the scenario that consumes them.
- Game Master-visible content and faction-visible content are related but not identical.
- Keep localization and UI metadata aligned with faction/catalog entries.

## Scenario Review Detail

- Check game mode resource identity.
- Check scenario world resource identity.
- Check playable factions.
- Check assigned player roles.
- Check spawn points and respawn logic.
- Check objective/task initialization.
- Check task state replication.
- Check faction catalogs.
- Check arsenal or supply integration.
- Check Game Master editable content.
- Check AI waypoint/objective distinction.
- Check Conflict-specific systems when editing Conflict scenarios.
- Check server startup scenario ID.
- Check dedicated-server logs for scenario load failures.
- Check client join flow after scenario start.
- Check restart behavior.
- Check mod dependency load order.
- Check localization for task/faction/player-facing text.
- Check performance when many placeable entities are spawned.
- Check cleanup/deletion of dynamically created scenario entities.

## Game Master Review Detail

- Verify entity appears in the expected placement category.
- Verify placement works as host.
- Verify placement works with client observation.
- Verify deletion/destruction works.
- Verify editable properties are present.
- Verify scripted behavior starts after placement.
- Verify replicated components initialize correctly.
- Verify user actions work after placement.
- Verify AI can interact with or navigate around placed objects when relevant.
- Verify catalogs update after add/remove/rename.
- Verify replacement content does not unintentionally alter unrelated scenarios.
- Verify new faction content appears only where intended.
- Verify budget/performance limits for large object sets.
- Verify saved scenario data after editor changes.
- Verify runtime behavior after a clean launch.

## Scenario Failure Detail

- Scenario does not appear: check scenario resource registration and server config.
- Scenario starts wrong mode: check game mode resource.
- Players cannot spawn: check factions, slots, spawn points, and respawn configuration.
- Faction content missing: check faction data and entity catalogs.
- Arsenal content missing: check arsenal/catalog metadata.
- Game Master content missing: check editable entity config and registry.
- Objective missing: check task initialization and scenario logic.
- Objective desyncs: check authority and replicated task state.
- AI ignores routes: check waypoints, navmesh, and runtime AI setup.
- Placed entity has no behavior: check prefab components and lifecycle.
- Placed entity desyncs: check replication setup.
- Server fails before join: check logs, addon load, script compile, and resource validation.
- Works in editor but not server: check scenario ID, mod list, and client-only assumptions.
- Works as host but not client: check RPC receiver, ownership, and authority.
- Works before restart but not after: check persistent scenario/config state.
- Works locally but not published: check addon dependencies and included resources.

## Data Ownership Detail

- Scenario resources own scenario setup.
- Faction resources own faction identity and available content.
- Catalog resources own discoverability.
- Prefabs own entity behavior and components.
- Game mode script owns runtime rules.
- Task systems own objective state.
- Game Master config owns editable placement behavior.
- Server config owns startup scenario selection.
- Workshop metadata owns published addon identity.
- Do not move responsibility into script when a documented data surface owns it.

## Scenario Test Matrix

- Open the scenario in Workbench.
- Start the scenario locally.
- Start the scenario through server config.
- Join before objective state changes.
- Join after objective state changes.
- Switch or remove a faction and retest player assignment.
- Place custom content through Game Master.
- Delete custom content through Game Master.
- Restart the scenario and confirm initialization.
- Run with a clean profile.
- Run with declared addon dependencies only.
- Review server logs for load, script, and resource errors.
