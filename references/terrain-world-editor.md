# Terrain World Editor

## When to read this reference

Read for terrain/world creation, World Editor UI, layers, entity placement, prefabs, navmesh generation, roads/rivers/lakes/forests/generators, map tooling, and editor-only world automation.

## Search terms

`World Editor`, `Create new World`, `Load World`, `Save World`, `Play Game`, `Server localhost`, `PeerTool`, `Terrain Tool`, `Navmesh Tool`, `Road Generator`, `River Generator`, `Lake Generator`, `Forest Generator`, `Prefab Library`, `Resource Browser`, `.ent`, `.layer`, `.terr`, `.nmn`

## Source authority summary

World Editor docs define top-bar actions, tools, object properties, prefab library behavior, log console, and navmesh tool UI. Terrain/navmesh/generator pages define specific workflows. Samples show world, terrain, and navmesh resource layout. API data is only for editor automation; manual Workbench validation remains required.

## World Editor top-bar actions

Key actions and shortcuts:

- Create new world or sub-scene: `Ctrl+N`.
- Load world: `Ctrl+O`.
- Save world: `Ctrl+S`.
- Go to World File: show loaded world in Resource Browser.
- Undo last action: `Ctrl+Z`.
- Redo: `Ctrl+Y`.
- Copy selected object: `Ctrl+C`.
- Paste on same position: `Ctrl+Shift+V`.
- Cut selected object: `Ctrl+X`.
- Play Game: `F5`.

Play Game options:

- Play inside viewport.
- Play fullscreen.
- Play from camera position. Default unit comes from Resource Manager options, Default Player Controller.
- Server localhost: starts game with background server. Docs warn direct IP connection needs a real address, not loopback like `127.0.0.1`.
- Server localhost + PeerTool: starts background server and local clients from PeerTool settings.

Use Server localhost + PeerTool for multiplayer debugging when a task affects replication or ownership.

## Basic tools

- Toggle Gizmo Space: `X`, switches manipulation tools between world and object reference.
- Entity select filter: every/active/inactive layers.
- Select parent entities: select parent when selecting child.
- Ground Manipulation Tool: shortcut `Q`; move selected objects by dragging to terrain/object/water surface. Not the same as Terrain Tool.
- Move Tool: shortcut `W`; move in screen plane and/or axes.
- Rotate Tool: shortcut `E`; rotate with arcs.
- Scale Tool: shortcut `R`; vertical green-bar widget.
- Vector Entity Tool: shortcut `V`; draws polyline or spline used by generators such as forests, walls, lakes.
- Bounding Volume Tool: edit bounding box visually.
- Terrain Tool: shortcut `Ctrl+T`; sculpt terrain.
- Navmesh Tool: generates navmesh/AI navigation grids.
- Measure Tool: measures length along 3D lines; only works on terrain entity.
- Import Objects: imports objects from CSV.
- Autotest Tool: runs autotest framework classes.
- Coords Tool: navigate to coordinates or create World Editor links. Requires registering `enfusion://` protocol in Resource Manager/Workbench options.

## Object properties retained from docs

Object Properties panel changes by entity type. Common areas:

- Entity information: root type on left; name field on right for script references.
- Components: listed under class.
- Scope of changes: entity instance, entity definition, modded entities, or parent prefab(s).
- Transformation: coordinates, angles, scale. Scale range documented as 0..1000.
- Flags:
  - Traceable: entity can be detected through trace methods.
  - Visible: entity is invisible in-game while visible in World Editor.
  - Static: entity expected to remain in position.
  - Feature: terrain feature drawn regardless of distance.
  - Proxy: prefab sub-element hidden when parent prefab is hidden.
  - Editor Only: exists only in editor.
  - Relative Y: altitude relative to surface below.
- Script: script slots for events/other cases.
- Unsorted: uncategorized settings.

## Navigation and selection

Viewport navigation:

- Mouse wheel moves camera forward/backward.
- Hold right mouse button and move mouse to rotate camera.
- While holding right mouse, mouse wheel changes camera speed.
- `W/S` move forward/backward, `A/D` sideways, `Q/Z` up/down.
- Double-click in Hierarchy focuses camera on entity; `F` focuses selected entity.
- `Esc` leaves preview; `F10` is hardcoded equivalent within World Editor.

