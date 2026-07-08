---
name: reforger
description: Build, review, and modify Arma Reforger mods and Enfusion Script code. Use for Arma Reforger scripting, Workbench, entities/components, replication/multiplayer, resources, prefabs, configs, scenarios, Game Master, terrain/world editor, weapons, vehicles, animation, audio, UI, AI, server config, Workshop packaging, and exact Reforger API lookup.
---

# Arma Reforger

Read this file in full when the skill triggers. This is the router, action loop, API lookup guide, and verification contract. The mandatory rules and action loop are requirements, not suggestions.

## Mandatory Rules

- MUST read every relevant reference in full before non-trivial Reforger work.
- MUST read multiple references when the task crosses systems.
- MUST NOT search references instead of reading them.
- MUST use real Reforger APIs from game-data search. Never guess class names, method signatures, attributes, inheritance, callbacks, or lifecycle methods.
- MUST verify every meaningful Reforger API call emitted in generated code, including helper calls, not only the main task API.
- MUST use listed search commands as starting points, then search closer names, topics, files, and snippets for the actual task.
- MUST find, open, and read relevant game-source examples before writing API-sensitive code.
- MUST use source snippets and examples to infer idiomatic usage patterns.
- MUST prefer direct source-backed APIs and idioms over composing generic calls, unless the generic composition is also source-backed and justified.
- MUST treat examples as guides, not law. Verify symbols and signatures separately.
- MUST prefer the smallest correct change that preserves current behavior.
- MUST keep local work local. Do not introduce managers, services, registries, wrappers, broad validation, or extra settings unless the request or demonstrated defect requires them.
- MUST break complex or cross-system work into small verified slices.
- MUST reread this file when the task becomes complex, crosses systems, or you are unsure whether the rules are being followed.
- MUST NOT modify this skill, references, scripts, or bundled data unless the user explicitly asks and confirms that change.

## Domain Grounding

- Arma Reforger uses Bohemia's Enfusion engine and Enforce Script, not Unity, Unreal, C#, SQF, or Arma 3 scripting.
- Many behaviors are data-driven through Workbench resources, prefabs, configs, components, and editor-authored assets.
- Exact API names and signatures must come from game-data search, not memory.
- Multiplayer work must account for authority, proxy, owner, replication, RPC, streaming, and dedicated-server behavior.
- Entity/component lifecycle, prefab wiring, resource paths, and Workbench configuration are common failure points.
- Examples show useful patterns, but the current API and relevant reference always win.

## Top Mistakes

- Writing code before reading the relevant reference.
- Guessing APIs or copying old Enfusion/Arma patterns without search verification.
- Treating examples as drop-in truth instead of implementation guidance.
- Solving data, prefab, or config problems only with script changes.
- Ignoring multiplayer authority or dedicated-server validation.
- Adding broad abstractions for a local gameplay or config fix.

## Action Loop

Follow this loop for every Reforger task:

1. MUST route the task to the smallest relevant reference set.
2. MUST read each relevant reference in full.
3. MUST query exact APIs with `scripts/query-reforger-data.py`.
4. MUST inspect relevant examples and bounded snippets from query results.
5. MUST self-audit before editing: am I following this file, have I read the references, have I verified every emitted API and source-backed idiom, and is this still the smallest correct local change?
6. MUST make only the current smallest correct local change or slice.
7. MUST verify that slice with available project checks and state any remaining Workbench, runtime, multiplayer, dedicated-server, packaging, editor, or asset validation.
8. MUST self-audit again before the final response, and between slices when continuing.

## Piecemeal Work Strategy

- For complex work, split the task into small slices that can be routed, searched, implemented, and verified independently.
- For each slice, read the relevant references, query exact APIs, inspect relevant examples/snippets, implement only that slice, then verify before moving on.
- For generated code, verify the actual code body: helper APIs, formatting/logging/resource/UI/component calls, and common idioms need source-backed evidence too.
- Stop and reassess when search results are weak, examples conflict, the requested scope expands, or the next step depends on Workbench, runtime, multiplayer, dedicated-server, packaging, editor, or asset validation.
- Do not batch unrelated fixes together. Do not add architecture, wrappers, managers, settings, or broad validation to make later slices easier unless the user request or demonstrated defect requires it.

## Routing

