# Reforger Generation Review

## Run Metadata

- Run date/time: `2026-07-08T13:01:34.7148556-04:00`
- Working directory: `C:\Users\Gray\Documents\VS\Reforger-Codex-Agent-Skill`
- Command runner: Codex via PowerShell
- Stopped early: no
- Current piece/checkpoint status: all categories complete, final score summary written
- `generation/tests.md` was read before starting the run: yes

Git status at run start:

```text
 M generation/design.md
 M generation/indexer-game-data.md
 M generation/searcher-game-data.md
 M generation/tooling-game-data-lookup.md
 D scripts/build-reforger-extended-api-reference.py
 M scripts/index-reforger-data.py
 M scripts/query-reforger-data.py
 M scripts/update-reforger-wiki-docs.py
 D scripts/validate-reforger-search.py
?? SKILL.md
?? generation/reference-builder.md
?? generation/refresh-reforger-sources.md
?? generation/search-exports/20260708T021537Z-search-usefulness.md
?? generation/search-exports/20260708T024412Z-search-usefulness.md
?? generation/search-exports/20260708T160857Z-search-usefulness.md
?? generation/search-exports/20260708T162014Z-search-usefulness.md
?? generation/search-exports/20260708T164226Z-search-usefulness.md
?? generation/tests.md
?? generation/wiki-docs-indexing.md
?? generation/wiki-index/
?? references/
?? scripts/index-reforger-wiki-docs.py
?? scripts/refresh-reforger-sources.py
?? scripts/tests/
```

## Piecewise Progress

| Piece | Status | Score | Notes |
| --- | --- | ---: | --- |
| Inventory scaffold | complete | n/a | Initial review file overwritten from scratch. |
| Category 1: Source And Data Status | complete | 5.00 | `generation/tests.md` re-read; all required source/data artifacts present. |
| Category 2: Game-Data Updater And Manifest | complete | 5.00 | `generation/tests.md` re-read; updater/check/manifest/cleanup contract passed. |
| Category 3: Game-Data Index And Search Usefulness | complete | 5.00 | `generation/tests.md` re-read; exact API, examples, snippets, validator, and benchmark passed. |
| Category 4: Wiki Index And Source Coverage Signals | complete | 4.83 | `generation/tests.md` re-read; preservation/structure strong, related-topic routing still broad. |
| Category 5: Runtime Reference Coverage And Quality | complete | 4.86 | `generation/tests.md` re-read; all references structured and clean, utility refs route correctly. |
| Category 6: `SKILL.md` Runtime-Boundary Compliance | complete | 5.00 | `generation/tests.md` re-read; runtime boundary, routing, commands, and mandatory rules passed. |
| Category 7: Cross-Source Codex Task Usefulness | complete | 4.72 | `generation/tests.md` re-read; core task routing is strong, broad/editor-heavy tasks still require refinement. |
| Category 8: Examples And Snippet Grounding | complete | 4.80 | `generation/tests.md` re-read; examples/snippets are useful, with known broad-topic noise. |
| CD-1 | complete | 5 | Verified `OnPostInit(IEntity owner)` and opened a real script-component snippet. |
| CD-2 | complete | 5 | Verified user-action base/method signatures and opened a handwritten example. |
| CD-3 | complete | 5 | Verified replication APIs and opened `RplTestComponent.c` plus `RplDocs.c`. |
| CD-4 | complete | 5 | Verified resource/spawn APIs and opened a source spawn flow. |
| CD-5 | complete | 5 | Verified layout/widget APIs and opened HUD widget source. |
| CD-6 | complete | 5 | Verified Workbench plugin API and opened real plugin snippets. |
| CD-7 | complete | 4 | Verified magazine APIs and examples; no exact magazine-state event callback selected. |
| CD-8 | complete | 4 | Verified compartment manager/slot APIs; exact occupant getter was not found. |
| CD-9 | complete | 5 | Verified `SoundComponent.SoundEvent` and opened sound-event examples. |
| CD-10 | complete | 4 | Verified animation command route; graph/table integration remains task-specific. |
| CD-11 | complete | 5 | Verified targeted AI task/waypoint source and avoided broad AI-only evidence. |
| CD-12 | complete | 5.00 | Hint/notification search recovered from unmatched lookup through targeted file/method queries. |
| CD-13 | complete | 5.00 | Scenario Framework action extension route verified with exact base class/method snippets. |
| CD-14 | complete | 5.00 | JsonApiStruct helper verified with parse/pack APIs and source examples. |
| CD-15 | complete | 5.00 | Patch review found concrete API mistakes and verified replacement routes. |
| Score Summary | complete | 4.78 | Overall category average passes. |
| Usefulness Summary | complete | n/a | Current generation is useful enough, with targeted improvement areas. |
| Recommended Next Fixes | complete | n/a | Fixes ordered by impact below. |

## Data Status

| Item | State |
| --- | --- |
| `SKILL.md` | present |
| `references/` | present |
| `raw/game-data/` | present |
| `raw/game-data/manifest.json` | present |
| `raw/game-data/indexes/manifest.json` | present |
| `generation/wiki-index/manifest.json` | present |
| Runtime references | `26` |
| Wiki index files | `13` |
| Game-data index files | `5` |
| Raw game source `.c` files | `6495` |

Raw game-data manifest:

```text
generatedAt: 2026-07-08T00:46:48.639878+00:00
repo: https://github.com/BohemiaInteractive/Arma-Reforger-Script-Diff.git
ref: main
commit: 2735631ce1400eaf9f1761c66cdee10c46921d37
sparsePath: scripts
checkoutArtifactsRemoved: .git, README.md, LICENSE
```

Game-data index manifest:

```text
indexer: index-reforger-data.py v3 config v3
commit: 2735631ce1400eaf9f1761c66cdee10c46921d37
outputs: symbols=85478, files=6495, examples=13957, inheritance=7572
```

Wiki index manifest:

```text
generatedAt: 2026-07-08T03:33:08+00:00
pages=310, rawAliases=316, sections=5402, chunks=5859
tables=710, codeBlocks=308, procedures=461, admonitions=1707
media=1219, links=8358, taxonomyCategories=48, taxonomyFamilies=148, topics=20
```

## Script And Tooling Overview

| Tool | Status | Notes |
| --- | --- | --- |
| `scripts/update-reforger-data.py` | pass | Help/check work; local raw data is up to date. |
| `scripts/index-reforger-data.py` | pass by manifest/search | Index manifest present; query outputs are source-grounded. |
| `scripts/query-reforger-data.py` | pass | Help includes all expected commands; exact API and examples are bounded. |
| `scripts/tests/validate-reforger-search.py` | pass | All search quality checks passed. |
| `scripts/tests/measure-reforger-search-usefulness.py` | pass | Average `14.00/14`, useful cases `13/13`; produced current human report `generation/search-exports/20260708T170406Z-search-usefulness.md`. |
| Known command failures | expected | Outside-path snippet command failed as intended with path rejection. |

## Reference Inventory

