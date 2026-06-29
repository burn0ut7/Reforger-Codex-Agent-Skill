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
- Line-count targets are quality gates, not quotas. Do not add repeated, generic, template, or meta-process text to reach a target. If source-grounded useful content is not available or cannot be curated in the current run, leave the reference below target, mark it `FAIL` or `INTENTIONALLY SHORT` only with proof, and stop before finalizing `SKILL.md`.
- Any generated reference containing filler sections such as `Operational Detail Retention`, `Expanded Source-Grounded Review Notes`, numbered repeated retention notes, or near-duplicate bullets added only to inflate line count fails the completeness audit.
- Every reference is standalone and useful without the `raw/` directory present.
- Do not include `raw/...` paths, "Sources Used" raw-source sections, or instructions to open `raw/` files in generated references or `SKILL.md`.
- `generation/review.md` must include exact raw source provenance for every generated reference. Keep raw source paths in review/audit output, not in runtime references.
- Every applicable reference has direct examples or an explicit no-example rationale.
- Every applicable reference has `Common Traps`, `Review Checklist`, or both.
- Every applicable reference has API lookup notes, and `api-main.md` includes exact signatures for mandatory common APIs rather than only search advice. Raw source paths for those signatures belong in `generation/review.md`.
- Markdown quality is a completeness gate, not cosmetic polish. Any runtime reference containing mojibake, raw wiki image links, image placeholders, collapsed heading runs, crawl navigation text, flattened inline tables, malformed tables, stale table-of-contents entries, copied crawler section dumps, or generic audit-only marker sections fails the rebuild.
- `api-main.md` must be curated for common coding tasks and must put mandatory common APIs near the top. A broad alphabetical mini-dump with required signatures appended later fails runtime usability even if all terms are present.
- Every required reference must satisfy semantic coverage gates, not just structure gates. A reference that meets line count, examples, traps, and API-note checks but omits required topic concepts is `FAIL`.
- `generation/review.md` must include a required-concept coverage matrix for every runtime reference. The audit must verify that each required concept marked `PASS` has runtime evidence in the reference text and raw provenance in the review.

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
- Helper scripts may verify semantic concept coverage by checking the required concept matrix, runtime evidence terms, required examples, and required API terms. They still may not write final topical prose.
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

The installed/distributed skill must remain usable without `raw/`. `raw/` is a local generation input cache, not a runtime dependency for Codex skill use. Do not require `raw/` to be committed or distributed with the skill; the committed runtime surface is `SKILL.md`, `references/`, `scripts/`, `agents/`, and `generation/`.

## Reference Strategy

References should be useful to load into context. Keep them dense, factual, navigable, and standalone. Avoid giant dumps when a summary plus stable in-skill lookup guidance is better.

References are written for Codex first, but they must still render cleanly for a human reviewer on GitHub. Do not leave broken markdown tables, raw HTML fragments, navigation junk, crawl artifacts, one-line dumps, or malformed headings in generated references.

Clean Markdown is required. Do not preserve raw crawler formatting just because it contains useful words. Convert scraped source material into curated Markdown before it enters a runtime reference.

Do not copy raw wiki extraction sections into runtime references as prose. Sections such as `Official Wiki Sources`, `High-Signal Doc Notes`, `Official Sample Sources`, `Relevant APIs`, and heading inventories are generation notes, not runtime content. Preserve their actionable information by rewriting it into the required topical structure: source coverage summary, core rules, workflows, examples, API notes, traps, review checklist, and follow-up lookup.

Runtime usability rule:

- `SKILL.md` must let Codex choose the correct reference quickly from the user's task.
- `SKILL.md` must route to every required runtime reference, including `common-task-recipes.md`.
- The first 80-120 lines of each topical reference should answer the most common workflow for that topic or clearly route to the section that does.
- Long references must put search terms, "When To Read This", key decisions, and lookup routing near the top.
- A reference fails the usability review if Codex must read the whole file to find the common task workflow, API lookup path, or major warnings.
- `api-main.md` fails runtime usability if mandatory common signatures are buried after broad generated/low-priority entries.

Runtime reference rule:

- Generated `references/*.md` and `SKILL.md` must not require, mention, link to, or instruct the agent to open `raw/` files.
- Do not include `Sources Used` sections with raw paths in references.
- Do not include raw source paths such as `raw/wiki-docs/...`, `raw/samples/...`, or `raw/game-data/...` in references or `SKILL.md`.
- Do not include disguised local provenance such as `official sample corpus/...`, `extracted game API/...`, `markdown/Arma_Reforger_*.md`, or generated source-file lists in runtime references. Exact local provenance belongs only in `generation/review.md`.
- References may name source families in prose, such as "official wiki docs", "official samples", or "extracted API data", but exact raw file paths belong only in `generation/review.md`.
- References must include enough summarized guidance, examples, signatures, traps, and routing to be useful without regeneration.

Size guidance:

- Useful detail targets are based on the current corpus shape: most normal topical references should land around 500-1000 nonblank lines when source material is dense, with smaller ranges only for genuinely narrower domains. These are useful-detail ranges, not padding quotas.
- A required topical reference under 250 nonblank lines fails the completeness audit unless `generation/review.md` gives a topic-specific reason backed by sparse source material and names the exact sparse source set.
- `overview.md` should usually land around 120-300 nonblank lines and fails under 80 nonblank lines unless it has a sparse-source justification. It still fails at any size if it cannot route code-vs-data decisions and raw-source usage without relying on another overview.
- `common-task-recipes.md`, `examples-patterns.md`, and `api-main.md` fail the completeness audit when under 200 nonblank lines unless `generation/review.md` gives a topic-specific sparse-source justification. Generic "compactness" is not a valid justification for these central references.
- Expected useful-detail ranges:
  - `overview.md`: 120-300 nonblank lines.
  - `scripting-core.md`: 500-1000 nonblank lines.
  - `scripting-language.md`: 450-900 nonblank lines.
  - `entity-component-lifecycle.md`: 500-900 nonblank lines.
  - `networking-multiplayer-replication.md`: 500-900 nonblank lines.
  - `resources-prefabs-configs.md`: 500-1000 nonblank lines.
  - `workbench-tools-debugging.md`: 450-850 nonblank lines.
  - `scenario-framework-game-master.md`: 450-850 nonblank lines.
  - `terrain-world-editor.md`: 450-850 nonblank lines.
  - `assets-weapons-vehicles-animation-audio.md`: 500-1000 nonblank lines.
  - `server-runtime-packaging.md`: 350-750 nonblank lines.
  - `examples-patterns.md`: 500-1000 nonblank lines.
  - `common-task-recipes.md`: 450-900 nonblank lines.
  - `api-main.md`: 500-1200 nonblank lines, with mandatory common signatures near the top.
  - `api-extended.md`: exempt because it is generated exhaustive fallback data.
