# Enfusion Language And Script Editor

## When To Read

Read this before writing or reviewing Enforce/Enfusion Script syntax, language constructs, style, memory/reference behavior, JSON/config-object language usage, or Script Editor validation/debugging workflow.

Use this reference for:

- choosing correct Enforce Script syntax instead of guessing from C#, SQF, Arma 3, Unity, or Unreal habits;
- understanding strong typing, identifiers, constants, scope, casting, arrays, maps, sets, vectors, and typename;
- checking operators, precedence, keyword behavior, loop forms, `thread`, `delete`, `ref`, `out`, `inout`, `notnull`, `modded`, `vanilla`, `this`, and `super`;
- applying official naming, formatting, file/class, variable, method, documentation, and moddability conventions;
- understanding ARC strong/weak references and cyclic-reference risks;
- using JSON and JsonApiStruct workflows at a language/API-usage level;
- using the Script Editor to navigate, validate, debug, inspect errors, search symbols, and run code in the console.

Do not use this as the primary source for:

- gameplay script patterns, user actions, logging patterns, or modded gameplay examples: read `script-events-actions-and-patterns.md`;
- entity/component lifecycle, event masks, activeness, prefab wiring, or component ownership: read `entities-components-and-lifecycle.md`;
- full Resource Manager/config/prefab authoring workflows: read `resource-manager-file-types-and-editors.md` and `prefabs-configs-containers-and-catalogs.md`;
- Workbench plugin authoring beyond Script Editor usage and script-editing plugins: read `workbench-plugins-and-editor-tools.md`;
- exact API signatures: query game data with `scripts/query-reforger-data.py`.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: Enforce Script syntax, SQF-to-Enforce migration, scripting values, operators, keywords, conventions, best practices, automatic reference counting, JSON syntax, JsonApiStruct language usage, Script Editor usage, and script-editing plugin behavior.
- Secondary/cross-reference topics: Config Object and BaseContainer only where they document script decorators/types used by language-level config classes; full config/resource authoring belongs to config/resource references.

Wiki pages reviewed:
- Enforce Script Syntax - https://community.bistudio.com/wiki/Arma_Reforger:Enforce_Script_Syntax - status: covered - reason: primary syntax and type overview.
- From SQF to Enforce Script - https://community.bistudio.com/wiki/Arma_Reforger:From_SQF_to_Enforce_Script - status: covered - reason: primary migration pitfalls from SQF habits.
- Scripting: Values - https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Values - status: covered - reason: primary owner for values, identifiers, type behavior, scope, casting, and type defaults.
- Scripting: Operators - https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Operators - status: covered - reason: primary owner for precedence and operator behavior.
- Scripting: Keywords - https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Keywords - status: covered - reason: primary owner for class, method, value, code, and control-flow keywords.
- Scripting: Conventions - https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Conventions - status: covered - reason: primary owner for naming, formatting, file/class, method, variable, Doxygen, and moddability conventions.
- Scripting: Best Practices - https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Best_Practices - status: covered - reason: primary owner for readability/performance coding guidance.
- Scripting: Automatic Reference Counting - https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Automatic_Reference_Counting - status: covered - reason: primary owner for ARC, strong/weak references, and cyclic-reference risks.
- Scripting: JSON - https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_JSON - status: covered - reason: primary owner for JSON format rules.
- JsonApiStruct Usage - https://community.bistudio.com/wiki/Arma_Reforger:JsonApiStruct_Usage - status: covered - reason: primary owner for JsonApiStruct registration, packing/expanding, callbacks, errors, and validation.
- Scripting: Config Object - https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Config_Object - status: partial - reason: included for `BaseContainerProps`, `Attribute`, and language-facing decorator semantics; full config workflows belong to `prefabs-configs-containers-and-catalogs.md`.
- BaseContainer Usage - https://community.bistudio.com/wiki/Arma_Reforger:BaseContainer_Usage - status: partial - reason: included for language/API caveats around BaseContainer references and `Get`/`Set`; full container/resource editing belongs elsewhere.
- Scripting: Do's and Don'ts - https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Do%27s_and_Don%27ts - status: covered - reason: reinforces script-safety and scoping rules.
- Scripting: Preprocessor Directives - https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Preprocessor_Directives - status: covered - reason: language-level preprocessing.
- Scripting: Preprocessor Macros - https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Preprocessor_Macros - status: covered - reason: language-level macro guidance.
- Script Editor - https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor - status: covered - reason: primary Script Editor usage, validation, navigation, debugging, and console workflow.
- Script Editor Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor_Plugin - status: partial - reason: included only for Script Editor module/API awareness and editor-plugin boundary; full plugin authoring belongs to `workbench-plugins-and-editor-tools.md`.
- Script Editor: Autocomplete Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor:_Autocomplete_Plugin - status: covered - reason: script-writing assistance, keyword/attribute suggestions, safety checks.
- Script Editor: Basic Code Formatter Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor:_Basic_Code_Formatter_Plugin - status: covered - reason: code formatting and warning support.
- Script Editor: Class Renaming Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor:_Class_Renaming_Plugin - status: covered - reason: script/editing refactor workflow.
- Script Editor: Create New Script Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor:_Create_New_Script_Plugin - status: covered - reason: editor workflow for script creation.
- Script Editor: Doxygen Filler Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor:_Doxygen_Filler_Plugin - status: covered - reason: documentation workflow.
- Script Editor: Fill From Template Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor:_Fill_From_Template_Plugin - status: covered - reason: template workflow.
- Script Editor: SVN Plugins - https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor:_SVN_Plugins - status: partial - reason: included only as Script Editor source-control surface; repository policy is project-specific.
- Script Editor Plugins category - https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Official_Tools/Script_Editor_Plugins - status: covered - reason: category confirms plugin family.

