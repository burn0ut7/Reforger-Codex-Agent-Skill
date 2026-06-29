# Arma Reforger Skill Rebuild Design

This file is the operating brief for Codex when rebuilding the Arma Reforger skill from local raw data and existing repository scripts.

The goal is repeatable skill creation, not one-off notes. A rebuild should produce a compact `SKILL.md`, useful runtime references under `references/`, an exhaustive generated API fallback, and an honest `generation/review.md` using the raw cache and checked-in scripts already present in this repository.

## Core Contract

Codex must create the skill from source data, not from previous generated output.

Use:

- Official wiki/docs cache under `raw/wiki-docs/`.
- Official sample mods under `raw/samples/`.
- Extracted API data under `raw/game-data/`.
- Existing checked-in scripts under `scripts/`.

Do not use:

- Old `SKILL.md`.
- Old runtime references.
- Old `generation/review.md`.
- Model memory as source truth.
- Internet search unless the user explicitly asks to refresh from the internet.
- Newly created one-off generator scripts for topical references.

The previous failure mode was repeated filler that passed structural checks while being useless. This design prevents that by making source inventory, topic-by-topic curation, manual usefulness review, and `SKILL.md`-last sequencing mandatory.

The second failure mode is over-compression: references that are structurally neat but too shallow to replace reading the wiki. This is also a failed rebuild. Runtime references must be dense, source-grounded operating manuals built from the wiki/docs, samples, and API data. They should be full of retained wiki procedure, warnings, field names, exact Workbench actions, config/resource shapes, source caveats, and implementation-sensitive details. Do not trade away useful detail for brevity.

## Allowed Scripts

Codex may run existing checked-in scripts:

- `scripts/update-reforger-data.ps1`
- `scripts/update-reforger-wiki-docs.py`
- `scripts/update-reforger-samples.ps1`
- `scripts/build-reforger-extended-api-reference.py`
- `scripts/audit-references.py`

Use update scripts only when raw data is missing or the user explicitly asks to refresh.

Use `scripts/build-reforger-extended-api-reference.py` to generate only:

```text
references/api-extended.md
```

Use `scripts/audit-references.py` as a quality aid, not as proof that the skill is good.

Do not create temporary or new scripts such as:

- `generate-reforger-skill.py`
- `build-references.py`
- `tmp_rebuild_runtime.py`
- Any script that writes topical references, `api-main.md`, `SKILL.md`, or `generation/review.md`.

If a checked-in helper script must change, treat that as a separate explicit repository edit. Do not smuggle script changes into an ordinary skill rebuild.

## Source Authority

Use sources in this order:

1. Official wiki/docs: rules, workflows, constraints, and Workbench procedures.
2. Official sample mods: concrete project layouts, examples, and patterns.
3. Extracted API data: exact signatures, inheritance, attributes, enums, and source locations.

Resolve conflicts this way:

- Docs beat samples for workflow rules.
- API data beats both for exact signatures.
- Samples are examples, not universal templates.
- If a source is missing or ambiguous, label uncertainty rather than inventing details.

## Non-Negotiable Detail Retention

The topical references are not summaries. They are the runtime documentation Codex will use instead of opening the raw wiki cache during normal Reforger tasks. Build them as detailed, practical, source-grounded references.

Preserve aggressively:

- Ordered Workbench procedures, including menu/tool names, setup prerequisites, rebuild/regeneration steps, and verification steps.
- Warnings, limitations, caveats, branch/version assumptions, editor/runtime differences, and multiplayer/server distinctions.
- Config shapes, field names, resource extensions, prefab/entity/component relationships, directory layouts, command shapes, startup/config snippets, and `.gproj`/Workshop metadata relationships.
- API names, attributes, callback names, enum names, class pairing rules, lifecycle order, authority/role terms, and exact signatures once verified.
- Sample mod layout patterns, file families, representative script/config excerpts, and how samples map to real implementation tasks.
- Source-specific gotchas that would change how Codex writes code, config, prefab wiring, editor tooling, server setup, asset integration, or deployment.

Compress only:

- Wiki navigation, page chrome, image placeholders, screenshot captions that do not carry procedural information, repeated introductory prose, and duplicate statements already preserved elsewhere.
- Giant raw serialized bodies only after extracting the meaningful fields, nesting relationships, resource references, inheritance, and implementation implications.
- Large tables only after preserving every field or row category that affects implementation decisions.

