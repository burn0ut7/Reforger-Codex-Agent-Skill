# Evidence contract

Use this contract to judge whether discovery, implementation, and validation prove the requested Reforger behavior.

## API emission gate

An engine API is verified only when indexed Game Data establishes its relevant owner, kind, signature, modifiers, attributes, inheritance, accessibility, and source provenance. Wiki snippets, generated web pages, examples, and model memory may guide discovery but cannot satisfy this gate. Before verification, retain a supplied identifier only as a labeled search term and describe other candidates generically by role.

Record every engine-facing identifier in changed lines in this ledger:

| Identifier | Exact owner/declaration | Signature/attributes | Relationship or usage evidence | Status |
| --- | --- | --- | --- | --- |

Exact code is ready only when every identifier is `verified`, `workspace-owned`, or a Wiki-confirmed language construct. Keep unresolved behavior at architecture or placeholder-pseudocode level.

## Design contract

Choose the design only after gathering:

1. Wiki evidence for the intended system model and constraints.
2. Exact Game Data declarations and relationships for the APIs involved.
3. Workspace evidence for current add-on behavior and conventions.
4. Resource or Workbench evidence when behavior depends on authored or live state.

Assign every requested behavior to an owning surface. A script change may coordinate with data or editor changes, but cannot stand in for missing prefab wiring, layout structure, resource identity, world state, or runtime configuration.

Complete the design when the chosen approach explains why it fits the authorities, how data and control flow through each surface, and how each claim will be validated.

## Evidence ledger

| Claim | Minimum sufficient evidence |
| --- | --- |
| Concept or intended workflow | Relevant packaged Official Wiki section |
| Engine declaration or relationship | Resolved compact Game Data research or targeted inspection; relationship evidence only when an edge is part of the claim |
| Engine usage pattern | Handwritten Game Data example plus separate declaration verification |
| Add-on declaration or behavior | Current workspace source/symbol evidence and relationships |
| Offline resource identity | Game Data resource result with canonical identity and provenance |
| Compilation | Latest complete `workbench_validate_scripts` result with `workbench_validate_scripts.success` true |
| Reload | Successful `workbench_reload` with `workbench_reload.reloadDispatched` true and replacement `workbench_reload.runtimeGeneration` |
| Authored resource, prefab, or world state | Exact live Workbench inspection and readback |
| Runtime or multiplayer behavior | Direct observation in each relevant runtime role or session |
| Diagnostic history | Reload-scoped or explicitly bounded Workbench logs |

Resolve conflicting evidence in favor of the authority that owns the claim. Keep parser analysis, compilation, reload, live state, behavior, and logs as separate facts.

## Owning-surface validation

| Changed surface | Required checks when available |
| --- | --- |
| Enforce Script | Repository checks, complete native compiler gate, reload, targeted live behavior, fresh logs |
| Override, inheritance, callback | Exact declarations, signature and attributes, relationships, compiler gate, runtime invocation |
| Prefab, config, or resource | Canonical identity, ancestry, effective component/property readback, dependent compile/reload, live spawn or load |
| World or editor data | Exact entity/layer/component readback, persistence status, targeted in-editor behavior |
| UI | Layout inspection, binding declarations, compiler gate, reload, relevant screen/input behavior |
| Multiplayer | Role/data-flow ledger, compiler gate, reload, authority/proxy and owner/non-owner runs, streaming/JIP, dedicated server |
| Server, package, or publish | Configuration/schema evidence, dependency/package inspection, dry run or staging validation where available |

## Multiplayer ledger

Before editing replication code, write a compact table:

| State/event | Created by | Authority | Owner | Sender to receiver | Persistence | Streaming/JIP consequence |
| --- | --- | --- | --- | --- | --- | --- |

Account for dedicated server, listen server, owning client, non-owning client, streamed-out proxies, and join-in-progress. Establish ownership and authority independently from Wiki and Game Data evidence.

## Workbench mutation contract

Complete these gates in order for live editor writes:

1. Confirm explicit intent to mutate live Workbench state and the persistence scope.
2. Check `workbench_status` when availability is uncertain, then inspect `workbench_state` and `workbench_project_context`.
3. Establish that the required editor/API is active and play-session state permits the operation.
4. Resolve an exact stable resource/entity/component identity; display name alone is insufficient.
5. Inspect the exact target and copy typed write descriptors or confirmation data unchanged.
6. Preview destructive operations and obtain required confirmation.
7. Perform one small mutation, then read back that target before continuing.
8. Run owning-surface validation and save only within the authorized persistence scope.

Keep diagnosis read-only. Launch, bridge installation, reload experiments, play control, process lifecycle operations, saves, and destructive changes require explicit task intent. A post-compile reload is authorized only for a requested implementation and must account for Save All and world-save effects.
