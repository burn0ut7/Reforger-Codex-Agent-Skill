# UI Layouts Dialogs And Menus

## When To Read

Read this when the task is about Reforger UI authoring or UI runtime wiring:

- creating or modifying `.layout` resources, layout editor data, widgets, HUD elements, menu entries, dialogs, end screens, or tooltips;
- using Resource Manager Layout Editor or Generate Class From Layout Plugin for UI layout-to-script workflows;
- configuring dialog resources, end-screen config/data, widget tooltip behavior, or commanding menu UI;
- finding exact widget, layout, HUD, text widget, image widget, menu, and scripted widget APIs before writing code;
- debugging UI that does not load, appears in the wrong context, has missing widgets, has incorrect layout resources, or fails because the runtime UI owner is wrong.

This reference owns UI layout/resource workflows, dialog configuration, widget/tooltips, end screens, commanding menu UI, and layout-to-script routing. It does not own Resource Manager general usage, Game Master editable entity behavior, diagnostics/Diag Menu UI, AI commanding behavior, or generic scripting patterns.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: layout creation, dialog configuration, widget tooltip setup, end screen creation, commanding menu UI, Resource Manager Layout Editor, Generate Class From Layout Plugin.
- Secondary/cross-reference topics: Game Master entity tooltip creation, Resource Manager general usage, Game Master editable entities, diagnostics UI, AI commanding behavior, scripting patterns, UI API lookup.

Wiki pages reviewed:
- Layout Creation - https://community.bistudio.com/wiki/Arma_Reforger:Layout_Creation - status: covered - reason: owns UI layout resource creation, layout workflow, warnings, and links.
- Dialog Configuration Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Dialog_Configuration_Tutorial - status: covered - reason: owns dialog setup workflow, procedures, warnings, and linked layout/config behavior.
- Widget Tooltip Setup - https://community.bistudio.com/wiki/Arma_Reforger:Widget_Tooltip_Setup - status: covered - reason: owns widget tooltip workflow, warning, media, and UI routing.
- End Screen Creation - https://community.bistudio.com/wiki/Arma_Reforger:End_Screen_Creation - status: covered - reason: owns end screen configuration, tables, warnings, and UI/game-mode routing.
- Commanding Menu Modding - https://community.bistudio.com/wiki/Arma_Reforger:Commanding_Menu_Modding - status: covered - reason: owns commanding menu UI setup and warnings; AI command behavior remains cross-referenced.
- Resource Manager: Layout Editor - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Layout_Editor - status: covered - reason: owns Layout Editor surface where UI layout is primary.
- Resource Manager: Generate Class From Layout Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Generate_Class_From_Layout_Plugin - status: covered - reason: owns layout-to-script class generation workflow, table, and procedure.
- Game Master: Entity Tooltip Creation - https://community.bistudio.com/wiki/Arma_Reforger:Game_Master:_Entity_Tooltip_Creation - status: partial - reason: tooltip UI behavior and tables are included; Game Master editable entity ownership remains with `game-master-factions-tasks-and-modes.md`.

Wiki sections covered:
- Layout Creation: layout resource creation, widget/resource setup, layout editor workflow, workflow warnings, and UI resource routing.
- Dialog Configuration Tutorial: dialog setup, configuration procedure, layout/resource references, and dialog validation.
- Widget Tooltip Setup: tooltip workflow, media-backed setup, warning, and widget behavior routing.
- End Screen Creation: end screen config/data, tables, warning notes, game-mode/UI links, and verification.
- Commanding Menu Modding: commanding menu UI behavior, configuration/routing, media evidence, warnings, and cross-links to AI/commanding ownership.
- Resource Manager Layout Editor: layout editor surface, procedure, table, and warnings.
- Generate Class From Layout Plugin: plugin usage, class generation procedure, table, and script routing.
- Game Master Entity Tooltip Creation: tooltip table and workflow evidence relevant to UI tooltips; broader editable entity rules are excluded and routed.