Wiki sections covered:
- Enforce Script Syntax > Page, Data Types, Object-Oriented Programming, Operations > Assignation, Operations > Logic - coverage: full.
- From SQF to Enforce Script > Similarities, If-Then-Else, for, foreach, while, switch, Others, Case Sensitivity, Typed Variables, Position, Array, Data Types, Object-Oriented Programming - coverage: full.
- Scripting: Values > Identifier, Value Declaration, const, Passing a Value, Types, primitive and object types, Scope, Casting - coverage: full.
- Scripting: Operators > Precedence, assignment, arithmetic, relational, logical, bitwise, string, indexing - coverage: full.
- Scripting: Keywords > Class Keywords, Method Keywords, Values Keywords, Code Keywords, Code Flow Keywords - coverage: full.
- Scripting: Conventions > Tag, File/Class, Method, Variable, Order, Script, Spacing, Method, Miscellaneous, Moddability, Example - coverage: full.
- Scripting: Best Practices > Code Format, Variable Format, Code Structuration, SOLID, DRY, Logical Simplifications, Examples, Comments, Files Organisation - coverage: full.
- Scripting: Automatic Reference Counting > Principle, Strong Reference, Weak Reference, Usage, Cyclic Reference problem/solution - coverage: full.
- Scripting: JSON and JsonApiStruct Usage sections - coverage: full.
- Script Editor > Features, Getting Started, Validation/Errors, Preferences, Navigation, Searching, Keyboard Shortcuts, Debugging, Console, VM Exceptions - coverage: full.
- Script Editor plugin pages - coverage: editor-usage/plugin-surface portions only.
- Config Object/BaseContainer sections - coverage: partial and routed.

