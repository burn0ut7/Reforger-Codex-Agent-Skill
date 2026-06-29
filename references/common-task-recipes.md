# Common Task Recipes

Use these recipes for frequent implementation tasks. They intentionally point back to the dense references when a task needs broader context.

## Create A ScriptComponent

Task type: runtime gameplay script.

Recipe:

1. Create a class extending `ScriptComponent`.
2. Add editor-visible fields with `Attribute` if the component needs data.
3. Use `EOnInit(IEntity owner)` for initialization that requires the owner.
4. Use `OnPostInit(IEntity owner)` when setup depends on components that must already exist.
5. Register event masks only for callbacks you need.
6. Attach the component to a prefab or entity in Workbench.
7. Test through Workbench game launch or Remote Console.

Example:

```c
class TAG_MyComponentClass : ScriptComponentClass
{
}

class TAG_MyComponent : ScriptComponent
{
	[Attribute("1.0", UIWidgets.EditBox, "Multiplier")]
	float m_fMultiplier;

	override void EOnInit(IEntity owner)
	{
		PrintFormat("TAG_MyComponent owner=%1 multiplier=%2", owner, m_fMultiplier);
	}
}
```

See `entity-component-lifecycle.md` and `scripting-core.md`.

## Add Editor Props And Attribute Fields

Task type: editor-facing script data.

Recipe:

1. Add `ComponentEditorProps` to the component class when editor metadata is needed.
2. Add `Attribute` to fields that designers configure.
3. Use `ResourceName` and `params: "et"` for prefab/entity resources.
4. Use specific widgets where the field needs constrained UI.
5. Validate values in runtime code because editor attributes do not guarantee correctness.

Example:

```c
[ComponentEditorProps(category: "GameScripted/MyAddon", description: "Example component")]
class TAG_ConfiguredComponentClass : ScriptComponentClass
{
}

class TAG_ConfiguredComponent : ScriptComponent
{
	[Attribute("", UIWidgets.ResourceNamePicker, "Prefab to spawn", params: "et")]
	ResourceName m_sPrefab;
}
```

See `entity-component-lifecycle.md`.

## Print Debug Info

Task type: diagnostics.

Recipe:

1. Use `Print()` for simple messages.
2. Use `PrintFormat()` for values.
3. Use `%1`, `%2`, etc. placeholders.
4. Escape literal percent signs as `%%`.
5. Prefer targeted logs over noisy per-frame logs.

Example:

```c
PrintFormat("Entity %1 at %2", owner, owner.GetOrigin());
```

See `scripting-core.md`.

## Get Entity Origin Or Transform

Task type: entity position/transform.

Recipe:

1. Use `IEntity.GetOrigin()` for position.
2. Use `GetTransform(out vector mat[4])` for full local transform.
3. Use `GetWorldTransform(out vector mat[4])` when world-space transform is required.
4. Use `GetYawPitchRoll()` for orientation as angles.
5. Keep local/world transform spaces explicit in code and review notes.

Example:

```c
vector origin = owner.GetOrigin();
vector transform[4];
owner.GetWorldTransform(transform);
```

See `api-main.md` and `entity-component-lifecycle.md`.

## Move Or Teleport An Entity

Task type: entity transform mutation.

Recipe:

1. Confirm the entity should be moved directly. Physics, character controllers, vehicles, and replicated entities may require a domain-specific API.
2. Use `SetOrigin()` for simple local-origin changes.
3. Use `SetWorldTransform()` or `SetTransform()` when the full matrix matters.
4. On replicated entities, perform authoritative movement on the authority side.
5. Re-test in multiplayer if clients need to observe the movement.

Example:

```c
vector newPosition = owner.GetOrigin() + "0 1 0";
owner.SetOrigin(newPosition);
```

See `entity-component-lifecycle.md` and `networking-multiplayer-replication.md`.

## Get Local Player Or Controlled Entity

Task type: player context.

Recipe:

1. First decide whether the code runs on client, server, or both.
2. Prefer game/player controller APIs already used in nearby code.
3. Do not assume local player context exists on dedicated server.
4. For user actions, use the action performer or owner context when available.
5. For multiplayer authority, resolve the replicated owner rather than trusting local input.

No universal one-liner is safe across all modules. Use existing project patterns and verify in `api-extended.md` for the specific player/controller classes in use.

See `networking-multiplayer-replication.md` and `api-extended.md`.

## Register Frame Or Update Events Safely

Task type: lifecycle/performance.

Recipe:

1. Register the frame event only when needed.
2. Use `SetEventMask(owner, EntityEvent.FRAME)` from a component.
3. Clear the event mask when work is complete.
4. Avoid expensive queries every frame.
5. Gate diagnostic logs so they do not spam.

Example:

```c
override void EOnInit(IEntity owner)
{
	SetEventMask(owner, EntityEvent.FRAME);
}

override void EOnFrame(IEntity owner, float timeSlice)
{
	// Do minimal per-frame work.
}
```

See `scripting-core.md` and `entity-component-lifecycle.md`.

## Add Or Modify A User Action

Task type: interaction.

Recipe:

1. Inspect the prefab's existing action/component setup.
2. Prefer data/prefab configuration for simple actions.
3. Add script only for behavior that cannot be expressed in config.
4. In multiplayer, execute authoritative state changes on the server/authority.
5. Use RPC only when an interaction must cross machine boundaries.
6. Test as host, client, and where possible dedicated server.

