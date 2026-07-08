# Entities, Components, And Lifecycle

## When To Read

Read this reference when the task is about generic Reforger entity/component behavior: entity lifecycle, lifecycle callback order, event masks, frame events, entity activeness, creating an entity class, creating a component class, making entities/components visible in Workbench, wiring components onto entities, using `FindComponent`, or setting up action contexts on an interactable entity.

Do not use this as the primary owner for script style, prefab/config data modeling, replication/authority, or domain-specific component behavior. Script implementation patterns live in `script-events-actions-and-patterns.md`. Prefab/config storage and overrides live in `prefabs-configs-containers-and-catalogs.md`. Multiplayer semantics live in `multiplayer-replication-and-authority.md`. Weapon, vehicle, audio, UI, AI, terrain, scenario, and Game Master component details belong to their own references.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: entity lifecycle, entity activeness, entity creation, component creation, action context setup, generic component wiring, and generic component-configuration warnings.
- Secondary/cross-reference topics: script coding patterns, prefab/config data modeling, replication, user-action scripting, domain-specific components, and Resource Manager editor surfaces.

Wiki pages reviewed:
- Entity Lifecycle - https://community.bistudio.com/wiki/Arma_Reforger:Entity_Lifecycle - status: covered - reason: owns lifecycle definitions, lifecycle callback order, event-method requirements, event-mask behavior, and example-code lessons.
- Entity Activeness - https://community.bistudio.com/wiki/Arma_Reforger:Entity_Activeness - status: covered - reason: owns active flag behavior, frame-event behavior, pre-0.9.8 note, good practices, and examples.
- Create an Entity - https://community.bistudio.com/wiki/Arma_Reforger:Create_an_Entity - status: covered - reason: owns generic entity class declaration, entity class companion declaration, `EntityEditorProps`, editable properties, uniqueness pattern, and Workbench visibility requirements.
- Create a Component - https://community.bistudio.com/wiki/Arma_Reforger:Create_a_Component - status: covered - reason: owns generic component declaration, component class companion declaration, `ComponentEditorProps`, properties, code, and Workbench visibility requirements.
- Action Context Setup - https://community.bistudio.com/wiki/Arma_Reforger:Action_Context_Setup - status: covered - reason: owns generic entity/action context wiring, required physical representation, context identity, action locations, parameters, and setup caveats.
- BaseDoorComponent - https://community.bistudio.com/wiki/Arma_Reforger:BaseDoorComponent - status: partial - reason: included only as a generic component-configuration warning example for axis, smoothing, and migrated data; full door/domain behavior is not owned here.

Wiki sections covered:
- Entity Lifecycle > Definitions, Lifecycle, Example Code - coverage: represented as lifecycle order, event prerequisites, event masks, and callback validation rules.
- Entity Activeness > Active Flag and Frame Events, Pre-0.9.8 Behaviour, Good Practices, Examples - coverage: represented as active/frame-event behavior and good-practice checks.
- Create an Entity > Declaration, Entity, Entity Class, `EntityEditorProps`, Filling, Add Code, Add Properties, Make It Unique, Final Code - coverage: represented as entity creation workflow and Workbench validation.
- Create a Component > Declaration, Component, Component Class, `ComponentEditorProps`, Filling, Add Code, Add Properties, Final Code - coverage: represented as component creation workflow and Workbench validation.
- Action Context Setup > Select Entity, Define Context, Add Action Location, Add Action, Add Parameters, Walkthrough Script Setup, Walkthrough World/Entity Setup - coverage: represented as generic action-context wiring and validation.
- BaseDoorComponent > Door Width Axis, Removed Angles from Sliding Doors, Smoothing Animations - coverage: represented as component-data warning examples, not door-system ownership.