Structured wiki records:
- Tables reviewed/included: data types, primitive type ranges/defaults/sizes, prefix cheat sheets, operator precedence, keyword tables, best-practice good/bad examples, config decorator parameter tables, Attribute widget compatibility/settings, JsonApiStruct works/does-not-work table, JSON examples, Script Editor feature/icon/shortcut tables.
- Procedures reviewed/included: Script Editor open/validate/error flow; searching and goto declaration; breakpoint/debug/watch/callstack/console flow; create script plugin parameters; autocomplete and formatter usage; JsonApiStruct declaration, file operations, packing, validation; BaseContainer read/update cautions.
- Admonitions reviewed/included: strong typing, identifier restrictions, string nullability, float precision, wrong casts returning null, no JSON comments, no trailing commas, ARC cyclic reference risk, local `ref` redundancy, `thread` scope, `delete` exception with external references, static reset behavior, read-only script files, Script Editor errors/callstack reading, BaseContainer reference limitations.
- Code blocks reviewed/included: syntax/operator/value examples, ARC examples, JSON examples, JsonApiStruct examples, Script Editor debug/console examples. Runtime reference paraphrases behavior and does not copy source bodies.
- Media reviewed: Script Editor layout, validation/errors, navigation/search, debugger, console, and plugin screenshots. Media is not copied; behavior is represented.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts\query-reforger-data.py attribute Attribute --limit 10`
  - `py -3 scripts\query-reforger-data.py files BaseContainer --limit 10`
  - `py -3 scripts\query-reforger-data.py symbol JsonApi --limit 10`
  - `py -3 scripts\query-reforger-data.py files ScriptEditor --limit 10`
- Symbols/methods/attributes verified: `Attribute`, `JsonApiStruct`, `BaseContainer`, `ScriptEditor`, and Script Editor plugin classes were found as exact lookup routes. Exact signatures remain query-owned.
- Examples/snippets reviewed: query output showed generated API records and handwritten Script Editor plugin implementations. Snippets were not embedded.

Samples and source examples:
- Official sample folders reviewed: `SampleMod_ModdedScript` for script folder/project layout and modded script task routing.
- Source example families reviewed through query output: Script Editor module, autocomplete plugin, formatter plugin, class renaming plugin, and related Workbench Script Editor files.

Coverage gaps:
- Missing, excluded, or intentionally deferred source: gameplay scripting examples, component lifecycle, user actions, config/prefab authoring, full Workbench plugin authoring, diagnostic/performance profiling.
- Reason and impact: those are owned by narrower references. This reference covers the language/editor layer and routes implementation APIs through query commands.

## Wiki Source Coverage

This reference owns the language surface Codex must understand before writing Arma Reforger script:

1. Enforce Script is an object-oriented language used by Enfusion. It is C-like, but Reforger behavior must be verified from Reforger sources.
2. Values are strongly typed; a variable keeps one type for its lifetime.
3. Identifiers are case-sensitive, must start with a letter or underscore, may contain ASCII letters/numbers/underscores, and cannot equal a keyword.
4. Primitive values, vectors, arrays, sets, maps, classes, enums, and typename each have different default values, pass-by behavior, comparison behavior, and naming prefixes.
5. Operators mostly follow C precedence, but Enforce-specific caveats matter for arrays, strings, vectors, `!`, indexing, and int division.
6. Keywords define class structure, method visibility, parameter passing, value ownership/reference behavior, code flow, threading, deletion, and modded-class behavior.
7. ARC replaces garbage collection. Strong references keep objects alive; weak references can become null; cyclic strong references leak until shutdown.
8. Official conventions require creator tags, Allman braces, tabs, PascalCase methods/classes, camelCase local variables/parameters, `m_`/`s_` member/static prefixes, and Doxygen-compatible public docs.
9. JSON syntax has strict formatting rules and no comments. JsonApiStruct provides script-side JSON registration/packing/expanding and callback/error events.
10. Script Editor is the official Workbench surface for editing, validating, navigating, debugging, searching, and inspecting scripts.

The wiki detail preserved here is intentionally dense because language mistakes cascade into bad API guesses and broken Reforger scripts.

## Terms And Concepts

- Enforce Script / Enfusion Script: object-oriented scripting language used by Enfusion and Arma Reforger.
- Strong typing: a value has one type and cannot change type during its lifetime.
- Value: data holder, either mutable variable or immutable constant.
- Identifier: the name of a value; case-sensitive and keyword-restricted.
- Primitive type: `int`, `float`, `bool`, `string`, `vector`, `void`, class pointer, or `typename`.
- Object type: class instance, enum, static array, dynamic array, set, map, or other managed object.
- Static array: fixed-size list; array size cannot change.
- Dynamic array: growable list; default value is null unless initialized.
- Set: unique-value collection; insertion order is not guaranteed.
- Map: key-value collection; float keys are not allowed.
- Typename: reflection-style class-information value; default is `typename.Empty`, not null.
- Scope: the area/lifetime where a variable exists and can be accessed.
- Cast: converting a base/interface-typed reference into a known underlying type. Wrong casts return null, not an exception.
- ARC: automatic reference counting; object lifetime depends on strong reference count.
- Strong reference: increments the object reference count.
- Weak reference: does not increment the object reference count and may become null.
- `ref`: strong-reference keyword for object references.
- `autoptr`: not useful in normal script because script classes inherit `Managed` and ARC handles them.
- `out`: parameter may be changed by the method.
- `inout`: parameter is used and may be changed by the method.
- `notnull`: class-pointer parameter must not be null; passing null raises a VM exception and the method is not called.
- `modded`: class extension that takes the original class place in modded script behavior.
- `vanilla`: refers to the unmodded version of a modded variable or method.
- `thread`: creates a script thread. Wiki guidance says use it in Workbench plugins; in game code prefer game call queue scheduling.
- JsonApiStruct: generated API-backed class for JSON conversion, file/string import/export, and backend callback data.
- Script Editor: Workbench module for script editing, validation, navigation, debugging, output, console, and search.

## Workbench / Resource / Data Surfaces

Script Editor surfaces:

- Text Editor: edits script files and shows line numbers, file tabs, script errors, warnings, breakpoints, bookmarks, and read-only state.
- Projects window: browses project/module script files and supports file search/context menu actions.
- Outline: lists symbols in the open file and navigates to variables, methods, classes, and related declarations.
- Output: displays `Print` and diagnostic output.
- Errors: displays validation/compilation errors; double-click navigates to location.
- Find Results: displays results from text/symbol searches.
- Find File: searches script file names.
- Find Symbol: searches script symbols across files.
- Find in Files: searches text across files.
- Goto Declaration: jumps to a symbol declaration from an open script file.
- Find in Entire Solution: project-wide reference/search from the selected symbol.
- Find Entity: finds named world entities with associated scripts when a world is open.
- Debug window: continue, step over, step into, step out, and stop.
- Breakpoints: enable/disable/remove breakpoints; invalid breakpoints indicate code no longer matches the running target.
- Watch: inspect current variable values during debugging.
- Callstack: shows method call order and must be read from bottom to top.
- Console: run script code during playmode or at a breakpoint; results appear in Output.

Script Editor plugin surfaces:

- Autocomplete Plugin: keyword/autocomplete assistance, safety checks, attribute decorators, default keywords, and configurable keyword/attribute presets.
- Basic Code Formatter Plugin: formatting and bad-practice warning support; formatter examples exist in game source.
- Class Renaming Plugin: class/word rename workflow with parameters controlling script/prefab file processing and directory scope.
- Create New Script Plugin: creates script files under selected addon/destination directories.
- Doxygen Filler Plugin: generates documentation/comment scaffolding around methods, constructors, destructors, overridden/static/obsolete methods, and separators.
- Fill From Template Plugin: creates script content from templates and parameters.
- SVN Plugins: source-control commands inside Script Editor; use only when the project uses SVN.

Config/language surfaces:

- `BaseContainerProps`: decorator that makes a class visible/editable in Config Editor when used for config-root language classes.
- `Attribute`: decorator that makes a member variable visible/editable in Config Editor, with default value, widget, description, params, enum choices, category, precision, enum type, and prefab behavior.
- `BaseContainer`: data container API surface; cannot be strongly referenced in script and must be used carefully when reading/updating config/prefab/world data.
- `JsonApiStruct`: JSON conversion API surface; register variables with `RegV`, then pack/expand/import/export/validate through exact API methods.

## Required Workflows

### Before Writing Any Script

1. Identify whether the task is language/editor, gameplay pattern, component lifecycle, resource/config, Workbench plugin, or domain workflow.
2. Read the owning reference for the task.
3. Use this reference for language syntax and Script Editor behavior.
4. Query exact APIs before writing API-sensitive code.
5. Prefer explicit Reforger types over `auto` when the type is known.
6. Keep the change local and avoid broad abstractions unless the defect/request requires them.

### Validate Script Syntax In Script Editor

1. Open Workbench.
2. Open Script Editor from Workbench's editor menu or Resource Manager welcome page.
3. Open or create the target script file from Projects/Text Editor.
4. Write the code in Text Editor.
5. Use Build > Validate Scripts.
6. Read Errors and Output.
7. Double-click errors to navigate to failing lines.
8. Fix the first/root syntax issue first; later errors can be cascade failures.
9. Validate again until compilation succeeds.

### Navigate Existing Code

1. Use Find File when the file name is known.
2. Use Find Symbol when looking for a class, method, variable, or enum symbol.
3. Use Find in Files for text matches.
4. Use Goto Declaration from a symbol in the Text Editor when available.
5. Use Find in Entire Solution for project-wide references.
6. Use Outline to navigate symbols in the current file.

For Codex work, prefer `scripts/query-reforger-data.py` for source-backed API lookup before using broad text search.

### Debug Script Runtime Behavior

1. Place a breakpoint beside the line number or use the shortcut.
2. Launch/run the target context so the code executes.
3. Use Continue, Step Over, Step Into, Step Out, and Stop to inspect flow.
4. Use Watch to inspect variable values.
5. Read Callstack from bottom to top.
6. Use Console only in playmode or when stopped at a breakpoint.
7. Treat Virtual Machine Exceptions as runtime failures requiring null/type/lifecycle review.
8. If a breakpoint becomes invalid, rebuild/reload and verify that running code matches edited code.

### Convert SQF Habits To Enforce Habits

1. Replace keyword-bridged SQF style with normal `if`, `else`, `else if`, `for`, `foreach`, `while`, and `switch`.
2. Respect case sensitivity everywhere.
3. Give variables concrete types; one variable cannot become another type later.
4. Use strongly typed arrays, sets, and maps; do not rely on mixed-type SQF-style arrays.
5. Use vectors and transform matrices according to Enfusion coordinate rules. The wiki notes Enfusion is left-handed.
6. Do not assume an Arma scheduler equivalent; the wiki warns that Enforce Script does not benefit from previous titles' scheduler.
7. Avoid uncontrolled thread creation. In game code route timing through game call queue patterns, after verifying exact APIs.

### Use JsonApiStruct

1. Create a class inheriting from `JsonApiStruct`.
2. Declare script variables with exact types.
3. Register each variable with `RegV` in the constructor.
4. For nested structure, register child objects and initialize them when needed.
5. For JSON input, use file load or raw expansion routes after querying exact methods.
6. For JSON output, pack and read string/file output after querying exact methods.
7. Handle `OnExpand`, `OnBufferReady`, `OnSuccess`, and `OnError` only after verifying exact signatures.
8. Validate by pack/expand/pack comparison and inspect formatted JSON externally when needed.

### Use Config Decorators In Script

1. Use `BaseContainerProps` only when defining script classes meant to be visible/editable in Config Editor.
2. Use `configRoot: true` for a base object config that should be selectable during config creation.
3. Decorate child classes too; inheriting from a decorated class is not enough for usability.
4. Use `Attribute` on member variables that should appear in Config Editor.
5. Store `Attribute` default values as strings, including bools, numbers, and vectors.
6. Use `uiwidget`, `params`, `enums`, `enumType`, and `desc` deliberately; exact allowed API values must be queried.
7. Route full resource/config authoring details to the config/prefab references.

## Configuration Fields And Tables

Core type behavior:

| Type | Passes by | Default | Naming prefix | Important caveat |
| --- | --- | --- | --- | --- |
| `bool` | value | `false` | `b` | Only true or false. |
| `int` | value | `0` | `i` | Division floors when both operands are ints. |
| `float` | value | `0.0` | `f` | Precision is approximate; use almost-equal checks where appropriate. |
| `string` | value | empty string | `s` | Cannot be null; comparison is case-sensitive. |
| `vector` | value | `0 0 0` equivalent | `v` | Holds three floats; supports value comparison. |
| `enum` | value | `0` | `e` | Default 0 may not map to a named enum value. |
| dynamic `array` | reference | null | `a` | Size can change; value equality is not direct. |
| static array | value | filled with item defaults | `a` | Fixed size; indexing is very efficient. |
| `set` | reference | null | none | Unique values; order not guaranteed. |
| `map` | reference | null | `m` | Keys must be unique; float cannot be a key. |
| class/object | reference | null | none | Wrong cast returns null. |
| `typename` | reference | `typename.Empty` | none | Cannot assign null; invalid type conversion returns empty. |

Identifier rules:

| Rule | Requirement |
| --- | --- |
| Allowed characters | ASCII letters, numbers, underscores. |
| First character | Letter or underscore; not a number. |
| Case | Case-sensitive. |
| Keyword conflict | Identifier cannot be identical to a keyword. |
| Variable style | camelCase for locals/parameters. |
| Constant style | UPPER_CASE with underscores and no member/static prefix. |

Convention rules:

| Item | Rule |
| --- | --- |
| Creator tag | Classes and global functions must use a unique creator tag to avoid conflicts. Do not use BI's `SCR_` tag for mod content. |
| File/class | File and class names should match; component files end with `Component`, entity files end with `Entity`. |
| Enum | Enum name starts with capital `E`; enum values are uppercase underscore-separated. |
| Location | Script files are conventionally under the game script tree for addon gameplay script. |
| Methods | PascalCase. |
| Parameters/local variables | camelCase. |
| Member variables | `m_` plus optional one-letter type prefix and PascalCase. |
| Static variables | `s_` plus optional one-letter type prefix and PascalCase. |
| Global variables | `g_`, but global variables are bad practice except absolute necessity. |
| Braces | Allman style; braces on new lines. |
| Indentation | Tabs, with Script Editor displaying tabs as four spaces. |
| Visibility | Prefer protected/private unless API is intentionally exposed. |
| Documentation | Public API should use Doxygen-compatible `//!` comments. |
| Method separator | Official convention uses a long separator comment between methods. |

