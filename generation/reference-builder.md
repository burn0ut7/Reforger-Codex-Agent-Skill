# Reference Builder Contract

This document defines how future runtime references must be generated for the Reforger Codex skill. It is generation-only. Do not create or edit `SKILL.md` from this document directly, and do not create runtime references in this step.

The references are for Codex, not for human browsing. They must be dense, source-grounded operating guides that let Codex perform Reforger scripting and modding work without guessing.

## Mandatory Read-Before-Reference Rule

Before planning, drafting, reviewing, or editing any individual runtime reference, read this document in full. Then review the relevant wiki index records, game-data query outputs, official samples, and raw game-source examples needed for that reference.

Do not create or revise a reference from memory, from an older generated reference, or from only a page/title list. The reference builder contract is the active instruction source for every reference pass.

## Source Priority

Use sources in this order:

1. Official wiki docs indexed under `generation/wiki-index/`.
2. Current game API and example lookup through `scripts/query-reforger-data.py`.
3. Official samples under `raw/samples/`.
4. Raw game-source examples found through the game-data query tool.

Wiki docs are the highest-value source. Do not compromise wiki coverage to make a reference short. If a wiki page contains concrete workflow steps, field meanings, tables, warnings, editor procedures, or tool behavior, the generated reference must preserve that information in structured form.

Game-data lookup is exact API truth. Any API-sensitive claim must include lookup keys or query commands so Codex can verify exact classes, methods, attributes, signatures, inheritance, examples, and snippets.

Official samples and raw game source are example truth. They show layout and implementation patterns, but do not override wiki workflow rules or current API signatures.

## Reference Generation Workflow

Generate references one file at a time.

For each reference:

1. Re-read this document.
2. Read the owned wiki topics in `generation/wiki-index/topics.json`.
3. Build a source inventory for the reference before drafting.
4. Read all relevant full sections from `generation/wiki-index/sections.jsonl`.
5. Review supporting `tables.jsonl`, `procedures.jsonl`, `admonitions.jsonl`, `code-blocks.jsonl`, `media.jsonl`, and `links.jsonl`.
6. Preserve all relevant wiki facts, ordered steps, warnings, fields, table meanings, tool procedures, and official URLs.
7. Query game data for exact API lookup keys, signatures, inheritance, attributes, examples, and snippets.
8. Review official sample folders and raw game-source examples for pattern grounding.
9. Write the reference using the standard format below.
10. Score the reference with the usefulness rubric and list any missed coverage.
11. Revise and rescore until it reaches at least `85/100` and has no automatic failure condition.

Do not split a wiki category across several references unless there is a real category boundary. If another reference needs the same concept, cross-link or route to the owning reference instead of duplicating ownership.

## Standard Reference Format

Every runtime reference must use this shape:

```md
# <Reference Title>

## When To Read
## Source Inventory
## Wiki Source Coverage
## Terms And Concepts
## Workbench / Resource / Data Surfaces
## Required Workflows
## Configuration Fields And Tables
## Procedures And Ordered Steps
## Warnings And Failure Modes
## API Lookup Keys
## Game-Data Query Commands
## Examples And Samples
## Follow-Up Keywords
## Verification
## Official Wiki Links
## Usefulness Score
```

If a section does not apply, keep the heading and state why it does not apply. Do not silently omit expected categories.

## Source Inventory Requirements

Every generated reference must include a compact `Source Inventory` section. This section is not filler; it is the evidence that the reference was built from the correct sources and that missed coverage was considered.

Use this inventory shape:

```md
## Source Inventory

Wiki ownership:
- Primary wiki topics/categories:
- Secondary/cross-reference topics:

Wiki pages reviewed:
- <Title> - <official URL> - status: covered | partial | excluded - reason:

Wiki sections covered:
- <Page title> > <heading path> - sectionId: <id> - coverage:

Structured wiki records:
- Tables reviewed/included:
- Procedures reviewed/included:
- Admonitions reviewed/included:
- Code blocks reviewed/included:
- Media reviewed:

Game-data/API evidence:
- Queries run:
- Symbols/methods/attributes verified:
- Examples/snippets reviewed:

Samples and source examples:
- Official sample folders reviewed:
- Raw game-source example families reviewed:

Coverage gaps:
- Missing, excluded, or intentionally deferred source:
- Reason and impact:
```

The inventory must name every owned primary wiki page that was reviewed. If an owned page is excluded, the reason must be concrete, such as duplicate alias, unrelated page after full review, or owned by another reference. A vague reason like "not needed" is not acceptable.

## Usefulness Scoring

Each reference must be scored out of `100`. Passing threshold is `85/100`, with no zero-score critical category.

Score categories:

