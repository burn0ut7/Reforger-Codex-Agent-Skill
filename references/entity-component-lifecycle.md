# Entity Component Lifecycle

## When to read this reference

Read before creating entities/components, adding editable component properties, wiring components to prefabs/world entities, registering event masks, using owner/component lookup, moving entities, or reasoning about editor/runtime lifecycle differences.

## Search terms

`ScriptComponentClass`, `ScriptComponent`, `ComponentEditorProps`, `Attribute`, `Add Component`, `Shift F7`, `OnPostInit`, `EOnInit`, `EOnFrame`, `SetEventMask`, `EntityEvent`, `GetOwner`, `FindComponent`, `GetOrigin`, `SetOrigin`, `_WB_`

## Source authority summary

The Create a Component page gives the strongest workflow for a World Editor component. The Entity Lifecycle page gives event order and callback caveats. Extracted API data verifies signatures. Samples show layout and naming, but docs define the component visibility and reload rules.

## Component creation workflow

1. Create a `.c` file named after the component class, for example `TAG_TeleportFieldComponent.c`.
2. Put the file in the Game script module, commonly `Scripts/Game/...`. A component script not in Game will not be listed in World Editor's Components list.
3. Name component classes with the `Component` suffix.
4. Define the matching component class immediately above the component:

```c
[ComponentEditorProps(category: "Tutorial/Component", description: "Warn then teleport humans")]
class TAG_TeleportFieldComponentClass : ScriptComponentClass
{
}

class TAG_TeleportFieldComponent : ScriptComponent
{
}
```

5. Use `ComponentEditorProps` to make the component visible in World Editor Add Component UI.
6. Compile/reload scripts in Workbench. The wiki specifically says scripts must be compiled and reloaded via `Shift+F7` before the component appears in World Editor.
7. Add the component to an entity in World Editor or to a prefab.
8. Verify editable fields serialize correctly and continue to work after prefab inheritance/override changes.

## ComponentEditorProps fields retained from docs

- `category`: category in the Create/Add Component tab where the component is found.
- `description`: documented as unused for now in the component tutorial, but still useful as human-facing intent.
- `color`: bounding-box line color when visible.
- `visible`: keeps bounding box always visible, drawn in `color`.
- `insertable`: documented field; check current API semantics before relying on it.
- `configRoot`: documented as unused in the tutorial.
- `icon`: direct path to a png used as World Editor component icon, e.g. an icon under Workbench data.

## Editable fields with Attribute

Use `[Attribute]` on fields that designers should edit in World Editor/prefabs. The teleport-field tutorial uses separate categories for Teleportation, Line Drawing, and Performance:

official-doc-example

```c
[Attribute(defvalue: "10", desc: "Warning radius", category: "Teleportation")]
protected float m_fWarningRadius;

[Attribute(defvalue: "2", desc: "Trigger radius", params: "0.25 10 0.25", category: "Teleportation")]
protected float m_fTriggerRadius;

[Attribute(defvalue: "1 0.75 0 1", desc: "Line colour", category: "Line Drawing")]
protected ref Color m_LineColour;

[Attribute(defvalue: "0.25", desc: "Duration between proximity checks", category: "Performance")]
protected float m_fCheckPeriod;
```

Do not rename serialized fields casually after a prefab or world entity uses them. Renames can break stored component data.

## Lifecycle facts from docs

Definitions:

- Frame: every drawing frame.
- Fixed Frame: fixed event 30 times per second.
- Physics Simulation Frame: fixed event at 60 simulations per second; configured in Workbench Options under Game Project / Modules / Physics Settings / Ticks.

Important caveat: some event methods are called only when enabled through `IEntity.SetEventMask()` or component event mask APIs, and some require engine conditions such as valid activated physics.

Lifecycle table highlights:

- Instantiation in Workbench play/game and Workbench edit includes constructors.
- Component `OnPostInit` and `EOnInit` happen during instantiation when conditions/event masks permit.
- Workbench edit mode has `_WB_SetTransform`, `_WB_OnInit`, `_WB_MakeVisible`, and `_WB_AfterWorldUpdate` style callbacks.
- Simulation init includes `EOnActivate`.
- Simulation loop can include `EOnFrame`, `EOnDiag`, `EOnFixedFrame`, `EOnSimulate`, `EOnPostSimulate`, `EOnPhysicsMove`, `EOnPostFrame`, and post-fixed/fixed-post callbacks.
- Destruction includes `OnDelete` and destructors.

Destruction warnings from docs:

- Do not delete components in an entity destructor; this can lead to null pointer exceptions.
- Do not reference the parent entity in a component destructor; the entity is already deleted by then.

## Event mask pattern

The component tutorial initializes arrays and enables frame callbacks in `OnPostInit`:

official-doc-example