## Resource Browser and Prefab Library

Resource Browser:

- Shows project data structure and data types: configs, textures, prefabs, etc.
- Can show content from subdirectories.

Prefab Library:

- Closely tied to world creation and not available in Resource Manager.
- Lists prefab-library entities by Data/PrefabLibrary categories such as Decals, Generators, Infrastructure, Props, Rocks, Structures, Vegetation, Walls.
- Uses underlight color coding for entity types:
  - Blue: regular prefabs.
  - Purple: Prefab Library entity.
  - Orange: editable prefab used by in-game editor.

Prefab Library details tab can include:

- Place By: origin or boundBox.
- Random Yaw: 0..360 degree Y-axis randomization.
- Align To Normal: place perpendicular to surface normal.
- Random Scale: min/max random scale.
- Random Vertical Offset: min/max vertical offset.
- Random Pitch Angle.
- Random Roll Angle.

Important prefab caveat: prefabs are wrapper entities pointing to other entities. Renaming a prefab affects display name only, but changing the prefab's entity target replaces all entities using that template.

## Navmesh tool workflow

Navmesh Tool UI can display:

- Result.
- Heightfield.
- Heightfield Filtered.
- Compact heightfield.
- Heightfield regions.
- Raw contours.
- Contours.
- Region connections.
- Polygons.
- Detailed Mesh.

Actions/settings:

- Choose navmesh to display in viewport.
- Vertical Offset changes display only, not the actual navmesh.
- Rebuild tile.
- Rebuild/regenerate changed tiles.
- Connect/disconnect to navmesh server.
- Generate.
- Stop Generation.
- Autosave when done.
- Save.
- Save As.

Navmesh workflow:

1. Open the world in World Editor.
2. Select the correct navmesh resource/project.
3. Generate or rebuild changed tiles after terrain/road/object blocker edits.
4. Inspect result and relevant debug display modes.
5. Save or Save As as appropriate.
6. Validate AI movement in-game, including vehicle/character navmesh differences where relevant.

## Terrain/world resource layout

Sample-derived layout:

```text
Worlds/<Project>/<World>.ent
Worlds/<Project>/<World>_Layers/default.layer
Worlds/<Project>/Terrain/<Terrain>.terr
Worlds/<Project>/Navmeshes/<Navmesh>.nmn
Terrains/...
```

Terrain work usually requires:

- World resource.
- Terrain entity/resource.
- Layers.
- Materials/surface layers.
- Collision and traceable surfaces.
- Navmesh rebuild.
- Map/export data if the task affects 2D map or generated geographic data.

## Generators and vector tools

Road, river, lake, forest, wall, powerline, object brush, and prefab generators are editor/data workflows. Use Vector Entity Tool or generator-specific tools, then inspect generated objects/resources for performance and collision.

Generator checklist:

1. Confirm target layer.
2. Confirm source prefabs/resources.
3. Use the specific generator tool.
4. Review generated object count and placement.
5. Rebuild navmesh if AI traversal or blockers are affected.
6. Test collision, streaming, and visual result in Play Game.

## Editor automation caveat

World Editor scripts must be editor-only. Wrap entity edits in `BeginEntityAction`/`EndEntityAction` for undo history, and use `WorldEditorTool`/`WorldEditorAPI` only in Workbench modules.

generated-pattern-from-docs

```c
m_API.BeginEntityAction("Changing generated entities");
// Set source variables, create/delete entities, update layer content.
m_API.EndEntityAction();
```

## API Notes

Use `api-extended.md` for `WorldEditor`, `WorldEditorAPI`, `WorldEditorPlugin`, `WorldEditorTool`, terrain/navmesh/generator classes, and editor callbacks. Use `api-main.md` for generic Workbench plugin shape and entity/resource APIs.

## Common Traps

- Editing the wrong layer.
- Forgetting navmesh rebuild after terrain/object/road changes.
- Treating vertical display offset as real navmesh offset.
- Using loopback address for Server localhost direct IP testing when docs require real address.
- Changing prefab entity target and unintentionally replacing all uses.
- Calling World Editor APIs from runtime code.

## Review Checklist