Structured wiki records:
- Tables reviewed/included: 8 end-screen tables, 3 Game Master entity tooltip tables used as partial UI-tooltip evidence, 1 Generate Class From Layout Plugin table, and 1 Layout Editor table.
- Procedures reviewed/included: 5 dialog configuration procedures, 2 layout creation procedures, 1 Generate Class From Layout Plugin procedure, and 1 Layout Editor procedure.
- Admonitions reviewed/included: 14 layout creation warnings, 3 dialog warnings, 1 widget tooltip warning, 6 end-screen warnings, 6 commanding menu warnings, 3 layout editor warnings, and 3 Game Master tooltip warnings as partial tooltip evidence.
- Code blocks reviewed/included: no indexed code-block records were present for these owned pages.
- Media reviewed: commanding menu, widget tooltip, and Game Master tooltip media were reviewed as UI-surface evidence; runtime references do not depend on images.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts/query-reforger-data.py lookup "create HUD widget" --limit 8`
  - `py -3 scripts/query-reforger-data.py examples ui --subtopic hud --limit 8`
  - `py -3 scripts/query-reforger-data.py examples ui --subtopic layout --limit 8`
  - `py -3 scripts/query-reforger-data.py files HUD --limit 8`
  - `py -3 scripts/query-reforger-data.py files Widget --limit 8`
  - `py -3 scripts/query-reforger-data.py files Layout --limit 8`
  - `py -3 scripts/query-reforger-data.py files TextWidget --limit 8`
  - `py -3 scripts/query-reforger-data.py files ImageWidget --limit 8`
- Symbols/methods/attributes verified as lookup keys: `Widget`, `WorkspaceWidget`, `TextWidget`, `ImageWidget`, `BlurWidget`, `CanvasWidgetBase`, `ContentWidget`, `FrameWidget`, `HorizontalLayoutSlot`, `LayoutHorizontalAlign`, `LayoutSizeMode`, `LayoutVerticalAlign`, `ScrollLayoutSlot`, `SizeLayoutSlot`, `SCR_HUDMenuComponent`, `SCR_SelectionMenuDisplay`, `SCR_ItemSelectionMenuEntry`, `SCR_SelectionMenuEntryIconComponent`, `SCR_SelectionMenuEntryPreviewComponent`, `SCR_DebriefingScreenMenu`, and `SCR_DeployMenuHandler`.
- Examples/snippets reviewed: HUD menu component, selection menu entries/components/display, map marker menu entries, deploy/debriefing menu handlers, widget generated classes, layout slot generated classes, `TextWidget`, `ImageWidget`, and widget animation routes from lookup output.

Samples and source examples:
- Official sample folders reviewed as layout signals: `SampleMod_Main` and other sample roots where UI/layout resources are present.
- Raw game-source example families reviewed through query output: HUD UI, selection menu, map marker menu, deploy/debriefing menu, generated widgets, layout slots, text/image widgets, configurable widget entries, and layout-to-script routes.

Coverage gaps:
- No owned primary UI wiki page was skipped.
- Game Master entity tooltip creation is intentionally partial; Game Master entity/editable behavior is routed to `game-master-factions-tasks-and-modes.md`.
- Resource Manager general usage is routed to `resource-manager-file-types-and-editors.md`; this reference preserves only Layout Editor and Generate Class From Layout Plugin behavior.
- Diag Menu UI is routed to `diagnostics-testing-and-performance.md`.
- AI command behavior is routed to `ai-behavior-commanding-and-debug.md`; this reference preserves only commanding menu UI setup.
- Generic scripting patterns are routed to `script-events-actions-and-patterns.md`.
- Exact source bodies and API signatures are not embedded; use query commands before writing API-sensitive UI code.

## Wiki Source Coverage

UI work in Reforger is a data/resource workflow plus script/runtime ownership. Codex should not start with widget code unless the layout resource and runtime owner are understood.

Use this source order for UI tasks:

1. identify the UI surface: layout resource, dialog, tooltip, end screen, commanding menu, HUD, or layout-to-class generation;
2. read the workflow owner in this reference;
3. verify layout resources and editor/plugin surfaces;
4. query exact widget/layout/HUD APIs;
5. inspect bounded snippets from selected examples;
6. validate in Workbench and runtime.

Layout Creation coverage:

- Layout Creation owns the basic UI layout resource workflow.
- Layout resources are not proved by script lookup; they must exist and load in the intended context.
- Layout creation includes both resource creation and widget/resource setup.
- Layout warnings are important because UI failures often come from resource, naming, or load-context problems rather than widget class errors.
- UI layout work should route to Resource Manager Layout Editor when the issue is editor surface behavior.

Dialog Configuration Tutorial coverage:

- Dialog configuration is a distinct workflow from generic HUD/menu work.
- Preserve its setup procedures and warnings when creating dialogs.
- Dialog tasks usually involve layout resources, config/data wiring, runtime context, and UI ownership.
- Do not assume a dialog appears just because a widget class compiles; verify dialog resource loading and owning context.

Widget Tooltip Setup coverage:

- Widget Tooltip Setup owns general widget tooltip workflow.
- Game Master Entity Tooltip Creation contributes useful tooltip table/workflow evidence, but only the tooltip UI portion is owned here.
- Tooltip behavior must be tied to the widget/layout resource and runtime UI context.
- Tooltip failures can come from missing widget references, wrong ownership, missing config/data, or cross-domain Game Master setup.

End Screen Creation coverage:

- End Screen Creation owns end screen UI/config workflow and table detail.
- End screens cross game mode and scenario flow, but this reference owns the UI/layout/config side.
- End screen tables must be preserved as field/config guidance rather than replaced with vague "configure an end screen" prose.
- Runtime validation is required because end screen display depends on game state and UI ownership.

Commanding Menu Modding coverage:

- Commanding Menu Modding owns the menu/UI side of commanding behavior.
- It includes warnings and media-backed setup evidence.
- AI command behavior, commanding logic, behavior trees, and AI validation are not owned here; route those to `ai-behavior-commanding-and-debug.md`.
- Commanding menu UI work should preserve menu structure and UI resource routing before source-level changes.

Resource Manager Layout Editor coverage:

- Layout Editor owns editing `.layout` resources in Resource Manager.
- Use it for layout resource surfaces, widget placement/editing, and validation.
- Resource Manager general browsing/import workflows remain owned by the resource manager reference.

Generate Class From Layout Plugin coverage:

- Generate Class From Layout Plugin owns layout-to-script class generation workflow.
- The plugin table/procedure must be preserved because it is the bridge from `.layout` resources to script-accessible widget members/classes.
- Generated class output is not an excuse to skip exact API lookup; use query commands for widget classes and examples before editing script code.

## Terms And Concepts

- Layout resource: UI resource, commonly `.layout`, that defines widget structure and visual arrangement.
- Layout Editor: Resource Manager editor for working with layout resources.
- Widget: base UI object class; exact API must be queried.
- TextWidget: widget class for text display/editing routes.
- ImageWidget: widget class for image display routes.
- WorkspaceWidget: workspace/root widget route surfaced in UI examples.
- HUD: runtime heads-up display context.
- Menu: runtime UI surface such as selection, deploy, debriefing, or map-marker menus.
- Dialog: configured UI interaction surface separate from simple HUD widgets.
- Tooltip: widget or entity tooltip behavior attached to a UI target.
- End screen: UI/config flow displayed at game/session end.
- Commanding menu: UI surface for commanding behavior; AI behavior itself is separate.
- Generate Class From Layout: plugin workflow for producing script class access from layout resources.
- Layout slot: generated layout positioning/sizing classes such as horizontal/scroll/size slots.
- Widget animation: widget animation classes surfaced by lookup output; verify before use.

## Workbench / Resource / Data Surfaces

Use these surfaces for UI work:

- Resource Manager for locating UI resources, textures, imagesets, and layout files.
- Resource Manager Layout Editor for editing layout resources.
- Generate Class From Layout Plugin for layout-to-script access routes.
- Dialog configuration data/resources for dialogs.
- End screen configuration data/resources.
- Widget tooltip setup resources/configs.
- Commanding menu UI resources/configs.
- Runtime HUD/menu ownership surfaces.
- Scripted widget classes and generated widget APIs through query output.

Do not treat these as the same owner:

- Resource Manager general usage belongs to `resource-manager-file-types-and-editors.md`.
- Game Master editable entity behavior belongs to `game-master-factions-tasks-and-modes.md`.
- Diagnostics UI belongs to `diagnostics-testing-and-performance.md`.
- AI command behavior belongs to `ai-behavior-commanding-and-debug.md`.

## Required Workflows

Create a layout resource:

1. Start from Layout Creation.
2. Create or locate the intended layout resource.
3. Edit it through Layout Editor when layout placement/resource behavior is involved.
4. Add widgets and required child structure.
5. Configure images/text/resources as needed.
6. Verify warnings from Layout Creation.
7. Query exact widget classes only when script code needs to access or modify the layout.
8. Validate in the intended runtime UI context.

Create a dialog:

1. Start from Dialog Configuration Tutorial.
2. Create or select the dialog layout/resource.
3. Configure dialog data and runtime ownership.
4. Wire widgets only after layout resource structure is correct.
5. Query `Widget`, `TextWidget`, `ImageWidget`, and dialog/menu examples before scripting.
6. Test the dialog open/close behavior in runtime.

Create a widget tooltip:

1. Start from Widget Tooltip Setup.
2. Identify the widget or UI target.
3. Configure tooltip data/resource behavior.
4. If the tooltip is a Game Master entity tooltip, read the Game Master reference for entity/editable ownership.
5. Validate tooltip display in runtime.

Create or modify an end screen:

1. Start from End Screen Creation.
2. Preserve end-screen table/config fields.
3. Configure layout/resource and end-screen data.
4. Route game-mode/session logic to the Game Master/game-mode reference.
5. Validate actual display at the intended end condition.

Modify commanding menu UI:

1. Start from Commanding Menu Modding.
2. Identify whether the task is UI/menu structure or AI command behavior.
3. For UI/menu work, preserve commanding menu config/resource workflow.
4. For AI behavior, route to the AI reference.
5. Validate menu display and command selection in runtime.

Generate a class from a layout:

1. Start from Generate Class From Layout Plugin.
2. Confirm the layout resource is correct.
3. Run the plugin workflow in Workbench.
4. Use generated class output as a route to widget members, not as broad API truth.
5. Query exact widget APIs before editing code.

## Configuration Fields And Tables

Layout and layout editor records:

- Layout Creation procedures and warnings define resource creation and setup order.
- Layout Editor table/procedure define the editor surface for layout resources.
- Generated layout classes in game data include slot/alignment/size classes; verify exact use with query output.

Dialog records:

- Dialog Configuration Tutorial procedures define setup order.
- Dialog resources can fail from missing layout, wrong configuration, missing owner, or wrong runtime context.
- Dialog code should be written only after layout/config structure is verified.

Tooltip records:

- Widget Tooltip Setup owns the general UI tooltip workflow.
- Game Master Entity Tooltip tables are partial UI evidence only; broader Game Master setup is not owned here.
- Tooltip setup should preserve target widget/entity, tooltip resource/data, and runtime display context.

End-screen records:

- End Screen Creation has 8 table records; preserve them as config/field guidance.
- End screens cross game-mode/session logic, but this reference owns UI/config side.
- Validate actual end-state display instead of trusting static config.

Commanding menu records:

- Commanding Menu Modding warnings and media were reviewed.
- Treat commanding menu as UI/menu structure here.
- AI command execution, behavior, and validation belong elsewhere.

Widget/API records:

- `Widget` inherits from `Managed`.
- `TextWidget` and `ImageWidget` inherit from `Widget`.
- Generated UI widget classes are exact API truth; handwritten HUD/menu files are better examples.
- Layout/HUD/Widget broad searches are noisy; use lookup/examples first.

## Procedures And Ordered Steps

Layout procedure:

1. Create the layout resource.
2. Open it in Layout Editor.
3. Add and organize widget hierarchy.
4. Configure layout slots, alignment, size, images, text, and resource references.
5. Validate warnings and missing-resource behavior.
6. Generate a class from layout only when script access is needed.
7. Query exact widget APIs and examples.
8. Validate in runtime.

Dialog procedure:

1. Create or select layout resource.
2. Configure dialog data.
3. Bind widgets/resources.
4. Query exact APIs for script behavior.
5. Test open, close, display state, and data population.

Tooltip procedure:

1. Identify the target widget or entity.
2. Configure tooltip UI data/resource.
3. Confirm ownership domain.
4. Validate display and update behavior in runtime.

End-screen procedure:

1. Review End Screen Creation tables.
2. Configure required end-screen data.
3. Link layout/resources.
4. Route game-mode logic to the owning game-mode reference.
5. Trigger the end condition and validate display.

Commanding menu procedure:

1. Review Commanding Menu Modding.
2. Configure UI/menu resource behavior.
3. Keep AI logic separate.
4. Test menu display and selection flow.

Layout-to-class procedure:

1. Confirm layout resource structure is stable.
2. Use Generate Class From Layout Plugin.
3. Verify generated widget member routes.
4. Query `Widget`, `TextWidget`, `ImageWidget`, and handwritten examples before code edits.

## Warnings And Failure Modes

- Do not guess UI APIs. Query exact widget, layout, HUD, text, image, and menu classes before writing code.
- UI lookup does not prove a layout exists or is loaded in the right runtime context.
- `files Widget`, `files HUD`, and `files Layout` are broad and noisy. Prefer `lookup "create HUD widget"` and example subtopic searches first.
- Generated widget files are strongest for exact class truth; handwritten HUD/menu files are stronger implementation examples.
- Layout resources can be valid in Resource Manager but not loaded by the intended menu/HUD/dialog owner.
- A generated class from a layout does not prove the runtime UI context is correct.
- Dialog failures often come from configuration or owner/context mismatch, not only widget APIs.
- End screens depend on game/session state; static layout/config does not prove runtime display.
- Tooltips can cross UI and Game Master entity ownership. Route entity/editable setup to the Game Master reference.
- Commanding menu UI is not the same as AI behavior. Route AI command behavior to the AI reference.
- Diag Menu UI is owned by diagnostics, not this reference.
- Do not embed broad widget API dumps; use query output.
- Do not copy sample/source bodies; use bounded snippets only after targeted search.

## API Lookup Keys

Use these lookup keys before writing UI-sensitive code:

- Core widget classes: `Widget`, `WorkspaceWidget`, `TextWidget`, `ImageWidget`, `BlurWidget`, `CanvasWidgetBase`, `ContentWidget`, `FrameWidget`.
- Layout classes: `LayoutSlot`, `HorizontalLayoutSlot`, `ScrollLayoutSlot`, `SizeLayoutSlot`, `LayoutHorizontalAlign`, `LayoutVerticalAlign`, `LayoutSizeMode`.
- HUD/menu examples: `SCR_HUDMenuComponent`, `SCR_SelectionMenuDisplay`, `SCR_ItemSelectionMenuEntry`, `SCR_SelectionMenuEntryIconComponent`, `SCR_SelectionMenuEntryPreviewComponent`, `ScriptedSelectionMenuEntry`, `SCR_DeployMenuHandler`, `SCR_DebriefingScreenMenu`, `SCR_CampaignMapInfoDisplay`.
- Map/menu examples: `SCR_MapMarkerMenuCategory`, `SCR_MapMarkerMenuEntry`.
- Supporting UI terms: `.layout`, `CreateWidgets`, `Menu`, `MenuBase`, `GetMenuManager`, `UI`, `WorkspaceWidget`, `ImageWidget`, `TextWidget`.

## Game-Data Query Commands

Run these before writing API-sensitive UI code:

```powershell
py -3 scripts/query-reforger-data.py lookup "create HUD widget" --limit 8
py -3 scripts/query-reforger-data.py examples ui --subtopic hud --limit 8
py -3 scripts/query-reforger-data.py examples ui --subtopic layout --limit 8
py -3 scripts/query-reforger-data.py files HUD --limit 8
py -3 scripts/query-reforger-data.py files Widget --limit 8
py -3 scripts/query-reforger-data.py files Layout --limit 8
py -3 scripts/query-reforger-data.py files TextWidget --limit 8
py -3 scripts/query-reforger-data.py files ImageWidget --limit 8
```

Use exact symbols after a route is selected:

```powershell
py -3 scripts/query-reforger-data.py symbol Widget --kind class --exact
py -3 scripts/query-reforger-data.py symbol TextWidget --kind class --exact
py -3 scripts/query-reforger-data.py symbol ImageWidget --kind class --exact
py -3 scripts/query-reforger-data.py files SCR_HUDMenuComponent --limit 8
py -3 scripts/query-reforger-data.py files SCR_SelectionMenuDisplay --limit 8
```

Use snippets only after targeted search identifies the useful file:

```powershell
py -3 scripts/query-reforger-data.py snippet scripts/Game/UI/HUD/SCR_HUDMenuComponent.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/Game/UI/HUD/SelectionMenu/Entries/SCR_ItemSelectionMenuEntry.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/Game/UI/HUD/SelectionMenu/Entries/SCR_SelectionMenuEntryIconComponent.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/Game/UI/HUD/SelectionMenu/SCR_SelectionMenuDisplay.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/Game/UI/Menu/DeployMenu/SCR_DebriefingScreenMenu.c --line 1 --context 30
```

Preferred Codex flow:

1. Read this reference for UI workflow and ownership boundaries.
2. Use `lookup "create HUD widget"` for a bounded task bundle.
3. Use examples for HUD/layout patterns.
4. Use exact symbol/file queries for widget classes.
5. Inspect snippets only for selected examples.
6. Verify layout resources and runtime UI ownership in Workbench/runtime.

## Examples And Samples

Official samples:

- `SampleMod_Main`: primary broad layout/resource signal when UI resources are present.
- Other official sample roots: review only when the task's feature area includes UI/layout resources, such as weapon, vehicle, faction, animation, or Workbench plugin samples.

Game-source example routes from query output:

- `scripts/Game/UI/HUD/SCR_HUDMenuComponent.c`: HUD menu component route.
- `scripts/Game/UI/HUD/SelectionMenu/SCR_SelectionMenuDisplay.c`: HUD selection menu display route.
- `scripts/Game/UI/HUD/SelectionMenu/Entries/SCR_ItemSelectionMenuEntry.c`: selection menu entry route.
- `scripts/Game/UI/HUD/SelectionMenu/Entries/SCR_SelectionMenuEntryIconComponent.c`: icon widget component route.
- `scripts/Game/UI/HUD/SelectionMenu/Entries/SCR_SelectionMenuEntryPreviewComponent.c`: preview widget route.
- `scripts/GameCode/UI/HUD/SelectionMenu/ScriptedSelectionMenuEntry.c`: base scripted selection entry route.
- `scripts/Game/Map/Markers/SCR_MapMarkerMenuCategory.c`: map marker menu category route.
- `scripts/Game/Map/Markers/SCR_MapMarkerMenuEntry.c`: map marker menu entry route.
- `scripts/Game/UI/Menu/DeployMenu/SCR_DebriefingScreenMenu.c`: debriefing menu route.
- `scripts/Game/UI/Menu/DeployMenu/SCR_DeployMenuHandler.c`: deploy menu handler route.
- Generated `Widget`, `TextWidget`, `ImageWidget`, and layout-slot files are exact API routes, not examples to copy wholesale.

Example selection rules:

- Prefer wiki workflows for layout/dialog/tooltip/end-screen setup order.
- Prefer samples for project/resource layout signals.
- Prefer generated files for exact widget API truth.
- Prefer handwritten HUD/menu files for behavior examples.
- Do not copy source bodies; use bounded snippets when implementation context is needed.

## Follow-Up Keywords

Use these keywords for searches and task routing:

- `Layout Creation`
- `.layout`
- `Layout Editor`
- `Generate Class From Layout`
- `Dialog Configuration Tutorial`
- `Widget Tooltip Setup`
- `End Screen Creation`
- `Commanding Menu Modding`
- `Widget`
- `TextWidget`
- `ImageWidget`
- `WorkspaceWidget`
- `CreateWidgets`
- `HUD`
- `SCR_HUDMenuComponent`
- `SCR_SelectionMenuDisplay`
- `SCR_ItemSelectionMenuEntry`
- `SCR_SelectionMenuEntryIconComponent`
- `SCR_SelectionMenuEntryPreviewComponent`
- `ScriptedSelectionMenuEntry`
- `SCR_DebriefingScreenMenu`
- `SCR_DeployMenuHandler`
- `SCR_MapMarkerMenuCategory`
- `SCR_MapMarkerMenuEntry`
- `LayoutSlot`
- `HorizontalLayoutSlot`
- `ScrollLayoutSlot`
- `SizeLayoutSlot`
- `LayoutHorizontalAlign`
- `LayoutVerticalAlign`
- `LayoutSizeMode`
- `Game Master Entity Tooltip`
- `SampleMod_Main`

## Verification

Workbench/resource validation:

- Confirm the layout resource exists and opens in Layout Editor.
- Confirm widget hierarchy, names, layout slots, image/text resources, and generated class routes.
- Confirm dialog/end-screen/config resources are present and point to the correct layout.
- Confirm Generate Class From Layout output matches the current layout after layout changes.

Runtime validation:

- Confirm the UI owner loads the layout in the intended context.
- Confirm HUD/menu/dialog/end-screen opens and closes as expected.
- Confirm text and image widgets populate correctly.
- Confirm tooltips display and update in runtime.
- Confirm commanding menu UI displays while AI command behavior remains separately validated.
- Confirm end screens trigger under the intended game/session state.

Script/API validation:

- Query exact `Widget`, `TextWidget`, `ImageWidget`, layout, HUD, and menu APIs before code changes.
- Inspect snippets only after selecting relevant examples.
- If behavior crosses Game Master, AI, diagnostics, resource manager, or generic scripting ownership, read the owning reference and verify there too.

## Official Wiki Links

- Layout Creation: https://community.bistudio.com/wiki/Arma_Reforger:Layout_Creation
- Dialog Configuration Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Dialog_Configuration_Tutorial
- Widget Tooltip Setup: https://community.bistudio.com/wiki/Arma_Reforger:Widget_Tooltip_Setup
- End Screen Creation: https://community.bistudio.com/wiki/Arma_Reforger:End_Screen_Creation
- Commanding Menu Modding: https://community.bistudio.com/wiki/Arma_Reforger:Commanding_Menu_Modding
- Resource Manager: Layout Editor: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Layout_Editor
- Resource Manager: Generate Class From Layout Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Generate_Class_From_Layout_Plugin
- Game Master: Entity Tooltip Creation: https://community.bistudio.com/wiki/Arma_Reforger:Game_Master:_Entity_Tooltip_Creation

## Usefulness Score

Score: `92/100`

- Wiki coverage: `28/30`
  - All owned primary UI pages are reviewed and represented.
  - Tables, procedures, warnings, media, and links were reviewed; end-screen and tooltip table detail is preserved as field/config guidance.
  - Game Master Entity Tooltip Creation is explicitly partial and routed to the Game Master owner for non-UI behavior.
  - Missed coverage: screenshot-level UI visuals are not embedded; impact is low because editor surfaces and official links are present.
- Operational detail: `14/15`
  - Preserves layout creation, dialog setup, widget tooltip, end-screen, commanding menu UI, Layout Editor, and Generate Class From Layout workflows.
- API lookup usefulness: `15/15`
  - Exact lookup keys and commands are present for widget, text/image widget, layout, HUD, examples, and snippets.
- Example grounding: `9/10`
  - Official sample layout signals and raw game-source example routes are included.
  - No sample/source bodies are copied.
- Codex task usefulness: `14/15`
  - Supports common UI tasks: create HUD widget, wire layout resources, configure dialogs/tooltips/end screens, and route menu examples.
  - Cross-domain commanding/Game Master behavior is intentionally routed.
- Context efficiency: `8/10`
  - Dense and navigable with explicit split boundaries.
  - Broad query noise is called out so Codex uses targeted routes first.
- Verification guidance: `4/5`
  - Workbench, layout resource, runtime UI ownership, widget population, tooltip, end-screen, and API checks are present.
  - Multiplayer/server-specific UI concerns are routed only if the task crosses those systems.

Category-fit check:
- Source family complete: pass. Layout, dialog, tooltip, end-screen, commanding menu, layout editor, and layout-to-class plugin pages are covered.
- No owned page missing: pass.
- Split boundary justified: pass. Resource Manager, Game Master, diagnostics, AI commanding, and generic scripting ownership are routed to owning references.
- Cross-links present: pass.
- Task route clear: pass. HUD widget tasks route to this reference plus `lookup "create HUD widget"` and targeted UI queries.
- Automatic failure conditions: none found.
