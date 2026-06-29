# Workbench Tools Debugging

## When to read this reference

Read for Workbench plugins, World Editor tools, Resource Manager/Script Editor/String Editor integration, editor-only automation, dialogs, context-menu plugins, diagnostics, log console, profiling, and destructive editor actions.

## Search terms

`WorkbenchPlugin`, `WorkbenchPluginAttribute`, `WorkbenchToolAttribute`, `Run`, `RunCommandline`, `Configure`, `OnResourceContextMenu`, `ResourceManager`, `ScriptEditor`, `LocalizationEditor`, `WorldEditor`, `WorldEditorTool`, `BeginEntityAction`, `EndEntityAction`, `ScriptDialog`, `ButtonAttribute`, `Log Console`, `Script Profiling`

## Source authority summary

Workbench plugin docs define the editor/plugin API, naming rules, module mapping, CLI entry points, and dialog behavior. The Workbench plugin tutorial and official `SampleMod_WorkbenchPlugin` show Resource Manager, Script Editor, Localization/String Editor, World Editor plugin, and World Editor tool patterns. Extracted API data verifies exact class/method signatures.

## Plugin and module placement

Workbench plugins are script files triggered from editors such as Resource Browser/Resource Manager, World Editor, Script Editor, and String Editor. Existing plugins are organized under WorkbenchGame editor directories.

Module mapping retained from docs:

| Editor | Typical WorkbenchGame directory | Module/API class |
| --- | --- | --- |
| Common plugins | WorkbenchGame root/common area | N/A |
| Resource Manager | `Scripts/WorkbenchGame/ResourceManager` or project subfolder | `ResourceManager` |
| World Editor tools/plugins | `Scripts/WorkbenchGame/WorldEditor` or project subfolder | `WorldEditor` |
| Script Editor | `Scripts/WorkbenchGame/ScriptEditor` or project subfolder | `ScriptEditor` |
| String Editor | `Scripts/WorkbenchGame/LocalizationEditor` or project subfolder | `LocalizationEditor` |

Project plugins should live under `Scripts/WorkbenchGame`, often in a subfolder such as `SamplePlugins` to keep the structure clear.

Naming rules:

- A plugin class and file should be named `ClassnamePlugin`.
- A tool class and file should be named `ClassnameTool`.
- Resource Manager/Script Editor/String Editor/World Editor examples all use `WorkbenchPluginAttribute`.
- World Editor tools use `WorkbenchToolAttribute` and inherit `WorldEditorTool`.

## WorkbenchPluginAttribute details

Signature from docs/API:

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

Important parameters:

- `name`: mandatory display name.
- `description`: hover/current-tool description; especially relevant for World Editor tools.
- `shortcut`: text shortcut such as `Ctrl+G` or `Ctrl+Shift+I`.
- `icon`: custom PNG icon; docs recommend `awesomeFontCode` instead where possible.
- `wbModules`: list of editor modules where the plugin appears, e.g. `{ "ResourceManager" }` or `{ "ScriptEditor" }`.
- `category`: menu submenu. Forward slash creates subcategories.
- `awesomeFontCode`: FontAwesome hex code with `0x` prefix, e.g. `0xF0C5`.
- `resourceTypes`: required for resource context-menu plugins to appear for selected resource types such as `fbx`, `xob`, `et`, `conf`, `layout`.

official-doc-example

```c
[WorkbenchPluginAttribute(name: "Sample Resource Manager Plugin", wbModules: { "ResourceManager" })]
class SampleResourceManagerPlugin : WorkbenchPlugin
{
	override void Run()
	{
		Print("I'm here!");
	}
}
```

If `Run()` has no non-empty code, the plugin will not appear in the Plugins tab. This intentionally prevents CLI-only plugins from cluttering the UI.

## Plugin entry points

- `Run()`: called when selecting Plugins > Plugin Name or using its shortcut. There is no way to distinguish menu click from shortcut.
- `RunCommandline()`: called from startup parameters with a plugin argument, for example launching Workbench with `-wbModule=ScriptEditor -plugin=TAG_MyPlugin pluginArguments`.
- `Configure()`: called from Plugins > Settings > Plugin Name. If empty/not overridden, the settings entry does not appear.
- `OnResourceContextMenu(notnull array<ResourceName> resources)`: called from Resource Manager Resource Browser context menu. The attribute must define `resourceTypes` for it to appear.

## Module access

Access the currently loaded editor module through Workbench:

```c
ScriptEditor scriptEditor = Workbench.GetModule(ScriptEditor);
WorldEditor worldEditor = Workbench.GetModule(WorldEditor);
ResourceManager resourceManager = Workbench.GetModule(ResourceManager);
```

