# Script Events, Actions, And Patterns

## When To Read

Read this before writing or reviewing practical gameplay script behavior in Arma Reforger.

Use this reference for:

- creating a gameplay script file after the project and language rules are understood;
- deciding how to structure a small gameplay class or helper method;
- modifying an existing script class with `modded`, `override`, and `super`;
- implementing a user action by routing through `ScriptedUserAction`;
- using events, invokers, callbacks, and debug output as script patterns;
- applying script-performance rules to loops, frame work, expensive requests, and cached calculations;
- finding real game-source examples for script components and user actions.

Do not use this as the primary source for:

- Enfusion syntax, keyword semantics, ARC, JSON, or Script Editor general usage: read `enfusion-language-and-script-editor.md`;
- component creation, lifecycle order, event masks, activeness, and prefab/component wiring: read `entities-components-and-lifecycle.md`;
- replication, authority, proxies, RPC, or dedicated-server network behavior: read `multiplayer-replication-and-authority.md`;
- Resource Manager, prefab, config, or attribute widget workflows: read `resource-manager-file-types-and-editors.md` and `prefabs-configs-containers-and-catalogs.md`;
- exact API signatures: query game data with `scripts/query-reforger-data.py`.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: scripting modding, script file creation, practical scripting example workflow, class template example, modded script example, event handler routing, user-action script pattern routing, and script-performance guidance where it affects implementation.
- Secondary/cross-reference topics: Script Editor usage, language syntax, component lifecycle, event masks, Resource Manager, terrain test setup, and diagnostics are mentioned only where needed to complete script-pattern workflows; their full ownership belongs to other references.

Wiki pages reviewed:
- Scripting Modding - https://community.bistudio.com/wiki/Arma_Reforger:Scripting_Modding - status: covered - reason: primary owner for modified script folder structure, `modded`/`override`/`super` pattern, sample modded scoring example, and script test/debug flow.
- Scripting Example - https://community.bistudio.com/wiki/Arma_Reforger:Scripting_Example - status: covered - reason: primary owner for script creation, method design, parameters, return values, pseudocode-to-code workflow, commenting, optimization, testing, and Debug Console use.
- Class Template Example - https://community.bistudio.com/wiki/Arma_Reforger:Class_Template_Example - status: covered - reason: primary owner for reusable generic/class-template pattern guidance and its limitations.
- Scripting: Performance - https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Performance - status: covered - reason: primary owner for implementation-level performance anti-patterns and code-shaping rules.
- Script Editor - https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor - status: partial - reason: only validation, breakpoints, console, and symbol navigation needed by script-pattern workflows are routed here; full editor behavior belongs to `enfusion-language-and-script-editor.md`.
- Resource Manager - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager - status: partial - reason: only the create-script entry point is relevant here; full resource browsing/editing belongs to `resource-manager-file-types-and-editors.md`.

