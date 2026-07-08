# Arma Reforger Skill Rebuild Design

This file is the operating brief for rebuilding the Arma Reforger Codex skill from local raw data and checked-in scripts. It is generation-facing; runtime files should be generated later from this design, the tooling contract, and source data.

Do not create or edit `SKILL.md` until the rebuild explicitly reaches the final skill-generation phase. The future `SKILL.md` must be compact and must be created from the complete context of this design, `generation/tooling-game-data-lookup.md`, the topical reference plan, and generated/raw data.

## Core Contract

Codex must create the skill from source data, not from previous generated output.

Use:

- Official wiki/docs cache under `raw/wiki-docs/`.
- Official sample mods under `raw/samples/`.
- Extracted game script/API data under `raw/game-data/`.
- Existing checked-in scripts under `scripts/`.
- The low-context lookup tooling contract in `generation/tooling-game-data-lookup.md`.
- The indexer contract in `generation/indexer-game-data.md`.
- The searcher contract in `generation/searcher-game-data.md`.

Do not use:

- Old `SKILL.md` as source truth.
- Old runtime references as source truth.
- Old `generation/review.md` as source truth.
- Model memory as source truth.
- Internet search unless the user explicitly asks to refresh from the internet.
- Newly created one-off topical-reference generators.

Raw game data must live in one place: `raw/game-data`. The extractor should sparse-checkout upstream `scripts/` directly into that directory and place generated schema, indexes, and manifests beside it. Do not maintain a separate raw source cache such as `raw/source-cache`, and do not copy scripts between raw data folders during normal refresh. After pulling data, the extractor must delete only these checkout artifacts inside `raw/game-data`: `.git`, `README.md`, and `LICENSE`.

The rebuild must produce a skill that is useful to Codex, not a human manual. Codex should be routed to the smallest useful reference and then to exact lookup data. Broad markdown dumps are a failure mode when they displace the exact source context needed for correct Reforger scripting.

## Low-Context Game Data Architecture

`generation/tooling-game-data-lookup.md` is the detailed tooling contract and source of truth for low-context Reforger game-data lookup.

`generation/searcher-game-data.md` is the detailed contract for the query helper that Codex should use over generated indexes. Future runtime guidance should route Codex to the searcher for exact API lookup, examples, inheritance, files, and bounded snippets instead of loading broad API/schema files.

Future generation must follow this layered model:

1. Router layer: future `SKILL.md` classifies the task and selects the smallest relevant reference.
2. Topical docs layer: runtime references provide general Reforger understanding, workflow risks, and lookup keys.
3. Generated index layer: compact generated indexes provide exact symbols, methods, files, examples, subtopics, evidence, and source locations.
4. Raw source layer: `raw/game-data/scripts/`, `raw/samples/`, and raw docs provide exact snippets and patterns after targeted lookup.

`raw/game-data` is both the temporary sparse Git checkout location for `BohemiaInteractive/Arma-Reforger-Script-Diff` and the generated-output directory. This keeps refresh efficient: Git fetches only the required sparse tree, the parser reads that tree in place without an extra extraction/copy stage, and then checkout artifacts are removed so the raw data folder contains only useful game data plus generated artifacts.

Mandatory rule: Codex must not guess Reforger APIs. Before writing API-sensitive Reforger code, Codex must search generated indexes or raw data for exact classes, methods, signatures, attributes, inheritance, and examples.

Generated runtime references should guide lookup rather than embed large API dumps. They should name search keys, classes, methods, file-name patterns, source modules, example families, and search subtopics. They should not copy large raw source bodies or route normal tasks through `api-extended.md`.

Future `SKILL.md` generation must use this model:

- Route the task.
- Read only relevant topical docs.
- Query exact game data.
- Use task lookup or subtopic filters when broad examples are too noisy.
- Inspect bounded raw snippets.
- Include Workbench, prefab, config, server, asset, or packaging steps when relevant.
- State residual compile, Workbench, runtime, multiplayer, dedicated-server, or package verification.

## Source Authority

Use sources in this order:

1. Official wiki/docs for workflows, rules, editor procedures, and constraints.
2. Current extracted game API data for exact signatures, inheritance, attributes, enums, and source locations.
3. Official samples and raw game scripts for concrete implementation patterns.
4. Existing project code for local conventions.

Resolve conflicts this way:

- API data wins for exact signatures.
- Docs win for workflow rules.
- Samples are examples, not universal templates.
- Project code wins for local style only when it does not contradict current API data.
- If a source is missing or ambiguous, label uncertainty instead of inventing details.

## Allowed Scripts

Codex may run existing checked-in scripts:

- `scripts/update-reforger-data.py`
- `scripts/update-reforger-wiki-docs.py`
- `scripts/update-reforger-samples.ps1`
- `scripts/build-reforger-extended-api-reference.py`
- `scripts/audit-references.py`
- `scripts/index-reforger-data.py`
- `scripts/query-reforger-data.py`
- `scripts/validate-reforger-search.py`