| Path | Lines | Bytes | Missing required headings | Query command refs | Critique |
| --- | ---: | ---: | ---: | ---: | --- |
| `references/ai-behavior-commanding-and-debug.md` | 471 | 33354 | 0 | 39 | Strong AI/behavior routing; broad AI search caveats remain important. |
| `references/animation-graphs-weapon-animation-and-export.md` | 684 | 47113 | 0 | 23 | Dense animation workflow coverage. |
| `references/api-lookup-and-common-symbols.md` | 513 | 25729 | 0 | 72 | Strong lookup utility; owns no workflow source. |
| `references/asset-import-models-materials-and-props.md` | 688 | 46774 | 0 | 30 | Strong asset pipeline coverage. |
| `references/audio-editor-signals-and-sound-systems.md` | 612 | 40920 | 0 | 24 | Strong audio workflow coverage. |
| `references/character-gear-inventory-and-arsenal.md` | 446 | 36713 | 0 | 21 | Focused gear/inventory reference. |
| `references/common-task-recipes.md` | 317 | 21768 | 0 | 48 | Good task router; intentionally not a source owner. |
| `references/diagnostics-testing-and-performance.md` | 618 | 30037 | 0 | 17 | Useful validation/performance reference. |
| `references/enfusion-language-and-script-editor.md` | 728 | 45411 | 0 | 33 | Dense language/editor coverage. |
| `references/entities-components-and-lifecycle.md` | 450 | 33990 | 0 | 22 | Clear lifecycle ownership. |
| `references/examples-and-sample-patterns.md` | 422 | 28106 | 0 | 53 | Good example router; no copied sample bodies found. |
| `references/game-master-factions-tasks-and-modes.md` | 796 | 45677 | 0 | 24 | Very broad but still source-dense. |
| `references/mod-projects-addons-workshop.md` | 617 | 41679 | 0 | 22 | Good addon/project/publishing coverage. |
| `references/multiplayer-replication-and-authority.md` | 533 | 23883 | 0 | 16 | Strong replication warnings. |
| `references/prefabs-configs-containers-and-catalogs.md` | 515 | 40847 | 0 | 21 | Strong prefab/config modeling coverage. |
| `references/resource-manager-file-types-and-editors.md` | 519 | 50598 | 0 | 19 | Very wiki-rich Resource Manager/editor coverage. |
| `references/scenario-framework.md` | 786 | 40120 | 0 | 19 | Dense Scenario Framework owner. |
| `references/script-events-actions-and-patterns.md` | 577 | 35851 | 0 | 33 | Strong scripting/user-action pattern reference. |
| `references/server-hosting-startup-and-runtime.md` | 706 | 35079 | 0 | 14 | Strong server/config coverage. |
| `references/start-here-source-authority.md` | 376 | 26484 | 0 | 18 | Good orientation/source hierarchy. |
| `references/terrain-creation-and-world-setup.md` | 407 | 31518 | 0 | 21 | Good terrain foundation owner. |
| `references/ui-layouts-dialogs-and-menus.md` | 521 | 30042 | 0 | 26 | Good UI/layout route. |
| `references/vehicles-creation-simulation-and-compartments.md` | 536 | 38585 | 0 | 22 | Strong vehicle setup coverage. |
| `references/weapons-prefabs-attachments-and-firearms.md` | 547 | 46895 | 0 | 32 | Strong weapon workflow coverage. |
| `references/workbench-plugins-and-editor-tools.md` | 611 | 32527 | 0 | 19 | Strong Workbench plugin reference. |
| `references/world-editor-tools-generators-and-navmesh.md` | 585 | 47445 | 0 | 39 | Strong world editor/navmesh coverage. |

## SKILL.md Audit

| Check | Result | Notes |
| --- | --- | --- |
| Frontmatter | pass | Only `name` and `description` fields. |
| Line count | pass | `126` lines; compact router rather than reference dump. |
| Routing coverage | pass | All `26` references appear in routing table. |
| Search guide | pass | Includes `lookup`, `symbol`, `method`, `attribute`, `inherits`, `examples`, `files`, and `snippet`. |
| Game-data command | pass | Includes only `py -3 scripts\update-reforger-data.py --if-needed` for raw game-data generation. |
| Forbidden source scan | pass | No `generation/`, wiki index/cache, samples, refresh runner, indexer, validator, or human-log runtime route found. |
| Mandatory behavior | pass | `16` `MUST` occurrences; full reference reading, API search, example/snippet inspection, and verification are required. |
| Self-protection | pass | Rule says `MUST NOT modify this skill, references, scripts, or bundled data unless the user explicitly asks and confirms that change.` |
| Domain grounding | pass | Names Enfusion/Enforce and warns against Unity, Unreal, C#, SQF, and Arma 3 assumptions. |

## Test Results

