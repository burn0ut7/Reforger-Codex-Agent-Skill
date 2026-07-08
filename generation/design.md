# Reforger Skill Generation Design

This is the generation-only master design for the future Reforger `SKILL.md`.
Use this file, the current `references/` set, and the approved game-data tooling model to generate the runtime skill.

Do not use an existing `SKILL.md` as source material for future generations. `SKILL.md` is an output artifact, not an input authority. If this design conflicts with an older `SKILL.md`, this design wins for generation.

## Source Authority And Runtime Boundary

Generation sources:

- `generation/reference-builder.md` is the contract for generating and reviewing runtime references.
- `generation/tooling-game-data-lookup.md` defines the low-context game-data lookup model.
- `generation/indexer-game-data.md` defines generated game-data index artifacts.
- `generation/searcher-game-data.md` defines the query script contract and bounded lookup behavior.
- `generation/wiki-docs-indexing.md` defines wiki cache/indexing as generation-time source preparation.
- `generation/refresh-reforger-sources.md` defines the generation-time refresh orchestration model.
- Wiki cache/indexes and official samples may be used while generating references, but they are not runtime dependencies.

Runtime skill sources:

- The generated `SKILL.md` may use `references/`.
- The generated `SKILL.md` may use `raw/game-data/`.
- The generated `SKILL.md` may use `scripts/query-reforger-data.py`.
- The generated `SKILL.md` may use `scripts/update-reforger-data.py` only to generate or refresh raw game data.

Runtime skill prohibitions:

- Do not route runtime Codex to `generation/`.
- Do not route runtime Codex to wiki cache/index files.
- Do not route runtime Codex to official samples as required source truth.
- Do not route runtime Codex to `scripts/refresh-reforger-sources.py`.
- Do not route runtime Codex to `scripts/index-reforger-data.py`.
- Do not route runtime Codex to `scripts/update-reforger-wiki-docs.py`.
- Do not route runtime Codex to `scripts/index-reforger-wiki-docs.py`.
- Do not route runtime Codex to validation scripts or human search exports.

The generated skill should be lean. It is a router, action loop, search guide, and verification contract for Codex. Detailed domain knowledge belongs in `references/`, and exact APIs belong in game-data query results.

## Future `SKILL.md` Contract

The future `SKILL.md` must be written for Codex, not a human reader. It must be read in full when the skill triggers.

Mandatory behavior:

- Read every relevant runtime reference in full before non-trivial Reforger work.
- Read multiple references when a task crosses systems.
- Do not search references instead of reading them.
- Use real Reforger APIs from game-data search; never guess API names, signatures, attributes, inheritance, or lifecycle methods.
- Verify every meaningful Reforger API call emitted in generated code, including helper calls, not only the main task API.
- Use the search commands in references as starting points, then search for closer task-specific context when needed.
- Find, open, and read relevant source examples before writing API-sensitive code.
- Use source snippets and examples to infer idiomatic usage patterns.
- Prefer direct source-backed APIs and idioms over composing generic calls, unless the generic composition is also source-backed and justified.
- Treat examples as guides, not law.
- Prefer the smallest correct change that preserves current behavior.
- Keep local work local.
- Do not introduce managers, services, registries, wrappers, broad validation, or extra settings unless the request or demonstrated defect requires them.
- Break complex or cross-system work into small verified slices.
- Reread `SKILL.md` when the task becomes complex, crosses systems, or Codex is unsure whether the rules are being followed.
- Self-audit before edits, between slices, and before the final response.
- Do not modify the skill, references, or skill tooling unless the user explicitly asks and confirms that change.

Required `SKILL.md` sections:

- Frontmatter with only `name` and `description`.
- A concise action loop: route, read references, query APIs, inspect examples/snippets, implement, verify.
- A piecemeal work strategy for complex tasks.
- A routing table for every runtime reference.
- A search guide for `scripts/query-reforger-data.py`.
- Game-data generation instructions for missing or stale `raw/game-data`.
- Verification guidance for Workbench, runtime, multiplayer, dedicated server, packaging, editor, and asset validation when relevant.

