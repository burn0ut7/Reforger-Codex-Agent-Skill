# Workbench Plugins And Editor Tools

## When To Read

Read this reference when a task involves creating, reviewing, or modifying Workbench plugins or editor extensions: Resource Manager plugins, Script Editor plugins, String Editor plugins, World Editor plugins, World Editor tools, plugin attributes, Workbench links, editor metadata/GUID behavior, command-line plugin execution, event-driven plugin execution, plugin settings, shortcuts, modals, context menus, and editor-only verification.

Use this as the primary owner for:

- choosing the correct Workbench plugin base class or editor module surface;
- registering a plugin with Workbench attributes;
- adding a Resource Manager context menu plugin;
- adding a Script Editor or String Editor plugin;
- creating a World Editor plugin or World Editor tool extension;
- routing exact Workbench API lookup before writing plugin code;
- validating editor-only behavior without confusing it with runtime gameplay behavior.

Do not use this reference as the owner for ordinary Resource Manager browsing, Diag Menu/profiling, world generator/navmesh operation, addon publishing, or Enfusion language syntax. Those topics belong to their narrower references.

## Source Inventory

Wiki ownership:

- Primary wiki topics/categories: Workbench Plugin Tutorial, Workbench Plugin, Resource Manager Plugin, Script Editor Plugin, String Editor Plugin, World Editor Plugin, Workbench Links, Workbench Metadata.
- Secondary/cross-reference topics: Resource Manager plugin category page, Script Editor plugin category page, World Editor plugin category page, Resource Manager editor operations, diagnostics, world-editor tools, addon packaging, language syntax.

Wiki pages reviewed:

- Workbench Plugin Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Workbench_Plugin_Tutorial - status: covered - reason: primary tutorial source for plugin data structure, attributes, settings, shortcuts, CLI/event execution, external command execution, editor plugin families, and World Editor extensions.
- Workbench Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Workbench_Plugin - status: covered - reason: primary API/concept page for plugin vs tool, modules/plugins, common methods, modals, attributes, buttons, and tutorial routing.
- Resource Manager Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager_Plugin - status: covered - reason: primary plugin-authoring source for setup, contextual menu options, and ResourceManager module API routes.
- Script Editor Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor_Plugin - status: covered - reason: primary plugin-authoring source for setup, ScriptEditor module API, and configuration.
- String Editor Plugin - https://community.bistudio.com/wiki/Arma_Reforger:String_Editor_Plugin - status: covered - reason: primary plugin-authoring source for setup, LocalizationEditorPlugin API, and LocalizationEditor module API.
- World Editor Plugin - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor_Plugin - status: covered - reason: primary plugin-authoring source for setup, WorldEditorPlugin API, WorldEditor module API, WorldEditorAPI API, and example routing.
- Workbench Links - https://community.bistudio.com/wiki/Arma_Reforger:Workbench_Links - status: covered - reason: primary source for Workbench link format and Resource Manager/Script Editor/World Editor link creation.
- Workbench Metadata - https://community.bistudio.com/wiki/Arma_Reforger:Workbench_Metadata - status: covered - reason: source for `.meta`, GUID, GUID change, and resource database behavior where plugin/tool workflows depend on identity and links.
- Modding/Official Tools/Resource Manager Plugins category - https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Official_Tools/Resource_Manager_Plugins - status: partial - reason: routing/source inventory only; individual Resource Manager plugin usage pages are owned by the Resource Manager reference unless plugin authoring is the task.
- Modding/Official Tools/Script Editor Plugins category - https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Official_Tools/Script_Editor_Plugins - status: partial - reason: routing/source inventory only; script editing plugin usage pages are cross-referenced to the language/editor reference where appropriate.
- Modding/Official Tools/World Editor Plugins category - https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Official_Tools/World_Editor_Plugins - status: partial - reason: routing/source inventory only; generator/navmesh/tool use belongs to the World Editor reference.

Wiki sections covered:

- Workbench Plugin Tutorial: Editor Plugins; World Editor Tools; Preparing Data Structure; Resource Manager Plugin; Basic structure; Workbench Attribute; attribute fields; adding categories/icons; expanding plugin functionality; settings; key shortcuts; CLI execution; event execution; external command execution; Script Editor Plugin; String Editor plugin; World Editor Plugin; World Editor Tool; tool setup; World Editor API usage; example routing.
- Workbench Plugin: Plugin; Tool; Scripting; Modules; Plugins; Common Methods; `Run`; `RunCommandline`; `Configure`; `OnResourceContextMenu`; Generic Modal; Scripted Modal; Attributes; Buttons; Tutorials.
- Resource Manager Plugin: Setup; Contextual Menu Option; ResourceManager Module API.
- Script Editor Plugin: Setup; ScriptEditor Module API; Configuration.
- String Editor Plugin: Setup; LocalizationEditorPlugin API; LocalizationEditor Module API.
- World Editor Plugin: Setup; WorldEditorPlugin API; WorldEditor Module API; WorldEditorAPI API; Example.
- Workbench Links: Format; Link Creation; Resource Manager links; Script Editor links; World Editor links.
- Workbench Metadata: `.meta` file; GUID; GUID Change; resource database file.

Structured wiki records:

- Tables reviewed/included: plugin data structure, Workbench attribute fields, external command/run table, Workbench link format.
- Procedures reviewed/included: expanding plugin functionality, `Configure`, Resource Manager plugin setup, Script Editor plugin setup, String Editor plugin setup, World Editor plugin setup, metadata/GUID change handling.
- Admonitions reviewed/included: editor-plugin caveats, attribute/icon/category warnings, module API warnings, context menu caveats, Workbench link format warnings, metadata/GUID warnings.
- Code blocks reviewed/included: CLI plugin execution, event plugin execution, `RunCommandline`, setup examples, sample plugin routing; code is summarized and routed, not copied.
- Media reviewed: Workbench plugin tutorial screenshots and Workbench link screenshots were treated as UI evidence, not copied.

Game-data/API evidence:

- Queries run:
  - `py -3 scripts\query-reforger-data.py symbol WorkbenchPlugin --kind class --exact`
  - `py -3 scripts\query-reforger-data.py examples workbench-plugin --limit 8`
  - `py -3 scripts\query-reforger-data.py files WorkbenchPlugin --limit 8`
  - `py -3 scripts\query-reforger-data.py files WorkbenchPluginAttribute --limit 8`
  - `py -3 scripts\query-reforger-data.py files WorldEditorPlugin --limit 8`
  - `py -3 scripts\query-reforger-data.py files ResourceManagerPlugin --limit 8`
  - `py -3 scripts\query-reforger-data.py files ScriptEditorPlugin --limit 8`
- Symbols/methods/attributes verified: `WorkbenchPlugin`, `WorkbenchPluginAttribute`, `WorkbenchToolAttribute`, `ResourceManagerPlugin`, `WorldEditorPlugin`, `LocalizationEditorPlugin`, Script Editor plugin routes, `RunCommandline`.
- Examples/snippets reviewed: Workbench plugin examples in Workbench, WorkbenchCommon, WorkbenchGame, Autotest, Resource Manager, Script Editor, and World Editor source families.

Samples and source examples:

- Official sample folder reviewed: `SampleMod_WorkbenchPlugin`.
- Official sample plugin families reviewed as routing signals: Resource Manager plugin, Script Editor plugin, String Editor plugin, World Editor plugin, World Editor tool.
- Game-source example families reviewed: Tracy plugin, flowmap tool, resave tools, resource test tool, world test tool, editable entity maintenance plugin, image set generator, localization plugins, resource import, terrain import, data-to-spreadsheet, VCS plugins, World Editor plugins.

Coverage gaps:

- General Resource Manager usage, file-type browsing, editor panels, and batch processor operation are intentionally excluded and owned by `resource-manager-file-types-and-editors.md`.
- Diagnostics, FPS diagnostic usage, Diag Menu, profiling, and autotests are intentionally excluded and owned by `diagnostics-testing-and-performance.md`.
- World Editor generator/navmesh/tool operation is intentionally excluded and owned by `world-editor-tools-generators-and-navmesh.md`; this reference owns only plugin/tool extension authoring.
- Addon packaging and publishing are intentionally excluded and owned by `mod-projects-addons-workshop.md`.
- Enfusion language syntax and Script Editor editing behavior are intentionally excluded and owned by `enfusion-language-and-script-editor.md`.

## Wiki Source Coverage

Workbench plugin model:

- Workbench plugins are editor extensions, not runtime gameplay systems.
- A plugin can target a Workbench module such as Resource Manager, Script Editor, String Editor, Localization Editor, or World Editor.
- Tools are a related Workbench extension concept, especially for World Editor workflows.
- Plugin authoring requires both script structure and Workbench registration metadata.
- Plugin behavior should be validated inside the intended Workbench module, not only by compiling script.

Workbench plugin tutorial coverage:

- The tutorial separates editor plugins from World Editor tools.
- It shows a data structure for Workbench plugin samples and editor extension files.
- It walks through a Resource Manager plugin as the basic plugin shape.
- It introduces the Workbench attribute surface used to register editor plugins.
- It covers fields such as plugin name, description, shortcut, icon, target Workbench modules, category, and Awesome Font icon code.
- It shows adding category information and custom icons.
- It expands plugin functionality through settings, key shortcuts, command-line execution, event execution, and running external executables.
- It routes Script Editor and String Editor plugins as separate plugin families.
- It covers creating World Editor extensions through World Editor plugin and World Editor tool concepts.
- It includes World Editor API usage and example tool routing.

Workbench Plugin page coverage:

- The page distinguishes plugin and tool concepts.
- It identifies scripting surfaces for modules, plugins, and common methods.
- `Run` is the normal command-style entry point to verify before implementing plugin behavior.
- `RunCommandline` is the route for command-line execution behavior.
- `Configure` is the route for plugin configuration behavior.
- `OnResourceContextMenu` is the Resource Manager context menu extension hook.
- Generic modal and scripted modal behavior are Workbench UI surfaces; exact classes and methods must be queried before use.
- Attributes and buttons are part of the plugin registration/UI surface.

Resource Manager Plugin coverage:

- Resource Manager plugins are set up as plugin classes targeting the Resource Manager module.
- Contextual menu options are a Resource Manager-specific extension surface.
- ResourceManager module API use belongs here only when authoring plugin behavior; ordinary Resource Manager usage belongs to the Resource Manager reference.
- Context menu behavior must be tested on selected resources, not only by loading Workbench.

Script Editor Plugin coverage:

- Script Editor plugins have their own setup and module API.
- Plugin configuration is separate from Enfusion language syntax.
- Use this reference for plugin extension behavior; use the language/editor reference for syntax, code formatting semantics, or editing workflow.

String Editor Plugin coverage:

- String Editor plugins use LocalizationEditorPlugin and LocalizationEditor module API routes.
- Localization editor plugin behavior is editor-only.
- Localization data/workflow ownership remains with localization or addon/project references when the task is not plugin authoring.

World Editor Plugin coverage:

- World Editor plugins have setup, plugin API, module API, and WorldEditorAPI routes.
- A World Editor tool is an extension surface used for editor interaction workflows.
- This reference owns the extension setup and API routing.
- Actual world-editing workflows, generator parameters, terrain, roads, rivers, forests, and navmesh operations belong to World Editor and terrain references.

Workbench Links coverage:

- Workbench links have a specific format.
- Link creation differs by target surface: Resource Manager, Script Editor, and World Editor.
- Links are useful for editor navigation and source provenance, but exact link behavior should be checked against the target module.

Workbench Metadata coverage:

- `.meta` files carry resource identity information used by Workbench.
- GUIDs are important for resource identity and references.
- GUID changes can break references or links if not handled deliberately.
- The resource database file is a Workbench data surface; do not treat it as ordinary hand-authored gameplay data.

Plugin categories:

- Resource Manager, Script Editor, and World Editor plugin category pages are routing indexes for related plugin pages.
- Category pages do not replace the specific plugin setup pages or the Workbench Plugin Tutorial.
- Use category pages to discover related official plugin pages when a future reference needs a more specific plugin type.

## Terms And Concepts

