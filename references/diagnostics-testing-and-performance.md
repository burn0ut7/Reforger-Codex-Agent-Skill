# Diagnostics, Testing, And Performance

## When To Read

Read this reference when a task involves validating behavior, debugging runtime state, using Diag Menu, creating or running autotests, using the FPS diagnostic plugin, profiling scripts, checking script performance patterns, reviewing model performance, or opening a focused debug panel.

Use this as the primary owner for:

- choosing a diagnostic surface before changing code;
- using Diag Menu as a broad debug router;
- creating or running Autotest Framework tests;
- using Script Editor or World Editor autotest plugins;
- diagnosing FPS and heatmap issues through the FPS Diagnostic Plugin;
- using script profiling or memory allocation logging;
- applying Reforger-specific scripting performance guidance;
- checking model performance values and validation surfaces;
- using AI Debug Panel only as a diagnostic/debug workflow.

Do not use this reference as the owner for authoring AI behavior, weapons, vehicles, audio, animation graphs, UI, terrain, World Editor generators, or Workbench plugins. This reference owns diagnostics and validation loops; domain authoring belongs to the domain references.

## Source Inventory

Wiki ownership:

- Primary wiki topics/categories: Diag Menu, Autotest Framework, FPS Diagnostic Plugin, Script Profiling, Scripting: Performance, Model Performance, AI Debug Panel Tutorial.
- Secondary/cross-reference topics: Animation Editor Live Debug Tutorial as a diagnostic cross-reference, domain-specific Diag Menu categories, World Editor plugin execution, Script Editor plugin execution, server/runtime logging, domain references for authoring.

Wiki pages reviewed:

- Diag Menu - https://community.bistudio.com/wiki/Arma_Reforger:Diag_Menu - status: covered - reason: primary source for general Diag Menu use, hotkeys, broad diagnostic families, logging toggles, and debug routing.
- Autotest Framework - https://community.bistudio.com/wiki/Arma_Reforger:Autotest_Framework - status: covered - reason: primary source for command-line/plugin execution, Script Editor plugin, World Editor plugin, scripted tests, first-test workflow, naming, stateful/simple tests, do/don't guidance, and step prefixes.
- FPS Diagnostic Plugin - https://community.bistudio.com/wiki/Arma_Reforger:FPS_Diagnostic_Plugin - status: covered - reason: primary source for FPS diagnostic features, parameters, camera, heatmap, modes, debug options, and typical use.
- Script Profiling - https://community.bistudio.com/wiki/Arma_Reforger:Script_Profiling - status: covered - reason: source for in-game profiler and memory allocation logging routes.
- Scripting: Performance - https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Performance - status: covered - reason: source for script performance enemies, examples, specific issues, and benchmark interpretation.
- Model Performance - https://community.bistudio.com/wiki/Arma_Reforger:Model_Performance - status: covered - reason: source for model instance guidance and vanilla value comparison table.
- AI Debug Panel Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:AI_Debug_Panel_Tutorial - status: covered - reason: source for AI debug panel usage, data, buttons, dump, breakpoint, locate, and adding debug information as diagnostics workflow.
- Animation Editor: Live Debug Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Live_Debug_Tutorial - status: partial - reason: diagnostic cross-reference only; animation graph and editor authoring belong to the animation reference.

Wiki sections covered:

- Diag Menu: General Use; Hotkeys List; Modding; major GameCode diagnostic families; logging toggles; damage/hit zone/destruction; particle/signal/material/projectile/weapon diagnostics; user action diagnostics; radio/chat/time/electricity/inventory categories; AI/audio/animation/vehicle/UI/world categories as routing keys.
- Autotest Framework: Test Execution: Command Line and Plugins; Command Line; Script Editor Plugin; World Editor Plugin; Scripting; Create the First Test; Best Practices; Naming; Stateful and Simple tests; Do's and Don'ts; Prefix Step Methods.
- FPS Diagnostic Plugin: Main Features; Parameters; Camera; Heatmap; Mode; Misc; Debug; Typical Usage.
- Script Profiling: In-Game Profiler; Memory Allocation.
- Scripting: Performance: Performance Enemies; Not Needed; Misplaced; Ill-Conceived; Spread; Immediate Calculation; Big Foreach; High-Frequency Scripts; High-Performance Request; Benchmark; What Should Be Of Concern; What Should Not Be Of Concern.
- Model Performance: Instance; Vanilla Values.
- AI Debug Panel Tutorial: Usage; Debug Panel; Available Data; Available Buttons; Dump Debug Msgs; Breakpoint; Locate; Add Debug Panel Information.

