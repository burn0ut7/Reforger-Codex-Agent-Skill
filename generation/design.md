# Arma Reforger Skill Generation Design

This file is the design source for regenerating the Arma Reforger Codex skill, its references, and its review output. It is written for Codex. Use judgment, inspect the raw data, and keep the final skill compact.

## Goal

Create a Codex skill for Arma Reforger modding and Enfusion Script work. `SKILL.md` should be a router and guardrail, not a large reference. Detailed information belongs in topical files under `references/`.

The skill should help Codex:

- Write and review Enfusion Script for Arma Reforger.
- Choose the right topical reference before non-trivial changes.
- Look up uncertain APIs before using them.
- Avoid common Reforger lifecycle, networking, prefab, Workbench, and performance traps.
- Verify code changes before final response.

## Source Priority

Use sources in this order:

1. Official wiki/docs data from `raw/wiki-docs/` as the highest-priority source of truth.
2. Official Bohemia sample mod data from `raw/samples/` for concrete examples and real project layouts.
3. Extracted game script/API data from `raw/game-data/` for exact API names, signatures, inheritance, and source paths.

Do not use existing `SKILL.md`, old generated references, old review output, internet searches, model memory, copied notes, or previous summaries as source material. This prevents cascading mistakes.

Generated references created during the current run may be cross-checked against each other for consistency, but they are outputs. They are not source material.

Samples are examples, not the highest authority. If samples conflict with current wiki/docs or current extracted API signatures, prefer wiki/docs and raw game API data.

## Refresh Rules

Refresh raw data only when asked or when required raw data is missing.

- Missing game data: run `scripts/update-reforger-data.ps1`.
- Missing wiki docs: run `scripts/update-reforger-wiki-docs.py`.
- Missing official samples: run `scripts/update-reforger-samples.ps1`.
- User asks to refresh game data: run the game data script.
- User asks to refresh docs/wiki data: run the wiki docs script.
- User asks to refresh samples/example data: run the samples script.
- User asks to refresh all data: run game data, wiki docs, and samples scripts.
- Otherwise, use the existing `raw/` data.

## Raw Inputs

Expected raw inputs:

- `raw/wiki-docs/schema.json`
- `raw/wiki-docs/pages/*.json`
- `raw/wiki-docs/markdown/*.md`
- `raw/wiki-docs/html/*.html`
- `raw/game-data/manifest.json`
- `raw/game-data/api-schema.json`
- `raw/game-data/api-index.md`
- `raw/game-data/addons_core/...`
- `raw/samples/README.md`
- `raw/samples/SampleMod_*/README.md`
- `raw/samples/SampleMod_*/Scripts/**/*.c`
- `raw/samples/SampleMod_*/Configs/**/*.conf`
- `raw/samples/SampleMod_*/Prefabs/**/*.et`
- `raw/samples/SampleMod_*/Worlds/**/*.ent`

## Output Layout

Use this layout:

```text
reforger/
  SKILL.md
  generation/
    design.md
    review.md
  scripts/
    update-reforger-data.ps1
    update-reforger-wiki-docs.py
    update-reforger-samples.ps1
    build-reforger-extended-api-reference.py
  references/
    overview.md
    scripting-core.md
    scripting-language.md
    entity-component-lifecycle.md
    networking-multiplayer-replication.md
    resources-prefabs-configs.md
    workbench-tools-debugging.md
    scenario-framework-game-master.md
    terrain-world-editor.md
    assets-weapons-vehicles-animation-audio.md
    server-runtime-packaging.md
    examples-patterns.md
    common-task-recipes.md
    api-main.md
    api-extended.md
  raw/
    game-data/
    wiki-docs/
    samples/
    tools/
```

`generation/review.md` is overwritten or created on every skill-generation run. It does not need timestamps in the filename.

Only create folders when needed.

## Reference Strategy

References should be useful to load into context. Keep them dense, factual, and navigable. Avoid giant dumps when a summary plus source pointers and search terms is better.