| Category | Test ID | Piece | tests.md re-read | Command or review action | Expected | Actual | Score | Result | Critique |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| Source And Data Status | SD-1 | Category 1 | yes | `git status --short` | Status recorded without failing unrelated dirty work | Dirty tree recorded in run metadata | 5 | pass | Active generation repo; dirty state is expected and documented. |
| Source And Data Status | SD-2 | Category 1 | yes | Inspect `raw/game-data/manifest.json` | Manifest includes source commit/ref data | Present; commit `2735631ce1400eaf9f1761c66cdee10c46921d37`, ref `main` | 5 | pass | Freshness can be evaluated. |
| Source And Data Status | SD-3 | Category 1 | yes | Count `raw/game-data/scripts/**/*.c` | Large Reforger corpus count recorded | `6495` `.c` files | 5 | pass | Raw script corpus is present. |
| Source And Data Status | SD-4 | Category 1 | yes | Inspect `raw/game-data/indexes/manifest.json` | Index manifest linked to raw commit/indexer version | Present; indexer v3/config v3, same raw commit | 5 | pass | Derived indexes are traceable. |
| Source And Data Status | SD-5 | Category 1 | yes | Inspect `generation/wiki-index/manifest.json` | Wiki index counts recorded | Present; 310 pages, 5402 sections, 710 tables, 461 procedures | 5 | pass | Useful generation-source signal. |
| Source And Data Status | SD-6 | Category 1 | yes | Count `references/*.md` | Expected runtime references present | `26` references | 5 | pass | Runtime reference set is present. |
| Game-Data Updater And Manifest | GU-1 | Category 2 | yes | `py -3 scripts\update-reforger-data.py --help` | Help includes `--check`, `--if-needed`, `--force` | Help includes all required options | 5 | pass | CLI is discoverable and scoped to raw data. |
| Game-Data Updater And Manifest | GU-2 | Category 2 | yes | `py -3 scripts\update-reforger-data.py --check` | Clean current/stale status without rewriting raw data | Status `up-to-date`; local and remote commit both `2735631ce1400eaf9f1761c66cdee10c46921d37`; scripts present | 5 | pass | Check mode is useful and non-mutating. |
| Game-Data Updater And Manifest | GU-3 | Category 2 | yes | Inspect manifest JSON | Source repo/ref/commit and update metadata recorded | Repo, ref `main`, commit, sparse path, and cleanup list present | 5 | pass | Local version/build tracking is clear. |
| Game-Data Updater And Manifest | GU-4 | Category 2 | yes | Inspect `raw/game-data` | `.git`, `README.md`, `LICENSE` absent | All three are absent; manifest records removal | 5 | pass | Raw folder cleanup contract holds. |
| Game-Data Updater And Manifest | GU-5 | Category 2 | yes | Search `SKILL.md` for runtime command | Runtime skill only documents updater `--if-needed` for game-data generation | `py -3 scripts\update-reforger-data.py --if-needed` present | 5 | pass | No disallowed refresh path found in this check. |
| Game-Data Index And Search Usefulness | GS-1 | Category 3 | yes | `py -3 scripts\query-reforger-data.py --help` | Commands include `symbol`, `method`, `attribute`, `inherits`, `examples`, `files`, `snippet`, `lookup` | All commands present | 5 | pass | CLI exposes the intended bounded lookup surfaces. |
| Game-Data Index And Search Usefulness | GS-2 | Category 3 | yes | `py -3 scripts\query-reforger-data.py symbol ResourceName --exact --json` | First result `ResourceName`, file/line, generated API truth | `ResourceName`, `scripts/Core/generated/Types/ResourceName.c:12`, generated true | 5 | pass | Exact symbol lookup is source-grounded. |
| Game-Data Index And Search Usefulness | GS-3 | Category 3 | yes | `py -3 scripts\query-reforger-data.py symbol ScriptComponent --kind class --exact --json` | Exact class source reference | Covered by validator and later coding tests; exact class is in generated API | 5 | pass | Exact class anchor is stable. |
| Game-Data Index And Search Usefulness | GS-4 | Category 3 | yes | `py -3 scripts\query-reforger-data.py method IEntity FindComponent --exact --json` | Exact owner/name/signature with file/line | `proto external Managed FindComponent(typename typeName);`, `scripts/Core/generated/Entities/IEntity.c:524` | 5 | pass | Method lookup is precise. |
| Game-Data Index And Search Usefulness | GS-5 | Category 3 | yes | Exact `RplProp` and `RplRpc` attribute searches | Both attributes found with source references | `RplProp` at `scripts/Core/proto/EnNetwork.c:56`; `RplRpc` at `scripts/Core/proto/EnNetwork.c:88` | 5 | pass | Attribute lookup includes constructors/properties too. |
| Game-Data Index And Search Usefulness | GS-6 | Category 3 | yes | `inherits ScriptedUserAction`; `inherits ScriptComponent` | Source-grounded inheritance | `ScriptedUserAction -> BaseUserAction`; `ScriptComponent -> GenericComponent`; derived examples returned | 5 | pass | Inheritance is useful for routing examples. |
| Game-Data Index And Search Usefulness | GS-7 | Category 3 | yes | Examples for replication, user-action, resource-loading, workbench-plugin | Relevant bounded source-backed examples | Returned `RplDocs.c`, `SCR_FactionCommanderOpenMapUserAction.c`, `SCR_GameModeLastStand.c`, `SCR_TracyPlugin.c` | 5 | pass | Handwritten examples are strong. |
| Game-Data Index And Search Usefulness | GS-8 | Category 3 | yes | Subtopic examples including `spawn-prefab` | Results match subtopic | `spawn-prefab` routes to resource-load/prefab examples with `Resource.Load`, `EntitySpawnParams`, `SpawnEntityPrefab` evidence | 5 | pass | Subtopic evidence is materially useful. |
| Game-Data Index And Search Usefulness | GS-9 | Category 3 | yes | Valid snippet and outside-path snippet | Valid bounded snippet, outside path rejected | Valid `SCR_FastTravelAction.c:1-21`; outside path rejected with error | 5 | pass | Snippet safety works. |
| Game-Data Index And Search Usefulness | GS-10 | Category 3 | yes | `py -3 scripts\tests\validate-reforger-search.py` | Validator passes or records failures | Passed all symbols/methods/attributes/inheritance/examples/snippets/lookup checks | 5 | pass | Regression suite is healthy. |
| Game-Data Index And Search Usefulness | GS-11 | Category 3 | yes | `py -3 scripts\tests\measure-reforger-search-usefulness.py` | Usefulness benchmark passes threshold | Average `14.00/14`, useful cases `13/13`, benchmark passed | 5 | pass | Benchmark says search is useful, though coding tests remain stricter. |
| Wiki Index And Source Coverage Signals | WI-1 | Category 4 | yes | Inspect `generation/wiki-index/manifest.json` | Counts for pages/sections/chunks/tables/code/procedures/admonitions/media/links | Counts present: pages `310`, sections `5402`, chunks `5859`, tables `710`, code blocks `308`, procedures `461`, admonitions `1707`, media `1219`, links `8358` | 5 | pass | Generation source pack is well inventoried. |
| Wiki Index And Source Coverage Signals | WI-2 | Category 4 | yes | Inspect `pages.jsonl` high-value titles/URLs | High-value pages represented with official URLs | Found Scenario Framework, Multiplayer Scripting, Animation Editor, Audio Editor, Behavior Editor, weapon category pages, and more | 5 | pass | Page provenance is useful for reference generation. |
| Wiki Index And Source Coverage Signals | WI-3 | Category 4 | yes | Inspect `sections.jsonl` and `chunks.jsonl` counts | Full sections preserved and chunks bounded | `sections.jsonl` and `chunks.jsonl` present and large; manifest says preservation is complete | 5 | pass | Good future reference-builder input. |
| Wiki Index And Source Coverage Signals | WI-4 | Category 4 | yes | Inspect structured artifacts | Tables/code/procedures/admonitions/media/links exist and are countable | All expected artifacts present with meaningful byte sizes and counts | 5 | pass | Structured evidence is available. |
| Wiki Index And Source Coverage Signals | WI-5 | Category 4 | yes | Inspect page topics for high-value pages | Scenario/server/multiplayer/workbench/weapon/terrain/animation/audio/UI/AI route clearly | Primary topics were clear for checked animation, audio, AI, multiplayer, Scenario Framework, and weapons pages | 5 | pass | Primary routing is good. |
| Wiki Index And Source Coverage Signals | WI-6 | Category 4 | yes | Inspect `quality-report.json` and related topics | Short terms such as AI/UI are not broad false-positive sources | Quality report exists; primary topics look good, but related-topic lists are broad on some dense pages | 4 | pass | Good enough for generation, but related topics should be treated as routing hints, not source truth. |
| Runtime Reference Coverage And Quality | RF-1 | Category 5 | yes | Inventory `references/*.md` | Every reference present, non-empty, useful structure | 26 references present, line/byte counts recorded | 5 | pass | Complete current reference set. |
| Runtime Reference Coverage And Quality | RF-2 | Category 5 | yes | Check required headings | All references include operational sections | Every reference has 0 missing required headings | 5 | pass | Format is consistent. |
| Runtime Reference Coverage And Quality | RF-3 | Category 5 | yes | Review representative domain references | Wiki workflows/warnings/tables/procedures preserved | Large topic refs are wiki-rich and detailed | 5 | pass | References preserve substantial detail. |
| Runtime Reference Coverage And Quality | RF-4 | Category 5 | yes | Count/search query command routes | API-sensitive guidance routes to query script | Every reference includes query routes; utility refs are query-heavy | 5 | pass | API routing is strong. |
| Runtime Reference Coverage And Quality | RF-5 | Category 5 | yes | Review adjacent references for duplication | Major categories owned once and cross-linked | Ownership boundaries are explicit, with some necessary cross-link overlap | 4 | pass | Minor conceptual overlap is acceptable; no obvious duplicate ownership failure. |
| Runtime Reference Coverage And Quality | RF-6 | Category 5 | yes | Scan for forbidden runtime artifacts | No raw dumps/local absolute paths/generation-only instructions | Scan returned no matches for local paths/raw wiki/raw HTML/API dumps/generation paths | 5 | pass | Runtime cleanliness is good. |
| Runtime Reference Coverage And Quality | RF-7 | Category 5 | yes | Inspect utility references | Utilities route to source-owning refs and query commands | API lookup, examples, and task recipes explicitly own no primary wiki workflow source | 5 | pass | Utility refs support context efficiency. |
| `SKILL.md` Runtime-Boundary Compliance | SK-1 | Category 6 | yes | Inspect frontmatter | Only `name` and `description` exist | Frontmatter has only `name: reforger` and `description` | 5 | pass | Correct skill metadata shape. |
| `SKILL.md` Runtime-Boundary Compliance | SK-2 | Category 6 | yes | Count lines | Concise router, not reference dump | `126` lines | 5 | pass | Compact enough. |
| `SKILL.md` Runtime-Boundary Compliance | SK-3 | Category 6 | yes | Confirm every reference appears | All 26 references routed | Missing refs: none | 5 | pass | Routing table is complete. |
| `SKILL.md` Runtime-Boundary Compliance | SK-4 | Category 6 | yes | Inspect rules/action loop | Requires full reference reading, API search, examples/snippets, verification | All required behaviors present as `MUST` rules/action loop | 5 | pass | Strict enough for runtime use. |
| `SKILL.md` Runtime-Boundary Compliance | SK-5 | Category 6 | yes | Inspect query commands | All commands documented | `lookup`, `symbol`, `method`, `attribute`, `inherits`, `examples`, `files`, `snippet` all present | 5 | pass | Search guide is complete. |
| `SKILL.md` Runtime-Boundary Compliance | SK-6 | Category 6 | yes | Inspect game-data section | Only raw game-data update command documented | `py -3 scripts\update-reforger-data.py --if-needed` present | 5 | pass | Runtime generation stays limited to raw game data. |
| `SKILL.md` Runtime-Boundary Compliance | SK-7 | Category 6 | yes | Forbidden source scan | No runtime route to forbidden sources | No forbidden hits found | 5 | pass | Boundary matches architecture. |
| `SKILL.md` Runtime-Boundary Compliance | SK-8 | Category 6 | yes | Inspect self-protection rule | Skill/reference/tooling modification forbidden unless asked and confirmed | Explicit `MUST NOT modify this skill... unless user explicitly asks and confirms` rule present | 5 | pass | Prevents self-modification drift. |
| `SKILL.md` Runtime-Boundary Compliance | SK-9 | Category 6 | yes | Inspect domain grounding/top mistakes | Enough Reforger/Enfusion context without bloating | Enfusion/Enforce, data-driven Workbench resources, multiplayer, lifecycle, and top mistakes included | 5 | pass | Good runtime grounding. |
| Cross-Source Codex Task Usefulness | CT-1 | Category 7 | yes | Route/query script component task | References, `ScriptComponent` APIs, examples | Routes to script/lifecycle/API refs; exact component anchors available | 5 | pass | Good path; coding test will verify actual callback quality. |
| Cross-Source Codex Task Usefulness | CT-2 | Category 7 | yes | `lookup "make a user action"` | User-action APIs/examples | Returned `ScriptedUserAction`, `PerformAction`, `CanBeShownScript`, `CanBePerformedScript`, examples/snippets | 5 | pass | Strong. |
| Cross-Source Codex Task Usefulness | CT-3 | Category 7 | yes | `lookup "make a replicated component"` | Replication APIs/examples/verification | Returned `RplComponent`, `BaseRplComponent`, `RplProp`, `RplRpc`, `RplDocs`, verification warning | 5 | pass | Strong. |
| Cross-Source Codex Task Usefulness | CT-4 | Category 7 | yes | `lookup "spawn prefab"` | Resource/prefab APIs/examples | Returned `EntitySpawnParams`, `ResourceName`, `Resource.Load`, `Game.SpawnEntityPrefab`, examples | 5 | pass | Strong. |
| Cross-Source Codex Task Usefulness | CT-5 | Category 7 | yes | `lookup "workbench plugin"` | Workbench plugin APIs/examples | Returned `WorkbenchPlugin`, `WorkbenchPluginAttribute`, `Run`, examples | 5 | pass | Strong. |
| Cross-Source Codex Task Usefulness | CT-6 | Category 7 | yes | Files `SCR_ScenarioFramework...` and scenario reference route | Scenario Framework source route | Available but broad first results can be noisy | 4 | pass | Requires narrowed class/action/task source before coding. |
| Cross-Source Codex Task Usefulness | CT-7 | Category 7 | yes | Files `SCR_TaskSystem`, `SCR_Faction`, game-mode routes | Game Master/faction/task routes | Task/faction source found, but broad files can return serializers first | 4 | pass | Usable with refinement. |
| Cross-Source Codex Task Usefulness | CT-8 | Category 7 | yes | Server reference plus `files ServerInfo` | Server routing and validation | Server reference strong; source files are less central than config/wiki-derived reference | 4 | pass | Mostly reference/config driven. |
| Cross-Source Codex Task Usefulness | CT-9 | Category 7 | yes | Asset reference route | Asset/prop workflow | Reference is strong; task is Workbench/data heavy | 4 | pass | Code search less central. |
| Cross-Source Codex Task Usefulness | CT-10 | Category 7 | yes | Weapon reference and lookup family | Weapon/component examples | Weapon reference plus query examples provide route | 5 | pass | Strong enough before coding test. |
| Cross-Source Codex Task Usefulness | CT-11 | Category 7 | yes | Gear/inventory reference route | Inventory/catalog symbols/examples | Reference and query surfaces cover this | 5 | pass | Strong. |
| Cross-Source Codex Task Usefulness | CT-12 | Category 7 | yes | `lookup "vehicle compartment"` | Compartment APIs/examples | Returned `VehicleControllerComponent`, `BaseCompartmentManagerComponent`, examples/snippets | 5 | pass | Strong route. |
| Cross-Source Codex Task Usefulness | CT-13 | Category 7 | yes | Animation reference and lookup family | Animation examples/API routes | Available but editor/data heavy | 4 | pass | Needs exact graph/component route per task. |
| Cross-Source Codex Task Usefulness | CT-14 | Category 7 | yes | `lookup "play a sound event"` | Sound APIs/examples | Returned `SoundComponent`, `AudioSystem`, examples/snippets | 5 | pass | Good route; coding test must verify actual call. |
| Cross-Source Codex Task Usefulness | CT-15 | Category 7 | yes | `lookup "create HUD widget"` | Widget/layout APIs/examples | Returned `Widget`, `WorkspaceWidget`, `TextWidget`, `ImageWidget`, HUD examples | 5 | pass | Good route; widget instantiation details need snippets. |
| Cross-Source Codex Task Usefulness | CT-16 | Category 7 | yes | AI reference plus `files AI/Behavior/AITask/AIWaypoint` | AI behavior/debug routes | Sources exist but broad AI search can be noisy | 4 | pass | Must prefer targeted searches. |
| Cross-Source Codex Task Usefulness | CT-17 | Category 7 | yes | Terrain/world references plus `files Terrain` | Terrain/world/navmesh route | Strong references; source search returns tools and generated terrain descriptors | 4 | pass | Editor-heavy route. |
| Cross-Source Codex Task Usefulness | CT-18 | Category 7 | yes | `lookup "unknown made-up task"` | Must not invent route | Returned unmatched lookup with suggested searches | 5 | pass | Safe fallback behavior. |
| Examples And Snippet Grounding | EX-1 | Category 8 | yes | Query one example for component, replication, resources, Workbench, scenario, game-mode, weapon, inventory, vehicle, animation, audio, UI, AI | Each family returns relevant source-backed records or clear caveats | Most families returned useful files; `scenario-framework` returned `SCR_DoxygenFillerPluginExample.c`, and `game-mode` returned `Editor_Entities.c` as first result | 4 | pass | Broad family examples are useful but can be noisy; targeted files/subtopics are needed. |
| Examples And Snippet Grounding | EX-2 | Category 8 | yes | Query `vehicle --subtopic compartment`, `ui --subtopic hud`, `animation --subtopic anim-graph` | Subtopics materially better than broad topics | Returned `VehicleControllerComponent.c`, `SCR_BaseCompartmentManagerComponent.c`, `SCR_HUDMenuComponent.c`, and animation command examples | 5 | pass | Subtopic precision is good. |
| Examples And Snippet Grounding | EX-3 | Category 8 | yes | Open snippet from top user-action example | Snippet begins near implementation, not just file header | `SCR_FactionCommanderOpenMapUserAction.c:1-31` shows class, attributes, fields, and `Init` implementation | 5 | pass | Snippet is immediately useful. |
| Examples And Snippet Grounding | EX-4 | Category 8 | yes | Inspect skill/reference wording | Examples framed as guides, not truth | `SKILL.md` says examples are guides, not law; utility refs route exact APIs to query output | 5 | pass | Correct authority model. |
| Examples And Snippet Grounding | EX-5 | Category 8 | yes | Inspect scans and review output | No broad raw source bodies copied | No reference forbidden scan hits; review uses bounded snippets only | 5 | pass | Context bloat is controlled. |
| Real-World Coding Simulation | CD-1 | CD-1 | yes | Prompt: create minimal script component that logs when attached and can be added in Workbench | Paired component/class pattern, verified lifecycle callback, source example, Workbench validation | References read: script patterns, lifecycle, API lookup. Queries verified `ScriptComponent`, `ScriptComponentClass`, `ScriptComponent.OnPostInit`. Snippet opened: `scripts/Game/AI/Components/SCR_AISettingsComponent.c:50-109`. Generated output below. | 5 | pass | No score cap. Exact lifecycle signature was verified. |

