# Resource Manager, File Types, And Editors

## When To Read

Read this reference when the task is about Resource Manager itself: browsing resources, finding files, using Resource Browser filters, reading Resource Manager log output, choosing the right editor for a file type, changing Resource Manager or editor options, using editor import settings, running Resource Manager utility plugins, or understanding what a Reforger resource extension represents.

Do not use this as the primary owner for prefab/config data modeling, domain asset creation, UI widget implementation, Workbench plugin authoring, terrain/world editing, or project packaging. Those workflows are owned by their narrower references. This file owns the Resource Manager surfaces and file/editor routing needed before Codex opens the deeper owner.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: Resource Manager, Resource Manager Options, File Types, Config Editor, Layout Editor, Imageset Editor, Model Editor, Texture Editor, Material Editor, Data To Spreadsheet, Resource Manager utility plugins, Resource Manager plugin/viewports category routing.
- Secondary/cross-reference topics: prefab/config data modeling, asset import/model QA, UI layout implementation, Workbench plugin authoring, terrain import, project publishing, and server/runtime workflows are named only as handoffs.

Wiki pages reviewed:
- Resource Manager - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager - status: covered - reason: owns the main interface, menus, Resource Browser, viewport, details/import settings, shortcuts, plugin entries, and log console.
- Resource Manager: Options - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Options - status: covered - reason: owns project/module/editor settings surfaced through Resource Manager.
- File Types - https://community.bistudio.com/wiki/Arma_Reforger:File_Types - status: covered - reason: owns extension routing and file-type distinctions.
- Resource Manager: Config Editor - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Config_Editor - status: covered - reason: owns Config Editor interface and value-editing surfaces.
- Resource Manager: Layout Editor - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Layout_Editor - status: covered - reason: owns Layout Editor controls, hierarchy, property grid, and editor-only UI layout surfaces.
- Resource Manager: Imageset Editor - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Imageset_Editor - status: covered - reason: owns imageset texture and quad editing surfaces.
- Resource Manager: Model Editor - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Model_Editor - status: covered - reason: owns Model Editor viewport, scene, details, collider, LOD, bone, runtime detail, and import-setting surfaces.
- Resource Manager: Texture Editor - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Texture_Editor - status: covered - reason: owns Texture Editor preview, channel, mip, histogram, conversion, and import-setting surfaces.
- Resource Manager: Material Editor - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Material_Editor - status: partial - reason: the wiki page is sparse; material workflow depth is routed to the asset import/material owner.
- Resource Manager: Data To Spreadsheet - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Data_To_Spreadsheet - status: covered - reason: owns spreadsheet export/import plugin surface, template classes, attribute selection, and parser workflow.
- Resource Manager: Generate Class From Layout Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Generate_Class_From_Layout_Plugin - status: covered - reason: owns the Resource Manager command and generated-script routing for layouts.
- Resource Manager: Batch Resource Processor Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Batch_Resource_Processor_Plugin - status: covered - reason: owns batch resource processing UI, parameters, and command-line surface.
- Resource Manager: Batch Texture Processor Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Batch_Texture_Processor_Plugin - status: covered - reason: owns batch texture processing UI and parameters.
- Resource Manager: Find Linked Resources Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Find_Linked_Resources_Plugin - status: covered - reason: owns dependency/link lookup plugin surface and output interpretation.
- Resource Manager: Resave Plugins - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Resave_Plugins - status: covered - reason: owns resave and resave-meta plugin usage and command-line surface.
- Resource Manager Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager_Plugin - status: partial - reason: this reference owns Resource Manager plugin placement/context; full Workbench plugin authoring belongs to `workbench-plugins-and-editor-tools.md`.
- Resource Manager Plugins category - https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Official_Tools/Resource_Manager_Plugins - status: covered - reason: category routing for Resource Manager plugin pages.
- Resource Manager Viewports category - https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Official_Tools/Resource_Manager_Viewports - status: covered - reason: category routing for editor viewport pages.

Wiki sections covered:
- Resource Manager > Interface, Window Menu, Workbench, Editors, View, Edit, Window, Utilities, Plugins, Resource Browser, Usage, Search bar, Filters, Options, Viewport, Tabs, Viewport Types, Log Console, Details / Import Settings, Import Settings, Parameters, General Shortcuts - coverage: represented as operational surfaces and routing checks.
- Resource Manager: Options > Game Project, General Parameters, Dependencies, Per platform parameters, Modules, Workbench, World Editor, Animation Editor, Script Editor, Audio Editor, Behavior Editor, Shortcuts - coverage: represented as option families and field names.
- File Types > extension table - coverage: represented as grouped extension routing.
- Config Editor > Main Interface, Value Interface, Advanced Usage - coverage: represented as editor surface and split boundary.
- Layout Editor > Top Bar, Hierarchy, Contextual Menu, Properties Tab, Transform, Behavior, Appearance, Text, Widget, Style, Script, Navigation, Events, Classes Tab, Last Used Prefabs Tab - coverage: represented as editor controls and UI-layout handoff.
- Imageset Editor > Top Bar, ImageSet Tab, Quads Tab, Quad Properties, Import Settings Tab - coverage: represented as imageset editing surface.
- Model Editor > Horizontal bar, Viewport UI, Options, Scene preset, Scene settings, Grid, Ground, Wireframe settings, Overlay settings, Environment settings, Lighting settings, Camera settings, Postprocessing, Details Tab, Materials, LODs, Colliders, Layers, Center of mass, Bones, Runtime Details, Import Settings Tab, General, Transform, Visual, Physics, Geometry Params - coverage: represented as model editor and import setting surface.
- Texture Editor > Horizontal Bar, Details Tab, Texture properties, Histogram, Color graph, Import Settings Tab, General, Target Format, Conversion, Color Space, Mips, Tiled Texture, Generate Cubemap, Volume Texture - coverage: represented as texture editor and import setting surface.
- Data To Spreadsheet > Description, Usage, Interface, Spreadsheet Parser, templates, ammo-data examples, import/export - coverage: represented as ordered workflow and API lookup routes.
- Utility plugins > usage, parameters, command-line, output - coverage: represented as tool procedures and verification checks.