- Falling below the useful-detail range is not automatically fatal if the hard minimum, required concepts, examples, traps/checklists, API notes, runtime usability, and exact sparse-source proof all pass. Falling below both the useful range and the hard minimum is a fail.
- Passing a line target with repeated or generic text is worse than failing the line target honestly. Never add non-domain filler to satisfy the count. The correct outcome for insufficient curated content is `INCOMPLETE` or `STRUCTURALLY VALID BUT DESIGN-INCOMPLETE`, not padded references.
- Split a reference if it grows too large to load usefully for a single task.
- Prefer section tables, concise examples, stable in-skill references, and search terms over long copied passages.
- For any large reference, include a short table of contents and useful search terms near the top.

Completion gate:

- Do not proceed from reference writing to `SKILL.md` until the reference completeness audit passes.
- Do not report the generation as complete when a required reference is below its threshold without a specific sparse-source justification.
- Do not report the generation as complete until `generation/review.md` includes a coverage map showing which source documents, sample groups, and API domains were preserved, summarized, deferred to `api-extended.md`, or intentionally omitted.
- Do not treat line counts, successful structural validation, or a passing helper script as sufficient proof of detail retention.
- Do not treat `generation/review.md` claims as sufficient proof of detail retention unless the claims are backed by runtime evidence in the generated references.
- If time, context, or tooling prevents expansion, write `generation/review.md` with status `INCOMPLETE`, list every failing reference, and stop. Do not create a final-sounding summary that says the skill was rebuilt.
- "Substantially more useful than before" is not a pass condition.

Semantic completeness rule:

- Each required reference must have a required-concept coverage matrix in `generation/review.md`.
- Each matrix row must include:
  - `Reference`
  - `Concept ID`
  - `Required concept`
  - `Raw source provenance`
  - `Runtime evidence terms`
  - `Required example or no-example rationale`
  - `Required API/signature coverage`
  - `Status`
  - `If failed, required expansion`
- `Runtime evidence terms` must be concrete strings, headings, method names, config fields, workflow step names, or example labels that appear in the generated runtime reference. Generic terms such as `workflow`, `check`, `system`, `verify`, `example`, `reference`, or the reference title do not count as evidence.
- A concept row is `PASS` only when the runtime reference contains enough detail for Codex to act without opening raw sources. A one-line mention or checklist-only mention is not enough unless the concept is intentionally narrow and the review says why.
- Every required concept must be represented by at least one of: a workflow subsection, a concrete example, an API note/signature, a trap, or a review check. High-risk concepts, especially lifecycle, networking, resources/prefabs/configs, Workbench tooling, and server/runtime, require at least two of those forms.
- A reference fails when most of its evidence is only `Confirm ...` checklist bullets. Checklists are review aids, not the main detail-retention mechanism.
- A reference fails when source coverage appears only in `generation/review.md` and not in the runtime reference.
- A reference fails when it has many broad bullets but lacks concrete nouns from the source domain, such as API names, config/resource names, Workbench steps, lifecycle callbacks, file types, or sample family names.
- `INTENTIONALLY SHORT` cannot be used for a missing required concept unless the review lists the exact sparse source set checked and explains why adding more would be padding.

Use the required topical reference template below. Within that structure, each topical reference must deliver:

- Key official wiki/doc guidance, with synthesized task-focused takeaways before any excerpt.
- At least three task-focused guidance sections unless the topic is genuinely narrow.
- Concrete examples from docs or official samples when useful.
- At least one direct code, config, command, or project-layout example, or an explicit "No direct example included because..." note.
- Common mistakes, traps, or review checks.
- Relevant APIs, with enough signatures or lookup targets to code safely.
- Follow-up search terms and lookup routing to `api-main.md` and `api-extended.md` for uncertain methods/classes.
- Source-family labels only; exact local provenance belongs in `generation/review.md`.

Required topical reference template:

```markdown
# <Reference Title>

Search terms: <task terms, API names, file/data names>

## When To Read This

## Source Coverage Summary

## Core Rules

## Workflows

## Examples

## API Notes

## Common Traps

## Review Checklist

## Follow-Up Lookup
```

Use this template as the default shape for every topical reference. Rename sections only when the topic clearly needs a better domain-specific label, but keep the same functional coverage. `overview.md`, `api-main.md`, and `api-extended.md` may use specialized structures, but they still need search terms, review guidance, and lookup routing where applicable.

Line count alone is not sufficient. A 300-line file made of copied source noise, repeated bullets, or generic advice is not acceptable. Conversely, a shorter file can be acceptable only when it is dense, source-grounded, and `generation/review.md` explains why more detail would be padding.

No-padding rule:

- Do not create sections whose purpose is to increase line count rather than help Codex do Reforger work.
- Do not use headings such as `Operational Detail Retention`, `Expanded Source-Grounded Review Notes`, `Retention Notes`, or similar meta-audit headings in runtime references.
- Do not use headings such as `Example Marker`, `Audit Marker`, `Coverage Marker`, or generic one-line marker sections to satisfy examples, API notes, or checklist gates.
- Do not add generic lines like "examples and snippets in this reference are summarized..." as a substitute for a concrete example or explicit no-example rationale.
- Do not add numbered repeated bullets that restate the same generic instruction with different numbers.
- Do not repeat the same checklist item across a reference unless each instance is tied to a different concrete workflow, API, sample, or trap.
- Each substantive bullet should preserve a distinct source-grounded rule, warning, API signature, workflow step, example implication, file shape, or review check.
- If a reference cannot meet its target without padding, record the exact gap in `generation/review.md` and keep the run incomplete. Do not mask the gap with filler.

Detail retention rules:

- Preserve every operational rule, warning, prerequisite, limitation, required file shape, required Workbench step, required config field, and API signature that would change how Codex writes or reviews a Reforger mod.
- Compress tutorial prose, screenshots, navigation text, repeated introductions, and long asset/config dumps, but keep the actionable sequence and the exact decision points.
- For each source document assigned to a reference, record in `generation/review.md` whether its actionable content was preserved as guidance, preserved as an example, summarized as background, superseded by API data, or intentionally omitted as non-actionable.
- The review coverage map must identify the top retained operational rules, top intentionally omitted details, and top details deferred to `api-main.md` or `api-extended.md`; it is not enough to list that a source was considered.
- If a source document is long or dense, the generated reference must include a coverage subsection for its major concepts rather than only naming the document in review.
- If multiple source documents repeat the same rule, merge the rule once and note the repeated source family in review.
- If the generated reference cannot preserve a detail without becoming too large, keep the task-critical detail in the topical reference and defer only exhaustive lookup material to `api-main.md` or `api-extended.md`.
- A rebuild that reduces a broad wiki/API corpus to mostly high-level summaries is incomplete even if every reference has examples, traps, and API notes.

Use wiki/docs information as the strongest generation source. Use game API data to verify names, signatures, inheritance, methods, and properties. Put exact source file paths in `generation/review.md`, not runtime references, except for `api-extended.md`, whose purpose is exhaustive source-file/line lookup from extracted API data.

Use official samples to add concrete examples and real file-layout patterns. Prefer small excerpts and summaries over large code dumps. For script examples, include enough context to show the pattern without requiring the raw sample file. For asset-heavy samples, summarize the structure and relevant `.conf`, `.et`, `.ent`, or README concepts instead of copying bulk asset data. Record exact sample paths in `generation/review.md`.

Markdown quality rules:

- Use one `#` title per reference, `##` for main sections, and `###` only when needed.
- Do not emit collapsed headings such as `# Glossary ### Prefab`, `## Root ### bindAddress`, or any line that contains multiple Markdown headings run together.
- Do not leave raw wiki image links such as `[](/wiki/File:...)`, `[image omitted]`, thumbnail placeholders, edit links, category noise, or navigation breadcrumbs in runtime references. If the image carries operational meaning, summarize the actionable point in prose.
- Do not leave flattened scraped tables such as `## Moddability table | Extension | File Type | ...` or any one-line table dump with many pipe characters. Convert valid small tables to real Markdown tables with one row per line; convert large or messy tables to bullet lists grouped by decision or workflow.
- Do not leave copied source section scaffolding in runtime references. Runtime references must not contain `Official Wiki Sources`, `High-Signal Doc Notes`, `Official Sample Sources`, `Relevant APIs`, `Headings:`, `Source family:`, `Source: markdown/...`, `Show details`, or UI-only crawl text such as `Copy`.
- Do not leave stale table-of-contents entries that point to sections removed during cleanup. After deleting or renaming sections, update the TOC or remove it.
- Do not leave API source-file paths such as `addons_core\scripts\...` in topical references or `api-main.md`; put exact API source provenance in `generation/review.md`. `api-extended.md` may include extracted source paths because it is the exhaustive search fallback.
- Do not leave mojibake or replacement-character artifacts in runtime references. Reject visible artifacts such as `â`, `Ã`, `ðŸ`, `�`, `â€œ`, `â€`, `â†`, `âš`, or `â“˜` unless they appear inside an intentionally quoted source excerpt with a correction note.
- Do not leave raw copied UI-key glyph corruption. Convert corrupted arrows, warning icons, notes, and key names into plain ASCII labels such as `WARNING`, `NOTE`, `Shift`, `Backspace`, `Left`, and `Right`.
- Do not leave source-crawl prose that depends on an omitted image without summarizing the image's actionable point.
- Include a short table of contents or search-term block for references over roughly 100 lines.
- Use fenced code blocks with language tags such as `c`, `json`, `text`, or `powershell`.
- Convert scraped tables that do not render cleanly into bullet lists.
- Remove meaningless copied UI text such as `Copy`, edit buttons, image-only links, icons, and navigation labels.
- Normalize encoding artifacts and punctuation in generated references.
- Do not cite raw local source paths in runtime references. Cite stable public URLs only when useful and available; otherwise record exact local provenance in `generation/review.md`.
- Summarize messy excerpts instead of copying raw scraped blocks.
- After writing references, grep for malformed Markdown and crawl artifacts. If any are found, fix the reference or mark the run incomplete.

Code example rules:

- Examples are additive. They must not replace source-grounded guidance, gotchas, or API notes.
- Examples must be concrete. A generic marker sentence is not an example.
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

The concept lists below are minimum semantic gates. They are not outlines and they are not optional. During rebuild, every concept must be covered in the runtime reference and recorded in the required-concept coverage matrix in `generation/review.md`.

For each required concept:

- Preserve the operational rule or workflow detail, not just the concept name.
- Include source-grounded examples when available.
- Include API lookup guidance or signatures when code is involved.
- Include traps or review checks for fragile workflows.
- Record exact raw provenance only in `generation/review.md`.

### `overview.md`

General Reforger context and modding map. Cover Enfusion, Workbench, addons, scripts, resources, prefabs, configs, world data, assets, Workshop, and where the raw data came from.

Required concepts:

- `OVR-ROUTING`: Route script-first, data-first, editor-first, server-first, asset-first, and mixed tasks to the correct references.
- `OVR-SOURCE-AUTHORITY`: Explain docs as rules, samples as examples, and API data as signature truth.
- `OVR-WORKBENCH-DATA`: Explain why many Reforger tasks require Workbench resources, prefabs, configs, worlds, or layouts rather than script-only changes.
- `OVR-VALIDATION`: Explain the verification loop: topical reference, API lookup, available project checks, and residual Workbench/runtime uncertainty.
- `OVR-RISK-ORDER`: Name high-risk areas that require deeper references: lifecycle, replication, resources/prefabs/configs, Workbench tooling, and packaging.

### `scripting-core.md`

Primary scripting reference. This should be the richest topical reference.

Use docs such as scripting first steps, scripting modding, examples, best practices, do's and don'ts, conventions, performance, ScriptInvoker, and script profiling.

Use official samples such as `SampleMod_ModdedScript` and script files from other sample mods for concrete examples.

Cover file/class organization, event/callback patterns, lifecycle patterns, modded class patterns, performance, debugging, profiling, and gotchas.

Include direct examples for a minimal script file/class, a modded class override from official samples, `Print`/`PrintFormat`, and `ScriptInvoker` where supported by generation sources.

Required concepts:

- `SCR-MODULES`: Script module/folder placement and consequences when scripts are outside recognized modules.
- `SCR-TAGGING`: Creator tag, class/file naming, and collision avoidance rules.
- `SCR-MODDED`: Modded-class file layout, exact override-signature verification, and `super` handling.
- `SCR-DEBUG`: `Print`, `PrintFormat`, log levels, Remote Console distinction, and noisy-log traps.
- `SCR-INVOKER`: `ScriptInvoker` accessor pattern, lazy initialization, subscription signature matching, and why direct public invoker mutation is risky.
- `SCR-PERF`: Performance rules for avoiding unnecessary, misplaced, excessive, same-frame, or too-frequent work.
- `SCR-PROFILING`: Profiling/diagnostic routing before performance claims.
- `SCR-EVENTS`: Event/callback registration and event-driven alternatives to polling.
- `SCR-EXAMPLES`: At least three concrete code examples: minimal class, modded override shape, and debug/invoker/event pattern.

### `scripting-language.md`

Enfusion Script language mechanics.

Cover keywords, operators, values, automatic reference counting, classes, inheritance, constructors/destructors, annotations/attributes, config objects, JSON, preprocessor directives, and macros.

Include direct examples for typed variables, arrays, loops, conditionals, class/method style, `ref` ownership/ARC-safe patterns, and JSON/config object usage where supported by generation sources.

Required concepts:

- `LANG-SYNTAX`: Enfusion syntax, classes, methods, constructors/destructors, inheritance, and override constraints.
- `LANG-TYPES`: Primitive values, vectors, arrays, maps/sets where supported, typed variables, constants, and enum naming.
- `LANG-ARC`: Automatic reference counting, `ref`, object lifetime, and native/managed reference traps.
- `LANG-ATTRIBUTES`: Annotations/attributes for serialized/editor fields and Workbench widget params.
- `LANG-CONFIG`: Config object usage, BaseContainer/config-class patterns, failure handling, and serialized-field stability.
- `LANG-JSON`: JSON read/write or API patterns when source-supported, including parse/failure handling.
- `LANG-PREPROCESSOR`: Preprocessor/macro usage, limits, and review risks.
- `LANG-EXAMPLES`: Direct examples for type declarations, control flow, class/method style, `ref`, attribute fields, and config/JSON use where supported.

### `entity-component-lifecycle.md`

Entity and component coding patterns.

