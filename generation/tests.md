# Reforger Generation Tests And Review Contract

This document defines the manual/agent test suite for evaluating the current Reforger skill generation. It is generation-only. Do not use it as runtime skill input.

The purpose is to produce a current, objective review of the data, indexes, search tooling, references, and `SKILL.md`. Every run must overwrite `generation/review.md` from scratch with current results.

## Mandatory Piecewise Test Loop

Follow this loop exactly for every review run. The review is built incrementally. Do not wait until the end to write results.

1. Reset review context.
   - Treat prior `generation/review.md` content as stale.
   - Overwrite `generation/review.md` from scratch with the run metadata and empty section scaffolding.
   - Do not append historical notes unless they are rediscovered in the current run.
2. Inventory current state.
   - Record date/time, working directory, and `git status --short`.
   - Record whether `SKILL.md`, `references/`, `raw/game-data/`, `raw/game-data/manifest.json`, `raw/game-data/indexes/manifest.json`, and `generation/wiki-index/manifest.json` exist.
   - Record counts for references, wiki-index files, game-data index files, and raw game source files when present.
   - Write the inventory to `generation/review.md` before starting Category 1.
3. Before every category and every individual Category 9 coding test, re-read this `generation/tests.md` file.
   - Treat this file as the active contract for the next piece of work.
   - Do not rely on memory of the scoring rules or previous review runs.
   - Record in `generation/review.md` that the test contract was re-read for that category or coding test.
4. Run categories in order, one category at a time.
   - Run or inspect one category below.
   - For every test, capture the command or review action, expected result, actual result, score, pass/fail, and critique.
   - For real-world coding simulations, capture the prompt, selected references, query commands, examples/snippets opened, expected code shape, actual answer/code summary, generated code/test output excerpt, verified APIs, API/idiom provenance, residual risks, score, and critique.
   - After the category is complete, immediately update `generation/review.md` with that category's results, scores, critique, and any score caps.
   - Stop and review the written category before moving on; do not batch multiple categories into an unwritten mental summary.
5. Run Category 9 as separate task pieces, not as one bulk category.
   - Each `CD-*` coding simulation is its own piece.
   - Before each `CD-*`, re-read this file, then read the selected references in full, then run closer searches, then inspect examples/snippets, then generate output, then score.
   - Immediately write that `CD-*` result to `generation/review.md` before starting the next `CD-*`.
   - If a `CD-*` produces route-only, placeholder-only, comment-driven, or unverified code, apply the score cap immediately and record the cap reason next to that test.
6. Apply automatic-fail checks after each category and each `CD-*` coding test.
   - Stop early only when a critical failure makes later scores unreliable.
   - Still write `generation/review.md` with the failed status and the current evidence gathered.
7. Score each category.
   - Average tests within the category.
   - Mark critical tests explicitly.
   - For Category 9, maintain a running count of coding tests scoring `4+`, coding tests below `3`, and route-only/placeholder-only/comment-driven outputs.
8. Compute overall result.
   - Average all scored tests.
   - Apply critical-test and automatic-fail rules.
9. Write current conclusions.
   - Summarize what is strong, weak, missing, stale, noisy, or unsafe.
   - List ordered next fixes by impact on Codex usefulness.
10. Final review sanity check.
   - Confirm `generation/review.md` contains current data only.
   - Confirm it includes concrete paths, counts, commands, actual answers, scores, and critiques.
   - Confirm it does not include raw wiki dumps, raw source bodies, or copied large snippets.

Piece boundaries:

- Categories 1 through 8 are category pieces.
- Category 9 is split into `15` individual coding-test pieces, `CD-1` through `CD-15`.
- A review run has at least `23` write checkpoints: initial scaffold/inventory, Categories 1-8, each of the 15 `CD-*` tests, score summary, usefulness summary, and recommended fixes.
- If the run is interrupted, `generation/review.md` must still show completed pieces, the next pending piece, and whether the partial run is pass/fail/blocked so far.

## Scoring System

Score every test from `0` to `5`.

| Score | Meaning |
| --- | --- |
| `5` | Complete, useful, source-backed, bounded, current, and no recovery needed. |
| `4` | Good and useful with minor gaps that do not block Codex. |
| `3` | Usable but requires follow-up search, review, or manual recovery. |
| `2` | Weak, incomplete, noisy, or partially misleading. |
| `1` | Mostly failing; little useful signal remains. |
| `0` | Missing, misleading, unsafe, unverifiable, or impossible to score. |

Pass/fail rules:

- Overall pass requires average score `>= 4.0`.
- Every required category must average `>= 3.5`.
- Every critical test must score `>= 4`.
- A critical test score below `4` fails the run even if the average passes.
- A score of `0` in API truth, runtime boundary, or source availability fails the run.
- Category 9 real-world coding simulations must average `>= 4.0`.
- No Category 9 coding test may score below `3` for an overall pass.
- At least `10` of the `15` Category 9 coding tests must score `4` or higher.
- If `3` or more Category 9 coding tests are route-only, placeholder-only, or comment-driven, the run fails regardless of the numeric average.

Automatic failure conditions:

- Missing `SKILL.md`.
- Missing `references/`.
- Missing `raw/game-data/manifest.json`.
- Missing `raw/game-data/indexes/manifest.json`.
- `scripts/query-reforger-data.py` cannot run.
- `SKILL.md` does not route all references.
- `SKILL.md` routes runtime Codex to forbidden generation/wiki/sample/indexer/validator/human-log sources.
- API-sensitive guidance exists without requiring game-data query verification.
- Query output lacks source file/line grounding for exact API tests.
- Any real-world coding task invents a Reforger API that was not verified through game-data search.
- Any real-world coding task emits meaningful Reforger helper API calls without provenance and claims they are verified.
- Any real-world coding task skips relevant reference reading before API-sensitive code.
- Any real-world coding task modifies or proposes modifying skill/reference/tooling files without an explicit skill-maintenance prompt.
- Any real-world coding task claims score `5` without exact verified APIs/signatures, helper-call provenance, source-backed idiom evidence, and enough generated output for human review.

## Review Output: `generation/review.md`

Every test run must overwrite `generation/review.md` with these sections:

1. `# Reforger Generation Review`
2. `## Run Metadata`
   - date/time,
   - working directory,
   - command runner,
   - `git status --short`,
   - whether the run stopped early,
   - current piece/checkpoint status.
3. `## Data Status`
   - `raw/game-data/manifest.json` summary,
   - `raw/game-data/indexes/manifest.json` summary,
   - raw `.c` file count,
   - index artifact presence/counts,
   - wiki index artifact presence/counts,
   - reference count,
   - `SKILL.md` presence.
4. `## Script And Tooling Overview`
   - updater status,
   - indexer status,
   - query script status,
   - validator/usefulness script status,
   - known command failures.
5. `## Reference Inventory`
   - one row per reference,
   - path,
   - line count,
   - byte count,
   - role,
   - concise critique.
6. `## SKILL.md Audit`
   - line count,
   - frontmatter fields,
   - routing coverage,
   - allowed runtime sources,
   - forbidden runtime source scan,
   - action-loop and mandatory-rule critique.
7. `## Test Results`
   - category,
   - test ID,
   - piece/checkpoint ID,
   - whether `generation/tests.md` was re-read for this piece,
   - command or review action,
   - expected answer,
   - actual answer,
   - score,
   - pass/fail,
   - notes/critique.
   - for coding simulations: prompt, selected references, queries run, examples/snippets opened, expected code shape, actual answer/code summary, generated code/test output excerpt, verified APIs, API/idiom provenance, emitted API calls, evidence for each call, source-backed idioms used, unverified helper calls, residual risks, score cap applied if any, score, and critique.
8. `## Score Summary`
   - category averages,
   - critical-test statuses,
   - overall average,
   - pass/fail result,
   - automatic-fail reasons if any.
9. `## Usefulness Summary`
   - strongest parts,
   - weakest parts,
   - likely Codex failure modes,
   - whether the current generation is useful enough.
10. `## Recommended Next Fixes`
   - ordered by impact,
   - include target path/tool/reference where possible.

For piecewise runs, `generation/review.md` must also make progress visible:

- Add a `## Piecewise Progress` section or equivalent table.
- List every category and every `CD-*` coding test as `pending`, `in progress`, `complete`, `failed`, or `blocked`.
- Update the status after every completed piece.
- Record the next pending piece if the run stops early.
- Do not mark a piece complete until its command output/review action, score, critique, and review text have been written.

The review must include paths and concrete counts. It must not include raw wiki page dumps, raw source bodies, full JSONL records, or stale carryover from previous reviews.

## Category 1: Source And Data Status

Critical: yes.