Structured wiki records:
- Tables reviewed/included: File Types extension table; Resource Manager Window Menu; Resource Browser contextual menus and search special characters; viewport tab table; General Shortcuts; plugin parameter tables; Data To Spreadsheet table; Layout Editor Events table; Model Editor horizontal-bar and shading tables.
- Procedures reviewed/included: Resource Manager interface opening/navigation; file system dump; plugin setup/context menu surface; Batch Resource Processor usage; Batch Texture Processor usage; Data To Spreadsheet export/import; Generate Class From Layout usage; Layout Editor clipping behavior; Model Editor material/collider inspection.
- Admonitions reviewed/included: candidate requirements and caveats around project dependencies, import settings, resource selection, plugin context, and editor validation were preserved as warnings/failure modes.
- Code blocks reviewed/included: command-line examples and plugin-generated output were reviewed, but exact generated source bodies are not copied here.
- Media reviewed: editor screenshots and images were treated as surface confirmation only; this runtime reference names controls instead of depending on images.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts\query-reforger-data.py files ResourceManager --limit 10`
  - `py -3 scripts\query-reforger-data.py files ResourceManagerPlugin --limit 10`
  - `py -3 scripts\query-reforger-data.py files ResourceName --limit 10`
  - `py -3 scripts\query-reforger-data.py examples resource-loading --subtopic resource-picker-config --limit 8`
  - `py -3 scripts\query-reforger-data.py examples ui --subtopic ui-layout-resource --limit 8`
- Symbols/methods/attributes verified as lookup routes: `ResourceManager`, `ResourceManagerPlugin`, `ResourceBrowser`, `ResourceName`, `ResourceNamePicker`, `Resource.Load`, `WorkbenchPlugin`, `WorkbenchPluginAttribute`, `SCR_DataToSpreadsheetPlugin`, `SCR_DataToSpreadsheetTemplatesAttribute`, `SCR_DataToSpreadsheetTemplatesComponent`, `SCR_DataToSpreadsheetTemplatesObject`, `SCR_ImageSetGenerator`, `TextureImportPlugin`, `BatchTextureProcessorPlugin`, `ResaveMetaPlugin`, `ResavePlugin`, `ResourceImportPlugin`, `TerrainImportPlugin`, `SCR_FindResourcesPlugin`.
- Examples/snippets reviewed: Resource Manager plugin files, Data To Spreadsheet plugin file, Resource Import and Texture Import tools, ResourceName/resource-picker examples, and UI layout resource examples were reviewed through query output.

Samples and source examples:
- Official sample folders reviewed: `SampleMod_Main`, `SampleMod_ModdedCar`, `SampleMod_ModdedWeapon`, `SampleMod_ModdedScript`, `SampleMod_AnimationWorkshop`, and `SampleMod_CinematicTutorial` as resource/file-layout signals only.
- Raw game-source example families reviewed through query output: Resource Manager plugins, resource-loading examples, resource-picker configuration, UI layout resources, texture import tools, resave tools, and find-linked-resources tooling.

Coverage gaps:
- Missing, excluded, or intentionally deferred source: full prefab/config modeling, material authoring, asset import QA, UI widget behavior, Workbench plugin registration architecture, and project publishing.
- Reason and impact: those are source-heavy workflows with their own reference owners. This reference keeps the Resource Manager/editor surface and points Codex to the owner before changing deeper data or code.

## Wiki Source Coverage

Resource Manager is the central Workbench surface for locating, opening, editing, importing, reimporting, saving, validating, and publishing resources. Treat it as the place where resource files become editor tabs and where file-type-specific editors expose their import/detail settings. It is not by itself the authority for how a weapon, vehicle, UI widget, prefab, or addon should be modeled.

The main Resource Manager page is interface-heavy and should be preserved as an operating map:
- `Workbench` menu: save the active resource, save all resources, open options, log in/out, publish the current project, or exit.
- `Editors` menu: use view/edit commands, undo/redo, reimport the selected resource, locate the file in the Resource Browser, or edit a selected prefab.
- `Window` menu: move between tabs, cycle tabs, close the current tab, undo closing a tab, open the Log Console, and open additional Resource Browser panes.
- `Utilities` menu: generate a GUID, produce a file-system dump, and use the Qt introspection tool.
- `Plugins` menu: exposes Resource Manager extension commands such as settings reset/reload, texture/model/material/terrain import tools, editable prefab update tools, bookmark tools, SVN tools, batch processors, resave tools, image set generation, in-game editor tools, engine/game settings, placeable entity registration, behavior-tree validation, XOB search, class generation from layout, localization, linked-resource search, prefab validation, and control-scheme generation.
- `Resource Browser`: use contextual menus, the search bar, search special characters, filters, options, and multiple viewports/tabs to narrow resources before opening a tool-specific editor.
- `Viewport` and `Details / Import Settings`: editors expose selected-resource detail panels, import settings, editable parameters, and sometimes "edit also selected files" behavior for batch-like edits.
- `Log Console`: keep it visible when running import, batch, resave, linked-resource, and validation plugins; many plugin failures are easier to diagnose from the log than from a silent editor state.

Resource Manager Options is a project/module/editor settings hub:
- `Game Project` general fields include `ID`, `GUID`, `TITLE`, `Dependencies`, `Engine Settings Path`, `Game Settings Path`, `Brush Library Path`, and `Welcome Screen Config`.
- Per-platform settings include `World File`, `SplashScreen`, `Engine`, and `Platform Hardware`.
- Module/settings families include defaults, audio, terrain generation material, user interface, Resource Manager, postprocess, material system, video, grass material, input device, graphics quality, water pool material, display, pipeline, clustered tiling, script project manager, navmesh manager, distant shadows quality profiles, environment quality profiles, input manager, physics, wetness render, Chimera global config, setting profiles, audio global config, menu manager, shadow quality profiles, and widget manager.
- Workbench settings include Qt stylesheet, SVN integration, auto-rebuild scripts, FPS limit, net API enablement, mouse inversion, `enfusion://` protocol registration, and export settings.
- Editor-specific option groups exist for World Editor, Animation Editor, Script Editor, Audio Editor, Behavior Editor, and shortcuts. Use this page to identify the setting surface; use the owning editor/domain reference before changing the system behavior behind it.

