# Animation Graphs Weapon Animation And Export

## When To Read

Read this when the task is about animation authoring or animation-driven runtime behavior:

- using Animation Editor panels, preview, workspace, anim sets, animation graphs, variables, commands, IK chains, bone masks, properties, live debug, and error/log surfaces;
- creating or editing animation graph nodes, state machines, transitions, sync behavior, templates, instances, custom properties, human variables, or action commands;
- exporting or importing animation through Enfusion Blender Tools and Animation Export Profiles;
- using Procedural Animation Editor, procedural nodes, signal processing, and vehicle setup in procedural animation workflows;
- setting up weapon animations, reference poses, pose libraries, object relations, bone constraints, reload/action events, export profiles, and Workbench validation;
- finding exact animation component, command, anim-graph, and scripted command APIs before writing code.

This reference owns animation editor, graph, export, procedural animation, action command, and weapon animation workflows. It does not own generic model import, weapon prefab/component setup, vehicle creation/simulation, audio authoring, general scripting patterns, or diagnostics tooling beyond animation-specific live-debug routing.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: Animation Editor, animation graph nodes, state machines, sync/templates/instances, custom properties, human variables, action commands, export profiles, animation instances, Blender animation import/export, procedural animation, weapon animation setup/tutorials.
- Secondary/cross-reference topics: generic asset import, weapon prefab setup, vehicle setup, audio systems, script implementation, diagnostics, cinematic samples, category pages for animation tutorials and weapon animation routing.

Wiki pages reviewed:
- Animation Editor - https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor - status: covered - reason: owns editor surfaces, preview, workspace, anim set, graph, controls, debug controls, file browser, properties, live debug, attachments debug, and errors.
- Animation Editor: Nodes - https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Nodes - status: covered - reason: owns graph evaluation, timing, and the main animation node family reference.
- Animation Editor: State Machine - https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_State_Machine - status: covered - reason: owns states, transitions, statement operators, and state-machine functions.
- Animation Editor: Sync Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Sync_Tutorial - status: covered - reason: owns sync table, animation events, sync node, and multi-animation sync workflow.
- Animation Editor: Templates and Instances Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Templates_and_Instances_Tutorial - status: covered - reason: owns template/instance workflow, preview model setup, filling instances, and reuse behavior.
- Animation Editor: Custom Properties - https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Custom_Properties - status: covered - reason: owns animation event and custom-property behavior.
- Animation Editor: Human Variables - https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Human_Variables - status: covered - reason: owns human animation variables and vehicle-related variable routing.
- Animation Editor: Character Action Commands - https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Character_Action_Commands - status: covered - reason: owns character action command routing such as weapon reload command behavior.
- Animation Editor: Vehicle Action Commands - https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Vehicle_Action_Commands - status: covered - reason: owns vehicle action command and variable routing for animation graphs.
- Animation Export Profiles - https://community.bistudio.com/wiki/Arma_Reforger:Animation_Export_Profiles - status: covered - reason: owns body/IK/misc/weapon/vehicle export profile families, format, export type, and creation workflow.
- Animation Instances Reference Table - https://community.bistudio.com/wiki/Arma_Reforger:Animation_Instances_Reference_Table - status: covered - reason: owns weapon/player instance mapping and reference-table usage.
- Enfusion Blender Tools: Import/Export Animation - https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Import/Export_Animation - status: covered - reason: owns Blender animation export/import surfaces and troubleshooting.
- Procedural Animation Editor - https://community.bistudio.com/wiki/Arma_Reforger:Procedural_Animation_Editor - status: covered - reason: owns procedural editor panels and basic node surface.
- Procedural Animation Editor Basics Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Procedural_Animation_Editor_Basics_Tutorial - status: covered - reason: owns file creation, input/output, project setup, signal processing, engine RPM/on signals, and vehicle setup.
- Procedural Animation Editor: Nodes - https://community.bistudio.com/wiki/Arma_Reforger:Procedural_Animation_Editor:_Nodes - status: covered - reason: owns procedural node family reference.
- Weapon Animation - https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Animation - status: covered - reason: owns weapon animation overview and official material routes.
- Weapon Animation/Setup - https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Animation/Setup - status: covered - reason: owns setup requirements, Workbench preparation, Blender preparation, weapon scene setup, animation export/import, and validation.
- Weapon Animation/Basic Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Animation/Basic_Tutorial - status: covered - reason: owns the detailed weapon animation tutorial workflow.
- Weapon Animation/Advanced Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Animation/Advanced_Tutorial - status: covered - reason: owns advanced weapon animation tutorial routing.
- Animation Editor: Buffer Node Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Buffer_Node_Tutorial - status: covered - reason: secondary tutorial evidence for buffer nodes and definitions.
- Animation Editor: Pose 2D Node Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Pose_2D_Node_Tutorial - status: covered - reason: secondary tutorial evidence for pose 2D tables and tips.
- Animation Editor: Live Debug Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Live_Debug_Tutorial - status: partial - reason: animation-specific live-debug workflow is covered; general diagnostics ownership remains with `diagnostics-testing-and-performance.md`.

