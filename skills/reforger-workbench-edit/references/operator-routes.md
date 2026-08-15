# Workbench operator routes

Choose exactly one route for each live mutation. Treat current tool schemas as authoritative, pass only accepted fields, preserve opaque values unchanged, and follow structured recovery instead of substituting another operation.

## Target and placement reads

| Need | Route | Completion |
| --- | --- | --- |
| Current selection | `workbench_world_selection_summary` to `workbench_inspect_entity` | One stable entity ID and current inspection |
| Entity search | `workbench_search_world_entities` or `workbench_list_entities` to `workbench_inspect_entity` | Exact structural match, not display-name inference |
| Nearby entity | `workbench_find_entities_by_radius` to `workbench_inspect_entity` | Exact hit inside the requested spatial bound |
| Hierarchy | `workbench_selected_entity_hierarchy` or exact entity inspection | Parent and child identities established |
| Layer eligibility | `workbench_layer_state` | Exact subscene and layer visible and unlocked |
| Placement | `workbench_get_viewport_context`, `workbench_sample_terrain`, or `workbench_trace` | Explicit world position and required surface facts |
| Resource | `workbench_search_resources` to `workbench_inspect_resource` | Canonical resource name and owning add-on |

Use `workbench_state` first. World mutation requires an active World Editor/API and edit mode, not a likely-running play session.

## World entities

| Operation | Read, write, readback |
| --- | --- |
| Create | Verify resource or class; establish subscene, layer, and position; call `workbench_create_entity`; inspect returned entity |
| Duplicate | Inspect source and destination; call `workbench_duplicate_entity`; inspect returned entity |
| Move | Inspect entity and destination; call `workbench_move_entity`; inspect transform |
| Rotate | Inspect entity; call `workbench_rotate_entity` with explicit live-schema angles; inspect transform |
| Atomic transform | Inspect entity; call `workbench_transform_entity` with position, angles, and uniform scale; compare returned transform and fresh inspection |
| Rename | Inspect entity; call `workbench_rename_entity`; inspect identity and name |
| Reparent | Inspect child and parent; call `workbench_reparent_entity`; inspect hierarchy |
| Delete | Inspect entity; preview and confirm `workbench_delete_entity` with unchanged `workbench_delete_entity.confirmationToken`; search or inspect to prove absence |
| Selection only | Call `workbench_set_selection` or `workbench_clear_selection`; read `workbench_world_selection_summary`; world content remains unchanged |

World content edits are native Workbench actions but remain unsaved until the authorized world-save route completes.

## Components and properties

| Operation | Read, write, readback |
| --- | --- |
| Add component | Inspect entity; verify exact component class in Game Data; call `workbench_add_component`; list and inspect returned component |
| Remove component | Call `workbench_list_components`, then `workbench_inspect_component`; preview and confirm `workbench_remove_component`; list again to prove absence |
| Entity property | Call `workbench_list_entity_properties`; copy `workbench_list_entity_properties.writeDescriptor`; pass it as `workbench_set_entity_properties.writeDescriptor`; list the property again |
| Component property | Call `workbench_inspect_component`; copy `workbench_inspect_component.writeDescriptor`; pass it as `workbench_set_component_properties.writeDescriptor`; inspect again |

Descriptors bind observed property and value. A stale or rejected descriptor requires new inspection; never reconstruct one manually.

## Prefabs

Choose the route by owning surface:

| Surface | Read, write, persistence and readback |
| --- | --- |
| Create from scene entity | Inspect entity and destination; preview and confirm `workbench_create_prefab`; inspect returned resource |
| Create GenericEntity resource | Verify destination and unlocked layer; preview and confirm `workbench_create_generic_prefab`; inspect returned resource |
| Open Prefab Editor root property | Call `workbench_inspect_prefab_context`; copy descriptor; call `workbench_set_prefab_property`; inspect context; preview and confirm `workbench_save_prefab` when saving is requested |
| Open Prefab Editor component property | Inspect prefab component; call `workbench_set_prefab_component_property`; inspect component; preview and confirm `workbench_save_prefab` when saving is requested |
| Saved prefab resource property | Inspect canonical prefab context and component; preview and confirm `workbench_set_prefab_resource_property`; require saved fresh inspection |
| Add saved-resource component | Inspect canonical prefab and verify class; preview and confirm `workbench_add_prefab_resource_component`; require saved fresh inspection |
| Remove saved-resource component | Inspect canonical prefab/component; preview and confirm `workbench_remove_prefab_resource_component`; require saved inspection proving absence |
| Save exact prefab | Identify one open entity or canonical resource; preview and confirm `workbench_save_prefab`; require saved result and inspection |

Project-relative destinations and canonical resource names are accepted; absolute filesystem paths are outside these routes. Resource-level confirmed mutations save the template. Prefab Editor property setters do not.

## Shape geometry

| Operation | Read, write, readback |
| --- | --- |
| Point edit | `workbench_get_shape_points` to `workbench_edit_shape_points` to get points again |
| Regular polygon | Get points; call `workbench_set_polyline_regular_polygon`; get points again |
| Whole-shape transform | Get points; choose local or world space; call `workbench_transform_shape_points`; get points again |
| Polyline resample | Get points; call `workbench_resample_polyline` with explicit space and spacing; verify count, endpoints or closure, and points |
| Spline replacement | Call `workbench_inspect_spline`; call `workbench_edit_spline` with explicit space; inspect again |
| Coordinate conversion | `workbench_convert_shape_points` is read-only; use returned points as explicit input to a later authorized edit |

## Confirmation, persistence, and rollback

- Preview and confirm destructive, resource-creation, resource-save, and saved-prefab-resource operations using each tool's returned confirmation token unchanged.
- World persistence: `workbench_save` saves all open tabs and the named active world. Call it only when that full scope is authorized; require `workbench_save.saveAllAccepted`, `workbench_save.worldSaveAccepted`, and `workbench_save.worldSaveStatus` for separate persistence claims.
- Prefab persistence: resource-level confirmed operations save immediately; Prefab Editor property setters require `workbench_save_prefab`.
- Rollback: call `workbench_undo` only for a known latest native undoable World Editor action and when rollback is authorized. Require `workbench_undo.historyAvailable` and `workbench_undo.changed` true, then re-inspect. Do not assume undo reverses auto-saved prefab-resource mutation.
- Redo: call `workbench_redo` only for the immediately verified undo belonging to this transaction, then re-inspect.
- Unsupported operation: when no exact public route exists, report it as unsupported. Keep authored files untouched and do not improvise UI automation or source mutation.