| ID | Test | Action | Expected `5` Result |
| --- | --- | --- | --- |
| SD-1 | Working tree status | Run `git status --short` | Current changed/untracked files are recorded without judging unrelated work as test failure. |
| SD-2 | Raw game data manifest | Inspect `raw/game-data/manifest.json` | Manifest exists and includes source commit/ref data usable for staleness review. |
| SD-3 | Raw scripts count | Count `raw/game-data/scripts/**/*.c` | Count is recorded and is large enough to represent the Reforger script corpus. |
| SD-4 | Game index manifest | Inspect `raw/game-data/indexes/manifest.json` | Manifest exists and links indexes to the raw game-data commit/indexer version. |
| SD-5 | Wiki index status | Inspect `generation/wiki-index/manifest.json` if present | Counts and output artifacts are recorded for future reference quality review. |
| SD-6 | Reference set status | Count `references/*.md` | All expected runtime references are present and count is recorded. |

Scoring notes:

- Score `5` when data exists, counts are recorded, and freshness is clear.
- Score `3` when data exists but freshness cannot be determined.
- Score `0` for missing critical game-data or index manifests.

## Category 2: Game-Data Updater And Manifest

Critical: yes.

| ID | Test | Action | Expected `5` Result |
| --- | --- | --- | --- |
| GU-1 | Updater help | Run `py -3 scripts\update-reforger-data.py --help` | Help runs and includes `--check`, `--if-needed`, and `--force`. |
| GU-2 | Check mode | Run `py -3 scripts\update-reforger-data.py --check` | Exits cleanly with current/stale status and does not rewrite raw data. |
| GU-3 | Manifest source fields | Inspect manifest JSON | Source repo/ref/commit and update metadata are recorded. |
| GU-4 | Raw folder cleanup contract | Inspect `raw/game-data` | `.git`, `README.md`, and `LICENSE` are not present inside `raw/game-data`. |
| GU-5 | Runtime command match | Compare `SKILL.md` command | Runtime skill only documents `py -3 scripts\update-reforger-data.py --if-needed` for game-data generation. |

Scoring notes:

- Score `0` if updater is missing or cannot show help.
- Score `0` if runtime skill routes to any non-updater refresh path.

## Category 3: Game-Data Index And Search Usefulness

Critical: yes.

| ID | Test | Action | Expected `5` Result |
| --- | --- | --- | --- |
| GS-1 | Query help | Run `py -3 scripts\query-reforger-data.py --help` | Commands include `symbol`, `method`, `attribute`, `inherits`, `examples`, `files`, `snippet`, and `lookup`. |
| GS-2 | Exact symbol | Run `py -3 scripts\query-reforger-data.py symbol ResourceName --exact --json` | First result is `ResourceName`, includes file/line, and is generated API truth. |
| GS-3 | Exact class | Run `py -3 scripts\query-reforger-data.py symbol ScriptComponent --kind class --exact --json` | First result is the class with source reference. |
| GS-4 | Exact method | Run `py -3 scripts\query-reforger-data.py method IEntity FindComponent --exact --json` | Returns exact owner/name/signature with file/line. |
| GS-5 | Attributes | Run exact `RplProp` and `RplRpc` attribute searches | Both attributes are found with source references. |
| GS-6 | Inheritance | Run `inherits ScriptedUserAction` and component inheritance searches | Derived/base relationships are source-grounded. |
| GS-7 | Example topics | Run examples for replication, user-action, resource-loading, workbench-plugin | Top results are relevant, bounded, and include source ranges. |
| GS-8 | Subtopic precision | Run examples with subtopics such as `spawn-prefab`, `rpc`, `character-inventory`, `compartment`, `hud`, `anim-graph` | Results match the requested subtopic, not just generic token matches. |
| GS-9 | Snippet safety | Run a known valid snippet and one rejected outside path | Valid snippet is bounded; outside path is rejected. |
| GS-10 | Validator | Run `py -3 scripts\tests\validate-reforger-search.py` | Passes or failures are recorded with exact failure messages. |
| GS-11 | Usefulness benchmark | Run `py -3 scripts\tests\measure-reforger-search-usefulness.py` | Report scores realistic Codex tasks and meets its threshold. |

Scoring notes:

- Score `5` when query output is exact, bounded, source-backed, and useful without recovery.
- Score `2` or less when top results are noisy enough to mislead Codex.
- Score `0` when exact API lookup lacks file/line grounding.

## Category 4: Wiki Index And Source Coverage Signals

Critical: no, but required for reference-generation confidence.