Each module exposes a different API. Do not assume World Editor prefab-editing APIs exist in Resource Manager or Script Editor.

Other plugins can be accessed through a Workbench module's `GetPlugin(TAG_ClassNamePlugin)` where supported.

## Dialogs and settings

Generic modal:

- `Workbench.Dialog()` creates a modal with caption, text, and optional detailed text.
- If detailed text is provided, the dialog has a Show Details button.

Scripted modal:

- `Workbench.ScriptDialog()` takes caption, text, and a class instance, usually `this`.
- Use `[Attribute]` on fields to expose options in the dialog.
- Use `[ButtonAttribute]` on methods to define buttons.
- If no buttons are defined, the dialog can still close with the close button or `Alt+F4`; return value is 0.

Button details:

```c
[ButtonAttribute("OK", true)]
int ButtonOK()
{
	return 1;
}

[ButtonAttribute("Cancel")]
int ButtonCancel()
{
	return 0;
}
```

Docs warn an empty string result converts to true/1. Use explicit int/bool return values for confirmation buttons.

## Resource Manager plugin pattern

The tutorial uses Resource Manager plugin to print from `Run()`, then expands into dialogs, import/export buttons, clipboard output, and settings.

Core ingredients:

1. Class inherits `WorkbenchPlugin` or specialized plugin.
2. Attribute has `wbModules: { "ResourceManager" }`.
3. `Run()` has code.
4. Optional `Configure()` opens `ScriptDialog`.
5. Optional `[Attribute]` fields and `[ButtonAttribute]` methods create settings/actions.

For destructive or external actions:

- Ask confirmation through `ScriptDialog`.
- Offer dry-run/log output where possible.
- Guard null/empty selections.
- Avoid running shell/process commands without explicit user intent.
- Remember startup parameter `scriptAuthorizeAll` can suppress security prompts; do not depend on it for normal users.

## Script Editor plugin pattern

The tutorial's Script Editor plugin:

1. Gets `ScriptEditor` module with `Workbench.GetModule(ScriptEditor)`.
2. Guards missing module.
3. Calls `GetCurrentFile(out file)`.
4. Guards no selected file.
5. Calls `Workbench.GetAbsolutePath(file, absPath)`.
6. Reads the current line with `GetLineText(currentLine, -1)`.
7. Exports file name to clipboard.

official-doc-example

```c
[WorkbenchPluginAttribute(name: "Sample Script Editor Plugin", category: "Sample Plugins", shortcut: "Ctrl+T", wbModules: { "ScriptEditor" })]
class SampleScriptEditorPlugin : WorkbenchPlugin
{
	override void Run()
	{
		ScriptEditor scriptEditor = Workbench.GetModule(ScriptEditor);
		if (!scriptEditor)
			return;

		string file;
		if (!scriptEditor.GetCurrentFile(file))
		{
			Print("No file is currently selected!");
			return;
		}

		string currentLine;
		scriptEditor.GetLineText(currentLine, -1);
		Print(currentLine);
	}
}
```

## String Editor / LocalizationEditor note

Docs call out that String Editor is internally referenced as `LocalizationEditor`. A String Editor plugin should use `wbModules: {"LocalizationEditor"}` and can use `LocalizationEditorPlugin` plus `LocalizationEditor` module APIs such as selected rows.

## World Editor plugin pattern

World Editor exposes more functions than other modules, including terrain manipulation, game-mode creation assistance, scenario loading/autotests, prefab/config edits, and entity selection.

Simple selected-entity count pattern:

```c
[WorkbenchPluginAttribute(name: "Sample World Editor Plugin", category: "Sample Plugins", shortcut: "Ctrl+T", wbModules: {"WorldEditor"})]
class SampleWorldEditorPlugin : WorldEditorPlugin
{
	override void Run()
	{
		WorldEditor worldEditor = Workbench.GetModule(WorldEditor);
		if (!worldEditor)
			return;

		WorldEditorAPI api = worldEditor.GetApi();
		Print(api.GetSelectedEntitiesCount());
	}
}
```

## World Editor tools

World Editor tools differ from plugins:

- Use `WorkbenchToolAttribute`.
- Inherit `WorldEditorTool`.
- Cannot be launched via CLI.
- Description parameter is shown in Current Tool panel.
- Category parameter is not relevant for tools.
- Tool parameters and buttons appear in Current Tool tab.
- `WorldEditorTool` provides `m_API`, so tools do not need to fetch `WorldEditorAPI` manually.

Docs state users should enable the Current Tool window from the Windows tab, choose a tool from the toolbar or Tools category, then edit properties in Current Tool tab. Users can drag-and-drop prefab resources into tool properties.