References are written for Codex first, but they must still render cleanly for a human reviewer on GitHub. Do not leave broken markdown tables, raw HTML fragments, navigation junk, crawl artifacts, one-line dumps, or malformed headings in generated references.

Size guidance:

- Keep normal topical references roughly 300-900 lines when possible.
- Split a reference if it grows too large to load usefully for a single task.
- Prefer section tables, concise examples, source paths, and search terms over long copied passages.
- `api-extended.md` is exempt from size limits because it is search-only fallback data.
- For any large reference, include a short table of contents and useful search terms near the top.

Each topical reference should include several examples and sections where they are useful. Use as many as needed to make the reference practical, while keeping the file focused and context-efficient:

- When to read it.
- Raw source files used.
- Key official wiki/doc guidance.
- Synthesized rules and task-focused takeaways before raw excerpts.
- Concrete examples from docs when useful.
- Common mistakes and traps.
- Relevant APIs, with enough signatures to code safely.
- Search terms for follow-up lookup.
- Direct code, config, project-layout, or command examples where the raw sources support them. Include multiple examples when a topic has multiple common workflows or failure-prone patterns.

Use wiki/docs information as the strongest source. Use game API data to verify names, signatures, inheritance, methods, properties, and source paths.

Use official samples to add concrete examples and real file-layout patterns. Prefer small excerpts and summaries over large code dumps. For script examples, include enough context to show the pattern, then cite the sample path. For asset-heavy samples, summarize the structure and identify the relevant `.conf`, `.et`, `.ent`, or README files instead of copying bulk asset data.

Markdown quality rules:

- Use one `#` title per reference, `##` for main sections, and `###` only when needed.
- Include a short table of contents or search-term block for references over roughly 100 lines.
- Use fenced code blocks with language tags such as `c`, `json`, `text`, or `powershell`.
- Convert scraped tables that do not render cleanly into bullet lists.
- Remove meaningless copied UI text such as `Copy`, edit buttons, image-only links, icons, and navigation labels.
- Normalize encoding artifacts and punctuation in generated references.
- Cite source paths and URLs visibly near the relevant content.
- Summarize messy excerpts instead of copying raw scraped blocks.

Code example rules:

- Examples are additive. They must not replace source-grounded guidance, gotchas, or API notes.
- Scripting-heavy references should include several direct code examples when raw sources support them, not just one token example.
- Config, prefab, resource, world, server, and packaging references should include several direct config, path-layout, command, or project-layout examples when raw sources support them.
- Prefer short examples from official docs and official samples. Do not copy large files.
- Label examples as `official-doc-example`, `official-sample-excerpt`, `generated-pattern-from-docs`, `example-observed`, or `pseudocode`.
- For `generated-pattern-from-docs`, `example-observed`, and `pseudocode`, state which APIs must be verified in `api-main.md` or `api-extended.md`.
- Do not invent unsupported complex examples. If the raw data does not support a complete example, provide a smaller verified example plus a clear uncertainty note.
- If an API appears only in comments, wiki prose, or samples but not clearly in the schema, mark it `example-observed, verify in project`.

Normalize common crawl artifacts before writing generated references:

- Replace mojibake punctuation such as `â€“`, `â€œ`, `â€�`, `â€™`, `â€˜`.
- Replace warning/info symbols with readable labels such as `WARNING` and `NOTE`.
- Remove image-only markdown noise unless the image path is important.
- Keep raw files unchanged; normalize only generated references.

## Common Task Recipes

Create `references/common-task-recipes.md` as a task-first companion to the topical references.

Purpose: let Codex solve common Reforger scripting tasks without having to infer recipes from raw doc excerpts.

Each recipe should include:

- When to use it.
- Required reference files.
- Minimal code shape or pseudocode.
- APIs that must be verified.
- Common traps.
- Source wiki/sample/API paths.

Required recipes:

- Create a `ScriptComponent` and `ScriptComponentClass`.
- Add `ComponentEditorProps` and editable `[Attribute]` fields.
- Print/debug with `Print` and `PrintFormat`.
- Get an entity's origin and transform.
- Move or teleport an entity with `IEntity.SetOrigin` or transform APIs.
- Get the local player or controlled entity, with a warning if the accessor is only found in docs/examples and not clearly present as a schema method.
- Register frame/update events safely.
- Add or modify a user action.
- Spawn an entity or prefab.
- Load a resource/prefab.
- Basic replicated/RPC action pattern.
- Create a Workbench plugin command.

Recipes must not pretend uncertain APIs are verified. If an API appears only in comments or examples, mark it as "example-observed, verify in project".

## Reference Files

### `overview.md`

General Reforger context and modding map. Cover Enfusion, Workbench, addons, scripts, resources, prefabs, configs, world data, assets, Workshop, and where the raw data came from.

### `scripting-core.md`

Primary scripting reference. This should be the richest topical reference.

Use docs such as scripting first steps, scripting modding, examples, best practices, do's and don'ts, conventions, performance, ScriptInvoker, and script profiling.

Use official samples such as `SampleMod_ModdedScript` and script files from other sample mods for concrete examples.

Cover file/class organization, event/callback patterns, lifecycle patterns, modded class patterns, performance, debugging, profiling, and gotchas.

Include direct examples for a minimal script file/class, a modded class override from official samples, `Print`/`PrintFormat`, and `ScriptInvoker` where supported by raw sources.

### `scripting-language.md`

Enfusion Script language mechanics.

Cover keywords, operators, values, automatic reference counting, classes, inheritance, constructors/destructors, annotations/attributes, config objects, JSON, preprocessor directives, and macros.

Include direct examples for typed variables, arrays, loops, conditionals, class/method style, `ref` ownership/ARC-safe patterns, and JSON/config object usage where supported by raw sources.

### `entity-component-lifecycle.md`

Entity and component coding patterns.

Use docs such as Create a Component, Create an Entity, Entity Lifecycle, Entity Activeness, BaseDoorComponent, Prefab Data, and Prefabs Basics.

Use official sample `.c`, `.et`, and `.conf` files where they demonstrate entity/component wiring.

Cover entity/component relationships, lifecycle callbacks, update behavior, prefab integration, safe extension, and lifecycle traps.

Include direct examples for `ScriptComponentClass` plus `ScriptComponent`, `ComponentEditorProps`, editable `[Attribute]` fields, `EOnInit`, and entity movement/teleport with `IEntity.SetOrigin` or transform APIs. If player access uses `g_Game.GetPlayer()` or another accessor that is not clearly present in schema, label it `example-observed, verify in project`.

### `networking-multiplayer-replication.md`

Multiplayer and network-safe scripting.

Use docs such as Multiplayer Scripting and any replication/server/network material. Cover authority, ownership, replication, RPC/network event patterns if present, client/server execution, synchronized state, debugging, and common multiplayer traps.

Use samples only if they show real multiplayer or replicated setup. Do not infer networking rules from samples that are not explicitly network-focused.

Include direct examples for authority/proxy/owner checks and a minimal RPC or replicated-property pattern if raw docs/API data supports it. Include one warning anti-example for client-local state/entity changes that should be authority-gated.

### `resources-prefabs-configs.md`

Resources, prefabs, config classes, UI/layout resources, and editor data.

Use Resource Manager, Resource Usage, Config Editor, Create a Config Class, Prefab Data, Prefabs Basics, dialog/layout/widget docs, and related API data.

Use official sample `.conf`, `.et`, `.ent`, and README files to show real resource, prefab, entity catalog, arsenal, editable prefab, and config layout patterns.

Include direct examples for config snippets, resource/prefab paths, entity catalog or arsenal config layout, and resource load or prefab spawn code if supported by raw API data.

### `workbench-tools-debugging.md`

Workbench, Script Editor, plugins, diagnostic tools, and profiling.

Use Workbench plugin docs, Script Editor docs, Diag Menu, Script Profiling, Resource Manager plugin docs, and World Editor plugin docs.

