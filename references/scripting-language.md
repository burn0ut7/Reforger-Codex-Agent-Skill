# Scripting Language

## When to read this reference

Read for Enfusion Script syntax, types, arrays, classes, constructors/destructors, inheritance, `ref`, attributes, config objects, JSON, preprocessor/macros, and language-level traps before writing or reviewing Reforger scripts.

## Search terms

`Enforce Script`, `class`, `override`, `constructor`, `destructor`, `int`, `float`, `bool`, `string`, `vector`, `array`, `ref`, `Attribute`, `UIWidgets`, `BaseContainer`, `JsonApiStruct`, `#define`, `preprocessor`, `modded`

## Source authority summary

Use official scripting pages for syntax, values, conventions, automatic reference counting, config objects, JSON, and preprocessor behavior. Use extracted API data for exact generated types and signatures. Use samples for idiomatic class layout and project naming.

## Basic syntax retained from first-steps docs

- Statements end with semicolons.
- Casing matters: `Print` and `print` are different.
- `if`, `else`, `for`, and `foreach` follow C-like syntax.
- `=` assigns; `==` compares.
- Arrays are zero-indexed.
- Strings need quotes.
- Comments use `//` for line comments.

official-doc-example

```c
int health = 75;
if (health > 50)
	Print("Healthy!");
else
	Print("Need medical attention");
```

## Primitive and common values

Common value types from docs and API:

- `int`: whole numbers.
- `float`: decimal numbers.
- `string`: text.
- `bool`: true/false.
- `vector`: 3D value used for positions, directions, rotations, and some colors/offsets.
- `ResourceName`: string-like resource reference with resource semantics.

Use `PrintFormat` for formatted strings and escape literal percent signs with doubled `%` in format strings.

## Arrays and iteration

Arrays store values of the same type:

```c
array<string> soldiers = {"Alpha", "Bravo", "Charlie"};
Print(soldiers[0]);
soldiers.Insert("Delta");
Print("Squad size: " + soldiers.Count());
```

Use `foreach` with or without index:

```c
foreach (string soldier : soldiers)
{
	Print(soldier);
}

foreach (int i, string soldier : soldiers)
{
	PrintFormat("%1: %2", i, soldier);
}
```

Use maps/sets only after checking project/API examples. Prefer matching existing project containers.

## Classes, inheritance, and overrides

Class syntax is C-like:

```c
class TAG_Example
{
	protected int m_iValue;

	void SetValue(int value)
	{
		m_iValue = value;
	}
}
```

For inheritance:

```c
class TAG_Component : ScriptComponent
{
	override protected void EOnInit(IEntity owner)
	{
		super.EOnInit(owner);
	}
}
```

Before using `override`, verify:

- Base class actually has the method.
- Return type and parameters match exactly.
- Qualifiers such as `protected`, `static`, `out`, `inout`, `notnull`, `ref`, and array dimensions are correct.
- Calling `super` is appropriate for that callback.

Constructors and destructors use class-name syntax. Generated/proto classes may have private constructors/destructors, so do not instantiate engine-managed classes unless API docs support it.

## Automatic reference counting and `ref`

Use `ref` for owned managed objects that need automatic reference-counting ownership, such as arrays of object references:

```c
protected ref array<IEntity> m_aNearbyCharacters;

protected override void OnPostInit(IEntity owner)
{
	m_aNearbyCharacters = {};
}
```

Component tutorial uses `protected ref array<ref Shape> m_aShapes;` for debug shape references. Preserve `ref` on object arrays when the object lifetime must be owned by the component.

Traps:

- Do not keep references to deleted entities/components without validity checks.
- Do not access owner from component destructor; the lifecycle docs warn the entity is already deleted by then.
- Do not delete child components manually from an entity destructor.

## Attributes and editor serialization

Use `[Attribute]` to expose fields in Workbench/World Editor/prefab data. Common documented arguments include:

- `defvalue`: default string value.
- `desc`: field description.
- `params`: widget constraints such as min/max/step.
- `category`: grouping in the editor UI.
- `UIWidgets.*`: widget selection where needed.
- Resource extension filters for resource pickers.

official-doc-example

```c
[Attribute(defvalue: "2", desc: "Trigger radius", params: "0.25 10 0.25", category: "Teleportation")]
protected float m_fTriggerRadius;

[Attribute("", UIWidgets.ResourceNamePicker, "Prefab to spawn", "et")]
protected ResourceName m_PrefabToSpawn;
```

Attribute defaults are serialized as strings. Make the default parseable for the target type.

## Config objects and BaseContainer

Config work is often data-first. Use config classes/objects when the source workflow expects `.conf` resources rather than hard-coded values.

Guidelines:

- Keep config classes stable once resources reference them.
- Use `BaseContainer`/config helpers according to the current API and project examples.
- Guard missing resources, missing fields, and failed casts.
- Preserve defaults for missing fields rather than crashing where possible.
- Keep config resource references as `ResourceName` or typed config object fields, not arbitrary strings unless the API expects strings.

generated-pattern-from-docs

```c
[Attribute("", UIWidgets.ResourceNamePicker, "Config resource", "conf")]
protected ResourceName m_ConfigResource;

void LoadConfig()
{
	if (m_ConfigResource == ResourceName.Empty)
	{
		Print("Missing config resource", LogLevel.WARNING);
		return;
	}

	// Verify BaseContainerTools/API usage before using in project code.
}
```

## JSON usage

Use JSON only when a wiki/source page or existing project code supports it for the task. `JsonApiStruct` and related serialization APIs are useful for structured data, but not every gameplay/config problem should become JSON.

Use JSON for:

- External data interchange where Reforger docs/project code already use JSON.
- Tooling/debug files where runtime config resources are not the intended solution.

Avoid JSON for:

- Prefab/component/editor data that belongs in `.et`/`.conf`.
- Multiplayer state that belongs in replicated properties or server authority.
- Dedicated-server secrets unless the server config docs define that field and storage pattern.

## Preprocessor and macros

Use preprocessor directives for narrow compile-time toggles, debug instrumentation, and source-supported macros. The entity lifecycle example uses:

```c
#define _PRINT_EVENTS
// #define _WB_WORLD_UPDATES
```

Then wraps event logging in `#ifdef _PRINT_EVENTS`. This is useful for temporary diagnostic builds.

Risks:

- Macros can hide method signatures and make API verification harder.
- Debug defines can accidentally ship noisy behavior.
- Conditional code can compile in one module/context and fail in another if dependencies differ.
- Prefer explicit code unless matching existing project macro patterns.

## Common language examples

generated-pattern-from-docs

```c
class TAG_DebugUtility
{
	static void Trace(string scope, string message)
	{
		PrintFormat("[%1] %2", scope, message);
	}
}
```

generated-pattern-from-docs

```c
protected ref array<ResourceName> m_aPrefabs = new array<ResourceName>();

void AddPrefab(ResourceName name)
{
	if (name == ResourceName.Empty)
		return;

	m_aPrefabs.Insert(name);
}
```

## API Notes

Use `api-main.md` for common generated types, `ResourceName`, `BaseContainer`, `Resource`, component/entity signatures, and Workbench plugin attribute shapes. Use `api-extended.md` for specialized generated containers, JSON helpers, proto types, and exact attribute constructors.

## Common Traps

- Incorrect casing or missing semicolon.
- Using `=` inside a condition where `==` was intended.
- Assuming arrays are one-indexed.
- Forgetting `ref` for owned managed objects.
- Treating serialized `[Attribute]` fields as safe to rename.
- Using JSON when Reforger config/prefab data is the correct surface.
- Leaving diagnostic preprocessor defines enabled in normal builds.

## Review Checklist

- Are type names and qualifiers verified?
- Are `ref` ownership and object lifetime safe?
- Are attributes tied to real editor/config needs?
- Are config/JSON failures guarded?
- Are macros/preprocessor uses justified and easy to remove?

## Type And Lifetime Detail

- Prefer explicit types in examples because Enfusion script errors are easier to read when the type is visible.
- Use `ref` for owned managed object references that need reference-counted lifetime semantics.
- Avoid storing borrowed references longer than the owner relationship guarantees.
- Arrays of managed objects should make ownership expectations clear.
- Passing objects into callbacks does not automatically make them safe to store forever.
- When a field is serialized by prefab/config data, renaming it can break existing saved resources.
- Treat field renames as data migrations, not cosmetic cleanup.

## Class And Inheritance Detail

- Use class pairs for components: `NameComponentClass` and `NameComponent`.
- Use `extends` for normal inheritance and `modded class` for extending existing loaded classes.
- Keep access modifiers deliberate; avoid exposing helper state as public because it is easier in a snippet.
- Override signatures must match exactly.
- Constructors are not a substitute for entity lifecycle callbacks on components.
- Static helpers should not hide world/entity/authority context.
- Use creator tags in class names when the project convention requires avoiding collisions.

## Attribute And Serialization Detail

- `[Attribute]` values become part of designer-facing serialized data.
- Default values should be valid enough for a new component instance to fail clearly.
- Resource picker `params` should match the resource family, such as entity prefab resources.
- Use check boxes for booleans and resource pickers for paths instead of free text when possible.
- Keep display names/descriptions stable enough for Workbench users.
- Validate loaded values at runtime because editor widgets constrain input but do not prove dependencies exist.
- Do not store player-facing localized text directly in script when localization resources are appropriate.

## Config And JSON Detail

- Use config/BaseContainer patterns for engine/game data where the Reforger systems expect config data.
- Use JSON for external/simple data only when it fits the task and is not replacing a native config surface.
- Always handle missing fields, malformed input, and absent resources.
- Keep config parsing separate from gameplay state mutation where possible.
- Avoid parsing large data repeatedly in frame callbacks.
- Log enough context to identify which config/resource failed.
- Treat config schema changes as compatibility changes for existing content.

## Preprocessor Detail

- Use preprocessor flags for diagnostics and conditional compilation only when necessary.
- Keep debug-only code easy to remove or disable.
- Do not hide required gameplay behavior behind local defines.
- Do not leave profiling or diagnostic defines enabled in normal addon output.
- Prefer runtime settings/config for user-facing behavior switches.
- Keep macro names namespaced enough to avoid collisions.
- Re-check compiled output when a macro changes callback signatures or attribute declarations.

## Syntax Review Detail

- Check array types and initialization syntax before adapting examples.
- Check enum names against the generated API rather than guessing.
- Check `typename` use when passing class/type identifiers.
- Check `notnull` annotations and guard code accordingly.
- Check whether a function expects `out` parameters.
- Check string formatting before using values in logs.
- Check vector literals and transform arrays for correct semantic meaning.
- Check casts from `Managed` or component lookups before dereferencing.
- Check method visibility when overriding protected base callbacks.
- Check whether a helper should be static, instance, or component-owned.
- Check whether a field needs `[Attribute]` or should remain internal.
- Check whether a serialized field needs a default value compatible with existing prefabs.
- Check whether JSON/config parsing can fail without crashing the feature.
- Check whether preprocessor conditions hide code needed by release builds.
- Check whether a code sample is pseudocode before treating it as exact syntax.
- Check exact function signatures in `api-main.md` or `api-extended.md`.
- Check whether source examples use project-specific `SCR_` classes.
- Check whether copied code needs creator tag replacement.
- Check whether ownership requires `ref`.
- Check whether object lifetime depends on entity lifecycle.