File Types is the extension router. Use it to decide which Resource Manager editor or reference owner should be opened next:
- Project, package, and metadata extensions: `.gproj`, `.meta`, `.rdb`, `.pak`, `.sig`, `.siga`, `.desc`.
- Script, config, and data extensions: `.c`, `.conf`, `.ct`, `.ent`.
- Prefab, world, terrain, and nav-related extensions: `.et`, `.layer`, `.terr`, `.topo`, `.nmn`, `.bterr`, `.bttile`, `.ttile`, `.asc`.
- UI, localization, and font extensions: `.layout`, `.imageset`, `.styles`, `.st`, `.fnt`, `.ttf`.
- Model, animation, physics, and material extensions: `.xob`, `.fbx`, `.anm`, `.agr`, `.ast`, `.asi`, `.asy`, `.afm`, `.ragdoll`, `.physmat`, `.gamemat`, `.emat`.
- Texture, image, audio, particle, and signal extensions: `.dds`, `.edds`, `.txa`, `.txo`, `.wav`, `.acp`, `.ptc`, `.snd`, `.smap`.
- Specialized extensions: `.adeb`, `.ae`, `.agf`, `.aw`, `.bt`, `.pap`, `.pre`, `.stars`, `.vhcsurf`.

Config Editor owns the editor surface for config classes and values:
- `Main Interface`: use the search field to locate data, inspect class and parent, and edit values.
- `Value Interface`: arrays and sliders are separate value-control shapes; do not treat them as plain text fields.
- `Advanced Usage`: config-prefab-from-config, inherited config files, and filling by config are editor workflows. The data model behind config classes and BaseContainer belongs to `prefabs-configs-containers-and-catalogs.md`.

Layout Editor owns UI layout editing controls, not runtime UI behavior:
- `Top Bar`: snap to grid while dragging, draw grid, deselect, live preview, border visibility, grid size, anchor grid size, zoom, root size, slot source, root DPI scaling, language, and compact mode.
- `Hierarchy`: use contextual menu actions to convert, wrap, expand/collapse hierarchy, copy, paste, duplicate, delete, rename, open prefab, save as prefab, or deselect.
- `Properties Tab`: use property-grid options to show only modified properties, expand/collapse groups, copy/paste all properties, or copy/paste one group.
- Major property groups include transform, slot, anchor, size-to-content, Z order, rotation, pivot, behavior, enabled/visible flags, pixel-perfect flag, opacity, clipping, tooltip, cursor ignore, appearance, color, inherited color, text, font size, minimum font size, widget, style, focus behavior, script, navigation, events, classes, and last-used prefabs.
- UI scripting, HUD behavior, dialogs, menus, and widget class design belong to `ui-layouts-dialogs-and-menus.md`; this reference only owns how the Layout Editor exposes layout data.

Imageset Editor owns texture-to-quad authoring:
- `Top Bar`: reload image, reset view, reset zoom.
- `ImageSet Tab`: select texture, add/remove data, and create entries from files.
- `Quads Tab`: manage quads list, add a quad, add a 3x3 quad, add a group, delete entries, and edit quad properties.
- Quad properties include name, position, dimensions, horizontal tile, vertical tile, and group.
- Import settings are part of the Resource Manager editor surface; UI use of imagesets belongs to the UI reference.

Model Editor owns model inspection and import surfaces:
- `Horizontal bar` and `Viewport UI`: view, shading, lighting, channels, overlays, wireframe, vertex normals, and vertex highlight.
- `Options` and scene preset controls: search bar, preset names, active preset, scene settings, grid, grid color, cell count, cell scale, ground, ground material, compass, axis, wireframe settings, overlay settings, environment colors/map/exposure, lighting color/exposure/size/rotation, camera exposure/FOV/position/angles, postprocessing, and preset save/new buttons.
- `Details Tab`: materials, LODs, selected LOD forcing, collider view, hide mesh, center of mass, collider outlines, transparent colliders, high-contrast background, collider filters, invalid-shape display, layers, center of mass, vertices, faces, colliders, occluders, projected occluders, land contacts, bones, and runtime details.
- `Import Settings Tab`: general presence/source/common settings, miscellaneous merge/export/legacy support settings, transform, visual settings, LOD removal, optimization, material assigns, physics, merged trimeshes, physical material assigns, geometry params, and COM autocenter.
- Asset import, collision, LOD policy, prop creation, and model QA are owned by `asset-import-models-materials-and-props.md`; use this reference to locate the editor field and the asset reference to decide the correct value.

