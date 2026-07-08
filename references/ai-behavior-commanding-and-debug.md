# AI Behavior, Commanding, And Debug

## When To Read

Read this when the task involves AI behavior trees, Behavior Editor nodes, scripted AI tasks/decorators, AI debug panels, AI group/character debugging, command-menu actions that drive AI behavior, or source lookup for AI implementation examples.

Do not use this as the owner for navmesh creation, command-menu layout resources, generic component lifecycle, or Game Master task/faction setup. For those, read the owning reference first and return here only for AI behavior/debug specifics:

- Navmesh and World Editor tools: `references/world-editor-tools-generators-and-navmesh.md`
- Commanding menu UI/layout ownership: `references/ui-layouts-dialogs-and-menus.md`
- Script implementation patterns: `references/script-events-actions-and-patterns.md`
- Entity/component lifecycle: `references/entities-components-and-lifecycle.md`
- Game Master, factions, tasks, and game modes: `references/game-master-factions-tasks-and-modes.md`

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: AI behavior authoring, Behavior Editor, Behavior Editor node reference, AI Debug Panel.
- Secondary/cross-reference topics: Commanding Menu Modding where the workflow creates AI commands; Diag Menu, Script Editor, Startup Parameters, Game Master, and navmesh pages as validation or setup routes only.

Wiki pages reviewed:
- Behavior Editor - https://community.bistudio.com/wiki/Arma_Reforger:Behavior_Editor - status: covered - reason: primary workflow source for behavior tree editor concepts, flow, scripted tasks/decorators, in-game setup, and example behavior construction.
- Behavior Editor: Nodes - https://community.bistudio.com/wiki/Arma_Reforger:Behavior_Editor:_Nodes - status: covered - reason: primary source for node families, parameters, return values, and node caveats.
- AI Debug Panel Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:AI_Debug_Panel_Tutorial - status: covered - reason: primary workflow source for live AI inspection and debug panel extension.
- Commanding Menu Modding - https://community.bistudio.com/wiki/Arma_Reforger:Commanding_Menu_Modding - status: partial - reason: this reference owns AI command behavior and command execution caveats; UI/layout presentation remains owned by `ui-layouts-dialogs-and-menus.md`.

Wiki sections covered:
- Behavior Editor: Editor Basics, Shortcuts, Controls, Behavior Tree, Flow Control, Node Events, Decorators, Tasks, Behavior Tree Flow, Returning Values, Force Node Result, Abort Type, In-Game Setup, Simple Action, Follow Player, Guard Player, Guard Player and Shoot Enemies, Scripted Decorator, Further Reading.
- Behavior Editor: Nodes: Page, Flow, Decorators, Scripted Decorators, Tasks, Utility Tasks, Scripted Tasks, Character Tasks, Waypoints, Group, Perception, Action Tasks, Smart Actions, Experimental / Work in Progress.
- AI Debug Panel Tutorial: Page, Usage, Debug Panel, Available Data, Dump Debug Msgs, Breakpoint, Locate, Add Debug Panel Information.
- Commanding Menu Modding: Class Creation, Execute, CanBeShown, CanBePerformed, Example, Command Declaration, Command Menu Declaration.