| ID | Test | Action | Expected `5` Result |
| --- | --- | --- | --- |
| WI-1 | Wiki index manifest | Inspect `generation/wiki-index/manifest.json` | Manifest exists and records page/section/chunk/table/code/procedure/admonition/media/link counts. |
| WI-2 | Page coverage | Inspect `generation/wiki-index/pages.jsonl` | High-value pages are represented with titles and official URLs. |
| WI-3 | Section preservation | Inspect `sections.jsonl` and `chunks.jsonl` counts | Sections preserve full content and chunks are bounded helpers. |
| WI-4 | Structured records | Inspect tables/code/procedures/admonitions/media/links artifacts | Structured wiki evidence exists and is countable. |
| WI-5 | Topic routing | Inspect `topics.json` or page topic fields | Scenario Framework, Server Config, Multiplayer Scripting, Workbench Plugin, weapon, terrain, animation, audio, UI, and AI topics route clearly. |
| WI-6 | Noisy routing review | Check quality report if present | Short terms such as AI/UI are not broad false-positive sources. |

Scoring notes:

- Score `5` when wiki index gives complete generation evidence.
- Score `3` when wiki index exists but topic routing is noisy.
- Score `0` only if wiki-index data needed for reference review is missing or unusable.

## Category 5: Runtime Reference Coverage And Quality

Critical: yes.

| ID | Test | Action | Expected `5` Result |
| --- | --- | --- | --- |
| RF-1 | Reference inventory | For each `references/*.md`, record path, line count, byte count, headings | Every reference is present, non-empty, and has useful structure. |
| RF-2 | Required headings | Check each reference for builder-required headings | All references include the expected operational sections or justified utility-reference variants. |
| RF-3 | Source richness | Review representative domain references | References preserve wiki-derived workflows, warnings, tables/fields/procedures, and official links. |
| RF-4 | API routing | Search references for query commands/API lookup keys | API-sensitive guidance routes to `scripts/query-reforger-data.py` and avoids broad API dumps. |
| RF-5 | Split boundaries | Review adjacent references for duplication | Major categories are owned once and cross-linked rather than duplicated. |
| RF-6 | Runtime cleanliness | Scan references for raw dumps/local absolute paths | No raw wiki dumps, copied source bodies, local absolute paths, or generation-only instructions. |
| RF-7 | Utility references | Review API lookup, examples, and task recipes | Utility references route to source-owning references and search commands without owning broad workflow detail. |

Scoring notes:

- Score `5` when a reference can guide Codex without loading unrelated files.
- Score `3` when useful but missing concrete workflow detail or critique.
- Score `0` when a reference is absent, shallow, misleading, or violates runtime boundaries.

## Category 6: `SKILL.md` Runtime-Boundary Compliance

Critical: yes.

| ID | Test | Action | Expected `5` Result |
| --- | --- | --- | --- |
| SK-1 | Frontmatter | Inspect `SKILL.md` frontmatter | Only `name` and `description` exist. |
| SK-2 | Line count | Count lines | Concise enough to be a router, not a reference dump. |
| SK-3 | Routing coverage | Confirm every `references/*.md` appears | All references are routed. |
| SK-4 | Mandatory behavior | Inspect rules/action loop | Requires full reference reading, API search for all meaningful emitted APIs, example/snippet inspection, source-backed idioms, and verification. |
| SK-5 | Search guide | Inspect query commands | Documents all query commands and says commands are starting points. |
| SK-6 | Game-data command | Inspect game-data section | Only raw game-data update command is documented. |
| SK-7 | Forbidden source scan | Search forbidden terms | No runtime routing to generation, wiki cache/indexes, samples, refresh scripts, indexers, validators, or human logs. |
| SK-8 | Skill self-protection | Inspect modification rule | Explicitly forbids modifying skill/reference/tooling files unless asked and confirmed. |
| SK-9 | Domain grounding | Inspect grounding/top mistakes | Provides enough Reforger/Enfusion context to prevent Unity/Unreal/C#/Arma 3 assumptions without bloating. |

Scoring notes:

- Score `0` if `SKILL.md` routes runtime Codex to forbidden sources.
- Score `0` if it allows API guessing.
- Score `5` when it is strict, compact, and aligned with the architecture.

## Category 7: Cross-Source Codex Task Usefulness

Critical: yes.

For each task, score whether the skill plus references plus query tooling let Codex answer without guessing, broad dumps, or stale source assumptions.

