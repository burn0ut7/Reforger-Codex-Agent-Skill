# Workbench operator routes

Choose exactly one route for each live mutation. Treat current tool schemas as authoritative, pass only accepted input fields, preserve required opaque values unchanged, and follow structured recovery rather than substituting another operation.

## Target and placement reads

| Need | Route | Completion |
| --- | --- | --- |
| Current selection | `workbench_world_selection_summary` -> `workbench_inspect_entity` | One stable `entityId` and current inspection |
| Entity search | `workbench_search_world_entities` or `workbench_list_entities` -> `workbench_inspect_entity` | Exact structural match, not display-name inference |
| Nearby entity | `workbench_find_entities_by_radius` -> `workbench_inspect_entity` | Exact hit inside the requested spatial bound |
| Hierarchy | `workbench_selected_entity_hierarchy` or exact entity inspection | Parent/child identities established |
| Layer eligibility | `workbench_layer_state` | Exact subscene/layer is visible and unlocked |
| Placement | `workbench_get_viewport_context`, `workbench_sample_terrain`, and/or `workbench_trace` | Explicit world position and required surface facts |
| Resource | `workbench_search_resources` -> `workbench_inspect_resource` | Canonical `resourceName` and owning add-on |

Use `workbench_state` first. World mutation requires an active World Editor/API and edit mode rather than a likely-running play session.

## World entities

| Operation | Read -> write -> readback |
| --- | --- |
| Create | Verify `resourceName` or entity `className`; establish exact `subScene`, `layerId`, and position -> `workbench_create_entity` -> inspect returned entity |
| Duplicate | Inspect source and destination -> `workbench_duplicate_entity` -> inspect returned entity |
| Move | Inspect entity and destination -> `workbench_move_entity` -> inspect transform |
| Rotate | Inspect entity -> `workbench_rotate_entity`, passing explicit angles through the live schema's `position` object -> inspect transform |
| Atomic transform | Inspect entity -> `workbench_transform_entity` with position, angles, and uniform scale -> compare returned transform and fresh inspection |
| Rename | Inspect entity -> `workbench_rename_entity` -> inspect identity/name |
| Reparent | Inspect child and parent -> `workbench_reparent_entity` -> inspect hierarchy |
| Delete | Inspect entity -> `workbench_delete_entity` preview -> confirm -> search or inspect to prove absence |
| Selection only | `workbench_set_selection` or `workbench_clear_selection` -> `workbench_world_selection_summary`; world content is unchanged |

World content edits are native Workbench actions but remain unsaved until the authorized world-save route completes.

## Components and properties

| Operation | Read -> write -> readback |
| --- | --- |
| Add component | Inspect entity; verify exact component class in Game Data -> `workbench_add_component` -> list/inspect returned component |
| Remove component | `workbench_list_components` -> `workbench_inspect_component` -> `workbench_remove_component` preview -> confirm -> list components to prove absence |
| Entity property | `workbench_list_entity_properties` -> copy its typed `writeDescriptor` -> `workbench_set_entity_properties` -> list property again |
| Component property | `workbench_inspect_component` -> copy its typed `writeDescriptor` -> `workbench_set_component_properties` -> inspect component again |

Descriptors bind the observed property and value. A stale/rejected descriptor requires a new inspection; never reconstruct one manually.

## Prefabs

Choose the route by owning surface:

| Surface | Read -> write -> persistence/readback |
| --- | --- |
| Create from scene entity | Inspect entity and project-relative destination -> `workbench_create_prefab` preview -> confirm -> inspect returned resource |
| Create GenericEntity resource | Verify project-relative destination and unlocked layer -> `workbench_create_generic_prefab` preview -> confirm -> inspect returned resource |
| Open Prefab Editor root property | `workbench_inspect_prefab_context` -> copy descriptor -> `workbench_set_prefab_property` -> inspect context -> `workbench_save_prefab` preview/confirm when saving is requested |
| Open Prefab Editor component property | Inspect prefab context/component -> `workbench_set_prefab_component_property` -> inspect component -> `workbench_save_prefab` preview/confirm when saving is requested |
| Saved prefab resource property | Inspect canonical prefab context/component -> `workbench_set_prefab_resource_property` preview -> confirm -> require `templateSaved` and fresh returned inspection |
| Add saved-resource component | Inspect canonical prefab -> verify class -> `workbench_add_prefab_resource_component` preview -> confirm -> require saved fresh inspection |
| Remove saved-resource component | Inspect canonical prefab/component -> `workbench_remove_prefab_resource_component` preview -> confirm -> require saved inspection proving absence |
| Save exact prefab | Identify one open `entityId` or canonical `resourceName` -> `workbench_save_prefab` preview -> confirm -> require saved result and inspection |

Project-relative destinations and canonical resource names are accepted; absolute filesystem paths are outside these routes. Resource-level confirmed mutations save the template. Prefab-editor property setters do not save it.

## Shape geometry

| Operation | Read -> write -> readback |
| --- | --- |
| Point edit | `workbench_get_shape_points` -> `workbench_edit_shape_points` -> get points again |
| Regular polygon | Get points -> `workbench_set_polyline_regular_polygon` -> get points again |
| Whole-shape transform | Get points; choose local/world space explicitly -> `workbench_transform_shape_points` -> get points again |
| Polyline resample | Get points -> `workbench_resample_polyline` with explicit space/spacing -> verify point count, endpoints/closure, and points |
| Spline replacement | `workbench_inspect_spline` -> `workbench_edit_spline` with explicit space -> inspect spline again |
| Coordinate conversion | `workbench_convert_shape_points` is read-only conversion; use its returned points as explicit input to a later authorized edit |

## Confirmation, persistence, and rollback

- Preview-confirm: `workbench_delete_entity`, `workbench_remove_component`, `workbench_create_prefab`, `workbench_create_generic_prefab`, `workbench_save_prefab`, and saved-prefab-resource add/remove/property operations. Inspect the preview, then echo its token unchanged.
- World persistence: `workbench_save` saves all open tabs and the existing named active world. Call it only when that full scope is authorized; require `saveAllAccepted`, `worldSaveAccepted`, and `worldSaveStatus` to support separate claims.
- Prefab persistence: resource-level confirmed operations save immediately; Prefab Editor property setters require the separate save-prefab route.
- Rollback: use `workbench_undo` only for a known latest native undoable World Editor action and only when rollback is authorized. Require `historyAvailable: true` and `changed: true`, then re-inspect. Do not assume undo reverses an auto-saved prefab-resource mutation.
- Redo: use `workbench_redo` only for the immediately verified undo that belongs to this transaction, then re-inspect.
- Unsupported operation: when no exact live tool route exists, report it as unsupported. Keep authored files untouched and do not improvise UI automation or source-file mutation as a substitute.