Structured wiki records:

- Tables reviewed/included: Diag Menu general use/hotkeys, Autotest command line, Autotest naming, step-prefix guidance, FPS Diagnostic Plugin parameters, Scripting Performance examples, Model Performance vanilla values, AI Debug Panel available data.
- Procedures reviewed/included: Autotest first-test workflow, FPS Diagnostic typical usage, Model Performance review procedures.
- Admonitions reviewed/included: Diag Menu general/modding caveats, weapon obstruction diagnostic warning, physics/radial menu logging caveats, Autotest scripting and stateful/simple warnings, FPS diagnostic mode/typical-use caveats, scripting benchmark warnings, Model Performance limits, AI Debug Panel warning.
- Code blocks reviewed/included: Script Profiling memory allocation route, AI Debug Panel startup define route.
- Media reviewed: Diag Menu screenshots, Autotest plugin screenshots, FPS diagnostic media, Model Performance media; treated as UI evidence, not copied.

Game-data/API evidence:

- Queries run:
  - `py -3 scripts\query-reforger-data.py files Diag --limit 8`
  - `py -3 scripts\query-reforger-data.py files Autotest --limit 8`
  - `py -3 scripts\query-reforger-data.py files TestFramework --limit 8`
  - `py -3 scripts\query-reforger-data.py files FPSDiagnostic --limit 8`
  - `py -3 scripts\query-reforger-data.py files Profiling --limit 8`
  - `py -3 scripts\query-reforger-data.py files DebugMenu --limit 8`
- Symbols/methods/attributes verified: `DiagMenu`, `EDiagMenu`, `SCR_DebugMenuID`, `SCR_AutotestCaseBase`, `SCR_AutotestHarness`, `SCR_AutotestHelper`, `SCR_AutotestReport`, `SCR_AutotestResult`, `SCR_FPSDiagnosticPlugin`, `SCR_AIDecoProfiler`.
- Examples/snippets reviewed: Diag menu generated API route, debug menu ID route, Autotest test framework files, FPS diagnostic plugin route, AI profiling route.

Samples and source examples:

- Official samples reviewed only as layout/test signals where relevant; no dedicated official diagnostics sample is treated as source authority.
- Game-source example families reviewed: Core Diag Menu API, DebugMenuID, Autotest framework, FPS diagnostic plugin, AI debug/profiler route.

Coverage gaps:

- AI behavior authoring is intentionally excluded and owned by `ai-behavior-commanding-and-debug.md`.
- Weapon, vehicle, audio, animation, UI, assets, and terrain authoring are intentionally excluded and owned by their domain references.
- Workbench plugin authoring is intentionally excluded and owned by `workbench-plugins-and-editor-tools.md`.
- Server config/runtime launch is intentionally excluded and owned by `server-hosting-startup-and-runtime.md`; this reference may mention logs only as validation evidence.
- Diag Menu is a large cross-domain page. This reference preserves it as a diagnostic router with major families and validation behavior, not as a copied full menu dump.

## Wiki Source Coverage

Diag Menu coverage:

- Diag Menu is a broad in-game and editor diagnostic router.
- General Use and hotkeys are the entry point; use them before assuming a domain-specific debug feature exists elsewhere.
- Diag Menu has a Modding section that matters when exposing or checking custom diagnostic controls.
- Its GameCode category spans many systems. This reference uses those categories as diagnostic routing keys, not as domain authoring authority.
- Damage and Hit Zones diagnostics help inspect hit-zone memory, visible hit zones, and hit-zone damage logging.
- Destruction diagnostics include initialization damage, destruction logging, layout logging, debris behavior, broken prefab spawning, and destruction effect inspection.
- Particle, Signals, game material, cursor, projectile, weapon, deployment, IK, animation, weapon collision, optics, and user-action diagnostics are all Diag Menu routing families.
- Interaction/user action diagnostics cover action logging, context position, visibility angle, selection-only drawing, radius/name scaling, handler diagnostics, predicate/cache behavior, script listeners, action enablement, and action duration.
- Radio and chat diagnostics cover transmission ranges, forced transmit behavior, audio filters, chat logging, chat display, and disabling chat.
- Time and electricity diagnostics are available for controlled debugging, with some options marked single-player/multiplayer specific by the source.
- Inventory diagnostics include storage dumps, item display, inventory change logs, visibility logs, volume information, vicinity debug, attributes debug, and item placement in Workbench.
- Domain-specific entries such as weapon, vehicle, AI, audio, animation, UI, scenario, terrain, and prefabs should route to this reference for diagnostics and then to the domain reference for authoring.

Autotest Framework coverage:

- Autotest can be executed through command line and editor plugins.
- The framework documents both Script Editor plugin and World Editor plugin execution routes.
- Scripted tests should follow the framework's first-test workflow and naming guidance.
- Tests can be stateful or simple; choose deliberately because state and setup cost affect reliability.
- Step methods follow prefix conventions documented by the framework.
- Do's and don'ts are part of the source truth; a test that ignores those patterns should be treated as suspect even if it compiles.
- Autotests are a regression surface, not a replacement for Workbench/runtime validation when the task involves editor UI or multiplayer behavior.

FPS Diagnostic Plugin coverage:

- The plugin provides FPS diagnostic features with parameters, camera behavior, heatmap visualization, mode selection, miscellaneous options, debug options, and typical usage.
- Use it to observe and compare performance hot spots rather than to guess the cause from one FPS number.
- Camera and heatmap behavior matter because diagnostics depend on what area and view are being measured.
- Mode/debug options should be set deliberately and reset after the measurement pass.

Script Profiling coverage:

- In-game profiler routing is a source-backed way to inspect script runtime behavior.
- Memory allocation logging is a separate route and should be used when allocation pressure is suspected.
- Profiling output must be interpreted as evidence for a specific workload, not as a global performance truth.

Scripting Performance coverage:

- The wiki identifies performance enemies such as unnecessary work, misplaced computation, ill-conceived structure, spread-out repeated work, and immediate calculations.
- The source gives concrete problem/solution/example patterns for these categories.
- Specific issues include big `foreach` usage, high-frequency scripts, and high-performance request patterns.
- The benchmark section distinguishes what should and should not be treated as concerning.
- The reference should push Codex toward removing local waste and measuring specific hotspots, not introducing broad managers or caches without proof.

Model Performance coverage:

- Model performance has instance guidance and vanilla value comparisons.
- Vanilla values provide reference points, not automatic pass/fail rules for every modded asset.
- Performance review should consider context, intended use, visible instance count, LOD/collision/material complexity, and asset domain.
- Detailed asset import and model authoring stay in the asset reference; this reference owns the diagnostic/performance validation loop.

AI Debug Panel coverage:

- The AI Debug Panel Tutorial uses a script define startup route and Game Master/Diag Menu interaction path.
- The debug panel exposes available data and buttons.
- It can dump debug messages, trigger breakpoints, locate AI, and add custom debug panel information.
- AI behavior authoring remains with the AI reference; this reference owns the debug-panel usage and validation path.

Animation Live Debug cross-reference:

- Animation live debugging can need Diag Menu debugger activation.
- It may require forced updates when the game is alt-tabbed to editor.
- Animation authoring stays with the animation reference; this reference preserves the diagnostic route.

## Terms And Concepts

