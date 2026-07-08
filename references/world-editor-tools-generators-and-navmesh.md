# World Editor Tools Generators And Navmesh

## When To Read

Read this when a task involves reusable World Editor operation: using editor tools, working with shape/vector/coordinate helper tools, generating roads/rivers/lakes/forests/power lines/walls/prefab placement, brushing objects, managing prefabs in a world, snapping/orienting entities to terrain, or building and validating navmesh.

Do not use this as the owner for terrain foundation setup, Terrain Creation Tool fundamentals, Workbench plugin authoring, generic asset import, Scenario Framework/Game Master authoring, or AI behavior scripting. Route those to their owning references and return here only for World Editor tool/generator/navmesh operations.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: World Editor interface and tool operation, World Editor tools, World Editor generators, object/shape/vector/coordinate workflows, prefab management/generation, snap/orient tooling, and navmesh tool/generation workflows.
- Secondary/cross-reference topics: terrain creation, Workbench plugin authoring, asset import, prefab/config modeling, AI behavior, Scenario Framework, Game Master, diagnostics, and server/runtime validation.

Wiki pages reviewed:
- World Editor - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor - status: covered - reason: primary editor interface, top bar, tool list, hierarchy, viewport, properties, browser, and console source.
- World Editor Tool - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor_Tool - status: covered - reason: primary common World Editor tool setup/API/example source; authoring detail cross-links to Workbench plugin reference.
- World Editor: Road Generator - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Road_Generator - status: covered - reason: primary road generator requirements, prefab, terrain adjustment, road options, and spline setting source.
- World Editor: River Generator - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_River_Generator - status: covered - reason: primary river width, material, clearance, shore wetness, physics, surface, and water offset source.
- World Editor: Lake Generator - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Lake_Generator - status: covered - reason: primary lake material, physics, flattening, OBB, depth, offset, and lake/water settings source.
- World Editor: Forest Generator - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Forest_Generator - status: covered - reason: primary forest obstacle, regeneration, debug, level, cluster, and object-distribution source.
- World Editor: Power Line Generator - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Power_Line_Generator - status: covered - reason: primary power line prefab, pole, clearance, randomisation, material, and debug source.
- World Editor: Powerline Generator Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Powerline_Generator_Tutorial - status: covered - reason: primary junction, main polyline, and secondary polyline procedure source.
- World Editor: Wall Generator - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Wall_Generator - status: covered - reason: primary middle/first/last object, global padding, wall group, placement, and terrain snapping source.
- World Editor: Prefab Generator - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Prefab_Generator - status: covered - reason: primary prefab placement/generation settings source.
- World Editor: Prefab Management Tool - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Prefab_Management_Tool - status: covered - reason: primary clone, suffix, children, and XOB import tool source.
- World Editor: Object Brush Tool - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Object_Brush_Tool - status: covered - reason: primary object brush radius, density, object config, randomization, alignment, obstacle, and area detection source.
- World Editor: Shape Area Tool - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Shape_Area_Tool - status: covered - reason: primary shape creation, conversion, practical-use, limitation, and console-message source.
- World Editor: Parallel Shape Tool - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Parallel_Shape_Tool - status: covered - reason: primary parallel offsets, margins, debug, snapping, use cases, limitations, and tips source.
- World Editor: Vector Tool - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Vector_Tool - status: covered - reason: primary vector/shape point creation, snapping, point management, selection, and generator route source.
- World Editor: Coords Tool - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Coords_Tool - status: covered - reason: primary coordinate navigation, copy, clipboard, history, use case, limitation, and tip source.
- World Editor: Ground Manipulation Tool - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Ground_Manipulation_Tool - status: covered - reason: primary snap/transform/ground-placement tool source.
- World Editor: Rotate Tool - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Rotate_Tool - status: covered - reason: primary rotate shortcut, snap angle, separate rotation, and transform-children source.
- World Editor: Navmesh Tool - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Navmesh_Tool - status: covered - reason: primary navmesh tool interface, rebuild, connect, generate, save, and autosave source.
- World Editor: Navmesh Tool Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Navmesh_Tool_Tutorial - status: covered - reason: primary setup/connect/generate/save procedure source.
- Navmesh Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Navmesh_Tutorial - status: covered - reason: primary navmesh definitions, streaming, creation, modification, regeneration, modding, config override, partial generation, and usage source.
- Snap And Orient Entities To Terrain Plugin - https://community.bistudio.com/wiki/Arma_Reforger:Snap_And_Orient_Entities_To_Terrain_Plugin - status: covered - reason: short routing/source page for terrain snapping/orientation plugin.
- World Editor generator/tool category pages - official category URLs - status: covered - reason: source inventory/routing evidence, not content-heavy workflow owners.
- World Editor: Terrain Creation Tool - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Terrain_Creation_Tool - status: excluded - reason: primary owner is `terrain-creation-and-world-setup.md`; this reference mentions it only as a boundary.
- World Editor: Terrain Preparation Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Terrain_Preparation_Tutorial - status: excluded - reason: primary owner is `terrain-creation-and-world-setup.md`.
- World Editor Plugin - https://community.bistudio.com/wiki/Arma_Reforger:World_Editor_Plugin - status: partial - reason: plugin authoring is owned by `workbench-plugins-and-editor-tools.md`; this reference keeps only tool-operation routing.