Do not replace a wiki workflow with a high-level paraphrase if the original page contains concrete steps. Do not replace multiple source pages with a generic checklist. If a source has useful details, those details must survive in the relevant reference, even when that makes the file long.

Short references are allowed only when the source packet proves the topic is genuinely sparse. "Concise" is not a goal for topical references; usefulness and detail retention are the goal. Prefer a long, well-sectioned reference over a compact guide that forces Codex back to raw docs.

## Rebuild Output

A complete rebuild produces:

```text
SKILL.md
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
generation/
  review.md
```

Runtime files are `SKILL.md` and `references/*.md`. They must be usable without `raw/`.

`generation/review.md` is an audit report. It may contain exact raw paths. Runtime files must not.

## Rebuild Sequence

Run these phases in order. Do not write `SKILL.md` until Phase 7.

## Piecemeal Reference Mode

Use this mode when the user asks to rebuild, generate, improve, or review one reference or a small named set of references.

Rules:

- Work only on the named reference or named references.
- Do not edit `SKILL.md`.
- Do not edit unrelated references, except for a narrow cross-link fix explicitly caused by the current reference.
- Do not rewrite `generation/review.md` as if the whole skill is complete.
- Record partial status as `INCOMPLETE` or leave review updates for a later full rebuild, depending on the user's request.
- Still use raw sources, source authority, API verification, and manual usefulness review.

For each reference in piecemeal mode, complete this mini-sequence:

1. Build a source packet.
2. Draft from the source packet.
3. Review for missing context, useful detail, examples, APIs, and traps.
4. Revise immediately if the reference is thin, generic, repetitive, or missing important source detail.
5. Stop after the named reference work is complete.

Do not use piecemeal mode to create multiple files for the same topic. If one topic is large, keep the topic in its assigned reference and use clear sections inside that file. Recommend splitting only when the source material belongs to a distinct topic already represented by another reference or when a new distinct topic is truly needed.

### Phase 0: Workspace And Raw Data Check

Before writing runtime files:

- Run `git status --short`.
- Identify existing user changes and avoid overwriting unrelated work.
- Check whether raw wiki docs, samples, and game API data exist.
- Refresh only missing data, unless the user requested a refresh.
- Confirm `scripts/build-reforger-extended-api-reference.py` exists.

If the user only asks to update this design, stop after editing this file.

### Phase 1: Source Inventory

Build a source inventory before writing references.

For each required reference, identify:

- Relevant wiki/docs pages.
- Relevant sample mods and files.
- Relevant API classes, methods, attributes, enums, or global functions.
- Known uncertainty or project-specific verification needs.

This can be done with shell search, file reads, and the existing API/index files. Do not write a new inventory generator.

The inventory must be recorded later in `generation/review.md` as exact raw provenance per reference.

For each reference, create a source packet before drafting. The source packet is a working checklist, not a runtime artifact. It must include:

- Wiki/docs selected for the reference.
- Wiki/docs considered but deferred, with the reason.
- Sample mods and files selected for concrete examples.
- Sample files considered but deferred, with the reason.
- API symbols, attributes, enums, and signatures to verify.
- High-value details that must survive compression.
- Ordered wiki procedures and field/config/resource names that must be retained verbatim or near-verbatim in compact form.
- Wiki warnings/caveats that must be preserved because they affect implementation or verification.
- Sample excerpts or patterns that should be represented in the runtime reference.
- Uncertainty or project-specific verification notes that must be preserved.
- Cross-topic details that should be routed to another reference instead of duplicated.

Do not draft the reference until the source packet is complete enough to avoid obvious missed context.

If the source packet for a reference does not include enough concrete wiki/doc detail to produce a dense reference, stop and expand the source packet before drafting. Do not fill gaps with model memory, generic Reforger advice, or broad "verify this" language.

### Phase 2: Topic Reference Drafts

Write references one topic at a time from the source inventory.

Each topical reference must include:

- When to read this reference.
- Search terms.
- Source authority summary without local raw paths.
- Common workflows near the top.
- Concrete Reforger-specific guidance.
- Source-backed examples or an explicit no-example rationale.
- API lookup notes.
- Common traps.
- Review checklist.

References must be useful, not artificially short. Preserve as much actionable detail from the raw wiki/docs as possible:

- Keep concrete workflows, prerequisites, order-sensitive Workbench steps, warnings, field names, config shapes, command shapes, and API names.
- Keep source-specific caveats that would change how Codex writes code or config.
- Keep examples when they teach an implementation pattern, even if they need to be shortened.
- Compress repeated prose, screenshots, navigation, UI fluff, and non-actionable background.
- Summarize large tables or serialized config/prefab bodies only after preserving the fields and relationships that matter for implementation.
- If preserving useful detail makes a reference long, prefer a well-structured long reference over a thin summary.

Line-count targets from `scripts/audit-references.py` are useful lower-bound heuristics, not padding goals. Falling below them is acceptable only when the source packet and `generation/review.md` justify that the topic is genuinely sparse. For normal Reforger topics with substantial wiki coverage, references should be near or above the audit's useful-detail range.

A short reference is acceptable only when source material is genuinely sparse or narrow and the reference still preserves the important operational details. A short reference for scripting, lifecycle, networking, resources/prefabs/configs, Workbench, terrain, assets, server, examples, recipes, or API curation is presumed incomplete unless the review proves otherwise.

Each topical reference should include detailed wiki-derived sections, not just routing prose:

- Prerequisites and setup assumptions.
- Step-by-step workflows from the docs.
- Important fields, options, resource types, and file/folder shapes.
- Source warnings and failure modes.
- Sample-backed patterns and concise excerpts.
- API verification notes with exact symbols to check.
- Practical validation steps in Workbench, runtime, multiplayer, server, or packaging context.

If one assigned reference becomes too broad, do not split it into multiple files for the same topic. Instead:

- Add clear sections and a table of contents inside the same reference.
- Move clearly unrelated material to the existing reference for that other topic.
- Recommend a new reference only when the source material represents a distinct topic that does not fit any existing reference.
- Record the split recommendation in `generation/review.md` or the final response instead of creating new files during an ordinary rebuild.

Reject and rewrite any reference that contains:

- Repeated numbered filler.
- Generic “verify everything” bullets.
- High-level summaries where the source wiki contains concrete ordered steps.
- Thin routing-only content for a topic with substantial wiki coverage.
- Placeholder phrases such as "follow the official workflow" without preserving the workflow's important steps.
- Vague statements such as "configure the prefab" without naming the relevant fields, resource types, component relationships, or verification steps available from source.
- Audit-marker sections.
- Raw crawler headings.
- Copied navigation text.
- Large uncurated source dumps.
- Local raw paths.
- Examples not tied to docs, samples, or verified API data.

### Phase 3: Topic Reference Review

After each reference draft, review it before moving on.

Ask:

- Can Codex use this to complete a real Reforger task?
- Did the source packet include every high-signal raw wiki/doc page for this topic?
- Did the reference preserve as much useful wiki detail as practical without copying navigation or filler?
- Would a future Codex still need to open the raw wiki page for ordinary task execution because this reference omitted concrete steps or fields? If yes, revise.
- Are wiki procedures represented as actionable steps rather than broad summaries?
- Were important prerequisites, ordered steps, warnings, config fields, and Workbench actions retained?
- Were source details compressed only when they were repetitive, non-actionable, or routed to a better reference?
- Does it preserve script/data/editor/server boundaries?
- Are lifecycle, networking, resource, Workbench, packaging, or authority risks called out where relevant?
- Are examples concrete and source-grounded?
- Are exact APIs verified or routed to API lookup?
- Is there any repeated filler?

If the answer is no, revise the reference immediately.

Do not mark a reference reviewed if it is merely readable. It must be operationally rich enough to solve realistic tasks in its topic area.

### Phase 4: `api-main.md`

Write `api-main.md` after topical references, because it should reflect the APIs that normal tasks actually need.

It must be curated manually from docs, samples, and API data.

Put common signatures near the top. Do not make an alphabetical dump.

Cover:

- `IEntity` transform, origin, orientation, component lookup, and event-mask APIs.
- `ScriptComponent`, `ScriptComponentClass`, `GenericComponent`, `GenericEntity`, and lifecycle/owner APIs.
- `Resource`, `ResourceName`, config, prefab, and resource-loading APIs.
- `Game`, world, spawn, delete, and player-access APIs when present.
- `BaseRplComponent`, `RplProp`, `RplRpc`, `OnRpl`, role, ownership, and replication serialization APIs.
- Input, user action, and widget/UI APIs.
- Workbench plugin, Script Editor, World Editor, and Resource Manager APIs.
- Weapon, vehicle, inventory, audio, animation, task, faction, and scenario lookup groups.