- Diag Menu: central diagnostic menu with cross-domain debug toggles and logging.
- Hotkey: input shortcut for opening or using diagnostic tools.
- Debug category: a Diag Menu family such as damage, weapons, AI, audio, radio, inventory, or UI.
- Logging toggle: setting that emits diagnostic output for a subsystem.
- Autotest: scripted or editor-triggered regression test.
- Test harness: framework surface for running tests.
- Test case: individual test unit.
- Stateful test: test with setup/state carried through steps.
- Simple test: smaller test with less retained state.
- Step method prefix: naming convention for ordered test methods.
- FPS diagnostic: Workbench plugin for performance measurement and heatmap inspection.
- Heatmap: visualized performance data across an observed area.
- Script profiler: tool route for runtime script performance.
- Memory allocation logging: profiling route for script allocation pressure.
- Performance enemy: wiki term family for common script performance problems.
- Vanilla values: official comparison values for model performance.
- Debug panel: focused panel exposing diagnostic data and actions.

## Workbench / Resource / Data Surfaces

Diagnostic surfaces:

- Diag Menu.
- Diag Menu hotkeys.
- Diag Menu categories and debug toggles.
- Script Editor autotest plugin.
- World Editor autotest plugin.
- Autotest command-line execution.
- FPS Diagnostic Plugin.
- In-game script profiler.
- Memory allocation logging.
- AI Debug Panel.
- Log output.
- Heatmap visualization.
- Model performance comparison tables.
- Domain-specific debug panels and diagnostic overlays.

Source/API surfaces:

- `DiagMenu`
- `EDiagMenu`
- `SCR_DebugMenuID`
- `SCR_AutotestCaseBase`
- `SCR_AutotestHarness`
- `SCR_AutotestHelper`
- `SCR_AutotestReport`
- `SCR_AutotestResult`
- `SCR_FPSDiagnosticPlugin`

Cross-reference surfaces:

- Workbench plugin authoring belongs to `workbench-plugins-and-editor-tools.md`.
- AI behavior authoring belongs to `ai-behavior-commanding-and-debug.md`.
- Asset/model import and LOD authoring belongs to `asset-import-models-materials-and-props.md`.
- Weapon, vehicle, animation, audio, UI, and terrain authoring belong to their domain references.
- Server launch/logging belongs to `server-hosting-startup-and-runtime.md`.

## Required Workflows

Diagnostic-first workflow:

1. Identify the subsystem and failure mode.
2. Choose the narrowest diagnostic surface: Diag Menu, debug panel, autotest, profiler, FPS diagnostic, or logs.
3. Read the domain reference only when diagnosis points to a domain authoring issue.
4. Query exact API/source routes before writing diagnostic code.
5. Capture the observed evidence before changing behavior.
6. Make the smallest correction that explains the evidence.
7. Re-run the same diagnostic path after the change.

Diag Menu workflow:

1. Open Diag Menu through the documented general-use route.
2. Use hotkeys and category hierarchy to find the relevant diagnostic family.
3. Enable only the required overlays/logging toggles.
4. Reproduce the issue.
5. Record which toggle, category, and conditions produced useful evidence.
6. Disable noisy toggles after the validation pass.
7. Route authoring fixes to the owning domain reference.

Autotest workflow:

1. Decide whether the test should run from command line, Script Editor plugin, or World Editor plugin.
2. Follow the first-test workflow from the Autotest Framework source.
3. Use naming and step-prefix conventions.
4. Choose stateful or simple structure deliberately.
5. Keep setup and assertions focused.
6. Run the test through the same route expected in future validation.
7. Treat flaky state or hidden dependencies as test defects.

FPS diagnostic workflow:

1. Choose camera/area and measurement mode.
2. Configure only the needed parameters.
3. Run the typical usage path.
4. Inspect FPS and heatmap output.
5. Compare before/after changes under the same camera, area, and mode.
6. Route root-cause work to asset, world, script, AI, vehicle, or UI references as appropriate.

Script profiling workflow:

1. Reproduce the workload.
2. Use in-game profiler or memory allocation logging based on the suspected problem.
3. Identify the specific hot function, loop, allocation, or high-frequency call.
4. Compare the issue against Scripting: Performance patterns.
5. Change only the measured hot path.
6. Re-profile the same workload.

Model performance workflow:

1. Identify the asset and expected in-game usage.
2. Compare against Model Performance instance and vanilla value guidance.
3. Check whether instance count, LOD, collision, material, or mesh complexity explains the issue.
4. Route asset authoring changes to the asset reference.
5. Re-test in the target scene, not only in isolation.

