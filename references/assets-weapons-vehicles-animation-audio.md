# Assets, Weapons, Vehicles, Animation, And Audio

Use this reference when a task is about authored content rather than pure script: weapons, magazines, ammunition, vehicles, characters, props, animation workspaces, or audio projects. Arma Reforger content is usually data-first. Script is normally the glue around prefabs, components, resources, user actions, and editor tooling.

## Asset Workflow Rules

Official creation tutorials repeat the same early constraints for weapons and vehicles:

- Prepare an addon structure before importing assets. The engine does not require one exact folder layout, but the official layout keeps automation plugins, Resource Manager views, and future maintenance predictable.
- Prepare the mesh outside Workbench, export it, then import and configure it through Workbench tools.
- Use official sample addons as the closest known-good layout when creating a new asset family.
- Do not skip prefab configuration. A mesh import by itself is not a playable weapon, vehicle, prop, character item, or sound-emitting entity.
- Treat screenshots and editor previews in the sample addons as workflow evidence, not runtime code.

## New Weapon Creation

The weapon creation tutorial is built around importing an FBX, adding sockets and skeleton data, then configuring the weapon in Workbench. The official new weapon sample is the practical reference for folder layout and asset dependencies.

Key workflow:

1. Prepare addon structure.
2. Prepare and export the mesh.
3. Import the FBX into Workbench.
4. Add required sockets and skeleton setup.
5. Configure the weapon prefab.
6. Configure related resources: attachments, magazines, ammunition, ballistic data, catalog entries, localization, previews, UI images, and user actions.
7. Validate in Resource Manager and World Editor before relying on in-game testing.

Important content boundaries:

- A weapon prefab is not just a model. Expect prefab components, attachment points, inventory data, muzzle/optic relationships, animation/audio links, item catalog entries, and localized display text.
- New magazines and ammunition must be wired through configs/resources that the weapon can resolve.
- Replacement weapons can override existing content, but replacement workflows should be isolated from new-asset workflows because they depend on base-game paths and inheritance.
- Weapon animation is its own layer. If the weapon appears but does not animate correctly, inspect animation workspaces and skeleton/socket alignment before changing gameplay script.

Common new weapon sample areas:

- Weapon prefabs and inherited prefab variants.
- Magazine and ammunition configs.
- Attachment prefabs and attachment slots.
- AIBallisticTables.
- Entity catalogs and arsenal-facing resources.
- User action script examples for weapon-specific interaction.
- UI previews, editor previews, and localization resources.

## Modded Weapon Workflow

A modded weapon task is usually smaller than a new weapon task:

- Locate the existing weapon prefab or config being modified.
- Create an inherited or overridden resource in the addon.
- Change only the fields needed for the behavior or presentation change.
- Keep all dependent resource references valid.
- Test both Workbench preview and in-game inventory/equipment behavior.

Use replacement patterns only when the user's intent is to replace base-game behavior globally. For a new variant, prefer inherited content so the original remains intact.

## Vehicle And Car Creation

The car creation tutorial mirrors the weapon workflow: import an FBX, add sockets/skeleton as needed, configure the prefab, then configure simulation. It explicitly separates asset preparation, prefab configuration, and simulation configuration.

Key workflow:

1. Prepare the addon structure.
2. Prepare and export the vehicle mesh.
3. Import resources through Workbench.
4. Configure prefab hierarchy and components.
5. Configure simulation data.
6. Validate placement and behavior in World Editor.
7. Test in game with driver/passenger, damage, physics, audio, and replication expectations.

Vehicle tasks often involve:

- Prefab inheritance from an existing vehicle.
- Physics and simulation resources.
- Wheel, suspension, seat, compartment, and damage setup.
- Camera, interaction, and user action setup.
- Vehicle-specific sound components and audio project references.
- Editor previews and placement validation.

## Modded Car Workflow

For modifying an existing car:

- Prefer inherited prefab/config changes when creating a variant.
- Use replacement only for intentional global replacement.
- Preserve component structure unless the task requires changing simulation or interaction.
- Validate editor preview first, then physics and network behavior in game.

Vehicle changes are high risk because a visual-only edit can still break physics, seat use, damage setup, replication, or audio. When reviewing a vehicle change, inspect both the visual resource graph and the prefab component graph.

## Character Gear And Props

Character gear and prop samples are useful for non-weapon assets:

- Gear items usually need prefab setup, inventory metadata, attachment/slot compatibility, visuals, and localization.
- Props need placement-ready prefabs, editor previews, collision/physics decisions, and optional interaction/audio components.
- New faction samples show how gear, entity catalogs, faction data, and scenario-facing content are connected.

Use the sample addons to distinguish a simple static prop from an inventory item, wearable item, arsenal item, or faction-linked item. Those categories have different config and prefab requirements.

## Animation Editor

The Animation Editor connects animations through node-based graph files called Workspaces. It is not just a clip viewer; it owns the logical graph that selects and blends animation behavior.

Main interface concepts:

- Toolbar: file operations, edit operations, graph/view/play menus, checks, reload/rebinarise/stress-test tools.
- Anim Editor Preview: real-time preview of model motion, clip playback, camera controls, IK display, bone display, collider display, animation LOD, timeline controls, playback speed, and motion options.
- Workspace: creates and selects animation templates, animation instances, sheets, and graph resources.
- Animation Graph: node-based animation behavior.
- Anim Set: animation slots and instance data.
- Log Console, Debug Controls, Live Debug, Attachments Debug, and Errors panels: validation and runtime inspection surfaces.

Animation workspace facts:

- A workspace contains the files needed for the animation logic.
- Animation templates describe slots by category.
- Animation instances fill the same template with different animation sets, such as rifle locomotion versus pistol locomotion.
- Default nodes matter. If no default node is configured, playing the graph may do nothing.
- Checks can verify Source Sync and display tags used in the workspace.
- The preview timeline can use motion modes such as moving the ground, moving the entity, resetting movement each loop, or keeping animation in place.

For weapon animation tasks:

- Validate sockets, skeleton, and animation workspace relationships together.
- Do not debug animation by editing gameplay code first.
- Confirm animation events/tags and attachment alignment in the editor.

## Audio Editor

The Audio Editor creates `.acp` audio project files and node graphs that connect generated or sampled sound into game entities through sound components.

The getting-started tutorial demonstrates replacing character footsteps, but the workflow generalizes:

1. Create or modify an `.acp`.
2. Build a node chain with a waveform source and a Sound node.
3. Audition the sound in the editor.
4. Name the Sound node to match the sound event expected by game code or data.
5. Attach the `.acp` to the target entity's SoundComponent or specialized sound component.
6. Save/apply prefab changes as needed.
7. Test in game and inspect audio debug output.

Fundamental node pattern:

- A Bank or Generator outputs audio.
- A Sound node represents the named sound event.
- Connections route output ports to input ports.
- The Sound node name must match the event name used by the game/entity.

Footstep tutorial details that matter for other tasks:

- The target entity's sound component lists attached `.acp` files.
- Existing event names can be discovered by opening the base `.acp` and inspecting Sound nodes.
- For character footsteps, the tutorial identifies `SOUND_CHAR_MOVEMENT_FOOT` as the event to replace.
- Replacing a sound on a placed entity affects that placed instance unless the change is applied to the prefab.
- Signals can control node parameters for context-dependent sound.
- Debugging includes log output, waveform/output tracking, and component inspection.

## Asset Review Checklist

- Is the task new content, inherited variant, or replacement?
- Are all referenced resources resolvable through Resource Manager?
- Does the prefab component graph match the asset type?
- Are editor previews, localization, catalogs, and UI-facing resources present where expected?
- For weapons: are magazines, ammo, attachments, ballistics, animation, and audio considered?
- For vehicles: are simulation, seats, wheels, physics, damage, interaction, and replication considered?
- For audio: does the Sound node name match the runtime event name?
- For animation: does the workspace have valid default graph behavior and expected tags/events?
- Does the sample addon closest to the task use the same structure?

## Common Traps

- Treating FBX import as the whole asset workflow.
- Editing script to fix a missing prefab/config/resource link.
- Replacing base-game content when an inherited variant was requested.
- Forgetting catalog/localization/editor preview resources.
- Renaming audio Sound nodes without matching the event name expected by the entity.
- Assuming an animation clip works without a valid workspace graph.
- Testing only single-player behavior for vehicles, weapons, and user actions that will run on a server.

## API Notes

- Asset workflows mostly depend on data and Workbench resources, but script often appears through user actions, scripted components, sound events, and editor plugins.
- Use `ResourceName` fields for prefab, texture, material, audio project, layout, and config references that designers must pick in Workbench.
- Use `Resource.Load()` only after validating that the `ResourceName` is non-empty and points to the intended resource type.
- Use `IEntity` transform APIs for placed test entities, but do not use direct transforms as a substitute for vehicle simulation or character movement systems.
- Use `RplRpc` and `RplProp` only for gameplay state or interaction; visual asset configuration belongs in prefab/config resources.
- For Workbench automation around assets, use `WorkbenchPlugin` and module APIs rather than runtime game APIs.

## generated-pattern-from-docs: Weapon Resource Walk

```c
[Attribute("", UIWidgets.ResourceNamePicker, "Weapon prefab", params: "et")]
ResourceName m_sWeaponPrefab;

void ValidateWeaponPrefab()
{
	Resource weaponResource = Resource.Load(m_sWeaponPrefab);
	if (!weaponResource)
	{
		PrintFormat("Weapon prefab is not loadable: %1", m_sWeaponPrefab);
		return;
	}
	PrintFormat("Weapon prefab resource resolved: %1", m_sWeaponPrefab);
}
```

This pattern is not a full weapon implementation. It is the runtime side of the documented Workbench asset workflow: keep the prefab path editable, load it through the resource system, and fail clearly when the asset graph is incomplete.

## Texture And Material Checks