```c
protected override void OnPostInit(IEntity owner)
{
	m_aNearbyCharacters = {};
	SetEventMask(owner, EntityEvent.FRAME);
}

override void EOnFrame(IEntity owner, float timeSlice)
{
	super.EOnFrame(owner, timeSlice);
}
```

Use this pattern only after checking current signatures. The extracted API has `ScriptComponent.OnPostInit(IEntity owner)`, `ScriptComponent.EOnFrame(IEntity owner, float timeSlice)`, and `GenericComponent.SetEventMask(notnull IEntity owner, int mask)`.

## Owner and component lookup

The component tutorial notes that `GetOwner()` and the `owner` callback parameter are not marked `notnull`, but a component cannot exist without an entity; a null owner would indicate a deeper problem. Still, robust task code should guard owner when code can run during delete/editor states or when using uncertain project hooks.

Use:

```c
IEntity owner = GetOwner();
if (!owner)
	return;

SomeComponent comp = SomeComponent.Cast(owner.FindComponent(SomeComponent));
if (!comp)
	return;
```

## Movement and transform APIs

Use `GetOrigin`/`SetOrigin` for simple world-position moves:

```c
vector pos = owner.GetOrigin();
owner.SetOrigin(pos + "0 0 5");
```

The teleport tutorial queries nearby characters, computes direction, then moves the character with `SetOrigin`:

```c
vector dir = vector.Direction(ownerPos, characterPos).Normalized();
character.SetOrigin(ownerPos + dir * m_fTeleportDistance);
```

Use matrix transforms when orientation matters:

```c
vector mat[4];
owner.GetTransform(mat);
owner.SetTransform(mat);
```

Be explicit about world versus local space. `GetTransform` and `SetTransform` are world transformation APIs in the extracted API. Use local APIs only when the parent-relative transform is intended.

## QueryEntities pattern

The component tutorial uses a throttled frame check:

1. Keep `m_fCheckDelay`.
2. Decrement by `timeSlice`.
3. When it reaches zero, reset it to `m_fCheckPeriod`.
4. Clear the nearby array.
5. Query entities by sphere from `owner.GetWorld()`.
6. Filter in a callback method.
7. Process the retained entities.

Source-backed callback:

```c
protected bool QueryEntitiesCallbackMethod(IEntity e)
{
	if (!e || !ChimeraCharacter.Cast(e))
		return false;

	m_aNearbyCharacters.Insert(e);
	return true;
}
```

## Prefab and Workbench integration

- Add components through World Editor Add Component or prefab editing workflows.
- Reload compiled scripts before expecting the class to appear.
- Keep component class category stable so designers can find it.
- Keep serialized attribute defaults meaningful.
- Re-open or re-save prefabs/worlds after class/field changes when Workbench requires it.
- Test both Workbench edit preview and actual runtime because `_WB_` callbacks and game callbacks differ.

## API Notes

Use `api-main.md` for `ScriptComponent`, `ScriptComponentClass`, `GenericComponent.SetEventMask`, `IEntity.GetOrigin`, `IEntity.SetOrigin`, `IEntity.GetTransform`, `IEntity.SetTransform`, and component lookup. Use `api-extended.md` for `_WB_` callbacks, `EntityEvent` enum values, `EQueryEntitiesFlags`, debug `Shape`, and specialized entity/component classes.

## Common Traps

- Component file outside Game module.
- Missing `ComponentClass` or wrong `ComponentClass` name.
- Forgetting `ComponentEditorProps`, causing no World Editor visibility.
- Not reloading scripts with `Shift+F7`.
- Registering expensive `EOnFrame` work without throttling.
- Deleting components from entity destructors.
- Accessing parent entity from component destructor.
- Moving replicated entities on clients without authority rules.

## Review Checklist

- Does class naming follow `XComponentClass` + `XComponent`?
- Is module placement correct?
- Are attribute fields stable and categorized?
- Are event masks and lifecycle callback signatures verified?
- Is Workbench Add Component/prefab wiring listed as a required verification step?

## Component Authoring Detail

- Start with the component class pair before writing behavior.
- Put editor metadata on the component class, not on random helper classes.
- Use stable category names so designers can find the component after reload.
- Keep attribute fields near the behavior that consumes them.
- Use `ResourceName` attributes for prefab/resource references.
- Use small helper methods for validation so lifecycle callbacks stay readable.
- Do not assume the owner has every component you expect; query and guard.
- Cache stable sibling components after setup when they are used often.
- Re-query only when the entity graph can change.

## Lifecycle Callback Detail

- `EOnInit` is for owner-aware setup.
- `OnPostInit` is useful when other components need to exist first.
- `EOnFrame` runs only after frame event registration.
- `EOnDiag` is diagnostic and should not carry required gameplay state.
- Cleanup must respect that other entities/components may already be gone.
- Avoid destructive owner/parent access from destructors.
- Do not spawn replicated children at arbitrary lifecycle points without checking replication insertion rules.
- If setup depends on resources, fail clearly when the resource cannot load.