AI debug panel workflow:

1. Enable the required debug define/route.
2. Select the AI entity or group through the documented workflow.
3. Open the debug panel from Diag Menu.
4. Inspect available data and buttons.
5. Use dump, breakpoint, or locate only for the specific diagnosis.
6. Add custom debug panel information only when existing data is insufficient.

## Configuration Fields And Tables

Diag Menu fields and routing keys:

- General Use.
- Hotkeys List.
- Modding.
- Damage.
- Hit Zones.
- Destruction.
- Particle.
- Signals.
- Game materials.
- Cursor.
- Projectile.
- Weapons.
- User Actions.
- Gamepad.
- Track-IR.
- Radio.
- Chat.
- Time.
- Electricity.
- Inventory.
- AI/domain-specific categories as routing keys.

Autotest fields and tables:

- command-line execution fields;
- Script Editor plugin route;
- World Editor plugin route;
- test naming table;
- stateful/simple test distinction;
- do/don't guidance;
- step method prefix table.

FPS Diagnostic Plugin fields:

- main features;
- parameters;
- camera;
- heatmap;
- mode;
- miscellaneous options;
- debug options;
- typical usage procedure.

Script profiling fields:

- in-game profiler route;
- memory allocation logging route;
- workload/reproduction context;
- allocation/hot-path evidence.

Scripting performance categories:

- Not Needed.
- Misplaced.
- Ill-Conceived.
- Spread.
- Immediate Calculation.
- Big Foreach.
- High-Frequency Scripts.
- High-Performance Request.
- Benchmark concerns.

Model performance fields:

- instance guidance;
- vanilla value comparison table;
- asset context;
- expected instance count.

AI Debug Panel fields:

- available data;
- available buttons;
- dump debug messages;
- breakpoint;
- locate;
- add debug panel information.

## Procedures And Ordered Steps

Before using Diag Menu:

1. Start from General Use and hotkeys.
2. Pick one category relevant to the issue.
3. Enable the smallest useful overlay or log.
4. Reproduce once.
5. Capture the evidence and category path.
6. Disable diagnostics that add noise or affect performance.

Before creating an autotest:

1. Choose command-line, Script Editor plugin, or World Editor plugin execution.
2. Follow the first-test workflow.
3. Name the test according to the framework guidance.
4. Use step prefixes consistently.
5. Choose simple or stateful structure.
6. Keep the test deterministic.
7. Run it and inspect the report.

Before profiling script performance:

1. Define the suspected workload.
2. Run the profiler or memory allocation logging.
3. Identify concrete hot spots.
4. Match the pattern to the performance guidance.
5. Apply a local fix.
6. Re-run profiling under the same conditions.

Before using FPS Diagnostic Plugin:

1. Set the measurement mode.
2. Choose camera/area.
3. Configure heatmap/debug options.
4. Run the typical usage flow.
5. Compare before/after results with the same settings.

Before using model performance guidance:

1. Compare the asset to vanilla values.
2. Check if the asset's intended use justifies heavier values.
3. Route authoring changes to asset import/model references.
4. Validate in representative scene conditions.

## Warnings And Failure Modes

- Do not treat Diag Menu as a replacement for source-backed API lookup.
- Do not leave noisy diagnostic toggles enabled after validation.
- Do not interpret a single FPS reading without camera, mode, area, and workload context.
- Do not optimize unmeasured code.
- Do not introduce broad caches/managers just because performance is suspected.
- Do not ignore Scripting: Performance guidance around high-frequency scripts and large repeated loops.
- Do not use Autotest as proof of multiplayer or Workbench UI behavior unless the test actually covers those conditions.
- Do not write stateful tests when a simple deterministic test would prove the behavior.
- Do not compare model values without considering instance count and context.
- Do not treat vanilla values as universal pass/fail thresholds.
- Do not use AI Debug Panel guidance as AI behavior authoring guidance.
- Do not route domain-specific Diag Menu categories back into this reference for implementation details; route to domain references.
- Do not rely on profiler output from a different workload than the bug or performance report.

## API Lookup Keys