| ID | Task | Required Evidence For `5` |
| --- | --- | --- |
| CT-1 | Make a script component | Routes to script patterns, lifecycle, API lookup; verifies `ScriptComponent`/`ScriptComponentClass`; finds examples. |
| CT-2 | Make a user action | Routes to script patterns and examples; verifies `ScriptedUserAction` and methods; opens relevant source example. |
| CT-3 | Make a replicated component | Routes to replication and lifecycle; verifies `RplComponent`, `RplProp`, `RplRpc`; includes multiplayer verification. |
| CT-4 | Spawn/load a prefab resource | Routes to prefabs/resources; verifies `ResourceName`, `Resource.Load`, spawn APIs; finds source examples. |
| CT-5 | Create Workbench plugin | Routes to Workbench plugins; verifies `WorkbenchPlugin` and attributes; finds plugin examples. |
| CT-6 | Build Scenario Framework content | Routes to Scenario Framework; finds `SCR_ScenarioFramework` source; includes Workbench/runtime verification. |
| CT-7 | Configure Game Master/faction/task/game mode | Routes to Game Master reference; finds faction/task/game-mode source examples; includes runtime verification. |
| CT-8 | Configure server | Routes to server reference; keeps replication semantics separate; records config/startup validation. |
| CT-9 | Import asset/prop | Routes to asset reference; includes Workbench/resource validation and no script-only bias. |
| CT-10 | Create weapon behavior | Routes to weapon reference; finds weapon/component/magazine examples; verifies APIs. |
| CT-11 | Use gear/inventory/arsenal | Routes to gear reference; verifies inventory/catalog symbols and examples. |
| CT-12 | Configure vehicle compartment | Routes to vehicle reference; verifies compartment manager/controller examples. |
| CT-13 | Work with animation graph | Routes to animation reference; finds animation examples and API routes. |
| CT-14 | Play sound event | Routes to audio reference; verifies sound event/component examples. |
| CT-15 | Create HUD/widget/UI | Routes to UI reference; verifies widget/layout APIs and examples. |
| CT-16 | Author AI behavior | Routes to AI reference; separates navmesh/UI ownership; finds AI behavior/debug sources. |
| CT-17 | Terrain/world/navmesh task | Routes to terrain/world references with correct split; validates editor/runtime requirements. |
| CT-18 | Unknown made-up task | Does not invent a confident route; recommends refinement/search and closest references only. |

Scoring notes:

- Score `5` when the route, query commands, examples, and verification are all clear.
- Score `3` when Codex can recover with additional search.
- Score `0` when a task encourages guessing, wrong reference routing, or unrelated confident fallback.

## Category 8: Examples And Snippet Grounding

Critical: yes.

| ID | Test | Action | Expected `5` Result |
| --- | --- | --- | --- |
| EX-1 | Example family breadth | Query examples for component, replication, resources, Workbench, scenario, game-mode, weapon, inventory, vehicle, animation, audio, UI, AI | Each family returns relevant source-backed records or clear caveats. |
| EX-2 | Example precision | Query high-value subtopics | Subtopic results are materially better than broad topic results. |
| EX-3 | Source snippet usefulness | Open snippets from top example results | Snippets begin near relevant implementation, not just file headers. |
| EX-4 | Example as guide | Inspect references and skill wording | Examples are framed as implementation patterns, not signature authority. |
| EX-5 | No broad source dumps | Inspect references/review output | No full raw source bodies are copied into runtime or review docs. |

Scoring notes:

- Score `5` when examples reduce implementation uncertainty without bloating context.
- Score `2` or lower when examples are noisy, generic, or unsafely treated as truth.

## Category 9: Real-World Reforger Coding Task Simulations

Critical: yes.

These tests evaluate whether the current skill architecture can guide Codex through realistic Arma Reforger coding work. They are dry-run coding simulations unless the reviewer intentionally runs them in a disposable fixture. Do not edit real project files for this category unless the test harness explicitly creates a temporary sandbox.

For each test:

1. Start from the prompt only.
2. Route using `SKILL.md`.
3. Read the selected references in full.
4. Run closer game-data searches instead of relying only on canned commands.
5. Open at least one relevant source example or bounded snippet when code patterns matter.
6. Produce a minimal code/config answer or patch plan in the review.
7. Include the generated code/test output excerpt needed for human review.
8. Score the answer against the expected code shape, API evidence, and API/idiom provenance.
9. Apply the coding simulation quality gates before assigning the final score.

Coding task scoring:

- `5`: Correct route, relevant references read, exact APIs/signatures verified for every meaningful emitted API call, source-backed idioms used, source examples/snippets inspected, generated Reforger-specific code/config/review output performs the requested behavior shape, and residual Workbench/runtime/server verification is clear.
- `4`: Correct and useful with one minor gap only. Missing functionality, missing exact API signatures, missing helper-call provenance, missing source-backed idiom evidence, or missing snippet/example inspection is not a minor gap.
- `3`: Useful route or incomplete draft, but the generated output needs manual API repair, more source inspection, or additional implementation before it could be applied.
- `2`: Weak placeholder, mostly planning, generic pseudocode, comment-driven output, or likely Reforger mistakes.
- `1`: Mostly generic engine/code answer with little source grounding.
- `0`: Hallucinates APIs, ignores references/search, uses wrong engine assumptions, or edits forbidden skill files.