Texture Editor owns texture inspection and import surfaces:
- `Horizontal Bar`: preview background, alpha mask, pick color to clipboard, lock texture settings, color scheme, brightness, channel toggle/isolation, filter mode, point/bilinear/trilinear filtering, mip level, auto scale-to-fit, and depth.
- `Details Tab`: texture properties, histogram, color graph, and reset.
- `Import Settings Tab`: target format, format compression, compression threshold, mip removal, max size, conversion, conversion quality, original pixel bit depth, color space, contains mips, generate mips, mip map function/filter, alpha fade start/end/value, tiled texture, cubemap generation, and volume texture.
- Texture authoring and material workflow belong to the asset import/material reference; this reference owns the Resource Manager editor controls.

Material Editor has a wiki page but little concrete detail in the indexed source. Treat it as a Resource Manager editor entry point and route material behavior, material resource setup, and material validation to `asset-import-models-materials-and-props.md`.

Data To Spreadsheet is a Resource Manager plugin for exporting and importing structured data through spreadsheet-style templates:
- The interface exposes `Prefab Config`, `Print To Console`, `Comma As Delimiter`, `Use Selection From Config`, `Import`, and `Export`.
- The `Spreadsheet Parser` works with a prefabs array, attributes array, and a list of attributes.
- Template record families include `SCR_DataToSpreadsheetTemplatesAttribute`, `SCR_DataToSpreadsheetTemplatesComponent`, `SCR_DataToSpreadsheetTemplatesObject`, `SCR_DataToSpreadsheetTemplatesObjectIndex`, and `SCR_DataToSpreadsheetTemplatesObjectArray`.
- The wiki includes example workflows for extracting ammo data from object arrays and importing/exporting spreadsheets. Preserve the distinction between selecting the correct prefab/config source, choosing attributes, exporting for review, then importing only after validating the data shape.

Resource Manager utility plugins are operational tools:
- `Generate Class From Layout`: run it from Resource Manager for selected layout resources when a script class needs to mirror layout structure. Verify generated code through API/search references before editing it into gameplay logic.
- `Batch Resource Processor`: use the plugin UI/parameters or command-line surface to process selected resource families. Keep the Log Console open and verify output files after running it.
- `Batch Texture Processor`: use plugin parameters for texture processing batches; validate texture import settings and output formats afterward.
- `Find Linked Resources`: use it to understand dependency/link relationships from a selected resource. Treat output as routing evidence before editing dependencies.
- `Resave Plugins`: use resave and resave-meta tooling when resources or metadata need to be regenerated. Verify the affected resource set and avoid broad resaves without a concrete reason.
- `Resource Manager Plugin`: this wiki page identifies setup, contextual menu placement, and ResourceManager module API surfaces. Full plugin authoring, registration, and Workbench extension patterns belong to `workbench-plugins-and-editor-tools.md`.

## Terms And Concepts

- Resource Manager: Workbench module for browsing, opening, importing, reimporting, editing, saving, validating, and running plugin actions on resources.
- Resource Browser: pane for searching, filtering, contextual actions, and opening resources into editor tabs.
- Resource viewport: editor/tab area for the currently opened resource, such as model, texture, layout, config, imageset, or plugin UI.
- Details / Import Settings: editor-side properties for the selected resource and its import pipeline; changing these can alter generated resource output.
- Resource Manager Options: project, module, Workbench, and editor settings surface.
- File type: extension-based routing signal for the resource editor and the owning reference.
- Config Editor: Resource Manager editor for class/parent/value inspection and config value editing.
- Layout Editor: Resource Manager editor for `.layout` resource structure and properties.
- Imageset Editor: Resource Manager editor for `.imageset` textures, quads, groups, and import settings.
- Model Editor: Resource Manager editor for model view, materials, LODs, colliders, bones, runtime details, and model import settings.
- Texture Editor: Resource Manager editor for texture preview, channel/mip inspection, and texture import settings.
- Data To Spreadsheet: Resource Manager plugin for exporting/importing structured prefab/config data through template definitions.
- ResourceManagerPlugin: API/plugin base surface for Resource Manager-specific plugins; verify exact usage through query output.

## Workbench / Resource / Data Surfaces

Primary Workbench surfaces:
- Resource Manager window and menus.
- Resource Browser panes and contextual menus.
- Resource viewports/editor tabs.
- Log Console.
- Details and Import Settings panel.
- Resource Manager Options dialog.
- Plugin entries under the Resource Manager plugin menu.

Primary resource/editor surfaces:
- `.conf` and related config resources open through Config Editor when Resource Manager owns the edit surface.
- `.layout` resources open through Layout Editor.
- `.imageset` resources open through Imageset Editor.
- `.xob`/model output resources and model imports open through Model Editor.
- `.edds`/texture resources and texture imports open through Texture Editor.
- Data To Spreadsheet, Batch Resource Processor, Batch Texture Processor, Find Linked Resources, Resave Plugins, and Generate Class From Layout are plugin surfaces, not gameplay systems.

Handoff boundaries:
- Use `prefabs-configs-containers-and-catalogs.md` before changing config class design, BaseContainer semantics, prefab inheritance, EntityCatalog, or ResourceName usage beyond Resource Manager routing.
- Use `asset-import-models-materials-and-props.md` before deciding model, texture, material, collision, LOD, or prop pipeline values.
- Use `ui-layouts-dialogs-and-menus.md` before implementing widget scripts, HUD behavior, dialog logic, menu logic, or UI layout runtime behavior.
- Use `workbench-plugins-and-editor-tools.md` before creating or registering a Resource Manager plugin.
- Use `mod-projects-addons-workshop.md` before changing project identity, addon layout, publishing, or packaging behavior.

