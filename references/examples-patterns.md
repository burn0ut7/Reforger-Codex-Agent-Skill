# Official Examples And Patterns

Use this file to choose the nearest official sample before writing or reviewing a mod. The sample addons are the best source for project layout, resource naming, prefab dependency shape, and Workbench-facing asset organization.

## Sample Selection

Pick the smallest sample that matches the task:

- Script-only behavior: use the modded script sample.
- Workbench editor extension: use the Workbench plugin sample.
- New weapon: use the new weapon sample.
- Modified weapon: use the modded weapon sample.
- Replacement weapon/vehicle: use the replacement sample.
- New vehicle: use the new car sample.
- Modified vehicle: use the modded car sample.
- Character gear: use the new character sample.
- Faction/catalog content: use the new faction sample.
- Prop: use the new prop sample.
- Animation workflow: use the animation workshop sample.
- Cinematic or sequence content: use the cinematic tutorial sample.
- Broad addon structure: use the main sample.

## SampleMod_Main

Broad reference addon. Use it when the task involves general addon structure rather than one specialized domain.

Typical content areas:

- Assets.
- Common shared resources.
- Configs.
- Language/localization.
- Missions.
- Prefabs.
- Terrains.
- UI resources.
- Worlds.
- Project metadata.

Patterns to reuse:

- Keep resource categories separated.
- Put localizable strings in language resources rather than hard-coded script text.
- Treat missions/worlds/prefabs/configs as connected data, not isolated files.
- Use the addon structure as a navigation model for mixed-content mods.

## SampleMod_ModdedScript

Best starting point for script behavior changes.

Use it for:

- Modded classes.
- Extending existing gameplay script.
- Scoring or game-mode behavior changes.
- Addon script module layout.
- Learning how script changes are packaged into a mod.

Pattern:

```c
modded class SomeExistingClass
{
	override void SomeMethod()
	{
		super.SomeMethod();
		// Add focused behavior after preserving base behavior.
	}
}
```

Review focus:

- Does the modded class target an existing class?
- Does the override call `super` when base behavior must be preserved?
- Is the script in the correct module for the class being modified?
- Is the change data-driven where a config/prefab edit would be better?

## SampleMod_WorkbenchPlugin

Best starting point for Workbench extension work.

Use it for:

- Resource Manager context menu plugins.
- Script Editor plugins.
- String Editor/Localization Editor plugins.
- World Editor plugins.
- World Editor tools.
- Workbench dialog and module access patterns.

Patterns:

- Annotate plugin classes with `WorkbenchPluginAttribute`.
- Use the attribute to declare name, description, shortcut, icon, module dependencies, category, font icon, and resource type filters.
- Implement `Run()` for normal command behavior.
- Implement `RunCommandline()` only for command-line execution.
- Implement `Configure()` for plugin configuration UI.
- Use module APIs rather than guessing editor state.

Review focus:

- Is the plugin loaded by the intended Workbench module?
- Are resource type filters narrow enough for context-menu commands?
- Does the plugin handle empty selection and invalid resources?
- Does the command use Workbench APIs instead of runtime game APIs?

## SampleMod_NewWeapon

Best starting point for adding a new weapon.

Use it for:

- New weapon prefab structure.
- Attachment setup.
- Magazine and ammunition resources.
- Ballistic data.
- Entity catalog integration.
- Arsenal-facing resources.
- Weapon-specific user action examples.
- UI and editor preview resources.
- Localization.

Pattern:

- Create the asset and prefab hierarchy first.
- Wire magazine/ammunition/attachment resources.
- Add catalog and UI-facing metadata.
- Validate placement/equipment behavior.
- Only add script where data cannot express the behavior.

Review focus:

- Are the weapon, magazines, ammunition, and attachments all present and linked?
- Are catalog entries and localization included?
- Does the prefab inherit from an appropriate base where possible?
- Are animation and audio references coherent?

## SampleMod_ModdedWeapon

Best starting point for changing an existing weapon.

Use it for:

- Existing weapon variant changes.
- Modified resource values.
- Audio or visual replacement on a weapon.
- Learning override boundaries.

Review focus:

- Is this a variant or a replacement?
- Are base-game dependencies intentional?
- Are only necessary fields overridden?
- Does the modified weapon still resolve magazine, ammo, animation, and audio resources?

## SampleMod_Replacement

Use only when the goal is to replace existing base-game content.

Patterns:

- Keep replacement scope explicit.
- Document which base prefabs/resources are replaced.
- Test all contexts where the base resource appears.

Review focus:

- Replacement can affect missions, arsenal, Game Master placement, factions, and existing scenarios.
- Inheritance is usually safer for a variant; replacement is appropriate only for global substitution.

## SampleMod_NewCar