Operator caveats:

| Operator/topic | Rule |
| --- | --- |
| `=` | Assignment, not equality. Use `==` for equality. |
| `/` | Int/int division returns floored int. |
| `%` | Integer modulo only; query float alternatives such as `Math.Repeat` before use. |
| `==` / `!=` | Arrays and objects compare references, not deep values. Vector compares values. String comparison is case-sensitive. |
| `!` | Works on bool, numeric zero, empty string, or null object, but `if (!stringOrNumber)` is discouraged; prefer explicit checks. |
| string `+` | Left operand must be string for automatic stringification. |
| `[]` | Efficient on static arrays. For other containers it behaves like `Get(i)`; cache or use `foreach` to avoid repeated calls. |
| bit shifts | Watch sign extension on right shift. |

Keyword caveats:

| Keyword | Rule |
| --- | --- |
| `private` | Accessible from same class methods. Modded class can use it, but children cannot. |
| `protected` | Accessible from class, children, and modded class. |
| `static` | Class-level. Static properties reset game-wide on modded scenario start/leave because game/scripts reload. |
| `override` | Compiler checks base method presence and signature. Static override dispatch depends on currently-known class. |
| `sealed` | Prevents class inheritance or method override. |
| `out` | Method may replace/change argument. |
| `inout` | Method uses and may replace/change argument. |
| `notnull` | Passing null causes VM exception and method is not called. Caller still must null-check before calling. |
| `new` | Constructor calls must use parentheses. |
| `delete` | Deletes object and nulls references, but can throw if an external reference such as an array still exists. |
| `thread` | Use in Workbench plugins; in game code prefer CallQueue scheduling after exact API lookup. |
| `debug` | Triggers breakpoint in Script Editor, but wiki notes it may not be highlighted. |