Wiki sections covered:
- Animation Editor: toolbar, top bar, preview, viewport buttons/display, workspace, anim set, animation graph, log console, controls, variables, commands, IK chains, bone masks, debug controls, file browser, properties, live debug, attachments debug, and errors.
- Animation Editor Nodes: graph evaluation, time/timing, common properties, attachment, blend, buffer, context, event, function, group select, IK, memory, procedural, sleep, source, state machine, tag, time, and variable node families.
- State Machine: state machine, state, transition, statements, operators, and functions.
- Sync Tutorial: sync overview, event tables, sync table, events in animations, sync node, and syncing multiple animations.
- Templates and Instances: template/instance definitions, preview model, instance filling, and instance reuse.
- Custom Properties: animation events and custom property setup.
- Human Variables: human animation variables and vehicle-related variables.
- Action Commands: character weapon reload command; vehicle get-in/get-out, gear switch, engine start/stop, lights, seat position, and pedals.
- Export Profiles: body, inverse kinematics, misc, weapon idle/generic weapon/pistol/rifle/machinegun/RPG/grenade/UGL profiles, ground vehicle/aircraft profiles, format, export type, and creation.
- Animation Instances: rifle, weapon instance, and player instance mapping.
- Blender animation import/export: export animations, top section, action list, action export list, import animation to Enfusion, and troubleshooting.
- Procedural Animation Editor: editor panels, node surface, file creation, input/output, project setup, signal processing, engine RPM, engine on, vehicle setup, and procedural node families.
- Weapon Animation: setup, basic tutorial, advanced tutorial, Blender preparation, pose library, reference poses, scene setup, object relations, bone constraints, export/import, Workbench validation, and official supporting materials.