- `Wiki coverage` - 30 points
  - 10 points: all owned primary wiki pages are reviewed and represented, or explicitly excluded with defensible reasons.
  - 7 points: all relevant primary sections are represented with their workflow/detail intact.
  - 5 points: tables, configuration fields, ordered procedures, and checklist-like instructions are preserved where present.
  - 4 points: warnings, notes, requirements, limitations, and failure modes are preserved where present.
  - 2 points: official wiki URLs and provenance links are present.
  - 2 points: coverage gaps and exclusions are listed with impact.
  - Deduct heavily for shallow summaries where wiki sections contain concrete workflow detail.
  - Deduct for missing lower-ranked but relevant pages; topic membership is uncapped and lower-scoring pages may still contain required details.

- `Operational detail` - 15 points
  - Full points require concrete Workbench steps, resource/config/prefab surfaces, field names, workflow order, and editor/tool behavior.
  - Deduct for vague instructions such as "configure the prefab" without naming the surfaces and checks.

- `API lookup usefulness` - 15 points
  - Full points require exact lookup keys and `scripts/query-reforger-data.py` commands for relevant classes, methods, attributes, inheritance, examples, and snippets.
  - Deduct for API-sensitive prose that cannot be verified from game-data lookup.

- `Example grounding` - 10 points
  - Full points require official sample references, raw game-source examples, or explicit no-example rationale.
  - Deduct if examples are generic or not tied to lookup commands.

- `Codex task usefulness` - 15 points
  - Full points require enough detail for Codex to perform common Reforger tasks in the topic without guessing or loading broad dumps.
  - Deduct if the reference does not route from task intent to exact workflow/API/example checks.

- `Context efficiency` - 10 points
  - Full points require dense, navigable content with strong headings and lookup keys.
  - Deduct for unrelated material, duplicated category ownership, raw dumps, or embedded API lists that belong in query output.

- `Verification guidance` - 5 points
  - Full points require concrete residual checks such as Workbench validation, runtime testing, dedicated-server/multiplayer checks, packaging checks, asset import validation, or editor/tool verification.

## Category Fit And Usefulness Checks

Each reference must include a category-fit check inside `Usefulness Score` before it can pass:

- Source family complete: all owned wiki source families are represented or explicitly excluded.
- No owned page missing: every high-value owned page is present in `Source Inventory`.
- Split boundary justified: the reference explains why nearby workflows are owned here or cross-linked elsewhere.
- Cross-links present: closely related but separately owned workflows point to the owning reference.
- Task route clear: common Codex tasks for the reference route to one primary reference plus query commands.

Automatic failure conditions for category balance:

- Reference becomes a broad dump of unrelated workflows.
- Workflow is split so far that one normal task requires several references before Codex can act.
- Utility reference duplicates full wiki source ownership instead of routing.
- Source-heavy workflow family is owned only by a utility reference.

Required task usefulness checks across the final reference set:

- make and wire a script component,
- create a replicated component,
- spawn or load a prefab resource,
- configure a server,
- create a Workbench plugin,
- build Scenario Framework content,
- create weapon or gear behavior,
- configure a vehicle compartment,
- import an asset or prop,
- create animation, audio, or UI behavior.

## Missed Coverage Penalties

Missed wiki coverage is the most serious reference-generation defect. Apply these caps and failures before accepting the numeric score:

- If any owned primary wiki page is not reviewed, maximum total score is `80/100`.
- If any owned primary wiki page is missing from `Source Inventory`, maximum total score is `80/100`.
- If a relevant primary wiki section is not represented, maximum `Wiki coverage` score is `24/30`.
- If a wiki page contains concrete workflow steps and the reference summarizes them without preserving the ordered workflow, maximum `Wiki coverage` score is `20/30`.
- If a wiki page contains relevant tables, field lists, config keys, startup parameters, prefab component surfaces, import settings, or editor option meanings and the reference omits them, maximum `Wiki coverage` score is `20/30`.
- If a warning, requirement, limitation, compatibility note, server/runtime caveat, or failure mode that affects correctness is omitted, maximum total score is `75/100`.
- If the reference cannot explain which relevant wiki records were excluded and why, maximum total score is `82/100`.
- If a detailed wiki workflow is reduced to a shallow paragraph, the reference automatically fails.
- If a reference owns a topic category but leaves meaningful pages to another reference without an explicit cross-reference and ownership note, the reference automatically fails.

These caps stack by taking the lowest applicable cap. A reference cannot pass by scoring well in non-wiki categories while missing important wiki material.

Automatic failure conditions:

- Missing relevant wiki category or page ownership.
- Missing `Source Inventory`.
- Missing owned primary wiki pages from `Source Inventory`.
- Wiki content reduced to shallow summary when the source has concrete workflow detail.
- Missing wiki tables, procedures, warnings, or field/config details without explicit exclusion rationale.
- API-sensitive claims without query commands.
- No official wiki links.
- No examples or explicit no-example rationale.
- Local raw paths in runtime reference output.
- Reference is too broad and should be split by category.
- Reference reads as a human article instead of a Codex operating guide.

A failing reference must be revised and rescored until it reaches `85/100` or higher.

