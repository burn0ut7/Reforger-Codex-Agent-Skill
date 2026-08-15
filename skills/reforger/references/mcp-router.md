# Reforger MCP capability guide

This reference describes what the Reforger Script Tools MCP server exposes, how its responses are represented, and where each tool family is useful. Workflow order, evidence gates, and task-completion rules belong to the Reforger skill and repository instructions rather than this reference.

## MCP interface

The live MCP tool catalogue and each tool's input schema define the available interface. Tool calls return machine-readable fields in `structuredContent`. Text and image payloads, including window captures, are returned in `content`.

Structured failures expose a stable code, message, recovery description, and retryability. Workbench failures can also include an operation phase and an integration-log reference.

Several results contain opaque values that identify a particular snapshot or target:

- `nextCursor` identifies the next page of the same result set.
- Catalogue and corpus revisions identify the indexed snapshot behind a result.
- Symbol references identify exact Game Data or workspace declarations.
- Entity, component, resource, editor, layer, and window IDs identify live Workbench objects.
- Read and inspection inputs are copy-ready arguments for a related tool.
- Write descriptors and confirmation tokens represent typed or previewed mutations.
- Runtime generations distinguish Workbench script activations.

## Capability map

| Information or operation | MCP tools | What the capability provides |
| --- | --- | --- |
| Official Reforger documentation | `official_wiki_status`, `search_official_wiki`, `read_official_wiki` | Packaged Wiki availability, ranked passages, exact line ranges, source URLs, and corpus revisions. |
| Compact Game Data research | `research_game_data` | One primary declaration for a natural-language or identifier query, compact alternatives, relevant direct members, and a follow-up description. |
| Exact Game Data declarations | `search_game_data_symbols`, `inspect_game_data_symbol`, `list_game_data_symbol_members` | Filtered declarations, signatures, attributes, ownership, inheritance metadata, and direct members. |
| Game Data relationships and source | `query_game_data_symbol_relationships`, `query_source_symbol_relationships`, `read_game_data_source` | Inheritance, overrides, implementations, references, callers, and bounded source passages. |
| Game Data text and resources | `search_game_data_text`, `search_game_data_resources` | Literal or regular-expression source occurrences and offline prefab, config, layout, world, or other resource identities. |
| Workspace declarations and source | `search_workspace_symbols`, `inspect_workspace_symbol`, `list_workspace_symbol_members`, `query_workspace_symbol_relationships`, `read_workspace_source`, `search_workspace_text` | Indexed declarations, relationships, bounded source, and textual occurrences from configured user add-ons. |
| Workbench availability and project context | `workbench_status`, `workbench_state`, `workbench_project_context` | Current connection, script status, editor mode, active world, loaded add-ons, layer context, and play-session state. |
| Native compilation | `workbench_validate_scripts` | A Workbench-authored compilation result with normalized, pageable diagnostics. |
| Resources and editors | `workbench_search_resources`, `workbench_inspect_resource`, `workbench_list_editors`, `workbench_open_editor`, `workbench_open_resource` | Live registered resources, compact metadata, available editor identities, and editor/resource opening. |
| World inspection | `workbench_world_selection_summary`, `workbench_selected_entity_hierarchy`, `workbench_list_entities`, `workbench_search_world_entities`, `workbench_inspect_entity`, `workbench_layer_state` | Selection, hierarchy, entity, component, prefab, layer, and world-revision facts from the active World Editor. |
| Spatial inspection | `workbench_find_entities_by_radius`, `workbench_sample_terrain`, `workbench_get_viewport_context`, `workbench_trace` | Nearby entities, terrain and water samples, camera and cursor context, and collision traces. |
| Prefab inspection and editing | `workbench_inspect_prefab_context`, `workbench_inspect_prefab_component`, and `workbench_*prefab*` mutation tools | Prefab ancestry, members, effective component values, creation, persistence, and typed property editing. |
| Entity and component editing | `workbench_create_entity`, `workbench_*entity`, `workbench_*component`, `workbench_undo`, `workbench_redo` | Undoable entity, transform, hierarchy, component, selection, and typed property operations. |
| Shape geometry | `workbench_get_shape_points`, `workbench_edit_shape_points`, `workbench_*shape*`, `workbench_*spline*`, `workbench_resample_polyline` | Polyline and spline inspection, coordinate conversion, generation, transformation, sampling, and editing. |
| Saving, reload, and play sessions | `workbench_save`, `workbench_reload`, `workbench_start_play_session`, `workbench_stop_play_session` | Save acknowledgements, script reload dispatch and runtime generation, and play-mode transition requests. |
| Logs and visual inspection | `workbench_read_logs`, `workbench_list_windows`, `workbench_capture_window` | Bounded integration or Workbench logs, visible window identities, and captured window imagery. |
| Workbench lifecycle and bridge | `workbench_launch`, `workbench_stop`, `workbench_restart`, `workbench_install_bridge` | Exact-project process lifecycle and managed bridge maintenance. |

## Search and inspection distinctions

`research_game_data` is a compact intent lookup. Symbol search is a filtered declaration catalogue. Symbol inspection expands one exact declaration, member tools enumerate an owner's direct members, and relationship tools expose semantic edges.

Text search scans readable source occurrences, including strings, comments, expressions, and local names. Source readers return bounded passages associated with an indexed revision.

Game Data and Official Wiki tools describe indexed static material. Workspace tools describe the configured add-on snapshot. Workbench tools describe or modify the current live editor and runtime.

## Dynamic tool details

Exact parameter limits, enums, optional fields, mutation previews, confirmation requirements, and failure codes are part of each live tool schema and description. The committed `docs/mcp-api.md` and its linked tool pages mirror that interface for repository inspection.
