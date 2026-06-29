# Arma Reforger Skill Generation Design

This file is the design source for regenerating the Arma Reforger Codex skill, its references, and its review output. It is written for Codex. Use judgment, inspect the raw data, and keep the final skill compact.

## Instruction Precedence For Generation

When regenerating this skill, treat this `generation/design.md` as the controlling project specification after system/developer instructions and required skill-creation rules.

- System/developer instructions and tool safety rules still have higher priority.
- The `skill-creator` skill provides generic skill packaging rules only. It does not weaken, replace, or reinterpret this design's source, size, completeness, or audit requirements.
- If `skill-creator` says to keep a skill concise, apply that to `SKILL.md`, not to topical files under `references/`.
- If there is tension between generic skill concision and this design's reference-depth requirements, satisfy both by keeping `SKILL.md` compact and putting the detail in `references/`.
- Do not use "context efficiency", "compactness", or "the skill validated" as a reason to accept thin required references.
- Passing `quick_validate.py` only proves the folder is structurally valid. It is not evidence that this design was followed.

## Non-Negotiable Build Contract

This is a multi-pass corpus generation task, not a normal concise skill edit. Do not try to satisfy it with a compact first pass.

- Keep `SKILL.md` compact.
- Make topical references detailed enough to stand on their own for real Reforger work.
- Do not write or rewrite final `SKILL.md` until required references pass the design completeness audit.
- Do not mark a run complete if any required reference fails the audit, even when `quick_validate.py` passes.
- If context, time, or tooling is not enough to finish, stop with `generation/review.md` status `INCOMPLETE` or `STRUCTURALLY VALID BUT DESIGN-INCOMPLETE`.
- Re-read this contract, the "Generation Boundary", the "Reference Strategy", and the "Validation" sections at every phase boundary before continuing.

Minimum required reference bar before `SKILL.md` may be finalized:

- Every required reference exists.
- Every non-exempt topical reference has at least 250 nonblank lines unless marked `INTENTIONALLY SHORT` with exact sparse-source proof.
- `common-task-recipes.md`, `examples-patterns.md`, and `api-main.md` each have at least 200 nonblank lines unless marked `INTENTIONALLY SHORT` with exact sparse-source proof.
- Every reference is standalone and useful without the `raw/` directory present.
- Do not include `raw/...` paths, "Sources Used" raw-source sections, or instructions to open `raw/` files in generated references or `SKILL.md`.
- `generation/review.md` must include exact raw source provenance for every generated reference. Keep raw source paths in review/audit output, not in runtime references.
- Every applicable reference has direct examples or an explicit no-example rationale.
- Every applicable reference has `Common Traps`, `Review Checklist`, or both.
- Every applicable reference has API lookup notes, and `api-main.md` includes exact signatures for mandatory common APIs rather than only search advice. Raw source paths for those signatures belong in `generation/review.md`.

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

## Generation Boundary

The skill generation pass is AI/Codex work guided by this design. Do not create or use an ad hoc deterministic script to generate topical references, `api-main.md`, `SKILL.md`, or `generation/review.md`.

Do not do a skeleton, stub, outline-only, or "compact first pass" generation and present it as complete. A generation run is incomplete until every required reference has been filled with source-grounded detail, examples, traps, and API notes according to this design, and until `generation/review.md` records exact raw source provenance for each reference. If the available time/context is not enough to finish that standard, stop with `generation/review.md` clearly marking the run incomplete and listing exactly which files still need expansion.

Allowed deterministic generation:

- Refresh raw data with the raw-data scripts.
- Generate only `references/api-extended.md` with `scripts/build-reforger-extended-api-reference.py`.

Allowed deterministic assistance:

- Use only committed, reviewed helper scripts that are already part of this skill repository.
- Helper scripts may inventory sources, classify source candidates, extract API signature candidates, check markdown structure, count lines, detect broad/glob source citations, verify required recipes, verify `SKILL.md` links, and produce audit output.
- Helper scripts may not be generated during an ordinary rebuild run. If a helper script must change, make that an explicit repository edit, review it, and commit it like any other skill source file.
- Helper scripts may not write final topical reference prose, `api-main.md`, `SKILL.md`, or `generation/review.md` unless this design is explicitly changed later. They can produce candidate data and fail/pass reports; Codex must curate the final reference text.
- The same checked-in script version must produce stable audit behavior for every user who runs the repo with the same inputs.

Everything else must be curated by Codex during the generation pass:

- `references/overview.md`
- `references/scripting-core.md`
- `references/scripting-language.md`
- `references/entity-component-lifecycle.md`
- `references/networking-multiplayer-replication.md`
- `references/resources-prefabs-configs.md`
- `references/workbench-tools-debugging.md`
- `references/scenario-framework-game-master.md`
- `references/terrain-world-editor.md`
- `references/assets-weapons-vehicles-animation-audio.md`
- `references/server-runtime-packaging.md`
- `references/examples-patterns.md`
- `references/common-task-recipes.md`
- `references/api-main.md`
- `SKILL.md`
- `generation/review.md`

Reason: these files require judgment, source prioritization, useful compression, example selection, uncertainty labeling, and routing decisions. A rigid script tends to flatten the docs, miss nuance, and create reference slop. Stable repository helper scripts are allowed only to make the process observable and enforceable.

Do not add scripts named or shaped like `generate-reforger-skill.py`, `build-references.py`, or similar deterministic reference/skill generators unless the design is explicitly changed later. Prefer names such as `audit-references.py`, `inventory-sources.py`, or `extract-api-candidates.py` for checked-in helper scripts that do not write final prose.

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
    audit-references.py
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
  generation-only raw inputs, not required for installed skill use:
  raw/
    game-data/
    wiki-docs/
    samples/
    tools/
