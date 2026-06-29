# Main API Quick Reference

Use this file before searching the extended API index. It collects high-frequency classes, methods, attributes, and signatures used across common Arma Reforger modding tasks. For exhaustive lookup, use `api-extended.md`.

## IEntity

Core entity API used by almost every runtime script.

Common transform methods:

```c
proto external vector GetOrigin();
proto external void SetOrigin(vector orig);
proto external void GetTransform(out vector mat[]);
proto external bool SetTransform(vector mat[4]);
proto external void GetWorldTransform(out vector mat[]);
proto external bool SetWorldTransform(vector mat[4]);
proto external void GetLocalTransform(out vector mat[]);
proto external void SetLocalTransform(vector mat[4]);
proto external vector GetYawPitchRoll();
proto external void SetYawPitchRoll(vector angles);
```

Common component/event methods:

```c
proto external Managed FindComponent(typename typeName);
proto external int FindComponents(typename typeName, notnull array<Managed> outComponents);
proto external EntityEvent SetEventMask(EntityEvent e);
proto external EntityEvent ClearEventMask(EntityEvent e);
```

Usage notes:

- Use `GetOrigin()` for simple position reads.
- Use full transform matrices when rotation/orientation/scale matter.
- Keep local/world transform space explicit.
- Use `FindComponent()` sparingly in hot paths; cache component references where lifecycle permits.
- Register only the event masks needed by callbacks.

## ScriptComponent

Base class for scripted components attached to entities.

Common methods and callbacks:

```c
proto external GenericEntity GetOwner();
override void EOnInit(IEntity owner);
override void OnPostInit(IEntity owner);
override void EOnFrame(IEntity owner, float timeSlice);
override void EOnDiag(IEntity owner, float timeSlice);
bool RplLoad(ScriptBitReader reader);
```

Usage notes:

- `EOnInit` receives the owner and is the normal place for owner-dependent setup.
- `OnPostInit` is useful when setup depends on already-created components.
- `EOnFrame` requires the frame event mask.
- Avoid per-frame component discovery and log spam.
- Replication-specific serialization belongs with replication-aware code, not generic component setup.

## GenericComponent Helpers

Component helper methods commonly used from component code:

```c
proto external void SetEventMask(notnull IEntity owner, int mask);
proto external void ClearEventMask(notnull IEntity owner, int mask);
proto external Managed FindComponent(typename typeName);
proto external int FindComponents(typename typeName, notnull array<Managed> outComponents);
```

Usage notes:

- Component event mask helpers require the owner entity.
- Prefer owner-passed callbacks over calling `GetOwner()` repeatedly when the callback already has `owner`.

## ComponentEditorProps

Class annotation used to expose component metadata to Workbench.

Typical shape:

```c
[ComponentEditorProps(category: "GameScripted/MyAddon", description: "Description")]
class TAG_ComponentClass : ScriptComponentClass
{
}
```

Usage notes:

- Keep category paths stable.
- Use meaningful descriptions for editor users.
- Do not treat editor metadata as runtime validation.

## Attribute

Field annotation used to expose configurable values.

Common examples:

```c
[Attribute("1.0", UIWidgets.EditBox, "Multiplier")]
float m_fMultiplier;

[Attribute("", UIWidgets.ResourceNamePicker, "Prefab", params: "et")]
ResourceName m_sPrefab;

[Attribute("1", UIWidgets.CheckBox, "Enabled")]
bool m_bEnabled;
```

Usage notes:

- Use `ResourceNamePicker` and `params` to restrict resource selection.
- Keep default values valid.
- Validate at runtime before using designer-entered values.

## ResourceName And Resource

Resource references and loading.

Common API:

```c
string GetPath();
bool IsExternal();
bool IsInternal();
static Resource Load(ResourceName name);
```

Usage notes:

- Prefer `ResourceName` fields over raw strings for resource paths.
- Use Workbench picker attributes for editable resource references.
- Check loaded resources for null before spawning or reading.

## Game Spawning

Common spawn methods:

```c
IEntity SpawnEntity(typename typeName, BaseWorld world = null, EntitySpawnParams params = null);
IEntity SpawnEntityPrefab(notnull Resource templateResource, BaseWorld world = null, EntitySpawnParams params = null);
```