| Task | Read |
| --- | --- |
| Source hierarchy, runtime boundaries, lookup-first behavior, orientation | `references/start-here-source-authority.md` |
| Addon/project setup, `.gproj`, local mod layout, publishing, Workshop, packaging checks | `references/mod-projects-addons-workshop.md` |
| Enforce/Enfusion syntax, values, operators, keywords, language rules, Script Editor usage | `references/enfusion-language-and-script-editor.md` |
| Gameplay script structure, events, invokers, user actions, logging patterns | `references/script-events-actions-and-patterns.md` |
| API lookup behavior, common symbol routes, search command patterns | `references/api-lookup-and-common-symbols.md` |
| Resource Manager surfaces, file types, editor tools, Resource Manager plugins | `references/resource-manager-file-types-and-editors.md` |
| Prefab/config/resource data modeling, BaseContainer, ResourceName, catalogs | `references/prefabs-configs-containers-and-catalogs.md` |
| Entity/component lifecycle, event masks, activeness, component wiring, action contexts | `references/entities-components-and-lifecycle.md` |
| Authority/proxy/owner, replication, RPC, RplProp/RplRpc, JIP | `references/multiplayer-replication-and-authority.md` |
| Server config, startup parameters, hosting, management, RCON/A2S | `references/server-hosting-startup-and-runtime.md` |
| Workbench plugin authoring and editor extension surfaces | `references/workbench-plugins-and-editor-tools.md` |
| Diag Menu, autotests, profiling, FPS diagnostics, performance validation | `references/diagnostics-testing-and-performance.md` |
| Scenario Framework hierarchy, setup, components, activation, conditions, actions, debugging | `references/scenario-framework.md` |
| Game Master, factions, tasks, game modes, Conflict, Capture & Hold, notifications, hints | `references/game-master-factions-tasks-and-modes.md` |
| Terrain foundation, world setup, heightmaps, terrain entity, environment baseline, 2D maps | `references/terrain-creation-and-world-setup.md` |
| World Editor tools, generators, shape/vector tools, navmesh workflows | `references/world-editor-tools-generators-and-navmesh.md` |
| Asset import, FBX/model pipeline, Blender tools, materials/textures, props, LOD, collision, particles | `references/asset-import-models-materials-and-props.md` |
| Weapon creation, weapon prefab/config setup, attachments, optics, suppressors, magazines/ammo routes | `references/weapons-prefabs-attachments-and-firearms.md` |
| Character gear, headgear, vests, inventory, protection, arsenal exposure | `references/character-gear-inventory-and-arsenal.md` |
| Vehicle creation, simulation, compartments, seats, controllers, damage/fuel/turrets | `references/vehicles-creation-simulation-and-compartments.md` |
| Animation Editor, graphs/nodes, state machines, procedural animation, export profiles, weapon animation | `references/animation-graphs-weapon-animation-and-export.md` |
| Audio Editor, signals, DSP nodes, sound events/components, music, occlusion, radio, voice audio side | `references/audio-editor-signals-and-sound-systems.md` |
| UI layouts, dialogs, widgets, tooltips, HUD/menu routes, layout-to-script workflows | `references/ui-layouts-dialogs-and-menus.md` |
| Behavior Editor, AI nodes, AI debug, commanding behavior, AI validation | `references/ai-behavior-commanding-and-debug.md` |
| Example routing and game-source example query routes | `references/examples-and-sample-patterns.md` |
| Compact task recipes that route to one primary reference plus query commands | `references/common-task-recipes.md` |

## Search Guide

Use `scripts/query-reforger-data.py` for exact API and source lookup:

```powershell
py -3 scripts\query-reforger-data.py lookup "<task phrase>" --limit 8
py -3 scripts\query-reforger-data.py symbol <name> --exact
py -3 scripts\query-reforger-data.py method [owner] <name> --exact
py -3 scripts\query-reforger-data.py attribute <name> --exact
py -3 scripts\query-reforger-data.py inherits <class>
py -3 scripts\query-reforger-data.py examples <topic> --limit 8
py -3 scripts\query-reforger-data.py files <query> --limit 8
py -3 scripts\query-reforger-data.py snippet <file> --line <n> --context <n>
```

Search rules:

- Start with `lookup` for common tasks, then refine with exact `symbol`, `method`, `attribute`, `inherits`, `examples`, and `files` searches.
- Use exact searches when a symbol or method name is known.
- Use generated game-data records for API signatures.
- Use handwritten game-source records for implementation patterns.
- Treat exact API verification as applying to every meaningful emitted API call, including helper calls used inside the code body.
- Prefer source-backed idioms from snippets/examples over composing generic calls unless the composition is also source-backed.
- Use `files` when broad `lookup` or `examples` results are too generic.
- Use `snippet` only after selecting an exact file and line from query output.
- If `lookup` is unmatched or ambiguous, refine the search. Do not force an unrelated recipe.

## Game Data

If `raw/game-data` is missing or stale, refresh only raw game data:

```powershell
py -3 scripts\update-reforger-data.py --if-needed
```

Use `raw/game-data` through the query script. Do not load broad raw data into context when a bounded query or snippet will answer the question.

## Verification

Before finalizing:

1. Re-read the references for the touched systems.
2. Confirm every meaningful emitted API call through `scripts/query-reforger-data.py`.
3. Inspect relevant example files or snippets for both task behavior and helper-call idioms.
4. Run available targeted checks.
5. State what was changed, what APIs/idioms were verified, and what still requires Workbench, runtime, multiplayer, dedicated-server, packaging, editor, or asset validation.