Use docs such as Create a Component, Create an Entity, Entity Lifecycle, Entity Activeness, BaseDoorComponent, Prefab Data, and Prefabs Basics.

Use official sample `.c`, `.et`, and `.conf` files where they demonstrate entity/component wiring.

Cover entity/component relationships, lifecycle callbacks, update behavior, prefab integration, safe extension, and lifecycle traps.

Include direct examples for `ScriptComponentClass` plus `ScriptComponent`, `ComponentEditorProps`, editable `[Attribute]` fields, `EOnInit`, and entity movement/teleport with `IEntity.SetOrigin` or transform APIs. If player access uses `g_Game.GetPlayer()` or another accessor that is not clearly present in schema, label it `example-observed, verify in project`.

Required concepts:

- `ECL-CLASS-PAIR`: `ScriptComponentClass`/`ScriptComponent` and entity/component class pairing rules.
- `ECL-EDITOR-PROPS`: `ComponentEditorProps`, categories/descriptions, and editable `[Attribute]` fields.
- `ECL-LIFECYCLE`: `EOnInit`, `OnPostInit`, delete/activation/deactivation/parent-child callbacks where source-supported.
- `ECL-EVENT-MASKS`: Event masks, frame/update callbacks, and when to avoid per-frame work.
- `ECL-OWNER`: Owner/entity guards, `GetOwner`, component lookup/cast guards, and optional sibling components.
- `ECL-TRANSFORM`: `IEntity` origin/transform APIs, local-vs-world transform distinction, and movement authority caveats.
- `ECL-PREFAB`: Prefab integration, serialized field stability, activeness, and Workbench preview traps.
- `ECL-EXAMPLES`: Component skeleton, editable field example, guarded init example, and movement/teleport example with verified API signatures.

### `networking-multiplayer-replication.md`

Multiplayer and network-safe scripting.

Use docs such as Multiplayer Scripting and any replication/server/network material. Cover authority, ownership, replication, RPC/network event patterns if present, client/server execution, synchronized state, debugging, and common multiplayer traps.

Use samples only if they show real multiplayer or replicated setup. Do not infer networking rules from samples that are not explicitly network-focused.

Include direct examples for authority/proxy/owner checks and a minimal RPC or replicated-property pattern if raw docs/API data supports it. Include one warning anti-example for client-local state/entity changes that should be authority-gated.

Required concepts:

- `NET-ROLES`: Authority/master, proxy, owner, owner proxy, remote proxy, and why client/server is not sufficient.
- `NET-MUTATION`: Authority-side state mutation and proxy/client read or presentation paths.
- `NET-RPLCOMP`: `BaseRplComponent` role/ownership API signatures and guarded lookup.
- `NET-RPLPROP`: `RplProp` state replication, update/bump/notify uncertainty, and initial-state concerns.
- `NET-RPC`: `RplRpc` purpose, attribute/signature verification, direction/target/reliability uncertainty, and initialization-path traps.
- `NET-SPAWN`: Authority-safe spawn/despawn/movement for replicated gameplay entities.
- `NET-USER-ACTIONS`: User action/client request routing through authority when gameplay state changes.
- `NET-EXAMPLES`: Authority check example, replicated property skeleton, RPC skeleton or explicit no-example rationale, and one anti-example.

### `resources-prefabs-configs.md`

Resources, prefabs, config classes, UI/layout resources, and editor data.

Use Resource Manager, Resource Usage, Config Editor, Create a Config Class, Prefab Data, Prefabs Basics, dialog/layout/widget docs, and related API data.

Use official sample `.conf`, `.et`, `.ent`, and README files to show real resource, prefab, entity catalog, arsenal, editable prefab, and config layout patterns.

Include direct examples for config snippets, resource/prefab paths, entity catalog or arsenal config layout, and resource load or prefab spawn code if supported by raw API data.

Required concepts:

- `RES-DATA-FIRST`: Data-first versus script-first decision rules for resources, prefabs, configs, and layouts.
- `RES-RESOURCENAME`: `ResourceName` field authoring, resource picker attributes, empty-value guards, and `Resource.Load`.
- `RES-PREFAB`: Prefab inheritance, override/modify/inherit distinctions, prefab component wiring, and serialized-field stability.
- `RES-CONFIG`: Config class/object workflow, BaseContainer/config access, defaults, and failure handling.
- `RES-CATALOG`: Entity catalog, arsenal, faction/scenario consumer relationships, and editable prefab implications.
- `RES-UI-LAYOUT`: Layout/widget resources versus widget script handlers and UI lookup traps.
- `RES-SPAWN`: Prefab/resource spawn workflow with `EntitySpawnParams` verification and authority caveats.
- `RES-EXAMPLES`: Config snippet, `ResourceName` field, resource load snippet, prefab/entity catalog layout example, and UI/layout example or no-example rationale.

### `workbench-tools-debugging.md`

Workbench, Script Editor, plugins, diagnostic tools, and profiling.

Use Workbench plugin docs, Script Editor docs, Diag Menu, Script Profiling, Resource Manager plugin docs, and World Editor plugin docs.

Use `SampleMod_WorkbenchPlugin` as the main concrete source for Workbench plugin examples.

Include direct examples for a `WorkbenchPluginAttribute` plugin class, a `Workbench.GetModule(...)` pattern if supported, and diagnostic/profiling commands or scripts where raw docs support them.

Required concepts:

- `WB-MODULE-SCOPE`: Workbench/editor module separation from runtime game modules.
- `WB-PLUGIN`: `WorkbenchPlugin`, `WorkbenchPluginAttribute`, `Run`, `RunCommandline`, and context-menu hooks where supported.
- `WB-MODULES`: Resource Manager, Script Editor, World Editor, String Editor or other module-specific APIs and availability boundaries.
- `WB-SELECTION`: Resource/world/script selection handling and empty-selection guards.
- `WB-DIAG`: Diag Menu, Script Editor, Remote Console, logs, and diagnostic routing.
- `WB-PROFILING`: Script profiling and performance workflow before optimization claims.
- `WB-AUTOMATION`: Resource registration/rebuild, command-line/plugin automation, and destructive-action safeguards.
- `WB-EXAMPLES`: Workbench plugin skeleton, module lookup or explicit no-example rationale, and diagnostic/profiling example.

### `scenario-framework-game-master.md`

Scenario Framework, Game Master, tasks, factions, and game mode content.

Use Scenario Framework, setup/update tutorials, Game Master tutorials, Task System Usage, Faction Creation, Entity Catalog, and Game Identity.

Use `SampleMod_NewFaction`, sample mission/config files, entity catalog configs, and relevant `.ent` files for real faction/scenario examples.

Include direct examples for faction config path shapes, entity catalog config structure, and a scenario/Game Master setup checklist. Put exact raw source paths in `generation/review.md`.

Required concepts:

- `SCN-DATA-FIRST`: Scenario/Game Master/faction work as data-first unless script integration is required.
- `SCN-FACTIONS`: Faction configs, groups, characters, gear, identity/display strings, and Conflict/Game Master integration.
- `SCN-CATALOG`: Entity catalogs, editable/placeable prefabs, and performance/replication implications.
- `SCN-TASKS`: Task system workflow, ownership, completion, cleanup, and script integration cautions.
- `SCN-GAMEMODE`: Scenario layers, game mode setup, world/config dependencies, and startup assumptions.
- `SCN-GM`: Game Master editable prefab setup and required Workbench/plugin steps.
- `SCN-EXAMPLES`: Faction config layout, entity catalog layout, scenario/Game Master checklist, and task example or no-example rationale.

### `terrain-world-editor.md`

Terrain creation, world editing, generators, navmesh, roads, rivers, and map tooling.

Use Terrain Tutorial, New Terrain Setup, Terrain Entity, World Editor docs, generator/tool pages, navmesh docs, and terrain preparation docs.

Use samples only where they include relevant world/editor files. Do not treat asset showcase worlds as general terrain guidance unless the docs support that pattern.

Include direct examples for world file layout, terrain/world-editor path layout, and generator/navmesh/road/river checklist items from docs.

Required concepts:

- `TER-WORLD`: New world/base scene setup, world resource layout, save points, and terrain entity placement.
- `TER-TERRAIN`: Terrain entity/origin requirements, terrain creation, sculpting, materials/layers, and collision implications.
- `TER-NAVMESH`: Navmesh generation/rebuild workflow and AI validation.
- `TER-ROADS-WATER`: Road, river, lake, and water workflows and their distinct resource/editor implications.
- `TER-GENERATORS`: Forest/object/shape/generator tools, generated-output review, and performance risks.
- `TER-MAP`: 2D map/map tooling and exported/generated data expectations.
- `TER-WE-TOOLS`: World Editor tool/API boundaries and editor-only automation caveats.
- `TER-EXAMPLES`: World layout example, terrain setup checklist, navmesh checklist, and road/river/generator checklist.

### `assets-weapons-vehicles-animation-audio.md`

Asset workflows that affect code and mod integration.

Use Assets, Textures, FBX Import, Model Performance, weapon pages, vehicle pages, animation editor pages, audio editor pages, sound component docs, and character gear docs.

Use official sample mods for concrete file layouts: new/modded weapons, new/modded cars, new character, new prop, replacement, animation workshop, and cinematic tutorial.

Include direct examples for weapon, vehicle, character gear, animation, and audio path/config layouts where official samples or docs provide them.

Required concepts:

- `ASSET-PIPELINE`: Asset preparation, import, resource processing, prefab/config setup, and script integration boundaries.
- `ASSET-MODEL-TEXTURE`: FBX/model, texture/material, LOD/collision/performance workflow and traps.
- `ASSET-WEAPON`: Weapon prefab/config surfaces: muzzle, magazine, attachments, effects, animation, audio, and user actions.
- `ASSET-VEHICLE`: Vehicle prefab/config surfaces: simulation, damage, fuel, seats, actions, physics, and controller components.
- `ASSET-GEAR`: Character gear, attachment points, inventory/arsenal/faction integration.
- `ASSET-ANIMATION`: Animation editor, graph/variables, controllers, authored resources, and script touchpoints.
- `ASSET-AUDIO`: Audio editor, sound events, signals, variables, occlusion, and runtime trigger paths.
- `ASSET-EXAMPLES`: Weapon, vehicle, gear, animation, and audio layout examples or explicit no-example rationale for any unsupported area.

### `server-runtime-packaging.md`

Runtime, startup, server hosting/config, Workshop, packaging, and deployment.

Use Startup Parameters, Server Config, Server Hosting, Server Management, Workshop, Backend API, REST API Usage, and system requirements.

Use samples for packaging/addon layout examples only. Do not use samples as server configuration authority unless the sample explicitly contains server/runtime configuration.

Include direct examples for startup parameters, server config fields, `.gproj` layout, and addon/project packaging layout when generation sources provide them.

Required concepts:

- `SRV-STARTUP`: Startup parameters, branch/version assumptions, and launch context.
- `SRV-CONFIG`: Server config fields, secrets/logging safety, ports/network settings, and dedicated-server behavior.
- `SRV-ADDONS`: Addon dependencies, load order, `.gproj`, project metadata, and packaging inclusion.
- `SRV-WORKSHOP`: Workshop publishing, metadata, dependency warnings, visibility, and backend/login caveats.
- `SRV-RUNTIME`: Dedicated server versus client/editor behavior and no local-player/UI assumptions.
- `SRV-SCENARIO`: Scenario/world/game mode startup configuration and server resource availability.
- `SRV-VALIDATION`: Static config checks, test-server launch when possible, logs, rollback, and residual runtime risk.
- `SRV-EXAMPLES`: Startup command/config snippet, server config snippet, `.gproj` or addon layout example, and packaging checklist.

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

Required concepts:

- `EX-SAMPLE-INVENTORY`: Every official sample mod named with purpose and primary systems demonstrated.
- `EX-LAYOUTS`: Common addon/project layout patterns including scripts, configs, prefabs, worlds, resources, and project metadata.
- `EX-SCRIPT-PATTERNS`: Modded script, component/user-action, and Workbench plugin script patterns with short code excerpts where source-supported.
- `EX-DATA-PATTERNS`: Config, prefab, entity catalog, arsenal, world, and faction layout patterns.
- `EX-ASSET-PATTERNS`: Weapon, vehicle, character, prop, replacement, animation, and cinematic sample patterns.
- `EX-CROSSLINKS`: Cross-links from each sample family to the topical references that should be read before reuse.
- `EX-UNCERTAINTY`: Warnings that samples are examples and signatures/workflows still require docs/API verification.

### `common-task-recipes.md`

Common Reforger coding recipes generated from official docs, official samples, and verified API signatures.

Use this as a fast path after `SKILL.md` routing when the user asks for a common task such as "make a component", "teleport a player", "spawn a prefab", "add a user action", or "make a simple RPC".

This reference should be practical and explicit. It should avoid long raw excerpts and instead point back to topical references for deep background.

Every recipe should include a direct example block when generation sources support it. If a complete verified code example is not available, include a smaller verified snippet plus an explicit uncertainty note.

Required concepts:

- `REC-COMPONENT`: Create `ScriptComponentClass` plus `ScriptComponent`, editor props, attributes, and guarded init.
- `REC-DEBUG`: Print/debug safely with context and log spam traps.
- `REC-TRANSFORM`: Get origin/transform and move/teleport owner/entity with verified `IEntity` APIs.
- `REC-PLAYER`: Get local player/controlled entity only with project-context warning and verification guidance.
- `REC-EVENTS`: Register frame/update/event masks safely and avoid polling.
- `REC-USER-ACTION`: Add/modify user actions with owner/user guards and authority routing.
- `REC-RESOURCE`: Use `ResourceName`, `Resource.Load`, prefab reference fields, and empty/failure guards.
- `REC-SPAWN`: Spawn prefab/entity with resource load, spawn params, and authority caveats.
- `REC-RPC`: Basic replicated/RPC skeleton with authority, `RplProp`, `RplRpc`, and verification notes.
- `REC-WORKBENCH`: Workbench plugin command skeleton with editor-only API boundaries.
- `REC-DATA-FIRST`: Explain whether each recipe is script-first, data-first, editor-first, or mixed.
- `REC-EXAMPLES`: Each required recipe must have a direct example or explicit no-example rationale.