Coding simulation quality gates:

- Route-only output max score is `3`, even if the route is correct.
- Comment-placeholder code max score is `2`. If the main behavior is a comment plus `Print()`, the test is placeholder-only.
- Generic pseudocode that does not perform the requested behavior max score is `2`.
- Code without verified exact API signatures max score is `3`.
- Code without at least one opened relevant example/snippet max score is `3`.
- Code using invented, unverified, or guessed Reforger API names scores `0`.
- Code with any meaningful emitted helper API call that lacks provenance max score is `3`.
- Code with verified APIs but a non-source-backed idiom, when a closer idiom is visible in opened snippets or docs, max score is `4`.
- Code that composes generic APIs where source evidence shows a direct purpose-built API cannot score `5` unless the composition is also source-backed and justified.
- A bare data class, empty subclass, or structure-only snippet max score is `3` unless it also demonstrates the requested parse/load/spawn/action/serialization behavior.
- A patch plan may score `4` or `5` only when code should not be generated yet because the task is primarily editor/data/config driven, and the plan includes concrete file/class/method/config routes, exact source evidence, and a reason code is not the right immediate artifact.
- Pure "read this reference, find a class, validate later" output max score is `3`.
- A coding test claiming score `5` must list exact verified APIs/signatures for task APIs and helper APIs, the snippet/example opened with file and line, source-backed idioms used, generated output that performs the task shape, and residual verification notes.

API/Idiom Provenance Required:

- Every coding test must list each meaningful emitted Reforger API call in the generated code or patch review.
- Each emitted API call must include evidence from a query command result, exact signature, or opened snippet file/line.
- Meaningful emitted APIs include helper calls such as logging, formatting, component lookup, resource loading, spawning, widget updates, sound calls, RPC calls, JSON helpers, config helpers, and similar support calls.
- Language syntax and local helper methods do not need query evidence unless they call Reforger APIs.
- Source snippets/examples must be used to identify common idioms. Prefer direct source-backed APIs and idioms over composing generic calls unless the composition is also source-backed and justified.

Failure examples that must be downgraded:

- A bare JSON/config subclass such as `class TAG_ConfigPayload : JsonApiStruct { string Name; int Count; }` without parse/serialize/config usage is incomplete and cannot score above `3`.
- A Scenario Framework answer that only says "read the reference, find `SCR_ScenarioFrameworkTask`, validate in runtime" is route-only and cannot score above `3`.
- A hint, sound, UI, or gameplay function whose main behavior is a comment saying to open the real API later plus `Print()` is placeholder-only and cannot score above `2`.
- A generated code body that verifies only the base class or lifecycle callback, while using additional Reforger helper calls without evidence, cannot score above `3`.
- A code body that uses logging, formatting, resource, UI, component, sound, RPC, JSON, or config helper calls without verifying their source-backed usage cannot score `5`.
- A code body that composes two generic APIs when opened snippets/docs show a direct source-backed API cannot score `5` unless that composition is also source-backed and justified.
- A component answer that avoids the required lifecycle callback because the callback was not verified cannot score above `3`.
- A domain answer for weapons, vehicles, animation, audio, AI, UI, or Scenario Framework that gives only ownership boundaries and next searches, with no concrete code/config/review artifact, cannot score above `3`.