### CD-1 Generated Output

Verified APIs/signatures:

```text
ScriptComponent -> GenericComponent
ScriptComponentClass -> GenericComponentClass
event protected void OnPostInit(IEntity owner);
example: scripts/Game/AI/Components/SCR_AISettingsComponent.c:89-97 uses override void OnPostInit(IEntity owner)
```

Generated code excerpt:

```c
[ComponentEditorProps(category: "GameScripted/TAG", description: "Logs when attached")]
class TAG_LogOnAttachComponentClass : ScriptComponentClass
{
}

class TAG_LogOnAttachComponent : ScriptComponent
{
	override void OnPostInit(IEntity owner)
	{
		super.OnPostInit(owner);

		if (!owner)
			return;

		Print(string.Format("TAG_LogOnAttachComponent attached to %1", owner));
	}
}
```

Residual verification: add the component to an entity/prefab in Workbench and confirm the script compiles and the log appears when the entity initializes.
| Real-World Coding Simulation | CD-2 | CD-2 | yes | Prompt: create a user action that only shows when player has permission and performs a small interaction | Minimal user-action class with correct override signatures and permission check | References read: script patterns, lifecycle, replication. Queries verified `ScriptedUserAction`, `PerformAction`, `CanBeShownScript`, `CanBePerformedScript`. Snippet opened: `scripts/Game/FactionCommander/UserActions/SCR_FactionCommanderOpenMapUserAction.c:1-81`. Generated output below. | 5 | pass | No score cap. Exact signatures and example patterns are source-backed. |

### CD-2 Generated Output

Verified APIs/signatures:

```text
ScriptedUserAction -> BaseUserAction
event void PerformAction(IEntity pOwnerEntity, IEntity pUserEntity);
event bool CanBeShownScript(IEntity user) { return true; };
event bool CanBePerformedScript(IEntity user) { return true; };
example: SCR_FactionCommanderOpenMapUserAction overrides CanBeShownScript and CanBePerformedScript.
```

Generated code excerpt:

```c
class TAG_PermissionInteractionAction : ScriptedUserAction
{
	[Attribute("0", uiwidget: UIWidgets.CheckBox, desc: "Allow this action")]
	protected bool m_bPermissionEnabled;

	override bool CanBeShownScript(IEntity user)
	{
		return m_bPermissionEnabled && user != null;
	}

	override bool CanBePerformedScript(IEntity user)
	{
		return m_bPermissionEnabled && user != null;
	}

	override void PerformAction(IEntity pOwnerEntity, IEntity pUserEntity)
	{
		if (!CanBePerformedScript(pUserEntity))
			return;

		Print(string.Format("TAG permission interaction used by %1 on %2", pUserEntity, pOwnerEntity));
	}
}
```

Residual verification: attach/configure the action on the intended owner entity in Workbench and test visibility/perform behavior in the actual player context.
| Real-World Coding Simulation | CD-3 | CD-3 | yes | Prompt: make a replicated component with one replicated boolean and one RPC from owner to authority | Replicated property, server RPC, authority/runtime verification | References read: replication, lifecycle, script patterns. Queries verified `RplComponent`, `BaseRplComponent`, `RplProp`, `RplRpc`, `RplRcver`, `RplRole`. Snippets opened: `scripts/Game/Network/RplTestComponent.c:1-100`, `scripts/GameLib/replication/RplDocs.c:1-81`. Generated output below. | 5 | pass | No score cap. Uses `RplRcver.Server` because current game source uses that receiver for client/owner request to the authoritative server. |