### `api-main.md`

Create this during the AI reference-building pass, not with a deterministic script.

Purpose: compact top-API reference for normal coding work. It should be curated by Codex while building the topical references, using official wiki/docs as source of truth and raw API schema for signatures.

Build `api-main.md` as a draft during core reference writing, then finalize it after topical references and recipes reveal which APIs are actually common. Do not freeze it before the topical references are complete.

Keep this file useful and bounded. Include only APIs that are clearly important for common Reforger scripting and modding tasks. Prefer APIs that appear in official docs, examples, lifecycle patterns, networking, entity/component work, resources/prefabs/configs, Workbench tooling, UI/input, game/world/player systems, scenarios, weapons, vehicles, animation, and audio.

Order `api-main.md` by practical coding priority, not alphabetically. Put search terms, mandatory common signatures, and task-domain API groups at the top before lower-priority generated entries. If broader generated entries are retained, place them after the curated common sections or split them into `api-extended.md`.

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

`api-main.md` fails if mandatory common signatures are present only in a late appendix after unrelated generated entries. The first 150 lines should be useful for ordinary component/entity/resource/network/Workbench tasks.

Required concepts:

- `API-ENTITY`: Exact common `IEntity` transform/origin/orientation/component/event-mask signatures near the top.
- `API-COMPONENT`: Exact `ScriptComponent`, `ScriptComponentClass`, `GenericComponent`, and related lifecycle/owner signatures.
- `API-GAME-SPAWN`: Exact `Game`, world, resource, prefab spawn/delete/player-access signatures when present, plus missing-API notes.
- `API-RESOURCE`: Exact `Resource`, `ResourceName`, config/prefab/resource-loading signatures and usage notes.
- `API-REPLICATION`: Exact `BaseRplComponent`, `RplRpc`, `RplProp`, role/ownership, `RplLoad`/`RplSave` or missing-gap notes.
- `API-INPUT-UI`: Exact input/action/user-action/widget signatures where present.
- `API-WORKBENCH`: Exact `WorkbenchPlugin`, `ScriptEditor`, `WorldEditor`, `ResourceManager`, plugin hook, and editor-only API signatures.
- `API-DOMAINS`: Curated lookup groups for weapon, vehicle, inventory, audio, animation, task, faction, scenario, and other common gameplay domains.
- `API-GAPS`: Expected-common APIs missing from schema or only observed in docs/samples listed explicitly with verification notes.
- `API-ORDER`: Mandatory common APIs appear before broad generated entries or alphabetical dumps.

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
9. Create a draft required-concept coverage matrix from the required concepts in this design. Do not write final references until every required concept has assigned source candidates or a documented sparse-source gap.

Phase 2 - Core references:

1. Start a draft `references/api-main.md` from verified API schema entries and cited docs/samples. Include exact signatures for mandatory API groups as they are encountered. Put exact schema/source paths in the draft review, not runtime references.
2. Build `references/scripting-core.md`, `references/entity-component-lifecycle.md`, `references/networking-multiplayer-replication.md`, and `references/resources-prefabs-configs.md` before lower-priority topics.
3. Build topical references from official wiki/docs first. Preserve the docs as the main source of truth.
4. Curate topical references directly as Codex-authored Markdown. Do not write or run a deterministic reference-generation script.
5. Add direct code, config, command, and project-layout examples where they improve the reference. Examples are additive to the source guidance and must be source-labeled by category, but must not cite local `raw/` paths in the reference.
6. Verify every API name/signature used in topical references, examples, and recipes against `raw/game-data/api-schema.json`.
7. For every required concept in each core reference, record runtime evidence terms in the draft review. If a concept has no runtime evidence in the reference, expand the reference before moving on.

Phase 3 - Remaining references and recipes:

1. Build the remaining topical references in priority order from this design.
2. Build `references/examples-patterns.md` from official samples as the central sample layout/example map. Inventory every official sample mod by name and purpose, without raw local file paths.
3. Build `references/common-task-recipes.md` from official docs, samples, and verified APIs. Include direct example blocks for supported recipes.
4. Finalize `references/api-main.md` after topical references and recipes reveal the actually common APIs. Record expected-common API gaps in `api-main.md` and in the draft review.
5. Check markdown quality for every reference: valid headings, fenced code blocks, readable lists/tables, source labels, no raw crawl noise, no copied crawler sections, no stale TOC entries, no flattened inline table dumps, no image placeholders, no mojibake, no image-only wiki links, no collapsed heading runs, no generic audit-marker sections, and clean GitHub rendering.
6. Complete the required-concept coverage matrix for every runtime reference. Every row must include source provenance, runtime evidence terms, example/API requirements, and `PASS`, `FAIL`, or `INTENTIONALLY SHORT`.
7. Write or update a draft `generation/review.md` before the pre-skill audit. The draft review must include source inventory, completeness table, coverage maps, required-concept matrix, actionable-detail retention notes, raw provenance, known gaps, and status `INCOMPLETE` or `STRUCTURALLY VALID BUT DESIGN-INCOMPLETE` until final validation passes.

Phase 4 - Pre-skill audit gate:

1. Run the checked-in audit script:

```powershell
py -3 scripts\audit-references.py
```

2. Before trusting the result, confirm the checked-in audit script implements every current hard gate in this design. If the script cannot verify semantic concept coverage, formatting gates, runtime-reference bans, and required recipe/API/sample coverage, the rebuild status is `STRUCTURALLY VALID BUT DESIGN-INCOMPLETE` until the script is updated or the review records a manual audit with equivalent evidence.
3. The audit must check:
   - Every required reference exists.
   - Nonblank line targets are met or have topic-specific `INTENTIONALLY SHORT` justification.
   - No runtime reference uses padding to meet line targets. Reject `Operational Detail Retention`, `Expanded Source-Grounded Review Notes`, repeated numbered retention bullets, repeated generic bullets, and any other section whose content is not distinct Reforger guidance.
   - No generated runtime reference or `SKILL.md` contains `raw/` paths or a raw-source `Sources Used` section.
   - `generation/review.md` contains exact raw source provenance for every generated reference.
   - Every applicable reference has traps/checklists and examples or explicit no-example rationale.
   - Every reference has a review coverage map for assigned source documents, sample groups, and API domains.
   - Every required concept from this design appears in `generation/review.md` with runtime evidence terms, raw provenance, and `PASS`/`FAIL`/`INTENTIONALLY SHORT` status.
   - Every required concept marked `PASS` has its runtime evidence terms present in the corresponding generated reference.
   - No reference passes primarily through generic checklist bullets. The audit must fail references where required concepts are only mentioned in review checklists without workflow, example, API, trap, or task guidance.
   - Topic-specific required terms are present for each reference. For example, networking must include authority/proxy/owner/RPC/replication terms; resources must include `ResourceName`, resource loading, prefab/config/catalog/layout terms; lifecycle must include component class pairs and lifecycle callback terms.
   - Reference runtime usability gates are met: common workflows near the top of references, clear lookup routing, and no whole-file scan required for ordinary tasks.
   - Markdown quality gates are met: no mojibake, no raw wiki image links, no image placeholders, no collapsed headings, no crawl navigation text, no copied crawler sections, no stale TOC entries, no flattened inline table dumps, no malformed tables, and no generic `Example Marker`/audit-marker sections.
   - `common-task-recipes.md` includes every required recipe.
   - `examples-patterns.md` inventories all official sample mods.
   - `api-main.md` includes mandatory API coverage with exact signatures or explicit missing-API gaps, and mandatory common signatures appear near the top rather than buried after low-priority generated entries. Exact schema/source paths for those entries belong in `generation/review.md`.
   - Existing `SKILL.md`, if present, references only existing files.