| ID | Real-World Prompt | Required References | Required Query Evidence | Expected Code/Answer Shape For `5` |
| --- | --- | --- | --- | --- |
| CD-1 | "Create a minimal script component that logs when attached and can be added in Workbench." | `script-events-actions-and-patterns.md`, `entities-components-and-lifecycle.md`, `api-lookup-and-common-symbols.md` | Verify `ScriptComponent`, `ScriptComponentClass`, lifecycle callbacks, and inspect a script-component example. | Includes paired component/class pattern when required by API, correct lifecycle callback names/signatures from search, no Unity-style methods, Workbench/prefab validation notes. If lifecycle callback names/signatures are not verified, max score is `3`. |
| CD-2 | "Create a user action that only shows when the player has permission and performs a small interaction." | `script-events-actions-and-patterns.md`, `entities-components-and-lifecycle.md`, possibly `multiplayer-replication-and-authority.md` | Verify `ScriptedUserAction`, visibility/perform methods, and inspect a handwritten user-action source file. | Minimal user-action class with correct override signatures, condition methods, target/user handling, and runtime validation note. |
| CD-3 | "Make a replicated component with one replicated boolean and one RPC from owner to authority." | `multiplayer-replication-and-authority.md`, `entities-components-and-lifecycle.md`, `script-events-actions-and-patterns.md` | Verify `RplComponent`, `BaseRplComponent`, `RplProp`, `RplRpc`, authority/proxy checks, and inspect `RplDocs.c` or `RplTestComponent`. | Code separates authority/proxy/owner, annotates replicated state/RPC correctly, avoids client-to-client assumptions, includes dedicated-server/JIP verification. |
| CD-4 | "Spawn a prefab from a `ResourceName` property on a component." | `prefabs-configs-containers-and-catalogs.md`, `entities-components-and-lifecycle.md`, `script-events-actions-and-patterns.md` | Verify `ResourceName`, `Resource.Load`, spawn API/entity spawn params, and inspect a spawn-prefab example. | Minimal component property/resource field, load/spawn flow with null/error guards, no broad manager, Workbench resource-picker/prefab validation. |
| CD-5 | "Load a UI layout resource and create/show a simple HUD widget." | `ui-layouts-dialogs-and-menus.md`, `resource-manager-file-types-and-editors.md`, `api-lookup-and-common-symbols.md` | Verify widget/layout/resource APIs and inspect HUD/layout examples. | Uses current UI/layout APIs, keeps layout resource separate from script, includes cleanup/ownership and UI runtime verification. |
| CD-6 | "Create a Workbench plugin command with a menu button and basic run handler." | `workbench-plugins-and-editor-tools.md`, `enfusion-language-and-script-editor.md`, `api-lookup-and-common-symbols.md` | Verify `WorkbenchPlugin`, `WorkbenchPluginAttribute`, plugin run/config methods, and inspect Workbench plugin examples. | Minimal plugin class/attribute using exact signatures, no runtime-game assumptions, includes Workbench validation. |
| CD-7 | "Add a weapon-related script that reacts to magazine or ammo state." | `weapons-prefabs-attachments-and-firearms.md`, `script-events-actions-and-patterns.md`, `api-lookup-and-common-symbols.md` | Verify weapon, muzzle, magazine component APIs and inspect weapon/magazine examples. | Uses real weapon/magazine component names, keeps prefab/config responsibilities separate, avoids invented ammo APIs, includes weapon prefab/runtime validation. |
| CD-8 | "Add a vehicle compartment interaction or check whether a character is in a compartment." | `vehicles-creation-simulation-and-compartments.md`, `entities-components-and-lifecycle.md`, `api-lookup-and-common-symbols.md` | Verify compartment manager/controller APIs and inspect vehicle compartment examples. | Correct component lookup/use, compartment-specific APIs verified, no generic Unity vehicle assumptions, includes in-game vehicle validation. |
| CD-9 | "Play a sound event from an entity component." | `audio-editor-signals-and-sound-systems.md`, `entities-components-and-lifecycle.md`, `api-lookup-and-common-symbols.md` | Verify sound component/event APIs and inspect sound-event examples. | Minimal code uses current sound API/resource flow, separates audio editor setup from script, includes audio-resource/runtime validation. Placeholder `Print()` output or comments that defer the real sound call max score `2`. |
| CD-10 | "Trigger an animation command or find the right animation component route for a character." | `animation-graphs-weapon-animation-and-export.md`, `entities-components-and-lifecycle.md`, `api-lookup-and-common-symbols.md` | Verify animation component/command APIs and inspect animation graph examples. | Provides exact API route or states uncertainty with next search, avoids generic animator assumptions, includes Animation Editor/runtime validation. |
| CD-11 | "Find or implement an AI behavior hook for a scripted AI task." | `ai-behavior-commanding-and-debug.md`, `script-events-actions-and-patterns.md`, `api-lookup-and-common-symbols.md` | Avoid broad `examples ai` alone; verify `AITask`, `AIWaypoint`, `SCR_AI`, or behavior APIs and inspect targeted source snippets. | Uses targeted AI/behavior source evidence, separates navmesh/UI ownership, includes AI debug/runtime validation. |
| CD-12 | "Create a notification or hint from gameplay script." | `game-master-factions-tasks-and-modes.md`, `script-events-actions-and-patterns.md`, `api-lookup-and-common-symbols.md` | Verify notification/hint APIs and inspect examples. If `lookup` is unmatched, targeted `files SCR_Hint...` or `files SCR_Notification...` searches must recover exact source evidence. | Minimal script route with exact API names, keeps config/data setup separate, includes in-game validation. Unmatched lookup plus targeted file route is max `3` unless exact call signatures are verified from snippet evidence. |
| CD-13 | "Add a Scenario Framework task/action route and find the right class to extend." | `scenario-framework.md`, `api-lookup-and-common-symbols.md`, possibly `game-master-factions-tasks-and-modes.md` | Prefer `files SCR_ScenarioFramework...` over broad examples; verify task/layer/action classes and inspect snippets. | Correct Scenario Framework class/source route, no guessed base class, includes Workbench/runtime Scenario Framework validation. Route-only output max score is `3`; score `4` or `5` requires a concrete class/action/task extension route with source-backed class names and snippet evidence. |
| CD-14 | "Write a small JSON/config object helper using Enfusion language rules." | `enfusion-language-and-script-editor.md`, `prefabs-configs-containers-and-catalogs.md`, `api-lookup-and-common-symbols.md` | Verify `JsonApiStruct`, `BaseContainer`, or config APIs as applicable and inspect examples. | Code respects Enforce syntax/value/ref behavior, uses verified config/JSON APIs, and includes serialization/config validation. A bare `JsonApiStruct` subclass without parse/serialize/config access usage max score is `3`. |
| CD-15 | "Review a proposed Reforger script patch for API mistakes." | Relevant topical reference by patch domain, `api-lookup-and-common-symbols.md` | Query every uncertain class/method/attribute and inspect examples when behavior is unclear. | Review findings lead with concrete API/source issues, no style-only noise, identifies missing Workbench/runtime/server validation. |

