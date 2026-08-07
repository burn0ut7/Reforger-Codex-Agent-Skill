# MCP router

Use this reference before the first Reforger MCP call. Choose a route by the claim that must be established, follow returned handoffs exactly, and stop only at that route's completion criterion.

- [Response protocol](#response-protocol)
- [Route table](#route-table)
- [Official Wiki route](#official-wiki-route)
- [Game Data declaration route](#game-data-declaration-route)
- [Resource route](#resource-route)
- [Workspace route](#workspace-route)
- [Compiler route](#compiler-route)
- [Reload and runtime route](#reload-and-runtime-route)
- [Freshness and recovery](#freshness-and-recovery)

## Response protocol

1. Treat the live MCP catalogue and call schemas as authoritative.
2. Read JSON fields from `structuredContent`; use `content` for text or image payloads.
3. When `isError` is true, read the stable structured `code`, `message`, `recovery`, and `retryable` fields. Follow `recovery` instead of guessing another tool or argument.
4. Copy revisions, add-on GUIDs, cursors, symbol references, entity/resource/component IDs, descriptors, confirmation tokens, and ready-made input objects unchanged.
5. Continue an opaque cursor when proof requires more results. Start over from the originating search after a stale cursor or reference.
6. Treat an exact engine identifier as a fact only after Game Data verification. Until then, preserve user-provided names solely as labeled search terms and describe all other candidates generically by their required role.

## Route table

| Needed evidence | Start | Continue |
| --- | --- | --- |
| Reforger concept or workflow | `official_wiki_status` when uncertain, then `search_official_wiki` | `read_official_wiki` |
| Exact engine declaration | `game_data_status` when scope/health is uncertain, then `search_game_data_symbols` | inspect, members, relationships, examples, source |
| Offline prefab/config/layout/world/resource identity | `search_game_data_resources` | live resource inspection when current registration/effective state matters |
| Add-on declaration or usage | `search_workspace_symbols` | inspect, members, relationships, source |
| Cross-source override/inheritance/modded-class fact | semantic search for the exact anchor | `query_source_symbol_relationships` |
| Literal string/comment/expression/regex evidence | `search_game_data_text` or `search_workspace_text` | returned source-read input |
| Native compilation | `workbench_status` when uncertain | `workbench_project_context`, then `workbench_validate_scripts` |
| Reloaded runtime | successful native validation | `workbench_reload`, state, logs, targeted live test |

Semantic search owns declarations. Literal search owns textual occurrences. Workbench owns live state.

## Official Wiki route

1. Call `official_wiki_status` on first use, uncertainty, or corpus failure.
2. Search narrow terms with `search_official_wiki`; use `pathPrefix` only when the domain subtree is known.
3. Compare titles, paths, headings, match kinds, and excerpts instead of accepting rank one automatically.
4. Copy the selected hit's read input unchanged to `read_official_wiki`.
5. Follow a returned continuation unchanged until the required section is complete.

Complete the route when the relevant concept is supported by a canonical source URL/logical path, corpus revision, and exact line range. Wiki examples inform design but do not satisfy the engine API gate.

## Game Data declaration route

1. Call `game_data_status` when availability, coverage, version, cache health, or selectable scope is uncertain. Require `available: true`; copy the required `addonGuid` values and retain `catalogueRevision`.
2. Search the declaration semantically with `search_game_data_symbols`. Use exact name, owner, kinds, add-on scope, or source category filters when they narrow ambiguity.
3. Select the declaration by qualified name, kind, signature, owner, add-on provenance, and source category. Copy its `inspectInput` unchanged to `inspect_game_data_symbol`.
4. Verify kind, qualified name, signature/callable form, modifiers, attributes, base/container type, conditional context, accessibility, declaration range, and source provenance as relevant to the emitted use.
5. When `membersTruncated` is true or the needed member is absent from the preview, call `list_game_data_symbol_members` with the same `symbolRef`; continue `nextCursor` until the needed member is found or all direct members are exhausted. Inspect the member's returned symbol reference.
6. Query semantic relationships only with supported values:
   - `query_game_data_symbol_relationships`: `directBase`, `derivedType`, `override`, `implementation`, `overriddenDeclaration`, `reference`, `caller`.
   - `query_source_symbol_relationships`: `direct`, `directBase`, `derivedType`, `moddedExtension`, `overriddenDeclaration`, `override`; set `depth` to `one` or `all`, and copy `anchorSource` from the semantic hit.
7. Use `search_game_data_examples` only for published topics: `resource-loading`/`spawn-prefab`, `replication`/`rpc-authority`, `entity-lifecycle`/`event-mask`, or `ui`/`widget-creation`. Prefer handwritten usage and keep declaration verification separate.
8. Copy `readSourceInput` unchanged to `read_game_data_source`. Continue `nextStartLine` when the required evidence crosses a bounded read.

Complete the route when the exact declaration and every relationship relevant to its use are proven. Search results alone are discovery, not verification.

### API ledger

Before finalizing changed code, inventory every engine-facing class, member, callback, attribute, enum value, helper, and inherited assumption in the changed lines. Record for each:

| Identifier | Exact owner/declaration | Signature/attributes | Relationship or usage evidence | Status |
| --- | --- | --- | --- | --- |

Set status to `verified`, `workspace-owned`, `language construct`, or `blocked`. Only the first three may reach exact emitted code. The route is incomplete while any emitted identifier is unaccounted for.

## Resource route

1. Use `game_data_status` when offline resource scope or catalogue revision is uncertain.
2. Call `search_game_data_resources` with basename/path terms and, when useful, exact kinds: `prefab`, `script`, `audio`, `world`, `config`, `model`, `material`, `texture`, `layout`, `animation`, `particle`, `ai`, `string`, or `other`.
3. Preserve `resourceName`, add-on provenance, logical path, registration/stale flags, and Workbench link.
4. Use `workbench_search_resources` and exact resource/prefab inspection when current registration, effective values, ancestry, component wiring, or editor state matters.

Complete the route when the canonical resource identity and owning add-on are known, and any claim about effective live state has Workbench inspection evidence.

## Workspace route

1. Use `search_workspace_symbols` for add-on declarations. Copy `inspectInput`/`symbolRef` unchanged to workspace inspection and member tools.
2. Use `query_workspace_symbol_relationships` for add-on definitions, inheritance, references, and callers.
3. Use `query_source_symbol_relationships` for exact edges across the workspace and selected Game Data scope.
4. Copy returned `readSourceInput` unchanged to `read_workspace_source`; continue bounded reads when needed.
5. Use workspace text search only for literal or regex evidence.

Complete the route when the relevant add-on declaration, usage, and relationships are proven from the same workspace snapshot. The workspace index is built once per MCP process; after editing, restart MCP before treating semantic reinspection as fresh.

## Compiler route

1. Call `workbench_status` when availability is uncertain; this establishes availability only.
2. Call `workbench_project_context` and verify that the intended add-on is loaded.
3. Call `workbench_validate_scripts` without a cursor to run the native compiler under the fixed WORKBENCH profile.
4. Preserve that result's cursor and continue all `nextCursor` pages; cursored calls page the same compilation without recompiling.
5. Account for every error and warning. Fix relevant failures, then call `workbench_validate_scripts` again without a cursor to create a fresh validation result.

Complete the route when the latest uncursored validation returns `success: true`, every diagnostic page is consumed, and remaining warnings are reported. Any code edit after that result reopens the gate.

## Reload and runtime route

Use this route only after the compiler route completes for an authorized implementation workflow.

1. Read `workbench_state` and `workbench_project_context`; verify the intended project/editor context and note whether a play session is likely running.
2. Call `workbench_reload`. It confirms Save All for open tabs and saves a named active world before reloading, so include those persistence effects in the implementation authorization.
3. Require `reloadDispatched: true` and a returned replacement `runtimeGeneration`. Record `worldSavedBeforeReload` and `worldSaveStatus`.
4. Read fresh `workbench_status` and `workbench_state` after reload.
5. Read `workbench_read_logs` with `source: "workbench"` and `mode: "latest"`. Use `source: "integration"` when a Workbench tool reports a log reference or integration failure. Logs are diagnostic history, not proof of current state or behavior.
6. Run the smallest live test that exercises the requested behavior. For World Editor play tests, start only when the world is ready. `accepted: true` confirms only that the command was issued; observe state, behavior, and fresh logs before claiming success.
7. Stop a play session started for this test, confirm the transition back to edit mode, and read final relevant logs.

Complete the route when reload is structurally confirmed, live behavior is observed in every feasible required role, fresh logs are reviewed, and the editor is left in the intended state. Report manual or unavailable runtime roles instead of inferring them.

## Freshness and recovery

- Read stable errors from `structuredContent` and follow their exact recovery. A missing tool or unsupported request is a blocked route, not permission to substitute an unrelated tool.
- On stale symbols, relationships, revisions, or cursors, repeat the originating semantic search and use new handoffs.
- On `game_data_unavailable`, call `game_data_status` and follow its recovery. Use generic architecture or placeholder pseudocode; omit exact engine identifiers, signatures, attributes, and snippets until declarations are verified.
- On unavailable Official Wiki data, follow the status recovery and stop before design. Return only the missing evidence, intended searches, and recovery; omit Reforger-specific design and pseudocode until conceptual evidence is available.
- On `game_data_changed`, activate the language server to refresh its index cache, then restart MCP.
- Treat workspace semantic evidence as a per-process snapshot. Restart MCP after workspace edits before semantic post-edit claims.
- Treat Workbench status, native validation, reload, logs, editor state, and runtime observation as separate evidence surfaces.