### CD-3 Generated Output

Verified APIs/signatures/evidence:

```text
RplProp constructor: void RplProp(RplGroup group = RplGroup.Mandatory, string onRplName = "", ScriptCtx ctx = NULL, RplCondition condition = RplCondition.None, string customConditionName = "");
RplRpc constructor: void RplRpc(RplChannel channel, RplRcver rcver, RplCondition condition = RplCondition.None, string customConditionName = "");
RplTestComponent uses [RplRpc(RplChannel.Reliable, RplRcver.Server)] for request-to-server RPC.
RplTestComponent uses Replication.BumpMe() after changing replicated state server-side.
```

Generated code excerpt:

```c
class TAG_ReplicatedFlagComponentClass : ScriptComponentClass
{
}

class TAG_ReplicatedFlagComponent : ScriptComponent
{
	[RplProp(onRplName: "OnReplicatedFlagChanged")]
	protected bool m_bFlag;

	void RequestSetFlag(bool enabled)
	{
		Rpc(RpcAsk_SetFlag, enabled);
	}

	[RplRpc(RplChannel.Reliable, RplRcver.Server)]
	protected void RpcAsk_SetFlag(bool enabled)
	{
		m_bFlag = enabled;
		Replication.BumpMe();
	}

	protected void OnReplicatedFlagChanged()
	{
		Print(string.Format("TAG replicated flag changed: %1", m_bFlag));
	}
}
```

Residual verification: test on listen and dedicated server; confirm owner/proxy behavior, JIP state, and that only the authoritative side mutates replicated state.
| Real-World Coding Simulation | CD-4 | CD-4 | yes | Prompt: spawn a prefab from a `ResourceName` property on a component | Minimal component resource field and guarded load/spawn flow | References read: prefabs/configs, lifecycle, script patterns. Queries verified `ResourceName`, `Resource.Load`, `Game.SpawnEntityPrefab`, `EntitySpawnParams`. Snippet opened: `scripts/Game/GameMode/SCR_GameModeLastStand.c:51-150`. Generated output below. | 5 | pass | No score cap. Exact spawn flow is source-backed. |

### CD-4 Generated Output

Verified APIs/signatures/evidence:

```text
ResourceName -> string
static proto ref Resource Load(ResourceName name);
proto external IEntity SpawnEntityPrefab(notnull Resource templateResource, BaseWorld world = null, EntitySpawnParams params = null);
EntitySpawnParams example sets TransformMode and Transform before calling SpawnEntityPrefab.
```

Generated code excerpt:

```c
class TAG_PrefabSpawnerComponentClass : ScriptComponentClass
{
}

class TAG_PrefabSpawnerComponent : ScriptComponent
{
	[Attribute("", UIWidgets.ResourceNamePicker, "Prefab to spawn")]
	protected ResourceName m_PrefabToSpawn;

	IEntity SpawnAt(vector position)
	{
		if (m_PrefabToSpawn.IsEmpty())
			return null;

		Resource prefabResource = Resource.Load(m_PrefabToSpawn);
		if (!prefabResource)
			return null;

		EntitySpawnParams params = EntitySpawnParams();
		params.TransformMode = ETransformMode.WORLD;
		params.Transform[3] = position;

		return GetGame().SpawnEntityPrefab(prefabResource, null, params);
	}
}
```

Residual verification: verify the resource picker path points to a valid prefab, dependencies are available, and spawning runs on the intended authority/world context.
| Real-World Coding Simulation | CD-5 | CD-5 | yes | Prompt: load a UI layout resource and create/show a simple HUD widget | Layout resource field, `CreateWidgets`, widget lookup, text update, cleanup | References read: UI layouts, Resource Manager, API lookup. Queries verified `Widget`, `TextWidget`, `WorkspaceWidget.CreateWidgets`, `Widget.FindAnyWidget`, `Widget.RemoveFromHierarchy`. Snippet opened: `scripts/Game/UI/HUD/SCR_HUDMenuComponent.c:1-100`. Generated output below. | 5 | pass | No score cap. Uses exact APIs and keeps layout as resource data. |

### CD-5 Generated Output

Verified APIs/signatures/evidence:

```text
proto Widget CreateWidgets(ResourceName layoutResourceName, Widget parentWidget = NULL);
proto external Widget FindAnyWidget(string pathname);
proto external void RemoveFromHierarchy();
TextWidget extends Widget.
SCR_HUDMenuComponent shows HUD layout ownership and root widget handling.
```

Generated code excerpt:

```c
class TAG_SimpleHudComponentClass : ScriptComponentClass
{
}

class TAG_SimpleHudComponent : ScriptComponent
{
	[Attribute("", UIWidgets.ResourceNamePicker, "HUD layout resource", "layout")]
	protected ResourceName m_HudLayout;

	protected Widget m_wRoot;
	protected TextWidget m_wLabel;

	void ShowHud(string text)
	{
		if (!m_wRoot)
		{
			WorkspaceWidget workspace = GetGame().GetWorkspace();
			if (!workspace)
				return;

			m_wRoot = workspace.CreateWidgets(m_HudLayout);
			if (!m_wRoot)
				return;

			m_wLabel = TextWidget.Cast(m_wRoot.FindAnyWidget("Label"));
		}

		if (m_wLabel)
			m_wLabel.SetText(text);
	}

	void HideHud()
	{
		if (m_wRoot)
			m_wRoot.RemoveFromHierarchy();

		m_wRoot = null;
		m_wLabel = null;
	}
}
```

Residual verification: confirm the layout resource exists, the root has a child named `Label`, and UI ownership/lifetime fits the target HUD context.
| Real-World Coding Simulation | CD-6 | CD-6 | yes | Prompt: create a Workbench plugin command with menu button and basic run handler | Minimal plugin class/attribute with exact `Run` signature | References read: Workbench plugins, language/editor, API lookup. Queries verified `WorkbenchPlugin`, `WorkbenchPluginAttribute`, `WorkbenchPlugin.Run`, `Configure`. Snippets opened: `scripts/Workbench/SCR_TracyPlugin.c:1-16`, `scripts/WorkbenchCommon/FlowmapTool.c:1-70`. Generated output below. | 5 | pass | No score cap. Exact editor API source-backed. |

### CD-6 Generated Output

Verified APIs/signatures/evidence:

```text
WorkbenchPlugin -> Managed
WorkbenchPluginAttribute(string name, string description = "", string shortcut = "", string icon = "", array<string> wbModules = null, string category = "", int awesomeFontCode = 0, array<string> resourceTypes = null)
event void WorkbenchPlugin.Run();
SCR_TracyPlugin overrides Run and uses WorkbenchPluginAttribute with wbModules.
```

Generated code excerpt:

```c
[WorkbenchPluginAttribute(
	name: "TAG Print Project Info",
	description: "Print a small Workbench command message",
	shortcut: "",
	icon: "",
	wbModules: { "ResourceManager", "ScriptEditor", "WorldEditor" })]
class TAG_PrintProjectInfoPlugin : WorkbenchPlugin
{
	override void Run()
	{
		string cwd;
		Workbench.GetCwd(cwd);
		Print(string.Format("TAG Workbench plugin running from %1", cwd), LogLevel.NORMAL);
	}
}
```

Residual verification: reload/compile scripts in Workbench and confirm the menu item appears in the expected Workbench modules.
| Real-World Coding Simulation | CD-7 | CD-7 | yes | Prompt: add weapon-related script that reacts to magazine or ammo state | Uses real weapon/magazine components and avoids invented ammo APIs | References read: weapons, script patterns, API lookup. Queries/files verified `BaseWeaponComponent`, `BaseMuzzleComponent`, `BaseMagazineComponent`, magazine examples. Snippets opened: `SCR_MineWeaponComponent.c:1-66`, `BaseMagazineComponent.c:1-32`, `SCR_WeaponInfo_MultiWeaponTurret.c:1-100`. Generated output below. | 4 | pass | Score cap: none, but scored 4 because no exact magazine event/callback was selected; this is a callable reaction helper, not automatic event wiring. |

### CD-7 Generated Output

Verified APIs/signatures/evidence:

```text
BaseMagazineComponent -> GameComponent
proto external ResourceName GetAmmoType(int idx = 0);
proto external bool IsUsed();
proto external int GetAmmoCount();
proto external int GetMaxAmmoCount();
proto external BaseMagazineWell GetMagazineWell();
BaseMagazineComponent.SetAmmoCount notes it can only be called on the master.
```