- Are world/layer/terrain/navmesh resources identified?
- Are exact editor tools/actions named?
- Are generated data and performance risks covered?
- Is navmesh/AI validation included?
- Is editor automation kept in Workbench modules?

## API Notes

- World Editor automation belongs in Workbench plugin/tool code, not runtime gameplay code.
- Verify `WorldEditor` and tool APIs in `api-extended.md` before writing editor automation.
- Use `ResourceName` for world, prefab, layer, and generated-resource paths.
- Use runtime entity APIs only for in-game behavior, not for modifying editor worlds.
- Navmesh and terrain generation are data workflows; script should not replace required editor baking/validation.

## generated-pattern-from-docs: Navmesh Validation Workflow

```text
Open world in World Editor.
Inspect terrain and object placement.
Run or update navmesh generation through the navmesh tool.
Check generated data in editor.
Run AI movement tests in the scenario context.
Rebuild after terrain, road, river, or obstacle changes.
```

This is a workflow example because the documented navmesh process is editor-driven.

## World Structure Detail

- Worlds contain terrain, objects, layers, generated data, and scenario-facing placement.
- Layers help organize large world content.
- Object placement changes can affect navigation, performance, and scenario behavior.
- Prefab instances inherit behavior from prefab resources, so changing a prefab can affect many placed objects.
- Changing a placed instance can be instance-only unless applied back to the prefab.
- Generated data should be regenerated when the source world data changes.
- Validate worlds in editor and runtime because editor placement does not prove gameplay behavior.

## Terrain Detail

- Terrain work affects visuals, movement, AI, and performance.
- Height and surface changes can invalidate navmesh.
- Road and river tools produce world data that other systems may consume.
- Generated terrain data should be treated as build output from editor workflows.
- Keep source terrain edits and generated data changes clear in review.
- Large terrain operations require performance checks.
- Do not debug terrain collision/navigation by editing gameplay script first.

## Navmesh Detail

- Navmesh must match terrain and obstacle state.
- Display offsets in editor views are not the same as actual navmesh data offsets.
- AI movement testing is required after navmesh changes.
- Regenerate navmesh after terrain, object, road, or river changes that affect traversal.
- Check both local preview and scenario runtime behavior.
- Keep navmesh generation settings documented for repeatability.
- Avoid committing stale generated navmesh after source-world edits.

## Editor Tool Detail

- Use Begin/End entity actions when changing world entities through editor APIs.
- Wrap destructive changes with confirmation and undo-safe behavior.
- Resource Browser and Prefab Library are placement sources, not runtime registries by themselves.
- World Editor plugins should handle no selection and mixed selection.
- Long-running generation tools need clear progress and failure logging.
- Editor automation should not silently change many entities without user-visible scope.
- Test editor tools on a copy or small selection before applying to a full world.

## World Review Detail

- Check world resource path.
- Check layer organization.
- Check terrain source changes.
- Check generated terrain output.
- Check road edits.
- Check river edits.
- Check object placement density.
- Check prefab instance overrides.
- Check collision after terrain changes.
- Check navmesh after terrain changes.
- Check navmesh after road or river changes.
- Check AI traversal in scenario context.
- Check world performance hotspots.
- Check streaming or visibility assumptions.
- Check Resource Browser dependencies.
- Check Prefab Library placement source.
- Check whether changes are instance-only or applied to prefab.
- Check generated-data freshness before packaging.
- Check editor-only APIs stay out of runtime scripts.
- Check world changes on a clean profile or separate test copy.

## Navmesh Review Detail

- Verify generation settings.
- Verify generated resource location.
- Verify visual navmesh coverage.
- Verify blocked areas.
- Verify traversal over slopes.
- Verify traversal near roads.
- Verify traversal near rivers.
- Verify traversal around placed props.
- Verify AI path tests in runtime.
- Verify no stale generated output remains after source edits.

## Editor Verification Detail

- Save the world after intended edits.
- Reopen the world to verify persistence.
- Inspect generated data timestamps.
- Inspect Resource Manager warnings.
- Run the scenario that uses the world.
- Test AI traversal through changed areas.
- Test player traversal through changed areas.
- Test vehicle traversal when roads or terrain changed.
- Package and clean-launch when published world content is involved.