Config decorator fields:

| Decorator | Key fields |
| --- | --- |
| `BaseContainerProps` | `category`, `description`, `color`, `visible`, `insertable`, `configRoot`, `icon`, `namingConvention`. |
| `Attribute` | `defvalue`, `uiwidget`, `desc`, `params`, `enums`, `category`, `precision`, `enumType`, `prefabbed`. |

`Attribute` details to preserve:

- `defvalue` is always a string, including bools, numbers, and vectors.
- Object defaults cannot be set through `defvalue`.
- Array default applies to new item values, not the array itself.
- `desc` provides tooltip text.
- `params` is widget-specific and can define numeric ranges, array max size, curve ranges, vector purpose/space, and resource picker filters.
- `enumType` should be preferred over dynamically creating enum arrays when using enum combobox/flags UI.

JSON format rules:

| JSON item | Rule |
| --- | --- |
| Root | Parent/root is always an object. |
| Property | Name left of colon; value right of colon. |
| Strings/properties | Use double quotes. |
| Commas | Required between following properties/items; forbidden after the last property/item. |
| Comments | Not allowed. |
| Boolean | Only `true` or `false`. |
| Number | Integer or float without quotes; cannot start with a period; scientific notation accepted. |
| String | Cannot contain raw line returns; use accepted escapes. |
| Object | Nested named object. |
| Array | Can contain direct values or objects. |