Use `SampleMod_WorkbenchPlugin` as the main concrete source for Workbench plugin examples.

Include direct examples for a `WorkbenchPluginAttribute` plugin class, a `Workbench.GetModule(...)` pattern if supported, and diagnostic/profiling commands or scripts where raw docs support them.

### `scenario-framework-game-master.md`

Scenario Framework, Game Master, tasks, factions, and game mode content.

Use Scenario Framework, setup/update tutorials, Game Master tutorials, Task System Usage, Faction Creation, Entity Catalog, and Game Identity.

Use `SampleMod_NewFaction`, sample mission/config files, entity catalog configs, and relevant `.ent` files for real faction/scenario examples.

Include direct examples for faction config paths, entity catalog config structure, and a scenario/Game Master setup checklist with source paths.

### `terrain-world-editor.md`

Terrain creation, world editing, generators, navmesh, roads, rivers, and map tooling.

Use Terrain Tutorial, New Terrain Setup, Terrain Entity, World Editor docs, generator/tool pages, navmesh docs, and terrain preparation docs.

Use samples only where they include relevant world/editor files. Do not treat asset showcase worlds as general terrain guidance unless the docs support that pattern.

Include direct examples for world file layout, terrain/world-editor path layout, and generator/navmesh/road/river checklist items from docs.

### `assets-weapons-vehicles-animation-audio.md`

Asset workflows that affect code and mod integration.

Use Assets, Textures, FBX Import, Model Performance, weapon pages, vehicle pages, animation editor pages, audio editor pages, sound component docs, and character gear docs.

Use official sample mods for concrete file layouts: new/modded weapons, new/modded cars, new character, new prop, replacement, animation workshop, and cinematic tutorial.

Include direct examples for weapon, vehicle, character gear, animation, and audio path/config layouts where official samples or docs provide them.

### `server-runtime-packaging.md`

Runtime, startup, server hosting/config, Workshop, packaging, and deployment.

Use Startup Parameters, Server Config, Server Hosting, Server Management, Workshop, Backend API, REST API Usage, and system requirements.

Use samples for packaging/addon layout examples only. Do not use samples as server configuration authority unless the sample explicitly contains server/runtime configuration.

Include direct examples for startup parameters, server config fields, `.gproj` layout, and addon/project packaging layout when raw sources provide them.

### `examples-patterns.md`

Official sample mod patterns and project layouts.

Use `raw/samples/README.md`, `raw/samples/SampleMod_*/README.md`, sample `.c`, `.conf`, `.et`, `.ent`, and `.gproj` files.

Purpose: give Codex a compact map of official sample projects and reusable example patterns without bloating every topical reference.

Include:

- Sample mod inventory and what each sample demonstrates.
- Script examples worth reusing, with short fenced `c` excerpts and source paths.
- Common addon/project layout patterns.
- Config, prefab, entity catalog, arsenal, world, Workbench plugin, weapon, vehicle, character, faction, replacement, cinematic, and animation sample patterns.
- Cross-links to topical references that should use each pattern.

Do not copy large asset files or large prefab/config bodies. Summarize structure and cite paths.

### `common-task-recipes.md`

Common Reforger coding recipes generated from official docs, official samples, and verified API signatures.

Use this as a fast path after `SKILL.md` routing when the user asks for a common task such as "make a component", "teleport a player", "spawn a prefab", "add a user action", or "make a simple RPC".

This reference should be practical and explicit. It should avoid long raw excerpts and instead point back to topical references for deep background.

Every recipe should include a direct example block when raw sources support it. If a complete verified code example is not available, include a smaller verified snippet plus an explicit uncertainty note.

### `api-main.md`

Create this during the AI reference-building pass, not with a deterministic script.

Purpose: compact top-API reference for normal coding work. It should be curated by Codex while building the topical references, using official wiki/docs as source of truth and raw API schema for signatures.