## Category Ownership Rules

Every major wiki topic, category, and high-value page must have one primary runtime reference owner. Secondary references may mention or route to that material, but they must not silently split ownership or duplicate partial versions.

When ownership is ambiguous, choose the reference that owns the primary user workflow:

- Generic entity/component concepts belong to `entities-components-and-lifecycle.md`.
- Domain-specific component pages, such as weapon, sound, vehicle, or Scenario Framework component pages, belong to the narrow domain reference and must not repeat generic component lifecycle rules.
- Script references may show how code interacts with components, but component creation, lifecycle, event masks, activeness, and prefab wiring are owned by `entities-components-and-lifecycle.md`.
- Tool/editor workflows belong to the reference for that tool surface.
- API-only context belongs to the scripting or API reference, but exact signatures still route to query commands.
- Asset setup belongs to the narrowest asset reference, such as weapons, vehicles, animation, audio, UI, or general asset import.
- Runtime deployment belongs to `server-hosting-startup-and-runtime.md`.
- Cross-cutting recipes belong to `common-task-recipes.md`, but only as routing; they do not own source detail.

Each generated reference must document its owned primary topics and secondary cross-reference topics in `Source Inventory`. If a page is intentionally owned elsewhere, name the owning reference.

## Fresh Category Derivation

The reference set must be derived from source evidence, not from `generation/design.md`, old `SKILL.md` routing, or previous reference category names. Future category changes must start from:

- wiki density and ownership signals in `generation/wiki-index/`,
- exact API and example lookup usefulness from `scripts/query-reforger-data.py`,
- official sample coverage under `raw/samples/`,
- raw game-source examples surfaced through query tooling.

Source-heavy wiki families should own references directly when they contain enough concrete workflow detail to justify it. Utility references may route to those owners, but must not become hidden owners of wiki source detail.

## Split And Balance Rules

Use these rules when deciding whether a source family is one reference or several:

- A single very large wiki page may own a reference by itself when it is workflow-dense, such as Scenario Framework, Diag Menu, Assets, or weapon prefab setup.
- A reference family above roughly `180k` wiki markdown characters must be reviewed for splitting.
- Split only at real workflow boundaries, such as project setup vs server runtime, terrain setup vs World Editor generators, or weapon prefab setup vs gear/inventory.
- Do not split one normal Codex task so far that Codex must open several references before it can act.
- Do not merge unrelated high-density workflows just because they share a tool name or wiki topic token.
- Do not create two references that both appear to own the same noun, such as generic components. Rename or narrow categories until ownership is obvious from the filename.
- Utility references must route to source-owning references instead of duplicating full source ownership.

## Reference Targets

The reference targets below replace older category lists. They are source-derived defaults. If later source review shows a concrete missing workflow family, update this section and preserve one primary owner per wiki page.

### `start-here-source-authority.md`

Purpose: first-read routing, source authority, lookup-first behavior, Reforger-specific risk areas, and common terms.

Owned wiki source families:

- Modding and Arma Reforger category pages.
- Getting Started, Data Modding Basics, Directory Structure, Game Identity, Dictionary, Workbench Metadata/Links where they define source hierarchy or project identity.

Split rationale:

- Owns orientation only. It must route to workflow owners instead of repeating their full content.

API/query expectations:

- Explain that exact APIs are never guessed.
- Route broad tasks to `scripts/query-reforger-data.py lookup "<task>"` and the owning reference.

Samples/examples:

- Mention official sample families only as routing signals.

Scoring expectations:

- High `Codex task usefulness` requires clear route from user intent to one primary reference and query command.

### `mod-projects-addons-workshop.md`

Purpose: addon/project setup, `.gproj`, local mod layout, publishing, Workshop, and packaging checks.

Owned wiki source families:

- Mod Project Setup, Mod Publishing Process, Workshop, Development Executables, project identity and packaging-related category pages.

Split rationale:

- Project packaging is distinct from server runtime. Keep startup/server fields in `server-hosting-startup-and-runtime.md`.

API/query expectations:

- `py -3 scripts/query-reforger-data.py files gproj`
- `py -3 scripts/query-reforger-data.py files addon`

Samples/examples:

- Official sample project roots and `.gproj` layouts.

Scoring expectations:

- Automatic failure if addon layout, publishing steps, or packaging validation are shallow.

### `enfusion-language-and-script-editor.md`

Purpose: Enforce/Enfusion syntax, language semantics, Script Editor usage, conventions, and migration gotchas.

Owned wiki source families:

- Enforce Script Syntax, From SQF to Enforce Script, Scripting: Values, Operators, Keywords, Conventions, Best Practices, Config Object where language-level.
- Script Editor pages where the workflow is editing language/script, not plugin development.

Split rationale:

- Language/reference rules are separate from gameplay scripting patterns and component workflows.

API/query expectations:

- `py -3 scripts/query-reforger-data.py attribute Attribute`
- `py -3 scripts/query-reforger-data.py files BaseContainer`
- `py -3 scripts/query-reforger-data.py symbol JsonApi`

Samples/examples:

- `SampleMod_ModdedScript` for language-level examples only.

Scoring expectations:

- High `Operational detail` requires concrete syntax rules, ARC/ref behavior where documented, and editor behavior, not generic programming advice.

### `script-events-actions-and-patterns.md`

Purpose: practical gameplay scripting structure, events, invokers, logging, modded classes, user actions, and reusable script patterns.

Owned wiki source families:

- Scripting Modding, Class Template Example, Scripting Example, Event Handlers, user-action scripting pages, performance guidance where it affects script implementation.

Split rationale:

- Owns script implementation patterns. Component creation, lifecycle, event masks, activeness, and prefab/component wiring belong to `entities-components-and-lifecycle.md`; exact API signatures belong to query output.

API/query expectations:

- `py -3 scripts/query-reforger-data.py symbol ScriptComponent --kind class --exact`
- `py -3 scripts/query-reforger-data.py symbol ScriptComponentClass --kind class --exact`
- `py -3 scripts/query-reforger-data.py inherits ScriptComponent`
- `py -3 scripts/query-reforger-data.py lookup "make a user action"`
- `py -3 scripts/query-reforger-data.py examples component --subtopic script-component`

Samples/examples:

- `SampleMod_ModdedScript`, user-action examples, and script-pattern examples that do not duplicate generic component lifecycle docs.

Scoring expectations:

- High `Codex task usefulness` requires enough detail to write the script side of gameplay behavior without duplicating component lifecycle ownership.

### `api-lookup-and-common-symbols.md`

Purpose: compact API lookup router and common-symbol guide. This is not an API dump.

Owned wiki source families:

- None as primary wiki ownership. It may cite scripting workflow pages as context only.

Split rationale:

- Utility reference. It owns query behavior, not wiki source detail.

API/query expectations:

- Include exact lookup commands for high-frequency anchors: `IEntity`, `FindComponent`, `ScriptComponent`, `ScriptComponentClass`, `ResourceName`, `RplProp`, `RplRpc`, `WorkbenchPlugin`.

Samples/examples:

- Route to query output and `examples-and-sample-patterns.md`.

Scoring expectations:

- Automatic failure if this becomes a broad API dump or owns workflow docs that belong elsewhere.

### `resource-manager-file-types-and-editors.md`

Purpose: Resource Manager, file types, editor surfaces, model/texture/layout editors, options, and data-to-spreadsheet workflows.

Owned wiki source families:

- Resource Manager, Resource Manager: Options, Config Editor, Layout Editor, Model Editor, Texture Editor, Data To Spreadsheet, File Types, Generate Class From Layout Plugin.

Split rationale:

- Owns tool/editor surfaces. Prefab/config data modeling belongs to `prefabs-configs-containers-and-catalogs.md`.

API/query expectations:

- `py -3 scripts/query-reforger-data.py files ResourceManager`
- `py -3 scripts/query-reforger-data.py examples resource-loading --subtopic resource-picker-config`
- `py -3 scripts/query-reforger-data.py examples ui --subtopic ui-layout-resource`

Samples/examples:

- Samples with resources, layouts, textures, model/editor outputs.

Scoring expectations:

- High `Wiki coverage` requires preserving editor option meanings, tables, procedures, and file-type distinctions.

### `prefabs-configs-containers-and-catalogs.md`

Purpose: prefab inheritance, config classes, BaseContainer, ResourceName, catalogs, resource references, and data wiring.

Owned wiki source families:

- Prefabs Basics, Data Modding Basics where data modeling, Create a Config Class, BaseContainer Usage, Entity Catalog, config/resource workflows.

Split rationale:

- Owns data model and prefab/config wiring. Narrow asset-specific prefab setup stays with the narrow reference, such as weapons or vehicles.

API/query expectations:

- `py -3 scripts/query-reforger-data.py symbol ResourceName --exact`
- `py -3 scripts/query-reforger-data.py method Resource Load --exact`
- `py -3 scripts/query-reforger-data.py examples resource-loading --subtopic resource-load`
- `py -3 scripts/query-reforger-data.py examples resource-loading --subtopic spawn-prefab`

Samples/examples:

- `SampleMod_Main`, prefab/config/catalog examples.

Scoring expectations:

- High `Wiki coverage` requires preserving config fields, prefab inheritance/override rules, and editor wiring checks.

### `entities-components-and-lifecycle.md`

Purpose: entity/component model, lifecycle, activeness, component wiring, action contexts, and entity creation.

Owned wiki source families:

- Entity Lifecycle, Entity Activeness, Create an Entity, Create a Component where lifecycle/entity-oriented, BaseDoorComponent, Action Context Setup.

Split rationale:

- Owns entity/component semantics. Script coding patterns stay in `script-events-actions-and-patterns.md`.

API/query expectations:

- `py -3 scripts/query-reforger-data.py symbol IEntity --kind class --exact`
- `py -3 scripts/query-reforger-data.py method IEntity FindComponent --exact`
- `py -3 scripts/query-reforger-data.py symbol GenericEntity --kind class --exact`
- `py -3 scripts/query-reforger-data.py examples component --subtopic lifecycle`

Samples/examples:

- Entity/component examples from official samples and raw game source.

Scoring expectations:

- High `Operational detail` requires lifecycle order, activeness behavior, and prefab/component validation checks.

### `multiplayer-replication-and-authority.md`

Purpose: multiplayer scripting, authority/proxy/owner roles, replication, RPC, JIP, and dedicated-server concerns.

Owned wiki source families:

- Multiplayer Scripting and network-specific runtime pages.
- Audio: Voice over Network only for network behavior; audio system detail remains with audio owner.

Split rationale:

- Networking is small but correctness-critical and should stay isolated from server config and general scripting.

API/query expectations:

- `py -3 scripts/query-reforger-data.py attribute RplProp --exact`
- `py -3 scripts/query-reforger-data.py attribute RplRpc --exact`
- `py -3 scripts/query-reforger-data.py symbol RplComponent --kind class --exact`
- `py -3 scripts/query-reforger-data.py symbol BaseRplComponent --kind class --exact`
- `py -3 scripts/query-reforger-data.py lookup "make a replicated component"`

Samples/examples:

- `scripts/GameLib/replication/RplDocs.c` via query output, replication and RPC examples.

Scoring expectations:

- Automatic failure if authority/proxy/owner distinctions or multiplayer verification are vague.

### `server-hosting-startup-and-runtime.md`

Purpose: Server Config, Startup Parameters, dedicated hosting, server management, RCON/A2S, runtime launch, and server validation.

Owned wiki source families:

- Server Config, Startup Parameters, Server Hosting, Server Management, official server/runtime pages.

Split rationale:

- Startup/server fields are dense enough to own a reference separate from packaging and multiplayer scripting.

API/query expectations:

- `py -3 scripts/query-reforger-data.py files server`
- `py -3 scripts/query-reforger-data.py examples game-mode`

Samples/examples:

- Game-mode/scenario examples only where needed for server startup context.

Scoring expectations:

- Automatic failure if server JSON fields, startup parameters, or dedicated-server validation are shallow.

### `workbench-plugins-and-editor-tools.md`

Purpose: Workbench plugins, editor plugin surfaces, Workbench UI extension points, and editor-only boundaries.

Owned wiki source families:

- Workbench Plugin Tutorial, Workbench Plugin, World Editor Plugin, Resource Manager Plugin, Script Editor Plugin, String Editor Plugin, Workbench Links/Metadata where tool-oriented.

Split rationale:

- Owns extension tooling. Diag/performance belongs to diagnostics; Resource Manager general usage belongs to resource-manager reference.

API/query expectations:

- `py -3 scripts/query-reforger-data.py symbol WorkbenchPlugin --kind class --exact`
- `py -3 scripts/query-reforger-data.py examples workbench-plugin`
- `py -3 scripts/query-reforger-data.py files WorkbenchPlugin`

Samples/examples:

- `SampleMod_WorkbenchPlugin`, raw Workbench plugin examples.

Scoring expectations:

- High `Operational detail` requires registration steps, editor surfaces, and Workbench validation.

### `diagnostics-testing-and-performance.md`

Purpose: Diag Menu, debugging panels, autotests, FPS diagnostics, profiling, script/model performance, and validation loops.

Owned wiki source families:

- Diag Menu, Autotest Framework, FPS Diagnostic Plugin, Script Profiling, Scripting: Performance where diagnostic/performance, Model Performance, relevant debug tutorials.

Split rationale:

- Diag Menu is extremely large and should not be buried inside Workbench/tools or UI.

API/query expectations:

- `py -3 scripts/query-reforger-data.py files Diag`
- `py -3 scripts/query-reforger-data.py files Autotest`
- `py -3 scripts/query-reforger-data.py files Profiling`

Samples/examples:

- Autotest and diagnostics examples if present; otherwise explain no-example rationale.

Scoring expectations:

- Automatic failure if Diag Menu coverage is shallow or treated as a generic debug note.

### `scenario-framework.md`

Purpose: Scenario Framework hierarchy, components, setup, update plugin, debugging, and framework-specific workflows.

Owned wiki source families:

- Scenario Framework, Scenario Framework Setup Tutorial, Scenario Framework Update Plugin.

Split rationale:

- Scenario Framework is a huge standalone workflow and should not be mixed into Game Master/factions.

API/query expectations:

- `py -3 scripts/query-reforger-data.py examples scenario-framework`
- `py -3 scripts/query-reforger-data.py files ScenarioFramework`
- `py -3 scripts/query-reforger-data.py files SCR_ScenarioFramework`

Samples/examples:

- Scenario framework examples from samples and raw game source.

Scoring expectations:

- High `Wiki coverage` requires preserving hierarchy, component roles, setup/update procedures, and debug workflow.

### `game-master-factions-tasks-and-modes.md`

Purpose: Game Master, factions, tasks, game modes, Conflict, Capture & Hold, hints, notifications, and editable entities.

Owned wiki source families:

- Game Master, Faction Creation, Task System Usage, Conflict, Capture & Hold Setup, General Game Mode Setup, Notification Creation, Hint Usage, editable entity/property/tutorial pages.

Split rationale:

- Faction Creation is dense but tightly bound to Game Master/tasks/modes, so keep it here unless future generation proves it needs its own reference.

API/query expectations:

- `py -3 scripts/query-reforger-data.py examples game-mode`
- `py -3 scripts/query-reforger-data.py files GameMode`
- `py -3 scripts/query-reforger-data.py files Faction`
- `py -3 scripts/query-reforger-data.py files Task`

Samples/examples:

- `SampleMod_NewFaction`, game-mode/faction/task examples.

Scoring expectations:

- High `Wiki coverage` requires preserving Faction Creation fields/workflows and task/game-mode setup procedures.

### `terrain-creation-and-world-setup.md`

Purpose: terrain creation, new terrain setup, terrain entity setup, terrain preparation, 2D maps, and world foundation workflow.

Owned wiki source families:

- Terrain Tutorial, New Terrain Setup, World Editor: Terrain Preparation Tutorial, World Editor: Terrain Creation Tool, Terrain: Terrain Entity, 2D Map Creation.

Split rationale:

- Owns world foundation workflow. Reusable World Editor tools/generators belong to the companion world-editor reference.

API/query expectations:

- `py -3 scripts/query-reforger-data.py files Terrain`
- `py -3 scripts/query-reforger-data.py files WorldEditor`

Samples/examples:

- Terrain/world folders in official samples and terrain-related raw examples.

Scoring expectations:

- High `Operational detail` requires ordered terrain setup steps, required resources, and validation checks.

### `world-editor-tools-generators-and-navmesh.md`

Purpose: World Editor tools, generators, roads, rivers, lakes, forests, object/shape tools, prefab generators, and navmesh.

Owned wiki source families:

- World Editor, World Editor Tool, Navmesh Tool and Tutorial, Road/River/Lake/Forest/Power Line/Wall generators, Object Brush, Shape Area, Parallel Shape, Coords, Prefab Management/Generator tools.

Split rationale:

- World Editor tool reference is dense and cross-cutting; terrain setup links here but does not own all tool details.

API/query expectations:

- `py -3 scripts/query-reforger-data.py files WorldEditor`
- `py -3 scripts/query-reforger-data.py files Navmesh`
- `py -3 scripts/query-reforger-data.py examples workbench-plugin --subtopic editor-ui`

Samples/examples:

- World/terrain sample assets and raw editor examples.

Scoring expectations:

- High `Wiki coverage` requires preserving tool-specific procedures and generator settings.

### `asset-import-models-materials-and-props.md`

Purpose: asset import, FBX, Blender tools, props, materials, textures, LOD, collision, particles, model QA, and asset browser integration.

Owned wiki source families:

- Assets, FBX Import, Enfusion Blender Tools, Model Quality Assurance, Prop Creation, Textures, Level Of Detail, Collision Layer, Particle Editor, Asset Browser Mod Integration.

Split rationale:

- The Assets and Prop Creation pages are large enough to justify a focused asset pipeline reference. Weapon/vehicle/audio/animation-specific workflows stay with narrower owners.

API/query expectations:

- `py -3 scripts/query-reforger-data.py files ResourceManager`
- `py -3 scripts/query-reforger-data.py examples resource-loading`

Samples/examples:

- `SampleMod_NewProp`, asset/model folders in official samples.

Scoring expectations:

- High `Wiki coverage` requires preserving import settings, file/resource surfaces, QA checks, and asset validation.

### `weapons-prefabs-attachments-and-firearms.md`

Purpose: weapon creation, prefab configuration, weapon-specific systems, weapon modding, optics, suppressors, collimators, muzzle/ammo/magazine links, and stat modifiers.

Owned wiki source families:

- Weapon Creation, Weapon Creation/Prefab Configuration, Weapon Creation/Asset Preparation, Weapon Modding, Weapon Components, Weapon Optic Creation, Weapon Suppressor Creation, Weapon Collimator Creation, Weapon Stats-Modifing Attachments, Weapon Slots And Bones.

Split rationale:

- Weapon prefab/config content is dense and task-critical enough to own a dedicated reference. `Weapon Components` is owned here only as a weapon-specific wiki page; generic component lifecycle and wiring rules remain owned by `entities-components-and-lifecycle.md`. Character gear/inventory is split to avoid making this a broad equipment dump.

API/query expectations:

- `py -3 scripts/query-reforger-data.py lookup "create weapon script"`
- `py -3 scripts/query-reforger-data.py examples weapon`
- `py -3 scripts/query-reforger-data.py examples weapon --subtopic magazine`
- `py -3 scripts/query-reforger-data.py files Weapon`

Samples/examples:

- `SampleMod_NewWeapon`, `SampleMod_ModdedWeapon`, weapon prefab/config/script folders.

Scoring expectations:

- Automatic failure if weapon prefab fields, weapon-specific component surfaces, or attachment workflows are summarized shallowly.

### `character-gear-inventory-and-arsenal.md`

Purpose: character gear creation, headgear/vest asset and prefab setup, inventory behavior, arsenal/catalog routes, and wearable equipment workflows.

Owned wiki source families:

- Character Gear Creation and subpages, headgear and vest asset preparation/prefab configuration, inventory/arsenal-related workflow pages.

Split rationale:

- Gear and inventory are frequent Codex tasks but should not be buried under weapon setup.

API/query expectations:

- `py -3 scripts/query-reforger-data.py examples inventory --subtopic character-inventory`
- `py -3 scripts/query-reforger-data.py files CharacterInventory`
- `py -3 scripts/query-reforger-data.py files Inventory`

Samples/examples:

- `SampleMod_NewCharacter`, gear folders, inventory examples from raw game source.

Scoring expectations:

- High `Operational detail` requires concrete gear prefab/config fields and inventory validation routes.

### `vehicles-creation-simulation-and-compartments.md`

Purpose: car/vehicle creation, asset preparation, prefab setup, simulation configuration, vehicle modding, wheeled simulation, compartments, and vehicle controls.

Owned wiki source families:

- Car Creation and subpages, Car Modding, Vehicle: Wheeled Simulation, vehicle-specific action/audio overlap where vehicle behavior is primary.

Split rationale:

- Vehicle simulation and compartment setup are distinct enough from generic asset import and should stay together for vehicle tasks.

API/query expectations:

- `py -3 scripts/query-reforger-data.py lookup "vehicle compartment"`
- `py -3 scripts/query-reforger-data.py examples vehicle --subtopic compartment`
- `py -3 scripts/query-reforger-data.py examples vehicle --subtopic vehicle-component`
- `py -3 scripts/query-reforger-data.py files Vehicle`

Samples/examples:

- `SampleMod_NewCar`, `SampleMod_ModdedCar`, vehicle compartment/simulation examples.

Scoring expectations:

- High `Operational detail` requires asset, prefab, simulation, compartment, and Workbench validation surfaces.

### `animation-graphs-weapon-animation-and-export.md`

Purpose: Animation Editor, animation graph/nodes, state machines, procedural animation, templates/instances, export profiles, action commands, and weapon animation workflows.

Owned wiki source families:

- Animation Editor family, Animation Export Profiles, Animation Instances Reference Table, Procedural Animation Editor, Weapon Animation tutorial/setup, character/vehicle action commands.

Split rationale:

- Animation node/reference pages are dense and should not be mixed with general assets or weapons.

API/query expectations:

- `py -3 scripts/query-reforger-data.py lookup "find animation graph examples"`
- `py -3 scripts/query-reforger-data.py examples animation`
- `py -3 scripts/query-reforger-data.py examples animation --subtopic anim-graph`

Samples/examples:

- `SampleMod_AnimationWorkshop`, `SampleMod_CinematicTutorial`, animation sample folders.

Scoring expectations:

- High `Wiki coverage` requires preserving node behavior, reference tables, export workflows, and weapon-animation setup.

### `audio-editor-signals-and-sound-systems.md`

Purpose: Audio Editor, signal editor, audio nodes, sound events/components, signals, music, occlusion, vehicle/weapon audio, and voice/network audio routing.

Owned wiki source families:

- Audio Editor family, Audio: Sound Events, Sound Components, Signals, Occlusion, Music Manager, Technical Fundamentals, Radio Broadcast Manager, SCR_SoundManagerModule, vehicle/building/tree/destruction audio pages.

Split rationale:

- Audio editor and runtime sound systems are dense and task-specific enough to stay separate from general assets.

API/query expectations:

- `py -3 scripts/query-reforger-data.py lookup "play a sound event"`
- `py -3 scripts/query-reforger-data.py examples audio`
- `py -3 scripts/query-reforger-data.py files Sound`

Samples/examples:

- Audio folders in weapon/vehicle samples where present, raw sound component examples.

Scoring expectations:

- High `Operational detail` requires preserving editor nodes, signal workflows, sound event/component setup, and runtime validation.

### `ui-layouts-dialogs-and-menus.md`

Purpose: layout creation, dialog configuration, widgets/tooltips, end screens, commanding menu, UI resources, and HUD/menu examples.

Owned wiki source families:

- Layout Creation, Dialog Configuration Tutorial, Widget Tooltip Setup, End Screen Creation, Commanding Menu Modding, Resource Manager layout editor pages where UI layout is primary.