If an expected common API is absent or only appears in samples/comments, say so explicitly.

### Phase 5: `api-extended.md`

Generate the exhaustive fallback:

```powershell
py -3 scripts\build-reforger-extended-api-reference.py
```

Then inspect audit output for markdown hygiene. If generated comments create malformed tables, TODO artifacts, mojibake, or other search-hostile output, prefer fixing the checked-in builder in a separate explicit edit. Do not hand-maintain large generated sections unless the user asks for a temporary local cleanup.

### Phase 6: Forward Tests

Before writing `SKILL.md`, run or simulate small coding-focused forward tests using the references.

Required test prompts:

1. Add a minimal `ScriptComponent` and matching `ScriptComponentClass` with one editable prefab/resource field and a guarded `EOnInit` debug print.
2. Add a component method that moves its owner entity to a supplied vector, verifying exact `IEntity` transform/origin APIs before writing code.
3. Add a user-action script patterned after official sample user actions, with uncertain APIs clearly marked.
4. Add a small replicated/RPC component skeleton that separates authority-side state changes from client-side calls and marks RPC attribute/signature uncertainty.
5. Add a Workbench plugin command skeleton using documented Workbench plugin attribute shape and editor-only API checks.
6. Add a config/prefab reference field example using `ResourceName` and explain whether the task is script-first, data-first, editor-first, or mixed.

Record results in `generation/review.md`.

Forward tests pass only if they:

- Route to the right references.
- Check `api-main.md` or `api-extended.md` for exact APIs.
- Label uncertainty instead of inventing signatures.
- Produce reviewable code/config.
- Avoid local raw paths in runtime output.

### Phase 7: `SKILL.md`

Write `SKILL.md` last.

It must be compact and act as a router and guardrail.

Frontmatter must contain only:

```yaml
---
name: reforger
description: ...
---
```

The body must include:

- Task routing to every runtime reference.
- API verification rule.
- Source authority rule.
- Reminder that many Reforger tasks are data-first, editor-first, server-first, asset-first, or mixed rather than script-only.
- Reminder to state residual Workbench/runtime/server verification needs.

Do not include:

- Raw paths.
- Provenance tables.
- Long examples.
- Topic detail that belongs in references.
- Generation or audit process detail.

### Phase 8: `generation/review.md`

Write `generation/review.md` last.

It must include:

- Status: `COMPLETE`, `INCOMPLETE`, or `STRUCTURALLY VALID BUT DESIGN-INCOMPLETE`.
- Whether raw data was refreshed.
- Source inventory summary.
- References written.
- Exact raw provenance per reference.
- API curation notes.
- Forward-test results.
- Validation results.
- Known gaps and manual review items.

Use `INCOMPLETE` if references are missing or not reviewed.

Use `STRUCTURALLY VALID BUT DESIGN-INCOMPLETE` if files exist and basic validation passes but quality, provenance, source coverage, or forward tests are not complete.

Use `STRUCTURALLY VALID BUT DESIGN-INCOMPLETE` if any topical reference is substantially below the audit useful-detail range without a source-backed sparse-topic justification.

Use `COMPLETE` only when the runtime skill is useful and all phases passed.

## Required References

### `overview.md`

Purpose: route ambiguous Reforger work.

Cover:

- Script-first, data-first, editor-first, server-first, asset-first, and mixed task routing.
- Docs as rules, samples as examples, API data as signature truth.
- Why many tasks require Workbench resources, prefabs, configs, worlds, layouts, or packaging.
- Verification loop: topical reference, API lookup, project search, residual runtime/Workbench uncertainty.
- Highest-risk areas: lifecycle, replication, resources/prefabs/configs, Workbench tooling, packaging.

### `scripting-core.md`

Purpose: primary Enfusion Script workflow reference.

Cover:

- Script module/folder placement.
- Creator tag and class/file naming.
- Modded class layout, override verification, and `super`.
- `Print`, `PrintFormat`, log levels, Remote Console, noisy-log traps.
- `ScriptInvoker` accessor and subscription patterns.
- Event/callback registration and alternatives to polling.
- Performance and profiling workflow.
- Examples for minimal class, modded override, debug/invoker/event pattern.

### `scripting-language.md`

Purpose: Enfusion language mechanics.

Cover:

- Syntax, classes, methods, constructors/destructors, inheritance, overrides.
- Primitive values, vectors, arrays, maps/sets where supported, constants, enums.
- Automatic reference counting, `ref`, object lifetime, native/managed traps.
- Attributes and annotations for serialized/editor fields.
- Config objects, `BaseContainer`, defaults, failure handling.
- JSON usage when source-supported.
- Preprocessor and macro risks.
- Examples for types, control flow, classes, `ref`, attributes, config/JSON.

### `entity-component-lifecycle.md`

Purpose: entity and component coding.

Cover:

- `ScriptComponentClass`/`ScriptComponent` pairing.
- `ComponentEditorProps` and editable `[Attribute]` fields.
- `EOnInit`, `OnPostInit`, delete, activation/deactivation, parent-child callbacks where source-supported.
- Event masks and update callbacks.
- Owner guards, `GetOwner`, component lookup/cast guards.
- `IEntity` origin/transform APIs and local-vs-world distinction.
- Prefab integration, serialized field stability, activeness, Workbench preview traps.
- Component skeleton, editable field, guarded init, movement/teleport examples.

### `networking-multiplayer-replication.md`

Purpose: multiplayer-safe scripting.

Cover:

- Authority/master, proxy, owner, owner proxy, remote proxy.
- Authority-side mutation and proxy/client presentation.
- `BaseRplComponent` lookup and role/ownership APIs.
- `RplProp` state replication, update/bump/notify uncertainty, initial-state concerns.
- `RplRpc` purpose, signature/attribute verification, direction/target/reliability uncertainty.
- Spawn/despawn/movement authority rules.
- User action routing when gameplay state changes.
- Authority example, replicated property skeleton, RPC skeleton or no-example rationale, anti-example.

### `resources-prefabs-configs.md`

Purpose: resources, prefabs, configs, UI/layout resources, and editor data.

Cover:

- Data-first versus script-first decision rules.
- `ResourceName`, picker attributes, empty-value guards, `Resource.Load`.
- Prefab inheritance, overrides, component wiring, serialized-field stability.
- Config class/object workflow, `BaseContainer`, defaults, failure handling.
- Entity catalogs, arsenal, faction/scenario consumers, editable prefab implications.
- Layout/widget resources versus widget scripts.
- Prefab/resource spawn workflow with API verification and authority caveats.
- Examples for config snippet, `ResourceName` field, resource load, catalog/prefab layout, UI/layout.

### `workbench-tools-debugging.md`

Purpose: Workbench, editor tooling, diagnostics, and profiling.

Cover:

- Workbench/editor module separation from runtime modules.
- `WorkbenchPlugin`, `WorkbenchPluginAttribute`, `Run`, `RunCommandline`, context-menu hooks where supported.
- Resource Manager, Script Editor, World Editor, String Editor or other module APIs.
- Selection handling and empty-selection guards.
- Diag Menu, Script Editor, Remote Console, logs.
- Script profiling and performance workflow.
- Resource registration/rebuild and destructive-action safeguards.
- Workbench plugin skeleton and diagnostic/profiling example.

### `scenario-framework-game-master.md`

Purpose: Scenario Framework, Game Master, tasks, factions, and game mode content.

Cover:

- Scenario/Game Master/faction work as data-first unless script integration is required.
- Faction configs, groups, characters, gear, identities, Conflict/Game Master integration.
- Entity catalogs, editable/placeable prefabs, performance/replication implications.
- Task system workflow, ownership, completion, cleanup, script integration cautions.
- Scenario layers, game mode setup, world/config dependencies.
- Game Master editable prefab setup and Workbench/plugin steps.
- Faction config layout, entity catalog layout, scenario/Game Master checklist, task example or no-example rationale.

### `terrain-world-editor.md`

Purpose: terrain creation, world editing, generators, navmesh, roads, rivers, and map tooling.

Cover:

- New world/base scene setup and world resource layout.
- Terrain entity/origin, sculpting, materials/layers, collision implications.
- Navmesh generation/rebuild and AI validation.
- Road, river, lake, and water workflows.
- Forest/object/shape/generator tools and performance risks.
- 2D map tooling and generated/exported data.
- World Editor tool/API boundaries and editor-only automation caveats.
- World layout, terrain setup, navmesh, road/river/generator checklists.

### `assets-weapons-vehicles-animation-audio.md`

Purpose: asset workflows that affect code and mod integration.