Keep this file useful and bounded. Include only APIs that are clearly important for common Reforger scripting and modding tasks. Prefer APIs that appear in official docs, examples, lifecycle patterns, networking, entity/component work, resources/prefabs/configs, Workbench tooling, UI/input, game/world/player systems, scenarios, weapons, vehicles, animation, and audio.

Mandatory `api-main.md` coverage:

- `IEntity`: `GetOrigin`, `SetOrigin`, `GetTransform`, `SetTransform`, `SetWorldTransform`, `GetYawPitchRoll`, `SetYawPitchRoll`, event mask/flag helpers.
- `ScriptComponent` and `ScriptComponentClass`: lifecycle events, owner access, insert/remove/delete events.
- `GenericEntity`, `GenericEntityClass`, `GenericComponent`, `GenericComponentClass`.
- `Game`: entity spawn, prefab spawn, delete APIs, and player access APIs if present in schema.
- Player access patterns: include exact schema methods when present; mark `g_Game.GetPlayer()` as example-observed if only present in docs/comments.
- `Resource`, `ResourceName`, prefab/config loading classes.
- `BaseRplComponent`, `RplRpc`, `RplProp`, `OnRpl`, replication role/ownership APIs.
- `ActionManager`, `InputManager`, user action related APIs if present.
- `WorkbenchPlugin`, `ScriptEditor`, `WorldEditor`, `ResourceManager`.
- UI/widget basics such as `Widget`, `UIWidget`, list/text/button widgets.
- Common asset/gameplay domains: weapon, vehicle, inventory, audio, animation, task, faction, scenario.

For every curated API entry, prefer concrete methods over class stubs. If an expected common API is missing from schema, add a "Not found / verify manually" note rather than omitting the gap.

### `api-extended.md`

Create this with `scripts/build-reforger-extended-api-reference.py`.

Purpose: exhaustive fallback search reference. Include every class, enum, global function, method, property, doc comment, signature, source file, line, inheritance value, modifier, and attribute available in `raw/game-data/api-schema.json`.

Load this only when topical references and `api-main.md` do not answer an API question, or when an exact signature is uncertain.

## `SKILL.md` Requirements

`SKILL.md` must stay concise. It should contain:

- Frontmatter with only `name` and `description`.
- Basic Arma Reforger, Enfusion, Workbench, and scripting context.
- Mandatory guardrails:
  - Read this before writing code. This file is the router and guardrail. Open the relevant reference before non-trivial code changes.
  - Prefer the smallest correct change that preserves current behavior.
  - Keep local work local. Do not introduce managers, services, registries, wrappers, broad validation, or extra settings unless the request or demonstrated defect requires them.
  - Look up every uncertain API in the topical reference, then `api-main.md`, then `api-extended.md`.
- A routing table for every reference file.
- Top things to know.
- Top mistakes.
- Top traps.
- Verification loop before final response.

Suggested routing:

| Task | Read |
| --- | --- |
| General orientation | `references/overview.md` |
| Non-trivial script change | `references/scripting-core.md` |
| Language syntax, ARC, config, JSON, macros | `references/scripting-language.md` |
| Entity/component lifecycle | `references/entity-component-lifecycle.md` |
| Multiplayer, authority, replication | `references/networking-multiplayer-replication.md` |
| Prefabs, resources, configs, UI layouts | `references/resources-prefabs-configs.md` |
| Workbench, plugins, debugging, profiling | `references/workbench-tools-debugging.md` |
| Scenario Framework, Game Master, tasks, factions | `references/scenario-framework-game-master.md` |
| Terrain, World Editor, navmesh, map tools | `references/terrain-world-editor.md` |
| Assets, weapons, vehicles, animation, audio | `references/assets-weapons-vehicles-animation-audio.md` |
| Server config, startup, Workshop, packaging | `references/server-runtime-packaging.md` |
| Official sample layouts and examples | `references/examples-patterns.md` |
| Common task recipes | `references/common-task-recipes.md` |
| Common API lookup | `references/api-main.md` |
| Exhaustive API fallback | `references/api-extended.md` |

## Generation Workflow