Required review fields for each coding test:

- Prompt.
- Piece ID.
- Confirmation that `generation/tests.md` was re-read immediately before this coding test.
- References selected and whether they were read in full.
- Query commands run.
- Source examples/snippets opened.
- Expected code shape.
- Actual answer/code summary.
- Generated code/test output excerpt.
- Verified APIs.
- API/Idiom Provenance.
- Emitted API Calls.
- Evidence For Each Call.
- Source-Backed Idioms Used.
- Unverified Helper Calls.
- Unverified or residual risks.
- Score cap applied, if any, and why.
- Score and pass/fail.

Generated code/test output rules:

- Include enough of the proposed code, patch, review findings, or command output for a human to judge quality without rerunning the test.
- Prefer compact fenced code blocks for generated code. Keep each excerpt focused on the relevant class, method, config fragment, or review finding.
- For dry-run coding simulations, include the proposed code shape even if it is not written to disk.
- For patch-review simulations, include the reviewed risky snippet or a minimal representative snippet plus the finding.
- For command-driven tests, include the important output lines, not full JSON payloads.
- Do not include full raw game source bodies, full wiki sections, full JSONL records, or unrelated boilerplate.
- If the answer is intentionally a patch plan rather than code, include pseudocode or a concrete file/method outline and explain why code should not be generated yet.
- A coding test cannot score `5` unless the review includes enough generated output for a human to assess correctness.
- Score at most `3` when the route and API evidence are good but generated output is missing or too vague for human review.

## Recommended Commands

Use these commands during the review when available:

```powershell
git status --short
py -3 scripts\update-reforger-data.py --check
py -3 scripts\query-reforger-data.py --help
py -3 scripts\tests\validate-reforger-search.py
py -3 scripts\tests\measure-reforger-search-usefulness.py
py -3 scripts\query-reforger-data.py symbol ResourceName --exact --json
py -3 scripts\query-reforger-data.py method IEntity FindComponent --exact --json
py -3 scripts\query-reforger-data.py attribute RplProp --exact --json
py -3 scripts\query-reforger-data.py lookup "make a replicated component" --json
py -3 scripts\query-reforger-data.py lookup "unknown made-up task" --json
```

Use targeted searches beyond this list whenever a task needs closer context. Record those extra commands in `generation/review.md`.

## Review Quality Bar

A review is useful only if a human can answer these questions from `generation/review.md`:

- What data exists right now, and what is stale or missing?
- Are the indexes/search tools usable for exact API lookup?
- Are references complete enough to guide Codex without wiki access?
- Does `SKILL.md` enforce the architecture?
- Which realistic Reforger tasks pass or fail?
- Can Codex produce source-grounded Reforger code for realistic tasks without guessing APIs?
- Can Codex verify helper calls and idioms in generated code, not only the primary task API?
- What should be fixed next, in priority order?

If the review cannot answer those questions with current evidence, the test run itself fails regardless of the numeric score.