Example authority pattern:

```c
void RequestUse()
{
	Rpc(RpcAsk_Use);
}

[RplRpc(RplChannel.Reliable, RplRcver.Server)]
protected void RpcAsk_Use()
{
	// Validate request on server before changing state.
}
```

See `networking-multiplayer-replication.md`, `assets-weapons-vehicles-animation-audio.md`, and `examples-patterns.md`.

## Spawn An Entity Or Prefab

Task type: runtime entity creation.

Recipe:

1. Decide whether spawning a class or prefab is appropriate.
2. Load a prefab resource with `Resource.Load()` when using a prefab.
3. Create `EntitySpawnParams`.
4. Set transform/origin in spawn params.
5. Use `Game.SpawnEntityPrefab()` for prefab resources.
6. Validate authority rules in multiplayer.

Example:

```c
Resource resource = Resource.Load(m_sPrefab);
EntitySpawnParams params = new EntitySpawnParams();
params.TransformMode = ETransformMode.WORLD;
params.Transform[3] = owner.GetOrigin();
IEntity spawned = GetGame().SpawnEntityPrefab(resource, owner.GetWorld(), params);
```

See `resources-prefabs-configs.md` and `api-main.md`.

## Load A Resource Or Prefab

Task type: resource access.

Recipe:

1. Store paths as `ResourceName` when possible.
2. Use editor attributes to restrict picker type.
3. Load with `Resource.Load(ResourceName name)`.
4. Check for null.
5. Keep resource paths data-driven instead of hard-coded in behavior code.

Example:

```c
[Attribute("", UIWidgets.ResourceNamePicker, "Prefab", params: "et")]
ResourceName m_sPrefab;

Resource resource = Resource.Load(m_sPrefab);
if (!resource)
{
	PrintFormat("Missing resource %1", m_sPrefab);
	return;
}
```

See `resources-prefabs-configs.md`.

## Basic Replicated Or RPC Action

Task type: multiplayer state/action.

Recipe:

1. Decide whether the result is state (`RplProp`) or an event (`RplRpc`).
2. Mutate replicated state on authority.
3. Call `Replication.BumpMe()` after changing an `RplProp` if the system requires explicit dirty marking.
4. Use reliable RPC for important one-off actions.
5. Validate sender/target and authority before applying gameplay effects.
6. Test join-in-progress behavior when state must persist.

Example:

```c
[RplProp(onRplName: "OnEnabledChanged")]
protected bool m_bEnabled;

void SetEnabled(bool enabled)
{
	if (m_bEnabled == enabled)
		return;

	m_bEnabled = enabled;
	Replication.BumpMe();
}

void OnEnabledChanged()
{
	PrintFormat("Enabled replicated: %1", m_bEnabled);
}
```

See `networking-multiplayer-replication.md`.

## Create A Workbench Plugin Command

Task type: editor extension.

Recipe:

1. Put the plugin in the Workbench plugin script module layout.
2. Add `WorkbenchPluginAttribute`.
3. Declare target Workbench modules and resource filters.
4. Implement `Run()` for command execution.
5. Use module APIs to inspect editor/resource state.
6. Handle empty or invalid selection.

Example:

```c
[WorkbenchPluginAttribute("TAG Example", "Runs an example command", "", "", {"ResourceManager"})]
class TAG_ExampleWorkbenchPlugin : WorkbenchPlugin
{
	override void Run()
	{
		Print("TAG Example Workbench plugin ran");
	}
}
```

See `workbench-tools-debugging.md` and `api-main.md`.

## API Notes

- Recipes are entry points, not substitutes for exact API lookup.
- Verify every method signature in `api-main.md` or `api-extended.md` before committing code.
- Use `ResourceName` for editable resource paths.
- Use `IEntity` transform APIs only when direct transform mutation is appropriate for the entity type.
- Use `ScriptComponent` lifecycle callbacks instead of constructor-style setup for entity-attached behavior.
- Use `RplRpc` and `RplProp` only after deciding whether the need is a one-off event or persistent state.
- Use `WorkbenchPlugin` APIs only for editor commands.

## Review Checklist

- Does the recipe match the task surface?
- Has the code been adapted to the correct script module?
- Are editor attributes valid for the resource or value type?
- Are null resources and missing components handled?
- Is multiplayer authority explicit?
- Are event masks registered and cleared deliberately?
- Are expensive operations kept out of frame callbacks?
- Are sample patterns used for asset/resource tasks?
- Are exact signatures verified after adapting the recipe?

## Common Traps

- Treating these snippets as complete production systems.
- Using direct movement APIs for character, vehicle, or physics movement that has a domain-specific controller.
- Running authoritative gameplay changes on clients.
- Loading resources by raw string when an editable `ResourceName` field is better.
- Leaving frame events enabled after the task is complete.
- Calling `FindComponent()` repeatedly in hot paths.
- Forgetting `super` in overrides that must preserve base behavior.
- Confusing Workbench editor APIs with runtime game APIs.

## generated-pattern-from-docs: Recipe Verification Loop

```c
// 1. Pick the recipe.
// 2. Verify the exact API signature.
// 3. Adapt to the prefab/config/module in the project.
// 4. Test in the intended runtime context.
```

The recipes deliberately omit project-specific class names where the official docs require choosing context first, especially player/controller lookup and user actions.