Structured wiki records:
- Tables reviewed/included: AI Debug Panel available data; Behavior Editor panel map, shortcuts, controls; Behavior Editor Nodes tables for flow, decorators, scripted decorators, tasks, utility tasks, scripted tasks, character tasks, waypoints, group, perception, action tasks, smart actions, and experimental nodes.
- Procedures reviewed/included: behavior flow-control usage, node events, return-value behavior, in-game setup, Follow Player, Guard Player, Guard Player and Shoot Enemies, command class creation, command declaration, and command menu declaration.
- Admonitions reviewed/included: running-task requirements, debug tree save warning, scripted-node performance warning, decorator/abort behavior, experimental-node warning, debug panel shared class warning, and command execution broadcast warning.
- Code blocks reviewed/included: AI Debug startup define route and wiki code examples; no source bodies are copied here.
- Media reviewed: Behavior Editor interface image and Commanding Menu page media; images are used only as evidence that the editor has named panels.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts\query-reforger-data.py files AI --limit 8`
  - `py -3 scripts\query-reforger-data.py examples ai --limit 8`
  - `py -3 scripts\query-reforger-data.py files Behavior --limit 8`
  - `py -3 scripts\query-reforger-data.py files AITask --limit 8`
  - `py -3 scripts\query-reforger-data.py files AIWaypoint --limit 8`
  - `py -3 scripts\query-reforger-data.py files SCR_AI --limit 8`
  - `py -3 scripts\query-reforger-data.py symbol AITaskScripted --exact --limit 8`
  - `py -3 scripts\query-reforger-data.py symbol DecoratorScripted --exact --limit 8`
  - `py -3 scripts\query-reforger-data.py symbol ENodeResult --exact --limit 8`
  - `py -3 scripts\query-reforger-data.py files SCR_BaseGroupCommand --limit 8`
  - `py -3 scripts\query-reforger-data.py files SCR_AIAgentDebugPanel --limit 8`
  - `py -3 scripts\query-reforger-data.py files AIControlComponent --limit 8`
- Symbols/methods/attributes verified: `AITaskScripted`, `DecoratorScripted`, `ENodeResult`, `SCR_BaseGroupCommand`, `SCR_AIAgentDebugPanel`, `AIControlComponent`, `AIAgent`, `BehaviorTree`, `BehaviorTreeSystem`, `BehaviorEditor`, `SCR_AIWaypoint`.
- Examples/snippets reviewed: handwritten AI behavior files under source search results, AI scripted-node examples, command files derived from `SCR_BaseGroupCommand`, AI debug panel files, and generated AI signature files.

Samples and source examples:
- Official sample folders reviewed: `SampleMod_Main` and `SampleMod_NewFaction` as layout signals for terrain/navmesh/faction/gameplay context that can affect AI testing.
- Game-source example families reviewed: AI behavior activity features, scripted AI inventory/weapon/vehicle nodes, AI waypoints, tutorial commanding stages, Scenario Framework AI slot/waypoint files, and command-menu implementations.

Coverage gaps:
- Missing, excluded, or intentionally deferred source: full navmesh tool workflows are deferred to `references/world-editor-tools-generators-and-navmesh.md`; command-menu visual/resource layout is deferred to `references/ui-layouts-dialogs-and-menus.md`; generic component and prefab lifecycle rules are deferred to their owning references.
- Reason and impact: AI behavior authoring often depends on navigation data, components, and UI commands, but duplicating those full workflows here would blur ownership. This reference gives the required cross-links and AI-specific checks.

## Wiki Source Coverage

The wiki coverage is centered on two dense authoring surfaces and one validation surface:

- Behavior Editor explains the authoring model: behavior trees are not single-state FSMs. Multiple branches can run, nodes return `Success`, `Failure`, or `Running`, and parent nodes react to those return values.
- Behavior Editor: Nodes supplies the node catalog: flow nodes, decorators, tasks, utility tasks, scripted tasks, character tasks, waypoint tasks, group tasks, perception, action tasks, smart actions, and experimental/WIP nodes.
- AI Debug Panel Tutorial supplies live inspection: enable the startup define, select an AI character or group, open the Diag Menu AI script panel, and inspect the agent/group state.
- Commanding Menu Modding supplies the command class/config path when player commands are used to drive AI behavior.

The AI reference preserves the wiki's operational details rather than treating AI as just script classes. Behavior tree correctness depends on graph flow, editor setup, AI components, behavior data assignment, runtime debug state, and source lookup for exact API.

## Terms And Concepts

- Behavior Tree: graph-driven AI behavior asset executed from a Root node through flow control and decorators.
- Root: the entry point node. It starts the tree and cannot be inserted from the node palette like ordinary nodes.
- Selector: evaluates child branches until one returns success; useful for OR-style logic.
- Sequence: evaluates children from left to right while they succeed; useful for AND-style ordered behavior.
- Parallel: executes children simultaneously, with optional child-result selection controlling its own return.
- Repeater: repeats its child sequence multiple times.
- Run BT: launches another behavior tree, keeping large behavior graphs modular.
- Node: one step in the behavior tree.
- Decorator: conditional gate or flow modifier that can test state, invert results, force results, use child results, or abort branches depending on configuration.
- Task: leaf operation that performs behavior such as movement, stance, firing, waiting, finding entities, assigning variables, or requesting actions.
- Immediate task: completes during one evaluation and allows the tree to continue.
- Running task: spans time and returns `Running`; it blocks further non-parallel flow until it succeeds or fails.
- Scripted task: task implemented in script; useful for custom behavior, but slower than native behavior tree logic according to the wiki.
- Scripted decorator: script-backed decorator for custom conditions.
- AI Agent: controller-side entity that orders actions to the controlled character.
- Controlled entity: usually the character entity controlled by the AI Agent. Several node outputs distinguish agent vs controlled entity.
- AI Debug Panel: live panel tied to one AI group or character.
- Commanding command: class/config-driven action shown in the commanding menu, optionally used for AI orders.

## Workbench / Resource / Data Surfaces

Behavior Editor surfaces:
- Node area: the main graph canvas.
- Nodes palette: source for adding graph nodes.
- Node parameters: selected-node configuration.
- Variables: graph-level variables and typed values.
- Debug panel: runtime/debug state in the editor.
- Console: editor feedback and diagnostic output.

Behavior Editor controls:
- Create or delete breakpoint: `F9`.
- Open: `Ctrl+O`.
- Save: `Ctrl+S`.
- Save As: `Ctrl+Shift+S`.
- Copy/cut/paste: `Ctrl+C`, `Ctrl+X`, `Ctrl+V`.
- Delete selected node, variable, or connection: `Del`.
- Move canvas: hold left mouse button in empty space.
- Connect nodes: drag from the black bar of one node to the black bar of another.
- Connect variables: connect through variable pins.
- Select multiple nodes: `Shift` drag or `Ctrl` click.
- Zoom: mouse wheel.
- Open scripted node script: double-click a scripted node.

AI runtime setup surfaces:
- Character prefab must have the AI component set required by the behavior: at minimum AI control, aiming, movement, and perception components for the wiki's basic AI character setup.
- The wiki points to `ChimeraCharacterAI` as a working AI character prefab baseline.
- `AIControlComponent` creates the AI Agent and exposes behavior data setup.
- `OverrideAIBehaviorData` is the behavior-tree assignment surface mentioned by the wiki.
- `Enable AI` activates the AI Agent.

AI Debug Panel surfaces:
- Startup define: use `-scrDefine AI_DEBUG` when the AI debug panel workflow is needed.
- Selection surface: select a Character or Group through Game Master.
- Diag route: Diag Menu > AI > AI Script > Open Debug Panel.
- Panel scope: one debug panel is assigned to one AI group or character.

Commanding surfaces:
- Command class inheritance route: command classes inherit from `SCR_BaseGroupCommand`; verify exact class and methods with query output before editing.
- Command config route: `Commands.conf` declares command classes and properties such as string ID and leader-only behavior.
- Menu config route: `CommandingMenu.conf` and `CommandingMapMenu.conf` decide where declared commands appear.

## Required Workflows

Build or modify an AI behavior tree:
1. Start from the Behavior Editor source material and identify whether the task is pure graph logic, scripted task/decorator logic, command-menu triggered logic, or navigation-dependent behavior.
2. Build flow from Root through Sequence, Selector, Parallel, Repeater, or Run BT rather than forcing large behaviors into one branch.
3. Use decorators for conditions and interruption rules. Decide whether `AbortType` is needed before relying on a decorator changing later.
4. Store values in variables when a node output cannot be connected directly to the next node input.
5. Keep Running tasks isolated or parallelized enough that they do not block unrelated behavior.
6. Use native behavior nodes where possible. Add scripted tasks/decorators only when the behavior cannot be represented in the editor.
7. Validate in-game with a properly configured AI character and open Behavior Editor runtime view.
8. If the behavior depends on navigation, validate navmesh and world setup through `references/world-editor-tools-generators-and-navmesh.md`.

Set up an AI character for behavior-tree testing:
1. Use or create a character prefab that has AI Control, AI Character Aiming, AI Character Movement, and Perception components appropriate for the behavior.
2. In the AI control component, assign the behavior tree in `OverrideAIBehaviorData`.
3. Enable AI so the AI Agent is active.
4. Run the game with Behavior Editor open.
5. In the right-panel list of running behavior trees, select the soldier/agent behavior tree and inspect the current tree state.
6. Do not edit the runtime debug tree expecting persistence; edit the original behavior tree source instead.

Create a simple action behavior:
1. Attach a Task directly under Root for the simplest behavior.
2. Use this only for trivial validation. For real behavior, wrap tasks in flow control and decorators so failure, running state, and repeated evaluation are clear.

Create a follow-player behavior:
1. Get the controlled/follow target entity.
2. Create a graph variable from the Variables panel.
3. Choose the correct type, commonly `GenericEntity` or `IEntity` depending on the node contract; verify exact type with query output.
4. Drag the variable into the graph.
5. Store the entity output into the variable, then read from the variable for movement.
6. Tune movement parameters such as obstacle avoidance and precision in node parameters.
7. Avoid recalculating and overwriting the target every tick when a decorator can test validity and skip that branch.

Create a guard-player behavior:
1. Assign the player variable on first run.
2. On subsequent runs, test variable validity and distance.
3. If the target is outside the threshold, stand up, lower weapon if needed, and move to the target with a tolerance.
4. Remember that movement as a Running task prevents later non-parallel checks until movement finishes.
5. When close enough, run the guard branch: crouch, raise weapon, create a randomized look position, orient, idle briefly, and repeat.
6. Add enemy engagement as a higher-priority or separate branch if needed; do not bolt it on without planning how Running state and aborts interact.

Add enemy engagement through scripted behavior:
1. Prefer existing native perception/target nodes when possible.
2. If custom target selection is required, implement a scripted task or decorator and verify the base class with:
   - `py -3 scripts\query-reforger-data.py symbol AITaskScripted --exact --limit 8`
   - `py -3 scripts\query-reforger-data.py symbol DecoratorScripted --exact --limit 8`
3. Return the correct node result values and verify `ENodeResult` before writing code.
4. Expose behavior parameters with attributes only after verifying the exact attribute syntax in the API lookup reference and query output.
5. Treat wiki code examples as concept examples; verify exact current signatures before implementation.

Debug AI live:
1. Launch with `-scrDefine AI_DEBUG`.
2. Select a character or group through Game Master.
3. Open Diag Menu > AI > AI Script > Open Debug Panel.
4. Check group/character call sign, current action, and available actions/priority.
5. For characters, also inspect threat level, unit roles, and unit states.
6. Use Dump Debug Msgs to capture recent AI events, optionally with a time interval.
7. Use Breakpoint to make Script Editor stop on the AI's next update.
8. Use Locate for selected characters when the entity is hard to find in-world.
9. To add new panel data, route to `SCR_AIAgentDebugPanel` through query output before editing; the same class is used for groups and characters.

Create an AI-related command-menu action:
1. Verify command ownership. If the task is only UI layout/menu placement, use `references/ui-layouts-dialogs-and-menus.md`; if it changes AI order behavior, continue here.
2. Create a class derived from `SCR_BaseGroupCommand`; verify the current class file and methods with query output.
3. Override behavior methods for execution and visibility:
   - `Execute` determines what the command does.
   - `CanBeShown` determines whether it appears.
   - `CanBePerformed` determines whether it can execute.
4. Treat `Execute` as network-sensitive. The wiki says it is broadcast to everyone, so add server/client checks appropriate to the action.
5. Declare the command in command config.
6. Add it to command menu and/or map command menu config.
7. Validate as leader/non-leader, in valid/invalid target context, and in multiplayer if the command has gameplay effect.

## Configuration Fields And Tables

Behavior Editor panel map:
- Node area: graph work surface.
- Nodes palette: node creation.
- Node parameters: selected node settings.
- Variables: typed graph variables.
- Debug: runtime behavior inspection.
- Console: editor output.

Behavior node return meanings:
- `Success`: requested test/action passed.
- `Failure`: condition did not match; this is not automatically an error.
- `Running`: action is ongoing and propagates upward until the whole tree is considered running unless parallel flow changes this.

Flow node table, preserved as operating guidance:
- Root: start of tree; cannot be removed or inserted from palette.
- Selector: executes children until one succeeds; returns running if a child runs, success if one succeeds, failure if all fail.
- Sequence: executes children left to right while each succeeds; fails if any child fails; runs while a child runs.
- Parallel: executes children regardless of their return; can use a selected child result.
- Repeater: repeats a child sequence.
- Run BT: executes another behavior tree.

Decorator table, preserved as operating guidance:
- Decorator tests a condition and may execute a child.
- Common parameters include negative result, use child result, always true, and abort type.
- Abort types include none, abort children branch, abort parent node with children, and abort parent node further children.
- If no abort type is set, the decorator evaluation is only tested once per tree execution according to the wiki.

Task families from Behavior Editor: Nodes:
- General tasks: Get Controlled Entity, Create Position, Follow Path, movement/position/action primitives.
- Utility tasks: Set/Clear Variable, Find Entity.
- Scripted tasks: custom behavior such as finding a target in radius.
- Character tasks: Fire, Change Stance, Throw Grenade, Character Raise Weapon, Character Set Movement Speed, and related character-only operations.
- Waypoints: Get Waypoint, with waypoint behavior/contact/danger outputs.
- Group: Get Group children and Create Group; note the wiki flags group iteration behavior as possibly changing.
- Perception: Pick Target.
- Action tasks: Request Action by action name/value.
- Smart actions: Perform, Find, Get Current, Get Position, and Get behavior tree for smart actions.
- Experimental / Work in Progress: Flocking, Get Random Point, Scripted Target; avoid depending on these without extra verification.

AI Debug Panel available data:
- Groups and characters: call sign, current action, available actions and their priority.
- Characters only: threat level, unit roles, unit states.

Commanding config surfaces:
- `Commands.conf`: declares command class and command properties.
- `CommandingMenu.conf`: declares regular command menu entries.
- `CommandingMapMenu.conf`: declares map command menu entries.
- Command class should be generic and configurable when the same class is reused for multiple command declarations.

## Procedures And Ordered Steps

Behavior Editor workflow:
1. Create the graph around clear return states: success, failure, and running.
2. Use Sequence for ordered requirements and Selector for fallback choices.
3. Put long-running actions behind Running-aware flow. Add Parallel only when independent behavior must continue during long-running work.
4. Use decorators for validity checks, distance checks, target checks, and branch interruption.
5. Set Abort Type only when the decorator must interrupt running children or siblings.
6. Use variables for entity/position values that cannot be connected directly between nodes.
7. Prefer native node combinations over script when possible.
8. Save the source behavior tree and validate the running instance separately.

Scripted task procedure:
1. Search exact base class:
   - `py -3 scripts\query-reforger-data.py symbol AITaskScripted --exact --limit 8`
2. Search existing scripted AI nodes:
   - `py -3 scripts\query-reforger-data.py files AITask --limit 8`
   - `py -3 scripts\query-reforger-data.py files SCR_AI --limit 8`
3. Open a bounded snippet of the closest handwritten example rather than copying a broad file.
4. Implement only the missing behavior, return verified node results, and expose only necessary parameters.
5. Re-test in Behavior Editor and runtime.

Scripted decorator procedure:
1. Search exact base class:
   - `py -3 scripts\query-reforger-data.py symbol DecoratorScripted --exact --limit 8`
2. Search the exact result enum:
   - `py -3 scripts\query-reforger-data.py symbol ENodeResult --exact --limit 8`
3. Keep the decorator focused on condition evaluation, not long-running action.
4. Verify abort behavior in the graph, not just in script.

Debug panel procedure:
1. Enable the AI debug define on launch.
2. Select the target group or character.
3. Open the AI script debug panel through Diag Menu.
4. Inspect actions, priority, threat, roles, states, and recent messages.
5. Use breakpoint only when Script Editor is ready for the next AI update.
6. Search `SCR_AIAgentDebugPanel` before adding fields or buttons.

Commanding AI procedure:
1. Search the command base:
   - `py -3 scripts\query-reforger-data.py files SCR_BaseGroupCommand --limit 8`
2. Search existing command examples:
   - `py -3 scripts\query-reforger-data.py files AIWaypoint --limit 8`
   - `py -3 scripts\query-reforger-data.py files SCR_AI --limit 8`
3. Implement command visibility separately from command performability.
4. Keep server-only gameplay changes guarded in `Execute`.
5. Register the command and menu entries.
6. Validate local, client, server, leader, non-leader, valid-target, invalid-target, and map-menu contexts as applicable.

## Warnings And Failure Modes

- Do not guess AI APIs. Behavior Editor wiki examples are concept guides; exact base classes, methods, return types, and files must be verified with `scripts/query-reforger-data.py`.
- Runtime debug behavior tree edits are not saved to the source behavior tree. Modify the original behavior tree asset.
- Running tasks block downstream non-parallel behavior until they return success or failure.
- A task that can return running must override the correct running-capability method; verify exact method names before writing code.
- A decorator with no abort type is evaluated only once per tree execution according to the wiki. Do not expect it to interrupt running behavior unless abort behavior is configured.
- `Failure` in a behavior tree is often a normal false result, not an exception or broken state.
- Scripted behavior tree nodes are powerful but slower; the wiki notes that native behavior trees without scripted nodes can run faster through parallelization, while scripted nodes run in a single thread.
- `Get Controlled Entity` output may need to be stored in a variable before another node can consume it.
- Group iteration behavior in the wiki is marked as subject to change. Verify current source before relying on it.
- Experimental/WIP nodes are not stable enough to depend on without current validation.
- AI debug panel extensions must account for the same panel class being used by both groups and characters.
- Commanding-menu `Execute` is broadcast to server and clients per the wiki. Guard server-only logic and UI-only logic explicitly.
- AI behavior that depends on movement must validate navmesh and world setup; a correct tree can still fail if navigation data is absent or invalid.
- Dedicated server and multiplayer behavior must be tested separately when commands, AI orders, or replicated state are involved.

## API Lookup Keys

Use these lookup keys before writing API-sensitive code:

- Behavior tree and AI bases: `BehaviorTree`, `BehaviorTreeSystem`, `AITask`, `AITaskScripted`, `Decorator`, `DecoratorScripted`, `ENodeResult`, `Node`.
- AI setup and runtime: `AIControlComponent`, `ChimeraAIControlComponent`, `AIAgent`, `ChimeraCharacterAI`, `AIComponentEntity`.
- AI source examples: `SCR_AI`, `SCR_AIActivity`, `SCR_AIFireteams`, `SCR_AIWaypoint`, `SCR_AIAgentDebugPanel`, `SCR_AIDebugVisualization`.
- Commanding: `SCR_BaseGroupCommand`, `SCR_WaypointGroupCommand`, `SCR_PlayerCommandsConfig`, `Commands.conf`, `CommandingMenu.conf`, `CommandingMapMenu.conf`.
- Cross-topic checks: `IEntity`, `GenericEntity`, `ResourceName`, `FindComponent`, `RplComponent` only when AI code crosses entity/resource/replication ownership.

## Game-Data Query Commands

Primary AI source routes:

```powershell
py -3 scripts\query-reforger-data.py files AI --limit 8
py -3 scripts\query-reforger-data.py files Behavior --limit 8
py -3 scripts\query-reforger-data.py files AITask --limit 8
py -3 scripts\query-reforger-data.py files AIWaypoint --limit 8
py -3 scripts\query-reforger-data.py files SCR_AI --limit 8
```

Exact AI API anchors:

```powershell
py -3 scripts\query-reforger-data.py symbol AITaskScripted --exact --limit 8
py -3 scripts\query-reforger-data.py symbol DecoratorScripted --exact --limit 8
py -3 scripts\query-reforger-data.py symbol ENodeResult --exact --limit 8
py -3 scripts\query-reforger-data.py files AIControlComponent --limit 8
```

Debug and commanding routes:

```powershell
py -3 scripts\query-reforger-data.py files SCR_AIAgentDebugPanel --limit 8
py -3 scripts\query-reforger-data.py files SCR_BaseGroupCommand --limit 8
py -3 scripts\query-reforger-data.py files Commanding --limit 8
```

Examples and snippets:

```powershell
py -3 scripts\query-reforger-data.py examples ai --limit 8
py -3 scripts\query-reforger-data.py snippet scripts/Game/AI/SCR_AIAgentDebugPanel.c --line 1 --context 40
py -3 scripts\query-reforger-data.py snippet scripts/Game/Commanding/Commands/SCR_BaseGroupCommand.c --line 1 --context 40
py -3 scripts\query-reforger-data.py snippet scripts/Game/AI/Group/SCR_AIWaypoint.c --line 1 --context 40
```

Search quality note: `examples ai` may return AI-adjacent resource, inventory, UI, and vehicle examples because many AI scripted nodes interact with those systems. For exact AI behavior authoring, prefer targeted file searches and bounded snippets.

## Examples And Samples

Useful game-source example routes:
- Behavior tree/API truth: generated `BehaviorTree`, `BehaviorTreeSystem`, `AITask`, `AITaskScripted`, `DecoratorScripted`, and `ENodeResult` files surfaced by exact query commands.
- Handwritten AI behavior patterns: `SCR_AIActivityFeatureBase`, `SCR_AIActivitySmokeCoverFeature`, fireteam/cluster activity files, and scripted AI node families found through `files SCR_AI`.
- AI inventory/resource/vehicle examples: scripted nodes under AI search results are useful when the behavior interacts with inventory, magazines, weapons, resource loading, or compartments, but the domain-specific reference still owns those systems.
- AI waypoint pattern: `SCR_AIWaypoint` and tutorial commanding stage files found by `files AIWaypoint`.
- AI debug implementation: `SCR_AIAgentDebugPanel` and `SCR_AIDebugVisualization`.
- Commanding pattern: `SCR_BaseGroupCommand`, derived command classes, and player commanding config files found by `files SCR_BaseGroupCommand`.

Official sample signals:
- `SampleMod_Main`: useful for world/navmesh/layout context when AI behavior must be tested in a world.
- `SampleMod_NewFaction`: useful as a faction/gameplay context signal when AI work is tied to faction or group availability.
- Samples are example/layout signals only. They do not replace wiki workflow rules or exact query output.

## Follow-Up Keywords

- Behavior Editor
- behavior tree
- BehaviorTree
- AITask
- AITaskScripted
- DecoratorScripted
- ENodeResult
- AbortType
- Running
- Selector
- Sequence
- Parallel
- AIControlComponent
- AIAgent
- OverrideAIBehaviorData
- Enable AI
- AI_DEBUG
- SCR_AIAgentDebugPanel
- SCR_AIDebugVisualization
- SCR_AIWaypoint
- SCR_BaseGroupCommand
- CommandingMenu
- Commands.conf
- navmesh
- Diag Menu
- Game Master AI selection

## Verification

Before finalizing an AI behavior or command change:

1. Re-read this reference and the owning cross-reference for any non-AI surface touched.
2. Run exact query commands for every AI base class, result enum, command class, component, and method used.
3. Use generated files for signatures and handwritten files for implementation patterns.
4. Validate Behavior Editor graph flow: root, branch order, return states, variables, decorators, abort type, running tasks, and script node boundaries.
5. Validate in a world with the necessary AI components and behavior data assigned.
6. If movement is involved, validate navmesh/world setup through the world-editor/navmesh reference.
7. If command-menu behavior is involved, validate command visibility, performability, config registration, menu placement, and server/client execution.
8. If debugging is involved, launch with AI debug enabled and inspect the live AI group/character panel.
9. If multiplayer or server-side behavior is involved, perform dedicated server or multiplayer runtime validation and state remaining uncertainty.

## Official Wiki Links

- Behavior Editor: https://community.bistudio.com/wiki/Arma_Reforger:Behavior_Editor
- Behavior Editor: Nodes: https://community.bistudio.com/wiki/Arma_Reforger:Behavior_Editor:_Nodes
- AI Debug Panel Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:AI_Debug_Panel_Tutorial
- Commanding Menu Modding: https://community.bistudio.com/wiki/Arma_Reforger:Commanding_Menu_Modding
- Diag Menu: https://community.bistudio.com/wiki/Arma_Reforger:Diag_Menu
- Startup Parameters: https://community.bistudio.com/wiki/Arma_Reforger:Startup_Parameters
- Game Master: https://community.bistudio.com/wiki/Arma_Reforger:Game_Master
- Multiplayer Scripting: https://community.bistudio.com/wiki/Arma_Reforger:Multiplayer_Scripting

## Usefulness Score

Score: 94/100

- Wiki coverage: 29/30. All owned primary pages were reviewed and represented. Tables, procedures, warnings, and official links are included. One point is reserved because Commanding Menu Modding is intentionally partial ownership, with UI/menu-layout details routed to the UI reference.
- Operational detail: 14/15. Behavior Editor panels, shortcuts, controls, node families, in-game setup, AI debug flow, and command setup are preserved. The reference avoids full code bodies, so exact implementation must still use query snippets.
- API lookup usefulness: 15/15. AI bases, result enums, debug classes, AI control components, and command classes are routed to exact query commands.
- Example grounding: 9/10. Game-source routes and official sample signals are included. The current `examples ai` route is noisy, so targeted file/snippet commands are emphasized.
- Codex task usefulness: 14/15. Codex can route common AI tasks from behavior authoring to API lookup and verification. One point is reserved because AI tasks often cross navmesh, faction, UI, or multiplayer ownership.
- Context efficiency: 9/10. The reference is dense and routes exact APIs to tools without broad dumps. Some node-family lists are necessarily long because the wiki tables are central source material.
- Verification guidance: 4/5. Workbench, runtime, AI debug, navmesh, command-menu, and multiplayer checks are listed. Exact project-specific test commands remain dependent on the mod being edited.

Category-fit check:
- Source family complete: pass. Behavior Editor, Behavior Editor Nodes, AI Debug Panel, and AI-specific Commanding Menu content are represented.
- No owned page missing: pass.
- Split boundary justified: pass. Navmesh, UI layout, scripting, lifecycle, and Game Master ownership are explicitly cross-linked.
- Cross-links present: pass.
- Task route clear: pass. AI behavior, scripted task/decorator, debug panel, and commanding workflows each route to one primary reference plus query commands.

Missed coverage and cap review:
- No owned primary wiki page was skipped.
- No relevant primary section was intentionally omitted.
- Tables, procedures, warnings, and command/config surfaces are represented.
- No automatic failure condition applies.