```

`generation/review.md` is overwritten or created on every skill-generation run. It does not need timestamps in the filename.

Only create folders when needed.

The installed/distributed skill must remain usable without `raw/`. `raw/` is a generation input cache, not a runtime dependency for Codex skill use.

## Reference Strategy

References should be useful to load into context. Keep them dense, factual, navigable, and standalone. Avoid giant dumps when a summary plus stable in-skill lookup guidance is better.

References are written for Codex first, but they must still render cleanly for a human reviewer on GitHub. Do not leave broken markdown tables, raw HTML fragments, navigation junk, crawl artifacts, one-line dumps, or malformed headings in generated references.

Runtime reference rule:

- Generated `references/*.md` and `SKILL.md` must not require, mention, link to, or instruct the agent to open `raw/` files.
- Do not include `Sources Used` sections with raw paths in references.
- Do not include raw source paths such as `raw/wiki-docs/...`, `raw/samples/...`, or `raw/game-data/...` in references or `SKILL.md`.
- References may name source families in prose, such as "official wiki docs", "official samples", or "extracted API data", but exact raw file paths belong only in `generation/review.md`.
- References must include enough summarized guidance, examples, signatures, traps, and routing to be useful without regeneration.

Size guidance:

- Keep normal topical references roughly 300-900 lines when possible. This is a real target, not decorative guidance.
- A required topical reference under 180 nonblank lines fails the completeness audit unless `generation/review.md` gives a topic-specific reason backed by sparse source material and names the exact sparse source set.
- `overview.md` may be shorter, but it still fails if it cannot route code-vs-data decisions and raw-source usage without relying on another overview.
- `common-task-recipes.md`, `examples-patterns.md`, and `api-main.md` fail the completeness audit when under 200 nonblank lines unless `generation/review.md` gives a topic-specific sparse-source justification. Generic "compactness" is not a valid justification for these central references.
- Split a reference if it grows too large to load usefully for a single task.
- Prefer section tables, concise examples, stable in-skill references, and search terms over long copied passages.
- `api-extended.md` is exempt from size limits because it is search-only fallback data.
- For any large reference, include a short table of contents and useful search terms near the top.

Completion gate:

- Do not proceed from reference writing to `SKILL.md` until the reference completeness audit passes.
- Do not report the generation as complete when a required reference is below its threshold without a specific sparse-source justification.
- Do not report the generation as complete until `generation/review.md` includes a coverage map showing which source documents, sample groups, and API domains were preserved, summarized, deferred to `api-extended.md`, or intentionally omitted.
- Do not treat line counts, successful structural validation, or a passing helper script as sufficient proof of detail retention.
- If time, context, or tooling prevents expansion, write `generation/review.md` with status `INCOMPLETE`, list every failing reference, and stop. Do not create a final-sounding summary that says the skill was rebuilt.
- "Substantially more useful than before" is not a pass condition.

Each topical reference must include several examples and sections where they are useful. Use as many as needed to make the reference practical, while keeping the file focused and context-efficient:

- When to read it.
- Generation provenance is recorded in `generation/review.md`, not in this reference.
- Key official wiki/doc guidance.
- Synthesized rules and task-focused takeaways before raw excerpts.
- Concrete examples from docs when useful.
- Common mistakes and traps.
- Relevant APIs, with enough signatures to code safely.
- Search terms for follow-up lookup.
- Direct code, config, project-layout, or command examples where the generation sources support them. Include multiple examples when a topic has multiple common workflows or failure-prone patterns.

For each required topical reference, include at least:

- A short table of contents or search-term block near the top.
- No raw-source `Sources Used` section. Exact raw wiki/sample/API files used must be listed under this reference's provenance entry in `generation/review.md`.
- At least three task-focused guidance sections unless the topic is genuinely narrow.
- At least one "Common traps" or "Review checklist" section.
- At least one direct example block or explicit "No direct example included because..." note.
- API lookup notes that point to `api-main.md` and `api-extended.md` for any uncertain method/class.
- No local raw paths, raw file references, or instructions to open `raw/`.

Line count alone is not sufficient. A 300-line file made of copied source noise, repeated bullets, or generic advice is not acceptable. Conversely, a shorter file can be acceptable only when it is dense, source-grounded, and `generation/review.md` explains why more detail would be padding.

Detail retention rules:

- Preserve every operational rule, warning, prerequisite, limitation, required file shape, required Workbench step, required config field, and API signature that would change how Codex writes or reviews a Reforger mod.
- Compress tutorial prose, screenshots, navigation text, repeated introductions, and long asset/config dumps, but keep the actionable sequence and the exact decision points.
- For each source document assigned to a reference, record in `generation/review.md` whether its actionable content was preserved as guidance, preserved as an example, summarized as background, superseded by API data, or intentionally omitted as non-actionable.
- If a source document is long or dense, the generated reference must include a coverage subsection for its major concepts rather than only naming the document in review.
- If multiple source documents repeat the same rule, merge the rule once and note the repeated source family in review.
- If the generated reference cannot preserve a detail without becoming too large, keep the task-critical detail in the topical reference and defer only exhaustive lookup material to `api-main.md` or `api-extended.md`.
- A rebuild that reduces a broad wiki/API corpus to mostly high-level summaries is incomplete even if every reference has examples, traps, and API notes.

Use wiki/docs information as the strongest generation source. Use game API data to verify names, signatures, inheritance, methods, and properties. Put exact source file paths in `generation/review.md`, not runtime references.

Use official samples to add concrete examples and real file-layout patterns. Prefer small excerpts and summaries over large code dumps. For script examples, include enough context to show the pattern without requiring the raw sample file. For asset-heavy samples, summarize the structure and relevant `.conf`, `.et`, `.ent`, or README concepts instead of copying bulk asset data. Record exact sample paths in `generation/review.md`.

Markdown quality rules:

- Use one `#` title per reference, `##` for main sections, and `###` only when needed.
- Include a short table of contents or search-term block for references over roughly 100 lines.
- Use fenced code blocks with language tags such as `c`, `json`, `text`, or `powershell`.
- Convert scraped tables that do not render cleanly into bullet lists.
- Remove meaningless copied UI text such as `Copy`, edit buttons, image-only links, icons, and navigation labels.
- Normalize encoding artifacts and punctuation in generated references.
- Do not cite raw local source paths in runtime references. Cite stable public URLs only when useful and available; otherwise record exact local provenance in `generation/review.md`.
- Summarize messy excerpts instead of copying raw scraped blocks.

Code example rules:

- Examples are additive. They must not replace source-grounded guidance, gotchas, or API notes.
- Scripting-heavy references should include several direct code examples when generation sources support them, not just one token example.
- Config, prefab, resource, world, server, and packaging references should include several direct config, path-layout, command, or project-layout examples when generation sources support them.
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
- Source-family label and matching provenance entry in `generation/review.md`.

Each required recipe must be a real task recipe, not a one-line pointer. Include a short decision note when the task may be better solved with prefab/config/resource data instead of script.

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

Include direct examples for a minimal script file/class, a modded class override from official samples, `Print`/`PrintFormat`, and `ScriptInvoker` where supported by generation sources.

### `scripting-language.md`

Enfusion Script language mechanics.

Cover keywords, operators, values, automatic reference counting, classes, inheritance, constructors/destructors, annotations/attributes, config objects, JSON, preprocessor directives, and macros.

Include direct examples for typed variables, arrays, loops, conditionals, class/method style, `ref` ownership/ARC-safe patterns, and JSON/config object usage where supported by generation sources.

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

Include direct examples for faction config path shapes, entity catalog config structure, and a scenario/Game Master setup checklist. Put exact raw source paths in `generation/review.md`.

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

Include direct examples for startup parameters, server config fields, `.gproj` layout, and addon/project packaging layout when generation sources provide them.

### `examples-patterns.md`

Official sample mod patterns and project layouts.

Use official sample README files, sample `.c`, `.conf`, `.et`, `.ent`, and `.gproj` files during generation. Do not include local raw sample paths in the finished reference.

Purpose: give Codex a compact map of official sample projects and reusable example patterns without bloating every topical reference.

Include:

- Sample mod inventory and what each sample demonstrates.
- Script examples worth reusing, with short fenced `c` excerpts and source-family labels. Exact raw paths go in `generation/review.md`.
- Common addon/project layout patterns.
- Config, prefab, entity catalog, arsenal, world, Workbench plugin, weapon, vehicle, character, faction, replacement, cinematic, and animation sample patterns.
- Cross-links to topical references that should use each pattern.

Do not copy large asset files or large prefab/config bodies. Summarize structure and cite paths.

### `common-task-recipes.md`

Common Reforger coding recipes generated from official docs, official samples, and verified API signatures.

Use this as a fast path after `SKILL.md` routing when the user asks for a common task such as "make a component", "teleport a player", "spawn a prefab", "add a user action", or "make a simple RPC".

This reference should be practical and explicit. It should avoid long raw excerpts and instead point back to topical references for deep background.

Every recipe should include a direct example block when generation sources support it. If a complete verified code example is not available, include a smaller verified snippet plus an explicit uncertainty note.

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

Phase 0 - Re-read gates:

1. Re-read "Non-Negotiable Build Contract", "Generation Boundary", "Reference Strategy", and "Validation".
2. Confirm the work is a full rebuild, partial expansion, or audit-only pass.
3. If the user asked for a full rebuild, do not stop after writing a compact useful set.

Phase 1 - Raw source readiness:

1. Apply the refresh rules. Pull game data, wiki docs, or official samples only when asked or when the required raw folder/file is missing.
2. Confirm required raw inputs exist: wiki schema/markdown/pages, game API schema/manifest, and official samples.
3. Run `scripts/build-reforger-extended-api-reference.py` to regenerate `references/api-extended.md` from raw game API data.
4. Load and inventory raw sources:
   - Wiki docs: titles, URLs, headings, markdown paths, page JSON, text length, categories.
   - Samples: README files, `.c`, `.conf`, `.et`, `.ent`, and project layout paths.
   - Game API schema: classes, enums, functions, methods, properties, docs, signatures, source files.
5. Use only checked-in helper scripts for inventory or audit. Do not create helper scripts during the rebuild unless the user's task is explicitly to change the skill tooling.
6. Create a source inventory for the review: available raw inputs, wiki counts, sample counts, API counts, skipped/empty pages, duplicate candidates, and source warnings.
7. Clean the wiki source set. Remove or flag empty pages, duplicate pages, broken category shells, and pages with no useful text.
8. Classify wiki pages, sample files, and APIs into the reference topics in this design.

Phase 2 - Core references:

1. Build `references/api-main.md` from verified API schema entries and cited docs/samples. Include exact signatures for the mandatory API groups. Put exact schema/source paths in `generation/review.md`.
2. Build `references/scripting-core.md`, `references/entity-component-lifecycle.md`, `references/networking-multiplayer-replication.md`, and `references/resources-prefabs-configs.md` before lower-priority topics.
3. Build topical references from official wiki/docs first. Preserve the docs as the main source of truth.
4. Curate topical references directly as Codex-authored Markdown. Do not write or run a deterministic reference-generation script.
5. Add direct code, config, command, and project-layout examples where they improve the reference. Examples are additive to the source guidance and must be source-labeled by category, but must not cite local `raw/` paths in the reference.
6. Verify every API name/signature used in topical references, examples, and recipes against `raw/game-data/api-schema.json`.

Phase 3 - Remaining references and recipes:

1. Build the remaining topical references in priority order from this design.
2. Build `references/examples-patterns.md` from official samples as the central sample layout/example map. Inventory every official sample mod by name and purpose, without raw local file paths.
3. Build `references/common-task-recipes.md` from official docs, samples, and verified APIs. Include direct example blocks for supported recipes.
4. Record expected-common API gaps in `api-main.md` and later in `generation/review.md`.
5. Check markdown quality for every reference: valid headings, fenced code blocks, readable lists/tables, source citations, no raw crawl noise, and clean GitHub rendering.

Phase 4 - Audit gate before `SKILL.md`:

1. Run the checked-in audit script:

```powershell
py -3 scripts\audit-references.py
```

2. The audit must check:
   - Every required reference exists.
   - Nonblank line targets are met or have topic-specific `INTENTIONALLY SHORT` justification.
   - No generated runtime reference or `SKILL.md` contains `raw/` paths or a raw-source `Sources Used` section.
   - `generation/review.md` contains exact raw source provenance for every generated reference.
   - Every applicable reference has traps/checklists and examples or explicit no-example rationale.
   - Every reference has a review coverage map for assigned source documents, sample groups, and API domains.
   - `common-task-recipes.md` includes every required recipe.
   - `examples-patterns.md` inventories all official sample mods.
   - `api-main.md` includes mandatory API coverage with exact signatures or explicit missing-API gaps. Exact schema/source paths for those entries belong in `generation/review.md`.
   - Existing `SKILL.md`, if present, references only existing files.
3. If any required reference fails the completeness audit, expand it before continuing. Do not continue to `SKILL.md` as if the generation passed.
4. Check reference size and usefulness. Split or trim anything that creates context bloat without adding practical lookup value, but do not trim below the required depth bar.

Phase 5 - Final skill and review:

1. Create `SKILL.md` as a compact router and guardrail that points to the generated references. This is AI/Codex-authored.
2. Create or validate `agents/openai.yaml` so the skill metadata matches `SKILL.md`.
3. Validate the skill folder and generated links.
4. Run `scripts/audit-references.py` again after `SKILL.md` is written.
5. Write `generation/review.md`, overwriting any prior review. This is AI/Codex-authored audit output, not script-generated, but it may quote or summarize the checked-in audit script's results.

Required audit table columns:

- `Reference`
- `Nonblank lines`
- `Line target met`
- `Runtime raw references absent`
- `Review provenance listed`
- `Source coverage mapped`
- `Actionable details retained`
- `Examples present`
- `Traps/checklist present`
- `API notes present`
- `Required coverage met`
- `Status`
- `If failed, required expansion`

Allowed `Status` values are only `PASS`, `FAIL`, or `INTENTIONALLY SHORT`. Use `INTENTIONALLY SHORT` only when the review gives a topic-specific sparse-source explanation and lists the exact raw files checked in `generation/review.md`.

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
- Reference completeness table with line counts, runtime raw-reference absence, review provenance status, example status, trap/checklist status, and pass/fail.
- Source coverage map for each generated reference, including source documents considered, major concepts preserved, concepts summarized, concepts deferred to `api-main.md` or `api-extended.md`, and concepts intentionally omitted.
- Actionable-detail retention notes for each generated reference: list any warnings, prerequisites, Workbench steps, config fields, API signatures, or sample patterns that were difficult to compress and how they were preserved.
- Any reference below the expected size target, with either a topic-specific sparse-source justification or explicit `FAIL` status. Do not use broad wording such as "intentionally compressed" as a substitute for a justification.
- A top-level generation status line: `COMPLETE`, `INCOMPLETE`, or `STRUCTURALLY VALID BUT DESIGN-INCOMPLETE`.
- If `quick_validate.py` passes but the completeness audit fails, use `STRUCTURALLY VALID BUT DESIGN-INCOMPLETE`.
- How `api-main.md` was curated.
- Expected-common APIs that were missing or only found in comments/examples.
- Task recipes written and any recipe uncertainty.
- Direct examples added per reference and any references that intentionally lack examples due to missing source support.
- Exact raw source provenance per reference: list the raw wiki/docs, sample, and API files used for each generated reference. This is where raw paths belong.
- Confirmation that generated `SKILL.md` and `references/*.md` contain no `raw/` paths and no instructions to open raw files.
- Markdown quality issues found and fixed, including broken tables, missing code fences, crawl artifacts, and unreadable copied excerpts.
- Confirmation that `api-extended.md` was generated exhaustively.
- Any source-data warnings.
- Any suspected gaps.
- Manual review items.

`generation/review.md` is for auditing only. Do not use it as source material in later generations.

## Validation

Before finishing generation:

- Re-read "Non-Negotiable Build Contract", "Generation Boundary", "Generation Workflow", and this "Validation" section.
- Confirm every reference in `SKILL.md` exists.
- Confirm no required reference is merely a stub, outline, short placeholder, or high-level summary when source material exists.
- Confirm each required reference satisfies the Reference Strategy completeness checklist. If not, expand it before finishing or mark the generation `INCOMPLETE`.
- Confirm each required reference has a source coverage map in `generation/review.md` and that every assigned source document's actionable content is preserved, summarized with rationale, deferred to API lookup, or intentionally omitted with rationale.
- Confirm references preserve actionable details from source docs, not just topic labels, representative examples, or broad summaries.
- Confirm required topical references are normally 300-900 lines, with topic-specific sparse-source review justification for any shorter file.
- Confirm `common-task-recipes.md`, `examples-patterns.md`, and `api-main.md` are substantial central references, not thin routing files. Under 200 nonblank lines is a failure unless specifically justified by sparse source material.
- Confirm references were generated from raw wiki/docs as the highest-priority source, but do not contain raw paths.
- Confirm official samples are used as examples only, not as rule authority over docs/API data.
- Confirm API signatures come from raw game data and that exact raw API provenance is recorded in `generation/review.md`.
- Confirm no generated output used old generated references or old `SKILL.md` as source.
- Confirm no deterministic script generated topical references, `api-main.md`, `SKILL.md`, or `generation/review.md`.
- Confirm `api-main.md` is compact and curated.
- Confirm `api-main.md` includes the mandatory common API coverage or records explicit gaps.
- Confirm `api-extended.md` is exhaustive and searchable.
- Confirm `common-task-recipes.md` exists and includes all required recipes.
- Confirm direct examples are present in scripting-heavy and task-recipe references where generation sources support them.
- Confirm examples are additive and do not replace official guidance, gotchas, or API notes.
- Confirm non-script references include useful config, path-layout, command, or project-layout examples where generation sources support them.
- Confirm every code/config example has a source label, but no local `raw/` path.
- Confirm uncertain example APIs are marked `example-observed`, `generated-pattern-from-docs`, or `pseudocode` with verification notes.
- Confirm references render as clean Markdown for GitHub review: no broken tables, malformed headings, raw HTML, raw navigation text, or unfenced code blocks.
- Confirm empty wiki pages are absent or flagged.
- Confirm scripting references are the richest references.
- Confirm API lookup routing is topical reference, then `api-main.md`, then `api-extended.md`.
- Confirm large references include search terms or a short table of contents.
- Confirm `SKILL.md` includes grep/search guidance for `api-extended.md` and `api-main.md`, but does not mention `raw/` paths.
- Confirm `agents/openai.yaml` exists or is intentionally skipped, and matches the generated `SKILL.md`.
- Run `py -3 scripts\audit-references.py` and fix every reported failure before claiming completion.
- Run the available skill validation tool if present, then fix any reported metadata or structure issues. Record this separately from the design completeness audit.

Hard stop rules:

- If any required reference has `Status = FAIL`, the generation is not complete.
- If `generation/review.md` does not include the required audit table, the generation is not complete.
- If `generation/review.md` does not include source coverage maps and actionable-detail retention notes for each generated reference, the generation is not complete.
- If any source document assigned to a generated reference is only named but not coverage-reviewed, the generation is not complete.
- If `SKILL.md` or any runtime reference contains local `raw/` paths or tells the agent to open `raw/`, the generation is not complete.
- If `generation/review.md` does not list exact raw source provenance per reference, the generation is not complete.
- If `common-task-recipes.md` is missing any required recipe, the generation is not complete.
- If `examples-patterns.md` does not inventory every official sample mod, the generation is not complete.
- If `scripts/audit-references.py` fails, the generation is not complete.

Suggested local audit commands:

```powershell
py -3 scripts\audit-references.py

Get-ChildItem references -File |
  Where-Object { $_.Name -ne 'api-extended.md' } |
  Select-Object Name,@{Name='NonblankLines';Expression={(Get-Content $_.FullName | Where-Object { $_.Trim() } | Measure-Object -Line).Lines}},Length |
  Sort-Object Name

Select-String -Path SKILL.md,references\*.md -Pattern 'raw/|raw\\|Sources Used|Source files|Raw source'
Select-String -Path references\*.md -Pattern 'Common traps|Review checklist|official-doc-example|official-sample-excerpt|pseudocode|generated-pattern-from-docs'
```

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