Structured wiki records:
- Tables reviewed/included: 3 buffer-node tables, 1 character-action-command table, 1 human-variable table, 45 animation-node tables, 1 pose-2D table, 5 state-machine tables, 6 vehicle-action-command tables, 14 export-profile tables, 2 animation-instance tables, 1 procedural-basics table, and 52 procedural-node tables.
- Procedures reviewed/included: 9 Animation Editor procedures, 1 live-debug procedure, 1 export-profile procedure, 4 Blender animation import/export procedures, 8 procedural-basics procedures, 1 procedural-editor procedure, 1 weapon-animation overview procedure, 19 weapon-animation basic tutorial procedures, and 10 weapon-animation setup procedures.
- Admonitions reviewed/included: Animation Editor, node/tutorial, export, Blender import/export, procedural animation, and weapon-animation notes/warnings were reviewed and represented as workflow warnings.
- Code blocks reviewed/included: 36 state-machine code/config examples, 2 export-profile examples, and 1 Blender animation import/export example were reviewed as shape evidence; source bodies are not copied.
- Media reviewed: editor screenshots, animation workflow images, Blender setup images, and weapon-animation setup media were reviewed as surface evidence; runtime use does not depend on images.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts/query-reforger-data.py lookup "find animation graph examples" --limit 8`
  - `py -3 scripts/query-reforger-data.py examples animation --limit 8`
  - `py -3 scripts/query-reforger-data.py examples animation --subtopic anim-graph --limit 8`
  - `py -3 scripts/query-reforger-data.py files CharacterAnimationComponent --limit 8`
  - `py -3 scripts/query-reforger-data.py files BaseAnimPhysComponent --limit 8`
  - `py -3 scripts/query-reforger-data.py files AnimPhysCommand --limit 8`
  - `py -3 scripts/query-reforger-data.py files Animation --limit 8`
- Symbols/methods/attributes verified as lookup keys: `CharacterAnimationComponent`, `CharacterAnimationComponentClass`, `SCR_CharacterAnimationComponent`, `SCR_CharacterAnimationComponentClass`, `BaseAnimPhysComponent`, `BaseAnimPhysComponentClass`, `AnimPhysCommandScripted`, `ScriptedCommand`, `CharacterCommandScripted`, `SCR_CharacterCommandLoiter`, `SCR_CharacterCommandSwim`, `SCR_CharacterCommandFly`, `SCR_CharacterCommandHandlerComponent`, and `SCR_ScenarioFrameworkActionCallAnimationCommand`.
- Examples/snippets reviewed: character command examples, loiter/swim/fly command routes, anim phys command route, character animation component route, scenario framework animation command route, scripted commands static table route, AI cinematic look-at route, and consumable/equipment animation use routes.

Samples and source examples:
- Official sample folders reviewed: `SampleMod_AnimationWorkshop`, `SampleMod_CinematicTutorial`.
- Cross-reference sample folders reviewed as layout signals only: `SampleMod_NewWeapon`, `SampleMod_ModdedWeapon`, `SampleMod_NewCar`, `SampleMod_ModdedCar`.
- Raw game-source example families reviewed through query output: character command examples, animation graph command use, character animation components, procedural animation command classes, and animation-triggering scenario action routes.

Coverage gaps:
- No owned primary animation wiki page was skipped.
- Buffer, pose 2D, and live-debug pages are included as secondary covered material because they add node/debug workflow evidence.
- Generic asset/model import is intentionally routed to `asset-import-models-materials-and-props.md`; this reference preserves animation import/export only.
- Weapon prefab/component setup is routed to `weapons-prefabs-attachments-and-firearms.md`; this reference preserves weapon animation setup only.
- Vehicle creation/simulation is routed to `vehicles-creation-simulation-and-compartments.md`; this reference preserves vehicle animation commands only.
- Audio authoring is routed to `audio-editor-signals-and-sound-systems.md`; this reference preserves animation-side command/timing concerns only.
- General script implementation is routed to `script-events-actions-and-patterns.md`; this reference provides animation lookup keys and example routes.
- Exact source bodies and API signatures are not embedded; use query commands before writing API-sensitive code.

## Wiki Source Coverage

Animation work in Reforger is split across editor graph authoring, data/export setup, procedural signal processing, and runtime command integration. Codex should preserve that split:

1. use the Animation Editor to understand the anim set, animation graph, controls, commands, variables, IK chains, bone masks, properties, preview, live debug, and errors;
2. use node and state-machine references to design graph behavior;
3. use sync/templates/instances/custom properties/human variables to wire reusable animation data;
4. use export profiles and Blender animation import/export workflows to move authored animation data into Workbench;
5. use Procedural Animation Editor for signal-driven behavior;
6. use weapon animation setup/tutorials for weapon-specific pose, scene, export, import, and validation workflows;
7. use game-data queries for exact component and command APIs.

Animation Editor coverage:

- Toolbar and top bar are the main editor command surfaces; use them to locate project/editor operations before searching source.
- Anim Editor Preview provides viewport controls and display options for inspecting animation behavior visually.
- Workspace is the place where graph/node work happens.
- Anim Set connects the graph to the set of animations and resources being authored.
- Animation Graph is the core graph surface; do not treat graph work as plain script work.
- Log Console and Errors are first-line validation surfaces when a graph, resource, or import fails.
- Controls include variables, commands, IK chains, and bone masks; these are graph-facing data/control surfaces, not arbitrary code names.
- Debug Controls, Live Debug, and Attachments Debug allow Workbench/runtime inspection of graph state and attachment behavior.
- File Browser and Properties connect selected graph/resources/nodes to editable properties.

Animation node coverage:

- Graph evaluation and time/timing sections are source authority for how graph execution should be reasoned about.
- Common node properties apply across node families; check them before assuming a family-specific setting.
- Attachment nodes route attachment behavior.
- Blend nodes include normal blend, N-way, T-way, additive, TW, queue, and switch-like behavior.
- Buffer nodes save/use/filter poses or data for later graph use.
- Context begin/end nodes organize context-scoped behavior.
- Event nodes emit or consume animation events.
- Function begin/call/end nodes organize reusable graph logic.
- Group select nodes select animation groups.
- IK nodes include IK2, IK2 plane, IK2 target, IK lock, IK rotation, RBF, and weapon IK.
- Memory nodes preserve state.
- Procedural nodes inside Animation Editor are separate from the standalone Procedural Animation Editor but share the idea of generated animation behavior.
- Sleep nodes control evaluation behavior.
- Source nodes include bind pose, pose, pose 2, source, source in-loop-out, and source sync.
- State-machine nodes embed state-machine behavior in graph flow.
- Tag nodes mark behavior.
- Time save/scale/use nodes manipulate time.
- Variable reset/set/update nodes manipulate graph variables.

State-machine coverage:

- A state machine is not just a switch; it owns states, transitions, and statements.
- States hold animation behavior and transition logic.
- Transitions define when and how the graph moves between states.
- Statement operators and functions are part of the animation graph expression system; preserve them when interpreting wiki examples.
- State-machine code/config examples were reviewed as structure evidence, but exact bodies belong in source/query output, not in this reference.

Sync/templates/instances/custom-property coverage:

- Sync Tutorial owns the sync table, animation events, sync node, and syncing between multiple animations.
- Sync tables and event tables are workflow-critical because animation clips must align behavior across animations.
- Events in animations are used to coordinate gameplay/graph behavior with authored timing.
- Templates and instances let one authored pattern be reused with different data.
- Preview model selection matters because instance/template work must be inspected against a valid model.
- Custom properties are attached through animation events/custom-property surfaces and should be treated as authored animation metadata.

Human variables/action-command coverage:

- Human Variables is the routing source for variables used by human animation graphs.
- Character action commands include weapon reload behavior.
- Vehicle action commands include get-in, get-out, gear switch, engine start/stop, lights, seat position type, and pedals.
- Action commands are graph/runtime integration points; verify exact command APIs through query output before scripting.

Export and instance coverage:

- Animation Export Profiles define how authored animation is exported for different body, IK, weapon, vehicle, and aircraft contexts.
- Weapon profile families include idles, generic weapon profiles, pistols, rifles, machineguns, RPGs, grenades, and UGLs.
- Vehicle profile families include ground vehicles and aircraft.
- Export profile format/export type/creation sections define the expected shape of export data.
- Animation Instances Reference Table provides weapon and player instance mapping; use it when an animation task refers to instances rather than graph nodes.

Blender animation import/export coverage:

- Export animations from Blender is the source for the Blender-side export workflow.
- Top section, action list, and action export list are separate surfaces; do not collapse them into one vague "export from Blender" step.
- Import animation to Enfusion is the Workbench-side import route.
- Troubleshooting includes incorrect save location, TXA registration failure from invalid relative path translation, and missing metafile creation.

Procedural Animation Editor coverage:

- Procedural Animation Editor owns procedural editor panels and procedural node surface.
- Basics Tutorial owns file creation, input/output, project setup, signal processing, engine RPM, engine on, and vehicle setup.
- Procedural node families include signal, constants, bone, rotation set/make/break, translate set/make/break, scale set/make/break, input/output/value/random/generator/math/conversion/envelope/interpolation/smoothing/clamp/trig-like signal nodes.
- Signal processing examples, especially engine RPM and engine on, are important for vehicle/animation tasks that are driven by runtime values.

Weapon animation coverage:

- Weapon Animation overview provides official supporting material routes.
- Weapon Animation Setup owns required Workbench and Blender preparation before a weapon animation tutorial can succeed.
- Basic Tutorial owns preparing Workbench, preparing Blender, enabling pose library, loading example files, setting reference poses, applying poses, adding weapon to the scene, object relations, bone constraints, animation export/import, and validation.
- Advanced Tutorial is included as advanced routing but should not replace the setup/basic workflow.
- Weapon animation tasks often touch weapon prefabs and assets, but this reference owns only the animation setup/export/graph side.

## Terms And Concepts

- Anim set: the resource/data set that connects animations to graph use.
- Animation graph: the node graph that evaluates animation behavior.
- Graph evaluation: how graph nodes produce the final pose/behavior over time.
- Animation node: a graph unit such as source, blend, IK, event, variable, state machine, or time node.
- Source node: a node that introduces authored animation/pose data.
- Blend node: a node that mixes poses or animation sources.
- Buffer node: a node family for storing/reusing filtered pose/data state.
- Event node: a node that works with animation events.
- Function node: a node family for reusable graph logic.
- IK node: inverse-kinematics node family, including weapon IK.
- State machine: graph structure with states, transitions, and transition statements.
- Transition: rule that moves animation behavior from one state to another.
- Sync table: data used to synchronize multiple animations or animation events.
- Template: reusable animation setup that can be instantiated.
- Instance: concrete data/config applying a template to a model or animation use case.
- Custom property: authored animation metadata/event data exposed for graph/runtime use.
- Human variable: variable family used by human animation behavior.
- Action command: command route connecting animation graph behavior with runtime character or vehicle actions.
- Export profile: data profile controlling animation export behavior.
- Animation instance: mapping used by weapon/player animation setup.
- Procedural animation: animation behavior generated or modified from signals/nodes rather than only authored clips.
- PAP node: procedural animation editor node.
- Signal: runtime or authored value used to drive procedural animation.
- Weapon animation setup: workflow for getting weapon poses, scene constraints, export/import, and graph/resource validation correct.

## Workbench / Resource / Data Surfaces

Animation Editor surfaces:

- Toolbar and top bar for editor commands.
- Preview viewport for model/animation inspection.
- Workspace for graph authoring.
- Anim Set for animation set/resource association.
- Animation Graph for node/state-machine work.
- Log Console and Errors for validation.
- Controls for variables, commands, IK chains, and bone masks.
- Debug Controls, Live Debug, and Attachments Debug for runtime/editor inspection.
- File Browser for resources.
- Properties for selected resources/nodes.

Animation data/resource surfaces:

- Animation nodes and state-machine statements.
- Sync tables and event tables.
- Templates and instances.
- Custom properties.
- Human variables.
- Character and vehicle action commands.
- Animation export profiles.
- Animation instance reference mappings.
- Blender action list and action export list.
- Imported animation resources.

Procedural animation surfaces:

- Procedural Animation Editor panels.
- Input/output files and project setup.
- Signal processing graph.
- Engine RPM and engine-on signal workflows.
- Procedural node families for transform, rotation, scale, math, conversion, envelope, smoothing, interpolation, clamp, and trigonometric behavior.

Weapon animation surfaces:

- Workbench setup for weapon animation.
- Blender scene setup with weapon/reference content.
- Pose library and reference poses.
- Object relation or bone constraint setup.
- Export/import profile selection.
- Animation instance/profile validation.

## Required Workflows

Use an Animation Editor graph:

1. Open the animation resource and confirm the anim set is correct.
2. Inspect the preview model, viewport display, and editor errors.
3. Locate graph controls: variables, commands, IK chains, and bone masks.
4. Work in the animation graph workspace.
5. Choose node families based on behavior: source for clips, blend for mixing, IK for target solving, event for timing, state machine for stateful transitions, variables for graph state.
6. Validate graph evaluation and time/timing behavior.
7. Use live debug/attachments debug when runtime behavior differs from editor expectations.

Build or modify a state machine:

1. Identify states and the animation behavior each state owns.
2. Define transition conditions.
3. Use the documented statement operators/functions for transition logic.
4. Verify transition timing and graph evaluation.
5. Use debug controls to confirm active state/transition behavior.

Set up sync:

1. Identify which animations need synchronization.
2. Review event tables and sync table requirements.
3. Add animation events at the correct authored timing.
4. Use sync nodes where graph behavior must align multiple animations.
5. Verify synced playback in editor preview and runtime.

Use templates and instances:

1. Create or select the template.
2. Set the preview model.
3. Fill the instance data.
4. Reuse the template through instances instead of duplicating graph/resource structure.
5. Validate that each instance maps to the intended model/resource behavior.

Export and import animation:

1. Select the correct export profile family for the target: body, IK, weapon, vehicle, aircraft, or specific weapon class.
2. In Blender, use the animation export workflow, top-section settings, action list, and action export list.
3. Export to the expected project-relative location.
4. Import animation to Enfusion.
5. Resolve troubleshooting issues before continuing: wrong save location, TXA registration failure, or missing metafile.
6. Validate imported animation in Animation Editor.

Set up procedural animation:

1. Create required procedural files.
2. Define input and output surfaces.
3. Complete project setup.
4. Add signal-processing nodes.
5. For vehicle-like examples, wire engine RPM and engine-on signals first.
6. Add procedural nodes only after signal routing is understood.
7. Validate in Procedural Animation Editor and runtime.

Set up weapon animation:

1. Prepare Workbench for the weapon animation workflow.
2. Prepare Blender and enable required pose-library support.
3. Load the example/reference file or equivalent source scene.
4. Set reference poses.
5. Apply poses from the pose library.
6. Add weapon content to the scene.
7. Choose object relations or bone constraints for the weapon scene setup.
8. Select the correct export profile and animation instance route.
9. Export from Blender and import to Enfusion.
10. Validate in Animation Editor and runtime with the weapon/prefab route.

## Configuration Fields And Tables

Animation Editor and node tables:

- Node families: attachment, blend, buffer, context, event, function, group select, IK, memory, procedural, sleep, source, state machine, tag, time, and variables.
- Common node properties: review before tuning specific node behavior.
- Time/timing properties: use when animation playback, sync, or transition timing is wrong.
- IK properties: review IK2, plane, target, lock, rotation, RBF, and weapon IK fields when solving hands/weapons/attachments.
- Variable properties: reset, set, and update nodes must match the variable data used by controls.

State-machine tables and code-shape records:

- State machine settings.
- State settings.
- Transition settings.
- Statement operators.
- Statement functions.
- Transition logic must be interpreted from the state-machine documentation and verified in editor/runtime.

Sync/template/instance tables:

- Event tables define animation event timing data.
- Sync table defines how animations synchronize.
- Template and instance setup depends on preview model and instance filling.
- Animation Instances Reference Table maps weapon/player instance usage and should guide instance lookup.

Action command tables:

- Character action commands include weapon reload routing.
- Vehicle action commands include get-in, get-out, gear switch, engine start/stop, lights, seat position type, and pedals.
- Action-command tables are graph integration references; exact script APIs still require query lookup.

Export profile tables:

- Body, inverse kinematics, misc, weapon idle, generic weapon, pistol, rifle, machinegun, RPG, grenade, UGL, ground vehicle, and aircraft profile families.
- Export type and format fields determine how authored data is exported.
- Creation workflow defines how to produce profile data rather than hand-guessing it.

Procedural node tables:

- PAP transform node families: bone, rotation set/make/break, translate set/make/break, scale set/make/break.
- Signal node families: input, output, value, random, generator, sum/sub/mul/div, min/max, exponent/log/conversions, envelope, interpolate, smoother, floor/ceil/round, clamp, and trigonometric-like nodes.
- Signal-processing examples should drive the first implementation before custom procedural graphs are created.

Weapon animation fields:

- Blender setup, pose library, reference pose data, object relation route, bone constraint route, export profile, action export list, import settings, and validation surfaces.
- Weapon animation instances and export profile data must match the intended weapon class/profile family.

## Procedures And Ordered Steps

Animation Editor procedure:

1. Open the animation resource.
2. Validate preview model and anim set.
3. Check log console and errors.
4. Inspect graph controls.
5. Edit graph nodes/state machines.
6. Validate timing, variables, commands, IK chains, and bone masks.
7. Use live debug and attachments debug for runtime differences.
8. Save only after graph/resource validation passes.

Animation graph node procedure:

1. Identify the behavior family: source, blend, IK, event, state, time, variable, or procedural.
2. Read the relevant node family fields.
3. Wire graph inputs/outputs.
4. Validate evaluation and time behavior.
5. Use editor errors/debug before changing unrelated resources.

State machine procedure:

1. Define states.
2. Define transitions.
3. Write transition statements using documented operators/functions.
4. Test transition order and timing.
5. Debug active state and graph flow.

Blender export/import procedure:

1. Prepare the Blender scene and action list.
2. Select export targets in the action export list.
3. Use the correct export profile.
4. Export animation to the expected relative project location.
5. Import animation in Enfusion.
6. Fix save location, TXA registration, or metafile failures before authoring graph behavior on top.

Procedural animation procedure:

1. Create procedural animation files.
2. Set inputs and outputs.
3. Complete project setup.
4. Build signal processing.
5. Use engine RPM/engine-on examples for vehicle-like signal behavior.
6. Connect procedural node outputs to animation behavior.
7. Validate editor and runtime results.

Weapon animation procedure:

1. Prepare Workbench.
2. Prepare Blender.
3. Enable pose-library support.
4. Load reference/example data.
5. Set reference poses.
6. Apply pose-library poses.
7. Add weapon to the scene.
8. Choose object relations or bone constraints.
9. Export with the correct profile.
10. Import and validate in Enfusion.
11. Test with the weapon/prefab setup in runtime.

## Warnings And Failure Modes

- Do not guess animation APIs. Query exact component and command classes before writing code.
- `files Animation` is broad and noisy. Prefer `lookup "find animation graph examples"`, `examples animation --subtopic anim-graph`, `files CharacterAnimationComponent`, `files BaseAnimPhysComponent`, and `files AnimPhysCommand`.
- Generated files are strongest for exact class and inheritance truth; handwritten character command files are stronger for implementation patterns.
- Animation graph work is not generic scripting. Validate graph evaluation, time/timing, variables, commands, and node family behavior in Animation Editor.
- State-machine transitions can fail from statement/operator mistakes even when animation clips are valid.
- Sync issues often come from missing or misaligned event tables/sync tables, not from source code.
- Template/instance failures often come from wrong preview model, incomplete instance filling, or mismatched resource mapping.
- Blender export failures can come from wrong save location, failed TXA registration, or missing metafile.
- Weapon animation setup depends on reference poses, pose-library use, object relations or bone constraints, export profiles, and correct import. Skipping setup usually creates later graph/runtime failures.
- Procedural animation depends on signal routing. Do not add complex procedural nodes until input/output and signal processing are validated.
- Vehicle action commands in this reference are animation command data; vehicle creation/simulation remains owned by the vehicle reference.
- Character/weapon animation can cross weapon prefabs, inventory, audio, and scripts. Use the owning references for those systems instead of duplicating setup here.
- Live debug is useful, but broad diagnostic tooling remains owned by the diagnostics reference.
- Runtime validation is required; editor preview does not prove all command, graph, attachment, weapon, or procedural behavior works in play mode.

## API Lookup Keys

Use these lookup keys before writing animation-sensitive code:

- Animation components: `CharacterAnimationComponent`, `CharacterAnimationComponentClass`, `SCR_CharacterAnimationComponent`, `SCR_CharacterAnimationComponentClass`, `BaseAnimPhysComponent`, `BaseAnimPhysComponentClass`.
- Command classes: `AnimPhysCommandScripted`, `ScriptedCommand`, `CharacterCommandScripted`, `SCR_CharacterCommandLoiter`, `SCR_CharacterCommandSwim`, `SCR_CharacterCommandSwimST`, `SCR_CharacterCommandFly`, `SCR_CharacterCommandHandlerComponent`, `SCR_CharacterCommandHandlerComponent_Tests`.
- Scenario/action route: `SCR_ScenarioFrameworkActionCallAnimationCommand`.
- Supporting search terms: `AnimGraph`, `AnimPhys`, `AnimationComponent`, `CharacterCommand`, `ScriptedCommandsStaticTable`, `AnimationSource`, `Animation`.
- Cross-domain lookup keys when needed: weapon animation tasks may need weapon lookup keys; vehicle animation command tasks may need vehicle lookup keys; audio-timed animation tasks may need audio lookup keys.

## Game-Data Query Commands

Run these before writing API-sensitive animation code:

```powershell
py -3 scripts/query-reforger-data.py lookup "find animation graph examples" --limit 8
py -3 scripts/query-reforger-data.py examples animation --limit 8
py -3 scripts/query-reforger-data.py examples animation --subtopic anim-graph --limit 8
py -3 scripts/query-reforger-data.py files CharacterAnimationComponent --limit 8
py -3 scripts/query-reforger-data.py files BaseAnimPhysComponent --limit 8
py -3 scripts/query-reforger-data.py files AnimPhysCommand --limit 8
py -3 scripts/query-reforger-data.py files Animation --limit 8
```

Use exact symbols after a route is selected:

```powershell
py -3 scripts/query-reforger-data.py symbol CharacterAnimationComponent --kind class --exact
py -3 scripts/query-reforger-data.py symbol BaseAnimPhysComponent --kind class --exact
py -3 scripts/query-reforger-data.py symbol AnimPhysCommandScripted --exact
py -3 scripts/query-reforger-data.py files SCR_CharacterAnimationComponent --limit 8
```

Use snippets only after targeted search identifies a useful file:

```powershell
py -3 scripts/query-reforger-data.py snippet scripts/Game/Character/Examples/SCR_CharacterCommandSwim.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/Game/Character/Commands/SCR_CharacterCommandLoiter.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/Game/Character/Examples/SCR_CharacterCommandFly.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/Game/Character/animPhysCommand.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/Game/Components/SCR_CharacterAnimationComponent.c --line 1 --context 30
```

Preferred Codex flow:

1. Read this reference for workflow and ownership boundaries.
2. Use `lookup "find animation graph examples"` for a bounded task bundle.
3. Use exact `files` or `symbol` commands for the component/command family.
4. Inspect bounded snippets only for selected handwritten examples.
5. Validate in Animation Editor, Workbench, and runtime.

## Examples And Samples

Official samples:

- `SampleMod_AnimationWorkshop`: primary sample layout signal for animation workshop content and animation-specific resources.
- `SampleMod_CinematicTutorial`: sample layout signal for cinematic/animation-adjacent workflows.
- `SampleMod_NewWeapon` and `SampleMod_ModdedWeapon`: cross-reference signals for weapon animation resource and weapon-related animation integration.
- `SampleMod_NewCar` and `SampleMod_ModdedCar`: cross-reference signals for vehicle action command/procedural vehicle animation context.

Game-source example routes from query output:

- `scripts/Game/Character/Examples/SCR_CharacterCommandSwim.c`: character command and anim-graph example.
- `scripts/Game/Character/Commands/SCR_CharacterCommandLoiter.c`: character command and custom animation data example.
- `scripts/Game/Character/Examples/SCR_CharacterCommandFly.c`: scripted command example.
- `scripts/Game/Character/Examples/SCR_CharacterCommandHandler_Tests.c`: command handler test/example route.
- `scripts/Game/Character/animPhysCommand.c`: `AnimPhysCommandScripted` route.
- `scripts/Game/Components/SCR_CharacterAnimationComponent.c`: handwritten character animation component route.
- `scripts/Game/ScenarioFramework/Actions/SCR_ScenarioFrameworkActionCallAnimationCommand.c`: scenario action route for calling animation commands.
- `scripts/Game/Character/Commands/SCR_ScriptedCommandsStaticTable.c`: scripted commands table route.
- `scripts/Game/AI/ScriptedNodes/Soldier/SCR_AICinematicLookAt.c`: AI/cinematic animation route.

Example selection rules:

- Prefer wiki workflows for editor surfaces, node families, export/import order, and weapon animation setup.
- Prefer official samples for resource/project layout.
- Prefer generated game files for exact component and inheritance truth.
- Prefer handwritten command/component files for implementation examples.
- Do not copy source bodies into references or answers; use bounded snippets when implementation context is needed.

## Follow-Up Keywords

Use these keywords for searches and task routing:

- `Animation Editor`
- `Animation Graph`
- `AnimGraph`
- `AnimPhys`
- `BaseAnimPhysComponent`
- `CharacterAnimationComponent`
- `SCR_CharacterAnimationComponent`
- `AnimPhysCommandScripted`
- `CharacterCommandScripted`
- `ScriptedCommand`
- `SCR_CharacterCommandLoiter`
- `SCR_CharacterCommandSwim`
- `SCR_CharacterCommandFly`
- `state machine`
- `transition`
- `statement operators`
- `statement functions`
- `sync table`
- `animation events`
- `templates and instances`
- `custom properties`
- `human variables`
- `character action commands`
- `vehicle action commands`
- `Animation Export Profiles`
- `Animation Instances Reference Table`
- `Procedural Animation Editor`
- `procedural animation nodes`
- `engine RPM`
- `engine on`
- `weapon animation setup`
- `pose library`
- `reference poses`
- `object relations`
- `bone constraints`
- `action export list`
- `TXA registration`
- `metafile`
- `SampleMod_AnimationWorkshop`
- `SampleMod_CinematicTutorial`

## Verification

Animation Editor validation:

- Confirm the expected anim set, preview model, graph, controls, variables, commands, IK chains, and bone masks.
- Check Log Console and Errors before assuming a source or export issue.
- Validate node family settings and graph evaluation.
- Validate state-machine states, transitions, statements, operators, and functions.
- Validate sync tables/events and multi-animation sync behavior.
- Use Live Debug and Attachments Debug for runtime graph/attachment differences.

Export/import validation:

- Confirm the export profile family matches body, IK, weapon, vehicle, aircraft, or specific weapon type.
- Confirm Blender action list and action export list are configured.
- Confirm animation export uses the expected relative project location.
- Confirm Enfusion import succeeds and produces required resource metadata.
- Resolve incorrect save location, TXA registration, or metafile errors before graph authoring.

Procedural animation validation:

- Confirm procedural files, input/output, and project setup.
- Confirm signal processing before adding complex nodes.
- Confirm engine RPM/engine-on signals when using vehicle-like examples.
- Validate procedural node output in editor and runtime.

Weapon animation validation:

- Confirm Workbench and Blender setup.
- Confirm pose library, reference poses, scene setup, object relations, or bone constraints.
- Confirm export profile and animation instance mapping.
- Confirm imported animation works with the intended weapon route.
- If the task changes weapon prefab/component behavior, route to `weapons-prefabs-attachments-and-firearms.md`.

Script/API validation:

- Query exact animation component and command APIs before writing code.
- Use snippets only for selected files.
- If behavior crosses replication, server runtime, audio, weapons, vehicles, or general script patterns, read the owning reference for that system and verify there too.

## Official Wiki Links

- Animation Editor: https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor
- Animation Editor: Nodes: https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Nodes
- Animation Editor: State Machine: https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_State_Machine
- Animation Editor: Sync Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Sync_Tutorial
- Animation Editor: Templates and Instances Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Templates_and_Instances_Tutorial
- Animation Editor: Custom Properties: https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Custom_Properties
- Animation Editor: Human Variables: https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Human_Variables
- Animation Editor: Character Action Commands: https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Character_Action_Commands
- Animation Editor: Vehicle Action Commands: https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Vehicle_Action_Commands
- Animation Export Profiles: https://community.bistudio.com/wiki/Arma_Reforger:Animation_Export_Profiles
- Animation Instances Reference Table: https://community.bistudio.com/wiki/Arma_Reforger:Animation_Instances_Reference_Table
- Enfusion Blender Tools: Import/Export Animation: https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Import/Export_Animation
- Procedural Animation Editor: https://community.bistudio.com/wiki/Arma_Reforger:Procedural_Animation_Editor
- Procedural Animation Editor Basics Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Procedural_Animation_Editor_Basics_Tutorial
- Procedural Animation Editor: Nodes: https://community.bistudio.com/wiki/Arma_Reforger:Procedural_Animation_Editor:_Nodes
- Weapon Animation: https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Animation
- Weapon Animation/Setup: https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Animation/Setup
- Weapon Animation/Basic Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Animation/Basic_Tutorial
- Weapon Animation/Advanced Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Animation/Advanced_Tutorial
- Animation Editor: Buffer Node Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Buffer_Node_Tutorial
- Animation Editor: Pose 2D Node Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Pose_2D_Node_Tutorial
- Animation Editor: Live Debug Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Animation_Editor:_Live_Debug_Tutorial

## Usefulness Score

Score: `94/100`

- Wiki coverage: `29/30`
  - All owned primary animation pages are reviewed and represented.
  - Secondary buffer, pose 2D, and live-debug pages are included where they improve graph/node/debug coverage.
  - Tables, procedures, warnings, code/config examples, media, and links were reviewed; dense table families are represented as node/profile/field families instead of copied dumps.
  - Missed coverage: exact screenshot-level UI placement is not embedded; impact is low because editor surfaces and official URLs are present.
- Operational detail: `14/15`
  - Preserves Animation Editor surfaces, graph/node families, state machines, sync, templates/instances, export/import, procedural animation, and weapon animation workflow order.
  - Some extremely large node tables are compressed into families to keep the reference usable.
- API lookup usefulness: `15/15`
  - Exact lookup keys and commands are present for animation components, command classes, examples, files, and snippets.
- Example grounding: `9/10`
  - Official animation/cinematic samples and cross-reference weapon/vehicle samples are named.
  - Game-source examples are routed through query output without copying bodies.
- Codex task usefulness: `15/15`
  - Supports common tasks: find animation graph examples, create/edit graph behavior, set up state machines/sync/templates, export/import animation, build procedural animation, and set up weapon animation.
- Context efficiency: `8/10`
  - Dense but navigable. The length is justified by the wiki source density and table-heavy node/profile references.
  - Split boundaries prevent this file from owning generic assets, weapons, vehicles, audio, scripting, or diagnostics.
- Verification guidance: `4/5`
  - Workbench, editor, export/import, procedural, weapon-animation, runtime, and API verification are present.
  - Multiplayer/server verification is routed only when a task crosses into those systems.

Category-fit check:
- Source family complete: pass. Animation Editor, nodes, state machines, sync, templates/instances, custom properties, human variables, action commands, export profiles, animation instances, Blender animation import/export, procedural animation, and weapon animation are covered.
- No owned page missing: pass.
- Split boundary justified: pass. Generic assets, weapons, vehicles, audio, scripting, diagnostics, multiplayer, and server runtime are routed to owning references.
- Cross-links present: pass.
- Task route clear: pass. Animation graph tasks route to this reference plus `lookup "find animation graph examples"` and targeted animation queries.
- Automatic failure conditions: none found.
