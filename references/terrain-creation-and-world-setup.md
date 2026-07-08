# Terrain Creation And World Setup

## When To Read

Read this when a task involves creating or preparing a terrain/world foundation: planning a new terrain, setting up a world file, sizing a terrain entity, importing height data, preparing terrain rasters and surface masks, setting baseline environment entities, using the Terrain Creation Tool for foundational terrain work, or generating a 2D map from terrain/world data.

Do not use this as the owner for reusable World Editor generators, roads/rivers/lakes/forests/object brush/navmesh workflows, general asset import, Scenario Framework setup, Game Master setup, server hosting, or Workbench plugin authoring. Route those to their owning references.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: terrain creation, new terrain setup, terrain entity definitions, terrain preparation, Terrain Creation Tool fundamentals, and 2D map creation.
- Secondary/cross-reference topics: World Editor generators/navmesh, asset import, Resource Manager file handling, Scenario Framework/Game Master placement, and Workbench plugin/tool extension.

Wiki pages reviewed:
- Terrain Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Terrain_Tutorial - status: covered - reason: primary terrain planning, data, file setup, heightmap, surface mask, layout, population, and final terrain workflow source.
- New Terrain Setup - https://community.bistudio.com/wiki/Arma_Reforger:New_Terrain_Setup - status: covered - reason: primary new-world, terrain entity, environment baseline, and AI setup source.
- World Editor: Terrain Preparation Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Terrain_Preparation_Tutorial - status: covered - reason: primary practical world/terrain/environment preparation workflow source.
- World Editor: Terrain Creation Tool - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Terrain_Creation_Tool - status: covered - reason: primary tool-surface source for terrain foundation actions.
- Terrain: Terrain Entity - https://community.bistudio.com/wiki/Arma_Reforger:Terrain:_Terrain_Entity - status: covered - reason: primary terrain sizing and grid vocabulary source.
- 2D Map Creation - https://community.bistudio.com/wiki/Arma_Reforger:2D_Map_Creation - status: covered - reason: primary generated map geometry, TOPO, raster background, PNG import, and map setup source.

Wiki sections covered:
- Terrain Tutorial > Goals, Vocabulary, Terrain Data, Height Map, ASC Format, Image Format, Rasters, Object Layers, Data Management, Project Planning, Research, Terrain Files Setup, Height Field Import, Surface Mask Setup, Main Usage, Secondary Usage, Import, Normal Map Generation, Order of Operations, Layout, Population, Good Habits, Entities Placement, Vector Tool Practice, Buildings and Structures Placement, Road Network, Forest Generators, Water Bodies, Rivers, Powerlines, Shorelines, Final Details, Roads, Rivers, Light Probes, Satellite Map, Final Words, Recommended Tools - coverage: represented as planning, source-data, setup, import, population, and validation guidance.
- New Terrain Setup > Terrain Setup, Create a New World, Create the Terrain Entity, Environment Setup, Sun, Transformation, Light color properties, Global Light color properties, Global Indirect light modificators, Skybox, Sky Preset, Celestial Bodies, Clouds, Fog, Ocean, Post-Process Effects, Weather, Local Environment Probe, AI Setup - coverage: represented as ordered world/environment setup and caveats.
- World Editor: Terrain Preparation Tutorial > Setup, World, Terrain, Additional Setup, Camera, Sun, Transformation, lighting properties, Skybox, Sky Preset, Planet Preset, Clouds, Ocean, Post-Process Effects, Weather, Local Environment Probe, Suggested Default Prefabs, Sculpting, Heightmap Import, First Editing, Terrain Tool - coverage: represented as practical preparation workflow and baseline prefabs/environment checklist.
- World Editor: Terrain Creation Tool > Manage, Height Map, Satellite Map, Surface Map, Tile Map, Sculpt, Paint, Holes, Info & Diags - coverage: represented as terrain-foundation tool surface, with reusable generator work routed elsewhere.
- Terrain: Terrain Entity > Vertex, Block, Tile, Terrain Grid Size, Grid Cell Size, Terrain Size, Heightmap - coverage: represented as terrain math and sizing vocabulary.
- 2D Map Creation > Generate Map Geometry Data, Generate TOPO, Generate Terrain Rasterization Background Image, Generate TGA, Convert to PNG, Paint.NET, GIMP, Import PNG, Setup - coverage: represented as ordered 2D map workflow.