Structured wiki records:
- Tables reviewed/included: Entity Lifecycle lifecycle table; Entity Activeness good-practice examples table.
- Procedures reviewed/included: entity declaration and editor visibility; component declaration and editor visibility; adding entity/component properties; uniqueness workflow; action-context setup; action location/action/parameter workflow; lifecycle/event-mask verification; active/frame-event validation.
- Admonitions reviewed/included: entity/component scripts must be created in the Game module to appear in Workbench lists; entity/component class companion names must exactly match the base name plus `Class`; scripts must be compiled/reloaded for editor visibility; event callbacks require event masks or specific conditions; active flag should be used for entities moved every frame without components using frame events; action contexts require valid physical representation; synchronized user actions require `RplComponent`; `ActionsManagerComponent` is not a substitute; BaseDoorComponent axis and migrated distance data warnings.
- Code blocks reviewed/included: lifecycle example, entity creation example, component creation example, action context example, and BaseDoorComponent examples were reviewed for workflow behavior. Full source bodies are not copied.
- Media reviewed: editor screenshots and diagrams were treated as setup confirmation only; this runtime reference preserves the operational steps and field meanings.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts\query-reforger-data.py symbol IEntity --kind class --exact`
  - `py -3 scripts\query-reforger-data.py method IEntity FindComponent --exact`
  - `py -3 scripts\query-reforger-data.py symbol GenericEntity --kind class --exact`
  - `py -3 scripts\query-reforger-data.py symbol GenericComponent --kind class --exact`
  - `py -3 scripts\query-reforger-data.py symbol ScriptComponent --kind class --exact`
  - `py -3 scripts\query-reforger-data.py symbol ScriptComponentClass --kind class --exact`
  - `py -3 scripts\query-reforger-data.py examples component --subtopic lifecycle --limit 8`
  - `py -3 scripts\query-reforger-data.py examples component --subtopic game-component --limit 8`
- Symbols/methods/attributes verified as lookup routes: `IEntity`, `IEntity.FindComponent`, `GenericEntity`, `GenericComponent`, `ScriptComponent`, `ScriptComponentClass`, `GenericComponentClass`, `EntityEditorProps`, `ComponentEditorProps`, `EOnInit`, `EOnFrame`, `OnPostInit`, `EventMask`, `RplComponent`.
- Examples/snippets reviewed: lifecycle and game-component query output including `SCR_AISettingsComponent`, `SCR_CacheNoteComponent`, `SCR_CallsignBaseComponent`, `SCR_CampaignServiceCompositionComponent`, `SCR_CampaignServiceEntityComponent`, `SCR_MineAwarenessComponent`, `SCR_ArmoryComponent`, `SCR_BaseLockComponent`, and `SCR_HybridPhysicsComponent`.

Samples and source examples:
- Official sample folders reviewed: `SampleMod_ModdedScript`, `SampleMod_Main`, `SampleMod_NewCar`, `SampleMod_ModdedCar`, `SampleMod_NewCharacter`, `SampleMod_NewFaction`, and `SampleMod_ModdedWeapon` as entity/component/prefab wiring layout signals only.
- Raw game-source example families reviewed through query output: script components, game components, lifecycle examples, frame-event examples, `FindComponent` usage, and component class declarations.

Coverage gaps:
- Missing, excluded, or intentionally deferred source: full user-action scripting, replication/authority, prefab inheritance/override rules, weapon/vehicle/audio/UI/AI-specific component fields, and full BaseDoorComponent domain behavior.
- Reason and impact: those are source-heavy workflows with separate reference owners. This reference keeps generic lifecycle and component wiring so Codex can route to the correct domain reference before changing specialized behavior.

## Wiki Source Coverage

Entity Lifecycle is the authority for when entity and component callbacks run. Treat lifecycle order and event-mask rules as correctness constraints, not style preferences. A callback appearing in example code does not mean it will run automatically in every context; some events require explicit event masks and some require engine-side conditions such as valid, active physics.

Lifecycle concepts:
- Entity and component construction is separate from later runtime callback behavior.
- `ScriptComponent` instances are created as part of the owning entity setup and receive component lifecycle events.
- Event callbacks are not all unconditional. Some require event masks set through `IEntity.SetEventMask` or component event-mask APIs.
- Some events require additional conditions, such as physics events requiring valid and activated physics.
- Lifecycle example code should be used to understand order and prerequisites, then exact APIs must be checked through query commands.

Lifecycle table expectations:
- Preserve callback order when writing or reviewing lifecycle-sensitive code.
- Decide whether initialization belongs in entity construction, component insertion, `EOnInit`, `OnPostInit`, or a later event based on dependencies.
- Do not assume another component is available before the lifecycle point where components are inserted and initialized.
- Do not use frame events without confirming the entity/component is active and has the required event mask.
- Do not use physics-active callbacks without confirming the entity has valid activated physics.

Entity Activeness owns frame-update behavior:
- The active flag and frame events are linked. Entities moved every frame but not using components with frame events should have the active flag set.
- Components using frame events can affect whether the owning entity needs active handling.
- Pre-0.9.8 behavior is documented as historical behavior; do not infer current behavior from it without checking current sources.
- Good practice is to avoid keeping entities active or receiving frame events unless the behavior actually requires it.
- Activeness should be validated in runtime, not only by code inspection.

Create an Entity owns generic entity setup:
- The entity script file must be in the Game module path expected by Workbench, otherwise it will not appear in the Entities list.
- Entity class names conventionally end with the `Entity` suffix.
- A companion entity class declaration is required for Workbench visibility.
- The companion class name must be exactly the entity name plus the `Class` suffix.
- `EntityEditorProps` controls how the entity appears in Workbench.
- After adding or changing the entity class, scripts must be compiled/reloaded before expecting the entity to appear in Workbench.
- Editable properties need appropriate attributes and should be validated in the editor after compile/reload.
- The wiki uniqueness example warns when more than one instance is placed; uniqueness is a behavior decision, not a default entity requirement.

Create a Component owns generic component setup:
- The component script file must be in the Game module path expected by Workbench, otherwise it will not appear in the Components list.
- Component class names conventionally end with the `Component` suffix.
- A companion component class declaration is required for Workbench visibility.
- The companion class name must be exactly the component name plus the `Class` suffix.
- `ComponentEditorProps` controls how the component appears in Workbench.
- After adding or changing the component class, scripts must be compiled and reloaded before expecting the component to appear in Workbench.
- A component cannot exist without an owning entity, so null-owner conditions usually indicate a deeper setup problem.
- Editable properties need attributes and category/description/default-value decisions that match the intended editor surface.
- Query exact class inheritance and method names before writing component code.

Action Context Setup owns generic action-context wiring:
- Select an entity that has valid physical representation so interaction can resolve correctly.
- Define a context with a unique context name used to register child actions.
- Fill the position field with valid `PointInfo` or derived data.
- The component `UIInfo` is required.
- Add action locations separately for contextual and general actions.
- Add action definitions separately for contextual and general actions.
- Add parameters where the action requires them.
- For user actions to synchronize and work as intended, the entity requires `RplComponent`; `ActionsManagerComponent` is not a substitute.
- Replication semantics are still owned by `multiplayer-replication-and-authority.md`; this reference only records the generic setup caveat.

BaseDoorComponent is included as a generic component-configuration warning:
- Door width axis is important for collision checks on sliding and rotating doors.
- Old sliding-door angle data must be migrated to distance parameters or warnings can occur.
- Smoothing animation values describe curve slopes at animation start and end.
- Full door setup, vehicle/building interaction, animation, and collision behavior are domain topics, not generic lifecycle ownership.

## Terms And Concepts

- `IEntity`: generated base entity API route. Query exact methods before use.
- `GenericEntity`: generated base entity class route.
- `GenericComponent`: generated base component route.
- `ScriptComponent`: parent class for script-created components.
- `ScriptComponentClass`: companion class route for script component editor visibility.
- Entity class: script class representing an entity type.
- Entity class companion: `EntityNameClass` declaration needed for Workbench/editor visibility.
- Component class: script class representing a component type.
- Component class companion: `ComponentNameClass` declaration needed for Workbench/editor visibility.
- Lifecycle callback: engine-called method at a specific entity/component lifecycle point.
- Event mask: opt-in mask that enables specific event callbacks.
- Active flag: entity state used for frame-update behavior when needed.
- Frame event: per-frame callback path; should be used deliberately.
- `FindComponent`: entity API route for finding a component by type.
- Action context: named context used to register child actions on an entity.
- Action location: placement/context data for where an action can be used.
- `RplComponent`: replication component needed for synchronized user actions; exact multiplayer behavior is owned elsewhere.

## Workbench / Resource / Data Surfaces

Primary surfaces:
- Entity script and companion entity class declaration.
- Component script and companion component class declaration.
- Workbench Entities list and Components list.
- `EntityEditorProps` and `ComponentEditorProps` metadata.
- Editable property attributes for editor-visible values.
- Entity prefab/component placement surfaces where the entity or component is attached.
- Lifecycle callback code paths.
- Event mask setup.
- Action context data, action locations, actions, and parameters.

Cross-reference surfaces:
- Prefab storage, prefab inheritance, component prefab files, and config object storage belong to `prefabs-configs-containers-and-catalogs.md`.
- Script syntax, class templates, logging patterns, invokers, and user-action script implementation belong to `script-events-actions-and-patterns.md`.
- Resource Manager editor operations belong to `resource-manager-file-types-and-editors.md`.
- Replication, authority, proxies, owners, and RPC behavior belong to `multiplayer-replication-and-authority.md`.
- Domain component fields belong to domain references, such as weapons, vehicles, audio, UI, AI, terrain, scenario, and Game Master.

## Required Workflows

Create a generic entity:
1. Confirm the task needs a new entity type, not only a component on an existing entity.
2. Create the entity script in the Game module path expected by Workbench.
3. Name the class with an `Entity` suffix.
4. Create the companion `EntityClass` declaration with the exact entity name plus `Class`.
5. Add `EntityEditorProps` metadata so Workbench can list it.
6. Add editor-visible properties only when needed.
7. Compile and reload scripts.
8. Confirm the entity appears in Workbench.
9. Place or instantiate it in the correct editor/prefab context.
10. Validate lifecycle behavior at runtime.

Create a generic component:
1. Confirm the behavior belongs in a component rather than a standalone entity or domain-specific system.
2. Create the component script in the Game module path expected by Workbench.
3. Name the class with a `Component` suffix.
4. Create the companion `ComponentClass` declaration with the exact component name plus `Class`.
5. Add `ComponentEditorProps` metadata so Workbench can list it.
6. Add attributes for editor-visible properties.
7. Compile and reload scripts.
8. Confirm the component appears in the Components list.
9. Attach the component to an entity or prefab.
10. Validate owner, lifecycle, and event-mask behavior at runtime.

Choose lifecycle placement:
1. Identify what data or other components the code needs.
2. Use earlier lifecycle hooks only for work that has no dependency on later initialization.
3. Use `OnPostInit` or later lifecycle points when other components or entity state must exist.
4. Set event masks only for callbacks that are actually needed.
5. Check physics/event prerequisites before using physics-related callbacks.
6. Use frame events only when continuous updates are required.
7. Validate callback order with targeted runtime logging or Workbench/runtime checks.

Use entity activeness safely:
1. Identify whether the entity itself moves every frame or whether a component handles frame updates.
2. Set active behavior when an entity moves every frame without a component frame-event path.
3. Avoid active/frame-event use for static or event-driven behavior.
4. Re-check activeness after component changes.
5. Validate runtime behavior and performance impact.

Wire a component to an entity:
1. Confirm the component is visible in Workbench after compile/reload.
2. Attach it to the intended entity/prefab.
3. Fill required properties.
4. Confirm the owner entity is valid.
5. Use `FindComponent` only after the lifecycle point where the target component should exist.
6. Query exact `FindComponent` signature before writing code.
7. Validate in Workbench and runtime.

Set up an action context:
1. Select an entity with valid physical representation.
2. Define a unique context name.
3. Fill required position data with valid `PointInfo` or derived data.
4. Ensure component `UIInfo` is present.
5. Add action locations for contextual or general actions.
6. Add contextual or general actions.
7. Add action parameters as needed.
8. Add `RplComponent` when actions must synchronize.
9. Route action script behavior to `script-events-actions-and-patterns.md` and replication behavior to `multiplayer-replication-and-authority.md`.

Use BaseDoorComponent as a component-data warning pattern:
1. Treat axis-like fields as behavior-critical when collision or animation depends on them.
2. Update migrated/deprecated data fields when the wiki notes changed parameters.
3. Validate logs after changing component data.
4. Route full door-specific behavior to the appropriate domain reference when it exists.

## Configuration Fields And Tables

Entity Lifecycle table:
- Treat the lifecycle table as the ordering source for callback timing.
- Preserve event-method prerequisites when writing code.
- Note that some event methods require `IEntity.SetEventMask` or related event-mask setup.
- Note that some event methods require engine state such as valid and active physics.
- Use the example code for order and behavior lessons, not as an API dump.

Entity Activeness table:
- Good-practice examples distinguish when an entity should be active and when component frame events are enough.
- Active flag is relevant for entities moved every frame without frame-event components.
- Pre-0.9.8 behavior is historical and should not be used as current behavior without verification.

Entity creation fields:
- Entity script location must be in the Game module path expected by Workbench.
- Entity class name should end in `Entity`.
- Companion class name must be entity name plus `Class`.
- `EntityEditorProps` makes the entity visible/configurable in Workbench.
- Editable property attributes control editor-visible values.
- Compile/reload is required before Workbench visibility checks.

Component creation fields:
- Component script location must be in the Game module path expected by Workbench.
- Component class name should end in `Component`.
- Companion class name must be component name plus `Class`.
- `ComponentEditorProps` makes the component visible/configurable in Workbench.
- Editable property attributes control editor-visible values.
- Compile/reload is required before Workbench visibility checks.

Action context fields:
- Context name is a unique identifier used to register child actions.
- Position must be valid `PointInfo` or derived data.
- Component `UIInfo` is required.
- Entity physical representation is required for proper interaction.
- `RplComponent` is required for synchronized actions to work as intended.

BaseDoorComponent warning fields:
- Door width axis affects collision checks for sliding and rotating doors.
- Sliding-door data should use new distance parameters where the wiki notes angle removal.
- Smoothing animation values define curve slope at animation start and end.

## Procedures And Ordered Steps

To check why an entity does not appear in Workbench:
1. Confirm the script is in the expected Game module location.
2. Confirm the entity class name ends with `Entity`.
3. Confirm the companion class exists.
4. Confirm the companion class name is exactly entity name plus `Class`.
5. Confirm `EntityEditorProps` metadata exists.
6. Compile and reload scripts.
7. Reopen or refresh the relevant Workbench list.

To check why a component does not appear in Workbench:
1. Confirm the script is in the expected Game module location.
2. Confirm the component class name ends with `Component`.
3. Confirm the companion class exists.
4. Confirm the companion class name is exactly component name plus `Class`.
5. Confirm `ComponentEditorProps` metadata exists.
6. Compile and reload scripts.
7. Reopen or refresh the Components list.

To debug a lifecycle callback that does not run:
1. Confirm the object exists and is attached in the expected context.
2. Confirm the callback is valid for entity vs component.
3. Check whether the callback requires an event mask.
4. Check whether the callback requires physics or another engine condition.
5. Confirm the entity/component is active if frame behavior is expected.
6. Add targeted temporary logging at lifecycle points if project practice allows.
7. Verify with runtime behavior, not only code inspection.

To debug `FindComponent` failure:
1. Query exact `IEntity.FindComponent` signature.
2. Confirm the searched component type is correct.
3. Confirm the component is attached to the same entity.
4. Confirm lookup happens after the lifecycle point when components are available.
5. Confirm the component exists in the actual prefab/placed entity, not only in a different prefab variant.
6. Validate with a bounded raw snippet or runtime check.

To debug action context setup:
1. Confirm the selected entity has valid physical representation.
2. Confirm the context name is unique and used consistently.
3. Confirm position data is valid.
4. Confirm component `UIInfo` exists.
5. Confirm action location and action definitions exist for the intended action kind.
6. Confirm action parameters are filled.
7. Confirm `RplComponent` exists when synchronized behavior is expected.
8. Route any authority/replication issue to the multiplayer reference.

## Warnings And Failure Modes

- Do not write lifecycle-sensitive code before checking lifecycle order.
- Do not assume callbacks run without event-mask setup.
- Do not assume frame events are free. Use them only when continuous updates are required.
- Do not keep entities active unnecessarily.
- Do not use historical pre-0.9.8 activeness behavior as current behavior.
- Do not place entity or component scripts outside the module path expected by Workbench if they must appear in editor lists.
- Do not omit the companion `EntityClass` or `ComponentClass`.
- Do not mismatch companion class names; the name must be the base class name plus `Class`.
- Do not expect Workbench lists to update before compiling/reloading scripts.
- Do not treat a null component owner as normal; a component cannot exist without an entity.
- Do not call `FindComponent` before the target component should exist in lifecycle order.
- Do not use action contexts on entities without valid physical representation.
- Do not expect synchronized user actions to work without `RplComponent`.
- Do not treat `ActionsManagerComponent` as a replacement for `RplComponent`.
- Do not make domain-specific changes from this generic reference alone.

## API Lookup Keys

Use these lookup keys when entity/component lifecycle work touches code:
- Entity classes and APIs: `IEntity`, `GenericEntity`, `IEntity.FindComponent`, `IEntity.SetEventMask`.
- Component classes and APIs: `GenericComponent`, `GenericComponentClass`, `ScriptComponent`, `ScriptComponentClass`.
- Lifecycle/event routes: `EOnInit`, `EOnFrame`, `OnPostInit`, `OnComponentInsert`, `EventMask`, `SetEventMask`.
- Editor metadata: `EntityEditorProps`, `ComponentEditorProps`, `Attribute`.
- Action context routes: `PointInfo`, `UIInfo`, `ActionsManagerComponent`, `RplComponent`.
- Example families: lifecycle components, game components, frame-event components, component owner access, `FindComponent` examples.

Do not assume method signatures or inheritance from these names. Query exact symbols, methods, examples, and snippets before writing code.

## Game-Data Query Commands

Use exact API lookup for entity/component anchors:

```powershell
py -3 scripts\query-reforger-data.py symbol IEntity --kind class --exact
py -3 scripts\query-reforger-data.py method IEntity FindComponent --exact
py -3 scripts\query-reforger-data.py symbol GenericEntity --kind class --exact
py -3 scripts\query-reforger-data.py symbol GenericComponent --kind class --exact
py -3 scripts\query-reforger-data.py symbol ScriptComponent --kind class --exact
py -3 scripts\query-reforger-data.py symbol ScriptComponentClass --kind class --exact
```

Use examples for lifecycle and generic game-component patterns:

```powershell
py -3 scripts\query-reforger-data.py examples component --subtopic lifecycle --limit 8
py -3 scripts\query-reforger-data.py examples component --subtopic game-component --limit 8
py -3 scripts\query-reforger-data.py files EventMask --limit 10
py -3 scripts\query-reforger-data.py files EntityEditorProps --limit 10
py -3 scripts\query-reforger-data.py files ComponentEditorProps --limit 10
```

Use snippets only after a query result gives an exact file and line:

```powershell
py -3 scripts\query-reforger-data.py snippet scripts/Game/Callsign/SCR_CallsignBaseComponent.c --line 1 --context 30
py -3 scripts\query-reforger-data.py snippet scripts/Game/Components/HybridPhysicsComponent.c --line 1 --context 30
py -3 scripts\query-reforger-data.py snippet scripts/Core/generated/Entities/IEntity.c --line 524 --context 30
```

If a query is broad, narrow by exact symbol, owner, topic, subtopic, generated-only, or handwritten-only before opening snippets.

## Examples And Samples

Use examples as layout and pattern evidence:
- Lifecycle examples from query output show `ScriptComponent`, `ScriptComponentClass`, `OnPostInit`, `EOnInit`, `EOnFrame`, `EventMask`, and `FindComponent` usage.
- Game component examples from query output show components attached to real game systems.
- `SCR_CallsignBaseComponent`, `SCR_CampaignServiceEntityComponent`, `SCR_HybridPhysicsComponent`, and similar query results are good first routes for lifecycle and frame-event snippets.

Official sample folders show entity/component wiring signals:
- `SampleMod_ModdedScript`: script component and modded script layout signal.
- `SampleMod_Main`: prefab/config/entity resource layout signal.
- `SampleMod_NewCar` and `SampleMod_ModdedCar`: entity/component prefab layout signals, but vehicle behavior belongs to the vehicle reference.
- `SampleMod_NewCharacter`: character entity and component wiring signal, but gear/inventory behavior belongs to the gear reference.
- `SampleMod_NewFaction`: editable entity/catalog setup signal, but Game Master/faction behavior belongs to its domain reference.
- `SampleMod_ModdedWeapon`: item/entity/component layout signal, but weapon behavior belongs to the weapon reference.

Do not copy sample bodies into this reference. Use samples for orientation, then verify exact APIs through query commands.

## Follow-Up Keywords

Entity Lifecycle, Entity Activeness, Create an Entity, Create a Component, Action Context Setup, BaseDoorComponent, `IEntity`, `GenericEntity`, `GenericComponent`, `ScriptComponent`, `ScriptComponentClass`, `IEntity.FindComponent`, `FindComponent`, `EntityEditorProps`, `ComponentEditorProps`, `Attribute`, `EventMask`, `SetEventMask`, `EOnInit`, `EOnFrame`, `OnPostInit`, `OnComponentInsert`, active flag, frame event, physical representation, `PointInfo`, `UIInfo`, `ActionsManagerComponent`, `RplComponent`, owner entity, component class, entity class, compile reload, Workbench Components list, Workbench Entities list.

## Verification

Before finalizing entity/component lifecycle work:
1. Confirm the task belongs to generic entity/component lifecycle; if it is domain-specific, open the narrow domain reference.
2. Confirm the relevant wiki lifecycle or setup page has been read.
3. Query exact APIs for every uncertain entity/component class, method, event, or metadata attribute.
4. Confirm entity/component scripts are in the expected module path.
5. Confirm companion class names and editor metadata.
6. Compile and reload scripts before checking Workbench visibility.
7. Confirm component attachment on the actual prefab or placed entity.
8. Confirm lifecycle callback prerequisites and event masks.
9. Confirm active/frame-event behavior in runtime.
10. Confirm action contexts have physical representation, UI info, action locations/actions/parameters, and `RplComponent` where synchronization is expected.
11. State any remaining Workbench, runtime, multiplayer, or domain validation that was not possible.

## Official Wiki Links

- Entity Lifecycle: https://community.bistudio.com/wiki/Arma_Reforger:Entity_Lifecycle
- Entity Activeness: https://community.bistudio.com/wiki/Arma_Reforger:Entity_Activeness
- Create an Entity: https://community.bistudio.com/wiki/Arma_Reforger:Create_an_Entity
- Create a Component: https://community.bistudio.com/wiki/Arma_Reforger:Create_a_Component
- Action Context Setup: https://community.bistudio.com/wiki/Arma_Reforger:Action_Context_Setup
- BaseDoorComponent: https://community.bistudio.com/wiki/Arma_Reforger:BaseDoorComponent

## Usefulness Score

Score: 93/100

- Wiki coverage: 28/30. All owned lifecycle, activeness, entity creation, component creation, action context, and BaseDoor warning pages are named, represented, and linked. BaseDoorComponent is intentionally partial because this reference owns only generic component-configuration warnings.
- Operational detail: 15/15. The reference preserves lifecycle/event-mask rules, activeness behavior, Workbench visibility requirements, entity/component setup workflows, action-context setup, and validation order.
- API lookup usefulness: 14/15. Exact lookup commands cover entity/component anchors, `FindComponent`, lifecycle examples, game-component examples, editor props, and event masks. Exact signatures remain delegated to query output.
- Example grounding: 9/10. Official sample families and game-source query routes are included as layout/pattern evidence without copying bodies.
- Codex task usefulness: 14/15. Codex can route normal tasks like creating an entity, creating a component, wiring components, checking lifecycle callbacks, and setting action contexts without guessing. Domain-specific behavior is intentionally cross-linked.
- Context efficiency: 9/10. The file is dense and owner-focused; it avoids duplicating script, prefab/config, replication, and domain component ownership.
- Verification guidance: 4/5. Workbench, compile/reload, lifecycle, action context, and runtime validation are covered; multiplayer/domain validation is delegated where appropriate.

Category-fit check:
- Source family complete: pass. Entity Lifecycle, Entity Activeness, Create an Entity, Create a Component, Action Context Setup, and generic BaseDoorComponent warnings are covered.
- No owned page missing: pass. Every owned primary page is listed in Source Inventory.
- Split boundary justified: pass. Script patterns, prefab/config data, replication, and domain-specific component behavior are explicitly routed elsewhere.
- Cross-links present: pass. Closely related workflows point to their owning references.
- Task route clear: pass. Codex can start from lifecycle/entity/component intent, use the relevant workflow, then query exact APIs and examples.

Missed coverage and exclusions:
- Full BaseDoorComponent behavior is excluded and only generic component-data warnings are retained.
- User-action script implementation is excluded and routed to `script-events-actions-and-patterns.md`.
- Replication/authority behavior is excluded and routed to `multiplayer-replication-and-authority.md`.
- Weapon, vehicle, audio, UI, AI, terrain, scenario, and Game Master component details are excluded to avoid duplicate ownership.