- Workbench: Reforger editor environment.
- Workbench module: editor surface such as Resource Manager, Script Editor, String Editor, Localization Editor, or World Editor.
- Plugin: editor extension registered through Workbench plugin APIs and attributes.
- Tool: editor extension concept, especially for World Editor interactions.
- `WorkbenchPlugin`: base class for many Workbench plugins.
- `WorkbenchPluginAttribute`: registration metadata for Workbench plugins.
- `WorkbenchToolAttribute`: registration metadata for Workbench tools.
- `ResourceManagerPlugin`: Resource Manager-specific plugin base.
- `ScriptEditorPlugin`: Script Editor plugin surface.
- `LocalizationEditorPlugin`: String/Localization editor plugin surface.
- `WorldEditorPlugin`: World Editor plugin base.
- `WorldEditorAPI`: API surface for World Editor plugin/tool behavior.
- `Run`: normal plugin execution entry point.
- `RunCommandline`: plugin command-line execution route.
- `Configure`: configuration entry point.
- `OnResourceContextMenu`: Resource Manager context menu hook.
- Workbench link: editor-specific URI/link format for opening resources or source locations.
- `.meta`: Workbench metadata file for resource identity.
- GUID: resource identity value used by Workbench metadata and references.

## Workbench / Resource / Data Surfaces

Plugin authoring surfaces:

- Workbench plugin script class.
- Workbench attribute registration.
- Target Workbench module list.
- Plugin category.
- Plugin shortcut.
- Plugin icon or Awesome Font code.
- Plugin settings/configuration.
- Command-line execution path.
- Event-driven execution path.
- External executable command path.
- Context menu extension path.
- Modal/dialog UI path.
- Workbench links.
- `.meta` file and GUID identity.
- Resource database.

Target module surfaces:

- Resource Manager: plugin setup, resource context menu, ResourceManager module API.
- Script Editor: plugin setup, ScriptEditor module API, configuration.
- String Editor / Localization Editor: LocalizationEditorPlugin API and module API.
- World Editor: plugin setup, WorldEditorPlugin API, WorldEditor module API, WorldEditorAPI, World Editor tools.

Cross-reference surfaces:

- Resource Manager daily editor usage belongs to `resource-manager-file-types-and-editors.md`.
- Script language and editing behavior belongs to `enfusion-language-and-script-editor.md`.
- World Editor tool operation, generators, and navmesh belong to `world-editor-tools-generators-and-navmesh.md`.
- Diagnostics/profiling belongs to `diagnostics-testing-and-performance.md`.
- Project packaging/publishing belongs to `mod-projects-addons-workshop.md`.

## Required Workflows

Workbench plugin authoring workflow:

1. Identify the target Workbench module.
2. Choose the narrowest plugin base or tool base for that module.
3. Query exact API classes and attributes before writing code.
4. Add the Workbench registration attribute with name, description, module target, category, shortcut, and icon metadata as needed.
5. Implement the smallest required entry point, usually `Run`, `RunCommandline`, `Configure`, or a module-specific hook.
6. Add settings or modal UI only when the task requires user input.
7. Validate inside the target Workbench module.
8. Verify that plugin behavior is editor-only and does not leak runtime assumptions into gameplay code.

Resource Manager plugin workflow:

1. Use `ResourceManagerPlugin` when the extension belongs to Resource Manager.
2. Register the plugin for the Resource Manager module.
3. Use context menu hooks only when behavior depends on selected resources.
4. Query `ResourceManagerPlugin`, `WorkbenchPluginAttribute`, and nearby examples.
5. Test with selected resources, no selection, and unexpected resource types.
6. Route ordinary file browsing/editor behavior to the Resource Manager reference.

Script Editor plugin workflow:

1. Use the Script Editor plugin setup page as workflow source.
2. Query Script Editor plugin examples and exact API.
3. Keep language syntax rules out of the plugin implementation decision.
4. Test command invocation and configuration inside Script Editor.

String Editor plugin workflow:

1. Use LocalizationEditorPlugin and LocalizationEditor module API routes.
2. Query localization editor plugin source examples.
3. Test against real localization data.
4. Keep localization content policy separate from plugin authoring.

World Editor plugin/tool workflow:

1. Decide whether the extension is a plugin or a tool.
2. Use WorldEditorPlugin and WorldEditorAPI routes for editor extension behavior.
3. Query exact World Editor plugin examples before writing code.
4. Keep terrain/generator/navmesh operations in their owning references.
5. Test with a world open, selected entities/resources as needed, and no-selection cases.

Workbench link workflow:

1. Choose the target surface: Resource Manager, Script Editor, or World Editor.
2. Use the Workbench Links format rules.
3. Confirm link target identity and GUID behavior where resources are involved.
4. Test the link from Workbench.

Metadata/GUID workflow:

1. Treat `.meta` and GUID data as identity surfaces, not normal gameplay data.
2. Avoid unnecessary GUID changes.
3. If GUID changes are required, inspect all references that may depend on the old GUID.
4. Rebuild or refresh Workbench data only through the appropriate tool workflow.

## Configuration Fields And Tables

Workbench plugin attribute fields to preserve:

- name;
- description;
- shortcut;
- icon;
- target Workbench modules;
- category;
- Awesome Font code;
- custom category metadata;
- custom icon metadata.

Plugin method/configuration surfaces to verify:

- `Run`;
- `RunCommandline`;
- `Configure`;
- `OnResourceContextMenu`;
- generic modal setup;
- scripted modal setup;
- button configuration;
- plugin settings.

Resource Manager plugin fields/surfaces:

- selected resource;
- contextual menu option;
- ResourceManager module API;
- resource browser behavior;
- resource type filtering, if implemented by the plugin.

Script Editor plugin fields/surfaces:

- ScriptEditor module API;
- plugin configuration;
- command behavior;
- target script or editor context.

String Editor plugin fields/surfaces:

- LocalizationEditorPlugin API;
- LocalizationEditor module API;
- selected localization file/context;
- export/import or validation behavior if implemented by a plugin.

World Editor plugin/tool fields/surfaces:

- WorldEditorPlugin API;
- WorldEditor module API;
- WorldEditorAPI;
- selected entities;
- world context;
- tool state;
- editor UI command or toolbar behavior.

Workbench link table concepts:

- link format;
- target module;
- resource/script/world target;
- optional line or resource target details where supported by the wiki link format.

Metadata fields:

- `.meta` file;
- GUID;
- GUID change behavior;
- resource database file.

## Procedures And Ordered Steps

Before writing a Workbench plugin:

1. Read this reference and the plugin page for the target editor module.
2. Query the exact base class and attribute.
3. Inspect one bounded example for the target plugin family.
4. Decide whether the plugin needs a command, context menu, configuration dialog, modal, event hook, or command-line path.
5. Implement the narrowest editor-only behavior.
6. Test in the target Workbench module.

Before adding a Workbench attribute:

1. Query `WorkbenchPluginAttribute`.
2. Check the tutorial attribute fields.
3. Set only required metadata first.
4. Add category, shortcut, icon, and module targets deliberately.
5. Test that the plugin appears in the expected editor surface.

Before adding command-line plugin execution:

1. Review the tutorial command-line execution section.
2. Query examples using `RunCommandline`.
3. Keep command-line arguments bounded and explicit.
4. Test success and missing/invalid argument behavior.

Before adding external executable behavior:

1. Review the tutorial external command section.
2. Confirm whether the task truly requires an external executable.
3. Keep external invocation editor-only.
4. Validate paths, arguments, working directory behavior, and failure reporting.

Before adding plugin UI:

1. Decide whether a simple command is enough.
2. Query modal/button examples.
3. Use generic or scripted modal routes based on needed UI complexity.
4. Test cancel, confirm, invalid input, and repeated invocation.

Before changing GUID/metadata behavior:

1. Confirm that the task involves resource identity, not plugin runtime state.
2. Review Workbench Metadata.
3. Avoid changing GUIDs unless required.
4. Validate links and resource references after the change.

## Warnings And Failure Modes

- Do not treat Workbench plugins as runtime gameplay systems.
- Do not guess Workbench API classes, attributes, or method signatures.
- Do not use a Resource Manager plugin page as authority for ordinary Resource Manager editor usage.
- Do not put World Editor generator/navmesh behavior into this reference; only plugin/tool extension setup belongs here.
- Do not change resource GUIDs casually; references and Workbench links can break.
- Do not assume a plugin registered for one Workbench module appears in another module.
- Do not add settings, modals, or external executable calls unless the plugin task requires them.
- Do not assume context menu code always has a valid selected resource.
- Do not assume selected entities exist in World Editor plugin/tool code.
- Do not copy official sample source bodies into runtime references.
- Do not rely on Workbench-only examples for dedicated-server or gameplay runtime behavior.
- Do not validate only by script compile; confirm plugin discovery and execution inside Workbench.

## API Lookup Keys

Core plugin symbols:

- `WorkbenchPlugin`
- `WorkbenchPluginAttribute`
- `WorkbenchToolAttribute`
- `ResourceManagerPlugin`
- `ScriptEditorPlugin`
- `LocalizationEditorPlugin`
- `WorldEditorPlugin`
- `WorldEditorAPI`

