# Asset Import Models Materials And Props

## When To Read

Read this when a task involves the general Reforger asset pipeline: importing FBX/model content, using Enfusion Blender Tools, preparing materials and textures, setting collision layers, validating model quality, configuring LODs, creating general props, using the Particle Editor, importing object lists, or registering assets in editor/game asset browsers.

Do not use this as the owner for weapon-specific prefab/component setup, vehicle simulation, character gear/inventory, animation graph authoring, audio event systems, UI layouts, terrain/world setup, generic prefab/config modeling, or Workbench plugin authoring. Route those to their owning references and return here only for the general asset import/model/material/collision/particle pipeline.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: general asset pipeline, FBX import, Enfusion Blender Tools, model quality assurance, prop creation, texture import/settings, LOD, collision layers, Particle Editor, Object Import Tool, and Asset Browser Mod Integration.
- Secondary/cross-reference topics: weapon assets, vehicles, character gear, animation export, audio setup, UI, terrain/world setup, prefab/config modeling, Workbench plugins, Resource Manager usage, and Game Master testing.

Wiki pages reviewed:
- Assets - https://community.bistudio.com/wiki/Arma_Reforger:Assets - status: covered - reason: official vanilla asset catalog and category provenance source; full catalog is not mirrored, but category ownership and follow-up route are preserved.
- FBX Import - https://community.bistudio.com/wiki/Arma_Reforger:FBX_Import - status: covered - reason: primary FBX/model import rules, LOD, collider, material, physics, socket, portal, export, and Workbench import source.
- Enfusion Blender Tools - https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools - status: covered - reason: primary Blender integration, import/export, layer preset, material, memory point, object tool, and QA route source.
- Enfusion Blender Tools: Batch FBX Export - https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Batch_FBX_Export - status: covered - reason: batch export option source.
- Enfusion Blender Tools: Materials Library - https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Materials_Library - status: covered - reason: Blender material library setup/usage source.
- Enfusion Blender Tools: Materials Preview - https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Materials_Preview - status: covered - reason: material import/export/sync/edit/debug channel source.
- Enfusion Blender Tools: Model Quality Assurance - https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Model_Quality_Assurance - status: covered - reason: model QA report, issue, convention, topology, collider, and UV source.
- Enfusion Blender Tools: Objects Tools - https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Objects_Tools - status: covered - reason: object sorting, collider/layer preset, and game material assignment source.
- Enfusion Blender Tools: P3D Conversion - https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_P3D_Conversion - status: covered - reason: P3D import, material conversion, obsolete LOD handling, object renaming, layer preset/material assignment, memory point conversion, and FBX batch conversion source.
- Enfusion Blender Tools: Import/Export ASC Elevation - https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Import/Export_ASC_Elevation - status: partial - reason: terrain/elevation import is cross-reference material; covered only where Blender Tools import/export capability affects general asset tooling.
- Enfusion Blender Tools: Import/Export Animation - https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Import/Export_Animation - status: partial - reason: animation export is owned by `animation-graphs-weapon-animation-and-export.md`; this reference records Blender Tools routing and troubleshooting only.
- Enfusion Blender Tools: MLOD Baking Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_MLOD_Baking_Tutorial - status: covered - reason: asset baking support page.
- Enfusion Blender Tools: Portal Tools - https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Portal_Tools - status: covered - reason: portal and portal volume tooling affects FBX/imported model setup.
- Enfusion Blender Tools: Rig Updater - https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Rig_Updater - status: partial - reason: rig update is animation/character adjacent; this reference preserves asset-tool routing only.
- Enfusion Blender Tools: Skeleton Updater - https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Skeleton_Updater - status: partial - reason: skeleton update is animation/character adjacent; this reference preserves asset-tool routing only.
- Prop Creation - https://community.bistudio.com/wiki/Arma_Reforger:Prop_Creation - status: covered - reason: primary end-to-end general prop tutorial and validation source.
- Textures - https://community.bistudio.com/wiki/Arma_Reforger:Textures - status: covered - reason: primary texture type, import setting, compression/conversion, color space, mip, and preview source.
- Level Of Detail - https://community.bistudio.com/wiki/Arma_Reforger:Level_Of_Detail - status: covered - reason: primary LOD basics, preview/debug, automatic/manual system, transitions, override, and save source.
- Collision Layer - https://community.bistudio.com/wiki/Arma_Reforger:Collision_Layer - status: covered - reason: primary layer setup, layer preset, and interaction matrix source.
- Particle Editor - https://community.bistudio.com/wiki/Arma_Reforger:Particle_Editor - status: covered - reason: primary particle editor interface, panel, preview, emitter, appearance, physics, animation, lifetime, and simulation source.
- Object Import Tool - https://community.bistudio.com/wiki/Arma_Reforger:Object_Import_Tool - status: covered - reason: primary CSV object import format source.
- Asset Browser Mod Integration - https://community.bistudio.com/wiki/Arma_Reforger:Asset_Browser_Mod_Integration - status: covered - reason: primary asset browser registry/config/label/test workflow source.
- Asset and Enfusion Blender Tools category pages - official category URLs - status: covered - reason: source inventory and routing evidence.