Best starting point for adding a vehicle.

Use it for:

- Vehicle asset import structure.
- New vehicle prefab setup.
- Vehicle simulation configuration.
- Editor previews.
- Placement testing.

Review focus:

- Does the prefab resolve all simulation resources?
- Are seat/compartment interactions preserved?
- Does physics behave in editor and runtime?
- Has multiplayer behavior been considered?

## SampleMod_ModdedCar

Best starting point for modifying an existing vehicle.

Use it for:

- Existing vehicle variant changes.
- Prefab inheritance or override patterns.
- Vehicle editor preview workflow.

Review focus:

- Does the edit affect physics, seats, damage, audio, or replication?
- Are inherited base resources still valid?
- Is replacement behavior intentional?

## SampleMod_NewCharacter

Best starting point for character gear and wearable items.

Use it for:

- Gear prefab structure.
- Inventory-facing items.
- Wearable compatibility.
- Character preview resources.

Review focus:

- Is the item configured for the correct slot/usage?
- Are visual, inventory, localization, and catalog references present?
- Does the item work on intended character types?

## SampleMod_NewFaction

Best starting point for faction-facing content.

Use it for:

- Faction data.
- Entity catalogs.
- Loadouts and gear sets.
- Scenario-facing content.
- Game Master and arsenal visibility.

Review focus:

- Are catalogs linked to faction resources?
- Are placeable entities and inventory items visible where expected?
- Does faction content show up in the intended scenario or Game Master context?

## SampleMod_NewProp

Best starting point for a placeable prop.

Use it for:

- Static or simple interactive prefab setup.
- Editor previews.
- Collision/physics setup.
- Basic placement validation.

Review focus:

- Is it a simple prop, interactive object, inventory item, or scenario object?
- Are collision and physics intentional?
- Is the prefab registered where the user expects to place it?

## SampleMod_AnimationWorkshop

Best starting point for animation editor and weapon animation workflows.

Use it for:

- Animation workspace structure.
- Animation graph/instance relationships.
- Weapon animation examples.
- Editor validation patterns.

Review focus:

- Does the workspace load cleanly?
- Is the graph default behavior valid?
- Are tags/events and attachments aligned?

## SampleMod_CinematicTutorial

Best starting point for cinematic and sequence content.

Use it for:

- Cinematic scene resources.
- Camera/character animation relationships.
- Tutorial-style scene assembly.

Review focus:

- Are camera, character, animation, and scene resources all linked?
- Does the sequence play in the intended context?

## Cross-Sample Patterns

- Official samples are data-heavy. If a solution is mostly script for an asset problem, re-check the relevant sample.
- Prefabs, configs, catalogs, localization, and previews usually move together.
- Replacement samples are not general variant samples.
- Workbench plugin code belongs to editor modules, not runtime gameplay assumptions.
- New asset samples are useful for folder structure even when the user is making a different asset in the same family.

## API Notes

- Samples often demonstrate resource shape more than API calls; when code is present, verify signatures in `api-main.md` and `api-extended.md`.
- Use `WorkbenchPlugin` APIs only inside editor plugin samples.
- Use `ResourceName` and `Resource.Load()` patterns when adapting sample resource references into script.
- Use `RplRpc`, `RplProp`, and authority checks when turning a sample user action into multiplayer gameplay.
- Use `IEntity` and `ScriptComponent` APIs for component samples, but preserve prefab/config relationships shown by the sample.

## generated-pattern-from-docs: Sample Adaptation

```c
// Adapt a sample by preserving the resource graph first, then changing names and data.
// Verify script signatures separately; samples are structural guidance, not an API index.
```

This is a no-code pattern because most official samples are resource and prefab examples. The important implementation step is choosing the nearest sample and preserving its asset/config/prefab relationships while changing only the task-specific content.

## Review Checklist

- Was the closest sample selected by task type?
- Is the task a new asset, modified variant, replacement, editor plugin, or script behavior change?
- Are resource folders and prefab/config relationships preserved?
- Are localization and UI/editor preview resources included when the sample includes them?
- Are catalog/faction/arsenal/Game Master registrations copied only when the feature needs those systems?
- Was replacement scope avoided unless global replacement was requested?
- Are script examples checked against current API references before reuse?

## Common Traps

- Using SampleMod_Replacement for a variant request.
- Copying a sample folder without updating resource references.
- Keeping visible names in script instead of localization resources.
- Moving sample assets into a flatter folder layout that breaks automation expectations.
- Treating editor screenshots/previews as optional when the content must be browsed in Workbench.
- Copying plugin code into runtime script modules.
- Copying runtime component code into Workbench plugin modules.
- Ignoring catalog registration and then wondering why content is not visible in arsenal, faction, or Game Master workflows.