1. Apply the refresh rules. Pull game data, wiki docs, or official samples only when asked or when the required raw folder/file is missing.
2. Confirm required raw inputs exist: wiki schema/markdown/pages, game API schema/manifest, and official samples.
3. Run `scripts/build-reforger-extended-api-reference.py` to regenerate `references/api-extended.md` from raw game API data.
4. Load and inventory raw sources:
   - Wiki docs: titles, URLs, headings, markdown paths, page JSON, text length, categories.
   - Samples: README files, `.c`, `.conf`, `.et`, `.ent`, and project layout paths.
   - Game API schema: classes, enums, functions, methods, properties, docs, signatures, source files.
5. Create a source inventory for the review: available raw inputs, wiki counts, sample counts, API counts, skipped/empty pages, duplicate candidates, and source warnings.
6. Clean the wiki source set. Remove or flag empty pages, duplicate pages, broken category shells, and pages with no useful text.
7. Classify wiki pages, sample files, and APIs into the reference topics in this design.
8. Build topical references from official wiki/docs first. Preserve the docs as the main source of truth.
9. Add direct code, config, command, and project-layout examples where they improve the reference. Examples are additive to the source guidance, must be source-labeled, and must cite official wiki/doc, sample, or API paths.
10. Build `references/examples-patterns.md` from official samples as the central sample layout/example map.
11. Build `references/common-task-recipes.md` from official docs, samples, and verified APIs. Include direct example blocks for supported recipes.
12. Verify every API name/signature used in topical references, examples, and recipes against `raw/game-data/api-schema.json`.
13. Curate `references/api-main.md` while building references. Include only the most useful APIs for common Reforger coding and cite exact signatures from raw game data.
14. Record expected-common API gaps in `api-main.md` and `generation/review.md`.
15. Check markdown quality for every reference: valid headings, fenced code blocks, readable lists/tables, source citations, no raw crawl noise, and clean GitHub rendering.
16. Check reference size and usefulness. Split or trim anything that creates context bloat without adding practical lookup value.
17. Create `SKILL.md` as a compact router and guardrail that points to the generated references.
18. Create or validate `agents/openai.yaml` so the skill metadata matches `SKILL.md`.
19. Validate the skill folder and generated links.
20. Write `generation/review.md`, overwriting any prior review.

## Document Classification

Use deterministic title/category matching first, then Codex judgment where a page clearly spans topics.

- Scripting core: scripting first steps, examples, best practices, conventions, performance, ScriptInvoker, profiling.
- Scripting language: keywords, operators, values, ARC, config object, JSON, preprocessor, conf files.
- Entity/component: component, entity, lifecycle, activeness, prefab data, prefab basics.
- Networking: multiplayer, replication, RPC, network, authority, ownership, voice/network.
- Resources/configs/prefabs: Resource Manager, resource usage, config, prefab, layout, rich text, widget.
- Workbench/tools: Workbench, Script Editor, plugin, Diag, profiling, editor tooling.
- Scenario/Game Master: scenario, Game Master, task, faction, entity catalog, game identity.
- Terrain/world editor: terrain, World Editor, navmesh, road, river, forest, lake, generator, shape, object brush.
- Assets/weapons/vehicles/animation/audio: asset, weapon, vehicle, animation, audio, sound, FBX, texture, model, character gear.
- Server/runtime: server, startup, Workshop, backend, REST API, system requirements.
- Examples/patterns: SampleMod README files, sample scripts, sample configs, sample prefabs, sample worlds, Workbench plugin samples, addon project layout.
- Common task recipes: component creation, debug print, entity/player movement, resource loading, prefab spawning, user actions, replication/RPC, Workbench plugin commands.

## API Use

Use `raw/game-data/api-schema.json` to verify exact class names, signatures, inheritance, modifiers, attributes, source files, and line numbers.

API domains to watch:

- Entity/component: `Entity`, `Component`, `IEntity`, lifecycle names.
- Network: `Replication`, `Rpl`, `RPC`, `Network`, `Authority`, `Proxy`, `Owner`.
- Resource/config/prefab: `Resource`, `Prefab`, `Config`, `BaseContainer`, `ResourceName`.
- Input/UI: `Input`, `Action`, `Widget`, `Menu`, `Layout`, `RichText`.
- Game/player/world: `Game`, `World`, `Player`, `Chimera`, `Camera`.
- Inventory/weapon/vehicle: `Inventory`, `Weapon`, `Muzzle`, `Magazine`, `Vehicle`, `Wheeled`, `Turret`.
- Audio/animation: `Audio`, `Sound`, `Animation`, `Anim`, `Signal`.
- Scenario/Game Master/task/faction: `Scenario`, `GameMaster`, `Task`, `Faction`, `Catalog`.
- Workbench/tools: `Workbench`, `Editor`, `Plugin`, `ResourceManager`, `WorldEditor`.

## Review Output

Write one review file:

```text
generation/review.md
```

Overwrite it on every skill-generation run.

Include:

- Whether raw data was refreshed.
- Official samples repo commit and any sample-source warnings.
- Game version/build id.
- Wiki document counts and skipped pages.
- API counts.
- References written.
- Approximate size and purpose of each reference.
- How `api-main.md` was curated.
- Expected-common APIs that were missing or only found in comments/examples.
- Task recipes written and any recipe uncertainty.
- Direct examples added per reference and any references that intentionally lack examples due to missing raw support.
- Markdown quality issues found and fixed, including broken tables, missing code fences, crawl artifacts, and unreadable copied excerpts.
- Confirmation that `api-extended.md` was generated exhaustively.
- Any source-data warnings.
- Any suspected gaps.
- Manual review items.

`generation/review.md` is for auditing only. Do not use it as source material in later generations.

## Validation

Before finishing generation:

- Confirm every reference in `SKILL.md` exists.
- Confirm references use raw wiki/docs as the highest-priority source.
- Confirm official samples are used as examples only, not as rule authority over docs/API data.
- Confirm API signatures come from raw game data.
- Confirm no generated output used old generated references or old `SKILL.md` as source.
- Confirm `api-main.md` is compact and curated.
- Confirm `api-main.md` includes the mandatory common API coverage or records explicit gaps.
- Confirm `api-extended.md` is exhaustive and searchable.
- Confirm `common-task-recipes.md` exists and includes all required recipes.
- Confirm direct examples are present in scripting-heavy and task-recipe references where raw sources support them.
- Confirm examples are additive and do not replace official guidance, gotchas, or API notes.
- Confirm non-script references include useful config, path-layout, command, or project-layout examples where raw sources support them.
- Confirm every code/config example has a source label and source path or URL.
- Confirm uncertain example APIs are marked `example-observed`, `generated-pattern-from-docs`, or `pseudocode` with verification notes.
- Confirm references render as clean Markdown for GitHub review: no broken tables, malformed headings, raw HTML, raw navigation text, or unfenced code blocks.
- Confirm empty wiki pages are absent or flagged.
- Confirm scripting references are the richest references.
- Confirm API lookup routing is topical reference, then `api-main.md`, then `api-extended.md`.
- Confirm large references include search terms or a short table of contents.
- Confirm `SKILL.md` includes grep/search guidance for `api-extended.md`, `api-main.md`, and sample paths.
- Confirm `agents/openai.yaml` exists or is intentionally skipped, and matches the generated `SKILL.md`.
- Run the available skill validation tool if present, then fix any reported metadata or structure issues.

## Priority Order

If tradeoffs are needed, prioritize:

1. Official wiki/docs information as source of truth.
2. Scripting correctness.
3. Entity/component lifecycle correctness.
4. Multiplayer/replication correctness.
5. Resource/prefab/config correctness.
6. API signature accuracy from raw game data.
7. Workbench/debugging usefulness.
8. Scenario/Game Master systems.
9. Terrain/world editor.
10. Assets/weapons/vehicles/animation/audio.
11. Server/runtime/packaging.
