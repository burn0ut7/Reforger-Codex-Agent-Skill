# Scripting Core

## When to read this reference

Read for Enfusion Script file placement, modded classes, logging, Remote Console use, `ScriptInvoker`, event/callback patterns, profiling, and performance-conscious scripting.

## Search terms

`Scripts/Game`, `Script Editor`, `Remote Console`, `Print`, `PrintFormat`, `LogLevel`, `modded class`, `override`, `super`, `ScriptInvoker`, `EOnFrame`, `SetEventMask`, `Script Profiling`, `Shift F7`

## Source authority summary

The scripting first-steps wiki page defines Remote Console and basic print/format behavior. Component and lifecycle pages define script module placement and event-mask requirements. Sample mod scripts show real project folders and modded class organization. Extracted API data verifies callback signatures.

## Workbench and Remote Console workflow

1. Install Arma Reforger Tools from Steam.
2. Launch Enfusion Workbench from Steam.
3. Open Script Editor from the Workbench icon/menu.
4. Open the Remote Console and Output tabs at the bottom of Script Editor if they are hidden.
5. For simple expressions, run code directly from Remote Console; basic exercises do not require loading a world or running the game.
6. For class/module changes, save files, compile/reload scripts, and verify in Workbench/game. Component pages specifically call out reloading via `Shift+F7` to make newly compiled components appear in World Editor.

Remote Console is good for `Print`, math, arrays, loops, and small diagnostics. It is not enough to validate prefab wiring, lifecycle callbacks, replication, or server behavior.

## File and module placement

- Runtime gameplay scripts belong in the Game script module, commonly under `Scripts/Game/...`.
- A script component that should appear in World Editor Add Component lists must be in the Game module; otherwise World Editor will not list it.
- Workbench plugins and tools belong in Workbench/editor modules such as `Scripts/WorkbenchGame/...`.
- Keep creator tag prefixes consistent with the project and sample convention. Examples often use `TAG_` for tutorial code and `SCR_` for shipped Reforger systems.
- Match file name to the primary class where the project convention expects it. Component tutorial uses `TAG_TeleportFieldComponent.c` for `TAG_TeleportFieldComponent`.

## Logging and print details

`Print("text");` writes to the log/output. `PrintFormat` substitutes `%1`, `%2`, etc. from later arguments.

```c
Print("Hello there!");
PrintFormat("Hello %1, welcome to %2!", "there", "Arma Reforger");
```

Percent signs are special in `PrintFormat`. Use doubled percent signs when the output should contain a literal percent:

```c
Print("5%");              // prints 5%
PrintFormat("5%%");       // prints 5%
PrintFormat("%1%%", 5);   // prints 5%
```

Use log levels when the API/project convention supports them:

```c
Print("Normal diagnostic", LogLevel.NORMAL);
Print("Potential setup issue", LogLevel.WARNING);
Print("Fatal setup issue", LogLevel.ERROR);
```

Avoid logging every `EOnFrame` unless profiling a short-lived issue. Frame logs can bury real errors and affect runtime behavior.

## Modded class workflow

Use `modded class` when extending an existing class without replacing the original file. Before writing the override:

1. Search the target project and API for the exact base class.
2. Verify the method is overridable/event/virtual and copy the signature exactly.
3. Call `super` unless the task intentionally replaces behavior and the source pattern supports skipping it.
4. Keep the modded class in the appropriate script module.
5. Test compile and the actual workflow that triggers the override.

official-sample-excerpt

```c
modded class SCR_BaseScoringSystemComponent
{
	override void SomeExistingCallback()
	{
		super.SomeExistingCallback();
		Print("Scoring callback reached");
	}
}
```

Do not use the placeholder callback name above without verifying a real signature in the target project/API.

## Event and callback registration

Prefer event callbacks and system-specific invokers over polling. If polling is required, register the event mask that enables the callback and make the frame work small.

From the component/lifecycle docs:

- Some entity/component event methods are called only when events were enabled through event masks.
- Some events also require engine conditions, such as valid and activated physics.
- `EOnFrame` runs every drawing frame.
- `EOnFixedFrame` is tied to a fixed 30 Hz event.
- physics simulation can run at 60 simulations per second and can execute multiple times per drawing frame.

Use `SetEventMask(owner, EntityEvent.FRAME)` on components when enabling `EOnFrame`; verify exact enum names in `api-main.md` or `api-extended.md`.

## ScriptInvoker pattern

Use `ScriptInvoker` when other code needs to subscribe to changes without polling.

generated-pattern-from-docs

```c
protected ref ScriptInvoker m_OnChanged = new ScriptInvoker();

ScriptInvoker GetOnChanged()
{
	return m_OnChanged;
}

protected void NotifyChanged()
{
	m_OnChanged.Invoke();
}
```