Wiki sections covered:
- Scripting Modding > Page - coverage: full for preparing script folder/class changes and testing modified script behavior.
- Scripting Modding > File structure - coverage: full for locating original script classes, creating the matching addon script tree, and avoiding `SCR_` naming conflicts in mod-owned files.
- Scripting Modding > Create a Modified Script > Syntax - coverage: full for `modded` and `override` behavior.
- Scripting Modding > Create a Modified Script > Writing - coverage: full for modifying an existing scoring class as a proof-of-concept and understanding mission-presence limitations.
- Scripting Modding > Create a Modified Script > Super - coverage: full for extending original behavior instead of replacing it blindly.
- Scripting Modding > Mod Test > Terrain Preparation - coverage: partial for script test scenario prerequisites only; terrain/world setup belongs elsewhere.
- Scripting Modding > Mod Test > Debug Process - coverage: full for breakpoint, console, and watch routing.
- Scripting Example > Create the Script > New File - coverage: full for Resource Manager and Script Editor script-file creation routes, module directory mapping, and creator-tag warning.
- Scripting Example > Get the Smallest Value > Method Setup - coverage: full for creating a class/method, naming precisely, adding parameters, using `notnull`, and returning the correct type.
- Scripting Example > Get the Smallest Value > Code Setup - coverage: full for planning human-readable logic before code, selecting error/default return values, and null/empty handling.
- Scripting Example > Get the Smallest Value > Writing, Commenting, Optimisation - coverage: full for translating logic to code, avoiding useless comments, and optimizing only after correctness.
- Scripting Example > Get the Average Value > Method Setup, Code Setup, Writing, Testing - coverage: full for extending an existing class with a second method, checking division-by-zero, and testing outputs.
- Scripting Example > Debug(Remote) Console - coverage: full for running script test code in the Game environment.
- Class Template Example > Page and Examples - coverage: full for generic reusable helper tradeoffs and restrictions.
- Scripting: Performance > Performance Enemies and Specific Issues - coverage: full for unneeded, misplaced, ill-conceived, spread, immediate, big-foreach, high-frequency, and high-performance-request rules.
- Scripting: Performance > Benchmark - coverage: full for what should and should not be performance concerns.

