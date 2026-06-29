# Resources Prefabs Configs

## When to read this reference

Read for `ResourceName`, resource loading, prefabs, config classes/objects, `BaseContainer`, UI layouts, entity catalogs, arsenal/faction consumers, serialized fields, and data-first workflows.

## Search terms

`ResourceName`, `Resource.Load`, `.et`, `.conf`, `.layout`, `BaseContainer`, `BaseContainerTools`, `Prefab`, `Prefab Data`, `Entity Catalog`, `Arsenal`, `Resource Manager`, `UIWidgets.ResourceNamePicker`, `WorkspaceWidget.CreateWidgets`

## Source authority summary

Use resource/prefab/config wiki pages and Resource Manager docs for workflows. Use sample mods for real layouts across configs, prefabs, UI, worlds, language, and project metadata. Use API data for `ResourceName`, `Resource.Load`, `BaseContainer`, spawn, and widget signatures.

## Data-first decision rules

Use data-first when the task is about:

- Placing content in Game Master, arsenal, faction, scenario, or world editor lists.
- Changing weapon/vehicle/gear stats, slots, audio/animation resources, preview images, or localized names.
- Wiring components, resources, and inherited prefab overrides.
- Defining catalogs, faction loadouts, scenarios, server startup, UI layout, or Workshop package metadata.

Use script-first only when behavior cannot be expressed in config/prefab/editor data or when a script hook is explicitly required.

## ResourceName fields

Use `ResourceName` for `.et`, `.conf`, `.layout`, texture, material, sound, animation, and other resource references. Provide editor picker attributes with extension filters.

generated-pattern-from-docs

```c
[Attribute("", UIWidgets.ResourceNamePicker, "Prefab to spawn", "et")]
protected ResourceName m_PrefabToSpawn;

[Attribute("", UIWidgets.ResourceNamePicker, "Config resource", "conf")]
protected ResourceName m_ConfigResource;

[Attribute("", UIWidgets.ResourceNamePicker, "UI layout", "layout")]
protected ResourceName m_LayoutResource;
```

Guard empty values:

```c
if (m_PrefabToSpawn == ResourceName.Empty)
{
	Print("Prefab resource is not assigned", LogLevel.WARNING);
	return;
}
```

## Resource loading and prefab spawning

`Resource.Load(ResourceName name)` loads a resource or gets it from cache. `Game.SpawnEntityPrefab(Resource templateResource, BaseWorld world = null, EntitySpawnParams params = null)` instantiates a prefab resource.

generated-pattern-from-docs

```c
Resource prefabResource = Resource.Load(m_PrefabToSpawn);
if (!prefabResource)
{
	PrintFormat("Could not load prefab resource %1", m_PrefabToSpawn, LogLevel.ERROR);
	return;
}

EntitySpawnParams params = new EntitySpawnParams();
// Verify current EntitySpawnParams fields before assignment.
IEntity entity = GetGame().SpawnEntityPrefab(prefabResource, null, params);
```

Authority caveat: replicated runtime entities should be spawned/inserted on the server/authority according to replication state rules.

## Prefab inheritance and serialized fields

Prefab work is often inheritance/override work:

- Base prefabs define common components/resources.
- Child prefabs override fields, meshes, materials, inventory, slots, audio, animation, or preview data.
- Serialized component field names matter; renaming code fields can break stored prefab data.
- Component class names and resource paths should remain stable after content ships.
- If moving resources, update every config/prefab/catalog/UI reference that points to them.

Prefab integration checklist:

1. Identify parent prefab and child override.
2. Identify which component/config owns the field.
3. Check inherited values before overriding.
4. Update editor preview/localization/catalog entries if the item appears in UI.
5. Re-save/rebuild resources in Workbench as required.
6. Test placement/spawn in actual runtime or Game Master path.

## Config classes and BaseContainer

Use config classes for structured `.conf` data. `BaseContainer` is a core config/container surface; `BaseContainerTools.LoadContainer(ResourceName)` and `SaveContainer` exist in API data for tool/editor flows.

Config workflow:

1. Decide whether the data belongs in `.conf`, prefab `.et`, UI `.layout`, world `.ent`, or script defaults.
2. Create/update config class only if existing project/source patterns support it.
3. Keep config class field names stable.
4. Use defaults and failure handling for missing fields.
5. Keep resource references typed as `ResourceName`.
6. Validate in Resource Manager/config editor and in the consuming system.

generated-pattern-from-docs