Use update scripts only when raw data is missing or the user explicitly asks to refresh.

`scripts/update-reforger-data.py` is the only game-data update script. Do not add a shell wrapper or second game-data updater; keep game-data refresh behavior in that one Python entrypoint.

It must support both normal refresh and cheap status checks:

- `--check`: compare local game-data commit to the remote ref without fetching, parsing, or writing.
- `--if-needed`: check first, then skip refresh when current or pull raw scripts when missing or stale.

Future index tooling must follow `generation/indexer-game-data.md` and must not duplicate upstream game-data freshness checks. It should check only whether derived indexes are stale relative to `raw/game-data/manifest.json`, the indexer version, and indexer configuration.

Search quality is the primary usefulness measure for the game-data tooling. After changing the parser, indexes, or searcher, run `scripts/validate-reforger-search.py` and inspect representative searches. Human search exports remain review-only artifacts and must not become Codex source truth.

If a checked-in helper script must change, treat that as an explicit repository edit. Do not hide tooling changes inside an ordinary skill rebuild.

## Reference Generation Rules

Topical references are runtime operating guides for Codex. They must preserve enough source-grounded detail to complete real Reforger tasks while keeping exact API/source lookup in generated indexes and raw data.

Each topical reference must include:

- When to read it.
- Task-surface classification guidance.
- Search terms and lookup keys.
- Common workflows and implementation surfaces.
- Concrete Reforger-specific traps.
- Source-backed examples or explicit no-example rationale.
- API lookup notes that point to generated indexes or raw data.
- Practical verification steps.

Preserve aggressively:

- Ordered Workbench procedures.
- Warnings and limitations.
- Config fields, resource types, prefab/component relationships, and server/package settings.
- API names, attributes, callback names, class pairing rules, authority terms, and enum names as lookup keys.
- Sample layout patterns and example families.
- Source-specific gotchas that change implementation choices.

Compress:

- Wiki navigation and page chrome.
- Screenshot captions that do not carry procedure.
- Repeated introductory prose.
- Large raw serialized bodies after extracting meaningful fields and relationships.
- Large API lists that belong in generated lookup indexes.

Reject and rewrite references that contain:

- Repeated filler.
- Generic "verify everything" prose without concrete lookup keys.
- High-level summaries where the source contains ordered steps.
- Vague instructions such as "configure the prefab" without naming relevant surfaces.
- Local machine-specific raw paths in runtime files.
- Large uncurated source dumps.
- Examples not tied to docs, samples, raw source, or verified API data.

## Required Runtime References

A complete rebuild should produce:

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

Runtime files are `SKILL.md` and `references/*.md`. They must be usable without exposing local raw paths. Generation and review files may record raw provenance.

## Rebuild Sequence

Run these phases in order.

### Phase 0: Workspace And Raw Data Check

- Run `git status --short`.
- Identify existing user changes and avoid overwriting unrelated work.
- Check whether raw wiki docs, samples, and game API data exist.
- Refresh only missing data unless the user requested a refresh.
- Confirm required checked-in scripts exist.

If the user only asks to update generation design or tooling docs, stop after editing generation docs.

### Phase 1: Source Inventory

Build a source inventory before writing runtime references.

For each required reference, identify relevant wiki/docs pages, sample mods and files, API classes/methods/attributes/enums/functions, lookup keys, and known uncertainty. Record exact provenance later in `generation/review.md`.

### Phase 2: Topic Reference Drafts

Write references one topic at a time from source inventory. Each draft must be operationally useful and lookup-oriented: it should tell Codex what to understand generally and exactly what to search next.

### Phase 3: Topic Reference Review

Review each reference before moving on.

Ask:

- Can Codex use this to complete a real Reforger task?
- Does it route to exact lookup data instead of forcing broad context loading?
- Did it preserve source-backed procedures, warnings, fields, and implementation surfaces?
- Are API-sensitive details represented as lookup keys or verified exact signatures?
- Are examples concrete and source-grounded?
- Is there filler or generic checklist padding?

Revise immediately if the answer is no.

### Phase 4: API Curation

`api-main.md` should remain compact and curated for high-frequency APIs. It should not become an alphabetical dump. It should point Codex toward generated lookup tooling for exact verification and include only common signatures repeatedly needed during normal work.

### Phase 5: Exhaustive API Fallback

`api-extended.md` may remain a generated fallback, but normal Codex workflows should not route to it first. Prefer compact generated indexes and bounded raw snippets. If generated comments or source data create malformed markdown, fix the generator rather than manually editing large generated output.

### Phase 6: Forward Tests

Before writing `SKILL.md`, simulate coding-focused forward tests using the references and lookup model.

Required prompts:

1. Add a minimal `ScriptComponent` and matching `ScriptComponentClass`.
2. Move an owner entity after verifying exact `IEntity` APIs.
3. Add a user-action script patterned after source examples.
4. Add a replicated/RPC component skeleton with authority separation.
5. Add a Workbench plugin command skeleton.
6. Add a config/prefab resource reference field example.

Forward tests pass only if Codex routes correctly, performs exact lookup, inspects bounded source snippets when needed, labels uncertainty, and avoids local raw paths in runtime output.

### Phase 7: `SKILL.md`

Write `SKILL.md` last.

It must be compact and act as a router and guardrail. It must be generated from this design, `generation/tooling-game-data-lookup.md`, final runtime references, and the validated lookup workflow.

Do not include raw paths, provenance tables, long examples, topic detail that belongs in references, tooling design detail that belongs in generation docs, or large API lists.

### Phase 8: `generation/review.md`

Write `generation/review.md` last.

It must include status, whether raw data was refreshed, source inventory summary, references written, exact raw provenance, API curation notes, lookup-tooling notes, forward-test results, validation results, known gaps, and manual review items.

## Required Reference Coverage

- `overview.md`: route ambiguous Reforger work, task-surface classification, source authority, lookup-first verification, highest-risk areas.
- `scripting-core.md`: script modules, naming, logging, modded classes, invokers, event/callback registration, performance, lookup keys.
- `scripting-language.md`: Enfusion syntax, classes, inheritance, ARC/ref lifetime, attributes, config objects, JSON, preprocessor use, lookup keys.
- `entity-component-lifecycle.md`: component/entity lifecycle, class pairs, attributes, event masks, owner guards, transforms, prefab integration, lookup keys.
- `networking-multiplayer-replication.md`: authority/proxy/owner roles, replicated properties, RPC, spawn/despawn authority, user action routing, dedicated-server implications, lookup keys.
- `resources-prefabs-configs.md`: resources, prefabs, configs, catalogs, layouts, `ResourceName`, resource loading, data-first workflows, lookup keys.
- `workbench-tools-debugging.md`: Workbench/editor boundaries, plugin APIs, editor tools, Resource Manager, Script Editor, World Editor, diagnostics, profiling, lookup keys.
- `scenario-framework-game-master.md`: Scenario Framework, Game Master, factions, catalogs, tasks, layers, game modes, editable prefabs, lookup keys.
- `terrain-world-editor.md`: world creation, terrain, navmesh, roads, rivers, generators, map tooling, editor-only automation boundaries, lookup keys.
- `assets-weapons-vehicles-animation-audio.md`: asset import, model/material/LOD/collision workflows, weapons, vehicles, gear, animation, audio, prefab/config surfaces, lookup keys.
- `server-runtime-packaging.md`: startup parameters, server config, dedicated-server behavior, addon dependencies, `.gproj`, Workshop packaging, scenario startup, logging, lookup keys.
- `examples-patterns.md`: official samples and raw source example families mapped to reusable patterns; examples are not signature authority.
- `common-task-recipes.md`: concise task recipes that route Codex to exact lookup steps.
- `api-main.md`: compact curated high-frequency API notes and lookup-tooling pointers.
- `api-extended.md`: generated exhaustive fallback only; do not route normal tasks here before compact indexes or targeted raw search.

## Validation

For a full rebuild, run available validation scripts and manual usefulness checks.

Minimum checks:

```powershell
py -3 scripts\audit-references.py
Select-String -Path SKILL.md,references\*.md -Pattern 'raw/|raw\\|Sources Used|Source files|Raw source'
Select-String -Path references\*.md -Pattern 'Detail \d+:|Operational Detail Retention|Expanded Source-Grounded Review Notes|Example Marker|Audit Marker|Coverage Marker'
Select-String -Path references\*.md -Pattern '\[image omitted\]|Official Wiki Sources|High-Signal Doc Notes|Official Sample Sources|Relevant APIs|Headings:|TODO:'
Select-String -Path references\api-main.md -Pattern 'IEntity|ScriptComponent|ResourceName|RplRpc|WorkbenchPlugin'
Select-String -Path SKILL.md -Pattern 'common-task-recipes.md'
```

Future lookup tooling should add validation for symbol lookup, method lookup, file lookup, example lookup, bounded snippet lookup, and normal workflows avoiding `api-extended.md`.

Passing commands are not enough. Manual usefulness review remains required.

## Completion Standard

Mark the rebuild `COMPLETE` only when runtime references are source-grounded and lookup-oriented, the low-context lookup model is implemented or explicitly accounted for, `api-main.md` is compact and curated, exhaustive API output is generated rather than hand-maintained, forward tests pass or are waived, `SKILL.md` is written last, `generation/review.md` records honest provenance/status, runtime files contain no local raw paths, and no output relies on repeated filler or broad API dumps as the normal path.

Otherwise mark the rebuild `INCOMPLETE` or `STRUCTURALLY VALID BUT DESIGN-INCOMPLETE`.