## Required Workflows

Resource lookup workflow:
1. Identify the intended resource family from the task: config, prefab, layout, imageset, model, texture, material, terrain, script, audio, or package.
2. Use the File Types routing list to identify likely extensions.
3. Search with Resource Browser using exact names first, then filters and special characters.
4. Open the resource into the appropriate editor viewport.
5. Inspect Details / Import Settings before changing values.
6. Keep the Log Console visible when running imports, resaves, processors, or validation plugins.
7. If the change touches a domain workflow, switch to the owning reference before editing.
8. Use query commands for exact API or source-example verification before writing code around the resource.

Resource Manager Options workflow:
1. Identify whether the setting is project-wide, platform-specific, module-specific, Workbench-specific, editor-specific, or shortcut-related.
2. For project identity fields such as ID, GUID, TITLE, dependencies, and settings paths, cross-check `mod-projects-addons-workshop.md`.
3. For module settings, identify the module family before changing values.
4. For Workbench settings such as SVN, auto-rebuild scripts, FPS limit, net API, protocol registration, or export settings, validate impact in Workbench after changing.
5. For editor settings, open the owning editor reference before assuming behavior.

Config Editor workflow:
1. Locate the config resource in Resource Browser.
2. Open it in Config Editor.
3. Use the search field to narrow classes or values.
4. Check the class and parent before editing inherited values.
5. Use the correct value control: array, slider, or plain value.
6. For advanced config-prefab or inherited-config workflows, switch to `prefabs-configs-containers-and-catalogs.md` before changing the data model.

Layout Editor workflow:
1. Open the `.layout` resource.
2. Use top-bar controls for grid, snapping, zoom, preview, root size, DPI scaling, language, and compact mode.
3. Use hierarchy/context menu actions for structural edits.
4. Use Properties Tab groups to adjust transform, slot, anchor, behavior, appearance, text, widget, style, script, navigation, events, classes, or prefab lists.
5. Use Generate Class From Layout only after confirming the layout structure is stable.
6. Route runtime widget/script behavior to `ui-layouts-dialogs-and-menus.md`.

Imageset Editor workflow:
1. Open the `.imageset` resource.
2. Confirm the source texture.
3. Use image reset/zoom controls to inspect the source.
4. Add/remove entries or import from files as needed.
5. Use Quads Tab to add individual quads, 3x3 quads, groups, and quad properties.
6. Validate position, dimensions, tiling, and grouping before using the imageset in UI.

Model Editor workflow:
1. Open the model resource in Model Editor.
2. Use viewport view/shading/lighting/channel/overlay controls to inspect geometry and materials.
3. Use scene preset and environment controls to make visual issues visible.
4. Inspect materials, LODs, colliders, layers, center of mass, vertices, faces, occluders, land contacts, bones, and runtime details.
5. Review import settings before changing transform, visual, physics, material, or geometry parameters.
6. Route asset-pipeline decisions to `asset-import-models-materials-and-props.md`.

Texture Editor workflow:
1. Open the texture resource.
2. Inspect preview background, alpha, color, channel isolation, filtering, mip level, and depth.
3. Review texture properties, histogram, and color graph.
4. Review import settings for target format, compression, max size, conversion, color space, mip generation, tiling, cubemap, and volume settings.
5. Route texture/material pipeline decisions to `asset-import-models-materials-and-props.md`.

Data To Spreadsheet workflow:
1. Select or configure the prefab/config source.
2. Choose whether to print to console, use comma delimiter, and use the selection from config.
3. Define templates and attributes through the plugin’s template records.
4. Export first and inspect the output.
5. Import only after the spreadsheet shape matches the expected prefab/config/template structure.
6. Verify the resulting resources in Resource Manager and through runtime/editor checks relevant to the owning domain.

Utility plugin workflow:
1. Narrow the target resources first.
2. Read plugin-specific parameters before execution.
3. Keep Log Console visible.
4. Run on a bounded selection where possible.
5. Inspect plugin output, affected files, and Resource Browser state.
6. Run domain-specific validation before committing to the result.

## Configuration Fields And Tables

Resource Manager tables/field groups to preserve:
- Window Menu table: Workbench actions, editor actions, window/tab actions, utilities, plugins, and tool-specific commands.
- Resource Browser contextual menu table: available file/resource actions depend on selection and resource type.
- Resource Browser special-character table: search syntax can change result shape; prefer exact resource names before broad token searches.
- Viewport Tabs table: tab actions control which resource/editor is active.
- General Shortcuts table: use shortcuts for Resource Manager navigation and editing only after confirming focus is in Resource Manager.

Resource Manager Options field groups:
- Game Project general parameters: `ID`, `GUID`, `TITLE`, `Dependencies`, `Engine Settings Path`, `Game Settings Path`, `Brush Library Path`, `Welcome Screen Config`.
- Per-platform parameters: `World File`, `SplashScreen`, `Engine`, `Platform Hardware`.
- Settings families: default, audio, terrain, UI, Resource Manager, postprocess, material, video, grass, input device, graphics quality, water pool, display, pipeline, clustered tiling, script project manager, navmesh, shadows, environment, input manager, physics, wetness, Chimera global, setting profiles, audio global, menu manager, widget manager.
- Workbench settings: Qt stylesheet, SVN integration, auto-rebuild scripts, FPS limit, net API, invert mouse, `enfusion://` protocol, export settings.
- Editor settings: World Editor, Animation Editor, Script Editor, Audio Editor, Behavior Editor, and shortcuts.