Common methods/hooks:

- `Run`
- `RunCommandline`
- `Configure`
- `OnResourceContextMenu`

Workbench module/search terms:

- Workbench
- ResourceManager
- ResourceBrowser
- ScriptEditor
- LocalizationEditor
- StringEditor
- WorldEditor
- Generic Modal
- Scripted Modal
- ButtonAttribute
- DateTimeUtcAsInt
- WorkbenchSearchResourcesCallback

Example families:

- Tracy plugin
- ImageSet generator
- Flowmap tool
- Resave tools
- Resource test tool
- World test tool
- Editable entity maintenance plugin
- VCS plugins
- Localization plugins
- World window data drop plugin

## Game-Data Query Commands

Use exact API lookup before writing plugin code:

```powershell
py -3 scripts\query-reforger-data.py symbol WorkbenchPlugin --kind class --exact
py -3 scripts\query-reforger-data.py files WorkbenchPluginAttribute --limit 8
py -3 scripts\query-reforger-data.py files WorkbenchPlugin --limit 8
```

Find target-module examples:

```powershell
py -3 scripts\query-reforger-data.py examples workbench-plugin --limit 8
py -3 scripts\query-reforger-data.py files ResourceManagerPlugin --limit 8
py -3 scripts\query-reforger-data.py files ScriptEditorPlugin --limit 8
py -3 scripts\query-reforger-data.py files WorldEditorPlugin --limit 8
```

Use snippets only after choosing a specific result:

```powershell
py -3 scripts\query-reforger-data.py snippet scripts/GameLib/workbench/workbench.c --line 1 --context 30
py -3 scripts\query-reforger-data.py snippet scripts/Workbench/SCR_TracyPlugin.c --line 1 --context 20
py -3 scripts\query-reforger-data.py snippet scripts/WorkbenchCommon/ResourceTestTool.c --line 1 --context 30
py -3 scripts\query-reforger-data.py snippet scripts/WorkbenchGame/ScriptEditor/SCR_VCSPlugins.c --line 1 --context 30
```

Use JSON when another tool or audit pass needs structured results:

```powershell
py -3 scripts\query-reforger-data.py examples workbench-plugin --limit 8 --json
```

## Examples And Samples

Official sample route:

- `SampleMod_WorkbenchPlugin`: primary official sample layout signal for Workbench plugin tasks.
- Sample Resource Manager plugin: route when the task adds a Resource Manager command or context menu plugin.
- Sample Script Editor plugin: route when the task extends Script Editor.
- Sample String Editor plugin: route when the task extends String/Localization Editor.
- Sample World Editor plugin: route when the task adds a World Editor plugin.
- Sample World Editor tool: route when the task adds tool-style editor interaction.

Game-source example routes:

- `scripts/Workbench/SCR_TracyPlugin.c`: compact Workbench plugin example.
- `scripts/WorkbenchCommon/FlowmapTool.c`: Workbench plugin/tool with command-line style evidence.
- `scripts/WorkbenchCommon/ResaveMetaTool.c` and `scripts/WorkbenchCommon/ResaveTool.c`: Resource Manager/workbench resave tool patterns.
- `scripts/WorkbenchCommon/ResourceTestTool.c`: Workbench plugin with UI/resource evidence.
- `scripts/WorkbenchCommon/WorldTestTool.c`: Workbench/world validation tool route.
- `scripts/WorkbenchGame/Editor/SCR_EditableEntityMaintenancePlugin.c`: WorkbenchGame editor plugin pattern.
- `scripts/WorkbenchGame/ScriptEditor/SCR_VCSPlugins.c`: Script Editor and Resource Manager VCS plugin family.
- `scripts/Workbench/WorldEditor/SCR_WorldWindowDataDropPlugin.c`: World Editor plugin route.

How to use examples:

1. Start with the official sample family matching the target editor module.
2. Query exact base classes and attributes.
3. Inspect one bounded game-source snippet for the same plugin family.
4. Keep source examples as patterns, not source of truth for wiki workflow rules.
5. Validate in Workbench.

## Follow-Up Keywords