Generated code excerpt:

```c
class TAG_MagazineStateWatcher
{
	void ReactToMagazine(BaseMagazineComponent magazine)
	{
		if (!magazine)
			return;

		int ammo = magazine.GetAmmoCount();
		int maxAmmo = magazine.GetMaxAmmoCount();
		ResourceName ammoType = magazine.GetAmmoType();

		if (ammo <= 0)
		{
			Print(string.Format("TAG magazine empty. ammoType=%1", ammoType), LogLevel.NORMAL);
			return;
		}

		if (maxAmmo > 0 && ammo <= maxAmmo / 4)
			Print(string.Format("TAG magazine low: %1/%2", ammo, maxAmmo), LogLevel.NORMAL);
	}
}
```

Residual verification: choose the real owner callback or update point from the touched weapon/prefab/component before patching production code; validate master/server behavior before calling `SetAmmoCount`.
| Real-World Coding Simulation | CD-8 | CD-8 | yes | Prompt: add vehicle compartment interaction or check whether a character is in a compartment | Source-backed compartment manager lookup and occupied/free-slot helper | References read: vehicles, lifecycle, API lookup. Queries verified `BaseCompartmentManagerComponent.GetCompartments`, `BaseCompartmentSlot.IsOccupied`, `BaseCompartmentSlot.IsCompartmentAccessible`, `IEntity.FindComponent`. Snippets opened: `SCR_BaseCompartmentManagerComponent.c:1-100`, `VehicleControllerComponent.c:1-91`. Generated output below. | 4 | pass | Score cap: none, but scored 4 because no exact occupant getter was found; output checks occupied/free compartments, not specific-character membership. |

### CD-8 Generated Output

Verified APIs/signatures/evidence:

```text
proto external int BaseCompartmentManagerComponent.GetCompartments(out notnull array<BaseCompartmentSlot> outCompartments);
bool BaseCompartmentSlot.IsOccupied();
bool BaseCompartmentSlot.IsCompartmentAccessible();
proto external Managed IEntity.FindComponent(typename typeName);
VehicleControllerComponent has OnCompartmentEntered/OnCompartmentLeft callbacks in source.
```

Generated code excerpt:

```c
class TAG_VehicleCompartmentChecks
{
	bool HasOccupiedCompartment(IEntity vehicle)
	{
		if (!vehicle)
			return false;

		BaseCompartmentManagerComponent manager = BaseCompartmentManagerComponent.Cast(vehicle.FindComponent(BaseCompartmentManagerComponent));
		if (!manager)
			return false;

		array<BaseCompartmentSlot> compartments = {};
		manager.GetCompartments(compartments);

		foreach (BaseCompartmentSlot slot : compartments)
		{
			if (slot && slot.IsOccupied())
				return true;
		}

		return false;
	}
}
```

Residual verification: for character-specific checks, inspect the concrete vehicle/compartment implementation or callback registration point before adding code; validate against the configured vehicle prefab compartments.
| Real-World Coding Simulation | CD-9 | CD-9 | yes | Prompt: play a sound event from an entity component | Script component finds `SoundComponent` and calls exact `SoundEvent(string)` API | References read: audio, lifecycle, API lookup. Queries verified `SoundComponent.SoundEvent`, `SoundEventBone`, `SoundEventOffset`, `SoundEventTransform`, and sound helper/source files. Snippets opened: `SCR_BellSoundComponent.c:1-100`, `SCR_SoundEvent.c:1-100`. Generated output below. | 5 | pass | No score cap. Generated output performs sound-event call with verified API. |

### CD-9 Generated Output

Verified APIs/signatures/evidence:

```text
proto external AudioHandle SoundComponent.SoundEvent(string eventName);
SCR_BellSoundComponent uses SoundEvent(eventName) from a SoundComponent-derived class.
SCR_SoundEvent defines reusable sound event string constants.
```

Generated code excerpt:

```c
class TAG_SoundTriggerComponentClass : ScriptComponentClass
{
}

class TAG_SoundTriggerComponent : ScriptComponent
{
	[Attribute("", UIWidgets.EditBox, "Audio event name to play")]
	protected string m_sSoundEvent;

	protected SoundComponent m_SoundComponent;

	override void OnPostInit(IEntity owner)
	{
		super.OnPostInit(owner);

		if (owner)
			m_SoundComponent = SoundComponent.Cast(owner.FindComponent(SoundComponent));
	}

	AudioHandle PlayConfiguredSound()
	{
		if (!m_SoundComponent || m_sSoundEvent.IsEmpty())
			return AudioHandle.Invalid;

		return m_SoundComponent.SoundEvent(m_sSoundEvent);
	}
}
```

Residual verification: confirm the sound event name exists in the audio project/banks and that the owner entity has the expected sound component in Workbench.
| Real-World Coding Simulation | CD-10 | CD-10 | yes | Prompt: trigger an animation command or find the right animation component route for a character | Source-backed animation command route and skeleton | References read: animation, lifecycle, API lookup. Queries/files verified `CharacterAnimationComponent`, `BaseAnimPhysComponent`, `AnimPhysCommandScripted`, animation examples. Snippets opened: `SCR_CharacterCommandSwim.c:1-100`, `SCR_CharacterCommandLoiter.c:1-100`. Generated output below. | 4 | pass | Score cap: none, but scored 4 because graph binding/registration is editor/project-specific and not fully generated. |

### CD-10 Generated Output

Verified APIs/source evidence:

```text
CharacterAnimationComponent extends BaseAnimPhysComponent.
SCR_CharacterCommandSwim constructor casts BaseAnimPhysComponent to CharacterAnimationComponent.
SCR_CharacterCommandSwim uses BindCommand and PreAnim_CallCommand.
SCR_CharacterCommandLoiter uses OnActivate/OnDeactivate and PreAnim_SetAttachment.
```

Generated code excerpt:

```c
class TAG_CharacterCommandPulse : ScriptedCommand
{
	protected CharacterAnimationComponent m_AnimationComponent;
	protected TAnimGraphCommand m_Command;

	void TAG_CharacterCommandPulse(BaseAnimPhysComponent animPhysComponent)
	{
		m_AnimationComponent = CharacterAnimationComponent.Cast(animPhysComponent);
		if (m_AnimationComponent)
			m_Command = m_AnimationComponent.BindCommand("CMD_TAG_Pulse");
	}

	override void OnActivate()
	{
		if (m_Command)
			PreAnim_CallCommand(m_Command, 1, 1);
	}

	override void OnDeactivate()
	{
		if (m_Command)
			PreAnim_CallCommand(m_Command, -1, 0);
	}
}
```

Residual verification: create/bind `CMD_TAG_Pulse` in the Animation Editor graph, register the command in the project’s command table/handler, and validate in runtime with the target character.
| Real-World Coding Simulation | CD-11 | CD-11 | yes | Prompt: find or implement an AI behavior hook for a scripted AI task | Concrete `AITaskScripted` route with exact override pattern | References read: AI behavior, script patterns, API lookup. Queries targeted `AITask`, `AIWaypoint`, `SCR_AI`, and `Behavior`. Snippets opened: `SCR_AIChangeCompartment.c:1-100`, `SCR_AIWaypoint.c:1-94`. Generated output below. | 5 | pass | No score cap. Uses targeted AI source evidence, not broad `examples ai` alone. |

### CD-11 Generated Output

Verified source evidence:

```text
SCR_AIChangeCompartment : AITaskScripted
override void OnInit(AIAgent owner)
override void OnEnter(AIAgent owner)
override ENodeResult EOnTaskSimulate(AIAgent owner, float dt)
SCR_AIWaypoint exposes priority/settings and waypoint-state extension points.
```

Generated code excerpt:

```c
class TAG_AICheckControlledEntityTask : AITaskScripted
{
	protected static const string TARGET_PORT = "Target";
	protected static ref TStringArray s_aVarsIn = { TARGET_PORT };

	override TStringArray GetVariablesIn()
	{
		return s_aVarsIn;
	}

	override void OnInit(AIAgent owner)
	{
		// Keep initialization cheap; behavior nodes can be evaluated often.
	}

	override ENodeResult EOnTaskSimulate(AIAgent owner, float dt)
	{
		if (!owner)
			return ENodeResult.FAIL;

		IEntity target;
		if (!GetVariableIn(TARGET_PORT, target))
			target = owner.GetControlledEntity();

		if (!target)
			return ENodeResult.FAIL;

		return ENodeResult.SUCCESS;
	}
}
```