Wiki sections covered:
- Assets > US, USSR, FIA, CIV asset category groupings - coverage: represented as official asset catalog ownership and domain cross-reference route.
- FBX Import > General Rules and Habits, Alignment, LODs, Collider shape, Collider Hierarchy, Collider Usage, General Rules, Performance, Restrictions, How To, Static, Dynamic Objects, Avoid Overlaps, layer preset on colliders, physical material, Materials, Center of Mass, Occluders, Probes and Probe Volumes, Portals and BSP Geometry, Sockets, Land Contacts, FBX Export, Import Process in the Workbench - coverage: represented as import rules, field groups, workflows, and warnings.
- Enfusion Blender Tools pages > Features, Import, Export, Installation, Updating, Interface, Top Menu, Import ASC/P3D/FBX, unsupported LOD handling, Layer Presets, Game Materials, material renaming, Memory Points, axis conversion, Model Quality Assurance, Settings, Object Tools, Material Tools, material library/preview, P3D conversion - coverage: represented as Blender Tools workflow and QA source.
- Prop Creation > preparation, structure, cutting parts, sockets, skeleton/rigging, colliders/material names, FBX export settings, textures, import/register model, import settings, physics, prefab creation, variants, procedural animation, user actions, audio, editor integration, asset registration, Game Master/new world testing - coverage: represented as ordered prop pipeline with domain cross-links.
- Textures > source image format, texture types, texture import, import settings, conversion, swizzling, color space, mips, texture properties, preview - coverage: represented as texture workflow and configuration.
- Level Of Detail > basics, preview, debug, automatic system, LOD transitions, manual override, save process - coverage: represented as LOD validation.
- Collision Layer > layer setup, layer preset setup, interaction matrix row setup - coverage: represented as collision setup workflow.
- Particle Editor > interface, effect/preview/emitter panels, preview tools, general emitter fields, particle appearance, physics, texture sheet animation, lifetime/color/size/rotation fields, stress/low-FPS simulation - coverage: represented as particle editor workflow.
- Object Import Tool > CSV file format - coverage: represented as object-import data requirement.
- Asset Browser Mod Integration > structure, register file, config duplication, editor integration, override, registry expansion, asset registration, manual/plugin methods, labels, in-game testing - coverage: represented as asset browser integration workflow.

