# Vehicles Creation Simulation And Compartments

## When To Read

Read this when the task is about vehicle-specific setup or behavior:

- creating a new car or wheeled vehicle from model data through prefab setup;
- preparing vehicle meshes, split parts, colliders, fire geometry, skeleton, rigging, textures, and imported model resources;
- configuring vehicle prefabs, actions, action contexts, compartments, compartment slots, seat behavior, and access points;
- tuning wheeled simulation: controller input, engine, gearbox, clutch, suspension, wheels, tyres, differentials, aerodynamics, and Pacejka-related values;
- modifying an existing vehicle's damage behavior, armor, collision impulse, fuel type, fuel capacity, consumption, driving behavior, turret, or exhaust effects;
- finding exact vehicle controller, compartment, simulation, damage, and debug APIs before writing code.

This reference owns vehicle creation, simulation, compartment setup, and vehicle modding. It does not own generic asset import, generic prefab/config modeling, generic entity/component lifecycle, vehicle animation commands, vehicle audio authoring, or Game Master/Conflict vehicle availability.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: car creation, car asset preparation, car prefab configuration, car simulation configuration, car modding, wheeled vehicle simulation.
- Secondary/cross-reference topics: generic asset import, generic prefab/config modeling, entity/component lifecycle, animation commands, audio authoring, Game Master and Conflict availability, server/runtime validation.

Wiki pages reviewed:
- Car Creation - https://community.bistudio.com/wiki/Arma_Reforger:Car_Creation - status: covered - reason: source family overview for adding a new car, structure preparation, and creation steps.
- Car Creation/Asset Preparation - https://community.bistudio.com/wiki/Arma_Reforger:Car_Creation/Asset_Preparation - status: covered - reason: owned vehicle mesh, orientation, split-part, collider, fire geometry, layer preset, skeleton, rigging, FBX, import, material, and texture workflow.
- Car Creation/Prefab Configuration - https://community.bistudio.com/wiki/Arma_Reforger:Car_Creation/Prefab_Configuration - status: covered - reason: owned vehicle prefab, action, action context, compartment, and compartment slot workflow.
- Car Creation/Simulation Configuration - https://community.bistudio.com/wiki/Arma_Reforger:Car_Creation/Simulation_Configuration - status: covered - reason: owned engine, gearbox, clutch, suspension, wheel, tyre, differential, aerodynamics, Pacejka, and debugging workflow.
- Car Modding - https://community.bistudio.com/wiki/Arma_Reforger:Car_Modding - status: covered - reason: owned workflow for changing existing vehicle prefab/material/damage/fuel/driving/turret/exhaust behavior and testing changes.
- Vehicle: Wheeled Simulation - https://community.bistudio.com/wiki/Arma_Reforger:Vehicle:_Wheeled_Simulation - status: covered - reason: owned detailed field guide for wheeled controller and simulation parameters.

Wiki sections covered:
- Car Creation: tutorial goals, adding a new car, structure preparation, and creation step map.
- Asset Preparation: preparing mesh, model orientation, splitting mesh into parts, naming objects, creating colliders, collision geometry, fire geometry, layer presets, skeleton setup, mesh rigging, FBX export settings, mesh import, model registration, collider/material checking, skeleton/hierarchy checking, and texture import.
- Prefab Configuration: basic car configuration, creating a new prefab, creating actions, `ActionsManagerComponent`, action contexts, additional actions, compartments setup, compartment overview, compartment configuration, and new compartment slots.
- Simulation Configuration: simulation setup, engine parameters, gearbox and clutch parameters, suspension parameters, wheels, differential and torque share, wheel, tyre, wheel positions, aerodynamics, Pacejka, and debugging.
- Car Modding: modifying an existing car, file structure, prefab preparation, multi material base color, component overview, damage behavior, damage manager overview, armor, collision impulse, fuel consumption, fuel handling overview, fuel type, fuel tank capacity, increased consumption, driving behavior, wheeled simulation overview, engine parameters, driving characteristics, turret addition, exhaust effects, and in-game testing.
- Vehicle Wheeled Simulation: `SCR_CarControllerComponent` and wheeled simulation parameter families for input/controller behavior, transmission, steering, throttle, braking, engine startup/shutdown, clutch, shifting, simulation solver, engine torque/RPM/friction, gearbox, differentials, axles, suspension, wheels, tyres, swaybars, aerodynamics, and debug interpretation.