File-type routing table:
- `.gproj`: addon/project file. Use project/addon reference.
- `.c`: Enfusion script file. Use scripting/language references and API lookup.
- `.conf`: config resource. Use Config Editor for editing surface and prefab/config reference for data model.
- `.ct`: config type/resource family; verify exact meaning from File Types and Resource Manager.
- `.ent`: entity-related resource; route to entity/component or prefab owner.
- `.et`: prefab/entity template resource. Use prefab/config and entity references.
- `.layout`: UI layout resource. Use Layout Editor here, then UI reference for runtime behavior.
- `.imageset`: UI image set resource. Use Imageset Editor here, then UI/asset references for use.
- `.xob` and `.fbx`: model/import-related resources. Use Model Editor here, then asset import reference.
- `.emat`, `.gamemat`, `.physmat`: material/physical material resources. Use Resource Manager surface here, then asset/material owner.
- `.dds`, `.edds`, `.txa`, `.txo`: texture/image resources. Use Texture Editor here, then asset/material owner.
- `.wav`, `.acp`, `.snd`, `.smap`: audio/sound resources. Route to audio reference for behavior.
- `.terr`, `.topo`, `.layer`, `.nmn`, `.bterr`, `.bttile`, `.ttile`: terrain/world/nav resources. Route to terrain/world references.
- `.anm`, `.agr`, `.ast`, `.asi`, `.asy`, `.afm`: animation resources. Route to animation reference.
- `.bt`: behavior tree/resource. Route to AI/behavior reference.
- `.pak`, `.rdb`, `.sig`, `.siga`, `.meta`, `.desc`: package/database/signature/metadata resources. Route to project/packaging reference before editing or publishing assumptions.

Editor-specific field groups:
- Config Editor: search field, class, parent, values, arrays, sliders, inherited config, config prefab from config, filling by config.
- Layout Editor: top bar, hierarchy, contextual menu, property grid, transform, slot, anchor, size-to-content, Z order, rotation, pivot, behavior, appearance, text, widget, style, script, navigation, events.
- Imageset Editor: texture, add/remove, from files, quads list, add, add 3x3, add group, delete, quad name, position, dimensions, horizontal/vertical tile, group.
- Model Editor: view, shading, lighting, channels, overlays, wireframe, normals, scene presets, grid, ground, environment, lighting, camera, postprocessing, materials, LODs, colliders, bones, runtime details, import settings.
- Texture Editor: preview background, alpha mask, color pick, lock texture settings, color scheme, brightness, channels, filter modes, mip level, depth, texture properties, histogram, color graph, target format, compression, max size, conversion, color space, mip generation, cubemap, volume texture.
- Data To Spreadsheet: Prefab Config, Print To Console, Comma As Delimiter, Use Selection From Config, Import, Export, Prefabs Array, Attributes Array, template records, and attribute list.

## Procedures And Ordered Steps

To diagnose "I cannot find/open the resource":
1. Identify the expected extension.
2. Search the Resource Browser by exact file stem.
3. Use Resource Browser filters for extension/resource type.
4. If needed, use search special characters from the Resource Manager page.
5. Open a second Resource Browser viewport if comparing locations.
6. Use `Locate file in resource browser` when starting from an open editor tab.
7. If the resource exists but opens in the wrong workflow, route by File Types and owning reference.

To modify import settings safely:
1. Open the resource in the correct editor.
2. Read Details / Import Settings before editing.
3. Confirm whether the setting applies to one selected file or multiple selected files.
4. Change the smallest necessary setting.
5. Reimport only the affected resource.
6. Watch Log Console for import errors.
7. Inspect generated output in the editor.
8. Run domain validation from the owning reference.

To run Batch Resource Processor:
1. Narrow the selected resources.
2. Open the Batch Resource Processor plugin.
3. Review plugin parameters.
4. Prefer a bounded selection over a broad project run.
5. Execute the process.
6. Review Log Console and generated output.
7. Verify affected resources in Resource Browser.

To run Batch Texture Processor:
1. Narrow selected texture resources.
2. Open Batch Texture Processor.
3. Review parameters and texture import settings.
4. Run on the intended selection.
5. Confirm output format, compression, mips, and color space in Texture Editor.

To find linked resources:
1. Select the source resource.
2. Run Find Linked Resources.
3. Read the output as dependency/routing evidence.
4. Open linked resources before editing.
5. Use the owning domain reference before changing dependencies.

To use Resave Plugins:
1. Determine whether resource data or metadata needs the resave.
2. Select the intended resource set.
3. Run the correct resave/resave-meta plugin.
4. Review Log Console.
5. Verify resource metadata and affected editor output.
6. Avoid broad resaves unless the task explicitly requires it.

To generate a class from a layout:
1. Stabilize the `.layout` structure in Layout Editor.
2. Ensure widget names/classes are intentional.
3. Run Generate Class From Layout.
4. Verify the generated output shape.
5. Use `api-lookup-and-common-symbols.md` and UI reference lookup commands before wiring runtime UI behavior.

To use Data To Spreadsheet:
1. Select the relevant prefab/config source.
2. Configure template records and attribute selection.
3. Choose delimiter and selection behavior.
4. Export first.
5. Review the spreadsheet shape and values.
6. Import only after confirming the template matches the intended data structure.
7. Reopen affected resources and validate domain behavior.

## Warnings And Failure Modes