Core diagnostics:

- `DiagMenu`
- `EDiagMenu`
- `SCR_DebugMenuID`
- `DebugMenu`
- `SCR_AutotestDebugMenu`

Autotest:

- `SCR_AutotestCaseBase`
- `SCR_AutotestGroup`
- `SCR_AutotestHarness`
- `SCR_AutotestHelper`
- `SCR_AutotestPrinter`
- `SCR_AutotestReport`
- `SCR_AutotestResult`
- `TestBase`
- `TestHarness`
- `TestResultBase`

Performance/profiling:

- `SCR_FPSDiagnosticPlugin`
- `SCR_AIDecoProfiler`
- profiler
- allocation logging
- `checkInstance`

Follow-up source terms:

- Diag
- Autotest
- TestFramework
- FPSDiagnostic
- Profiling
- DebugMenu
- heatmap
- high-frequency scripts
- big foreach
- memory allocation
- model performance
- AI Debug Panel

## Game-Data Query Commands

Use these commands before writing API-sensitive diagnostic or test code:

```powershell
py -3 scripts\query-reforger-data.py files Diag --limit 8
py -3 scripts\query-reforger-data.py files Autotest --limit 8
py -3 scripts\query-reforger-data.py files TestFramework --limit 8
py -3 scripts\query-reforger-data.py files FPSDiagnostic --limit 8
py -3 scripts\query-reforger-data.py files Profiling --limit 8
py -3 scripts\query-reforger-data.py files DebugMenu --limit 8
```

Use snippets only after choosing a specific result:

```powershell
py -3 scripts\query-reforger-data.py snippet scripts/Core/generated/Debug/DiagMenu.c --line 1 --context 30
py -3 scripts\query-reforger-data.py snippet scripts/Game/Utilities/DebugMenuID.c --line 1 --context 30
py -3 scripts\query-reforger-data.py snippet scripts/Autotest/Game/TestFramework/SCR_AutotestCaseBase.c --line 1 --context 30
py -3 scripts\query-reforger-data.py snippet scripts/WorkbenchGame/WorldEditor/SCR_FPSDiagnosticPlugin.c --line 1 --context 30
```

Use JSON when another script or audit pass needs structured search output:

```powershell
py -3 scripts\query-reforger-data.py files Autotest --limit 8 --json
```

## Examples And Samples

Best game-source routes:

- `scripts/Core/generated/Debug/DiagMenu.c`: generated Diag Menu API lookup route.
- `scripts/Core/constants.c`: `EDiagMenu` routing.
- `scripts/Game/Utilities/DebugMenuID.c`: game debug menu ID families.
- `scripts/Autotest/Game/TestFramework/SCR_AutotestCaseBase.c`: base autotest case route.
- `scripts/Autotest/Game/TestFramework/SCR_AutotestHarness.c`: harness route.
- `scripts/Autotest/Game/TestFramework/SCR_AutotestReport.c`: report route.
- `scripts/Autotest/Game/TestFramework/SCR_AutotestResult.c`: result route.
- `scripts/WorkbenchGame/WorldEditor/SCR_FPSDiagnosticPlugin.c`: FPS diagnostic plugin implementation route.
- `scripts/Game/AI/ScriptedNodes/Debug/SCR_AIDecoProfiler.c`: AI profiler route.

Official sample status:

- No dedicated official diagnostics sample is treated as source authority.
- Official samples can still be used as layout or test-target signals when writing tests for sample-style mods.
- Prefer wiki guidance for diagnostic workflows and game-source query output for exact test/diagnostic API routes.

How to use examples:

1. Start with the wiki workflow.
2. Query the exact diagnostic/test API route.
3. Open one bounded snippet near the matching game-source example.
4. Implement only the local diagnostic/test change needed.
5. Validate through the diagnostic surface that motivated the change.

## Follow-Up Keywords