Structured wiki records:
- Tables reviewed/included: 1 asset-preparation table, 2 prefab-configuration tables, 3 simulation-configuration tables, 3 car-modding tables, and 22 wheeled-simulation parameter tables.
- Procedures reviewed/included: 1 Car Creation procedure, 2 asset-preparation procedures, 3 prefab-configuration procedures, 1 Car Modding procedure, and 1 Wheeled Simulation procedure.
- Admonitions reviewed/included: 5 Car Creation notes/warnings, 13 asset-preparation notes/warnings, 7 prefab-configuration notes/warnings, 3 simulation-configuration notes/warnings, 8 car-modding notes/warnings, and 1 wheeled-simulation note.
- Code blocks reviewed/included: 2 wheeled-simulation code/config examples were reviewed as field-shape evidence; exact code bodies are not copied.
- Media reviewed: vehicle workflow screenshots and diagrams were reviewed as editor-surface evidence; runtime use does not depend on images.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts/query-reforger-data.py lookup "vehicle compartment" --limit 8`
  - `py -3 scripts/query-reforger-data.py examples vehicle --subtopic compartment --limit 8`
  - `py -3 scripts/query-reforger-data.py examples vehicle --subtopic vehicle-component --limit 8`
  - `py -3 scripts/query-reforger-data.py files Vehicle --limit 8`
  - `py -3 scripts/query-reforger-data.py files BaseCompartmentManagerComponent --limit 8`
  - `py -3 scripts/query-reforger-data.py files VehicleControllerComponent --limit 8`
  - `py -3 scripts/query-reforger-data.py files SCR_CarControllerComponent --limit 8`
- Symbols/methods/attributes verified as lookup keys: `VehicleControllerComponent`, `BaseVehicleControllerComponent`, `CarControllerComponent`, `CarControllerComponent_B`, `SCR_CarControllerComponent`, `SCR_CarControllerComponent_B`, `BaseCompartmentManagerComponent`, `SCR_BaseCompartmentManagerComponent`, `Vehicle`, `BaseVehicle`, `BaseLightManagerComponent`, `SCR_VehicleDamageManagerComponent`, `SCR_VehicleDebug`, and vehicle available-action condition classes.
- Examples/snippets reviewed: vehicle controller, base compartment manager, vehicle class, car controller, vehicle debug, vehicle damage manager, vehicle lights/action conditions, and AI vehicle compartment handling routes.

Samples and source examples:
- Official sample folders reviewed: `SampleMod_NewCar`, `SampleMod_ModdedCar`.
- Official sample layout signals reviewed: vehicle assets, wheeled vehicle prefabs, vehicle configs, editor previews, vehicle sounds, particles, vehicle part prefabs, turret-related prefab routes, and vehicle script folders.
- Game-source example families reviewed through query output: vehicle controllers, compartment manager, vehicle damage, vehicle debug, HUD available-action conditions, AI vehicle compartment use, and car controller routes.

Coverage gaps:
- No owned primary wiki page was skipped.
- Generic FBX/model/material import is intentionally routed to `asset-import-models-materials-and-props.md`; this file preserves only vehicle-specific asset requirements.
- Generic prefab/config modeling is routed to `prefabs-configs-containers-and-catalogs.md`; this file preserves vehicle-specific prefab, action, and compartment wiring.
- Generic component lifecycle is routed to `entities-components-and-lifecycle.md`; this file preserves vehicle component ownership only where it affects vehicle tasks.
- Vehicle animation command authoring is routed to `animation-graphs-weapon-animation-and-export.md`.
- Vehicle audio authoring is routed to `audio-editor-signals-and-sound-systems.md`.
- Game Master, Conflict, faction, and scenario availability are routed to `game-master-factions-tasks-and-modes.md`.
- Exact source bodies and API signatures are not embedded; use query commands before writing API-sensitive code.

## Wiki Source Coverage

Vehicle creation is a chained workflow. Codex should keep the order intact:

1. create or choose the source vehicle structure;
2. prepare vehicle asset parts, colliders, skeleton, rig, materials, textures, and import settings;
3. create a vehicle prefab and wire actions/action contexts;
4. configure compartments and compartment slots;
5. configure wheeled simulation fields;
6. test in Workbench/play mode and tune using debug output;
7. only then modify damage, fuel, turret, exhaust, and gameplay behavior.

Car Creation provides the top-level tutorial route. It is mainly a map to the vehicle creation subpages, but it still matters because it frames the workflow as a full vehicle task, not only a script or only a model import. It ties structure preparation to the creation steps and keeps the vehicle work grounded in an addon/resource layout.

Asset Preparation covers the vehicle-specific asset work. The important wiki-backed details are:

- orient the model as expected by the vehicle tools and game runtime before exporting;
- split the mesh into vehicle parts that can be addressed independently for animation, damage, doors, wheels, glass, lights, or other runtime behavior;
- use predictable object names so the imported hierarchy and later prefab wiring are readable;
- create collision geometry separately from render geometry and keep collision shapes aligned with intended physical behavior;
- create fire geometry for hit/protection behavior where the vehicle should receive damage or ballistic interaction;
- apply correct layer presets so collision and fire geometry behave as the engine expects;
- set up skeleton and rigging so moving parts, wheels, doors, suspension, and related authored pieces can be driven by the vehicle runtime;
- export with the documented FBX settings, then import and register the model in Workbench;
- inspect colliders, materials, skeleton, and hierarchy after import instead of assuming the 3D source exported cleanly;
- import textures and verify material assignment as part of vehicle validation, not as a separate cosmetic afterthought.

Prefab Configuration owns the first playable vehicle wiring:

- create the vehicle prefab from the imported model/resource;
- add the basic car configuration before layering extra gameplay behavior;
- configure actions through the vehicle action manager surface;
- create action contexts so entry, exit, seat, door, and related interactions appear in the correct place and are valid for the intended compartment;
- add additional actions only after the base vehicle can be entered and operated;
- configure compartments as the bridge between the physical prefab, seats, crew/passenger roles, action contexts, and runtime compartment manager behavior;
- configure compartment slots so seat/crew positions, entry behavior, visibility, and occupancy are not left implicit.

Simulation Configuration owns first-pass drivability. It is not just "tune the car"; it separates parameter families:

- engine parameters define power source behavior, torque/RPM behavior, startup/shutdown behavior, and responsiveness;
- gearbox and clutch parameters define how engine output transfers to wheels and how shifting changes vehicle feel;
- suspension parameters define body/wheel interaction, travel, spring/damper behavior, and stability;
- wheel parameters define radius, mass, brake torque, wheel positions, and the relationship between visual/physical wheels;
- tyre parameters define grip, rolling behavior, drag, roughness, friction, and tread-like behavior;
- differential and torque share parameters decide how power is distributed across outputs and axles;
- aerodynamics and Pacejka-related values affect high-speed behavior and tyre force behavior;
- debugging is a normal part of simulation setup because many values are interdependent.

Car Modding covers changing an existing vehicle. It is useful when Codex is asked to modify behavior instead of creating a new car:

- prepare the prefab copy/override before editing inherited values;
- use the file structure and prefab preparation steps to keep modded resources distinct from source assets;
- change multi material base color through the material/resource workflow, not by editing unrelated visual data;
- review component ownership before changing damage, fuel, driving, turrets, or exhaust so the edit lands on the correct component/config surface;
- modify damage through the damage manager and hit/protection values, including armor and collision impulse behavior;
- modify fuel through fuel type, tank capacity, and consumption surfaces;
- modify driving through wheeled simulation and controller-related fields;
- add a turret through vehicle-specific prefab/component wiring, while routing weapon-specific turret behavior to weapon and animation/audio references when needed;
- change exhaust effects through the vehicle's effect/particle/resource setup and test in game.

Vehicle: Wheeled Simulation is the dense field reference. Preserve these parameter families when answering vehicle simulation tasks:

- controller/input: type, transmission mode, reverse/neutral/drive handling, steering coefficients and speeds, throttle curve/reaction/turbo behavior, brake curve/turbo behavior;
- engine lifecycle: startup time, startup attempts, startup chance, air intakes, drowning behavior, shutdown behavior, and light timing;
- clutch/shifting: engaging/disengaging times, RPM ranges, shift latency, shift smoothing, up/down shift thresholds, and turbo shift factors;
- solver/simulation: solver type, solver rate, simulation stability, engine inertia, engine friction, power, torque, and RPM relationships;
- gearbox: reverse/forward gears, ratios, efficiency, and their effect on acceleration/top speed;
- differentials and axles: differential type, ratio, strength, outputs, axle torque share, handbrake effects, and axle/differential relationships;
- suspension: steering-related suspension behavior, spring/damper values, travel, limits, and contact behavior;
- wheels and tyres: radius, ratio, mass, brake torque, rolling resistance, drag, roughness, friction, and tyre behavior;
- swaybars/aero: body stability and high-speed forces;
- debug: use the wheeled simulation debug route to interpret the result instead of changing unrelated values randomly.

## Terms And Concepts

- Vehicle prefab: the playable vehicle resource that combines model, components, actions, compartments, simulation, damage, fuel, effects, and editor data.
- Vehicle controller: the component family that drives vehicle control behavior. Query exact classes before scripting because generated and handwritten classes both exist.
- Car controller: wheeled vehicle controller specialization. Use it for exact lookup when the task is specifically car/wheeled behavior.
- Compartment: a vehicle occupancy slot or area that a character can enter, occupy, leave, or use for role-specific behavior.
- Compartment manager: the component route for occupancy and compartment logic. Use it for seats, entry/exit, AI vehicle use, and pilot/passenger checks.
- Compartment slot: prefab configuration for where and how a compartment is used; it must line up with action contexts and vehicle model layout.
- Action context: a configured context that lets actions appear and execute at the intended vehicle location.
- Collision geometry: physical interaction geometry; do not treat it as render mesh.
- Fire geometry: geometry used for hit/damage/ballistic interaction.
- Layer preset: the collision/fire setup preset that determines how authored geometry participates in runtime systems.
- Damage manager: vehicle damage behavior surface. Use it for hit zones, armor-like behavior, collision impulse, and damage-state changes.
- Fuel handling: vehicle fuel type, capacity, and consumption behavior.
- Wheeled simulation: the simulation configuration surface for engine, clutch, gearbox, differential, suspension, wheel, tyre, and aero behavior.
- Pacejka: tyre model/tuning family used for wheel-force behavior; adjust with debug feedback.
- Turret addition: vehicle-specific mounting and prefab work; weapon mechanics, animation, and audio remain separate owners.
- Exhaust effects: vehicle effect/particle setup that must be validated in runtime, not just in resource preview.

## Workbench / Resource / Data Surfaces

Use these surfaces for vehicle work:

- Resource Manager: locate vehicle model resources, prefabs, materials, textures, particles, sounds, editor preview textures, and configs.
- Model import and model inspection: validate the imported hierarchy, skeleton, colliders, fire geometry, materials, and texture assignments.
- Prefab Edit Mode: configure vehicle components, inherited prefab values, action managers, action contexts, compartments, slots, damage, fuel, simulation, effects, and turret additions.
- Component property panels: edit controller, compartment manager, damage manager, fuel, simulation, action, and effect fields.
- Action manager/action context surfaces: expose entry/exit/use behavior to the player and AI in the expected place.
- Wheeled simulation configuration: tune driving behavior from controller/input through engine, gearbox, clutch, suspension, wheels, tyres, differentials, and aero.
- Debug/diagnostic surfaces: use vehicle debug, wheeled simulation debug, physics/collision checks, and in-game testing to confirm behavior.
- Editor preview and catalog/config routes: ensure the vehicle appears correctly where the mod intends it to be used, while leaving Game Master/Conflict availability to the game-mode reference.

## Required Workflows

Create a new car or wheeled vehicle:

1. Review the source model against vehicle orientation, scale, part splitting, skeleton, and naming expectations.
2. Split mesh parts by runtime function: body, wheels, doors, glass, lights, damageable parts, and any moving or replaceable pieces.
3. Create collision geometry for physical behavior and fire geometry for damage/ballistic behavior.
4. Apply documented layer presets and material assignments.
5. Rig the mesh to the expected skeleton; verify moving parts and wheel/door relationships.
6. Export FBX with the vehicle workflow settings.
7. Import/register the model and inspect hierarchy, colliders, materials, skeleton, and textures.
8. Create the vehicle prefab and add the basic car configuration.
9. Add actions, action contexts, compartments, and compartment slots.
10. Configure initial wheeled simulation values.
11. Validate entry, driving, collision, damage, fuel, effects, and editor/runtime behavior.

Configure vehicle compartments:

1. Identify the intended roles: driver, passenger, gunner, cargo, AI-only, or special-use positions.
2. Configure the compartment manager/component route on the vehicle prefab.
3. Configure compartment slots in the prefab so each seat/role has a clear target.
4. Configure action contexts near the correct entry/access points.
5. Add or verify available actions for entering, leaving, switching, or using the compartment.
6. Test with a player and, if relevant, AI.
7. Use query output for exact compartment APIs before writing script behavior.

Configure wheeled simulation:

1. Start with controller/input behavior and transmission type.
2. Set engine power, torque, RPM, friction, startup, and shutdown behavior.
3. Configure clutch and shifting so gear changes match intended vehicle class.
4. Configure gearbox ratios and efficiency.
5. Configure differentials, axle torque share, and handbrake behavior.
6. Configure suspension travel, springs, dampers, steering influence, and stability.
7. Configure wheels and tyres: radius, mass, brake torque, rolling resistance, drag, roughness, and friction.
8. Tune aerodynamics and Pacejka-related values after the basic vehicle can drive.
9. Use debug output and test repeatedly; do not compensate for a bad model/collider setup by random simulation changes.

Modify an existing car:

1. Make the prefab/resource changes in a mod-owned override/copy pattern.
2. Identify whether the requested behavior belongs to material, damage, fuel, driving, turret, exhaust, or availability.
3. For material color, change the material/resource surface.
4. For damage, use the damage manager and hit/protection surfaces.
5. For fuel, use fuel type/capacity/consumption surfaces.
6. For driving, use wheeled simulation/controller fields.
7. For turret, wire the vehicle-specific mount and prefab route, then verify weapon/animation/audio owners where needed.
8. For exhaust, update the effect/particle route and test in game.
9. Validate in runtime; inherited prefab changes often look correct in the editor but fail in play if the wrong child/component was edited.

## Configuration Fields And Tables

Asset preparation fields and tables to preserve:

- model orientation and scale expectations;
- object naming conventions for parts;
- split part names and hierarchy;
- collision geometry setup and layer presets;
- fire geometry setup and layer presets;
- skeleton assignment, bone hierarchy, and rigging relationships;
- FBX export settings;
- import/model registration settings;
- material and texture assignment checks.

Prefab configuration fields and tables to preserve:

- base vehicle prefab/resource selection;
- action manager component and action entries;
- action context locations and parameters;
- additional action setup;
- compartment manager/component route;
- compartment definitions;
- compartment slot definitions;
- entry/exit/use action relationships;
- editor-visible component/property setup.

Simulation configuration fields and tables to preserve:

- engine power, torque, RPM, friction, startup, shutdown, drowning, and air intake behavior;
- gearbox reverse/forward gears, ratios, and efficiency;
- clutch max torque and engage/disengage timing;
- shifting smoothing, latency, thresholds, and turbo factors;
- suspension steering, spring, damper, travel, and limit behavior;
- wheel radius, ratio, mass, brake torque, and position;
- tyre rolling resistance, drag, roughness, friction, and tread-related behavior;
- differential type, ratio, strength, output mapping, and torque share;
- axle configuration and handbrake effect;
- swaybar and aerodynamic behavior;
- Pacejka/debug values.

Car modding fields and tables to preserve:

- inherited prefab/resource structure;
- material base color and multi material usage;
- component overview for deciding where the requested behavior belongs;
- damage manager values, armor/protection values, and collision impulse behavior;
- fuel type, fuel tank capacity, and fuel consumption;
- driving characteristics and engine parameter changes;
- turret prefab/component routes;
- exhaust effect/particle references;
- in-game testing checklist.

Wheeled simulation field guide:

- `SCR_CarControllerComponent` is a key lookup route for car control behavior.
- Controller tables are not optional background; use them to avoid changing the wrong field family.
- Engine, clutch, gearbox, differential, axle, suspension, wheel, and tyre fields interact. Change one family at a time and verify.
- Generated controller classes are useful for exact class shape; handwritten `GameCode/Vehicle` files are better for behavior examples.

## Procedures And Ordered Steps

Vehicle asset preparation procedure:

1. Confirm model orientation and part naming.
2. Split vehicle body and moving/damageable parts.
3. Build collision geometry.
4. Build fire geometry.
5. Apply layer presets.
6. Set skeleton and rigging.
7. Export FBX.
8. Import/register model.
9. Check colliders/materials.
10. Check skeleton/hierarchy.
11. Import and verify textures.

Vehicle prefab procedure:

1. Create the new vehicle prefab from the imported model.
2. Add the basic car/vehicle configuration.
3. Add an action manager.
4. Create entry/use action contexts.
5. Add additional actions after the base actions work.
6. Add and configure compartments.
7. Add new compartment slots.
8. Test entry/exit/seat behavior.

Vehicle simulation procedure:

1. Configure controller/transmission input behavior.
2. Configure engine values.
3. Configure gearbox and clutch.
4. Configure suspension.
5. Configure wheels, wheel positions, and tyres.
6. Configure differential and torque share.
7. Configure aerodynamics.
8. Tune Pacejka-related behavior.
9. Use debug output and runtime tests to adjust.

Vehicle modding procedure:

1. Prepare the existing prefab/resource for modded changes.
2. Change material/base color only on the material route.
3. Change damage behavior through damage manager and hit/protection surfaces.
4. Change fuel behavior through fuel handling fields.
5. Change driving behavior through wheeled simulation/controller fields.
6. Add turret through vehicle-specific prefab/component routes.
7. Change exhaust effects through effect/particle references.
8. Test results in game.

## Warnings And Failure Modes

- Do not guess Reforger vehicle APIs. Query exact symbols and examples before writing API-sensitive vehicle code.
- `files Vehicle` is broad and noisy. Prefer targeted routes such as `lookup "vehicle compartment"`, `files VehicleControllerComponent`, `files BaseCompartmentManagerComponent`, and `files SCR_CarControllerComponent`.
- Generated files are strongest for exact class truth; handwritten `GameCode/Vehicle` files are stronger for implementation patterns.
- A vehicle can look correct in the model editor but still fail if collision geometry, fire geometry, layers, skeleton, or hierarchy do not match prefab expectations.
- Do not use render mesh as a substitute for collision/fire geometry.
- Wrong layer presets can break collision, hit behavior, or physical interaction.
- Compartment slots, action contexts, and available actions must agree. If entry actions appear in the wrong place or do nothing, inspect all three surfaces.
- Vehicle compartment script lookup does not prove prefab configuration. Always verify seats/compartments/actions in Workbench and runtime.
- Wheeled simulation fields are coupled. Random changes to tyres, torque, differential, or suspension can mask the real defect.
- Do not solve bad driving by only changing engine power; inspect mass, wheels, tyres, differentials, suspension, gear ratios, and collision setup.
- Fuel behavior can involve type, capacity, consumption, and component setup; changing only one field may not produce the intended behavior.
- Damage behavior can involve hit zones, fire geometry, armor/protection, damage manager, and collision impulse.
- Turret additions cross into weapon, animation, and audio systems. This reference owns vehicle mounting/configuration, not full turret weapon behavior.
- Exhaust changes depend on effect/particle resources and runtime validation.
- Prefab inheritance can hide the edited value. Confirm whether the change is on the active inherited child/component.
- Vehicle behavior must be tested in play mode; editor property values are not sufficient proof.
- Multiplayer or dedicated-server vehicle behavior needs runtime/server verification when ownership, replication, or authority matters.

## API Lookup Keys

Use these lookup keys before writing or changing vehicle code:

- Vehicle/control classes: `Vehicle`, `VehicleClass`, `BaseVehicle`, `VehicleControllerComponent`, `VehicleControllerComponentClass`, `BaseVehicleControllerComponent`, `CarControllerComponent`, `CarControllerComponent_B`, `SCR_CarControllerComponent`, `SCR_CarControllerComponent_B`.
- Compartment classes: `BaseCompartmentManagerComponent`, `BaseCompartmentManagerComponentClass`, `SCR_BaseCompartmentManagerComponent`, `SCR_BaseCompartmentManagerComponentClass`.
- Vehicle damage/debug classes: `SCR_VehicleDamageManagerComponent`, `SCR_VehicleDamageManagerComponentClass`, `SCR_VehicleDebug`, `SCR_VehicleDebugClass`.
- Action/condition routes: `SCR_VehicleLightsCondition`, `SCR_VehicleControllerTypeCondition`, `SCR_VehicleEngineOnCondition`, `SCR_VehicleHasAnyGroundContactCondition`.
- Related routes to verify when needed: `BaseLightManagerComponent`, `LightManagerComponent`, `Compartment`, `CompartmentManagerComponent`, `DamageManagerComponent`, `HitZone`, `Pilot`, `Wheeled`.

## Game-Data Query Commands

Run exact or targeted queries before writing API-sensitive vehicle code:

```powershell
py -3 scripts/query-reforger-data.py lookup "vehicle compartment" --limit 8
py -3 scripts/query-reforger-data.py examples vehicle --subtopic compartment --limit 8
py -3 scripts/query-reforger-data.py examples vehicle --subtopic vehicle-component --limit 8
py -3 scripts/query-reforger-data.py files Vehicle --limit 8
py -3 scripts/query-reforger-data.py files BaseCompartmentManagerComponent --limit 8
py -3 scripts/query-reforger-data.py files VehicleControllerComponent --limit 8
py -3 scripts/query-reforger-data.py files SCR_CarControllerComponent --limit 8
```

Use exact symbols when class shape matters:

```powershell
py -3 scripts/query-reforger-data.py symbol VehicleControllerComponent --kind class --exact
py -3 scripts/query-reforger-data.py symbol BaseCompartmentManagerComponent --kind class --exact
py -3 scripts/query-reforger-data.py symbol CarControllerComponent --kind class --exact
py -3 scripts/query-reforger-data.py symbol SCR_CarControllerComponent --kind class --exact
```

Use snippets only after a targeted result identifies a useful file:

```powershell
py -3 scripts/query-reforger-data.py snippet scripts/GameCode/Vehicle/VehicleControllerComponent.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/GameCode/Vehicle/SCR_BaseCompartmentManagerComponent.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/GameCode/Vehicle/SCR_CarControllerComponent.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/Game/Vehicle/SCR_VehicleDebug.c --line 1 --context 30
```

Prefer this order for Codex vehicle tasks:

1. Read this reference for workflow and boundaries.
2. Run `lookup "vehicle compartment"` for a bounded task bundle.
3. Run targeted `files` or `examples` commands for the exact symbol/family.
4. Open bounded snippets for the selected handwritten examples.
5. Verify prefab/component/action/simulation behavior in Workbench and runtime.

## Examples And Samples

Official samples:

- `SampleMod_NewCar`: use as the primary layout signal for a new vehicle addon. Review its vehicle asset, config, prefab, script, sound, UI/editor preview, and resource organization when building a new car-like sample.
- `SampleMod_ModdedCar`: use as the primary layout signal for modifying an existing vehicle. Review its wheeled vehicle asset/prefab/config/editor preview/particle/sound organization and turret-related prefab routes when changing an existing car.

Game-source example routes from query output:

- `scripts/GameCode/Vehicle/VehicleControllerComponent.c`: handwritten vehicle controller behavior and component pattern route.
- `scripts/GameCode/Vehicle/SCR_BaseCompartmentManagerComponent.c`: handwritten compartment manager route.
- `scripts/GameCode/Vehicle/Vehicle.c`: handwritten base vehicle route.
- `scripts/GameCode/Vehicle/SCR_CarControllerComponent.c`: car controller route.
- `scripts/Game/Vehicle/SCR_VehicleDebug.c`: vehicle debug route.
- `scripts/Game/Components/Damage/SCR_VehicleDamageManagerComponent.c`: vehicle damage manager route.
- `scripts/Game/UI/HUD/AvailableActions/Conditions/Game/Vehicle/SCR_VehicleLightsCondition.c`: available-action condition route for vehicle lights.
- `scripts/Game/UI/HUD/AvailableActions/Conditions/Game/Vehicle/SCR_VehicleControllerTypeCondition.c`: vehicle controller type condition route.
- `scripts/Game/UI/HUD/AvailableActions/Conditions/Game/Vehicle/SCR_VehicleEngineOnCondition.c`: engine-on condition route.
- AI vehicle compartment examples surfaced through `SCR_AIUtils`, `SCR_AIChangeCompartment`, `SCR_AIFindAvailableVehicle`, and `SCR_AIGetEmptyCompartment` are useful when the task includes AI seat/compartment behavior.

Example selection rules:

- Prefer official samples for project/resource layout.
- Prefer wiki workflows for Workbench order, field families, and authoring surfaces.
- Prefer generated game files for exact class names and inheritance.
- Prefer handwritten game files for behavior patterns and examples.
- Do not copy source bodies into a reference or answer; use bounded snippets when implementation context is needed.

## Follow-Up Keywords

Search or route with these keywords when the task gets more specific:

- `vehicle compartment`
- `BaseCompartmentManagerComponent`
- `SCR_BaseCompartmentManagerComponent`
- `VehicleControllerComponent`
- `SCR_CarControllerComponent`
- `CarControllerComponent`
- `VehicleWheeledSimulation`
- `wheeled simulation`
- `compartment slot`
- `action context`
- `ActionsManagerComponent`
- `vehicle damage manager`
- `SCR_VehicleDamageManagerComponent`
- `fuel handling`
- `vehicle fuel consumption`
- `vehicle turret`
- `vehicle exhaust`
- `vehicle collision geometry`
- `fire geometry`
- `layer preset`
- `Pacejka`
- `differential`
- `torque share`
- `suspension`
- `tyre friction`
- `vehicle debug`
- `SampleMod_NewCar`
- `SampleMod_ModdedCar`

## Verification

Workbench/resource validation:

- Confirm imported model hierarchy, part names, skeleton, colliders, fire geometry, materials, and textures.
- Confirm collision and fire geometry use the intended layer presets.
- Confirm the vehicle prefab resolves inherited values on the active child/component.
- Confirm action manager entries and action contexts are visible and placed correctly.
- Confirm compartments and compartment slots map to intended seats/roles.
- Confirm editor previews/config/catalog routes only if the task needs placement or selection.

Runtime validation:

- Spawn the vehicle and verify enter/exit, driver/passenger/gunner roles, action visibility, seat occupancy, and compartment switching.
- Drive the vehicle and verify steering, acceleration, braking, shifting, suspension, wheel contact, and stability.
- Use simulation/debug surfaces to inspect wheeled behavior while tuning.
- Damage the vehicle and verify hit behavior, fire geometry, protection, collision impulse, and damage states.
- Verify fuel type, capacity, and consumption over time.
- Verify turret mount/control only after the base vehicle functions.
- Verify exhaust/effect changes in play mode.

Script/API validation:

- Run exact game-data queries before coding against vehicle, controller, compartment, damage, or condition classes.
- Use snippets only for the selected implementation file.
- If the task involves replication, authority, or server behavior, route to `multiplayer-replication-and-authority.md` and `server-hosting-startup-and-runtime.md` for final checks.

## Official Wiki Links

- Car Creation: https://community.bistudio.com/wiki/Arma_Reforger:Car_Creation
- Car Creation/Asset Preparation: https://community.bistudio.com/wiki/Arma_Reforger:Car_Creation/Asset_Preparation
- Car Creation/Prefab Configuration: https://community.bistudio.com/wiki/Arma_Reforger:Car_Creation/Prefab_Configuration
- Car Creation/Simulation Configuration: https://community.bistudio.com/wiki/Arma_Reforger:Car_Creation/Simulation_Configuration
- Car Modding: https://community.bistudio.com/wiki/Arma_Reforger:Car_Modding
- Vehicle: Wheeled Simulation: https://community.bistudio.com/wiki/Arma_Reforger:Vehicle:_Wheeled_Simulation

## Usefulness Score

Score: `93/100`

- Wiki coverage: `29/30`
  - All six owned primary vehicle pages are reviewed and represented.
  - The reference preserves asset preparation, prefab configuration, simulation configuration, car modding, and wheeled simulation field families.
  - Tables, procedures, warnings, code/config examples, media, and links were reviewed; field-heavy data is represented as compact parameter families instead of copied tables.
  - Missed coverage: exact screenshot-dependent UI visuals are not embedded; impact is low because editor surfaces and official URLs are present.
- Operational detail: `14/15`
  - Vehicle workflows are ordered from asset preparation through prefab, compartments, simulation, modding, and validation.
  - Dense wheeled-simulation fields are grouped by behavior family to keep them usable without becoming a table dump.
- API lookup usefulness: `15/15`
  - Exact lookup keys and commands are provided for vehicle controllers, car controllers, compartment managers, examples, files, and snippets.
- Example grounding: `9/10`
  - Official car samples and game-source example families are named with routing guidance.
  - No source bodies are copied; snippets are query-routed.
- Codex task usefulness: `14/15`
  - Supports common tasks: create a car, configure compartments, tune simulation, modify fuel/damage/driving, add turret/exhaust routes, and find exact APIs.
  - Broad vehicle availability in Game Master/Conflict is intentionally cross-linked.
- Context efficiency: `8/10`
  - The reference is dense and navigable, with explicit boundaries to avoid duplicate ownership.
  - It remains longer than a utility reference because the owned wiki source family is workflow-heavy.
- Verification guidance: `4/5`
  - Workbench, runtime, simulation/debug, damage/fuel, and script/API checks are present.
  - Dedicated-server/multiplayer checks are routed rather than duplicated.

Category-fit check:
- Source family complete: pass. Car Creation, all car subpages, Car Modding, and Vehicle Wheeled Simulation are covered.
- No owned page missing: pass.
- Split boundary justified: pass. Generic assets, generic prefabs, lifecycle, animation, audio, Game Master/Conflict, multiplayer, and server runtime are routed to owning references.
- Cross-links present: pass.
- Task route clear: pass. A vehicle compartment task routes to this reference plus `lookup "vehicle compartment"` and targeted compartment/controller queries.
- Automatic failure conditions: none found.