Usage notes:

- Use `SpawnEntityPrefab()` for prefab resources.
- Use `EntitySpawnParams` to set transform and placement behavior.
- In multiplayer, spawn authoritative gameplay entities on the server/authority.
- Do not hard-code resource paths when editor data can supply them.

## Replication Attributes And Functions

RPC declaration:

```c
void RplRpc(RplChannel channel, RplRcver rcver, RplCondition condition = RplCondition.None, string customConditionName = "");
```

Common state/event pattern:

```c
[RplProp(onRplName: "OnValueChanged")]
protected int m_iValue;

[RplRpc(RplChannel.Reliable, RplRcver.Server)]
protected void RpcAsk_DoThing()
{
}
```

Common replication helpers:

```c
Replication.BumpMe();
bool RplSave(ScriptBitWriter writer);
bool RplLoad(ScriptBitReader reader);
```

Usage notes:

- Use `RplProp` for state that join-in-progress clients need.
- Use RPC for one-off events or requests.
- Mutate authoritative state on authority, not on proxy clients.
- Validate sender and gameplay permission on server-side RPC handlers.
- Use custom codecs only when default property replication is insufficient.

## BaseRplComponent

Replication-aware component base used by many networked entities.

Usage notes:

- Check authority/proxy role before applying gameplay state.
- Use owner/controller ownership deliberately for client requests.
- Do not assume local player context exists on a dedicated server.
- Pair replicated state with explicit callbacks when clients must react visually.

## WorkbenchPlugin

Base class for Workbench plugins.

Common methods:

```c
override void Run();
override void RunCommandline();
override void Configure();
override void OnResourceContextMenu(notnull array<ResourceName> resources);
```

Plugin attribute shape:

```c
WorkbenchPluginAttribute(
	string name,
	string description = "",
	string shortcut = "",
	string icon = "",
	array<string> wbModules = null,
	string category = "",
	int awesomeFontCode = 0,
	array<string> resourceTypes = null
)
```

Usage notes:

- Use Workbench plugins only for editor behavior.
- Declare module dependencies such as Resource Manager, Script Editor, or World Editor.
- Narrow context-menu resource types where possible.
- Handle invalid selection and missing module state.

## InputManager

Game input manager type.

Common relationship:

```c
class InputManager : ActionManager
```

Common access:

```c
InputManager GetInputManager();
```

Usage notes:

- Use project-local input/action patterns before adding new input logic.
- Keep client-only input separate from server authority changes.

## ScriptEditor

Workbench Script Editor API is useful for editor plugins, not runtime gameplay.

Common methods:

```c
string GetCurrentFile();
int GetCurrentLine();
string GetLineText(int line);
void SetLineText(int line, string text);
```

Usage notes:

- Use from Workbench plugin code loaded with Script Editor module access.
- Validate file and line state before editing text.

## WorkspaceWidget

UI layout creation helper.

Common method:

```c
Widget CreateWidgets(ResourceName layoutResourceName, Widget parentWidget = NULL);
```

Usage notes:

- Store layout paths as `ResourceName`.
- Keep UI layout resources separate from gameplay logic.
- Validate widget creation before dereferencing child widgets.

## Print And PrintFormat

Common debug output:

```c
Print("Message");
PrintFormat("Value %1", value);
```

Usage notes:

- `PrintFormat` placeholders use `%1`, `%2`, and so on.
- Escape literal percent signs as `%%`.
- Do not leave high-frequency frame logs in finished code.

## Query And Discovery Reminder

When this file is not enough:

1. Search `api-extended.md` for exact class or method names.
2. Check the dense topical reference for lifecycle/networking/resource context.
3. Use official samples for resource and prefab shape.
4. Prefer verified signatures over memory.

## Additional Core Terms

`GenericEntity`

Signature:

```c
class GenericEntity : IEntity
```

Usage notes:

- Many script APIs return `GenericEntity` for an entity owner or concrete entity object.
- Treat it as an entity handle; inspect components and transforms through entity/component APIs.

`GenericEntityClass`

Signature:

```c
class GenericEntityClass : IEntitySource
```