```c
class TAG_Config
{
	[Attribute(defvalue: "1", desc: "Enabled")]
	bool m_bEnabled;

	[Attribute("", UIWidgets.ResourceNamePicker, "Prefab", "et")]
	ResourceName m_Prefab;
}
```

## Entity catalogs, arsenal, faction, and scenario consumers

Official samples show content paths such as:

```text
Configs/EntityCatalog/US/US_InventoryItems.conf
Configs/EntityCatalog/USSR/USSR_InventoryItems.conf
PrefabsEditable/Auto/Systems/Arsenal/ArsenalBoxes/...
Prefabs/Weapons/...
Prefabs/Characters/...
UI/Textures/EditorPreviews/...
Language/...
```

Adding a prefab file alone does not make content available. You usually need catalog/config entries and may need faction, arsenal, Game Master editable, preview image, and localization updates.

## UI layout resources

Layouts are data resources; widget scripts are code. Keep this distinction clear:

- `.layout` defines widget hierarchy/visual structure.
- Generated layout class workflows belong to Resource Manager when supported.
- Runtime scripts create widgets through `WorkspaceWidget.CreateWidgets(ResourceName layoutResourceName, Widget parentWidget = NULL)`.
- UI resources often need imagesets, fonts, rich text, and localization resources.

generated-pattern-from-docs

```c
Widget root = GetGame().GetWorkspace().CreateWidgets(m_LayoutResource, parent);
if (!root)
	return;
```

Verify workspace access in the current UI context; dedicated server has no normal UI workspace.

## Project layout patterns from samples

Common sample layout families:

```text
Scripts/Game/...
Scripts/WorkbenchGame/...
Configs/...
Configs/Weapons/Ammo/...
Configs/Weapons/AIBallisiticTables/...
Configs/EntityCatalog/...
Prefabs/...
PrefabsEditable/...
Worlds/...
UI/Textures/EditorPreviews/...
Language/localization.*
addon.gproj or <AddonName>.gproj
previewImage.jpg
thumbnail.png
```

Use the closest sample family (`SampleMod_NewWeapon`, `SampleMod_NewCharacter`, `SampleMod_Main`, etc.) for layout, then verify details in topical references and API.

## Resource Manager validation

After changing resources/configs/prefabs:

- Open Resource Manager/Workbench.
- Confirm resources resolve with no missing dependency indicators.
- Rebuild/process imported assets when source files changed.
- Re-save prefabs/configs if class/schema changes require it.
- Test the consuming path: spawn prefab, open layout, load config, place Game Master item, or launch scenario/server.

## API Notes

Use `api-main.md` for `ResourceName`, `Resource.Load`, `BaseContainer`, `BaseContainerTools`, `Game.SpawnEntityPrefab`, `EntitySpawnParams`, and `WorkspaceWidget.CreateWidgets`. Use `api-extended.md` for specialized config classes, entity catalog systems, widget classes, and generated Resource Manager APIs.

## Common Traps

- Treating prefab/config/catalog tasks as script-only.
- Forgetting empty `ResourceName` guards.
- Breaking prefab serialized data by renaming fields.
- Spawning replicated prefabs on a client.
- Adding weapon/gear prefab but not catalog/arsenal/faction/UI data.
- Assuming UI layout code works on dedicated server.

## Review Checklist

- Is the task classified as data-first/script-first/mixed?
- Are resource extensions and picker widgets correct?
- Are prefab inheritance and serialized field stability addressed?
- Are catalogs/factions/arsenal/Game Master consumers covered?
- Are Workbench Resource Manager validation steps listed?

## ResourceName Detail

- Use `ResourceName` for paths that refer to Workbench-managed resources.
- Pair `ResourceName` fields with resource picker attributes so designers avoid free-text mistakes.
- Keep resource type filters narrow, such as entity prefab resources for spawnable prefabs.
- Check for empty values before loading.
- Check `Resource.Load()` result before using the resource.
- Log the failing path when load fails.
- Do not hard-code addon-local paths in reusable script when prefab/config data can provide them.
- Avoid renaming resources without updating all prefab/config/catalog references.

## Prefab Detail

- Prefab inheritance is the normal path for variants.
- Replacement is a global behavior change and should be explicit.
- Serialized component fields are part of the prefab contract.
- Removing a component can break user actions, audio, animation, damage, inventory, or replication.
- Adding a component in script is not the same as adding it to a prefab for designers.
- Reopen saved prefabs after structural edits to check serialized data.
- Test inherited prefab variants in the systems that consume them.
- Keep preview resources current for content that appears in editor browsers.