4. If any required reference fails the completeness audit, expand it before continuing. Do not continue to `SKILL.md` as if the generation passed.
5. Check reference size and usefulness. Split or trim anything that creates context bloat without adding practical lookup value, but do not trim below the required depth bar.

Phase 5 - Final skill, forward tests, and final review:

1. Create `SKILL.md` as a compact router and guardrail that points to the generated references. This is AI/Codex-authored.
2. Create or validate `agents/openai.yaml` so the skill metadata matches `SKILL.md`.
3. Validate the skill folder and generated links.
4. Run the coding-focused forward-test prompts against a temporary throwaway fixture, or record an explicit user waiver.
5. Update `generation/review.md` with forward-test results, validation results, residual risks, and provisional final status.
6. Run `scripts/audit-references.py` again after the review is updated. The final audit must include all pre-skill checks plus `SKILL.md` routing/link checks, `SKILL.md` runtime-reference checks, forward-test results or waiver, final review status, and final runtime usability. If it fails, fix the references, `SKILL.md`, or review and rerun from the affected phase.
7. Update `generation/review.md` one last time with final audit results and final status. This is AI/Codex-authored audit output, not script-generated, but it may quote or summarize the checked-in audit script's results.

Required audit table columns:

- `Reference`
- `Nonblank lines`
- `Line target met`
- `Runtime raw references absent`
- `Review provenance listed`
- `Source coverage mapped`
- `Required concepts mapped`
- `Required concepts evidenced in runtime`
- `Actionable details retained`
- `Runtime usability met`
- `Examples present`
- `Traps/checklist present`
- `API notes present`
- `No padding/filler present`
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

Write one review file, first as a draft during generation and then as the final audit record:

```text
generation/review.md
```

Overwrite it on every skill-generation run. During generation, keep its top-level status as `INCOMPLETE` or `STRUCTURALLY VALID BUT DESIGN-INCOMPLETE` until all hard stops pass.

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
- Required-concept coverage matrix for every generated reference, using every concept ID listed in this design.
- Actionable-detail retention notes for each generated reference: list any warnings, prerequisites, Workbench steps, config fields, API signatures, or sample patterns that were difficult to compress and how they were preserved.
- Runtime usability review: confirm `SKILL.md` routes quickly, each reference exposes common workflows near the top, long references have search terms and lookup routing near the top, and ordinary tasks do not require whole-file scanning.
- Any reference below the expected size target, with either a topic-specific sparse-source justification or explicit `FAIL` status. Do not use broad wording such as "intentionally compressed" as a substitute for a justification.
- A top-level generation status line: `COMPLETE`, `INCOMPLETE`, or `STRUCTURALLY VALID BUT DESIGN-INCOMPLETE`.
- If `quick_validate.py` passes but the completeness audit fails, use `STRUCTURALLY VALID BUT DESIGN-INCOMPLETE`.
- How `api-main.md` was curated.
- Expected-common APIs that were missing or only found in comments/examples.
- Task recipes written and any recipe uncertainty.
- Direct examples added per reference and any references that intentionally lack examples due to missing source support.
- Exact raw source provenance per reference: list the raw wiki/docs, sample, and API files used for each generated reference. This is where raw paths belong.
- Confirmation that generated `SKILL.md` and `references/*.md` contain no `raw/` paths and no instructions to open raw files.
- Confirmation that generated runtime references contain no filler sections, repeated retention bullets, duplicated generic line-count padding, or headings such as `Operational Detail Retention`.
- Markdown quality issues found and fixed, including broken tables, flattened inline table dumps, stale TOC entries, missing code fences, copied crawler sections, image placeholders, crawl artifacts, and unreadable copied excerpts.
- Confirmation that `scripts/audit-references.py` implements the current design gates, or a clear `STRUCTURALLY VALID BUT DESIGN-INCOMPLETE` status if it does not.
- Confirmation that `api-extended.md` was generated exhaustively.
- Any source-data warnings.
- Any suspected gaps.
- Manual review items.

Required source coverage map format:

| Source or source group | Assigned reference | Actionable content retained | Examples retained | Deferred lookup | Omitted content | Omission reason |
| --- | --- | --- | --- | --- | --- | --- |

Rules for this table:

- Use exact source paths only in `generation/review.md`, not runtime references.
- Include every source document, sample group, and API domain that materially influenced a reference.
- Use `none` rather than leaving a cell blank.
- For each generated reference, add a short note below the table naming the top retained operational rules, top intentionally omitted details, and top details deferred to API lookup.
- `Omitted content` must be limited to non-actionable prose, duplicate material, screenshots/navigation, obsolete/conflicting material, or exhaustive lookup data available in `api-extended.md`.
- If the omission reason is `too large`, the rebuild is incomplete unless the omitted material is exhaustive API lookup data or non-actionable bulk asset/config data.

Required concept coverage matrix format:

| Reference | Concept ID | Required concept | Raw source provenance | Runtime evidence terms | Required example/API coverage | Status | If failed, required expansion |
| --- | --- | --- | --- | --- | --- | --- | --- |

Rules for this table:

- Include every required concept ID from the `Reference Files` section.
- `Runtime evidence terms` must be concrete strings that appear in the runtime reference. Use multiple terms when one term would be too weak.
- `Required example/API coverage` must name the concrete example, signature, config shape, command, checklist, or no-example rationale that satisfies the concept.
- A `PASS` row must be auditable by grep against the runtime reference and by provenance against raw source inventory.
- A `FAIL` row must list the exact missing runtime expansion.
- `INTENTIONALLY SHORT` is allowed only for sparse-source concepts with exact source proof and only when the runtime reference still gives useful routing or uncertainty guidance.
- Do not mark concepts `PASS` merely because the review says the concept was considered.

`generation/review.md` is for auditing only. Do not use it as source material in later generations.

## Forward-Test Prompts

After references, `SKILL.md`, and review are written, run or simulate coding-focused forward tests against a temporary throwaway fixture. These tests should produce code or config diffs that can be reviewed with grep/API checks; do not use vague research prompts or tasks that require launching Workbench/game runtime.

Required forward-test prompts:

1. "Use the Reforger skill to add a minimal `ScriptComponent` and matching `ScriptComponentClass` with one editable prefab/resource field and a guarded `EOnInit` debug print."
2. "Use the Reforger skill to add a component method that moves its owner entity to a supplied vector, verifying the exact `IEntity` transform/origin APIs before writing code."
3. "Use the Reforger skill to add a user-action script patterned after official sample user actions, with uncertain APIs clearly marked for project verification."
4. "Use the Reforger skill to add a small replicated/RPC component skeleton that separates authority-side state changes from client-side calls and marks every RPC attribute/signature that needs project verification."
5. "Use the Reforger skill to add a Workbench plugin command skeleton that uses the documented Workbench plugin attribute shape and checks editor-only API usage."
6. "Use the Reforger skill to add a config/prefab reference field example using `ResourceName` and explain whether the task is script-first or data-first."

Forward-test review requirements:

- Record each prompt in `generation/review.md` with `PASS`, `FAIL`, or `NOT RUN`.
- For each test, list the references opened, APIs checked, generated files or diff summary, and review result.
- A test passes only if the output uses routed references, checks uncertain APIs in `api-main.md` or `api-extended.md`, labels uncertainty instead of inventing signatures, and produces reviewable code/config text.
- If tests are not run because the generation pass is only updating design or audit tooling, state that explicitly. A full rebuild cannot be marked complete unless the forward tests are run or a user explicitly waives them.

## Validation

Before finishing generation:

- Re-read "Non-Negotiable Build Contract", "Generation Boundary", "Generation Workflow", and this "Validation" section.
- Confirm every reference linked from `SKILL.md` exists and every required reference from this design is linked or intentionally excluded with review rationale.
- Confirm every required reference satisfies the Reference Strategy gates: template coverage, line-depth target, actionable detail retention, source-family labeling, examples, traps/review checks, API notes, and follow-up lookup routing.
- Confirm `generation/review.md` contains the required completeness table, source coverage maps, actionable-detail retention notes, exact generation provenance, and status line.
- Confirm `generation/review.md` contains a required-concept coverage matrix with every concept ID from this design.
- Confirm every concept marked `PASS` has concrete runtime evidence in the referenced runtime file.
- Confirm no required concept is satisfied only by a generic checklist bullet or by a review-only claim.
- Confirm runtime usability: `SKILL.md` routes quickly, common workflows are near the top of references, and ordinary tasks do not require reading an entire long reference.
- Confirm source authority was respected: wiki/docs first, samples as examples only, and game API data for exact signatures.
- Confirm no generated output used old generated references or old `SKILL.md` as source.
- Confirm no deterministic script generated topical references, `api-main.md`, `SKILL.md`, or `generation/review.md`.
- Confirm `api-main.md`, `api-extended.md`, `common-task-recipes.md`, and `examples-patterns.md` meet their special coverage requirements.
- Confirm examples are additive, source-labeled, and do not replace official guidance, gotchas, or API notes.
- Confirm examples are concrete examples, not generic `Example Marker` or audit-marker placeholders.
- Confirm uncertain example APIs are marked `example-observed`, `generated-pattern-from-docs`, or `pseudocode` with verification notes.
- Confirm no reference contains line-count padding, repeated generic retention notes, `Operational Detail Retention`, `Expanded Source-Grounded Review Notes`, or equivalent meta-audit filler.
- Confirm references render as clean Markdown for GitHub review: no broken tables, flattened inline table dumps, malformed headings, raw HTML, raw navigation text, stale TOC entries, copied crawler sections, image placeholders, unfenced code blocks, mojibake, image-only wiki links, collapsed heading runs, or generic marker sections.
- Confirm `api-main.md` puts mandatory common signatures near the top and is not an alphabetical mini-dump with the important entries appended at the end.
- Confirm empty wiki pages are absent or flagged.
- Confirm `SKILL.md` includes grep/search guidance for `api-extended.md` and `api-main.md`, includes a route to `common-task-recipes.md`, and does not mention `raw/` paths.
- Confirm `agents/openai.yaml` exists or is intentionally skipped, and matches the generated `SKILL.md`.
- Run the coding-focused forward-test prompts or record an explicit user waiver in `generation/review.md`.
- Run `py -3 scripts\audit-references.py` and fix every reported failure before claiming completion.
- Run the available skill validation tool if present, then fix any reported metadata or structure issues. Record this separately from the design completeness audit.

Hard stop rules:

- If any required reference has `Status = FAIL`, the generation is not complete.
- If `generation/review.md` does not include the required audit table, the generation is not complete.
- If `generation/review.md` does not include source coverage maps and actionable-detail retention notes for each generated reference, the generation is not complete.
- If `generation/review.md` does not include the required-concept coverage matrix for every concept ID in this design, the generation is not complete.
- If any required concept has `Status = FAIL`, the generation is not complete.
- If any required concept marked `PASS` lacks runtime evidence in the generated reference, the generation is not complete.
- If a required concept is only mentioned in generic review checklist text and lacks workflow, example, API note, trap, or task guidance, the generation is not complete.
- If any source document assigned to a generated reference is only named but not coverage-reviewed, the generation is not complete.
- If runtime usability review fails for `SKILL.md` or any required reference, the generation is not complete.
- If any runtime reference contains filler sections, repeated generic retention bullets, or line-count padding, the generation is not complete.
- If any runtime reference contains mojibake, raw wiki image links, image placeholders, collapsed heading runs, raw navigation text, copied crawler sections, stale TOC entries, flattened inline table dumps, malformed tables, or generic audit-marker sections, the generation is not complete.
- If `api-main.md` buries mandatory common signatures after broad generated/low-priority entries, the generation is not complete.
- If `SKILL.md` or any runtime reference contains local `raw/` paths or tells the agent to open `raw/`, the generation is not complete.
- If `generation/review.md` does not list exact raw source provenance per reference, the generation is not complete.
- If `common-task-recipes.md` is missing any required recipe, the generation is not complete.
- If `examples-patterns.md` does not inventory every official sample mod, the generation is not complete.
- If a full rebuild lacks forward-test results or an explicit user waiver, the generation is not complete.
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
Select-String -Path references\*.md -Pattern 'Operational Detail Retention|Expanded Source-Grounded Review Notes|Retention note|Preserve documented workflow|Retain the official workflow step'
Select-String -Path references\*.md -Pattern '\[\]\(/wiki/File:|# .*###|## .*###|Example Marker|Audit Marker|Coverage Marker|â|Ã|ðŸ|�'
Select-String -Path references\*.md -Pattern '\[image omitted\]|Official Wiki Sources|High-Signal Doc Notes|Official Sample Sources|Relevant APIs|Headings:|Source family:|Show details|Copy |TODO:'
$runtimeRefs = Get-ChildItem references -File | Where-Object { $_.Name -ne 'api-extended.md' }
Select-String -Path $runtimeRefs.FullName -Pattern 'official sample corpus/|extracted game API/|markdown/Arma_Reforger_|addons_core\\scripts'
Select-String -Path generation\review.md -Pattern 'Required concept coverage matrix|OVR-|SCR-|LANG-|ECL-|NET-|RES-|WB-|SCN-|TER-|ASSET-|SRV-|EX-|REC-|API-'
Select-String -Path SKILL.md -Pattern 'common-task-recipes.md'
Select-String -Path references\api-main.md -Pattern 'Mandatory Common Signatures|IEntity|ScriptComponent|ResourceName|RplRpc|WorkbenchPlugin' | Select-Object -First 40
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