Wiki sections covered:
- World Editor > Top Bar, Create/Load/Save World, undo/redo/copy/paste/cut, Play Game, gizmo space, entity filter, parent selection, tool buttons, Hierarchy/Create, Viewport, Object Properties, Tool Properties, Navigation, Resource Browser, Prefab Library, Details Tab, Log Console - coverage: represented as editor operating surface and verification checklist.
- World Editor Tool > Setup, WorldEditorTool API, WorldEditorAPI API, Example - coverage: represented as common source/API route without duplicating plugin authoring.
- Generator pages > Requirements, Prefabs, Options, terrain/shape/path settings, debug settings, randomisation, materials, physics/surface settings, and generation controls - coverage: represented by generator family and settings group.
- Shape/vector/tool pages > main interface, creation/conversion, snapping, offsets, point management, coordinates, transform settings, limitations, console messages, and practical use cases - coverage: represented as reusable tool workflows.
- Navmesh pages > definitions, streaming, creation, modification, full/partial regeneration, current tile/tile range, modding/config override, connect/generate/save, autosave, usage - coverage: represented as navmesh setup/build/validation workflow.

Structured wiki records:
- Tables reviewed/included: World Editor interface/tool lists; generator setting tables/field lists; shape/vector/coords/navmesh tool option lists; navmesh definition/config records where present.
- Procedures reviewed/included: World Editor operation procedures; generator setup/generate/debug flows; powerline tutorial steps; shape/vector/parallel shape creation flows; navmesh setup/connect/generate/save and regeneration flows.
- Admonitions reviewed/included: tool limitation notes, generator requirement caveats, object/terrain snapping caveats, navmesh streaming and regeneration warnings, and partial generation plus modding cautions.
- Code blocks reviewed/included: source/API examples are routed to query commands; runtime reference does not copy source bodies.
- Media reviewed: World Editor/tool screenshots and generator/navmesh media were reviewed as UI evidence; runtime reference does not embed media.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts/query-reforger-data.py files WorldEditor --limit 8`
  - `py -3 scripts/query-reforger-data.py files WorldEditorTool --limit 8`
  - `py -3 scripts/query-reforger-data.py files Navmesh --limit 8`
  - `py -3 scripts/query-reforger-data.py files ObjectBrush --limit 8`
  - `py -3 scripts/query-reforger-data.py files RoadGenerator --limit 8`
  - `py -3 scripts/query-reforger-data.py files ForestGenerator --limit 8`
  - `py -3 scripts/query-reforger-data.py files PrefabGenerator --limit 8`
  - `py -3 scripts/query-reforger-data.py files ShapeTool --limit 8`
  - `py -3 scripts/query-reforger-data.py files LakeGenerator --limit 8`
  - `py -3 scripts/query-reforger-data.py files WallGenerator --limit 8`
  - `py -3 scripts/query-reforger-data.py files PowerLine --limit 8`
  - `py -3 scripts/query-reforger-data.py files CoordsTool --limit 8`
  - `py -3 scripts/query-reforger-data.py files SelectionBrush --limit 8`
- Symbols/methods/attributes verified: `WorldEditor`, `WorldEditorTool`, `WorldEditorIngame`, `EditorEntityIterator`, `SCR_ObjectBrushTool`, `SCR_SelectionBrushTool`, `SCR_CoordsTool`, `MeasureTool`, `SCR_AutoSpawnerTool`, `SCR_RoadGeneratorEntity`, `RoadGeneratorEntity`, `LakeGeneratorEntity`, `WallGeneratorEntity`, `PrefabGeneratorEntity`, `NavmeshCustomLinkComponent`, `NavmeshWorldComponent`, `NavmeshSystem`, `NavmeshGeneratorMain`.
- Examples/snippets reviewed: World Editor module/tool routes, object brush and selection brush routes, generator entity routes, navmesh component/system routes, and sample world/navmesh layout signals.

Samples and source examples:
- Official sample folders reviewed: `SampleMod_Main` as a layout signal for worlds, terrain, layers, and navmesh resources.
- Raw game-source example families reviewed: World Editor tools, object brush/selection brush, generator entity families, navmesh generated component/system files, and Workbench World Editor helper tools surfaced by query.

Coverage gaps:
- Missing, excluded, or intentionally deferred source: terrain foundation workflow, Terrain Creation Tool fundamentals, Workbench plugin authoring, generic asset import, Scenario Framework/Game Master authoring, server hosting, and AI behavior authoring.
- Reason and impact: those are separate workflow owners. This reference preserves World Editor tool/generator/navmesh operation and cross-links related owners instead of duplicating their wiki source detail.

## Wiki Source Coverage

The World Editor wiki family is a practical tool surface. Codex should treat it as an editor workflow source, not as a scripting-only reference. The reference preserves three layers:

- Editor operating layer: World Editor top bar, hierarchy, viewport, object/tool properties, browser/library tabs, details, and log console.
- Tool layer: move/rotate/measure/coords/shape/vector/parallel-shape/ground manipulation/object brush/prefab management operations.
- Generator/navmesh layer: road, river, lake, forest, power line, wall, prefab generation, snap/orient entities, and navmesh generation and validation.

The `World Editor` page owns the practical UI map:
- Top Bar operations include creating/loading/saving worlds, going to the world file, undo/redo, copy/paste/cut, playing the game, toggling gizmo space, entity selection filtering, and selecting parent entities.
- Tool buttons include ground manipulation, move, rotate, scale, vector entity, bounding volume, terrain, navmesh, weather editor, measure, import objects, autotest, polyline area, prefab/generator tools, coords, autospawner, map export, shapefile import, and geographic export.
- Hierarchy/Create surfaces are used for world entity organization and creation.
- Object Properties and Tool Properties are separate inspection/configuration surfaces.
- Viewport navigation, Resource Browser, Prefab Library, Details, and Log Console are normal verification surfaces, not optional UI.

The generator pages are field-heavy. The reference keeps the settings by generator family instead of mixing them into terrain setup:
- Road Generator: requirements, prefab setup, terrain height adjustment, height-map priority, falloff widths, road clearance/width, spline points, closed spline, road type, width, vertical scale, beginning/ending pieces, random seed, force full length, mid-piece sequence, road sort, and material sort bias.
- River Generator: requirements, river width, spline upward offset, reverse flow, material, clearance, shore wetness, physics, surface, physics layer, geometry-as-OBB behavior, minimum depth, and water offset.
- Lake Generator: material name, surface material name, physics layer, reverse point order, flatten by bottom plane, geometry-as-OBB behavior, minimum depth, water surface offset, shore wetness, and lake flag.
- Forest Generator: obstacle avoidance, avoid objects/roads/rivers/power lines/tracks/lakes, regenerate by obstacle changes, seed, partial regeneration, full regeneration, debug print/draw options, tree/entity follow-terrain behavior, forest levels, clusters, outline scale curves, object density fields, circle/strip cluster controls, frequency, and amplitude.
- Power Line Generator: prefab requirements, pole setup, distance, default/start/end/junction poles, yaw rotation for start/end poles, clearance, random pitch/roll controls, powerline material, debug draw, and color.
- Wall Generator: middle/first/last object groups, padding, right/up offsets, global pre/post padding, overshoot, wall groups, exact placement, start-from-end, X-as-forward, rotate-180, very-small-object behavior, debug, and snap-to-terrain.
- Prefab Generator: prefab names, weights, vertices-only generation, distance, shape alignment, X-as-forward, forward flip, right/up/forward offsets, gap, random spacing, Perlin density/distribution/size/frequency/seed/amplitude/offset/throw-away, and debug draw.

The tool pages are workflow-heavy:
- Object Brush Tool owns brush usage, radius, strength, scale/density falloff, override brush, object config, min/max scale, prefab selection, bot distance, random pitch/roll/yaw, prefab offsets, random vertical offset, randomization override, weight, align-to-normal, scale falloff, and obstacle avoidance.
- Shape Area Tool owns creating common shapes, circle/rectangle/star settings, point settings, snap-to-terrain, center-on-position, closing shape, converting existing shapes, use cases, console messages, limitations, and tips.
- Parallel Shape Tool owns margins, offset safety, minimum point distance, debug logs, snap-to-ground, spline usage, child shape creation, symmetrical shapes, duplicate removal, offset direction, road shoulder/river bank/wall use cases, console messages, limitations, and tips.
- Vector Tool owns new shape creation, terrain/anchor snapping, elevation reset, split/merge/reverse/delete/subdivide/select-all, active layer selection, selecting entities in/near shapes, geometry occlusion, far-shape display, and generator routing.
- Coords Tool owns coordinate entry, options, data/history, navigating to manual coordinates, copying current position, navigating from clipboard, bug documentation, collaborative work, recurring test points, console messages, limitations, and tips.
- Ground Manipulation Tool owns snap horizontal/vertical/rotation, transform specs, separate snap/rotate, keep elevation, negative elevation, transform children, snap to ground, and physics placement.
- Rotate Tool owns shortcuts, snap angle, separate rotation, and transforming children.

Navmesh pages preserve both tool use and runtime correctness:
- Navmesh Tutorial defines navmesh streaming, creation, modification, full/partial regeneration, current tile, tile range, modding, config override, partial generation, and usage.
- Navmesh Tool owns show/vertical offset, rebuild tile, rebuild/regenerate changed tiles, connect/disconnect, generate/stop generation, autosave when done, save, and save as.
- Navmesh Tool Tutorial owns the setup/connect/generate/save sequence.

## Terms And Concepts

- World Editor: Workbench module used to create, edit, inspect, and validate world/entity content.
- World Editor Tool: editor tool surface that operates inside World Editor. Exact script/API names must be checked by query before code changes.
- Tool Properties: per-tool configuration panel. Do not confuse it with selected entity Object Properties.
- Object Properties: selected entity/property inspection and edit surface.
- Resource Browser / Prefab Library: World Editor asset/prefab lookup surfaces.
- Shape: editor geometry used by tools and generators to define paths, areas, offsets, and placement controls.
- Vector Tool: shape/point authoring tool used as input for generator and area workflows.
- Shape Area Tool: helper for creating common shape areas and converting shapes.
- Parallel Shape Tool: helper for deriving offset/parallel shapes for shoulders, banks, walls, and similar layout tasks.
- Coords Tool: coordinate navigation/history/copy tool for repeatable locations, collaboration, bug docs, and test points.
- Object Brush: brush-based prefab/object placement tool with density, randomization, alignment, and obstacle filters.
- Generator: world placement/content tool that derives roads, rivers, lakes, forests, power lines, walls, or prefab placement from shapes/settings.
- Navmesh: navigation mesh data used by AI/navigation systems. Navmesh workflow includes tool connection, generation, saving, streaming/modding concerns, and runtime validation.
- Navmesh streaming: navmesh loading behavior that affects runtime and server/client validation.
- Current tile / tile range: navmesh generation and editing scope controls.
- Snap to terrain: editor behavior that places/orients entities against terrain; verify tool-specific settings rather than assuming every tool uses the same snapping behavior.

## Workbench / Resource / Data Surfaces

World Editor surfaces:
- Top Bar: file/world actions, undo/redo/edit actions, play, gizmo space, selection controls, and tool launch buttons.
- Hierarchy/Create: entity organization and creation.
- Viewport: visual editing and navigation.
- Object Properties: selected object data and transformation.
- Tool Properties: active tool/generator settings.
- Resource Browser: resource lookup.
- Prefab Library: prefab lookup and placement.
- Details Tab: selected object/resource details.
- Log Console: tool messages, warnings, and validation output.

Generator and tool surfaces:
- Shape/vector surfaces feed road, river, lake, forest, power line, wall, and prefab generator workflows.
- Object Brush and Selection Brush-style tools operate directly on world placement and selections.
- Prefab Management and Prefab Generator affect prefab instances/placement; generic prefab/config modeling remains owned by `prefabs-configs-containers-and-catalogs.md`.
- Navmesh Tool and Navmesh Generator surfaces affect generated navmesh resources and runtime navigation behavior.

Split boundaries:
- Terrain entity creation, heightmap import, surface masks, terrain sizing, Terrain Creation Tool fundamentals, and 2D map creation stay in `terrain-creation-and-world-setup.md`.
- Workbench plugin classes, plugin attributes, CLI/event plugin execution, and editor plugin authoring stay in `workbench-plugins-and-editor-tools.md`.
- Asset import, model/material/texture/collision/LOD/particle workflows stay in `asset-import-models-materials-and-props.md`.
- AI behavior authoring and AI debug panels stay in `ai-behavior-commanding-and-debug.md`; this reference owns navmesh tool/generation setup.

## Required Workflows

World Editor operating workflow:
1. Open or create the world from the World Editor surface.
2. Confirm the active world/resource, save state, selected entity, and active tool before editing.
3. Use Hierarchy/Create for entity organization and creation.
4. Use Viewport navigation and gizmo space intentionally; verify whether the task needs local/world gizmo behavior.
5. Use Object Properties for selected object data and Tool Properties for active tool settings.
6. Use Resource Browser or Prefab Library for resource/prefab selection.
7. Watch Details and Log Console for validation and tool messages.
8. Save and run/play only after confirming the tool result is stable.

Shape/vector preparation workflow:
1. Create or select the shape/path used by the target generator.
2. Use Vector Tool for point creation, terrain/anchor snapping, elevation reset, point split/merge/reverse/delete/subdivide, active layer filtering, and entity selection by shape.
3. Use Shape Area Tool for common area shapes or converting existing shapes.
4. Use Parallel Shape Tool when the task needs derived shoulders, banks, walls, or offset boundaries.
5. Use Coords Tool for repeatable coordinates, bug locations, recurring test points, and collaborative navigation.
6. Verify snap settings, layer selection, point ordering, and shape closure before running generators.

Road generator workflow:
1. Prepare required road prefabs and a valid spline/shape route.
2. Decide whether the generator should adjust terrain height and set height-map priority/falloff widths.
3. Configure road clearance, road width, road type, spline points, closed spline behavior, vertical scale, beginning/ending pieces, random seed, and mid-piece sequence.
4. Generate the road, inspect terrain/mesh transition, and validate road sorting/material sorting.
5. Route terrain height/surface defects back to terrain foundation only when the generator output shows a terrain-data issue.

River and lake generator workflow:
1. Prepare shape/spline and material/physics inputs.
2. Configure river width or lake material/surface material, flow/order behavior, geometry-as-OBB, depth, water offset, shore wetness, clearance, and physics layer.
3. Generate and inspect water placement, shore blending, collision/physics expectations, and terrain intersection.
4. Validate in editor and runtime when water affects traversal, AI, mission routes, or visual presentation.

Forest generator workflow:
1. Define the forest area/shape and obstacle rules.
2. Configure obstacle avoidance for objects, roads, rivers, power lines, tracks, and lakes.
3. Configure regeneration behavior, seed, full/partial regeneration, debug output, and follow-terrain behavior.
4. Configure forest levels, clusters, outline scale curves, object density fields, and cluster types.
5. Generate, inspect density/performance, verify obstacle avoidance, and rerun with debug shapes if needed.

Power line generator workflow:
1. Prepare main and secondary polylines where required.
2. Create junctions where the tutorial workflow requires them.
3. Configure pole prefabs, default/start/end/junction poles, distances, yaw rotation, clearance, pitch/roll randomization, and material.
4. Generate and inspect pole orientation, cable/material alignment, terrain clearance, and junction behavior.

Wall generator workflow:
1. Prepare shape/path and wall object groups.
2. Configure middle/first/last object groups, pre/post padding, right/up offsets, overshoot, exact placement, start direction, X-forward behavior, rotation, and terrain snapping.
3. Generate and inspect endpoints, small-object behavior, terrain snapping, and wall group transitions.

Prefab generator and prefab management workflow:
1. Use Prefab Generator when shape-driven prefab placement is the task.
2. Configure prefab names, weights, distance, shape alignment, X-forward/flip, offsets, gap/random spacing, Perlin distribution, and debug draw.
3. Use Prefab Management Tool for clone/suffix/children/XOB import operations.
4. Route data-modeling problems to the prefab/config reference; keep placement/tool behavior here.

Object Brush workflow:
1. Choose brush radius/strength and falloff behavior.
2. Configure object list: prefab, min/max scale, weight, offsets, random pitch/roll/yaw, vertical offset, normal alignment, and randomization override.
3. Configure obstacle avoidance: objects, roads, rivers, power lines, land, ocean, forests, lakes, detection radius/height, and area detection.
4. Paint/place, inspect density and collisions, and verify results in the viewport and runtime if gameplay interaction matters.

Navmesh workflow:
1. Confirm the world and required navmesh resources/components are present.
2. Use Navmesh Tool setup, connect, generate, and save sequence.
3. Use show/vertical offset to inspect the mesh.
4. Use rebuild tile or rebuild/regenerate changed tiles for targeted edits; use full regeneration only when needed.
5. Use current tile and tile range controls when limiting generation scope.
6. Save or Save As after generation; use autosave only when appropriate.
7. Validate navmesh streaming, partial generation, config override behavior, and runtime AI traversal.

## Configuration Fields And Tables

World Editor interface fields/surfaces:
- Top Bar actions: create/load/save world, go to world file, undo/redo, copy/paste/cut, play game, toggle gizmo space, entity selection filter, select parent entities.
- Panels: Hierarchy/Create, Viewport, Object Properties, Tool Properties, Resource Browser, Prefab Library, Details Tab, Log Console.

Road Generator settings:
- Requirements and prefabs.
- Terrain: adjust height map, adjust height map priority, falloff start width, road falloff width.
- Road: generate road, road clearance, road width.
- Road Options: spline points, closed spline, type, width, V scale, beginning piece, ending piece, random seed, force full length, mid-piece sequence, road sort, material sort bias.

River/Lake settings:
- River: width, spline offset up, reverse flow, material, clearance, shore wetness, physics/surface, physics layer, geometry as OBB, minimum depth, water offset.
- Lake: material name, surface material name, physics layer, reverse point order, flatten by bottom plane, geometry as OBB, minimum depth, water surface offset, shore wetness, lake flag.

Forest Generator settings:
- Obstacles: avoid objects, roads, rivers, power lines, tracks, and lakes.
- Generation: seed, partial regeneration, regenerate entire forest.
- Debug: print area, print entity count, print performance details, draw debug shapes, draw debug obstacle/rectangulation/regeneration shapes.
- Forest/levels/clusters: global outline scale curve/distance, top/bottom/outline levels, circle/strip clusters, min/max density, offsets, frequency, amplitude.

Power Line Generator settings:
- Prefabs and pole setup: distance, default/start/end/default junction pole, yaw rotation for start/end pole.
- Clearance and randomisation: pitch/roll angles, both-side pitch/roll, per-pole pitch/roll application.
- Power lines: material, debug draw, color.

Wall Generator settings:
- Middle/first/last object groups: object choice, vertex-only behavior, pre/post padding, right/up offsets.
- Global: pre/post padding, overshoot, offset right/up, wall groups.
- Other: pre-pad first, exact placement, start from end, use X as forward, rotate 180, use for very small objects, debug, snap to terrain.

Prefab/Object placement settings:
- Prefab Generator: prefab names, weights, only to vertices, distance, align with shape, use X as forward, flip forward, offsets, gap, random spacing, Perlin density/threshold/distribution/size/frequency/seed/amplitude/offset/throw-away, debug draw.
- Object Brush: radius, strength, scale/density falloff, subarea count, object config, prefab, min/max scale, bot distance, random angles, vertical offsets, weight, align to normal, obstacles and area detection.

Shape/navigation tool settings:
- Shape Area: shape type, width/length, circle segments, rectangle segments per side, star branch count, star inner radius ratio, snap to terrain, centre on position, shape closing.
- Parallel Shape: offset safety margin, min point distance, debug log, snap to ground, spline usage, create as child, symmetrical shape, duplicate removal, offset direction.
- Vector Tool: terrain/anchor snapping, reset elevation, split/merge/reverse/delete/subdivide/select all, anchor snap distance, tangent mode, gizmo mode, clone point data, active layer, shape/entity selection.
- Coords Tool: coordinates, options, data/history, manual navigation, current position copy, clipboard navigation.
- Ground Manipulation: horizontal/vertical/rotation snapping, transform specs, separate snap/rotation, keep elevation, negative elevation, transform children, snap to ground, physics placement.
- Rotate Tool: snap angle, rotate separately, transform children.

Navmesh settings:
- Show and vertical offset.
- Rebuild tile.
- Rebuild/regenerate changed tiles.
- Connect/disconnect.
- Generate and stop generation.
- Autosave when done.
- Save and Save As.
- Full/partial regeneration, current tile, tile range, streaming, config override, and usage.

## Procedures And Ordered Steps

General editor procedure:
1. Open the intended world.
2. Confirm save state, active layer, selected entity, and active tool.
3. Make the smallest tool/generator change needed.
4. Inspect the result in viewport, properties, details, and log console.
5. Save only after the output is correct.
6. Run/play or runtime-test when gameplay, AI, collision, navigation, or mission placement can be affected.

Generator procedure:
1. Prepare required shape/path/resource/prefab inputs.
2. Configure generator-specific field groups before generation.
3. Use debug visualization, logging, and performance options where available.
4. Generate.
5. Inspect output against terrain, collisions, object spacing, material/surface expectations, and runtime behavior.
6. Regenerate only the affected scope when the generator supports partial or changed-area regeneration.

Powerline tutorial procedure:
1. Create junction data where needed.
2. Create or select the main polyline.
3. Create secondary polyline branches where needed.
4. Configure poles/material/randomization and generate.
5. Inspect junctions, pole direction, cable alignment, and clearance.

Shape tool procedure:
1. Use Shape Area Tool for common area creation or conversion.
2. Use Vector Tool to refine points, snapping, layers, and point order.
3. Use Parallel Shape Tool for offset shapes.
4. Use Coords Tool to navigate/reproduce exact positions.
5. Use Ground Manipulation/Rotate tools for placement and transform cleanup.

Navmesh procedure:
1. Prepare world/navmesh inputs.
2. Open Navmesh Tool.
3. Connect.
4. Generate or rebuild the required scope.
5. Inspect with show/vertical offset and tile controls.
6. Save or Save As.
7. Validate runtime navigation and streaming.

## Warnings And Failure Modes

- Do not treat World Editor tool output as source truth until it is saved and validated in the world.
- Do not confuse Tool Properties with Object Properties; generator settings live on the active tool, while selected entities have their own properties.
- Generator output depends on shape/path point order, closure, snapping, active layer, terrain shape, prefab availability, and obstacle settings.
- Terrain Creation Tool and terrain preparation are not owned here. If the issue is heightmap, terrain entity sizing, surface masks, or terrain data, switch to `terrain-creation-and-world-setup.md`.
- Workbench plugin authoring is not owned here. If the task is implementing a new World Editor plugin/tool class, switch to `workbench-plugins-and-editor-tools.md` and then verify API signatures by query.
- Asset import issues are not generator issues. If a prefab/model/material/collision resource is invalid, switch to the asset import or prefab/config reference.
- Road, river, lake, forest, power line, wall, and prefab generators can create large world changes. Prefer scoped regeneration and debug visualizations before broad regeneration.
- Forest and object brush density can create performance and readability problems. Use debug/performance outputs and inspect entity counts.
- Obstacle avoidance settings must be checked deliberately. Avoiding roads/rivers/power lines/lakes/objects/land/ocean is generator-specific and not universal.
- Navmesh generation must be saved and runtime-validated. Visual mesh display in the editor is not enough to prove AI can traverse correctly.
- Navmesh streaming and partial generation can affect runtime behavior. Validate changed tiles and relevant tile ranges.
- Snapping/orientation tools can move large selections or child transforms if settings are wrong. Confirm selection and transform-children behavior before applying.
- Coords/history/clipboard workflows are excellent for bug reproduction, but coordinate systems and active world context must match.

## API Lookup Keys

Use these lookup keys when World Editor work touches script/API/tool implementation or source-backed examples:
- `WorldEditor`
- `WorldEditorTool`
- `WorldEditorIngame`
- `WorldEditorPlugin`
- `EditorEntityIterator`
- `MeasureTool`
- `SCR_CoordsTool`
- `SCR_ObjectBrushTool`
- `SCR_SelectionBrushTool`
- `SCR_ParallelShapeTool`
- `SCR_AutoSpawnerTool`
- `SCR_RoadGeneratorEntity`
- `RoadGeneratorEntity`
- `ForestGeneratorCluster`
- `SCR_ForestGeneratorTreeBase`
- `LakeGeneratorEntity`
- `WallGeneratorEntity`
- `PrefabGeneratorEntity`
- `SCR_PowerlineGeneratorPointData`
- `NavmeshCustomLinkComponent`
- `NavmeshWorldComponent`
- `NavmeshSystem`
- `NavmeshGeneratorMain`

Do not guess exact class names, inheritance, attributes, methods, or file locations from this reference. Use query output before writing API-sensitive World Editor, generator, or navmesh code.

## Game-Data Query Commands

Core World Editor/tool routes:
```powershell
py -3 scripts/query-reforger-data.py files WorldEditor --limit 8
py -3 scripts/query-reforger-data.py files WorldEditorTool --limit 8
py -3 scripts/query-reforger-data.py files ObjectBrush --limit 8
py -3 scripts/query-reforger-data.py files CoordsTool --limit 8
py -3 scripts/query-reforger-data.py files SelectionBrush --limit 8
```

Generator routes:
```powershell
py -3 scripts/query-reforger-data.py files RoadGenerator --limit 8
py -3 scripts/query-reforger-data.py files ForestGenerator --limit 8
py -3 scripts/query-reforger-data.py files PrefabGenerator --limit 8
py -3 scripts/query-reforger-data.py files LakeGenerator --limit 8
py -3 scripts/query-reforger-data.py files WallGenerator --limit 8
py -3 scripts/query-reforger-data.py files PowerLine --limit 8
py -3 scripts/query-reforger-data.py files ShapeTool --limit 8
```

Navmesh routes:
```powershell
py -3 scripts/query-reforger-data.py files Navmesh --limit 8
py -3 scripts/query-reforger-data.py symbol NavmeshWorldComponent --kind class --exact
py -3 scripts/query-reforger-data.py symbol NavmeshCustomLinkComponent --kind class --exact
py -3 scripts/query-reforger-data.py files NavmeshGeneratorMain --limit 8
```

Bounded snippet routes after selecting a result:
```powershell
py -3 scripts/query-reforger-data.py snippet scripts/GameLib/generated/WorkbenchAPI/Modules/WorldEditor.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/WorkbenchGame/WorldEditor/ObjectBrush/SCR_ObjectBrushTool.c --line 1 --context 40
py -3 scripts/query-reforger-data.py snippet scripts/WorkbenchGame/WorldEditor/SCR_SelectionBrushTool.c --line 1 --context 40
py -3 scripts/query-reforger-data.py snippet scripts/Game/Generators/PrefabGeneratorEntity.c --line 1 --context 40
py -3 scripts/query-reforger-data.py snippet scripts/Game/Generators/WallGeneratorEntity.c --line 1 --context 40
py -3 scripts/query-reforger-data.py snippet scripts/Game/generated/AI/NavmeshWorldComponent.c --line 1 --context 30
```

Related ownership routes:
```powershell
py -3 scripts/query-reforger-data.py files Terrain --limit 8
py -3 scripts/query-reforger-data.py files WorkbenchPlugin --limit 8
py -3 scripts/query-reforger-data.py files ResourceManager --limit 8
py -3 scripts/query-reforger-data.py files AI --limit 8
```

## Examples And Samples

Official sample layout signal:
- `SampleMod_Main` includes world, terrain, layer, and navmesh resource families that are useful for layout orientation. Use it to understand project shape and world/navmesh resource presence only; do not copy sample source bodies into references or implementations.

Raw game-source example routes:
- World Editor module route: `files WorldEditor` for `WorldEditor` and core editor module/source routes.
- World Editor tool route: `files WorldEditorTool` for concrete tool classes such as `MeasureTool`, `SCR_CoordsTool`, object brush, autospawner, and destruction/setup tools.
- Object/selection brush route: `files ObjectBrush` and `files SelectionBrush` for brush-based placement and selection tools.
- Generator route: `files RoadGenerator`, `files ForestGenerator`, `files PrefabGenerator`, `files WallGenerator`, `files LakeGenerator`, and `files PowerLine`.
- Navmesh route: `files Navmesh`, exact navmesh component symbol lookups, and `files NavmeshGeneratorMain`.

Example use pattern:
1. Read this reference for the workflow family and split boundaries.
2. Query exact tool/generator/navmesh source records.
3. Open bounded snippets only for the selected query result.
4. Validate in Workbench/World Editor and, for navmesh or gameplay-affecting placement, validate at runtime.

## Follow-Up Keywords

World Editor:
- World Editor
- WorldEditor
- WorldEditorTool
- Hierarchy
- Tool Properties
- Object Properties
- Resource Browser
- Prefab Library
- Log Console
- viewport
- gizmo space
- entity select filter

Tools:
- Coords Tool
- Vector Tool
- Shape Area Tool
- Parallel Shape Tool
- Ground Manipulation Tool
- Rotate Tool
- Object Brush Tool
- Selection Brush
- Snap And Orient Entities To Terrain
- Measure Tool

Generators:
- Road Generator
- River Generator
- Lake Generator
- Forest Generator
- Power Line Generator
- Powerline Generator Tutorial
- Wall Generator
- Prefab Generator
- Prefab Management Tool
- autospawner
- obstacle avoidance
- debug shapes
- partial regeneration

Navmesh:
- Navmesh Tool
- Navmesh Tutorial
- NavmeshWorldComponent
- NavmeshCustomLinkComponent
- NavmeshSystem
- NavmeshGeneratorMain
- navmesh streaming
- current tile
- tile range
- partial generation
- full regeneration
- config override

Cross-reference routes:
- terrain foundation
- Terrain Creation Tool
- Workbench plugin
- asset import
- prefab config
- AI behavior
- Scenario Framework
- Game Master

## Verification

World Editor verification:
- Confirm active world, active layer, selected object, selected shape/path, and active tool before applying a tool action.
- Inspect viewport output, Object Properties, Tool Properties, Details, and Log Console after each significant tool/generator run.
- Save only after generated output is correct.
- Use Play Game/runtime validation when generated content affects traversal, collision, AI, mission routes, or player-facing world layout.

Generator verification:
- Verify required prefabs/resources are valid before generation.
- Verify shape/path point order, closure, snapping, and terrain alignment.
- Use debug visualization, logging, and performance options where available.
- Inspect generator output for collisions, gaps, material/surface alignment, object density, obstacle avoidance, terrain intersections, and endpoint behavior.
- Prefer scoped or partial regeneration where available.

Navmesh verification:
- Verify the navmesh tool can connect before generating.
- Inspect mesh display and vertical offset.
- Rebuild changed tiles or selected tile ranges where possible.
- Save generated navmesh output.
- Validate AI/navigation behavior at runtime, especially when streaming, tile ranges, or partial generation are involved.
- Validate dedicated-server/runtime behavior when mission loading, AI traversal, or navmesh streaming affects multiplayer/server behavior.

Split-boundary verification:
- If terrain entity sizing, heightmap import, terrain surfaces, or 2D map output is the failure point, switch to `terrain-creation-and-world-setup.md`.
- If a tool must be implemented or extended as a plugin, switch to `workbench-plugins-and-editor-tools.md`.
- If a generated prefab/model/material fails because the asset itself is invalid, switch to `asset-import-models-materials-and-props.md` or `prefabs-configs-containers-and-catalogs.md`.
- If AI behavior does not use valid navmesh output correctly, switch to `ai-behavior-commanding-and-debug.md` after navmesh verification passes.

## Official Wiki Links

- World Editor: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor
- World Editor Tool: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor_Tool
- World Editor: Road Generator: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Road_Generator
- World Editor: River Generator: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_River_Generator
- World Editor: Lake Generator: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Lake_Generator
- World Editor: Forest Generator: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Forest_Generator
- World Editor: Power Line Generator: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Power_Line_Generator
- World Editor: Powerline Generator Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Powerline_Generator_Tutorial
- World Editor: Wall Generator: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Wall_Generator
- World Editor: Prefab Generator: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Prefab_Generator
- World Editor: Prefab Management Tool: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Prefab_Management_Tool
- World Editor: Object Brush Tool: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Object_Brush_Tool
- World Editor: Shape Area Tool: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Shape_Area_Tool
- World Editor: Parallel Shape Tool: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Parallel_Shape_Tool
- World Editor: Vector Tool: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Vector_Tool
- World Editor: Coords Tool: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Coords_Tool
- World Editor: Ground Manipulation Tool: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Ground_Manipulation_Tool
- World Editor: Rotate Tool: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Rotate_Tool
- World Editor: Navmesh Tool: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Navmesh_Tool
- World Editor: Navmesh Tool Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:World_Editor:_Navmesh_Tool_Tutorial
- Navmesh Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Navmesh_Tutorial
- Snap And Orient Entities To Terrain Plugin: https://community.bistudio.com/wiki/Arma_Reforger:Snap_And_Orient_Entities_To_Terrain_Plugin
- World Editor Generators category: https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Official_Tools/World_Editor_Generators
- World Editor Tools category: https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Official_Tools/World_Editor_Tools
- World Editor Plugins category: https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Official_Tools/World_Editor_Plugins

## Usefulness Score

Score: 92/100

- Wiki coverage: 29/30. All owned primary World Editor, tool, generator, and navmesh pages are reviewed, named, linked, and represented. One point is reserved because terrain-specific World Editor tool pages are intentionally excluded and routed to `terrain-creation-and-world-setup.md`.
- Operational detail: 14/15. The reference preserves editor surfaces, generator field groups, tool procedures, navmesh workflow, warnings, and verification loops. One point is reserved because exact UI labels can vary by Workbench version and must be validated in editor.
- API lookup usefulness: 14/15. Query commands cover WorldEditor, WorldEditorTool, navmesh, object brush, selection brush, generators, and snippets. One point is reserved because many World Editor tasks are data/editor operations rather than script implementation.
- Example grounding: 9/10. `SampleMod_Main` layout signals and raw game-source routes are included. One point is reserved because official samples are layout evidence only and cannot prove generator correctness.
- Codex task usefulness: 14/15. Codex can route normal World Editor generator/navmesh tasks from workflow to exact query commands and verification without loading broad dumps. One point is reserved because terrain, AI, and asset follow-up tasks intentionally require cross-reference routing.
- Context efficiency: 8/10. Dense field groups and split boundaries avoid duplicate ownership. Two points are reserved because the owned page family is broad and must cover many generator/tool families in one file.
- Verification guidance: 4/5. Workbench, generator, navmesh, runtime, and dedicated-server conditions are covered. One point is reserved because final editor/generator output quality must be visually/runtime validated.

Category-fit check:
- Source family complete: pass; World Editor, tool, generator, shape/vector, object brush, prefab management, snap/orient, and navmesh source families are represented.
- No owned page missing: pass; every owned primary page appears in Source Inventory and Official Wiki Links.
- Split boundary justified: pass; terrain foundation, plugin authoring, asset import, AI behavior, Scenario Framework, Game Master, and server workflows are routed to owning references.
- Cross-links present: pass; related workflow owners are named where task boundaries cross.
- Task route clear: pass; tool/generator/navmesh tasks route to this reference plus query commands and bounded snippets.
- Missed coverage cap: no cap applies. No relevant owned wiki page, field group, procedure, warning, or verification family is omitted without rationale.