Subscription guidance:

- Expose an accessor rather than public mutable invoker state unless the project already does otherwise.
- Subscribe in lifecycle points where both publisher and subscriber exist.
- Unsubscribe when the subscriber can be deleted before the publisher.
- Do not invoke from constructors when listeners are not attached yet.

## Basic language reminders from first-steps docs

- Casing matters: `Print` is not `print`.
- Statements need semicolons.
- Use `==` for comparison and `=` for assignment.
- Arrays are zero-based.
- Strings require quotes.
- `foreach (int i, string item : items)` gets index and item.

official-doc-example

```c
array<string> soldiers = {"Alpha", "Bravo", "Charlie"};
soldiers.Insert("Delta");
Print("Squad size: " + soldiers.Count());

foreach (int i, string soldier : soldiers)
{
	PrintFormat("%1: %2", i, soldier);
}
```

## Profiling and performance workflow

Use Script Profiling/diagnostic tooling before changing algorithms blindly. For a hot path:

1. Reproduce the behavior with logs disabled or minimized.
2. Enable profiling or targeted diagnostics.
3. Identify the script callback or system with real cost.
4. Reduce frequency first: replace frame polling with event callbacks or fixed checks where possible.
5. Cache resource/config lookups that do not need to be repeated every frame.
6. Keep per-frame allocations low; reuse arrays where safe.
7. Re-test with profiling after the change.

The teleport-field component tutorial checks nearby entities every `m_fCheckPeriod`, not on every frame, by decrementing a delay and querying only when the period elapses. That pattern is preferable to doing expensive queries every frame.

## API Notes

Check `api-main.md` for `Print`, `LogLevel`, `ScriptComponent`, `GenericComponent.SetEventMask`, `IEntity.GetOrigin`, `IEntity.SetOrigin`, `Game`, and Workbench plugin basics. Use `api-extended.md` for specialized callback names, sample-derived classes, and generated systems.

## Common Traps

- Creating a component outside the Game module and wondering why Add Component cannot find it.
- Forgetting `Shift+F7` or equivalent script reload after adding classes.
- Copying wiki/tutorial code with placeholder creator tags or method names.
- Spamming `Print` in `EOnFrame`.
- Overriding a method with a slightly wrong signature.
- Treating Remote Console success as evidence that a class, prefab, or multiplayer flow works.

## Review Checklist

- Is the script in the correct module?
- Are class names, file names, creator tag, and suffixes consistent?
- Are overrides and callbacks signature-verified?
- Are logs gated or temporary?
- Is polling justified and event mask usage correct?

## Workbench Execution Detail

- Use the Script Editor for normal script editing and compile feedback.
- Use Workbench game launch when prefab, component, world, or input context matters.
- Use Remote Console for fast script execution and inspection, but treat it as a diagnostic surface.
- Use the console to test small expressions, not to prove that prefab serialization or multiplayer behavior is correct.
- Keep script reload expectations explicit; a reload can compile code but cannot always repair already-spawned entity state.
- When a class does not appear in Add Component, check module placement, class suffix, class metadata, and compile errors before changing code shape.
- When a method override does not fire, verify the exact callback signature in the API reference before changing lifecycle logic.
- When a log does not appear, confirm the code path, authority role, event mask registration, and module load state.

## Script Module Placement Detail

- Game runtime script belongs in game/runtime script modules, not Workbench plugin modules.
- Workbench plugin script belongs in the Workbench script module layout.
- Shared helper code must be visible to the module that consumes it.
- A class can compile in one context and still be unavailable in another if the module boundary is wrong.
- Component classes need the paired `ScriptComponentClass` subclass for editor-facing component definitions.
- Modded classes must be compiled into a module that loads after or alongside the class being modified.
- Do not resolve module mistakes by duplicating classes; fix the module ownership.

## Modded Class Detail

- Use `modded class` only when extending an existing class.
- Use `override` only when the base class has the method with the same signature.
- Call `super` when base behavior initializes state, dispatches events, updates replication, or performs cleanup.
- Skip `super` only when intentionally replacing the base behavior and after checking side effects.
- Avoid broad modded overrides for data changes that a prefab/config can handle.
- Keep modded behavior small and documented because multiple mods can target the same class.
- Test modded class changes in the actual game context where the base class is constructed.

## Diagnostic Logging Detail

- `PrintFormat` placeholders are ordinal and start at `%1`.
- Literal percent signs need escaping as `%%`.
- Logs in `EOnFrame` should be temporary, throttled, or gated by diagnostics.
- Authority-role logs should include role information when debugging replication.
- Resource logs should include the resource path and whether loading returned null.
- Component logs should include owner and class name.
- Workbench plugin logs should include module/selection context.

## Event And Polling Detail