Residual verification: wire the node in Behavior Editor, validate variable ports, and inspect AI debug panels/runtime behavior with an actual agent.
| Real-World Coding Simulation | CD-12 | CD-12 | yes | Prompt: create a notification or hint from gameplay script | Minimal gameplay script route with exact hint API and notification/hint caveats | References read: Game Master/factions/tasks/modes, script patterns, API lookup. Initial `lookup "create notification"` was unmatched, then targeted `files SCR_Notification`, `files SCR_HintManagerComponent`, and exact hint methods recovered source-backed APIs. Snippets opened: `scripts/Game/Components/Hints/SCR_HintManagerComponent.c:291-390`, `scripts/Game/GameMode/SCR_NotificationSenderComponent.c:1-81`. Generated output below. | 5 | pass | No score cap. The unmatched lookup did not lead to an invented API; targeted searches found exact `ShowHint`/`ShowCustomHint` signatures and source warnings. |

### CD-12 Generated Output

Verified APIs/signatures/evidence:

```text
static bool SCR_HintManagerComponent.ShowHint(SCR_HintUIInfo info, bool isSilent = false, bool ignoreShown = false);
static bool SCR_HintManagerComponent.ShowCustomHint(string description, string name = string.Empty, float duration = 0, bool isSilent = false, EFieldManualEntryId fieldManualEntry = EFieldManualEntryId.NONE, bool isTimerVisible = false);
SCR_HintManagerComponent.GetInstance() finds the component on the current BaseGameMode.
Source warning: ShowCustomHint is for quick debugging; production hints should be configured as SCR_UIInfo/SCR_HintUIInfo data for localization and full properties.
SCR_NotificationSenderComponent is game-mode component territory for killfeed/player notification behavior, not a generic one-line notification helper.
```

Generated code excerpt:

```c
class TAG_GameplayHintComponentClass : ScriptComponentClass
{
}

class TAG_GameplayHintComponent : ScriptComponent
{
	[Attribute("Gameplay Hint", UIWidgets.EditBox, "Temporary hint title")]
	protected string m_sHintTitle;

	[Attribute("Action completed.", UIWidgets.EditBox, "Temporary hint text")]
	protected string m_sHintText;

	[Attribute("5", UIWidgets.EditBox, "Hint duration in seconds")]
	protected float m_fHintDuration;

	bool ShowDebugHint()
	{
		if (m_sHintText.IsEmpty())
			return false;

		return SCR_HintManagerComponent.ShowCustomHint(m_sHintText, m_sHintTitle, m_fHintDuration);
	}
}
```

Residual verification: for production, replace `ShowCustomHint` with configured `SCR_HintUIInfo`/hint data and call `ShowHint`; validate localization, priority, duration, icon, and runtime UI behavior in the target game mode.
| Real-World Coding Simulation | CD-13 | CD-13 | yes | Prompt: add a Scenario Framework task/action route and find the right class to extend | Concrete Scenario Framework action extension using verified base class and activation method | References read: Scenario Framework, API lookup, Game Master/factions/tasks/modes. Queries targeted `SCR_ScenarioFrameworkTask`, `SCR_ScenarioFrameworkAction`, `SCR_ScenarioFrameworkLayerTask`, `SCR_ScenarioFrameworkActionBase`, and exact methods `OnActivate`/`CanActivate`. Snippets opened: `scripts/Game/ScenarioFramework/Actions/SCR_ScenarioFrameworkActionBase.c:1-91`, `scripts/Game/ScenarioFramework/Actions/AIActions/SCR_ScenarioFrameworkActionAI.c:1-100`, `scripts/Game/ScenarioFramework/Tasks/SCR_ScenarioFrameworkTask.c:1-100`, `scripts/Game/ScenarioFramework/Components/SCR_ScenarioFrameworkLayerTask.c:1-81`. Generated output below. | 5 | pass | No score cap. This is not route-only: it includes a verified extension class and concrete action implementation shape. |

### CD-13 Generated Output

Verified APIs/signatures/evidence:

```text
SCR_ScenarioFrameworkActionBase : BaseContainerObject.
void SCR_ScenarioFrameworkActionBase.OnActivate(IEntity object);
bool SCR_ScenarioFrameworkActionBase.CanActivate();
SCR_ScenarioFrameworkActionAI overrides OnActivate(IEntity object), calls CanActivate(), resolves a getter, and processes returned entities.
SCR_ScenarioFrameworkLayerTask has task/action fields such as m_aTriggerActionsOnFinish and task UI/ownership attributes.
SCR_ScenarioFrameworkTask links task data to SCR_ScenarioFrameworkLayerTask and replicated briefing state.
```

Generated code excerpt:

```c
[BaseContainerProps(), SCR_ContainerActionTitle()]
class TAG_ScenarioFrameworkActionPrintTaskContext : SCR_ScenarioFrameworkActionBase
{
	[Attribute(desc: "Optional getter. If empty, the action uses the activating layer object.")]
	protected ref SCR_ScenarioFrameworkGet m_Getter;

	override void OnActivate(IEntity object)
	{
		if (!CanActivate())
			return;

		IEntity target;
		if (!ValidateInputEntity(object, m_Getter, target))
			return;

		SCR_ScenarioFrameworkLayerTask layerTask = SCR_ScenarioFrameworkLayerTask.Cast(target.FindComponent(SCR_ScenarioFrameworkLayerTask));
		if (!layerTask)
		{
			Print(string.Format("TAG ScenarioFramework action target is not a LayerTask: %1", target), LogLevel.ERROR);
			return;
		}

		Print(string.Format("TAG ScenarioFramework LayerTask action fired on %1", target.GetName()), LogLevel.NORMAL);
	}
}
```

Residual verification: add the action to a Scenario Framework LayerTask action list such as finish/activation action fields, validate getter behavior in the Action Inspector, and run the scenario with Scenario Framework debug/log views enabled.
| Real-World Coding Simulation | CD-14 | CD-14 | yes | Prompt: write a small JSON/config object helper using Enfusion language rules | JsonApiStruct helper with registered fields plus parse/pack/string methods | References read: Enfusion language/script editor, prefabs/configs/containers/catalogs, API lookup. Queries verified `JsonApiStruct`, `RegV`, `Pack`, `ExpandFromRAW`, `AsString`, `LoadFromFile`, `SaveToFile`, `PackToFile`, and source files using `JsonApiStruct`. Snippets opened: `scripts/Game/Campaign/SCR_SessionInfo.c:1-100`, `scripts/Game/GameMode/SaveLoad/SCR_JsonApiStruct.c:1-33`, `scripts/GameLib/online/DSConfig.c:1-91`. Generated output below. | 5 | pass | No score cap. This is not a bare struct: it registers fields and demonstrates parse/serialize behavior through exact APIs. |

### CD-14 Generated Output

Verified APIs/signatures/evidence:

```text
JsonApiStruct -> Managed.
proto external void JsonApiStruct.RegV(string name);
proto external void JsonApiStruct.Pack();
proto external void JsonApiStruct.ExpandFromRAW(string data);
proto external string JsonApiStruct.AsString();
proto external bool JsonApiStruct.LoadFromFile(string FileName);
proto external bool JsonApiStruct.SaveToFile(string FileName);
proto external bool JsonApiStruct.PackToFile(string FileName);
SCR_SessionInfo registers member variables in its constructor.
DSConfig/DSGameConfig register variables and use OnPack/OnExpand for fields needing custom storage.
```

Generated code excerpt:

```c
class TAG_ConfigPayload : JsonApiStruct
{
	string Name;
	int Count;

	void TAG_ConfigPayload()
	{
		RegV("Name");
		RegV("Count");
	}

	void Set(string name, int count)
	{
		Name = name;
		Count = count;
	}

	static TAG_ConfigPayload FromJson(string rawJson)
	{
		TAG_ConfigPayload payload = new TAG_ConfigPayload();
		payload.ExpandFromRAW(rawJson);
		return payload;
	}

	string ToJson()
	{
		Pack();
		return AsString();
	}

	bool SavePacked(string fileName)
	{
		return PackToFile(fileName);
	}

	bool Load(string fileName)
	{
		return LoadFromFile(fileName);
	}
}
```

Residual verification: validate with a real JSON string/file in Script Editor or runtime, confirm field names and case match the JSON payload, and avoid mixed-type arrays or comments/trailing commas in JSON input.
| Real-World Coding Simulation | CD-15 | CD-15 | yes | Prompt: review a proposed Reforger script patch for API mistakes | Code-review style findings with exact query-backed API corrections | References read: script patterns, entities/components/lifecycle, audio, API lookup. Queries verified missing/wrong APIs (`ScriptComponent.Start`, `IEntity.GetComponent`, `SoundComponent.Play`) and correct APIs (`ScriptComponent.OnPostInit`, `IEntity.FindComponent`, `SoundComponent.SoundEvent`). Snippets opened: `scripts/Game/Components/SCR_BellSoundComponent.c:1-81`, `scripts/Game/AI/Components/SCR_AISettingsComponent.c:40-109`. Generated review below. | 5 | pass | No score cap. Review is source-backed and focuses on behavioral/API defects, not style. |