The action loop must require slice-level verification. For each slice, Codex should route to the smallest reference set, read those references in full, query exact APIs, inspect source examples/snippets, implement only that slice, verify it, then reassess before continuing. The skill should explicitly require Codex to ask whether it is following `SKILL.md`, whether references were read, whether every emitted API and helper-call idiom was verified, and whether the change is still the smallest correct local change.

## Piecemeal Runtime Strategy Requirement

The generated `SKILL.md` must make piecemeal work a first-class runtime behavior, not just a general preference.

Required behavior:

- For any complex, multi-file, cross-system, or uncertain task, Codex must break the work into the smallest useful slices.
- Before each slice, Codex must stop and think: am I being useful, am I following `SKILL.md`, have I read the right references, have I searched real APIs, and am I following the skill's best practices?
- During each slice, Codex must keep scope local and implement only the current verified change.
- After each slice, Codex must verify what can be verified, state what remains unverified, and reassess whether another slice is still needed.
- For generated code, Codex must verify the actual code body, including helper APIs, formatting/logging/resource/UI/component calls, and common idioms.
- If the answer to any self-check is weak or uncertain, Codex must reread `SKILL.md`, reroute to the right references, and search closer game-data context before continuing.
- The generated skill should use strict `MUST` language for this behavior while staying compact.

## Reference Routing Table Requirements

The future `SKILL.md` must include a routing table that covers every current runtime reference. Each route should name when to read that reference and likely adjacent references for cross-domain tasks.

Required reference routes:

| Reference | Primary Use |
| --- | --- |
| `references/start-here-source-authority.md` | Source hierarchy, runtime boundaries, lookup-first behavior, general orientation. |
| `references/mod-projects-addons-workshop.md` | Addon/project setup, `.gproj`, local mod layout, publishing, Workshop, packaging checks. |
| `references/enfusion-language-and-script-editor.md` | Enforce/Enfusion syntax, language rules, values/operators/keywords, Script Editor usage. |
| `references/script-events-actions-and-patterns.md` | Gameplay scripting patterns, script structure, events/invokers, user actions, logging patterns. |
| `references/api-lookup-and-common-symbols.md` | API lookup behavior, common symbol routes, search command patterns. |
| `references/resource-manager-file-types-and-editors.md` | Resource Manager surfaces, file types, editor tools, Resource Manager plugins. |
| `references/prefabs-configs-containers-and-catalogs.md` | Prefab/config/resource data modeling, BaseContainer, ResourceName, catalogs. |
| `references/entities-components-and-lifecycle.md` | Entity/component lifecycle, event masks, activeness, component wiring, action contexts. |
| `references/multiplayer-replication-and-authority.md` | Authority/proxy/owner, replication, RPC, RplProp/RplRpc, JIP, dedicated-server verification. |
| `references/server-hosting-startup-and-runtime.md` | Server config, startup parameters, hosting, management, RCON/A2S, runtime validation. |
| `references/workbench-plugins-and-editor-tools.md` | Workbench plugin authoring and editor extension surfaces. |
| `references/diagnostics-testing-and-performance.md` | Diag Menu, autotests, profiling, FPS diagnostics, performance validation. |
| `references/scenario-framework.md` | Scenario Framework hierarchy, setup, components, activation/conditions/actions, debugging. |
| `references/game-master-factions-tasks-and-modes.md` | Game Master, factions, tasks, game modes, Conflict, Capture & Hold, notifications, hints. |
| `references/terrain-creation-and-world-setup.md` | Terrain foundation, world setup, heightmaps, terrain entity, environment baseline, 2D maps. |
| `references/world-editor-tools-generators-and-navmesh.md` | World Editor tools, generators, shape/vector tools, navmesh workflows. |
| `references/asset-import-models-materials-and-props.md` | Asset import, FBX/model pipeline, Blender tools, materials/textures, props, LOD, collision, particles. |
| `references/weapons-prefabs-attachments-and-firearms.md` | Weapon creation, weapon prefab/config setup, attachments, optics, suppressors, magazines/ammo routes. |
| `references/character-gear-inventory-and-arsenal.md` | Character gear, headgear, vests, inventory, protection, arsenal exposure. |
| `references/vehicles-creation-simulation-and-compartments.md` | Vehicle creation, simulation, compartments, seats, controllers, damage/fuel/turrets. |
| `references/animation-graphs-weapon-animation-and-export.md` | Animation Editor, graphs/nodes, state machines, procedural animation, export profiles, weapon animation. |
| `references/audio-editor-signals-and-sound-systems.md` | Audio Editor, signals, DSP nodes, sound events/components, music, occlusion, radio, VoN audio side. |
| `references/ui-layouts-dialogs-and-menus.md` | UI layouts, dialogs, widgets, tooltips, HUD/menu routes, layout-to-script workflows. |
| `references/ai-behavior-commanding-and-debug.md` | Behavior Editor, AI nodes, AI debug, commanding behavior, AI validation. |
| `references/examples-and-sample-patterns.md` | Example routing, official sample intent, game-source example query routes. |
| `references/common-task-recipes.md` | Compact task recipes that route to one primary reference plus query commands. |