Structured wiki records:
- Tables reviewed/included: Assets category tables; FBX import tables; Textures import setting/conversion tables; Level Of Detail table; Collision Layer table; Object Import Tool CSV table; Prop Creation table; Enfusion Blender Tools material/object tables.
- Procedures reviewed/included: FBX import/export procedures; Blender Tools installation/update/import/export/material/object/QA procedures; Prop Creation end-to-end procedures; texture import procedure; LOD save process; Particle Editor preview/simulation procedures; Asset Browser Mod Integration workflow.
- Admonitions reviewed/included: FBX restrictions/performance/collider warnings; Blender Tools troubleshooting notes; Prop Creation material/layer/physics failure notes; texture compression/color-space cautions; LOD/particle/collision limitations; asset browser registry/test warnings.
- Code blocks reviewed/included: Object Import Tool CSV example shape and minor tool snippets were reviewed; runtime reference does not copy source bodies.
- Media reviewed: FBX import, Blender Tools, Prop Creation, LOD, Particle Editor, Asset Browser screenshots/media were reviewed as UI evidence; runtime reference does not embed media.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts/query-reforger-data.py files ResourceManager --limit 8`
  - `py -3 scripts/query-reforger-data.py examples resource-loading --limit 8`
  - `py -3 scripts/query-reforger-data.py files Asset --limit 8`
  - `py -3 scripts/query-reforger-data.py files Blender --limit 8`
  - `py -3 scripts/query-reforger-data.py files Particle --limit 8`
  - `py -3 scripts/query-reforger-data.py files ValidateFBX --limit 8`
  - `py -3 scripts/query-reforger-data.py files ResourceImport --limit 8`
  - `py -3 scripts/query-reforger-data.py files ParticleEffectEntity --limit 8`
- Symbols/methods/attributes verified: `ResourceManager`, `ResourceImportPlugin`, `ValidateFBXPlugin`, `AssetLibraryUtils`, `BlenderRestAPI`, `TerrainExportTool`, `ParticleEditor`, `Particles`, `ParticleEffectInfo`, `ParticleEffectEntity`, `ParticleEffectEntityClass`, `ParticleEffectEntitySpawnParams`, `ReplicatedParticleEffectEntity`, `SCR_RepeatingParticleEffectEntity`.
- Examples/snippets reviewed: Resource Manager route, resource-loading examples, Blender Tools helpers, Validate FBX plugin, Resource Import plugin, generated Particle Editor module, particle effect entity/source routes.

Samples and source examples:
- Official sample folders reviewed: `SampleMod_NewProp`, `SampleMod_Main`, plus animation/weapon/vehicle samples only as cross-reference signals.
- Raw game-source example families reviewed: Workbench asset/import validation tools, Enfusion Blender Tools helpers, Resource Manager import plugin, particle entity/effect routes, and resource-loading examples surfaced by query.

Coverage gaps:
- Missing, excluded, or intentionally deferred source: weapon-specific asset and attachment workflows, vehicle-specific creation/simulation, character gear/inventory, animation graph/export authoring, audio editor/sound systems, UI layout implementation, terrain setup, generic prefab/config modeling, and Workbench plugin authoring.
- Reason and impact: those are separate workflow owners. This reference preserves the general asset pipeline and cross-links domain-specific owners instead of duplicating their source detail.

## Wiki Source Coverage

This reference owns the general asset pipeline from external DCC/source content to a validated Reforger resource. Codex should treat wiki workflow order as the main source of truth: prepare source files, validate FBX/model rules, import through Workbench/Resource Manager surfaces, configure textures/materials/collision/LOD, build prefab or asset browser registration when needed, then validate in Workbench and runtime.

The `Assets` page is a large official catalog, not a tutorial. It groups vanilla asset references by faction and family, including US, USSR, FIA, and CIV categories with character, group, vehicle, weapon tripod, and similar category groupings. This reference does not mirror the full catalog. Use the official link for human provenance and use domain references for weapon, vehicle, character, and faction-specific usage.

FBX Import coverage:
- General rules and habits come before import. Alignment, scale, LOD names, collider naming, collider hierarchy, and material naming must be correct in source files.
- LODs are part of the model import contract, not a later polish pass. Validate LOD transition behavior and save process with the LOD workflow.
- Collider shape, hierarchy, usage, restrictions, performance, overlap avoidance, layer presets, and physical material/game material assignment affect runtime correctness.
- Static and dynamic object import differs. Buildings/infrastructure/trees and dynamic objects have different expectations.
- Center of mass, occluders, probes/probe volumes, portals, BSP geometry, sockets, and land contacts are import-time considerations.
- FBX export and Workbench import are the handoff from DCC to Resource Manager/Workbench resources.

Enfusion Blender Tools coverage:
- The tools provide Blender-side import/export and preparation utilities for Reforger assets.
- Installation and updating must be kept in sync with the expected tool version.
- Interface coverage includes top menu and side section tool surfaces.
- Import routes include ASC, P3D, FBX, unsupported LOD discarding, layer presets, game materials, material renaming, memory points, and axis-to-single-point conversion.
- Export routes include ASC, TXA, FBX batch export, and related object/material tooling.
- Materials Library and Materials Preview support material import/export, FBX export, material export, synchronization, editing, and debug channels.
- Model Quality Assurance surfaces issues around conventions, non-Enfusion data, mesh topology, short edges, small faces, UCX colliders, and UVs.
- Objects Tools cover automatic sorting, collider/layer preset setup, assigning layer presets, and assigning game material.
- P3D Conversion covers installation, related settings/parameters, material conversion table, P3D import interface, imported content overview, obsolete LOD discarding, object renaming, layer presets/game materials, memory point axis conversion, and FBX batch conversion.
- Portal Tools, Rig Updater, Skeleton Updater, animation import/export, and ASC elevation pages are represented as asset-tool routes but domain behavior belongs to terrain or animation references when the task is terrain/animation-specific.

Prop Creation coverage:
- The prop tutorial is an end-to-end workflow: goals, preparation, structure, cutting objects into parts, sockets, skeleton/rigging, colliders/material names, FBX export settings, texture preparation, model import/registration, import settings, physics setup, troubleshooting, prefab creation, variants, procedural animation, scripted actions, sounds, editor integration, asset registration, and testing.
- Cross-domain steps in the prop tutorial are not ignored. They are preserved as handoff points:
  - procedural animation routes to the animation reference;
  - sound routes to the audio reference;
  - scripted user actions route to script/action references;
  - prefab creation routes to prefab/config modeling when the task becomes data modeling;
  - Game Master testing routes to the Game Master reference.

Texture coverage:
- Source image format and texture types matter before import.
- Texture types include base color, roughness, metalness, normal, opacity, height, masks, global mask, detail mask, normal mask, camo mask, ambient occlusion, cavity, global/macro textures, emissive, and environment cube maps.
- Import settings include format compression, compression threshold, mips removal, max size, conversion type, conversion quality, original pixel bit depth, swizzling, color space, contains/generate mips, mip map function/filter, tiled texture, volume texture, cube map generation, texture properties, and preview.
- Color space and mip settings are correctness/performance decisions, not cosmetic details.

LOD, collision, particle, and asset browser coverage:
- Level Of Detail covers basics, preview, debug, automatic system, LOD transitions, manual override, and save process.
- Collision Layer covers layer setup, layer preset setup, and interaction matrix row setup.
- Particle Editor covers the editor interface, effect panel, preview panel, emitter panel, preview controls, emitter fields, appearance, physics, texture sheet animation, lifetime, color/size/rotation behaviors, stress testing, and low-FPS simulation.
- Object Import Tool covers CSV file format for importing object lists.
- Asset Browser Mod Integration covers asset structure, register/config creation, config duplication, editor integration, override behavior, registry expansion, asset registration, manual method, plugin method, labels, and in-game testing.

## Terms And Concepts

- Asset pipeline: the full route from source content to validated Reforger resource/prefab/editor-visible asset.
- Source model: external DCC content prepared before Workbench import.
- FBX import: model import workflow with alignment, LOD, collider, material, socket, probe, portal, and Workbench import requirements.
- Enfusion Blender Tools: Blender integration package for import/export, material/object tools, P3D conversion, model QA, and related helpers.
- Game material: material assignment used by engine/game systems; do not treat it as only a visual material.
- Physical material: material/collision behavior data that affects physical interaction.
- Layer preset: collision/layer classification assigned to colliders.
- Interaction matrix: collision relationship setup between layer presets.
- UCX collider: collider convention surfaced by model QA and FBX/collider workflows.
- LOD: level-of-detail resource behavior for model performance and transitions.
- Mips: texture mipmap data. Mip creation, removal, and filtering affect rendering quality and performance.
- Swizzling: texture channel mapping behavior.
- Color space: texture import setting such as sRGB/linear treatment; incorrect settings can break visual output.
- Particle effect: visual effect resource/entity using Particle Editor data and particle effect entity routes.
- Asset browser integration: registry/config workflow that makes assets visible and categorized in editor/game asset browser contexts.
- Prop: general placeable object pipeline. Weapon/vehicle/gear-specific assets are separate domain workflows.

## Workbench / Resource / Data Surfaces

Workbench and Resource Manager surfaces:
- Resource Manager: resource visibility, import routes, file-type handling, generated resources, and editor integrations.
- Import settings: per-resource import configuration for models/textures and related resources.
- Model/texture/material editors: validation and preview surfaces for imported assets.
- Particle Editor: effect editing and simulation/preview surface.
- Asset Browser: editor/game registration target for placeable or browsable assets.
- World Editor/Game Master/new world test surfaces: final validation contexts for placeable assets and props.

Source/DCC surfaces:
- Blender with Enfusion Blender Tools installed.
- FBX export settings from the DCC pipeline.
- P3D conversion tooling where older source content is involved.
- Materials library/preview and material synchronization/editing surfaces.
- Model QA report window and issue reporting.

Data/resource surfaces:
- FBX/model resource outputs.
- Texture resources and imported texture properties.
- Material resources and game material assignments.
- Collider/layer preset data.
- LOD data and save output.
- Particle effect resources/entities.
- Asset browser registry/config/label data.
- Prefab resources for placeable props. Generic prefab modeling is owned by `prefabs-configs-containers-and-catalogs.md`.

## Required Workflows

General asset import workflow:
1. Identify whether the task is a general asset, weapon, vehicle, character gear, animation, audio, UI, or terrain workflow.
2. If it is general asset/prop/model/material/texture/collision/particle work, use this reference.
3. Prepare source model and texture files before Workbench import.
4. Validate FBX naming, alignment, scale, LODs, collider hierarchy, material names, sockets, portals, probes, and land contacts.
5. Use Enfusion Blender Tools for Blender-side import/export, material/object tools, model QA, and conversion support.
6. Import through Workbench/Resource Manager.
7. Configure import settings, materials, game materials, physical materials, layer presets, textures, mips, color space, and LOD behavior.
8. Create prefabs or asset browser registration only after imported resources are valid.
9. Validate in editor and runtime.

FBX import workflow:
1. Prepare source model with correct alignment, scale, hierarchy, object names, material names, LODs, colliders, sockets, occluders/probes/portals if needed, and land contacts where relevant.
2. Apply collider shape and hierarchy rules.
3. Assign layer preset and physical/game material data.
4. Avoid collider overlaps and performance-heavy layouts.
5. Export FBX using the documented source-tool settings.
6. Import in Workbench and inspect import settings.
7. Fix model/material/collider/LOD warnings before building gameplay data on top.

Enfusion Blender Tools workflow:
1. Install or update the tools as documented.
2. Use Import surfaces for ASC, P3D, and FBX when applicable.
3. Use layer preset and game material helpers to prepare objects.
4. Use memory point and axis conversion helpers where source content requires them.
5. Use Materials Library/Preview for material setup, synchronization, editing, and debug channels.
6. Use Model Quality Assurance before Workbench import or before accepting an imported model.
7. Use P3D conversion only when the source pipeline requires it, then re-validate converted FBX/model output.

Prop Creation workflow:
1. Establish tutorial goal and project structure.
2. Cut the object into the required parts.
3. Add sockets.
4. Set skeleton and rigging mesh when required.
5. Prepare colliders and material names.
6. Set FBX export settings.
7. Prepare textures.
8. Import and register the new model.
9. Configure import settings and physics.
10. Resolve common failures such as empty geometry parameters, wrong game material, wrong layer preset, or wrong import parameters.
11. Create base prefab, smaller part prefabs, and prop variants.
12. Add procedural animation, scripted action, or sound only as cross-reference handoffs to their owning references.
13. Integrate with editor/asset browser: placeable entity, preview images, display name, localization table, strings, labels, and registration.
14. Test result, Game Master visibility, and new-world placement.

Texture workflow:
1. Choose source image format and texture type.
2. Configure texture import settings: compression, max size, conversion, quality, bit depth, swizzling, color space, mips, filters, tiled/volume/cube behavior, and preview.
3. Verify imported texture visually and in material context.
4. Revisit color space or mips when output is visually wrong or performance-heavy.

LOD workflow:
1. Build LOD resources with intended transitions.
2. Use preview/debug surfaces to inspect behavior.
3. Decide whether automatic or manual system applies.
4. Verify LOD0 to LOD1 and LOD1 to LOD2/LOD3+ transitions.
5. Use manual override only when the documented behavior requires it.
6. Save and revalidate in the editor.

Collision workflow:
1. Define layer setup.
2. Define layer presets.
3. Configure interaction matrix rows.
4. Apply layer presets to colliders or object tool outputs.
5. Validate collision in editor and runtime, especially for dynamic objects and gameplay-interactive props.

Particle workflow:
1. Open Particle Editor and use Effect/Preview/Emitter panels deliberately.
2. Configure preview aids: grid, movement simulation, global wind, stress test, low-FPS simulation, helper model, ground visibility, and FOV as needed.
3. Configure emitter fields: shape type/size, cone angles, max number, birth rate, offsets, angles, local transform.
4. Configure appearance: material, center/scale, stretch/size multipliers, rotation, UV, billboard, fade, velocity angle, random angle, and flip settings.
5. Configure physics: velocity, air resistance, wind influence, parent velocity relation, gravity, restitution, and spring.
6. Configure texture sheet animation and lifetime/color/size/rotation behavior.
7. Validate in editor preview and runtime, especially under stress/low-FPS simulation.

Asset Browser Integration workflow:
1. Prepare the asset structure.
2. Create a register file.
3. Create or duplicate config.
4. Add the register file to the editor.
5. Use override behavior where required.
6. Expand registries array.
7. Register assets manually or through the documented plugin method.
8. Add modded labels.
9. Test result in game/editor context.

## Configuration Fields And Tables

FBX/model fields:
- Alignment.
- LOD naming and structure.
- Collider shape, collider hierarchy, collider usage.
- Static and dynamic object handling.
- Layer preset usage parameter on colliders.
- Physical material/game material.
- Materials.
- Center of mass.
- Occluders.
- Probes and probe volumes.
- Portals and BSP geometry.
- Sockets.
- Land contacts.
- FBX export settings.
- Workbench import settings.

Texture fields:
- Texture types: base color, roughness, metalness, normal, opacity, height, masks, global mask, detail mask, normal mask, camo mask, ambient occlusion, cavity, global/macro textures, emissive, environment cube map.
- Import settings: format compression, compression threshold, remove mips, max size, conversion, conversion quality, original pixel bit depth, swizzling, color space, contains mips, generate mips, mip map function, filter, normalize, color noise, mip map filter, tiled texture, volume texture, generate cube map.
- Texture properties and texture preview.

Blender Tools fields/surfaces:
- Installation and updating.
- Top menu and side section.
- Import ASC, P3D, FBX.
- Discard unsupported LODs.
- Layer presets.
- Game materials.
- Rename materials.
- Memory points.
- Convert axis to single point.
- Export ASC and TXA.
- Model Quality Assurance.
- Object Tools.
- Material Tools.
- Batch FBX export only-visible option.
- Materials import/export/synchronization/editing/debug channels.
- P3D material conversion table and conversion options.

Prop Creation fields:
- Structure.
- Object parts.
- Sockets.
- Skeleton and rigging mesh.
- Colliders and material names.
- FBX export settings.
- Texture preparation/import.
- Model import/registration.
- Import settings.
- Physics setup.
- Prefab and variant creation.
- Procedural animation, action, and sound handoff points.
- Placeable entity generation.
- Preview images.
- Display name.
- Localization table and strings.
- Labels.
- Asset registration.

LOD fields:
- Basics.
- Preview.
- Debug.
- Automatic system.
- LOD0 to LOD1 transition.
- LOD1 to LOD2 and LOD3+ transitions.
- Manual override.
- Save process.

Collision fields:
- Layers setup.
- Layer presets setup.
- Interaction matrix row setup.

Particle Editor fields:
- Effect panel and preview panel.
- Grid, move/rotate tools, world/local coordinate switch, cone angle volume, emit source volume, snap to ground, reset rotations, FOV, stats, helper model, ground, movement simulation, global wind, stress test, low-FPS simulation.
- Emitter general fields: shape type/size, cone angle, max number, birth rate, offsets, angles, local transform.
- Particle appearance: material, center, scale, stretch/size, rotation, UV, billboarding, fade, velocity/random angle, UV flip.
- Physics: velocity, air resistance, wind influence, parent velocity relation, gravity, restitution, spring.
- Texture sheet animation and particle lifetime fields.

Asset Browser fields:
- Register file.
- Config.
- Override behavior.
- Registries array.
- Asset registration.
- Manual method.
- Plugin method.
- Modded label.
- In-game test.

Object Import Tool:
- CSV file format is the important data contract. Verify the wiki table before creating or exporting object import CSV data.

## Procedures And Ordered Steps

FBX and model import procedure:
1. Prepare model alignment, object hierarchy, LODs, colliders, materials, sockets, and special geometry.
2. Run Blender Tools object/material helpers and model QA when using Blender.
3. Export FBX.
4. Import through Workbench.
5. Inspect import settings and generated resources.
6. Fix collider, layer preset, material, LOD, or texture warnings.
7. Validate in editor preview and runtime placement.

Prop creation procedure:
1. Prepare project/resource structure.
2. Cut the object into parts.
3. Add sockets.
4. Set skeleton and rigging mesh if needed.
5. Prepare colliders and material names.
6. Configure FBX export.
7. Prepare and import textures.
8. Import/register model.
9. Configure physics and import settings.
10. Create prefab, smaller part prefabs, and variants.
11. Add optional procedural animation, user actions, and sound through owning references.
12. Generate placeable entity and preview images.
13. Configure display name, localization, labels, and asset registration.
14. Test in Workbench/editor, Game Master if relevant, and a new world.

Texture procedure:
1. Choose texture type.
2. Set import compression/conversion/color-space/mip settings.
3. Preview texture resource.
4. Verify in material/model context.
5. Reimport or adjust settings when output is wrong.

Particle procedure:
1. Configure effect, preview, and emitter panels.
2. Set emitter shape, rate, transform, appearance, physics, texture sheet, lifetime, color, size, and rotation behavior.
3. Use stress and low-FPS simulation before accepting the effect.
4. Query exact particle entity/API routes if script or prefab behavior depends on the effect.

Asset browser integration procedure:
1. Prepare structure.
2. Create register file and config.
3. Add register file to editor.
4. Use override/registry expansion if required.
5. Register assets manually or by plugin method.
6. Add labels.
7. Test in game/editor context.

## Warnings And Failure Modes

- Do not start from scripts when the imported model, material, texture, collider, or LOD is invalid.
- Do not treat visual material assignment as enough. Game material, physical material, layer preset, and interaction matrix can affect gameplay behavior.
- Collider hierarchy, shape, naming, overlap, restrictions, and performance are import correctness issues.
- Static and dynamic object workflows are different. Validate the correct object category.
- LOD configuration affects performance and visibility; preview/debug and save behavior are required checks.
- Texture color space, compression, mips, swizzling, and conversion can make a correct source image render incorrectly.
- Particle effects must be tested under preview, stress, and low-FPS conditions where relevant.
- Prop Creation crosses animation, audio, actions, prefabs, localization, labels, and Game Master. Use this reference for the general prop pipeline and route domain-specific steps to their owners.
- Asset Browser Mod Integration is not the same as Resource Manager browsing. Register/config/label/test steps matter.
- The official Assets page is a large catalog. Do not copy the full catalog into runtime references; use it as provenance and route domain asset use to domain references.
- Blender Tools and Workbench versions can drift. Validate tool behavior in the current Workbench/Blender setup.
- API-sensitive asset/editor/plugin claims must come from query output, not memory.

## API Lookup Keys

Use these lookup keys when asset work touches API, editor tooling, or source-backed examples:
- `ResourceManager`
- `ResourceImportPlugin`
- `ValidateFBXPlugin`
- `AssetTypes`
- `AssetLibraryUtils`
- `BlenderRestAPI`
- `BlenderOperatorDescription`
- `GetPathToAssetsFromGuids`
- `GetPrefabGUID`
- `LocatePrefabsFromPath`
- `ParticleEditor`
- `Particles`
- `ParticleEffectInfo`
- `ParticleEffectEntity`
- `ParticleEffectEntitySpawnParams`
- `ReplicatedParticleEffectEntity`
- `SCR_RepeatingParticleEffectEntity`
- `WorkbenchPlugin`
- `ResourceManagerPlugin`

Do not guess exact class names, inheritance, attributes, methods, or file locations from this reference. Use game-data query output before writing API-sensitive asset import, Blender Tools, Resource Manager, or particle code.

## Game-Data Query Commands

Core asset/editor routes:
```powershell
py -3 scripts/query-reforger-data.py files ResourceManager --limit 8
py -3 scripts/query-reforger-data.py examples resource-loading --limit 8
py -3 scripts/query-reforger-data.py files Asset --limit 8
py -3 scripts/query-reforger-data.py files ValidateFBX --limit 8
py -3 scripts/query-reforger-data.py files ResourceImport --limit 8
```

Blender Tools routes:
```powershell
py -3 scripts/query-reforger-data.py files Blender --limit 8
py -3 scripts/query-reforger-data.py files AssetLibraryUtils --limit 8
py -3 scripts/query-reforger-data.py files BlenderRestAPI --limit 8
```

Particle routes:
```powershell
py -3 scripts/query-reforger-data.py files Particle --limit 8
py -3 scripts/query-reforger-data.py files ParticleEffectEntity --limit 8
py -3 scripts/query-reforger-data.py symbol ParticleEffectEntity --kind class --exact
py -3 scripts/query-reforger-data.py symbol ParticleEffectEntitySpawnParams --exact
```

Bounded snippet routes after selecting a result:
```powershell
py -3 scripts/query-reforger-data.py snippet scripts/WorkbenchGameCommon/ValidateFBXPlugin.c --line 1 --context 40
py -3 scripts/query-reforger-data.py snippet scripts/WorkbenchCommon/ResourceImportTool.c --line 1 --context 40
py -3 scripts/query-reforger-data.py snippet scripts/WorkbenchGameCommon/EnfusionBlenderTools/AssetLibraryUtils.c --line 1 --context 40
py -3 scripts/query-reforger-data.py snippet scripts/GameLib/generated/WorkbenchAPI/Modules/ParticleEditor.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/GameLib/generated/Particles/ParticleEffectEntity.c --line 1 --context 30
```

Cross-reference routes:
```powershell
py -3 scripts/query-reforger-data.py examples weapon --limit 8
py -3 scripts/query-reforger-data.py examples vehicle --limit 8
py -3 scripts/query-reforger-data.py examples animation --limit 8
py -3 scripts/query-reforger-data.py examples audio --limit 8
py -3 scripts/query-reforger-data.py files EntityCatalog --limit 8
```

## Examples And Samples

Official sample layout signals:
- `SampleMod_NewProp` is the primary sample family for general prop asset layout and validation.
- `SampleMod_Main` shows general asset/material/texture/model resource organization and test-world context.
- Animation, weapon, and vehicle samples are cross-reference signals only; use their owning references for domain workflow details.

Raw game-source example routes:
- Validate FBX route: `files ValidateFBX` for Workbench-side validation tooling.
- Resource import route: `files ResourceImport` for Resource Manager import plugin behavior.
- Blender Tools route: `files Blender`, `files AssetLibraryUtils`, and `files BlenderRestAPI`.
- Particle route: `files Particle`, `files ParticleEffectEntity`, and exact particle entity symbol lookups.
- Resource-loading examples: `examples resource-loading` for Reforger resource loading and prefab/resource routes when asset work touches script or data-driven loading.

Example use pattern:
1. Read this reference for the asset pipeline and split boundary.
2. Query exact asset/editor/particle symbols before writing code.
3. Use bounded snippets only for selected files.
4. Validate imported resources in Workbench and runtime.
5. Route to domain references when the asset becomes a weapon, vehicle, gear item, animation graph, audio system, UI layout, terrain object, or prefab/config modeling task.

## Follow-Up Keywords

Asset import:
- FBX Import
- alignment
- LOD
- collider hierarchy
- collider usage
- layer preset
- physical material
- game material
- center of mass
- occluders
- probes
- portals
- BSP geometry
- sockets
- land contacts
- Workbench import

Blender Tools:
- Enfusion Blender Tools
- Blender Rest API
- Import ASC
- Import P3D
- Import FBX
- Batch FBX Export
- material library
- material preview
- model quality assurance
- object tools
- P3D conversion
- memory points
- layer presets
- game materials

Textures/materials:
- source image format
- base color
- roughness
- metalness
- normal
- opacity
- masks
- ambient occlusion
- emissive
- environment cube map
- compression
- swizzling
- color space
- mips
- texture preview

Props and browser:
- Prop Creation
- placeable entity
- preview images
- localization table
- labels
- Asset Browser Mod Integration
- register file
- registries array
- modded label

Particles:
- Particle Editor
- ParticleEffectEntity
- emitter
- preview panel
- shape type
- birth rate
- particle appearance
- texture sheet animation
- lifetime
- stress test
- low FPS simulation

Cross-reference routes:
- weapon asset
- vehicle asset
- character gear
- animation export
- sound event
- UI layout
- terrain object
- prefab config
- Workbench plugin

## Verification

Asset import verification:
- Confirm imported resources appear in Resource Manager and open in the relevant editor/preview surface.
- Confirm FBX alignment, scale, hierarchy, LODs, colliders, material names, sockets, probes/portals, and land contacts.
- Confirm import settings after Workbench import.
- Confirm model QA and Validate FBX routes do not report blocking issues.

Material/texture verification:
- Confirm texture type and import settings match intended use.
- Confirm compression, conversion, color space, mip settings, and swizzling in preview and model/material context.
- Confirm game material and physical material behavior in runtime when gameplay interaction matters.

Collision/LOD verification:
- Confirm collider layer presets and interaction matrix behavior.
- Confirm static/dynamic object collision behavior in runtime.
- Confirm LOD preview/debug behavior and saved LOD transitions.
- Confirm performance expectations for dense or repeated assets.

Prop and asset browser verification:
- Confirm prefab/variant creation only after imported resources validate.
- Confirm placeable entity, preview images, display names, localization, labels, and asset registration.
- Test in Workbench/editor, Game Master when relevant, and a new world.

Particle verification:
- Confirm effect preview, emitter settings, material/appearance, physics, texture sheet, and lifetime behavior.
- Use stress and low-FPS simulation when the effect may appear frequently or under performance pressure.
- Validate particle effect entity/prefab behavior at runtime if spawned or controlled by code.

Split-boundary verification:
- If the task becomes weapon setup, switch to `weapons-prefabs-attachments-and-firearms.md`.
- If the task becomes vehicle simulation or compartments, switch to `vehicles-creation-simulation-and-compartments.md`.
- If the task becomes character gear or inventory, switch to `character-gear-inventory-and-arsenal.md`.
- If the task becomes animation graph/export, switch to `animation-graphs-weapon-animation-and-export.md`.
- If the task becomes audio event/system setup, switch to `audio-editor-signals-and-sound-systems.md`.
- If the task becomes prefab/config modeling, switch to `prefabs-configs-containers-and-catalogs.md`.
- If the task becomes Workbench plugin authoring, switch to `workbench-plugins-and-editor-tools.md`.

## Official Wiki Links

- Assets: https://community.bistudio.com/wiki/Arma_Reforger:Assets
- FBX Import: https://community.bistudio.com/wiki/Arma_Reforger:FBX_Import
- Enfusion Blender Tools: https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools
- Enfusion Blender Tools: Batch FBX Export: https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Batch_FBX_Export
- Enfusion Blender Tools: Import/Export ASC Elevation: https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Import/Export_ASC_Elevation
- Enfusion Blender Tools: Import/Export Animation: https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Import/Export_Animation
- Enfusion Blender Tools: MLOD Baking Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_MLOD_Baking_Tutorial
- Enfusion Blender Tools: Materials Library: https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Materials_Library
- Enfusion Blender Tools: Materials Preview: https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Materials_Preview
- Enfusion Blender Tools: Model Quality Assurance: https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Model_Quality_Assurance
- Enfusion Blender Tools: Objects Tools: https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Objects_Tools
- Enfusion Blender Tools: P3D Conversion: https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_P3D_Conversion
- Enfusion Blender Tools: Portal Tools: https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Portal_Tools
- Enfusion Blender Tools: Rig Updater: https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Rig_Updater
- Enfusion Blender Tools: Skeleton Updater: https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Blender_Tools:_Skeleton_Updater
- Prop Creation: https://community.bistudio.com/wiki/Arma_Reforger:Prop_Creation
- Textures: https://community.bistudio.com/wiki/Arma_Reforger:Textures
- Level Of Detail: https://community.bistudio.com/wiki/Arma_Reforger:Level_Of_Detail
- Collision Layer: https://community.bistudio.com/wiki/Arma_Reforger:Collision_Layer
- Particle Editor: https://community.bistudio.com/wiki/Arma_Reforger:Particle_Editor
- Object Import Tool: https://community.bistudio.com/wiki/Arma_Reforger:Object_Import_Tool
- Asset Browser Mod Integration: https://community.bistudio.com/wiki/Arma_Reforger:Asset_Browser_Mod_Integration
- Assets category: https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Assets
- Assets guidelines category: https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Assets/Guidelines
- Assets tutorials category: https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Assets/Tutorials
- Enfusion Blender Tools category: https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Official_Tools/Enfusion_Blender_Tools

## Usefulness Score

Score: 91/100

- Wiki coverage: 28/30. All owned primary asset, FBX, Blender Tools, prop, texture, LOD, collision, particle, object import, and asset browser pages are reviewed, named, linked, and represented. Two points are reserved because the huge Assets catalog is intentionally represented as category/provenance and routed to official links/domain references rather than mirrored as a copied catalog.
- Operational detail: 14/15. The reference preserves import settings, Blender Tools surfaces, prop workflow, texture/material settings, LOD, collision, particle fields, asset browser registration, and validation order. One point is reserved because exact editor UI labels and import options require current Workbench verification.
- API lookup usefulness: 14/15. Query commands cover ResourceManager, resource-loading examples, Asset, Blender, Particle, ValidateFBX, ResourceImport, ParticleEffectEntity, and snippets. One point is reserved because most asset import work is editor/data workflow rather than script API.
- Example grounding: 9/10. `SampleMod_NewProp`, `SampleMod_Main`, raw game-source routes, and query examples are included. One point is reserved because samples are layout evidence only and do not replace Workbench validation.
- Codex task usefulness: 14/15. Codex can route general asset import, prop creation, texture/material, LOD, collision, particle, and asset browser tasks without guessing. One point is reserved because domain asset tasks intentionally route to separate references.
- Context efficiency: 8/10. Content is dense, structured, and avoids copied tables/API dumps. Two points are reserved because the source family is broad and the reference must include many workflows.
- Verification guidance: 4/5. Workbench, import, material/texture, collision/LOD, prop/browser, particle, and runtime checks are covered. One point is reserved because final model/visual/collision quality must be verified in editor/runtime.

Category-fit check:
- Source family complete: pass; all owned general asset pipeline source families are represented.
- No owned page missing: pass; every owned primary page appears in Source Inventory and Official Wiki Links.
- Split boundary justified: pass; weapon, vehicle, gear, animation, audio, UI, terrain, prefab/config, and plugin authoring workflows are routed to their owning references.
- Cross-links present: pass; related workflow owners are named where tasks leave general asset import.
- Task route clear: pass; import asset/prop, validate FBX, configure material/texture, set collision/LOD, create particles, and register asset all route through this reference plus query commands.
- Missed coverage cap: no cap applies. No relevant owned wiki page, field group, procedure, warning, or validation family is omitted without rationale.