## Transform Detail

- `GetOrigin()` is the quick position read.
- `SetOrigin()` is a direct position write and should be used only when direct mutation is appropriate.
- Full transform arrays are needed when rotation and orientation matter.
- World-space and local-space transforms are not interchangeable.
- Vehicles, characters, and physics-driven objects can require specialized movement paths.
- On replicated entities, direct movement from a client can desync or be overwritten.
- For spawned entities, set transform through spawn params where possible.

## Event Mask Detail

- Register only the callbacks needed by the component.
- Clear masks when temporary work completes.
- Do not register frame work from every instance if a manager or event callback can handle it.
- Keep per-frame logic small and bounded.
- Avoid repeated world queries from many component instances.
- If a component sleeps or disables behavior, clear its frame mask.
- Re-enable masks explicitly when behavior resumes.

## Workbench Verification Detail

- Reload scripts after adding new component classes.
- Confirm the component appears under the intended category.
- Add it to a prefab and save the prefab.
- Reopen the prefab to ensure serialized attributes persist.
- Place the prefab in World Editor when owner/world behavior matters.
- Run the game from Workbench to verify lifecycle callbacks.
- For replicated components, test host/client roles rather than only local preview.

## Component Failure Cases

- Component does not compile: inspect syntax, imports/module visibility, and class pair names.
- Component compiles but is not visible: inspect `ComponentEditorProps`, module placement, and script reload.
- Component is visible but cannot be added: inspect class inheritance and editor metadata.
- Component can be added but fields do not persist: inspect `[Attribute]` declarations and field renames.
- Component initializes but owner is null: inspect lifecycle usage and callback signature.
- Component runs locally but not in prefab: inspect whether it was actually attached and saved.
- Component works in editor but not server: inspect client-only assumptions and addon load order.
- Frame callback never runs: inspect event mask registration.
- Frame callback runs too often: inspect throttling and clear-mask logic.
- Transform update does nothing: inspect authority, physics, controller, and world/local space.
- Spawned prefab is null: inspect `ResourceName`, `Resource.Load()`, and spawn params.
- Sibling component lookup fails: inspect prefab component graph and lifecycle order.
- Destroy cleanup crashes: inspect deleted owner/parent/component assumptions.
- Replicated child does not appear: inspect spawn timing and hierarchy insertion.

## Integration Detail

- Attach components through prefab data when designers need reusable behavior.
- Add components through script only for dynamic composition that cannot be authored in data.
- Keep component fields stable after content ships.
- Prefer small components with clear owner contracts.
- Put cross-entity coordination in a manager only when per-entity components would duplicate expensive work.
- Avoid global state for entity-specific behavior.
- Keep local visual reactions separate from authority-side state mutation.
- Treat component dependencies as explicit requirements in comments or validation logs.
- Use Workbench placement to verify editor metadata.
- Use runtime launch to verify lifecycle.
- Use multiplayer launch to verify authority and replication.
- Use server logs to verify dedicated-server behavior.
- Use prefab reopen/save checks to verify serialization.
- Use Resource Manager checks for referenced resources.
- Use API lookup when a lifecycle callback does not fire.

## Owner Graph Detail

- Know whether the component owns behavior or only observes state.
- Know whether sibling components are required or optional.
- Know whether parent/child entity relationships can change during runtime.
- Know whether the component should survive prefab inheritance changes.
- Know whether the component needs runtime-created children.
- Know whether those children need replication.
- Know whether owner deletion can happen during callbacks.
- Know whether delayed callbacks can fire after deletion.
- Know whether Workbench-authored fields are required.
- Know whether defaults are safe for a newly added component.
- Know whether resources referenced by attributes are loaded on server and client.
- Know whether movement touches physics, animation, or controller systems.
- Know whether user actions call into the component.
- Know whether the component is part of a weapon, vehicle, character, prop, or scenario entity.
- Know whether the component should log failures once or continuously.
- Know whether component state must persist for join-in-progress.
- Know whether cleanup must clear event masks.
- Know whether cleanup must unsubscribe from invokers.
- Know whether state belongs in prefab data, runtime fields, or replicated fields.

## Component Test Matrix

- Add component to a new prefab.
- Add component to an inherited prefab.
- Save and reopen the prefab.
- Run with default attribute values.
- Run with deliberately invalid resource values.
- Run with missing optional sibling components.
- Run with required sibling components present.
- Delete the owner during gameplay.
- Disable behavior and confirm event masks are cleared.
- Re-enable behavior and confirm callbacks resume.
- Spawn the prefab at runtime.
- Place the prefab in a world.
- Test as host.
- Test as connected client.
- Test dedicated server when gameplay state is server-side.