- Register `EntityEvent.FRAME` only when frame work is needed.
- Clear frame masks when work is complete.
- Prefer event/callback-driven behavior over repeated polling.
- Avoid expensive entity queries in `EOnFrame`.
- Cache component references after lifecycle setup if the owner graph is stable.
- Revalidate cached references if the entity can be deleted, replaced, or reconfigured.
- Keep diagnostic `EOnDiag` behavior separate from gameplay updates.

## Failure Triage Detail

- Compile error first: fix syntax, type names, includes/module visibility, and override signatures.
- Editor visibility second: check component class metadata, category, and module placement.
- Runtime no-op third: check lifecycle callback execution, event masks, and owner references.
- Data no-op fourth: check prefab/config/resource wiring in Workbench.
- Multiplayer no-op fifth: check authority, owner, streaming, and RPC receiver.
- Packaging no-op sixth: check addon metadata, dependency order, and server/client mod load state.

## Code Review Detail

- Check every `override` against a verified base signature.
- Check every `modded class` target exists in the current API/source set.
- Check every `PrintFormat` call for correct placeholder count.
- Check every resource load for a null branch.
- Check every component lookup for a null branch unless the owner contract guarantees it.
- Check every frame callback for bounded cost.
- Check every callback registration for a matching reason.
- Check every persistent field for serialization consequences.
- Check every helper class for correct module visibility.
- Check every Workbench-only type for accidental runtime use.
- Check every runtime type for accidental Workbench plugin coupling.
- Check every user action or input path for authority handoff.
- Check every spawned entity for world, transform, and resource validity.
- Check every script-facing UI path for dedicated-server separation.
- Check every sample-derived class name for project tag replacement.
- Check every debug define for removal before release.
- Check every scripted component against prefab Add Component visibility.
- Check every data-first task for unnecessary script.
- Check every script-first task for missing data/prefab integration.
- Check every public method for whether it should be protected or private.
- Check every static cache for world/session lifetime assumptions.
- Check every timer or delayed callback for entity deletion safety.
- Check every array traversal for mutation during iteration.
- Check every event subscription for unsubscribe/cleanup needs.
- Check every log message for enough context to triage failures.
- Check every runtime answer for a compile and in-Workbench verification step.
- Check every multiplayer answer for at least host/client verification.
- Check every server answer for dedicated-server log verification.
- Check every packaging answer for declared addon dependency verification.

## Runtime Context Detail

- Identify whether the code runs in editor preview, local game, listen server, client, or dedicated server.
- Identify whether the code path depends on player input.
- Identify whether the code path depends on UI widgets.
- Identify whether the code path depends on world placement.
- Identify whether the code path depends on prefab serialization.
- Identify whether the code path depends on a loaded scenario.
- Identify whether the code path depends on addon dependency order.
- Identify whether the code path depends on replicated identity.
- Identify whether the code path depends on streamed proxy presence.
- Identify whether the code path depends on Workbench-only modules.
- Separate debug convenience from shipped behavior.
- Separate editor-only validation from runtime validation.
- Separate server mutation from client presentation.
- Separate resource lookup from gameplay execution.
- Separate sample structure from exact API signatures.
- State the minimum verification environment in the answer.
- State when Remote Console is insufficient.
- State when a clean profile test is required.
- State when a dedicated server test is required.
- State when a Workbench prefab save/reopen check is required.
- State when a multiplayer two-peer test is required.
- State when a Workshop/package test is required.
- State when script compile alone is enough for the requested change.

## Minimal Verification Matrix

- New script class: compile, reload scripts, instantiate or call in intended context.
- New component: compile, Add Component visibility, prefab save/reopen, runtime launch.
- Modded class: compile, base behavior still runs when required, target context reaches override.
- Logging change: compile and verify log appears only at intended frequency.
- Resource-loading code: compile, valid resource path, invalid resource path, clean profile.
- User action: compile, host use, client use, authority validation.
- Spawn code: compile, valid prefab, failed load branch, server/client observation.
- Workbench helper: compile in Workbench module, plugin discovery, selection/context guard.
- Server-facing code: compile, dedicated startup, server log, client join.
- Packaged addon: clean profile, declared dependency load, published-resource availability.
- Multiplayer state: host/client mutation, proxy observation, join-in-progress state.
- Performance-sensitive code: profiling or bounded test with representative entity count.
- UI code: client context, missing widget guard, no dedicated-server dependency.
- Scenario code: scenario start, restart, client join after start.
- Asset integration code: prefab resource graph and runtime behavior both verified.
- Cleanup code: deletion path and delayed-callback safety verified.
- Event-mask code: registration, callback execution, and clear path verified.
- API-sensitive code: exact signature checked in `api-main.md` or `api-extended.md`.
- Sample-derived code: sample structure preserved and project-specific names replaced.