## Procedures And Ordered Steps

Language check before writing:

1. Choose the correct owning reference for the task.
2. Identify exact classes/methods/attributes through game-data query before coding.
3. Check this reference for type, keyword, operator, ARC, and convention rules.
4. Use explicit types where known.
5. Prefer clear code over one-line compression.
6. Order cheap boolean checks before expensive method calls.
7. Cache repeated method calls inside loops when needed.
8. Prefer `foreach` for start-to-end array iteration.
9. Use early returns to reduce nested code when it improves clarity.
10. Validate in Script Editor or with available project checks.

Class/file creation checklist:

1. Pick a unique creator tag.
2. Name the file and class consistently.
3. Put component/entity suffixes where convention requires them.
4. Use PascalCase class/method names.
5. Use camelCase parameters/local variables.
6. Use member/static prefixes for class fields.
7. Use Allman braces and tab indentation.
8. Keep visibility protected/private unless external access is intended.
9. Add Doxygen comments for public API.
10. Query exact base class, constructor, and override signatures before writing.

ARC checklist:

1. Use `ref` only for managed objects that must stay alive.
2. Do not use `ref` on value types.
3. Do not add redundant `ref` to local method variables that are already strong for scope lifetime.
4. Use `array<ref T>`, `map<K, ref T>`, or `set<ref T>` when the container must keep contained objects alive.
5. Use weak references for parent/back references to avoid cycles.
6. Null-check weak references before use.
7. Avoid cyclic strong references; make one side weak.

Cast/null checklist:

1. Cast only when the underlying type is known.
2. Check cast result for null.
3. For `notnull` parameters, null-check before calling.
4. Treat VM exceptions from null calls as real runtime defects.
5. Do not rely on exceptions for normal flow.

Script Editor validation checklist:

1. Open Script Editor through Workbench.
2. Open the file in Text Editor.
3. Run Validate Scripts.
4. Navigate errors from the Errors panel.
5. Fix syntax and missing brace/semicolon issues first.
6. Revalidate until successful.
7. Use Output to inspect compile/runtime messages.

Script Editor debug checklist:

1. Place breakpoints on executable lines.
2. Run the target context.
3. If breakpoints are invalid, ensure code matches the running build/reloaded scripts.
4. Use Watch to inspect values.
5. Use Callstack bottom-up.
6. Use Console only in playmode or breakpoint context.
7. Stop or ignore VM exceptions deliberately; do not ignore them as validation.

JsonApiStruct checklist:

1. Define a class inheriting from `JsonApiStruct`.
2. Register variables with `RegV` using exact case.
3. Initialize nested object members if expecting nested expansion/packing.
4. Use supported types: float, int, bool, string, array, object, and array of objects.
5. Avoid multi-type arrays; Enforce Script does not support mixed-type arrays even though JSON does.
6. Handle missing variables/types as ignored/unsupported expansion cases.
7. Query exact `JsonApiStruct` methods before calling them.
8. Validate by comparing pack/expand/pack output.

## Warnings And Failure Modes

- Do not guess Reforger syntax from C#, SQF, Arma 3, Unity, or Unreal.
- Do not use `auto` for known types; it hides intent and weakens autocomplete.
- Do not use snake_case except uppercase constant naming.
- Do not use BI's `SCR_` tag for mod-owned public classes/global symbols.
- Do not use global variables unless absolutely necessary.
- Do not make variables/functions public unless they are intentionally exposed.
- Do not rely on string or int truthiness for clarity; prefer explicit checks.
- Do not expect exact float arithmetic.
- Do not compare dynamic arrays by value with `==`; that checks reference identity.
- Do not use `new Class` without parentheses.
- Do not put mixed types in Enforce arrays.
- Do not use float values as map keys.
- Do not assume enum default `0` is a valid named enum value.
- Do not assume a failed cast throws; it returns null.
- Do not pass null into `notnull` parameters.
- Do not use strong cyclic object references; ARC will not collect isolated cycles.
- Do not use `ref` on value types.
- Do not strongly reference BaseContainer in script.
- Do not edit `IEntitySource` through plain BaseContainer and expect the saved world/prefab to update; use World Editor API routes after exact lookup.
- Do not create uncontrolled `thread` usage in game scripts; wiki guidance routes game timing away from `thread`.
- Do not assume static values persist across modded scenario start/leave; script reload resets them.
- Do not write comments that just restate what the code does; comments should explain why.
- Do not treat read-only core script files as editable addon files.
- Do not ignore Script Editor validation errors or VM exceptions.
- Do not put comments or trailing commas in JSON.
- Do not assume JsonApiStruct supports mixed-type arrays or fields without matching registered variables.

## API Lookup Keys

Use these lookup keys when writing API-sensitive code:

- `Attribute`
- `BaseContainerProps`
- `BaseContainerCustomTitle`
- `NamingConvention`
- `UIWidgets`
- `ParamEnum`
- `ParamEnumArray`
- `CallbackMethod`
- `BaseContainer`
- `IEntitySource`
- `IEntityComponentSource`
- `JsonApiStruct`
- `EJsonApiError`
- `ResourceName`
- `typename`
- `Managed`
- `ScriptEditor`
- `WorkbenchPlugin`
- `SCR_AutocompletePlugin`
- `SCR_BasicCodeFormatterPlugin`
- `SCR_ClassRenamingPlugin`
- `SCR_AiScriptGeneratorPlugin`

Common method names to verify before use:

- `RegV`
- `Pack`
- `AsString`
- `ExpandFromRAW`
- `LoadFromFile`
- `SaveToFile`
- `PackToFile`
- `StoreFloat`
- `StoreInt`
- `StoreObject`
- `StartArray`
- `ItemString`
- `EndArray`
- `OnPack`
- `OnExpand`
- `OnBufferReady`
- `OnSuccess`
- `OnError`
- `Get`
- `Set`
- `AlmostEqual`
- `Repeat`

Do not copy signatures from memory. Query exact records every time API-sensitive code is written.

## Game-Data Query Commands

Use these commands from the repo root:

```powershell
py -3 scripts\query-reforger-data.py attribute Attribute --limit 10
py -3 scripts\query-reforger-data.py files BaseContainer --limit 10
py -3 scripts\query-reforger-data.py symbol JsonApiStruct --exact
py -3 scripts\query-reforger-data.py files ScriptEditor --limit 10
```

For config decorators:

```powershell
py -3 scripts\query-reforger-data.py symbol Attribute --exact
py -3 scripts\query-reforger-data.py method Attribute Attribute --exact
py -3 scripts\query-reforger-data.py symbol BaseContainerProps --exact
py -3 scripts\query-reforger-data.py files UIWidgets --limit 10
py -3 scripts\query-reforger-data.py files ParamEnum --limit 10
```

For JsonApiStruct:

```powershell
py -3 scripts\query-reforger-data.py symbol JsonApiStruct --exact
py -3 scripts\query-reforger-data.py method JsonApiStruct RegV --exact
py -3 scripts\query-reforger-data.py method JsonApiStruct Pack --exact
py -3 scripts\query-reforger-data.py method JsonApiStruct ExpandFromRAW --exact
py -3 scripts\query-reforger-data.py method JsonApiStruct AsString --exact
py -3 scripts\query-reforger-data.py files EJsonApiError --limit 10
```

For Script Editor and plugins:

```powershell
py -3 scripts\query-reforger-data.py files ScriptEditor --limit 20
py -3 scripts\query-reforger-data.py symbol ScriptEditor --exact
py -3 scripts\query-reforger-data.py files SCR_AutocompletePlugin --limit 10
py -3 scripts\query-reforger-data.py files SCR_BasicCodeFormatterPlugin --limit 10
py -3 scripts\query-reforger-data.py files SCR_ClassRenamingPlugin --limit 10
```

For language primitives and utility APIs:

```powershell
py -3 scripts\query-reforger-data.py symbol typename --exact
py -3 scripts\query-reforger-data.py files Math --limit 10
py -3 scripts\query-reforger-data.py files Managed --limit 10
```

For source snippets after exact query output:

```powershell
py -3 scripts\query-reforger-data.py snippet <scripts/...file.c> --line <line> --context 30
```

Do not load broad schema/API dumps for this topic. Query exact symbols, methods, files, examples, or bounded snippets.

## Examples And Samples

Official sample reviewed:

- `SampleMod_ModdedScript`: confirms a standalone addon project can contain a project descriptor plus a script tree for modded script examples. It routes to the gameplay/script-pattern reference for implementation patterns.

Use the sample as a layout signal only:

- project descriptor: has `ID`, `GUID`, `TITLE`, dependencies, and platform configurations;
- script files live under a game script tree;
- read the sample only after this reference and exact API query output establish the language/API rules.

Useful game-data routes:

```powershell
py -3 scripts\query-reforger-data.py files ScriptEditor --limit 20
py -3 scripts\query-reforger-data.py files JsonApiStruct --limit 20
py -3 scripts\query-reforger-data.py examples component --subtopic script-component --limit 10
```

Do not paste sample source into new code without verifying exact current API signatures and ownership references.

## Follow-Up Keywords

Use these search/query terms when this reference is not enough:

- `Enforce Script`
- `strong typing`
- `identifier`
- `camelCase`
- `PascalCase`
- `Allman`
- `creator tag`
- `modded`
- `vanilla`
- `super`
- `this`
- `ref`
- `ARC`
- `strong reference`
- `weak reference`
- `cyclic reference`
- `notnull`
- `out`
- `inout`
- `thread`
- `delete`
- `typename`
- `BaseContainerProps`
- `Attribute`
- `UIWidgets`
- `ParamEnum`
- `JsonApiStruct`
- `RegV`
- `EJsonApiError`
- `Script Editor`
- `Validate Scripts`
- `Find Symbol`
- `Goto Declaration`
- `Callstack`
- `Watch`
- `Virtual Machine Exception`
- `Autocomplete Plugin`
- `Basic Code Formatter Plugin`
- `Class Renaming Plugin`
- `Doxygen Filler Plugin`