- Do not treat Resource Manager as a substitute for domain references. It shows where data is edited; it does not decide correct prefab, weapon, vehicle, UI, animation, audio, terrain, or server behavior.
- Do not edit project identity fields such as `ID`, `GUID`, `TITLE`, dependencies, or settings paths without checking addon/project ownership.
- Do not run broad batch processors or resave plugins without a bounded resource set and a concrete reason.
- Do not assume a selected file and "edit also selected files" behavior affects only one resource.
- Do not ignore Log Console when using imports, processors, resaves, linked-resource tools, or validation plugins.
- Do not change import settings from memory. Texture/model import settings are easy to misread and must be checked in the editor and domain reference.
- Do not treat a file extension as the full workflow. `.layout`, `.et`, `.conf`, `.xob`, `.emat`, and `.edds` route to different owners after the Resource Manager surface is understood.
- Do not copy generated class output from Layout Editor into gameplay code without querying exact APIs and checking UI reference behavior.
- Do not treat Data To Spreadsheet import as harmless. It can write structured data back into resources and should be verified against templates and selected attributes.
- Do not confuse Resource Manager plugin use with Workbench plugin authoring. Using a plugin is owned here; creating one belongs to the Workbench plugin reference.
- Do not rely on sample resource layout alone. Samples show structure, but current wiki workflow and query-verified API routes are the authority.

## API Lookup Keys

Use these lookup keys when Resource Manager work touches script/API behavior:
- Resource Manager/plugin surfaces: `ResourceManager`, `ResourceManagerPlugin`, `ResourceBrowser`, `WorkbenchPlugin`, `WorkbenchPluginAttribute`.
- Resource references and loading: `ResourceName`, `ResourceNamePicker`, `Resource.Load`, `Resource`.
- UI layout resource routing: `CreateWidgets`, `.layout`, `UIWidgets.ResourceNamePicker`, `ScriptedWidgetComponent`.
- Data To Spreadsheet: `SCR_DataToSpreadsheetPlugin`, `SCR_DataToSpreadsheetTemplates`, `SCR_DataToSpreadsheetTemplatesAttribute`, `SCR_DataToSpreadsheetTemplatesComponent`, `SCR_DataToSpreadsheetTemplatesObject`, `SCR_DataToSpreadsheetTemplatesObjectIndex`, `SCR_DataToSpreadsheetTemplatesObjectArray`, `SCR_EDataToSpreadsheetDataType`.
- Resource Manager examples/tools: `SCR_ImageSetGenerator`, `TextureImportPlugin`, `BatchTextureProcessorPlugin`, `ResaveMetaPlugin`, `ResavePlugin`, `ResourceImportPlugin`, `TerrainImportPlugin`, `SCR_FindResourcesPlugin`, `SCR_VCSLogResourceManagerPlugin`.

Do not assume any method signature from these names. Query exact symbol, method, inheritance, example, and snippet data before writing code.

## Game-Data Query Commands

Use Resource Manager file and plugin lookups first:

```powershell
py -3 scripts\query-reforger-data.py files ResourceManager --limit 10
py -3 scripts\query-reforger-data.py files ResourceManagerPlugin --limit 10
py -3 scripts\query-reforger-data.py files ResourceName --limit 10
```

Use exact symbols when writing Workbench or Resource Manager plugin code:

```powershell
py -3 scripts\query-reforger-data.py symbol ResourceManager --exact
py -3 scripts\query-reforger-data.py symbol ResourceManagerPlugin --kind class --exact
py -3 scripts\query-reforger-data.py symbol WorkbenchPlugin --kind class --exact
py -3 scripts\query-reforger-data.py symbol ResourceName --exact
```

Use example searches for resource picker, resource loading, and UI layout resource patterns:

```powershell
py -3 scripts\query-reforger-data.py examples resource-loading --subtopic resource-picker-config --limit 8
py -3 scripts\query-reforger-data.py examples ui --subtopic ui-layout-resource --limit 8
py -3 scripts\query-reforger-data.py files ResourceNamePicker --limit 10
py -3 scripts\query-reforger-data.py files SCR_DataToSpreadsheet --limit 10
```

Use snippets only after a query result gives an exact file and line:

```powershell
py -3 scripts\query-reforger-data.py snippet scripts/WorkbenchGame/ResourceManager/SCR_FindResourcesPlugin.c --line 1 --context 30
py -3 scripts\query-reforger-data.py snippet scripts/WorkbenchGame/ResourceManager/SCR_DataToSpreadsheet.c --line 1 --context 30
py -3 scripts\query-reforger-data.py snippet scripts/Workbench/SCR_ImageSetGenerator.c --line 1 --context 30
```

If a query returns broad or noisy results, narrow by exact symbol, owner, topic, subtopic, generated-only, or handwritten-only before opening snippets.

## Examples And Samples

Use examples as routing and pattern evidence:
- Resource Manager plugin examples: query `files ResourceManagerPlugin` to find generated API truth and handwritten plugin examples.
- Data To Spreadsheet examples: query `files SCR_DataToSpreadsheet` and then inspect bounded snippets.
- Image set generation examples: query `files SCR_ImageSetGenerator`.
- Texture import examples: query `files TextureImportPlugin` or `files BatchTextureProcessorPlugin`.
- Resource picker examples: query `examples resource-loading --subtopic resource-picker-config`.
- UI layout resource examples: query `examples ui --subtopic ui-layout-resource`.

Official sample folders show resource layout signals:
- `SampleMod_Main`: representative project, config, prefab, material, texture, terrain, and UI texture resource layout.
- `SampleMod_ModdedScript`: script/project layout signal.
- `SampleMod_ModdedWeapon`: weapon configs, prefabs, material, texture, and inventory catalog layout signal.
- `SampleMod_ModdedCar`: vehicle prefab, material, editor preview, localization, and config layout signal.
- `SampleMod_AnimationWorkshop` and `SampleMod_CinematicTutorial`: project and resource-layout signals for animation/cinematic assets.