Structured wiki records:
- Tables reviewed/included: New Terrain Setup environment tables; Terrain Tutorial terrain-data table; Terrain Creation Tool parameter/tool tables; Terrain Preparation environment tables.
- Procedures reviewed/included: 2D map output and import procedures; new terrain setup procedures; terrain file/height field/surface mask procedures; Terrain Creation Tool workflow; terrain preparation setup/import/editing procedure.
- Admonitions reviewed/included: terrain planning and source-data warnings; surface mask and normal-map cautions; environment setup notes; terrain entity sizing limitations; Terrain Creation Tool operational warnings; 2D map image conversion/import notes.
- Code blocks reviewed/included: none required for this reference; exact tool/API behavior routes through query commands.
- Media reviewed: Terrain Creation Tool UI images and 2D map creation media were reviewed as tool-surface evidence; runtime reference does not embed media.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts/query-reforger-data.py files Terrain --limit 8`
  - `py -3 scripts/query-reforger-data.py files WorldEditor --limit 8`
  - `py -3 scripts/query-reforger-data.py files TerrainToolDesc --limit 8`
  - `py -3 scripts/query-reforger-data.py files TerrainImport --limit 8`
  - `py -3 scripts/query-reforger-data.py files TerrainToBlender --limit 8`
- Symbols/methods/attributes verified: `TerrainImportPlugin`, `TerrainExportTool`, `TerrainTile`, `TerrainToolDesc`, `TerrainToolDesc_HeightAdd`, `TerrainToolDesc_HeightExact`, `TerrainToolDesc_HeightNoise`, `TerrainToolDesc_HeightSmooth`, `TerrainToolDesc_HeightUser`, `TerrainToolDesc_LayerAdd`, `WorldEditor`.
- Examples/snippets reviewed: terrain import tool route, Terrain To Blender export route, generated terrain tool descriptor route, and World Editor module/tool routes.

Samples and source examples:
- Official sample folders reviewed: `SampleMod_Main` as layout signal for `Assets`, `Configs`, `Missions`, `Prefabs`, `Terrains`, `UI`, `Worlds`, and project root shape.
- Raw game-source example families reviewed: Workbench terrain import tool, Enfusion Blender terrain export tool, generated terrain tool descriptors, and World Editor tool/module files surfaced by query.

Coverage gaps:
- Missing, excluded, or intentionally deferred source: roads, rivers, lakes, forests, object brush, powerline/wall generators, navmesh, and broad World Editor tool operation are deferred to `world-editor-tools-generators-and-navmesh.md`.
- Reason and impact: those pages are reusable World Editor workflows rather than terrain foundation setup. This reference keeps the terrain setup workflow intact and cross-links generator/navmesh follow-up instead of duplicating ownership.

## Wiki Source Coverage

Terrain foundation begins with planning, not tooling. The terrain wiki emphasizes defining project scope, collecting references, deciding the real-world or fictional basis, and understanding the data types before opening the editor. Codex should preserve that order: plan and collect source data first, prepare terrain files second, create/import terrain data third, then populate and validate.

Core wiki coverage preserved here:
- Terrain data types: height maps, raster layers, and object layers are separate inputs with different jobs.
- Height map input: ASC and image-style formats are handled as source height data; import quality depends on scale, precision, and preparing the source data before import.
- Raster data: surface masks, satellite/background imagery, and map imagery are not interchangeable. Surface masks drive terrain material/surface assignment, while satellite or 2D map imagery is visual/reference output.
- Object layers: object placement and generated layers are part of terrain/world population, but reusable generator authoring belongs to the World Editor tool reference.
- Data management: keep source data organized and reproducible; terrain creation involves many generated/intermediate resources.
- Project planning and research: terrain quality depends on research, intended gameplay scale, landmarks, road/water/forest planning, and consistent naming.
- Terrain files setup: create the world/terrain resources and expected folder layout before importing height data or painting surfaces.
- Height field import: import the height field into the terrain entity/tooling, then validate terrain scale, shape, and normals before continuing.
- Surface mask setup: set up the surface mask and surface/material assignment early because later terrain painting and material rebuilds depend on it.
- Order of operations: block out major terrain shape, roads, water, forests, powerlines, shorelines, entities, light probes, satellite/2D map outputs, and final details in a deliberate sequence.
- New terrain/world setup: create a new world, create a terrain entity, set baseline environment entities, then add AI/environment defaults only when relevant.
- Terrain entity sizing: understand grid, cell, block, tile, and heightmap relationships before committing to a terrain scale.
- Terrain Creation Tool: use Manage, Height Map, Satellite Map, Surface Map, Tile Map, Sculpt, Paint, Holes, and Info & Diags as terrain-foundation surfaces.
- 2D map creation: generate map geometry data, generate TOPO, rasterize terrain background, convert image output, import PNG, and complete map setup.

## Terms And Concepts

- Terrain foundation: the terrain/world baseline that must exist before scenario, Game Master, navmesh, generator, or domain content work can be reliable.
- World file: the Workbench world resource that contains the terrain entity, environment entities, and later placed content.
- Terrain entity: the entity that defines the terrain grid, size, heightmap relationship, and terrain data binding.
- Vertex: the terrain sampling point used by the terrain grid.
- Block: a terrain subdivision used by terrain data and tooling. Block-level operations matter for tool diagnostics and surface/height edits.
- Tile: a terrain/map subdivision used by tile-map style operations and tool ownership.
- Terrain grid size: the terrain grid dimension. It participates in the final terrain size calculation.
- Grid cell size: the real-world spacing represented by each terrain grid cell.
- Terrain size: the resulting terrain extent from grid and cell sizing choices.
- Heightmap: terrain elevation source data. Treat it as foundational; changing scale or import assumptions late can invalidate downstream work.
- Raster: image-like terrain data such as surface masks or generated visual backgrounds.
- Surface mask: raster-like data that maps terrain surface/material usage.
- Satellite map: visual terrain/map imagery and workflow output, not a replacement for surface/material setup.
- Object layer: source or generated placement data for objects.
- Local environment probe: environment lighting/reflection baseline used during world setup.
- Suggested default prefabs: baseline world/environment prefabs recommended by the preparation workflow to make a terrain/world usable for editing and validation.
- TOPO: topographic output generated as part of 2D map creation.

## Workbench / Resource / Data Surfaces

Terrain work crosses several Workbench surfaces:
- World Editor: create/open the world, place terrain/environment entities, inspect scene hierarchy, use terrain tools, and validate the world visually.
- Terrain Creation Tool: foundational terrain edit surface with Manage, Height Map, Satellite Map, Surface Map, Tile Map, Sculpt, Paint, Holes, and Info & Diags panels.
- Resource Manager: file/resource visibility and project layout surface. Use the Resource Manager reference for general browsing, options, and file-type behavior.
- Terrain data/resources: heightmaps, surface masks, satellite/map images, terrain entity data, world resources, and generated map outputs.
- Environment setup surfaces: sun, skybox, celestial bodies or planet preset, clouds, fog, ocean, post-process effects, weather, and local environment probe.
- AI setup note: new terrain pages mention AI setup as a world baseline concern, but AI behavior and navmesh authoring route to `ai-behavior-commanding-and-debug.md` and `world-editor-tools-generators-and-navmesh.md`.

Resource ownership boundaries:
- This file owns how terrain/world foundation uses terrain files and environment surfaces.
- `resource-manager-file-types-and-editors.md` owns Resource Manager UI, options, file type distinctions, and editor/plugin surfaces.
- `prefabs-configs-containers-and-catalogs.md` owns generic prefab/config/container/catalog modeling.
- `asset-import-models-materials-and-props.md` owns FBX/model/material/texture/collision/LOD/particle import and asset QA.

## Required Workflows

Terrain planning workflow:
1. Define terrain scope, playable area, performance target, and intended gameplay.
2. Gather references and source data before editor work: height data, maps, imagery, roads, rivers, landmarks, vegetation expectations, and settlement layout.
3. Decide source-data organization and naming before importing.
4. Separate heightmap, surface mask, satellite/reference imagery, object layers, and final 2D map output in the plan.
5. Identify follow-up workflows early: navmesh, roads/rivers/forest generators, asset import, Scenario Framework, Game Master, and server validation.

Terrain files/setup workflow:
1. Create or open the addon/project that will own the terrain resources.
2. Create the world resource and terrain resource structure.
3. Create the terrain entity in the world.
4. Choose terrain grid/cell/heightmap assumptions deliberately before import.
5. Import the height field and validate terrain scale, shape, and orientation.
6. Set up surface masks/material assignments before heavy population.
7. Generate or rebuild normal data when the terrain workflow requires it.
8. Use Terrain Creation Tool diagnostics to confirm block/pixel/surface state before moving into generator-heavy work.

New terrain/world setup workflow:
1. Create a new world.
2. Create the Terrain Entity and bind terrain data.
3. Add baseline environment setup: Sun, skybox or sky preset, celestial bodies/planet preset where applicable, clouds, fog, ocean, post-process effects, weather, and local environment probe.
4. Use suggested default prefabs from the terrain preparation workflow where applicable.
5. Add camera/editor convenience setup for early editing.
6. Perform first sculpting/editing and heightmap import checks.
7. Only after terrain foundation is stable, move into generators, navmesh, scenario content, or domain-specific placement.

Terrain layout/population workflow:
1. Block major landforms and gameplay routes first.
2. Place or plan road networks, rivers, water bodies, forests, powerlines, shorelines, major structures, and landmarks in that order when the terrain plan needs them.
3. Treat roads/rivers/forests/powerlines as cross-reference workflows owned by the World Editor tools/generators reference, while keeping their planning order visible here.
4. Add entities and buildings after major terrain and route shape are stable.
5. Add light probes and final details late.
6. Generate satellite/2D map outputs after terrain layout is stable enough to represent.

2D map workflow:
1. Generate map geometry data.
2. Generate TOPO output.
3. Generate a terrain rasterization background image.
4. Generate TGA output.
5. Convert the generated image to PNG using the image workflow described by the wiki, including Paint.NET or GIMP routes where relevant.
6. Import the PNG into the project.
7. Complete map setup and verify alignment against the terrain/world.

## Configuration Fields And Tables

Terrain entity fields/concepts to preserve:
- Vertex: understand how terrain samples are represented.
- Block: understand terrain subdivision and block-level diagnostics.
- Tile: understand tile-map interactions and tile ownership/release behavior in tooling.
- Terrain Grid Size: choose deliberately because it affects terrain extent and data shape.
- Grid Cell Size: choose deliberately because it affects real-world scale.
- Terrain Size: verify after grid/cell settings instead of assuming the result.
- Heightmap: verify source dimensions, scale, and import behavior before downstream work.

Terrain Creation Tool surfaces:
- Manage: top-level terrain operation surface.
- Height Map: import height map, export height map, rebuild height map, bake selection, and generate normal map.
- Satellite Map: import satellite map for visual/reference terrain imagery.
- Surface Map: fix block border, change surface map size, rebuild terrain materials, and related options.
- Tile Map: minimap controls, scale to fit, center on camera, claim tiles, release tiles, and cogwheel options.
- Sculpt: common values, common controls, sculpt, flatten, smooth, and noise.
- Paint: strength, radius, falloff, angle, brush shape/type, surface layer list, basic painting, and extra surface-layer operations.
- Holes: add/remove hole and enable/disable block.
- Info & Diags: block and pixel-under-cursor diagnostics, block diagnostics, pixel diagnostics, basic surface diagnostics, and surface-layer merge/replace operations.

Environment setup surfaces:
- Sun: transformation, light color properties, global light color properties, and indirect light modifiers.
- Skybox/sky preset and celestial/planet preset: baseline sky and celestial configuration.
- Clouds, fog, ocean, post-process effects, and weather: visual/world baseline, not just decoration.
- Local environment probe: validation point for lighting/reflection baseline.
- AI setup: terrain setup mentions it as a baseline, but navmesh/AI behavior details are owned elsewhere.

2D map surfaces:
- Map geometry data and TOPO generation.
- Terrain rasterization background image.
- TGA output and PNG conversion/import.
- Image editing route through Paint.NET or GIMP when needed.

## Procedures And Ordered Steps

Terrain Tutorial procedure summary:
1. Set goals and vocabulary.
2. Prepare terrain data: height map, rasters, and object layers.
3. Manage source data and project planning.
4. Research the terrain, routes, landmarks, and intended gameplay.
5. Set up terrain files.
6. Import height field data.
7. Set up surface masks and material usage.
8. Generate normal maps when required.
9. Follow an order of operations for layout, population, road/water/forest/powerline/shoreline work, final details, light probes, and satellite map output.
10. Use recommended external tools only as supporting preparation/conversion tools, not as Reforger source authority.

New terrain setup procedure summary:
1. Create a new world.
2. Create the terrain entity.
3. Configure environment baseline in a deliberate sequence: sun, sky/planet/celestial setup, clouds, fog, ocean, post-process, weather, and local environment probe.
4. Add AI setup only after terrain/world baseline exists and route deeper AI/navmesh work to the owning references.

Terrain preparation procedure summary:
1. Create/open the world.
2. Add or configure terrain.
3. Add extra editor baseline such as camera and environment setup.
4. Use suggested default prefabs where applicable.
5. Perform sculpting and heightmap import.
6. Do first editing passes.
7. Use the terrain tool for subsequent terrain foundation edits.

Terrain Creation Tool procedure summary:
1. Use Manage and Height Map operations for import/export/rebuild/bake/normal-map actions.
2. Use Satellite Map and Surface Map operations for visual and surface/material data work.
3. Use Tile Map operations when terrain tile ownership or tile view is relevant.
4. Use Sculpt and Paint tools for terrain shape and surface layers.
5. Use Holes for terrain holes/block enablement.
6. Use Info & Diags before assuming a terrain/surface problem is a script or asset issue.

2D map procedure summary:
1. Generate map geometry data.
2. Generate TOPO.
3. Generate rasterized background.
4. Generate TGA.
5. Convert TGA to PNG.
6. Import PNG.
7. Complete setup and validate against the world.

## Warnings And Failure Modes

- Do not start with scripts or Scenario Framework when the terrain/world foundation is not stable.
- Do not treat heightmap, satellite imagery, surface mask, and 2D map output as the same data. They have different purposes and validation paths.
- Terrain scale is hard to fix late. Verify terrain grid size, grid cell size, terrain size, and heightmap assumptions before population.
- Surface mask and material setup should happen before heavy painting/population. Late surface changes can force rebuilds and rework.
- Imported height data must be checked visually and numerically; wrong scale/orientation causes downstream road, water, navmesh, and map issues.
- Terrain Creation Tool diagnostics should be used before guessing at script/API causes for terrain block, pixel, or surface-layer issues.
- Terrain work can pull in asset, generator, navmesh, scenario, and server topics. Keep the normal task routed to this reference plus one follow-up reference instead of opening many broad files.
- New terrain environment setup is not optional polish. Sun, sky, weather, ocean/fog/post-process, and local environment probe settings affect world validation.
- 2D map image generation requires conversion/import steps and alignment validation. Do not assume the first generated image is ready for runtime use.
- Generator-heavy operations such as forests, roads, rivers, lakes, walls, powerlines, object brush, and navmesh are intentionally not detailed here; use the World Editor tools/generators reference for those workflow controls.
- Asset import/material/model issues belong to the asset pipeline reference unless the defect is specifically terrain raster, terrain surface, or terrain entity setup.

## API Lookup Keys

Use these lookup keys when terrain/world work touches API, editor tooling, or source-backed examples:
- `Terrain`
- `TerrainImportPlugin`
- `TerrainExportTool`
- `TerrainTile`
- `TerrainToolDesc`
- `TerrainToolDesc_HeightAdd`
- `TerrainToolDesc_HeightExact`
- `TerrainToolDesc_HeightNoise`
- `TerrainToolDesc_HeightSmooth`
- `TerrainToolDesc_HeightUser`
- `TerrainToolDesc_LayerAdd`
- `WorldEditor`
- `WorldEditorTool`
- `ResourceManagerPlugin`

Do not guess exact class names, inheritance, attributes, or methods from this reference. Use game-data query output before writing API-sensitive terrain or editor code.

## Game-Data Query Commands

Core terrain/source routes:
```powershell
py -3 scripts/query-reforger-data.py files Terrain --limit 8
py -3 scripts/query-reforger-data.py files WorldEditor --limit 8
py -3 scripts/query-reforger-data.py files TerrainToolDesc --limit 8
py -3 scripts/query-reforger-data.py files TerrainImport --limit 8
py -3 scripts/query-reforger-data.py files TerrainToBlender --limit 8
```

Exact symbol follow-up routes:
```powershell
py -3 scripts/query-reforger-data.py symbol TerrainToolDesc --exact
py -3 scripts/query-reforger-data.py files TerrainImportPlugin --limit 8
py -3 scripts/query-reforger-data.py files TerrainExportTool --limit 8
py -3 scripts/query-reforger-data.py files WorldEditorTool --limit 8
```

Bounded snippet routes after selecting a file from query output:
```powershell
py -3 scripts/query-reforger-data.py snippet scripts/WorkbenchCommon/TerrainImportTool.c --line 1 --context 40
py -3 scripts/query-reforger-data.py snippet scripts/WorkbenchGameCommon/EnfusionBlenderTools/TerrainToBlender.c --line 1 --context 40
py -3 scripts/query-reforger-data.py snippet scripts/Core/generated/WorkbenchAPI/Terrain/TerrainToolDesc.c --line 1 --context 30
```

Related follow-up routes when the terrain task crosses ownership:
```powershell
py -3 scripts/query-reforger-data.py files Navmesh --limit 8
py -3 scripts/query-reforger-data.py files ObjectBrush --limit 8
py -3 scripts/query-reforger-data.py files ResourceManager --limit 8
py -3 scripts/query-reforger-data.py files GameMode --limit 8
```

## Examples And Samples

Official sample layout signal:
- `SampleMod_Main` shows a project shape with world/terrain-adjacent folders such as `Assets`, `Configs`, `Missions`, `Prefabs`, `Terrains`, `UI`, and `Worlds`. Use it as layout evidence only; do not copy sample source bodies into a reference or implementation.

Raw game-source example routes:
- `TerrainImportPlugin` route: use `files TerrainImport` and a bounded snippet to inspect Resource Manager terrain import tooling.
- `TerrainExportTool` / `TerrainTile` route: use `files TerrainToBlender` and a bounded snippet to inspect terrain export/tool behavior.
- `TerrainToolDesc` route: use `files TerrainToolDesc` for generated Terrain Tool descriptor class names and inheritance.
- `WorldEditor` route: use `files WorldEditor` for the generated World Editor module and related editor tool examples.

Example use pattern:
1. Read this reference to understand the terrain/world workflow.
2. Query exact terrain/editor symbols with the commands above.
3. Open bounded snippets only for the selected files and line ranges.
4. Route out to the World Editor generators/navmesh or asset references only when the task actually crosses those boundaries.

## Follow-Up Keywords

Terrain/world setup:
- terrain tutorial
- terrain setup
- new terrain
- terrain entity
- terrain grid size
- grid cell size
- terrain size
- heightmap
- ASC
- surface mask
- raster
- satellite map
- terrain preparation
- Terrain Creation Tool
- TerrainToolDesc
- TerrainImport
- TerrainToBlender
- 2D map
- TOPO

Cross-reference routes:
- road generator
- river generator
- lake generator
- forest generator
- powerline
- shoreline
- object brush
- navmesh
- World Editor tool
- asset import
- Resource Manager
- Scenario Framework
- Game Master
- AI setup

## Verification

Terrain/world foundation verification:
- Open the world in Workbench/World Editor and visually confirm terrain scale, orientation, and baseline environment.
- Confirm terrain entity grid/cell/heightmap settings produce the intended terrain size.
- Verify height field import before adding major content.
- Verify surface mask/material assignment and rebuild terrain materials where the tool workflow requires it.
- Use Terrain Creation Tool Info & Diags for block, pixel-under-cursor, surface, and merge/replace issues.
- Confirm local environment probe and environment settings produce usable lighting and visibility.
- Validate 2D map output against terrain/world alignment after PNG import.
- If adding roads, rivers, forests, powerlines, object brush output, or navmesh, switch to `world-editor-tools-generators-and-navmesh.md` for that workflow and verify there.
- If adding Scenario Framework, Game Master, server, weapon, vehicle, UI, asset, audio, or animation content, switch to the owning reference and keep terrain validation separate.

Residual checks:
- Workbench/editor validation is required for terrain and map output; query output alone cannot prove the terrain is visually correct.
- Runtime validation is required after terrain foundation changes that affect gameplay routes, AI navigation, map display, or scenario placement.
- Dedicated-server validation is required only when terrain/world changes affect runtime mission loading, server scenario setup, or multiplayer traversal.

## Official Wiki Links

- Terrain Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Terrain_Tutorial
- New Terrain Setup: https://community.bistudio.com/wiki/Arma_Reforger:New_Terrain_Setup
- World Editor: Terrain Preparation Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Terrain_Preparation_Tutorial
- World Editor: Terrain Creation Tool: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Terrain_Creation_Tool
- Terrain: Terrain Entity: https://community.bistudio.com/wiki/Arma_Reforger:Terrain:_Terrain_Entity
- 2D Map Creation: https://community.bistudio.com/wiki/Arma_Reforger:2D_Map_Creation

## Usefulness Score

Score: 93/100

- Wiki coverage: 29/30. All six owned primary wiki pages are reviewed, named, linked, and represented. Terrain Tutorial, New Terrain Setup, Terrain Preparation, Terrain Creation Tool, Terrain Entity, and 2D Map Creation sections are covered with procedures, fields, tool surfaces, and warnings. One point is reserved because generator-adjacent details from Terrain Tutorial are intentionally routed to the later World Editor tools/generators reference instead of duplicated here.
- Operational detail: 14/15. The reference preserves planning, data preparation, terrain files, heightmap import, surface mask setup, terrain entity sizing, environment setup, Terrain Creation Tool panels, and 2D map workflow. One point is reserved because exact Workbench UI labels can still vary by version and must be verified in Workbench.
- API lookup usefulness: 14/15. Terrain, WorldEditor, TerrainToolDesc, TerrainImport, and TerrainToBlender routes are included with exact query commands and snippet commands. One point is reserved because terrain tasks are mostly editor/data workflows rather than rich script APIs.
- Example grounding: 9/10. `SampleMod_Main` layout signal and raw game-source routes are included. One point is reserved because official samples are layout evidence only and do not replace Workbench terrain validation.
- Codex task usefulness: 14/15. Codex can plan terrain setup, route exact API/tool lookups, preserve split boundaries, and identify validation steps without broad dumps. One point is reserved for still-needing the companion World Editor generators/navmesh reference for generator-heavy tasks.
- Context efficiency: 9/10. Content is dense and scoped to terrain foundation. Cross-reference boundaries avoid duplicate ownership. One point is reserved because terrain foundation necessarily references several adjacent workflows as follow-up keys.
- Verification guidance: 4/5. Workbench, terrain tool diagnostics, map alignment, runtime, and dedicated-server conditions are covered. One point is reserved because visual terrain validation cannot be proven from text.

Category-fit check:
- Source family complete: pass; all owned terrain foundation pages are represented.
- No owned page missing: pass; every owned primary page appears in Source Inventory and Official Wiki Links.
- Split boundary justified: pass; generators/navmesh, asset import, scenarios, server, and Workbench plugin authoring are routed to owning references.
- Cross-links present: pass; follow-up references are named where workflows leave terrain foundation.
- Task route clear: pass; terrain creation, new terrain setup, terrain entity sizing, heightmap import, surface mask setup, 2D map creation, and terrain tool diagnostics all route through this reference plus bounded query commands.
- Missed coverage cap: no cap applies. No relevant owned wiki page, table, procedure, warning, or field family is omitted without rationale.