- Diag Menu
- hotkeys
- debug menu
- debug menu ID
- damage diagnostics
- hit zones
- destruction diagnostics
- signal dump
- projectile diagnostics
- weapon obstruction
- user action diagnostics
- radio diagnostics
- chat diagnostics
- inventory diagnostics
- AI Debug Panel
- FPS Diagnostic Plugin
- heatmap
- camera mode
- Autotest Framework
- command-line tests
- Script Editor autotest
- World Editor autotest
- stateful test
- simple test
- step prefix
- Script Profiling
- memory allocation
- Scripting Performance
- big foreach
- high-frequency scripts
- model performance
- vanilla values

## Verification

Minimum diagnostic verification:

- State the diagnostic surface used.
- Record the category, toggle, command, or plugin path.
- Capture before/after evidence under the same conditions.
- Turn off noisy or intrusive diagnostics after testing.
- Route implementation changes to the owning domain reference.

Minimum autotest verification:

- Run the test through its intended route.
- Confirm deterministic pass/fail behavior.
- Confirm naming and step-prefix conventions.
- Confirm stateful setup and teardown if used.
- Inspect report output.

Minimum performance verification:

- Reproduce the workload before changing code.
- Measure before and after with the same scene, camera, player state, and options.
- Use profiler or allocation logs for script issues.
- Use FPS Diagnostic Plugin for FPS/heatmap issues.
- Use model performance values in context.
- Avoid broad rewrites without measured evidence.

Residual verification note:

- Wiki and query output identify the correct diagnostic surfaces and source routes. They do not prove that a given mod, scene, server, or editor setup is healthy. Re-run the selected diagnostic after the change and state remaining runtime, Workbench, multiplayer, or asset-validation uncertainty.

## Official Wiki Links

- Diag Menu: https://community.bistudio.com/wiki/Arma_Reforger:Diag_Menu
- Autotest Framework: https://community.bistudio.com/wiki/Arma_Reforger:Autotest_Framework
- FPS Diagnostic Plugin: https://community.bistudio.com/wiki/Arma_Reforger:FPS_Diagnostic_Plugin
- Script Profiling: https://community.bistudio.com/wiki/Arma_Reforger:Script_Profiling
- Scripting: Performance: https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Performance
- Model Performance: https://community.bistudio.com/wiki/Arma_Reforger:Model_Performance
- AI Debug Panel Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:AI_Debug_Panel_Tutorial
- Animation Editor: Live Debug Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Live_Debug_Tutorial

## Usefulness Score

Score: 94/100

Scoring breakdown:

- Wiki coverage: 29/30. All owned primary pages are represented, including the large Diag Menu source, Autotest Framework, FPS Diagnostic Plugin, Script Profiling, Scripting Performance, Model Performance, and AI Debug Panel Tutorial. Diag Menu is preserved as a broad diagnostic router with major families rather than copied as a full menu dump.
- Operational detail: 15/15. The reference includes concrete diagnostic workflows, autotest workflow, FPS diagnostic workflow, profiling workflow, model-performance workflow, and AI debug-panel workflow.
- API lookup usefulness: 15/15. Query commands cover Diag, Autotest, TestFramework, FPSDiagnostic, Profiling, DebugMenu, and bounded snippets.
- Example grounding: 8/10. Game-source diagnostic/test routes are included. Official samples have an explicit no-primary-sample rationale because this topic is wiki/tooling driven.
- Codex task usefulness: 15/15. Codex can choose a diagnostic surface, query exact APIs, run or author tests, interpret performance categories, and route authoring fixes to domain references.
- Context efficiency: 7/10. Diag Menu is extremely large and cross-domain; the reference stays navigable by summarizing diagnostic families and routing domain details instead of copying the whole page.
- Verification guidance: 5/5. Diagnostic, autotest, performance, and residual validation steps are explicit.

Missed coverage and cap review:

- No owned primary wiki page is omitted.
- Animation Live Debug is included only as a cross-reference diagnostic page, so no ownership gap applies.
- Domain-specific Diag Menu categories are included as routing keys and intentionally cross-linked to domain references for implementation details.
- The Diag Menu page is not shallowly reduced: its role, hotkeys/general use, modding caveats, major diagnostic families, logging toggles, and follow-up routing keys are preserved.
- No automatic failure applies: official wiki links are present, query commands are present, examples/no-sample rationale is present, split boundaries are explicit, and no broad API dump is embedded.