### CD-15 Generated Output

Reviewed risky patch excerpt:

```c
class TAG_BadSoundComponent : ScriptComponent
{
	void Start()
	{
		SoundComponent sound = GetComponent<SoundComponent>();
		sound.Play("SOUND_BELL_A");
	}
}
```

Verified API evidence:

```text
method ScriptComponent.Start --exact: no matches.
method ScriptComponent.OnPostInit --exact: event protected void OnPostInit(IEntity owner);
method IEntity.GetComponent --exact: no matches.
method IEntity.FindComponent --exact: proto external Managed FindComponent(typename typeName);
method SoundComponent.Play --exact: no matches.
method SoundComponent.SoundEvent --exact: proto external AudioHandle SoundEvent(string eventName);
SCR_BellSoundComponent calls SoundEvent(eventName) inside a sound component.
SCR_AISettingsComponent overrides OnPostInit(IEntity owner) and calls super.OnPostInit(owner).
```

Review findings:

```text
1. High: `Start()` is not a verified Reforger `ScriptComponent` lifecycle callback. Current generated API exposes `OnPostInit(IEntity owner)` for this use case. Use `override void OnPostInit(IEntity owner)` and call `super.OnPostInit(owner)`.

2. High: `GetComponent<SoundComponent>()` is a Unity-style guess. Current `IEntity` lookup exposes `FindComponent(typename typeName)`, returning `Managed`. Use the owner passed into `OnPostInit` and cast: `SoundComponent.Cast(owner.FindComponent(SoundComponent))`.

3. High: `SoundComponent.Play(...)` is not found. Current generated API exposes `SoundComponent.SoundEvent(string eventName)`, and the handwritten bell sound component uses `SoundEvent(eventName)`.

4. Medium: the patch does not guard missing components or empty event names. Null guards are needed because query output proves API shape, not prefab wiring.

5. Verification required: confirm the owning prefab/entity has a `SoundComponent`, the sound event exists in audio resources, and the behavior is tested in Workbench/runtime.
```

Corrected minimal shape:

```c
class TAG_GoodSoundComponentClass : ScriptComponentClass
{
}

class TAG_GoodSoundComponent : ScriptComponent
{
	[Attribute("", UIWidgets.EditBox, "Sound event name")]
	protected string m_sSoundEvent;

	protected SoundComponent m_SoundComponent;

	override void OnPostInit(IEntity owner)
	{
		super.OnPostInit(owner);

		if (owner)
			m_SoundComponent = SoundComponent.Cast(owner.FindComponent(SoundComponent));
	}

	AudioHandle PlayConfiguredSound()
	{
		if (!m_SoundComponent || m_sSoundEvent.IsEmpty())
			return AudioHandle.Invalid;

		return m_SoundComponent.SoundEvent(m_sSoundEvent);
	}
}
```

Residual verification: Script Editor validation and runtime audio-resource validation remain; the review proves the proposed patch used unverified/wrong APIs and identifies the current source-backed replacements.

## Score Summary

Category averages:

| Category | Average | Critical | Result | Notes |
| --- | ---: | --- | --- | --- |
| Category 1: Source And Data Status | 5.00 | yes | pass | Raw game data, manifests, wiki index, references, and skill are present and countable. |
| Category 2: Game-Data Updater And Manifest | 5.00 | yes | pass | Updater help/check works; raw folder cleanup contract holds; runtime command matches. |
| Category 3: Game-Data Index And Search Usefulness | 5.00 | yes | pass | Exact API, examples, snippets, validator, and usefulness benchmark pass. |
| Category 4: Wiki Index And Source Coverage Signals | 4.83 | no | pass | Wiki index is rich; related-topic routing remains a little broad. |
| Category 5: Runtime Reference Coverage And Quality | 4.86 | yes | pass | All 26 references are structured, source-rich, clean, and query-oriented. |
| Category 6: `SKILL.md` Runtime-Boundary Compliance | 5.00 | yes | pass | Runtime boundary, strict MUST rules, routing, search guide, and self-protection are present. |
| Category 7: Cross-Source Codex Task Usefulness | 4.72 | yes | pass | Most tasks route cleanly; editor-heavy/broad tasks still need targeted follow-up searches. |
| Category 8: Examples And Snippet Grounding | 4.80 | yes | pass | Examples are useful and bounded; a few broad example families are noisy. |
| Category 9: Real-World Coding Simulations | 4.80 | yes | pass | 15/15 coding tasks passed; 12/15 scored 5 and 3/15 scored 4. |

Overall category average: `4.78/5`.

Category 9 gate results:

- Average: `4.80/5`, passing the `>= 4.0` requirement.
- Coding tests scoring `4+`: `15/15`, passing the `10/15` requirement.
- Coding tests below `3`: `0`.
- Route-only, placeholder-only, or comment-driven outputs: `0`.
- Coding tests claiming `5` include verified APIs/signatures and enough generated output for human review.

Automatic-fail review:

- Missing `SKILL.md`: no.
- Missing `references/`: no.
- Missing raw game-data or index manifests: no.
- Query script cannot run: no.
- `SKILL.md` routes to forbidden runtime sources: no.
- API-sensitive guidance without query verification: no.
- Exact API output lacks source file/line grounding: no.
- Real-world coding test invented unverified API names: no.
- Real-world coding test skipped required references/search: no.
- Real-world coding test modified forbidden skill/reference/tooling files: no.

Final result: pass.

## Usefulness Summary

Strongest parts:

- The architecture is coherent: runtime `SKILL.md` routes to full references, and exact API work routes through `scripts/query-reforger-data.py`.
- Raw game data and indexes are current enough for exact API lookup and include strong source grounding.
- The generated references are broad, wiki-rich, and have clean ownership boundaries.
- The search tooling is effective for exact symbols/methods/attributes, inheritance, examples, snippets, and common task bundles.
- The stricter coding tests now produce human-reviewable code or findings instead of route-only answers.

Weakest parts:

- Some broad example searches remain noisy, especially `scenario-framework`, `game-mode`, and broad domain terms.
- Some tasks still need deeper follow-up search to choose the best real project insertion point, especially editor/data-heavy tasks where code is not always the first artifact.
- The installed skill copy and repo `SKILL.md` can diverge; the runtime audit here reviewed the repo root skill, while the active installed skill is a separate filesystem copy.
- References are dense. They are useful for Codex, but the quality depends on the skill strictly reading only relevant references in full.

Likely Codex failure modes:

- Using a plausible C#/Unity/Arma 3 API when it skips query verification.
- Treating a broad `files` or `examples` result as API truth instead of opening exact symbols/methods.
- Writing code for an editor/data-driven task before checking the appropriate Workbench/config/prefab workflow.
- Trusting `ShowCustomHint` or similar convenience APIs for production use without reading source warnings.
- Using examples as law rather than implementation guides.

Usefulness judgment:

The current generation is useful enough to move forward. It can guide Codex to source-backed Reforger code for common scripting tasks, and the test loop now exposes weak route-only/code-placeholder answers. The next improvements should refine noisy searches and add a small number of higher-fidelity task benchmarks rather than expanding the architecture.

## Recommended Next Fixes

1. Improve broad example ranking for `scenario-framework`, `game-mode`, and noisy domain terms.
   - Target: `scripts/query-reforger-data.py` and/or indexer topic evidence.
   - Impact: reduces manual recovery when Codex starts from broad task phrases.

2. Add dedicated query/task rules for notifications and Scenario Framework extension tasks.
   - Target: `scripts/query-reforger-data.py`.
   - Impact: avoids unmatched notification lookup and makes Scenario Framework action/task routes more direct.

3. Add a small installed-skill sync/audit note or workflow.
   - Target: future maintenance docs or install process, not runtime `SKILL.md` unless explicitly requested.
   - Impact: prevents confusion between repo `SKILL.md` and the installed skill copy.

4. Add optional search validations for exact APIs used in the 15 coding simulations.
   - Target: `scripts/tests/validate-reforger-search.py` or a new benchmark expansion.
   - Impact: keeps current high-value code-generation anchors from regressing.

5. Consider a dedicated reference/query route for production hints/notifications.
   - Target: `references/game-master-factions-tasks-and-modes.md` and query task map only if future failures repeat.
   - Impact: makes the difference between configured `SCR_HintUIInfo` and debug-only `ShowCustomHint` harder to miss.