## Config And BaseContainer Detail

- Use config data where Reforger systems expect config-driven behavior.
- `BaseContainer` access should be guarded because fields/resources may be absent.
- Config schema changes can affect existing resources.
- Keep parsing and validation close to load time.
- Avoid doing config traversal repeatedly during frame updates.
- Prefer clear failure logs over silent defaults when required config is missing.
- Do not replace entity catalog or faction config with ad hoc script lists.

## Catalog And Consumer Detail

- Entity catalogs make content discoverable to systems.
- Arsenal and inventory visibility can require catalog and UI metadata.
- Game Master placement can require editable entity config and registry updates.
- Faction content needs faction-side references, not just standalone prefabs.
- Scenario content must link to the game mode/scenario systems that consume it.
- UI layouts need widget resources and script code that creates/uses them in the right context.
- Dedicated servers should not execute client UI layout code.

## Resource Manager Verification Detail

- Open Resource Manager and resolve the edited resource.
- Check missing dependency warnings.
- Rebuild or process imported assets after source changes.
- Validate prefab inheritance and overrides visually.
- Inspect resource references before publishing.
- Confirm addon dependencies include resources referenced from other addons.
- Test a clean launch where only declared dependencies are available.

## Prefab Review Detail

- Check inherited prefab source before editing overrides.
- Check whether an override is local to the variant or intended as replacement.
- Check component order only when the engine/system depends on it.
- Check entity catalogs for discoverability.
- Check faction data for faction-specific content.
- Check arsenal metadata for player equipment.
- Check Game Master editable config for placeable content.
- Check localization for display names and descriptions.
- Check UI layouts for client-only assumptions.
- Check audio project paths for sound-emitting prefabs.
- Check animation workspace references for animated assets.
- Check material and texture dependencies for visual assets.
- Check collision and physics resources for props/vehicles.
- Check damage setup for vehicles and interactive objects.
- Check inventory slot compatibility for gear.
- Check magazine/ammo compatibility for weapons.
- Check simulation configs for vehicles.
- Check generated data after import or rebuild.
- Check saved prefab reload after structural edits.
- Check clean profile launch for local-only path mistakes.

## Config Consumer Detail

- A config can be valid but unused if no system references it.
- A prefab can be valid but undiscoverable if no catalog references it.
- A catalog entry can be valid but invisible if faction/scenario data excludes it.
- A UI layout can load but fail if expected widgets are renamed.
- A resource can load in editor but fail on server if addon dependencies are missing.
- A replacement resource can affect more systems than the edited test case.
- A field default can work for new prefabs but not migrate old serialized content.
- A missing localization key can look like a UI bug.
- A missing preview can look like a browser/catalog bug.
- A wrong resource extension can make picker filtering misleading.
- A hard-coded path can pass locally and fail after publishing.
- A script list can drift from the real catalog.

## Resource Dependency Detail

- Identify every resource directly edited by the change.
- Identify every resource indirectly referenced by those resources.
- Identify base prefabs and inherited prefabs separately.
- Identify config resources and prefab resources separately.
- Identify generated resources and source resources separately.
- Identify local-only files before publishing.
- Identify addon dependencies for cross-addon references.
- Identify whether a resource is editor-only or runtime-required.
- Identify whether a resource is client-only or server-required.
- Identify whether a UI layout is needed by dedicated server code.
- Identify whether catalog entries point at the final prefab variant.
- Identify whether faction data points at the final catalog.
- Identify whether scenario data points at the final faction/game mode resources.
- Identify whether Game Master config points at editable prefabs.
- Identify whether replacement resources affect existing missions.
- Identify whether asset import output was regenerated after source changes.
- Identify whether Resource Manager reports unresolved references.
- Identify whether a clean launch reproduces successful resource loading.

## Data Change Matrix

- New prefab: create, save, reopen, place, run.
- Inherited prefab: inspect base, override only needed fields, test inherited behavior.
- Replacement prefab: document replaced resource and test all known consumers.
- New config: validate schema and identify consuming system.
- Catalog edit: verify discoverability in the target system.
- Faction edit: verify scenario and arsenal consumers.
- UI layout edit: create widgets and guard missing children.
- Resource path edit: load in editor and clean runtime profile.
- Asset import: rebuild generated outputs and inspect dependencies.
- Localization edit: verify display text in the consuming UI.
- Workshop package: verify included files and dependency metadata.