## Verification

Before finalizing script code:

- Confirm the task's owning reference was read.
- Confirm every uncertain class, method, attribute, enum, and callback signature was queried.
- Confirm explicit types are used where known.
- Confirm variables follow identifier/naming conventions.
- Confirm member/static/global variables use correct prefixes or avoid globals.
- Confirm constructors use parentheses.
- Confirm object casts are null-checked.
- Confirm `notnull` callers null-check before calling.
- Confirm ARC ownership is deliberate and cyclic strong references are avoided.
- Confirm JSON is valid: double quotes, no comments, no trailing commas, valid arrays/objects.
- Confirm JsonApiStruct registered variable names match exact case.
- Confirm config decorators are queried before use.
- Confirm Script Editor validation succeeds or remaining errors are reported.
- Confirm runtime behavior is tested in Workbench/game/server as relevant.
- Confirm debugging findings distinguish compile errors, VM exceptions, and gameplay logic defects.

Residual uncertainty to state in final answers:

- If code was not validated in Workbench/Script Editor, state that syntax/API lookup was performed but Workbench validation remains.
- If code depends on runtime entity/component/prefab/server behavior, state that language correctness is not full runtime verification.
- If Script Editor plugin or config behavior is involved, state the exact query commands used for API verification.

## Official Wiki Links

- Enforce Script Syntax: https://community.bistudio.com/wiki/Arma_Reforger:Enforce_Script_Syntax
- From SQF to Enforce Script: https://community.bistudio.com/wiki/Arma_Reforger:From_SQF_to_Enforce_Script
- Scripting: Values: https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Values
- Scripting: Operators: https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Operators
- Scripting: Keywords: https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Keywords
- Scripting: Conventions: https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Conventions
- Scripting: Best Practices: https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Best_Practices
- Scripting: Automatic Reference Counting: https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Automatic_Reference_Counting
- Scripting: JSON: https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_JSON
- JsonApiStruct Usage: https://community.bistudio.com/wiki/Arma_Reforger:JsonApiStruct_Usage
- Scripting: Config Object: https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Config_Object
- BaseContainer Usage: https://community.bistudio.com/wiki/Arma_Reforger:BaseContainer_Usage
- Script Editor: https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor
- Script Editor Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor_Plugin
- Script Editor: Autocomplete Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor:_Autocomplete_Plugin
- Script Editor: Basic Code Formatter Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor:_Basic_Code_Formatter_Plugin
- Script Editor: Class Renaming Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor:_Class_Renaming_Plugin
- Script Editor: Create New Script Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor:_Create_New_Script_Plugin
- Script Editor: Doxygen Filler Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor:_Doxygen_Filler_Plugin
- Script Editor: Fill From Template Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor:_Fill_From_Template_Plugin
- Script Editor: SVN Plugins: https://community.bistudio.com/wiki/Arma_Reforger:Script_Editor:_SVN_Plugins

## Usefulness Score

Score: 92/100

- Wiki coverage: 28/30. All primary language/editor pages were reviewed and represented. Config Object and BaseContainer are intentionally partial because full config/resource ownership belongs elsewhere. Official links and coverage gaps are listed.
- Operational detail: 14/15. The reference preserves concrete language rules, editor surfaces, validation/debug procedures, JSON/config decorator details, and common failure modes.
- API lookup usefulness: 14/15. Attribute, BaseContainer, JsonApiStruct, ScriptEditor, and plugin query routes are provided. Exact signatures remain query-owned.
- Example grounding: 8/10. `SampleMod_ModdedScript` and query-surfaced Script Editor plugin files are included as routing/example signals without copying source bodies.
- Codex task usefulness: 14/15. Codex can write syntax-correct, convention-aware, query-backed script and know when to route to gameplay/component/config owners.
- Context efficiency: 9/10. The reference is dense and scoped to language/editor behavior, with cross-links instead of duplicating gameplay/config/plugin ownership.
- Verification guidance: 5/5. Includes Script Editor validation, runtime/debugging caveats, API lookup, ARC, JSON, and Workbench verification guidance.

Category-fit check:

- Source family complete: pass. Language syntax, values, operators, keywords, conventions, best practices, ARC, JSON, JsonApiStruct, and Script Editor sources are represented.
- No owned page missing: pass. Every owned primary page is listed in Source Inventory.
- Split boundary justified: pass. Gameplay scripting, entity/component lifecycle, config/resource authoring, and Workbench plugin authoring are explicitly routed elsewhere.
- Cross-links present: pass. Nearby workflow owners are named in When To Read and Source Inventory.
- Task route clear: pass. Codex should read this for language/editor rules, then query exact APIs and move to the narrow workflow reference for implementation behavior.

Missed coverage/cap review:

- No owned primary wiki page was skipped.
- No detailed language/editor workflow was reduced to a shallow one-line summary.
- Tables, procedures, warnings, decorator fields, JSON rules, and Script Editor workflows are represented.
- Local raw paths, raw wiki dumps, broad API dumps, and live scraping instructions are not included.
- No automatic failure condition applies.