Do not copy sample bodies into a reference or assume sample code signatures are current. Use sample layout for orientation, then verify exact API through query commands.

## Follow-Up Keywords

Resource Manager, Resource Browser, ResourceManager, ResourceManagerPlugin, ResourceName, ResourceNamePicker, Resource.Load, WorkbenchPlugin, WorkbenchPluginAttribute, Config Editor, Layout Editor, Imageset Editor, Model Editor, Texture Editor, Material Editor, Data To Spreadsheet, Batch Resource Processor, Batch Texture Processor, Find Linked Resources, Resave Plugins, Generate Class From Layout, ResourceImportPlugin, TerrainImportPlugin, TextureImportPlugin, SCR_DataToSpreadsheet, SCR_ImageSetGenerator, `.conf`, `.et`, `.layout`, `.imageset`, `.xob`, `.fbx`, `.emat`, `.edds`, `.gproj`, `.meta`, import settings, Log Console, Details panel, Resource Manager Options.

## Verification

Before finalizing Resource Manager-related work:
1. Confirm the task belongs to this reference; if it is actually prefab modeling, asset import, UI implementation, plugin authoring, terrain/world, packaging, or runtime behavior, open the owning reference.
2. Confirm the exact file type and editor surface.
3. Reopen the resource in Resource Manager after edits.
4. Check Details / Import Settings for unintended changes.
5. Check Log Console after imports, processors, resaves, linked-resource searches, validation, or class generation.
6. If code was changed, run the exact query commands for every uncertain class/method/attribute before writing or reviewing the code.
7. If resources were generated or imported, inspect the output in the correct editor.
8. If the edited resource feeds a domain workflow, run the domain verification from the owning reference.
9. If the task affects project settings, dependencies, or publishing, verify through addon/project packaging checks.
10. State any remaining Workbench-only, runtime, or domain validation that was not possible.

## Official Wiki Links

- Resource Manager: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager
- Resource Manager: Options: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Options
- File Types: https://community.bistudio.com/wiki/Arma_Reforger:File_Types
- Resource Manager: Config Editor: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Config_Editor
- Resource Manager: Layout Editor: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Layout_Editor
- Resource Manager: Imageset Editor: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Imageset_Editor
- Resource Manager: Model Editor: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Model_Editor
- Resource Manager: Texture Editor: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Texture_Editor
- Resource Manager: Material Editor: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Material_Editor
- Resource Manager: Data To Spreadsheet: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Data_To_Spreadsheet
- Resource Manager: Generate Class From Layout Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Generate_Class_From_Layout_Plugin
- Resource Manager: Batch Resource Processor Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Batch_Resource_Processor_Plugin
- Resource Manager: Batch Texture Processor Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Batch_Texture_Processor_Plugin
- Resource Manager: Find Linked Resources Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Find_Linked_Resources_Plugin
- Resource Manager: Resave Plugins: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Resave_Plugins
- Resource Manager Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager_Plugin
- Resource Manager Plugins category: https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Official_Tools/Resource_Manager_Plugins
- Resource Manager Viewports category: https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Official_Tools/Resource_Manager_Viewports

## Usefulness Score

Score: 93/100

- Wiki coverage: 28/30. All owned Resource Manager, Options, File Types, editor, and utility plugin pages are named, represented, and linked. Material Editor is partial because the source page is sparse, and the score reflects that limited source detail.
- Operational detail: 15/15. The reference preserves menu surfaces, Resource Browser usage, editor controls, option families, file-type routing, import settings, plugin workflows, and ordered checks.
- API lookup usefulness: 14/15. Resource Manager, plugin, resource-loading, resource-picker, UI layout, and Data To Spreadsheet lookup routes are included. Exact signatures remain intentionally delegated to query output.
- Example grounding: 9/10. Official samples and game-source query routes are included as layout/pattern signals without copying bodies. Some sample-specific Resource Manager screenshots are not available as runtime evidence.
- Codex task usefulness: 14/15. Codex can route common tasks such as finding a resource, choosing an editor, generating layout classes, using Data To Spreadsheet, and checking Resource Manager plugin APIs without guessing. Deeper domain tasks intentionally cross-link to owner references.
- Context efficiency: 9/10. The file is dense and navigable, with strict split boundaries. It is long because the owned wiki family is editor-surface heavy.
- Verification guidance: 4/5. Workbench/editor/log/import validation is concrete; runtime validation is delegated to domain owners where appropriate.

Category-fit check:
- Source family complete: pass. Resource Manager pages, Options, File Types, editor pages, Data To Spreadsheet, utility plugins, and plugin category routes are covered.
- No owned page missing: pass. All owned primary pages reviewed are listed in Source Inventory.
- Split boundary justified: pass. Prefab/config modeling, asset import, UI runtime behavior, Workbench plugin authoring, terrain/world, publishing, and server/runtime work are explicitly routed elsewhere.
- Cross-links present: pass. Nearby workflows route to their owning references.
- Task route clear: pass. Codex can start from file type/editor intent, query exact API when needed, and open domain references only when the task leaves the Resource Manager surface.

Missed coverage and exclusions:
- Material Editor has only sparse indexed source detail, so the reference records the entry point and routes material workflow to the asset/material owner.
- Full Workbench plugin authoring is intentionally excluded from this source-owning reference and routed to `workbench-plugins-and-editor-tools.md`.
- Full prefab/config modeling, asset import QA, UI implementation, terrain/world, addon packaging, and server/runtime workflows are excluded to avoid duplicate ownership.