Structured wiki records:
- Tables reviewed/included: script module directory table; commenting bad/good example table; class-template pros/cons table; performance original-vs-optimized tables for misplaced work, early exit, spreading work, caching, and heavy calculations.
- Procedures reviewed/included: script file creation routes; locate original script and mirror folder structure; modified script writing; `super` extension flow; test scenario/debug process; method design and test flow.
- Admonitions reviewed/included: creator tag required to avoid class conflicts; do not use BI `SCR_` for mod-owned classes; use precise names; `notnull` parameter intent; pick safe default/error returns; division-by-zero can crash; Debug Console must run in Game environment; class templates have Script Editor detection limitations; template methods must be valid for every candidate type; performance can harm the whole game.
- Code blocks reviewed/included: sample method/class flow, modded scoring sample, class-template helper sample, performance examples. Runtime reference paraphrases patterns and does not copy source bodies.
- Media reviewed: Script Editor symbol search and folder-structure screenshots, modified script `super` workflow images, prefab test GIF, breakpoint/debug images. Media is not copied; the workflow behavior is represented.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts\query-reforger-data.py symbol ScriptComponent --kind class --exact`
  - `py -3 scripts\query-reforger-data.py symbol ScriptComponentClass --kind class --exact`
  - `py -3 scripts\query-reforger-data.py inherits ScriptComponent`
  - `py -3 scripts\query-reforger-data.py lookup "make a user action"`
  - `py -3 scripts\query-reforger-data.py examples component --subtopic script-component`
  - `py -3 scripts\query-reforger-data.py inherits ScriptedUserAction`
  - `py -3 scripts\query-reforger-data.py examples user-action`
  - `py -3 scripts\query-reforger-data.py method ScriptedUserAction PerformAction --exact`
  - `py -3 scripts\query-reforger-data.py method ScriptedUserAction CanBeShownScript --exact`
  - `py -3 scripts\query-reforger-data.py method ScriptedUserAction CanBePerformedScript --exact`
- Symbols/methods/attributes verified: `ScriptComponent`, `ScriptComponentClass`, `ScriptedUserAction`, `BaseUserAction`, `PerformAction`, `CanBeShownScript`, `CanBePerformedScript`, and representative derived script-component/user-action classes.
- Examples/snippets reviewed: script component examples, `ScriptedUserAction` derived examples, a faction-commander user action snippet, and a hybrid physics script component snippet.

Samples and source examples:
- Official sample folders reviewed: `SampleMod_ModdedScript`.
- Game-source example families reviewed through query output: script component examples, user-action examples, and `ScriptedUserAction` inheritance/examples.

Coverage gaps:
- Missing, excluded, or intentionally deferred source: full Script Editor reference, full Resource Manager workflow, full component lifecycle/event-mask behavior, test terrain/world construction, network authority, and domain-specific action details for weapons/vehicles/inventory.
- Reason and impact: those are owned by narrower references. This reference keeps enough routing to write gameplay script patterns without making it a duplicate component, resource, terrain, or multiplayer guide.

## Wiki Source Coverage

This reference owns the practical script-pattern layer after language syntax is known:

1. A gameplay script task starts by identifying the correct module/folder and creating the script file through Resource Manager or Script Editor.
2. Script files and classes should use a unique creator tag; do not use BI's `SCR_` prefix for mod-owned public classes.
3. Modified script work should mirror the original script module/folder location closely enough for Workbench and the script compiler to resolve it.
4. Existing game classes are modified with `modded`; methods are replaced or extended with `override`.
5. Use `super` when the goal is to extend original behavior and preserve existing logic.
6. A modified script proof-of-concept can be mission/context-dependent. Confirm that the original system exists in the tested scenario before treating the code as broken.
7. Script examples should be designed in stages: class, method, parameters, return value, plain-language logic, code, comments, optimization, and test.
8. A method name should be specific to the job it performs. Generic names like "Method" are teaching placeholders, not production names.
9. `notnull` parameters are useful when null input is invalid, but callers still need safe checks before calling exact APIs.
10. Pick explicit error/default return behavior when input is missing or empty. Returning `-1`, `0`, null, or false must match the method's meaning.
11. Always check divisor values before division; division by zero is a crash-class failure.
12. Comments should explain why, constraints, and non-obvious decisions. Comments that merely restate each line add noise.
13. Optimize after correctness. Wiki guidance says to make it work, make it readable, and only then make it fast.
14. Debug Console script tests must run in the Game environment.
15. Class templates reduce generic-code repetition, but Script Editor detection and type-validity limitations mean they should be used only when the reusable pattern is worth the tradeoff.
16. Script performance should be shaped by asking if work is needed, needed there, needed that often, and needed immediately.

## Terms And Concepts

- Gameplay script pattern: a repeatable structure for implementing behavior, such as a class helper, modded method extension, component script, user action, event callback, or invoker listener.
- Creator tag: the modder/team prefix used on file and class names to avoid collisions.
- `modded`: keyword used to modify an existing script class.
- `override`: keyword used to replace or extend a base method implementation with a matching signature.
- `super`: call to the original/base implementation; use it when extending existing behavior rather than fully replacing it.
- Script module: one of the script roots such as Core, GameLib, Game, GameCode, Workbench, or WorkbenchGame.
- User action: an interaction/action class route commonly implemented by extending `ScriptedUserAction` and overriding action visibility/performance hooks.
- Script component: a script-defined component class route based on `ScriptComponent` and `ScriptComponentClass`.
- Event/callback: a method invoked by engine or gameplay systems; exact event names and signatures must be queried.
- Invoker: callback/listener pattern used by game scripts to notify other code; exact invoker APIs must be queried.
- Debug Console: Script Editor console surface used to run code in the selected runtime environment.
- Performance enemy: code that is unneeded, misplaced, badly shaped, too frequent, too immediate, or too broad for the task.
- Class template: generic class declaration pattern that can operate over multiple compatible types.

## Workbench / Resource / Data Surfaces

Script creation surfaces:

- Resource Manager Resource Browser: use the create action to create a new Script file.
- Script Editor project/file tree: use the create-script workflow when creating script files from inside the editor.
- Script Editor Find Symbol: use it to locate original classes before creating a modified-script counterpart.
- Script Editor Debug Console: run focused script tests after selecting the Game environment.
- Script Editor Breakpoints, Console, and Watch: use them to step through script behavior during Workbench/game testing.

Script module directory mapping from the wiki:

| Script module | Typical directory roots |
| --- | --- |
| core | `Core` |
| gameLib | `GameLib` |
| game | `Game`, `GameCode` |
| workbench | `Workbench` |
| workbenchGame | `WorkbenchGame` |

Modified script layout signals:

- The wiki's modded scoring tutorial locates original scoring scripts in a game-mode scoring directory and creates a matching mod-owned subfolder for modified versions.
- The official modded script sample confirms the mod can contain a project descriptor plus script files under a `Scripts/Game/...` tree.
- Keep modified script work near the original module/family so future Codex lookups can compare original behavior, modded behavior, and sample layout.

User-action surfaces:

- User actions are script classes and data/prefab-driven interaction behavior. This reference owns the script-side pattern only.
- Visibility and performance hooks such as `CanBeShownScript`, `CanBePerformedScript`, and `PerformAction` must be queried before use.
- Registration, component manager ownership, prefab setup, and interaction placement must be verified in the component/prefab owning references.

Script component surfaces:

- Script components use `ScriptComponentClass` and `ScriptComponent` as exact API lookup anchors.
- This reference can route to script-component examples, but component lifecycle, event masks, activeness, and prefab wiring are owned by `entities-components-and-lifecycle.md`.

## Required Workflows

### Create A Practical Gameplay Script

1. Read `enfusion-language-and-script-editor.md` if syntax, ARC, keywords, or editor behavior are uncertain.
2. Identify whether the task is a helper class, modified existing class, script component, user action, or domain-specific behavior.
3. Query exact base classes, callback methods, attributes, and examples before writing code.
4. Create the script file through Resource Manager or Script Editor.
5. Use a unique creator tag for the file and class.
6. Choose a precise class and method name.
7. Start with the smallest local behavior needed for the requested change.
8. Avoid managers, services, registries, wrappers, broad validation, and extra settings unless the defect/request proves they are needed.
9. Validate in Script Editor or the available project checks.
10. Test in Workbench/game/runtime context appropriate to the behavior.

### Modify Existing Game Script Behavior

1. Use Script Editor symbol search or the query script to find the exact original class.
2. Open or inspect the original source around the method being changed with bounded snippets.
3. Confirm the original method signature through game-data lookup.
4. Create the mod-owned script file in the corresponding module/family.
5. Declare a `modded` version of the original class.
6. Override only the method needed.
7. Call `super` when preserving original behavior is required.
8. Avoid copying the whole original class into the modded file.
9. Test in a scenario where the original system exists.
10. If behavior depends on game mode, mission, prefab, or server state, state that runtime verification is required.

### Design A Small Method

1. State the method's single responsibility in plain language.
2. Name the method after that responsibility.
3. Define parameters using exact types and `notnull` only when null input is invalid.
4. Define the return type before writing the body.
5. Decide empty-input/default/error behavior.
6. Write plain-language logic first when the branch/loop shape is non-trivial.
7. Translate the logic to code.
8. Put cheap/null/empty checks before expensive work.
9. Add comments only for why/constraints/non-obvious behavior.
10. Add a focused test route using Debug Console, Workbench runtime, or existing project tests.

### Implement A User Action Script

1. Query `ScriptedUserAction` and its methods before coding.
2. Query user-action examples and inspect a bounded snippet near the top result.
3. Extend `ScriptedUserAction` only after confirming it is the correct base for the task.
4. Use `CanBeShownScript` for UI visibility logic.
5. Use `CanBePerformedScript` for performability/availability logic.
6. Use `PerformAction` for the action effect.
7. Keep visibility checks cheap; they can run often.
8. Guard client-only UI/audio behavior from dedicated-server contexts when examples show that distinction.
9. Route prefab/action registration and interaction placement to component/prefab references.
10. Verify in Workbench/runtime with the owning entity and user entity contexts.

### Use Script Component Examples Without Owning Lifecycle

1. Query exact `ScriptComponent` and `ScriptComponentClass` records.
2. Query examples with the `script-component` subtopic.
3. Use examples to see class-pair naming, attributes, fields, and helper-method structure.
4. Do not infer lifecycle order or event-mask rules from this reference.
5. Read `entities-components-and-lifecycle.md` before wiring components, selecting event masks, or reasoning about activeness.

### Apply Script Performance Guidance

1. Ask whether the operation is needed at all.
2. Ask whether it is needed in this class/entity/instance or should be centralized.
3. Ask whether all data needs to be processed or whether an early acceptable result can stop the loop.
4. Ask whether work can be spread over frames instead of performed all at once.
5. Ask whether a heavy result can be computed once and cached behind a getter.
6. For big `foreach` loops, narrow the list before iterating and continue early for invalid items.
7. For high-frequency scripts, reduce calls, buffer, or cache.
8. For high-performance requests such as very long raycasts, reconsider the need and find a smaller query.
9. Do not optimize away required normal checks, such as verifying a player is alive before an action.
10. State Workbench/runtime profiling or diagnostic verification when performance was part of the change.

## Configuration Fields And Tables

Script file/module table:

| Topic | Rule |
| --- | --- |
| Script roots | Use the module/folder family that matches the target class or system. |
| Creator tag | Prefix mod-owned filenames/classes with a unique tag. Do not use `SCR_` for mod-owned public classes. |
| Class/file match | Keep file and class naming aligned for discoverability. |
| Modified script location | Mirror the original script family closely enough to make the relationship obvious. |
| Read-only source | Do not edit official/source-truth files directly; create mod-owned script files. |

Modified script keywords:

| Keyword | Pattern use |
| --- | --- |
| `modded` | Modify an existing class. |
| `override` | Replace or extend an existing method with a matching signature. |
| `super` | Call original/base behavior when extending behavior. |

Method-design fields:

| Field | Decision to make |
| --- | --- |
| Responsibility | What single job does this method do? |
| Name | Is it precise enough to describe the job? |
| Parameters | What exact types are accepted, and are any `notnull`? |
| Return type | What exact type is returned? |
| Empty input | What does the method return if the input list/entity/resource is missing or empty? |
| Error/default value | Is the fallback meaningful to the caller? |
| Test route | How will the result be validated? |

Class-template tradeoffs:

| Benefit | Risk |
| --- | --- |
| Reduces repeated generic helper code. | Script Editor may not detect every template issue. |
| Works well when operations are valid for every target type. | Methods called on the template type must exist for all intended types. |
| Can centralize casting/helper behavior. | A type that lacks a required method causes errors. |

Script-performance table:

| Pattern problem | Preferred response |
| --- | --- |
| Not needed | Remove code or split processing so only needed cases run. |
| Misplaced | Move responsibility/data to the correct owner or central class. |
| Ill-conceived | Stop once an acceptable result is found. |
| Too spread in one frame | Spread work over multiple frames when correctness allows. |
| Immediate repeated calculation | Compute once, cache in a member, expose through a getter. |
| Big `foreach` | Narrow inputs and continue early for non-viable items. |
| High-frequency scripts | Use cheaper calls, buffering, or caching. |
| Excessive request | Reconsider scope and query a smaller area/data set. |

## Procedures And Ordered Steps

Script file creation checklist:

1. Confirm the task belongs in script and not only in data/prefab/config.
2. Choose the owning reference for the workflow.
3. Use Resource Manager or Script Editor to create the script file.
4. Place it in the correct script module/family.
5. Prefix with the modder/team tag.
6. Use exact base classes and method signatures from query output.
7. Validate scripts before runtime testing.

Modified script checklist:

1. Find the original class.
2. Query the original method signature.
3. Create a mod-owned file for the modified class.
4. Declare `modded class ExistingClassName`.
5. Override the exact method.
6. Call `super` if original logic must remain.
7. Keep the override small.
8. Test in a context where the original system exists.

User-action checklist:

1. Run `lookup "make a user action"`.
2. Verify `ScriptedUserAction` inheritance and methods.
3. Inspect one top user-action snippet.
4. Add only the fields needed by the action.
5. Keep visibility/performability checks cheap and null-safe.
6. Put the actual effect in `PerformAction`.
7. Guard presentation/client-only behavior when examples show dedicated-server separation.
8. Validate registration/prefab/action availability in Workbench/runtime.

Performance checklist:

1. Remove unneeded work.
2. Move misplaced work to the correct owner.
3. Stop loops early when possible.
4. Spread unavoidable heavy work.
5. Cache repeated heavy results.
6. Avoid high-frequency expensive calls.
7. Do not remove correctness checks to chase micro-optimizations.
8. Verify with runtime/profiling when performance is the goal.

Debug/test checklist:

1. Validate scripts in Script Editor.
2. Use breakpoints on executable lines.
3. Use Watch for current variable state.
4. Use Console only in the correct runtime environment.
5. For Debug Console examples, select Game environment.
6. If a breakpoint does not hit, confirm scripts were recompiled/reloaded and the tested scenario reaches the code.
7. State any remaining Workbench/runtime/server verification.

## Warnings And Failure Modes

- Do not use this reference as a syntax guide; read the language/editor reference first for language-level uncertainty.
- Do not use BI's `SCR_` prefix for mod-owned public classes.
- Do not guess method signatures for `override`; query the exact method before writing.
- Do not copy entire original classes into modded files when a small override is enough.
- Do not omit `super` when the original behavior must remain.
- Do not call `super` when the task intentionally replaces behavior; make that intent explicit.
- Do not assume a modded proof-of-concept works in every mission. It may require a specific game mode/system to be present.
- Do not treat class-template helpers as universally safe. Called methods must be valid for every candidate type.
- Do not write generic method names in production code.
- Do not return a default/error value without deciding what the caller should do with it.
- Do not divide without checking whether the divisor can be zero.
- Do not write comments that restate individual lines.
- Do not prematurely optimize before correctness/readability.
- Do not ignore script performance when logic runs every frame, across many entities, or over large lists.
- Do not make user-action visibility checks expensive.
- Do not assume user actions are purely client-side or server-side; verify examples and runtime context.
- Do not infer component lifecycle, event masks, or activeness rules from this reference.
- Do not infer replication/authority behavior from local script examples.
- Do not skip Workbench/runtime validation for behavior that depends on game mode, prefab wiring, action manager registration, or server/client context.

## API Lookup Keys

Use these lookup keys when writing API-sensitive gameplay script code:

- `ScriptComponent`
- `ScriptComponentClass`
- `GenericComponent`
- `GenericComponentClass`
- `ScriptedUserAction`
- `BaseUserAction`
- `PerformAction`
- `CanBeShownScript`
- `CanBePerformedScript`
- `Init`
- `IEntity`
- `GenericComponent`
- `Attribute`
- `ComponentEditorProps`
- `UIWidgets`
- `Print`
- `DbgUI`
- `ScriptInvoker`
- `Invoker`
- `EventHandler`
- `EventHandlers`

Common example families to query:

- script component examples;
- user-action examples;
- modded script examples;
- invoker/event examples;
- debug/logging examples;
- performance-sensitive examples only after exact task routing.

Do not copy signatures from memory. Query exact symbols, methods, inheritance, examples, and snippets every time API-sensitive code is written.

## Game-Data Query Commands

Use these commands from the repo root.

Script component anchors:

```powershell
py -3 scripts\query-reforger-data.py symbol ScriptComponent --kind class --exact
py -3 scripts\query-reforger-data.py symbol ScriptComponentClass --kind class --exact
py -3 scripts\query-reforger-data.py inherits ScriptComponent
py -3 scripts\query-reforger-data.py examples component --subtopic script-component
```

User action anchors:

```powershell
py -3 scripts\query-reforger-data.py lookup "make a user action"
py -3 scripts\query-reforger-data.py inherits ScriptedUserAction
py -3 scripts\query-reforger-data.py method ScriptedUserAction PerformAction --exact
py -3 scripts\query-reforger-data.py method ScriptedUserAction CanBeShownScript --exact
py -3 scripts\query-reforger-data.py method ScriptedUserAction CanBePerformedScript --exact
py -3 scripts\query-reforger-data.py examples user-action
```

Modded script and existing-class routes:

```powershell
py -3 scripts\query-reforger-data.py files ScoringSystem --limit 20
py -3 scripts\query-reforger-data.py files modded --limit 20
py -3 scripts\query-reforger-data.py files super --limit 20
```

Events, invokers, and debug routes:

```powershell
py -3 scripts\query-reforger-data.py files EventHandler --limit 20
py -3 scripts\query-reforger-data.py files ScriptInvoker --limit 20
py -3 scripts\query-reforger-data.py files Print --limit 20
py -3 scripts\query-reforger-data.py files DbgUI --limit 20
```

Snippets after exact query output:

```powershell
py -3 scripts\query-reforger-data.py snippet <scripts/...file.c> --line <line> --context 30
```

Do not load broad schema/API dumps for this topic. Use exact symbol, method, inheritance, example, file, and snippet queries.

## Examples And Samples

Official sample reviewed:

- `SampleMod_ModdedScript`: confirms a modded-script addon can contain a project descriptor and script files under a game script tree. The sample modifies scoring classes with `modded`, uses `override`, calls `super` when extending original suicide behavior, and keeps score-calculation replacement local to the overridden method.

Use the sample as a layout/pattern signal only:

- verify exact current method signatures before writing overrides;
- do not copy sample source blindly;
- keep the changed method small;
- test in a mission where the original scoring system exists.

Useful game-source example routes:

```powershell
py -3 scripts\query-reforger-data.py examples user-action --limit 12
py -3 scripts\query-reforger-data.py examples component --subtopic script-component --limit 12
py -3 scripts\query-reforger-data.py inherits ScriptedUserAction
py -3 scripts\query-reforger-data.py inherits ScriptComponent
```

Representative snippets reviewed through query output:

- `scripts/Game/FactionCommander/UserActions/SCR_FactionCommanderOpenMapUserAction.c` shows a `ScriptedUserAction` with attributes, initialization, dedicated-server guard, visibility/performability hooks, and action behavior.
- `scripts/Game/Components/HybridPhysicsComponent.c` shows a `ScriptComponentClass` plus `ScriptComponent` pair, component editor props, attributes, fields, helper methods, and comments.

Use snippets only after a query returns exact file/line results. Keep snippets bounded.

## Follow-Up Keywords

Use these as search/query terms when this reference is not enough:

- `Scripting Modding`
- `Scripting Example`
- `Class Template Example`
- `Scripting Performance`
- `modded`
- `override`
- `super`
- `creator tag`
- `ScriptComponent`
- `ScriptComponentClass`
- `ScriptedUserAction`
- `BaseUserAction`
- `PerformAction`
- `CanBeShownScript`
- `CanBePerformedScript`
- `Init`
- `Attribute`
- `ComponentEditorProps`
- `UIWidgets`
- `ScriptInvoker`
- `EventHandler`
- `Print`
- `DbgUI`
- `Debug Console`
- `Game environment`
- `breakpoint`
- `Watch`
- `performance enemies`
- `high-frequency scripts`
- `big foreach`
- `premature optimization`

## Verification

Before finalizing gameplay script code:

- Confirm the owning reference was read for the task.
- Confirm language/syntax uncertainty was checked in `enfusion-language-and-script-editor.md`.
- Confirm exact classes, methods, attributes, enum values, and callback signatures were queried.
- Confirm the script file uses a modder/team tag.
- Confirm a modified class overrides only the needed method.
- Confirm `super` use matches the intended behavior.
- Confirm user-action visibility and performability checks are cheap and null-safe.
- Confirm component lifecycle/prefab wiring questions were routed to `entities-components-and-lifecycle.md`.
- Confirm replication/authority questions were routed to `multiplayer-replication-and-authority.md`.
- Confirm expensive loops, per-frame work, and large searches were checked against the performance rules.
- Confirm Script Editor validation was run when available.
- Confirm Workbench/runtime behavior was tested in a scenario where the target system exists.
- Confirm dedicated-server/multiplayer behavior was tested or explicitly left as residual verification when relevant.

Residual uncertainty to state in final answers:

- If Workbench validation was not run, say that API lookup/source review was done but Script Editor validation remains.
- If the behavior depends on prefab wiring or action registration, say that Workbench/prefab verification remains.
- If the behavior depends on server/client/authority, say that multiplayer or dedicated-server verification remains.
- If performance was changed, say whether profiling/runtime measurement was performed.

## Official Wiki Links

- Scripting Modding: https://community.bistudio.com/wiki/Arma_Reforger:Scripting_Modding
- Scripting Example: https://community.bistudio.com/wiki/Arma_Reforger:Scripting_Example
- Class Template Example: https://community.bistudio.com/wiki/Arma_Reforger:Class_Template_Example
- Scripting: Performance: https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Performance
- Script Editor: https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor
- Resource Manager: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager

## Usefulness Score

Score: 91/100

- Wiki coverage: 28/30. All primary scripting-pattern pages were reviewed and represented. Script Editor and Resource Manager are intentionally partial because their full workflows are owned elsewhere. Official wiki links and coverage gaps are listed.
- Operational detail: 14/15. The reference preserves script creation routes, module/folder mapping, modified script workflow, `super` usage, method-design steps, user-action pattern, debugging route, and performance checklist.
- API lookup usefulness: 14/15. Exact query commands are included for `ScriptComponent`, `ScriptComponentClass`, `ScriptedUserAction`, user-action methods, inheritance, examples, events, invokers, and snippets. Exact signatures remain query-owned.
- Example grounding: 9/10. `SampleMod_ModdedScript`, script-component examples, user-action examples, and representative bounded snippets are included as routes without copying source bodies.
- Codex task usefulness: 14/15. Codex can route common gameplay script tasks, user actions, modded class changes, method design, and performance checks without guessing or loading broad dumps.
- Context efficiency: 8/10. The reference is dense and scoped. It includes some component/user-action route detail because those are common script tasks, but lifecycle and prefab ownership remain explicitly cross-linked.
- Verification guidance: 4/5. Includes Script Editor, Workbench/runtime, prefab/action registration, multiplayer/server residuals, and performance verification. Full profiling workflow belongs to diagnostics.

Category-fit check:

- Source family complete: pass. Scripting Modding, Scripting Example, Class Template Example, and Scripting: Performance are represented.
- No owned page missing: pass. Every owned primary page is listed in Source Inventory.
- Split boundary justified: pass. Language/editor basics, component lifecycle, prefab/resource wiring, replication, diagnostics, and terrain setup are explicitly routed elsewhere.
- Cross-links present: pass. Nearby workflow owners are named in When To Read, Source Inventory, Required Workflows, and Verification.
- Task route clear: pass. Common tasks route to this reference plus exact query commands: create a practical script, modify an existing script, implement a user action, use script-component examples, and apply performance guidance.

Missed coverage/cap review:

- No owned primary wiki page was skipped.
- No relevant primary section was omitted without an ownership note.
- Tables, procedures, warnings, template limitations, module mapping, user-action query routes, and performance examples are represented.
- No full wiki page, source body, broad API dump, machine-specific filesystem path, or live wiki-fetch instruction is included.
- No automatic failure condition applies.