- Workbench plugin
- editor plugin
- Workbench tool
- Resource Manager plugin
- Script Editor plugin
- String Editor plugin
- Localization Editor plugin
- World Editor plugin
- World Editor tool
- `WorkbenchPlugin`
- `WorkbenchPluginAttribute`
- `WorkbenchToolAttribute`
- `ResourceManagerPlugin`
- `ScriptEditorPlugin`
- `LocalizationEditorPlugin`
- `WorldEditorPlugin`
- `WorldEditorAPI`
- `Run`
- `RunCommandline`
- `Configure`
- `OnResourceContextMenu`
- generic modal
- scripted modal
- plugin category
- shortcut
- icon
- Workbench links
- `.meta`
- GUID
- resource database

## Verification

Minimum plugin verification:

- Confirm scripts compile.
- Confirm the plugin appears in the intended Workbench module.
- Confirm it does not appear in unintended modules unless deliberately registered there.
- Invoke the plugin through the intended UI command, context menu, shortcut, event hook, or command-line path.
- Test no-selection and invalid-selection behavior for Resource Manager and World Editor plugins.
- Test settings/configuration behavior if `Configure` or settings are used.
- Test cancel/confirm/invalid input behavior for modal UI.
- Test command-line behavior with missing, valid, and invalid arguments when `RunCommandline` is used.
- Confirm external executable calls report failures clearly if used.
- Confirm Workbench links open the expected target.
- Confirm GUID/metadata changes do not break expected references.

Residual verification note:

- Game-data lookup verifies API names and example routes. It does not prove editor registration, UI placement, context menu selection, command-line invocation, metadata identity, or Workbench link behavior. Those must be verified inside Workbench.

## Official Wiki Links

- Workbench Plugin Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Workbench_Plugin_Tutorial
- Workbench Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Workbench_Plugin
- Resource Manager Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager_Plugin
- Script Editor Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor_Plugin
- String Editor Plugin: https://community.bistudio.com/wiki/Arma_Reforger:String_Editor_Plugin
- World Editor Plugin: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor_Plugin
- Workbench Links: https://community.bistudio.com/wiki/Arma_Reforger:Workbench_Links
- Workbench Metadata: https://community.bistudio.com/wiki/Arma_Reforger:Workbench_Metadata
- Resource Manager Plugins category: https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Official_Tools/Resource_Manager_Plugins
- Script Editor Plugins category: https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Official_Tools/Script_Editor_Plugins
- World Editor Plugins category: https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Official_Tools/World_Editor_Plugins

## Usefulness Score

Score: 95/100

Scoring breakdown:

- Wiki coverage: 30/30. All owned primary pages are represented, including tutorial, API/concept page, module-specific plugin pages, Workbench links, metadata, and category routing pages. Tables, setup procedures, warnings, code-block routes, media evidence, and official URLs are covered structurally.
- Operational detail: 15/15. The reference preserves plugin setup, attributes, target modules, CLI/event execution, external command routing, context menus, modals, Workbench links, metadata/GUID handling, and validation order.
- API lookup usefulness: 15/15. Exact query commands cover `WorkbenchPlugin`, `WorkbenchPluginAttribute`, plugin examples, Resource Manager plugin, Script Editor plugin, and World Editor plugin routes.
- Example grounding: 9/10. Official `SampleMod_WorkbenchPlugin` families and game-source Workbench examples are routed clearly. Score is not full only because sample source bodies are intentionally not copied.
- Codex task usefulness: 15/15. Codex can route a Workbench plugin task to the correct module owner, query exact APIs, inspect a bounded example, implement narrowly, and verify in Workbench.
- Context efficiency: 8/10. The reference is dense because Workbench plugin ownership spans several editor modules, but it avoids duplicating Resource Manager, diagnostics, World Editor operation, packaging, and language ownership.
- Verification guidance: 5/5. Workbench discovery, module targeting, command invocation, selection cases, modals, CLI, external process, links, metadata, and GUID verification are explicit.

Missed coverage and cap review:

- No owned primary wiki page is omitted.
- Resource Manager, Script Editor, and World Editor plugin category pages are included as routing/source inventory, not full workflow owners, so no category-ownership leak applies.
- General Resource Manager usage, diagnostics, World Editor operation, packaging, and language syntax are excluded by design and cross-linked to their owners.
- No automatic failure applies: official wiki links are present, query commands are present, examples are routed, split boundaries are explicit, and no broad API dump is embedded.
