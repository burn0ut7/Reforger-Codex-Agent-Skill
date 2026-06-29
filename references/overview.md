# Overview

## When to read this reference

Read this first when an Arma Reforger task is ambiguous, crosses code/data/editor/server boundaries, or might need Workbench resources rather than only Enfusion Script.

## Search terms

`script-first`, `data-first`, `editor-first`, `asset-first`, `server-first`, `Workbench`, `ResourceName`, `prefab`, `config`, `RplComponent`, `Game Master`, `World Editor`, `Workshop`, `api-main.md`, `api-extended.md`

## Source authority summary

Use official wiki/docs as workflow truth, official sample mods as concrete implementation patterns, and extracted API data as exact signature truth. Samples show how Bohemia structures real addon content, but samples do not override docs or current API signatures.

## Task classification

Most Reforger tasks are mixed. Decide the primary surface before writing anything:

- Script-first: classes, components, modded overrides, invokers, event masks, RPCs, Workbench plugins, UI scripts, runtime behavior. Route to `scripting-core.md`, `scripting-language.md`, `entity-component-lifecycle.md`, `networking-multiplayer-replication.md`, and `api-main.md`.
- Data-first: configs, entity catalogs, factions, arsenal content, prefabs, Game Master editable entities, terrain/world data, server config, Workshop metadata. Route to `resources-prefabs-configs.md`, domain-specific reference, then only add code if the data cannot express the behavior.
- Editor-first: Workbench procedures, Resource Manager processing, World Editor terrain/navmesh/generator work, Script Editor plugins, String Editor, diagnostics. Route to `workbench-tools-debugging.md` or `terrain-world-editor.md`.
- Asset-first: FBX/model import, materials, textures, LOD/collision, weapons, vehicles, animation graphs, sound events/signals. Route to `assets-weapons-vehicles-animation-audio.md`.
- Server-first: startup parameters, dedicated server config, Workshop addon IDs, scenario startup, ports, logs, secrets, deployment rollback. Route to `server-runtime-packaging.md`.
- Multiplayer-first: authority/proxy/owner role, replicated properties, RPCs, streaming/JIP, dedicated server behavior. Route to `networking-multiplayer-replication.md` before coding.

## High-risk boundaries

- A component script must live in the Game script module if it should appear in World Editor Add Component lists.
- Workbench/editor plugin scripts belong in Workbench/editor script modules and must not leak editor-only API calls into runtime game code.
- Entity/component lifecycle callbacks often require event masks. Some callbacks only fire when the right event mask is set and additional conditions are satisfied.
- Multiplayer logic should be written around authority/proxy/owner roles, not around a naive "server/client" branch.
- A client-created entity is local to that client and unknown to the server; it cannot be broadcast to everyone later as if it were a server authority entity.
- Runtime replicated items generally require prefab spawning and authority-side insertion. Loadtime items must be deterministic across server and clients.
- Prefabs/configs/catalogs often decide whether content appears in Game Master, arsenal, factions, scenarios, UI, and Workshop packages.
- Dedicated servers do not instantiate some client-only components and do not have normal local-player/UI assumptions.

## Normal verification loop

1. Classify the task type and open the closest topical reference.
2. Search the user project for creator tag, module paths, existing class naming, prefab/config organization, and sample-like patterns.
3. Verify exact APIs in `api-main.md`; fall back to `api-extended.md` for less common classes, attributes, enums, generated systems, and `SCR_` classes.
4. For editor/data work, list exact Workbench or Resource Manager actions that must be performed after file edits.
5. For multiplayer/server work, state authority, ownership, streaming/JIP, and dedicated-server verification needs.
6. After implementation, check compile/runtime evidence available from files and state residual Workbench/game/server tests that cannot be executed from code alone.

## Routing table

| User task mentions | Start with | Then check |
| --- | --- | --- |
| "component", "ScriptComponent", "Add Component", entity behavior | `entity-component-lifecycle.md` | `scripting-core.md`, `api-main.md` |
| "modded class", override, debug print, invoker | `scripting-core.md` | `scripting-language.md`, project search |
| "RPC", "replicate", "server/client", JIP | `networking-multiplayer-replication.md` | `api-main.md`, project role checks |
| "prefab", `.et`, "config", `.conf`, catalog | `resources-prefabs-configs.md` | sample patterns, API resource calls |
| "Workbench plugin", Resource Manager, Script Editor | `workbench-tools-debugging.md` | `api-main.md`, sample Workbench plugin |
| "Game Master", faction, task, scenario | `scenario-framework-game-master.md` | resources/configs, sample faction/catalog layouts |
| "terrain", "navmesh", road, river, lake, generator | `terrain-world-editor.md` | Workbench/World Editor validation |
| "weapon", "vehicle", "animation", "audio", "FBX" | `assets-weapons-vehicles-animation-audio.md` | resources/configs, samples |
| "server", "startup", "Workshop", `.gproj` | `server-runtime-packaging.md` | server logs, packaging checklist |
| "show me a common pattern" | `examples-patterns.md` | topical reference for the implementation |
| "fast recipe" | `common-task-recipes.md` | API verification and project search |

## Source-backed examples

generated-pattern-from-docs

Minimal routing for a component request:

```text
Task: "Add a component that moves nearby characters."
Type: mixed script + prefab/editor wiring.
References: entity-component-lifecycle, scripting-core, api-main.
Must preserve: class/class-name pairing, Game module placement, ComponentEditorProps, Add Component visibility, Shift+F7 script reload, event mask for frame callback, owner origin/SetOrigin use, prefab/world placement verification.
```

generated-pattern-from-docs

Minimal routing for a replicated action:

```text
Task: "Turn a device on for all players."
Type: multiplayer script + prefab replication setup.
References: networking-multiplayer-replication, entity-component-lifecycle, api-main.
Must preserve: authority-side state mutation, owner asks authority via RPC, authority broadcasts presentation or uses RplProp, Replication.BumpMe when needed, no RPC from EOnInit, broadcast only reaches streamed proxies.
```

## API Notes

Use `api-main.md` for common APIs: `IEntity`, `ScriptComponent`, `GenericComponent`, `Game`, `Resource`, `ResourceName`, `BaseRplComponent`, `RplProp`, `RplRpc`, `WorkbenchPlugin`, `WorkspaceWidget`, and input/UI basics. Use `api-extended.md` for exhaustive generated classes, Workbench module APIs, weapon/vehicle/audio/animation systems, and project-specific `SCR_` classes.

## Common Traps

- Answering with code only when the task needs prefab, config, catalog, world, UI layout, Workshop, or Workbench actions.
- Copying sample code without checking current API signatures and target project base classes.
- Assuming `server == authority` for every object; locally created client entities can be authority but remain local.
- Forgetting that editor preview/Workbench behavior differs from runtime/game behavior.
- Forgetting to state residual verification: script compile, Workbench Add Component visibility, prefab serialization, multiplayer two-peer test, dedicated server startup, or Workshop packaging.

## Review Checklist

- Did the answer classify the task boundary?
- Did it route to the right reference before proposing implementation?
- Did it verify exact APIs or mark uncertainty?
- Did it include non-code Workbench/data/server steps when required?
- Did it keep local raw provenance out of runtime output?

## Task Boundary Notes

- A content task can require script review when user actions, replication, or custom components are part of the asset.
- A script task can require data review when the script stores `ResourceName`, prefab, catalog, UI layout, or config references.
- A server task can require Workshop review when addons must load from published IDs.
- An editor task can require runtime review when a Workbench plugin generates files that game code later consumes.