Cover:

- Asset preparation, import, resource processing, prefab/config setup.
- FBX/model, texture/material, LOD/collision/performance workflow.
- Weapon prefab/config surfaces: muzzle, magazine, attachments, effects, animation, audio, user actions.
- Vehicle prefab/config surfaces: simulation, damage, fuel, seats, actions, physics, controller components.
- Character gear, attachment points, inventory/arsenal/faction integration.
- Animation editor, graph variables, controllers, authored resources, script touchpoints.
- Audio editor, sound events, signals, variables, occlusion, runtime trigger paths.
- Examples for weapon, vehicle, gear, animation, audio layouts or explicit no-example rationale.

### `server-runtime-packaging.md`

Purpose: runtime, startup, server hosting/config, Workshop, packaging, and deployment.

Cover:

- Startup parameters, branch/version assumptions, launch context.
- Server config fields, secrets/logging safety, ports/network settings, dedicated-server behavior.
- Addon dependencies, load order, `.gproj`, project metadata, packaging inclusion.
- Workshop publishing, metadata, dependency warnings, visibility, backend/login caveats.
- Dedicated server versus client/editor behavior and no local-player/UI assumptions.
- Scenario/world/game mode startup configuration.
- Static config checks, test-server launch when possible, logs, rollback.
- Startup/config snippet, `.gproj` or addon layout example, packaging checklist.

### `examples-patterns.md`

Purpose: official sample mod map and reusable patterns.

Cover:

- Every official sample mod by name, purpose, and primary systems.
- Common addon/project layouts: scripts, configs, prefabs, worlds, resources, project metadata.
- Modded script, component/user-action, and Workbench plugin patterns with short excerpts where source-supported.
- Config, prefab, entity catalog, arsenal, world, and faction layout patterns.
- Weapon, vehicle, character, prop, replacement, animation, and cinematic sample patterns.
- Cross-links from sample families to topical references.
- Warnings that samples are examples and signatures/workflows still require docs/API verification.

### `common-task-recipes.md`

Purpose: fast path for common coding tasks.

Cover recipes for:

- Create `ScriptComponentClass` plus `ScriptComponent`.
- Add editor props and attribute fields.
- Print debug info safely.
- Get entity origin or transform.
- Move or teleport an entity.
- Get local player or controlled entity with project-context warning.
- Register frame/update/event masks safely.
- Add or modify a user action.
- Spawn an entity or prefab.
- Load a resource or prefab.
- Basic replicated or RPC action.
- Create a Workbench plugin command.
- State whether each recipe is script-first, data-first, editor-first, or mixed.

Each recipe must have a direct example or explicit no-example rationale.

### `api-main.md`

Purpose: compact curated API reference for normal coding work.

See Phase 4.

### `api-extended.md`

Purpose: exhaustive generated fallback from extracted API data.

See Phase 5.

## Validation

Run after a full rebuild:

```powershell
py -3 scripts\audit-references.py
Select-String -Path SKILL.md,references\*.md -Pattern 'raw/|raw\\|Sources Used|Source files|Raw source'
Select-String -Path references\*.md -Pattern 'Detail \d+:|Operational Detail Retention|Expanded Source-Grounded Review Notes|Example Marker|Audit Marker|Coverage Marker'
Select-String -Path references\*.md -Pattern '\[image omitted\]|Official Wiki Sources|High-Signal Doc Notes|Official Sample Sources|Relevant APIs|Headings:|TODO:'
Select-String -Path references\api-main.md -Pattern 'IEntity|ScriptComponent|ResourceName|RplRpc|WorkbenchPlugin'
Select-String -Path SKILL.md -Pattern 'common-task-recipes.md'
```

Passing commands are not enough. Manual usefulness review remains required.

## Completion Standard

Mark the rebuild `COMPLETE` only when:

- All runtime references are source-grounded, useful, and non-repetitive.
- `api-main.md` contains curated common signatures near the top.
- `api-extended.md` is generated from the checked-in script.
- Forward tests pass or are explicitly waived by the user.
- `SKILL.md` is written last and routes to every runtime reference.
- `generation/review.md` records exact raw provenance and honest status.
- Runtime files contain no local raw paths.
- No output relies on repeated filler or audit-only prose.

Otherwise mark the rebuild `INCOMPLETE` or `STRUCTURALLY VALID BUT DESIGN-INCOMPLETE`.