- Imported mesh resources commonly depend on texture and material resources that are separate from the mesh file.
- A weapon, vehicle, prop, or character item can look broken while its prefab logic is correct if textures or materials are missing.
- Texture naming and placement should follow the same addon structure as the asset, so Resource Manager can keep dependencies understandable.
- Do not fix missing texture paths in script; fix the material/resource assignment.
- Validate textures in Workbench viewport and in-game lighting because editor preview lighting can hide material mistakes.
- For replacement content, confirm that texture/material overrides affect only the intended inherited prefab or resource.
- For published addons, check that texture and material resources are included in the addon and not only available from a local work folder.

## Weapon Detail Checklist

- Mesh imported and visible in Workbench.
- Skeleton and sockets configured where the weapon requires them.
- Prefab inherits from a suitable base or intentionally defines the required components.
- Magazine compatibility is configured.
- Ammunition resources are linked.
- Ballistic data is present where required.
- Attachment slots match expected optic, muzzle, underbarrel, or accessory behavior.
- Inventory and arsenal metadata are present.
- Entity catalog entries are present when the weapon must be discoverable by systems.
- Localization exists for player-facing names and descriptions.
- UI image and editor preview resources are present where the sample uses them.
- Animation workspace references are coherent with skeleton/socket setup.
- Audio project and event names match expected weapon events.
- User actions are authority-safe if they change gameplay state.
- Multiplayer testing covers equip, fire, reload, drop, pickup, and join-in-progress visibility.

## Vehicle Detail Checklist

- Mesh import and collision setup are separated from gameplay simulation setup.
- Prefab hierarchy follows a known vehicle pattern.
- Simulation configuration is present and linked.
- Wheel and suspension data are coherent with the mesh.
- Seats and compartments are usable.
- User actions for entering, leaving, and interacting are intact.
- Damage components and hit zones are still valid after prefab edits.
- Audio project references resolve.
- Camera and occupant views are checked.
- Physics behavior is tested on uneven ground.
- Server authority is respected for gameplay-changing interactions.
- Clients observe vehicle movement and state changes correctly.

## Animation Detail Checklist

- Workspace opens without errors.
- Graph has a valid default node.
- Template and instance relationships are understood.
- Animation tags and events match the consumer system.
- Preview uses the correct first-person or third-person context where relevant.
- Additive, in-place, and root-motion choices are intentional.
- Attachment debug verifies weapon or prop alignment.
- Source sync and error panels are checked before changing script.

## Audio Detail Checklist

- `.acp` file is attached through the entity's sound component.
- Sound node names match event names expected by code or data.
- Node graph has a valid source-to-Sound chain.
- Signals are used where parameters must change at runtime.
- Audio is auditioned in the editor and tested in game.
- Prefab changes are applied to the prefab when global behavior is intended.
- Instance-only changes are used only for one placed entity.

## Asset Packaging Detail

- Check mesh import resources.
- Check texture resources.
- Check material resources.
- Check generated previews.
- Check prefab inheritance.
- Check config dependencies.
- Check catalog entries.
- Check localization keys.
- Check UI images.
- Check audio project references.
- Check animation workspace references.
- Check collision and physics data.
- Check inventory metadata.
- Check faction or arsenal availability.
- Check Game Master visibility when required.
- Check replacement scope.
- Check sample addon parity.
- Check Resource Manager warnings.
- Check in-editor preview.
- Check in-game behavior.
- Check multiplayer authority for interactions.
- Check dedicated server load for gameplay assets.
- Check published addon includes every referenced resource.
- Check clean profile behavior after packaging.

## Asset Failure Detail

- Weapon appears but cannot fire: check magazine, ammunition, muzzle, and action setup.
- Weapon fires but looks wrong: check model, material, texture, animation, and attachment setup.
- Weapon works locally but not client: check replication and authority for actions/state.
- Vehicle appears but cannot drive: check simulation, seats, controls, and physics data.
- Vehicle drives badly: check wheels, suspension, mass, collision, and terrain interaction.
- Vehicle desyncs: check server authority and replicated components.
- Prop appears without collision: check physics/collision resources.
- Gear appears but cannot equip: check inventory slot and character compatibility.
- Faction gear missing: check faction, catalog, arsenal, and localization resources.
- Animation does not play: check workspace default node, tags, events, skeleton, and sockets.
- Audio silent: check `.acp`, Sound node event name, component filenames, and runtime trigger.
- Texture missing: check material assignment, texture resource path, and packaged addon files.
- Preview missing: check editor preview/UI image resources.
- Replacement affects too much: check inherited versus replacement resource scope.

## Asset Test Matrix

- Open the asset resource in Workbench.
- Inspect Resource Manager dependencies.
- Open the prefab and inspect components.
- Save and reopen the prefab.
- Place the prefab in World Editor.
- Run the game from Workbench.
- Test inventory/equipment behavior for gear and weapons.
- Test physics and seats for vehicles.
- Test sound trigger events.
- Test animation preview and runtime animation behavior.
- Test client observation for gameplay-changing interactions.
- Test clean profile packaging.