World Editor API edit actions must be wrapped:

```c
m_API.BeginEntityAction("Processing entity");
// create/delete/move/update source variables
m_API.EndEntityAction();
```

This makes changes part of World Editor history so Undo (`Ctrl+Z`) can revert them.

## World Editor tool sample details

The official sample tool:

- Exposes an array of prefab variants with `[Attribute(..., params: "et")]`.
- Exposes random scale toggle.
- Uses `[ButtonAttribute("Delete all")]` and `[ButtonAttribute("Randomise scale")]`.
- Tracks created entities in an array.
- Deletes all created entities if Escape is pressed.
- Uses `TraceWorldPos` on mouse movement/press/release to find cursor position.
- Creates an entity from a random prefab in the current layer.
- Converts entity to source, changes `scale` or `angles` source variables, and wraps changes in `BeginEntityAction`/`EndEntityAction`.

## Diagnostics and logs

Workbench Log Console:

- Shows error, fatal, warning, spam, verbose, debug, and normal logs.
- Can be cleared.
- Has filters for errors, warnings, info, and advanced filter options.

Use logs to diagnose compile errors, missing resources, plugin visibility, Script Editor module access, and Workbench API failures.

## Profiling

Use Script Profiling for performance problems. For Workbench tools, first confirm the editor automation is not doing repeated expensive operations on every mouse move or frame. For runtime scripts, route back to `scripting-core.md`.

## API Notes

Use `api-main.md` for `WorkbenchPlugin`, `WorkbenchPluginAttribute`, `WorkbenchToolAttribute`, `Workbench.GetModule`, `ScriptEditor`, `WorldEditorPlugin`, `ResourceManagerPlugin`, and `ButtonAttribute`. Use `api-extended.md` for `WorldEditorTool`, `WorldEditorAPI`, `LocalizationEditor`, process/dialog APIs, Resource Manager module methods, and editor-specific generated classes.

## Common Traps

- Putting plugin scripts under runtime Game module.
- Empty `Run()` causing a plugin not to appear.
- Forgetting `resourceTypes` for resource context-menu plugins.
- Treating String Editor as `StringEditor` instead of `LocalizationEditor`.
- Making World Editor changes without `BeginEntityAction`/`EndEntityAction`.
- Running destructive editor tools without confirmation or undo-safe action wrapping.
- Calling Workbench APIs from runtime game scripts.

## Review Checklist

- Is the plugin/tool in `Scripts/WorkbenchGame`?
- Does the class/file suffix match Plugin or Tool?
- Are `wbModules`, shortcuts, category, icon code, and resource types correct?
- Are null selections and module lookups guarded?
- Are destructive edits undo-safe and confirmation-gated?

## Plugin Module Detail

- Workbench plugins belong in the Workbench script module layout.
- Runtime gameplay components do not belong in plugin modules.
- Plugin class names should make their editor purpose clear.
- Resource Manager plugins should declare resource filters when they operate on specific resource types.
- Script Editor plugins should validate current file and line state before editing text.
- World Editor plugins should validate selected entities and wrap changes in editor actions.
- Localization/String Editor plugins should use the correct editor module naming and APIs.

## Attribute Detail

- `WorkbenchPluginAttribute` controls Workbench-visible name, description, shortcut, icon, modules, category, font icon, and resource types.
- Keep shortcuts optional and avoid collisions.
- Use category grouping so commands are discoverable.
- Use resource type filters to avoid offering a command on incompatible resources.
- Do not rely on the attribute to validate runtime behavior; still guard in code.
- Keep plugin descriptions short and operational.
- Check exact constructor signature in `api-main.md` or `api-extended.md`.

## Debugging Detail

- Start with compile output.
- Then verify plugin discovery in the intended Workbench module.
- Then verify selection/context.
- Then verify file/resource/world mutations.
- For generated files, check the actual output resource and Resource Manager warnings.
- For editor text edits, verify line indexes and file paths before writing.
- For destructive operations, use confirmation and undo-safe transaction patterns.

## generated-pattern-from-docs: Resource Manager Command

```c
[WorkbenchPluginAttribute("TAG Resource Check", "Checks selected resources", "", "", {"ResourceManager"})]
class TAG_ResourceCheckPlugin : WorkbenchPlugin
{
	override void OnResourceContextMenu(notnull array<ResourceName> resources)
	{
		foreach (ResourceName resourceName : resources)
		{
			PrintFormat("Selected resource: %1", resourceName);
		}
	}
}
```

This example shows the documented Resource Manager plugin shape: Workbench attribute, Resource Manager module dependency, resource context callback, and guarded handling of selected resources.

Workbench plugin examples must still be checked against exact generated API signatures before implementation.