Usage notes:

- Class metadata for generic entity definitions.
- Usually appears around entity type declarations rather than gameplay logic.

`GenericComponent`

Signature:

```c
class GenericComponent : Managed
```

Usage notes:

- Base component functionality for component discovery and event mask helpers.
- `ScriptComponent` builds on component behavior for script-defined components.

`GenericComponentClass`

Signature:

```c
class GenericComponentClass : Managed
```

Usage notes:

- Class metadata for components.
- Pair script components with their `ScriptComponentClass` subclasses unless using engine-provided component classes.

`Game`

Signature:

```c
class Game
```

Usage notes:

- Game-level services include spawning and input access.
- Use project-specific game subclasses when nearby code does so.

`WorldEditor`

Signature:

```c
class WorldEditor
```

Usage notes:

- Workbench World Editor API surface for editor plugins/tools.
- Do not call World Editor APIs from runtime gameplay code.

`ResourceManager`

Signature:

```c
class ResourceManager
```

Usage notes:

- Workbench Resource Manager API surface for resource-oriented plugins.
- Use it to inspect or operate on resources in editor context.

`OnRpl`

Signature:

```c
[RplProp(onRplName: "OnRpl_Value")]
protected int m_iValue;

void OnRpl_Value()
{
}
```

Usage notes:

- `OnRpl` is a naming convention often used for replication callbacks.
- The callback name must match the `onRplName` attribute value.
- Put client-side visual/state reaction in the callback; keep authoritative mutation on the authority.

## Signature Index

- Signature: `vector IEntity.GetOrigin()`
- Signature: `void IEntity.SetOrigin(vector orig)`
- Signature: `void IEntity.GetTransform(out vector mat[])`
- Signature: `bool IEntity.SetTransform(vector mat[4])`
- Signature: `void IEntity.GetWorldTransform(out vector mat[])`
- Signature: `bool IEntity.SetWorldTransform(vector mat[4])`
- Signature: `vector IEntity.GetYawPitchRoll()`
- Signature: `void IEntity.SetYawPitchRoll(vector angles)`
- Signature: `Managed IEntity.FindComponent(typename typeName)`
- Signature: `int IEntity.FindComponents(typename typeName, notnull array<Managed> outComponents)`
- Signature: `GenericEntity ScriptComponent.GetOwner()`
- Signature: `void ScriptComponent.EOnInit(IEntity owner)`
- Signature: `void ScriptComponent.OnPostInit(IEntity owner)`
- Signature: `void ScriptComponent.EOnFrame(IEntity owner, float timeSlice)`
- Signature: `Resource Resource.Load(ResourceName name)`
- Signature: `IEntity Game.SpawnEntityPrefab(Resource templateResource, BaseWorld world, EntitySpawnParams params)`
- Signature: `void RplRpc(RplChannel channel, RplRcver rcver, RplCondition condition, string customConditionName)`
- Signature: `void WorkbenchPlugin.Run()`
- Signature: `void WorkbenchPlugin.Configure()`
- Signature: `void WorkbenchPlugin.OnResourceContextMenu(notnull array<ResourceName> resources)`
- Signature: `Widget WorkspaceWidget.CreateWidgets(ResourceName layoutResourceName, Widget parentWidget)`

## Review Checklist

- Is the exact class or method present in this file?
- If not, was `api-extended.md` searched?
- Is the code using runtime APIs in runtime modules and Workbench APIs in editor modules?
- Are replication attributes paired with authority checks?
- Are resource APIs paired with null checks?
- Are transform APIs appropriate for the entity type?

## Common Traps

- Copying a signature from memory when generated API data exists.
- Calling Workbench APIs in game runtime scripts.
- Treating `RplProp` callbacks as authority-side mutation hooks.
- Using direct transform setters on controlled characters or simulated vehicles without checking the domain system.
- Assuming `Resource.Load()` success.
- Storing resource paths as raw strings in designer-facing components.

## generated-pattern-from-docs: API Verification

```c
// Search api-main.md first for common signatures.
// Search api-extended.md for exact generated classes, inherited methods, and uncommon APIs.
// Then adapt code to the lifecycle, data, and multiplayer reference for the task.
```