The routing table must not replace reading. When a task matches a reference, Codex must read the relevant reference in full before acting.

## Search And API Lookup Model

The future `SKILL.md` must make `scripts/query-reforger-data.py` the normal API lookup path.

Supported query commands to document:

- `lookup "<task phrase>"` for bounded task-oriented bundles.
- `symbol <name>` for classes, enums, functions, methods, properties, and common symbols.
- `method [owner] <name>` for method/function signatures.
- `attribute <name>` for attributes such as replication and editor metadata.
- `inherits <class>` for base/derived relationships.
- `examples <topic>` for implementation-pattern routes.
- `files <query>` for source discovery by symbol, topic, module, or path text.
- `snippet <file> --line <n> --context <n>` for bounded source context.

Search rules for the generated skill:

- Query before writing API-sensitive code.
- Treat exact API verification as covering every meaningful emitted API call, including helper calls inside generated code.
- Use exact searches when the symbol or method is known.
- Prefer generated game-data records for API signatures.
- Prefer handwritten game-source records for examples and implementation patterns.
- Prefer source-backed idioms from snippets/examples over composing generic calls unless the composition is also source-backed.
- Use `files` to discover closer source context when a broad `lookup` or `examples` result is too generic.
- Use `snippet` only after selecting an exact file and line.
- Do not load broad API dumps into context.
- Do not assume examples are current API truth; verify symbols and methods separately.
- If `lookup` is unmatched or ambiguous, refine with `symbol`, `method`, `attribute`, `inherits`, `examples`, and `files` rather than forcing an unrelated recipe.

Runtime examples may include commands like:

```powershell
py -3 scripts\query-reforger-data.py lookup "make a replicated component" --limit 8
py -3 scripts\query-reforger-data.py symbol ScriptComponent --kind class --exact
py -3 scripts\query-reforger-data.py method IEntity FindComponent --exact
py -3 scripts\query-reforger-data.py attribute RplProp --exact
py -3 scripts\query-reforger-data.py examples replication --limit 8
py -3 scripts\query-reforger-data.py files SCR_ScenarioFrameworkTask --limit 8
py -3 scripts\query-reforger-data.py snippet scripts/Game/Some/File.c --line 120 --context 30
```

The command examples are examples only. Codex should search for closer names, topics, files, and snippets based on the actual task.

## Game Data Update Resources

Generation-side tooling may use the full source refresh model documented in `generation/refresh-reforger-sources.md`, the game-data indexer design, the searcher design, and wiki indexing docs.

The generated runtime `SKILL.md` must only include the game-data updater path needed to make `raw/game-data` available:

```powershell
py -3 scripts\update-reforger-data.py --if-needed
```

Runtime game-data update rules:

- Use `scripts/update-reforger-data.py --if-needed` when `raw/game-data` is missing or stale.
- Use `scripts/update-reforger-data.py --check` only to check remote status without fetching or writing.
- Do not instruct runtime Codex to run the game-data indexer directly.
- Do not instruct runtime Codex to run wiki or sample update scripts.
- Do not instruct runtime Codex to run the refresh orchestrator.

`scripts/update-reforger-data.py` owns only raw game data: checking remote commit, pulling sparse `scripts/` from BohemiaInteractive's script diff repository, writing `raw/game-data/manifest.json`, and cleaning repository metadata from `raw/game-data`.

## Reference Generation Workflow

When creating or revising any runtime reference:

1. Read `generation/reference-builder.md` first.
2. Review relevant wiki index records and structured wiki data.
3. Query exact game APIs and source examples through the game-data search tooling.
4. Review official samples only as generation-time layout/example signals.
5. Generate one reference at a time.
6. Include the required standard headings from the reference builder.
7. Preserve wiki workflow detail, warnings, tables, fields, procedures, and official links.
8. Route exact APIs to query commands instead of embedding API dumps.
9. Score the reference with the builder rubric.
10. Revise until it reaches the required score and has no automatic failure.

Runtime references should be dense and useful for Codex, but they must not contain raw wiki dumps, raw HTML, local absolute paths, broad API dumps, or copied source bodies.

## Do Not Leak To `SKILL.md`

The following are design/generation-only details and must not appear in the generated runtime `SKILL.md`:

- `generation/` paths.
- Wiki scraping instructions.
- Wiki cache/index file paths.
- Sample update or sample inspection requirements.
- Reference-builder scoring rubric.
- Human search exports.
- Search quality validators.
- Refresh orchestration.
- Indexer implementation details.
- Instructions to use `scripts/index-reforger-data.py`.
- Instructions to use `scripts/update-reforger-wiki-docs.py`.
- Instructions to use `scripts/index-reforger-wiki-docs.py`.
- Instructions to use `scripts/update-reforger-samples.ps1`.

The generated `SKILL.md` can say references were curated from source material, but it must not ask runtime Codex to inspect the generation pipeline.

## Future `SKILL.md` Generation Checklist

Before accepting a generated `SKILL.md`, verify:

- It has only `name` and `description` frontmatter fields.
- It is concise enough to serve as a router and action loop.
- It includes every runtime reference in the routing table.
- It requires reading relevant references in full.
- It requires game-data search before API-sensitive work.
- It requires verification of all meaningful emitted APIs, including helper calls.
- It requires source-backed idioms and does not treat task-level API verification as sufficient for generated code correctness.
- It requires piecemeal task decomposition for complex or cross-system tasks.
- It requires self-audit checkpoints before edits, between slices, and before final response.
- It requires rereading `SKILL.md` when complexity or uncertainty increases.
- It explains `query-reforger-data.py` commands at a practical level.
- It includes raw game-data update instructions using `py -3 scripts\update-reforger-data.py --if-needed`.
- It does not mention `generation/`, wiki cache/indexes, samples, refresh scripts, indexer scripts, validators, or human logs.
- It states examples are guides, not law.
- It states search commands are starting points, not exhaustive answers.
- It states Codex must inspect closer relevant examples and snippets when needed.
- It includes the smallest-correct-change and local-work-local guardrails.
- It says not to modify the skill unless explicitly asked and confirmed.

## Validation For This Design

This design is correct when:

- `generation/design.md` exists and is the only changed file for this step.
- `SKILL.md` is untouched.
- No file under `references/` is changed.
- The current runtime reference list is represented in the routing requirements.
- Runtime allowed sources are limited to `references/`, `raw/game-data/`, `scripts/query-reforger-data.py`, and `scripts/update-reforger-data.py`.
- Runtime forbidden sources include `generation/`, wiki docs/cache/indexes, samples, refresh scripts, indexers, validators, and human logs.
- Game-data update instructions use the actual updater interface.