Split rationale:

- UI should not inherit Diag Menu just because Diag has UI headings; diagnostics owns Diag Menu.

API/query expectations:

- `py -3 scripts/query-reforger-data.py lookup "create HUD widget"`
- `py -3 scripts/query-reforger-data.py examples ui --subtopic hud`
- `py -3 scripts/query-reforger-data.py examples ui --subtopic layout`
- `py -3 scripts/query-reforger-data.py files HUD`

Samples/examples:

- UI/layout folders in official samples and raw HUD/widget examples.

Scoring expectations:

- High `Wiki coverage` requires preserving layout editor and dialog configuration procedures.

### `ai-behavior-commanding-and-debug.md`

Purpose: Behavior Editor, AI debug, behavior nodes, commanding AI workflows, AI validation, and AI-specific source routes.

Owned wiki source families:

- Behavior Editor, Behavior Editor: Nodes, AI Debug Panel Tutorial, Commanding Menu Modding where AI/commanding is primary.

Split rationale:

- Navmesh tool details are owned by `world-editor-tools-generators-and-navmesh.md`; this reference cross-links there for AI navigation setup.

API/query expectations:

- `py -3 scripts/query-reforger-data.py files AI`
- `py -3 scripts/query-reforger-data.py examples ai`
- `py -3 scripts/query-reforger-data.py files Behavior`

Samples/examples:

- AI/behavior examples from samples and raw game source.

Scoring expectations:

- High `Operational detail` requires editor/debug setup and clear navmesh cross-linking.

### `examples-and-sample-patterns.md`

Purpose: official sample map and raw game-source example family router.

Owned wiki source families:

- None by default. Tutorial pages remain owned by their workflow reference; this file links to them.

Split rationale:

- Utility reference. It owns sample/task mapping, not wiki workflow content.

API/query expectations:

- Include example and lookup commands for entity/component lifecycle, script events/actions, replication, resources, Workbench plugins, weapons, inventory, vehicles, animation, audio, UI, AI, game modes, and scenario framework.

Samples/examples:

- All official sample roots: `SampleMod_Main`, `SampleMod_ModdedScript`, `SampleMod_WorkbenchPlugin`, `SampleMod_NewWeapon`, `SampleMod_ModdedWeapon`, `SampleMod_NewCar`, `SampleMod_ModdedCar`, `SampleMod_NewCharacter`, `SampleMod_NewFaction`, `SampleMod_NewProp`, `SampleMod_AnimationWorkshop`, `SampleMod_CinematicTutorial`, `SampleMod_Replacement`.

Scoring expectations:

- High `Example grounding` requires sample-to-task mapping and query commands, without duplicating workflow references.

### `common-task-recipes.md`

Purpose: compact Codex task recipes that route to exactly one primary reference plus query commands and verification notes.

Owned wiki source families:

- None as primary source ownership. This is a router.

Split rationale:

- Utility reference. It should reduce context bloat by routing, not become a condensed duplicate of every workflow.

API/query expectations:

- Include task lookup commands for entity/component lifecycle, script events/actions, replicated behavior, prefab/resource loading, server config, Workbench plugin, Scenario Framework, weapon/gear behavior, vehicle compartment, asset/prop import, animation, audio, and UI.

Samples/examples:

- Route to `examples-and-sample-patterns.md`.

Scoring expectations:

- Automatic failure if a recipe requires opening several broad references before Codex can act.

## Reference Review Loop

After generating each reference, run this review:

1. Re-read this document.
2. Compare `Source Inventory` against `generation/wiki-index/topics.json`, `pages.jsonl`, `sections.jsonl`, and the structured wiki records.
3. Check all owned wiki pages and primary topic sections are represented.
4. Check procedures, tables, warnings, fields, and editor surfaces are preserved.
5. List missed coverage, partial coverage, and exclusions with impact.
6. Check API-sensitive claims have query commands.
7. Check examples and samples are included or explicitly not applicable.
8. Check category fit: source family complete, split boundary justified, related workflow cross-links present, and no utility-reference ownership leak.
9. Check duplicate ownership: no other reference appears to own the same concept, and repeated nouns are narrowed with explicit primary-owner and cross-link language.
10. Check required task usefulness routes where the reference participates.
11. Check the reference is dense, navigable, and Codex-oriented.
12. Apply missed-coverage and category-balance caps/failures before accepting the score.
13. Score all categories out of `100`.
14. Revise and rescore until it passes.

Record the final score in the reference itself under `Usefulness Score`.

## Runtime Safety Rules

Runtime references must not include:

- local absolute paths,
- raw wiki dumps,
- raw HTML,
- broad API dumps,
- uncited copied source bodies,
- instructions to scrape the live wiki,
- claims that exact APIs are valid without game-data lookup.

Runtime references may include official wiki URLs for human follow-up and query commands for Codex lookup.
