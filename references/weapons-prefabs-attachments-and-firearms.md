# Weapons Prefabs Attachments And Firearms

## When To Read

Read this when the task is about creating, modifying, debugging, or scripting weapon behavior in Arma Reforger:

- creating a new firearm or weapon variant;
- preparing weapon meshes, slots, bones, colliders, materials, textures, and model registration;
- configuring weapon prefabs, inventory item behavior, action contexts, muzzle behavior, magazine wells, ammo, ballistics, zeroing, dispersion, deployment, and obstruction;
- adding or changing optics, suppressors, collimators, muzzle attachments, magazine compatibility, and stat-modifying attachments;
- finding exact weapon API, component, muzzle, magazine, fire-mode, or weapon UI source routes.

Use this as the primary reference for weapon-specific setup. Do not use it as the owner for generic asset import, generic prefab data modeling, generic component lifecycle, character inventory/gear, weapon animation authoring, or weapon audio authoring. Those are separate references.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: weapon creation, weapon asset preparation, weapon prefab configuration, weapon components, weapon slots and bones, weapon modding, optics, suppressors, collimators, stat-modifying attachments.
- Secondary/cross-reference topics: general asset import, prefab/config modeling, entity/component lifecycle, animation, audio, character gear/inventory, arsenal/entity catalog integration.

Wiki pages reviewed:
- Weapon Creation - https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Creation - status: covered - reason: top-level workflow and sample-family orientation.
- Weapon Creation/Asset Preparation - https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Creation/Asset_Preparation - status: covered - reason: owned weapon mesh, slot, collider, skeleton, texture, and import workflow.
- Weapon Creation/Prefab Configuration - https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Creation/Prefab_Configuration - status: covered - reason: main weapon prefab, inventory, action, ballistics, ammo, magazine, crate, arsenal, deployment, zeroing, dispersion, obstruction, and AI targeting workflow.
- Weapon Modding - https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Modding - status: covered - reason: owned existing-weapon modification, inherited prefab, new ammo/magazine/config, material, sound, particle, and test workflow.
- Weapon Components - https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Components - status: covered - reason: weapon-specific slot, UI info, muzzle, magazine, and component field surface.
- Weapon Slots And Bones - https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Slots_And_Bones - status: covered - reason: owned weapon body/attachment split, slot/snap point, simulation, and bone convention source.
- Weapon Optic Creation - https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Optic_Creation - status: covered - reason: owned optic asset, memory point, prefab, inventory, attachment, scope, PIP, and arsenal workflow.
- Weapon Suppressor Creation - https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Suppressor_Creation - status: covered - reason: owned suppressor asset, script/config class, prefab, muzzle integration, stat manager, sound, arsenal, and verification workflow.
- Weapon Collimator Creation - https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Collimator_Creation - status: covered - reason: owned collimator reticle, projection plane, material, prefab, component, controller, script API, and testing workflow.
- Weapon Stats-Modifing Attachments - https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Stats-Modifing_Attachments - status: covered - reason: owned stat modifier hierarchy, attachment attributes, stats manager, API route, and muzzle effect special case.

Wiki sections covered:
- Weapon Creation: tutorial goal, add new weapon, structure preparation, creation steps.
- Weapon Creation/Asset Preparation: prepare mesh, object orientation, object cutting/naming, slots and snap points, colliders and material names, skeleton and rigging, FBX export, texture preparation, model registration, collider/material checks, skeleton/hierarchy checks, texture import.
- Weapon Creation/Prefab Configuration: prefab setup, inventory configuration, action context adjustment and debug, weapon characteristics, behavior, obstruction, accessory modifiers, deployment, zeroing, dispersion, ammunition creation, ballistic properties, penetration, tracers, AI target selection, magazine well, magazine prefab setup, tracer magazine setup, crate filling, arsenal crates, regular crates.
- Weapon Modding: goals, file structure, inherited prefab and drag/drop variant creation, prefab inheritance and apply-to-prefab workflows, component parameters, ammo and magazine configs, AI config changes, magazine application, material retexture, sound change, particle effects, muzzle flash, explosion effect, in-game testing.
- Weapon Components: slot classes, PointInfo, EntitySlotInfo, InventoryStorageSlot, EquipmentStorageSlot, LoadoutSlotInfo, RegisteringComponentSlotInfo, SoundPointInfo, DecalSlotInfo, emissive slots, UI info classes, grenade/magazine/muzzle/weapon UI info.
- Weapon Slots And Bones: splitting weapon, body, attachments, slot/snap point conventions, slots, attachments, simulation, bones.
- Weapon Optic Creation: structure, mesh preparation, colliders, memory points, slots, optic mesh for PIP, model import, texture/material, reticle, prefab, inventory, character modifiers, attachment configuration, optic configuration, diagnostics, base sight properties, 2D scope, PIP scope, arsenal integration.
- Weapon Suppressor Creation: prerequisites, structure, model orientation, naming, snap points, collision mesh, layer preset/material, export, texturing, attachment script/config class, script reload, base and child prefab, MeshObject, InventoryItemComponent, suppressor attributes, muzzle effects, obstruction, ActionsManager adjustment, localization, weapon muzzle integration, AttachmentSlotComponent, stats manager, weapon sound component, arsenal, final testing.
- Weapon Collimator Creation: structure, plane UV, geometry definition, reticle material, material script bindings, prefab creation, component setup, collimator configuration, reticle size/colors/indices, ADS enable percentage, day/night brightness, testing, potential traps, script API lookup route.
- Weapon Stats-Modifing Attachments: overview, modifiable stats, attaching/detaching hierarchies, configuring attachment attributes, custom attributes, stats manager component, Set/Clear/Get API families, muzzle effect special case.

Structured wiki records:
- Tables reviewed/included: Weapon Components field tables, Weapon Slots And Bones slot/bone tables, Weapon Stats modifier tables, Weapon Creation prefab/ballistics/AI tables, asset-preparation and modding tables.
- Procedures reviewed/included: Weapon Creation, asset preparation, prefab configuration, weapon modding, optic creation, suppressor creation, collimator creation, stat modifier setup, slots/bones setup.
- Admonitions reviewed/included: mesh/import caveats, prefab inheritance cautions, action context/debug caveats, ballistic/material warnings, collimator runtime-only warning, suppressor script naming and localization warnings, attachment obstruction and stats manager requirements.
- Code blocks reviewed/included: attachment config class pattern, collimator material binding route, weapon configuration examples. Exact code must be verified through query/source snippets before reuse.
- Media reviewed: workflow screenshots and diagrams were reviewed as source evidence for editor surfaces, but this runtime reference does not depend on images.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts/query-reforger-data.py lookup "create weapon script" --limit 8`
  - `py -3 scripts/query-reforger-data.py examples weapon --limit 8`
  - `py -3 scripts/query-reforger-data.py examples weapon --subtopic magazine --limit 8`
  - `py -3 scripts/query-reforger-data.py files Weapon --limit 8`
  - `py -3 scripts/query-reforger-data.py files BaseWeaponComponent --limit 8`
  - `py -3 scripts/query-reforger-data.py files BaseMuzzleComponent --limit 8`
  - `py -3 scripts/query-reforger-data.py files BaseMagazineComponent --limit 8`
- Symbols/methods/attributes verified as lookup keys: `WeaponComponent`, `BaseWeaponComponent`, `MuzzleComponent`, `BaseMuzzleComponent`, `MagazineComponent`, `BaseMagazineComponent`, `WeaponSlotComponent`, `SCR_WeaponStatsManagerComponent`, `BaseWeaponStatsManagerComponent`, `SCR_WeaponAttachmentAttributes`, `AttachmentSlotComponent`.
- Examples/snippets reviewed: weapon component examples, weapon HUD/fire-mode/muzzle/magazine examples, Workbench weapon helper routes, AI weapon/magazine/muzzle examples, rocket ejector muzzle component route.

Samples and source examples:
- Official sample folders reviewed: `SampleMod_NewWeapon`, `SampleMod_ModdedWeapon`, weapon-related folders in `SampleMod_Main`, weapon animation sample folders as cross-reference signals only.
- Raw game-source example families reviewed through query output: `SCR_MineWeaponComponent`, `SCR_WeaponComponent`, `SCR_RocketEjectorMuzzleComponent`, weapon HUD info, BIKI weapon helper, AI weapon evaluation and magazine/muzzle helper files.

Coverage gaps:
- Weapon animation tutorials are intentionally owned by `animation-graphs-weapon-animation-and-export.md`; this reference only links the requirement to assign/verify weapon animation resources.
- Weapon audio authoring is intentionally owned by `audio-editor-signals-and-sound-systems.md`; this reference only preserves weapon/suppressor sound-component integration points.
- Character gear, wearable inventory, and arsenal-wide gear behavior are intentionally owned by `character-gear-inventory-and-arsenal.md`; this reference only covers weapon and attachment catalog exposure.
- Exact method signatures and code bodies are not embedded; use query commands before writing API-sensitive code.

## Wiki Source Coverage

Weapon creation starts with a strict division between source assets, registered resources, and configured prefabs. The top-level tutorial frames the workflow as: prepare the project structure, prepare weapon mesh/data, import/register resources, configure the prefab, connect weapon-specific components, expose it to inventory/arsenal systems, then test in game.

Asset preparation coverage:
- Mesh orientation matters. Weapon models need consistent forward/up orientation so aim, attachments, sockets, colliders, and animations line up after import.
- The source mesh should be cut into functional objects where needed: body, magazine, bolt, trigger, selector, attachment surfaces, moving parts, and collision pieces.
- Object names are part of the workflow because downstream import, material creation, socket selection, and Workbench lists depend on predictable names.
- Slots and snap points are authored in the DCC tool as bones, empties, or memory/snap points. The imported weapon prefab later uses these identifiers as `Pivot ID`, attachment slots, muzzle positions, sight points, magazine points, or similar field values.
- Collider and material naming are not cosmetic. Correct collider geometry, layer presets, and game material assignment drive physics, damage, obstruction, hit behavior, and Workbench validation.
- Skeleton setup and mesh rigging are required for weapons with moving parts or attachment points that need animation/simulation. Bones and mesh skinning must be verified after import.
- FBX export and model import must preserve scene hierarchy when sockets/empties are required. If snap points or collimator geometry points do not appear in Workbench, revisit export/import hierarchy settings.
- After model registration, check colliders/materials, skeleton/hierarchy, and texture import before moving on to prefab setup.

Prefab configuration coverage:
- Weapon prefab setup is not just assigning a mesh. It includes inventory representation, action contexts, weapon behavior, muzzle/magazine/ammo data, ballistics, deployment, obstruction, AI targeting, and crate/arsenal exposure.
- Inventory configuration determines how the weapon appears and behaves as an item. Validate display name, item physical attributes, preview render attributes, storage behavior, and catalog exposure.
- Action contexts must be checked for the weapon and its muzzle/attachment interactions. The wiki specifically routes through action context adjustment, adding new action contexts, debug, location changes, and radius adjustment.
- `ActionsManagerComponent` debug is a weapon workflow tool. Use it when actions do not appear, appear at the wrong location, or are inaccessible because context/radius/offset is wrong.
- Weapon characteristics and behavior configuration cover the functional weapon behavior surface: weapon operation, muzzle behavior, fire mode, obstruction, deployment, zeroing, dispersion, ammo, magazines, and AI-facing properties.
- Obstruction has a dedicated theory/configuration workflow. Treat obstruction as a correctness feature for weapon behavior and attachment compatibility, not as a cosmetic setting.
- Accessory modifiers and stat-modifying attachments can alter weapon behavior when attachments are added or removed. Do not hardcode these effects without checking the configured attributes and stats manager routes.
- Deployment configuration includes adding deployment points, base deployment, bipod deployment, deployment IK targets, and deployment aim modifiers. Validate both Workbench configuration and runtime behavior.
- Zeroing and dispersion have dedicated configuration surfaces. Do not assume default values are suitable for a new caliber, barrel, optic, or attachment setup.
- Ammunition creation includes ammo configuration, ballistic properties, drag/ballistic coefficient choices, ballistic tables, barrel length versus muzzle velocity, penetration, damage, tracers, and AI target selection.
- Magazine well and magazine prefab setup connect the weapon to compatible magazines and ammo. A weapon can appear valid but fail in use if magazine well, magazine prefab, ammo config, or arsenal/catalog entries are incomplete.
- Crate filling and arsenal crate workflows are part of weapon usability. Weapon prefabs and attachments must be exposed through the right crate/catalog lists for the intended faction or faction-less use.

Weapon modding coverage:
- Existing weapon modification can use inherited prefabs or drag/drop duplication, but inheritance must remain intentional. Apply-to-prefab and inheritance tree workflows affect whether changes remain in an override, inherited child, or duplicated asset.
- For new variants, preserve structure: prefab inheritance, component parameter changes, ammo type creation, explosive effects, new components, new ammo AI config, magazine config, and weapon application order.
- New magazine and ammo changes must connect both directions: the magazine must use the ammo config, and the weapon must accept the magazine through its magazine well/configuration.
- Retexturing uses material creation/import and application to the asset. Material work belongs to the asset pipeline, but weapon modding owns the weapon-specific decision to apply the material to the weapon variant.
- Weapon sound changes and particle effects are cross-linked to the audio/asset references, but this reference owns the integration step: assign changed sounds/effects back to the weapon, muzzle, suppressor, or explosion effect and test in game.

Weapon component coverage:
- `PointInfo` carries pivot identity, offset, and angles.
- `EntitySlotInfo` extends point placement with child pivot, enabled state, prefab resource, physics interaction, inherited skeleton behavior, and attach/detach physics behavior.
- `InventoryStorageSlot` adds editor-facing slot naming.
- `EquipmentStorageSlot` adds allowed item types, occluder behavior, and animated mesh reference for runtime mesh-state changes.
- `LoadoutSlotInfo` adds equipment area and meshes to hide.
- `RegisteringComponentSlotInfo` controls whether attached entities register actions, damage, controllers, weapons, compartments, or lights back to the parent entity.
- `SoundPointInfo`, `DecalSlotInfo`, emissive glass/light surface slots, and UI info classes give weapon-specific positions and presentation data.
- Weapon UI info surfaces include names, descriptions, icons, ammo type/caliber text, fire-mode icons/imagesets, magazine indicators, and weapon name display.

Slots and bones coverage:
- Split the weapon into body and attachment concepts before configuring slots. Attachments need clear snap points and simulation/bone conventions.
- Slots and snap points require consistent naming and orientation. The same identifier may be selected later in component `Pivot ID`, `Child Pivot ID`, attachment point, muzzle effect position, optic sight point, or inventory storage slot.
- Bones and simulation are separate but related. Bones drive animated/skeletal behavior; slot simulation and attachment setup determine what can attach, detach, move, or register back to the parent.

Optic coverage:
- Optic setup includes mesh preparation, colliders, memory points, slots, points, optional PIP mesh, model registration, texture/material setup, reticle setup, and prefab creation.
- Inventory configuration makes the optic a usable item; attachment configuration makes it compatible with weapon slots; optic configuration makes it function as a sight.
- Character modifiers and diagnostic tools are part of the setup loop. Optics must be checked in runtime view, not just in the prefab editor.
- Base sight properties, 2D scope configuration, scope view, reticle setup, PIP scope setup, and arsenal integration are separate checks. Do not treat a visible optic mesh as a working optic.

Suppressor coverage:
- Suppressor setup spans asset preparation, script/config class compatibility, prefab setup, muzzle integration, stats, sound, effects, catalog exposure, and runtime verification.
- The attachment config class controls compatibility between suppressor and weapon attachment point. Use a unique mod tag for script file and class naming to avoid collisions.
- Recompile or reload scripts after defining the attachment config class before expecting the class to appear in Workbench fields.
- The suppressor prefab should usually inherit from a base suppressor prefab, with a child prefab pattern when variants/reskins are expected.
- Configure `MeshObject`, `InventoryItemComponent`, suppressor attachment attributes, muzzle effect component, optional obstruction attributes, optional action context offsets, and localization.
- Integrate with the weapon by opening the weapon prefab, selecting its muzzle component, adding an `AttachmentSlotComponent` as a child, configuring pivot/child pivot, assigning attachment point type, adding `SCR_WeaponStatsManagerComponent`, and updating `WeaponSoundComponent` for normal/suppressed sound sets.
- Add the suppressor to the relevant Entity Catalog weapon attachments list with weapon-attachment item type/mode and suitable supply cost. Then validate arsenal visibility, inventory pickup, attachment, function with/without suppressor, stats changes, muzzle effects, and sound switching.

Collimator coverage:
- Collimator setup includes projection-plane UV, projection-plane geometry definition, reticle material setup, manual material binding edits, prefab component setup, reticle configuration, and in-game parallax testing.
- The projection plane needs square reticle texture assumptions and correct aimpoint placement. Geometry should not visibly protrude unless the optic design requires it.
- Upper and lower projection-plane edges can be defined with memory points/empties; import scene hierarchy or the sockets will not be available.
- Reticle material setup uses opacity and emissive behavior. The wiki notes that some bindings must be edited in the material file outside Workbench; treat this as a source-backed workflow, not an optional style preference.
- Collimator prefab setup differs from regular optic setup because 2D PIP sights are not desired. Prefer a prefab path that avoids inherited unwanted components where practical.
- Add `SCR_CollimatorSightsComponent` and `SCR_CollimatorControllerComponent` in the required parent/child relationship, then configure sight points and collimator projection/reticle settings.
- Reticle size, texture portion, color arrays, default reticle index, reticle info array, ADS enable/disable percentages, and day/night brightness are separate configuration fields.
- Collimator behavior must be tested in game. The wiki specifically warns that collimator functionality does not work in World Editor; verify parallax/reticle behavior while aiming down sights in runtime.

Stat-modifying attachment coverage:
- Stat modifiers can be applied through attachment attributes and weapon stats manager behavior, not by scattering ad hoc script changes.
- The workflow covers weapon stats that can be modified, attachment/detachment hierarchy, attachment configuration, custom attachment attributes, `SCR_WeaponStatsManagerComponent`, `BaseWeaponStatsManagerComponent`, Set/Clear/Get API families, and a muzzle effects special case.
- If an attachment changes muzzle speed, dispersion, sound, effects, or other weapon stats, verify both the attachment prefab attributes and the weapon-side stats manager integration.

## Terms And Concepts

- Weapon prefab: the configured entity/resource that combines model, inventory, action, weapon, muzzle, magazine, ammo, sound, animation, and attachment behavior.
- Base/child prefab: inheritance structure used to preserve shared configuration while allowing variants, reskins, or playable child resources.
- Weapon component: weapon-specific gameplay component family; verify exact class names through query output before coding.
- Muzzle component: component family controlling muzzle/fire/ammo/magazine relationships and muzzle effects.
- Magazine component: component family controlling magazine item/ammo data and magazine behavior.
- Magazine well: compatibility surface connecting a weapon/muzzle to valid magazines.
- Attachment slot: child component/slot that permits an attachment class to mount at a specific pivot/snap point.
- Attachment type/config class: compatibility class used by attachments and weapons to decide what can mount where.
- Pivot ID: named bone/empty/socket from the imported model or hierarchy used by slot, effect, sight, or attachment placement.
- Child Pivot ID: named point on the child/attachment used to align the attached entity to the parent slot.
- Obstruction: configuration preventing incompatible attachment combinations or enforcing required related attachments.
- Weapon stats manager: component route for applying/clearing attachment-driven weapon stat changes.
- Collimator: sight using projected reticle behavior; must be tested in runtime ADS.
- PIP optic: picture-in-picture optic setup; different from collimator setup.
- Arsenal/catalog exposure: data route that makes weapons or attachments available in crates, arsenals, inventory, or faction equipment lists.

## Workbench / Resource / Data Surfaces

- Resource Browser: locate weapon meshes, materials, textures, prefabs, configs, catalogs, particles, sounds, and scripts.
- Model import settings: preserve hierarchy/sockets where needed, check colliders/materials, register model resources, and verify skeleton/hierarchy.
- Prefab Edit Mode: configure weapon entity tree, components, child components, action contexts, slots, muzzle/magazine components, attachment slots, mesh object, sound component, stats manager, and inventory item attributes.
- Component Properties panel: primary surface for weapon behavior, inventory, actions, muzzle/magazine/ammo links, optics, suppressors, collimators, deployment, zeroing, dispersion, obstruction, and UI info.
- ActionsManagerComponent debug: inspect and repair weapon action context locations/radii when actions do not show or are misplaced.
- Entity Catalog and arsenal configs: expose weapons, magazines, ammo, and attachments to faction or faction-less lists.
- Script Editor: create unique attachment config classes when the weapon/attachment needs new compatibility classes; reload scripts before selecting those classes in Workbench.
- Runtime game test: final authority for ADS, collimator parallax, attachment behavior, magazine compatibility, firing, deployment, sound/effects, inventory, arsenal, and AI behavior.

## Required Workflows

### Create A New Weapon

1. Start from the weapon tutorial and sample family, then decide whether the task is new weapon, variant, retexture, attachment, optic, suppressor, or collimator.
2. Prepare structure so automation and Workbench navigation remain predictable.
3. Prepare mesh:
   - orient model correctly;
   - split body, magazine, moving parts, and attachments as needed;
   - name objects clearly;
   - add slots/snap points and memory points;
   - create colliders with correct material/layer choices;
   - set up skeleton/bones and rig moving pieces;
   - prepare textures/material names.
4. Export/import model:
   - preserve scene hierarchy when sockets are required;
   - register the model;
   - verify colliders/materials, skeleton/hierarchy, sockets, and texture import.
5. Create/configure prefab:
   - build base and child prefab structure where variants are expected;
   - set inventory representation;
   - adjust action contexts;
   - configure weapon behavior, muzzle, magazine, ammo, deployment, zeroing, dispersion, obstruction, and AI target properties.
6. Expose to gameplay:
   - configure magazine well and magazine prefab;
   - add ammo/magazine/weapon to required crates, arsenal configs, or entity catalogs;
   - validate faction/faction-less availability.
7. Test in runtime:
   - spawn/equip weapon;
   - inspect inventory display and item preview;
   - verify actions, magazine compatibility, firing, fire mode, zeroing, deployment, obstruction, AI behavior, effects, audio, and multiplayer/dedicated-server behavior when relevant.

### Modify An Existing Weapon

1. Choose inherited prefab or duplicated variant intentionally.
2. Keep prefab inheritance readable; use apply-to-prefab or inheritance tree based on whether the change belongs to the inherited source or the child.
3. Change component parameters only after identifying the owning component and verifying exact API/source route if code is involved.
4. For new ammo:
   - create ammo config;
   - set ballistic and damage/penetration properties;
   - configure AI ammo targeting where needed;
   - connect ammo to magazine.
5. For new magazine:
   - create magazine prefab/config;
   - assign ammo;
   - apply magazine compatibility to weapon/magazine well.
6. For retexture:
   - create/import material and textures;
   - apply material to weapon asset/prefab variant;
   - validate in game lighting and inventory preview.
7. For sound/effect changes:
   - edit audio/particle resources in their owning tools;
   - assign changed resources to weapon/muzzle/suppressor/explosion components;
   - test firing and attachment states.

### Add A Suppressor

1. Prepare suppressor asset with correct orientation, object naming, snap point, collision mesh, layer preset, game material, export, texture, and material setup.
2. Create or reuse the attachment config class. If creating a new one, use a unique prefix and reload scripts.
3. Create suppressor base prefab and child prefab when variants are expected.
4. Configure suppressor prefab:
   - `MeshObject`;
   - `InventoryItemComponent`;
   - suppressor attachment attributes;
   - muzzle effect component;
   - optional obstruction attributes;
   - optional action context offsets;
   - localization.
5. Integrate with weapon:
   - open weapon prefab;
   - select muzzle component;
   - add child `AttachmentSlotComponent`;
   - configure `Pivot ID`, `Child Pivot ID`, and attachment point type;
   - add `SCR_WeaponStatsManagerComponent`;
   - update `WeaponSoundComponent` with normal/suppressed sound files.
6. Expose suppressor in Entity Catalog or arsenal list with weapon-attachment item type/mode.
7. Test inventory, attachment, firing, sound, muzzle effect, stat changes, and removal.

### Add An Optic

1. Prepare optic mesh with colliders, memory points, slots, points, and optional PIP mesh.
2. Import/register model and set texture/material resources.
3. Create optic prefab and configure inventory item behavior.
4. Configure attachment compatibility so the optic can mount to the intended weapon slot.
5. Configure optic behavior:
   - base sight properties;
   - 2D scope or PIP scope where appropriate;
   - scope view;
   - reticle;
   - character modifiers if needed.
6. Add to arsenal/catalog and test sight alignment, inventory, attachment, ADS, and runtime visuals.

### Add A Collimator

1. Prepare projection plane UV and geometry.
2. Define projection plane upper/lower edges with sockets/empties where possible.
3. Import hierarchy so the points are visible in Workbench.
4. Configure reticle material and required bindings.
5. Create collimator prefab without unwanted PIP components.
6. Add and parent collimator sight/controller components correctly.
7. Configure reticle angular size, texture portion, colors, reticle info array, ADS enable timing, and brightness.
8. Test only in game: ADS state, parallax, reticle movement, movement sway, and day/night brightness.

### Add Stat-Modifying Attachment Behavior

1. Decide whether the attachment modifies speed, dispersion, sound, effect, or other weapon stats.
2. Configure attachment attributes on the attachment prefab.
3. Add or verify the weapon-side stats manager component.
4. Use query output for exact classes and methods before scripting any custom attribute or stats manager behavior.
5. Test attach/detach, stat application, stat clearing, muzzle effects, and sound/effect switching.

## Configuration Fields And Tables

Weapon asset fields and checks:
- Object orientation: must match expected weapon forward/up axes.
- Object cutting: body, magazine, moving parts, attachments, collision pieces as needed.
- Object naming: drives imported material/resource names and Workbench selection clarity.
- Slots/snap points: must exist in imported hierarchy and use stable names.
- Colliders: require correct shape, material, layer preset, and relation to weapon parts.
- Skeleton/bones: required for animated or simulated weapon parts.
- Texture/material resources: verify BCR/NMO/material setup through asset reference when doing broad material work.

Weapon prefab fields and checks:
- Inventory item display name and physical attributes.
- Preview/render attributes for inventory presentation.
- Action contexts: location, radius, offsets, and debug visibility.
- Weapon characteristics and behavior parameters.
- Obstruction phases/configuration.
- Accessory modifiers and stats manager integration.
- Deployment points, base deployment, bipod deployment, IK targets, and aim modifiers.
- Zeroing and dispersion.
- Ammo config, ballistic properties, air drag, ballistic tables, barrel length versus muzzle velocity, penetration, damage, tracer setup.
- AI target selection, priority values, and ballistic tables.
- Magazine well and magazine prefab linkage.
- Crate/arsenal/entity catalog list inclusion.

Weapon component field groups:
- `PointInfo`: `Pivot ID`, `Offset`, `Angles`.
- `EntitySlotInfo`: `Auto Transform`, `Child Pivot ID`, `Enabled`, `Prefab`, `Disable Physics Interaction`, `Inherit Parent Skeleton`, attach/detach physics toggles.
- `EquipmentStorageSlot`: allowed item types, occluders, animated mesh reference.
- `LoadoutSlotInfo`: area and meshes to hide.
- `RegisteringComponentSlotInfo`: register actions, damage, controllers, weapons, compartments, lights.
- UI info: name, description, icon, ammo type, caliber, fire-mode imagesets, magazine indicator, weapon name visibility.

Suppressor fields:
- Attachment type/config class.
- Muzzle speed coefficient.
- Muzzle dispersion factor.
- Obstructed attachment types and required attachment types.
- Muzzle effect particle, effect position, reset-on-fire behavior.
- Weapon sound file list including suppressed firing sound.
- Entity Catalog item type/mode and supply cost.

Optic/collimator fields:
- Sight points and eye point.
- Reticle texture/material.
- Scope view and PIP view settings.
- Collimator projection plane points.
- Reticle angular size and texture portion.
- Reticle color array and reticle info array.
- ADS activation/deactivation percentage.
- Day/night brightness.

## Procedures And Ordered Steps

- New weapon procedure: structure -> mesh -> slots/colliders/skeleton -> export/import -> model registration -> prefab setup -> inventory/action contexts -> weapon behavior -> ammo/magazine/ballistics -> crates/arsenal -> runtime test.
- Weapon variant procedure: inherit or duplicate -> modify prefab/components -> apply or keep override intentionally -> update ammo/magazine/material/sound/effects as required -> test in game.
- Ammo/magazine procedure: create ammo config -> configure ballistics/damage/AI -> create magazine prefab/config -> assign ammo -> connect magazine well -> add to crates/arsenal -> test reload/fire.
- Suppressor procedure: asset -> config class -> prefab -> inventory/attachment attributes -> muzzle effect -> weapon muzzle slot -> stats manager -> sound component -> catalog/arsenal -> attach/fire/remove test.
- Optic procedure: mesh/memory points -> import -> material/reticle -> prefab inventory -> attachment compatibility -> optic/scope settings -> arsenal -> ADS/runtime validation.
- Collimator procedure: projection plane -> geometry points -> material binding -> prefab without unwanted PIP -> sight/controller components -> reticle configuration -> in-game parallax/ADS validation.
- Stat modifier procedure: attribute setup -> stats manager on weapon -> optional custom attributes -> query exact API -> attach/detach tests.

## Warnings And Failure Modes

- Do not guess weapon APIs. Use query commands for every class, method, attribute, inheritance, and example route before writing code.
- A weapon can import cleanly but fail at runtime if sockets, pivots, magazine wells, ammo config, action contexts, or catalog entries are wrong.
- If imported sockets/empties are missing, check export/import scene hierarchy settings before editing prefabs around the missing data.
- If actions do not appear or are hard to interact with, inspect action context location/radius/offset and use action debug routes.
- If attachments do not mount, verify both sides: weapon attachment slot type and attachment prefab/config type.
- If suppressor stats or sounds do not change, verify `SCR_WeaponStatsManagerComponent`, suppressor attributes, and `WeaponSoundComponent`.
- If an attachment should block another attachment, configure obstruction; do not rely on UI expectations alone.
- If a collimator does not behave correctly, test in game, not World Editor. Check UV orientation, projection geometry, reticle material binding, ADS state, and projection plane points.
- Script files do not use metafiles and can collide by path/name. Use a unique mod tag for custom attachment config classes and files.
- Localization affects user-visible attachment and action labels. Missing localization can surface as broken or confusing user actions.
- Weapon animation and audio assignments can make a weapon appear broken even when prefab/component data is correct. Route deeper authoring to animation/audio references, then return here for integration.
- Dedicated server and multiplayer behavior must be verified when weapon behavior is gameplay-relevant, especially deployables, mines, fired projectiles, replicated state, inventory, and attachment state.

## API Lookup Keys

Use these keys for exact lookup. Do not treat this list as an API dump.

- Weapon components: `WeaponComponent`, `BaseWeaponComponent`, `WeaponComponentClass`, `BaseWeaponComponentClass`, `WeaponSlotComponent`, `WeaponSlotComponentClass`.
- Muzzle components: `MuzzleComponent`, `BaseMuzzleComponent`, `MuzzleInMagComponent`, `RocketEjectorMuzzleComponent`, `SCR_RocketEjectorMuzzleComponent`.
- Magazine components: `MagazineComponent`, `BaseMagazineComponent`, `MagazineWell`.
- Attachment and slots: `AttachmentSlotComponent`, `EntitySlotInfo`, `InventoryStorageSlot`, `EquipmentStorageSlot`, `RegisteringComponentSlotInfo`, `SCR_WeaponAttachmentAttributes`, `SCR_WeaponAttachmentSuppressorAttributes`, `SCR_WeaponAttachmentObstructionAttributes`.
- Stats: `SCR_WeaponStatsManagerComponent`, `BaseWeaponStatsManagerComponent`.
- Sound/effects integration: `WeaponSoundComponent`, `SCR_MuzzleEffectComponent`.
- UI and examples: `SCR_WeaponInfoVehicle`, `SCR_WeaponInfo_MultiWeaponTurret`, `SCR_BIKIWeaponHelper`.
- AI weapon examples: `SCR_AIEvaluateExpectedWeapon`, `SCR_AIEvaluateSuppressionWeapon`, `SCR_AIGetMagazineWell`, `SCR_AIGetMuzzleMagazineWell`.

## Game-Data Query Commands

Run exact lookups before writing API-sensitive code:

```powershell
py -3 scripts/query-reforger-data.py lookup "create weapon script" --limit 8
py -3 scripts/query-reforger-data.py examples weapon --limit 8
py -3 scripts/query-reforger-data.py examples weapon --subtopic magazine --limit 8
py -3 scripts/query-reforger-data.py files Weapon --limit 8
py -3 scripts/query-reforger-data.py files BaseWeaponComponent --limit 8
py -3 scripts/query-reforger-data.py files BaseMuzzleComponent --limit 8
py -3 scripts/query-reforger-data.py files BaseMagazineComponent --limit 8
```

Use generated-file routes for exact signatures:

```powershell
py -3 scripts/query-reforger-data.py symbol BaseWeaponComponent --kind class --exact
py -3 scripts/query-reforger-data.py symbol WeaponComponent --kind class --exact
py -3 scripts/query-reforger-data.py symbol BaseMuzzleComponent --kind class --exact
py -3 scripts/query-reforger-data.py symbol MuzzleComponent --kind class --exact
py -3 scripts/query-reforger-data.py symbol BaseMagazineComponent --kind class --exact
py -3 scripts/query-reforger-data.py symbol MagazineComponent --kind class --exact
py -3 scripts/query-reforger-data.py inherits WeaponComponent
```

Use handwritten/game-source examples for implementation patterns:

```powershell
py -3 scripts/query-reforger-data.py snippet scripts/Game/Weapon/SCR_MineWeaponComponent.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/Game/Components/Weapons/SCR_RocketEjectorMuzzleComponent.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/Game/UI/HUD/WeaponInfo/SCR_WeaponInfoVehicle.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/WorkbenchGame/ResourceManager/BIKI/Helpers/SCR_BIKIWeaponHelper.c --line 1 --context 30
```

Use broader discovery only when exact commands miss:

```powershell
py -3 scripts/query-reforger-data.py files AttachmentSlotComponent --limit 8
py -3 scripts/query-reforger-data.py files WeaponStatsManager --limit 8
py -3 scripts/query-reforger-data.py files WeaponSoundComponent --limit 8
py -3 scripts/query-reforger-data.py files Collimator --limit 8
py -3 scripts/query-reforger-data.py files Suppressor --limit 8
py -3 scripts/query-reforger-data.py files Optic --limit 8
```

## Examples And Samples

Official sample routes:
- `SampleMod_NewWeapon`: use for new weapon structure, asset folders, prefab/config layout, and tutorial alignment.
- `SampleMod_ModdedWeapon`: use for inherited or modified weapon patterns, ammo, magazine, entity catalog, arsenal config, particles, sounds, scripts, and UI/resource layout.
- `SampleMod_Main`: use only for relevant arsenal/weapon rack/catalog layout signals.
- Weapon folders in animation samples: use only as cross-reference signals for animation setup; animation authoring belongs to the animation reference.

Raw game-source examples surfaced by query:
- `SCR_MineWeaponComponent` for a concrete handwritten weapon component route.
- `SCR_WeaponComponent` for another weapon component specialization route.
- `SCR_RocketEjectorMuzzleComponent` for muzzle-specific component specialization.
- `SCR_WeaponInfoVehicle` and `SCR_WeaponInfo_MultiWeaponTurret` for fire-mode, muzzle, magazine, turret, and weapon UI information patterns.
- `SCR_BIKIWeaponHelper` for Workbench/resource-manager helper discovery around weapon data.
- AI weapon task files for magazine, muzzle, expected weapon, and suppression weapon examples.

Do not copy sample or source bodies into runtime references. Use sample names for layout direction, query output for exact file/line routes, and snippets only when implementing or debugging a specific task.

## Follow-Up Keywords

- weapon creation
- weapon prefab
- weapon asset preparation
- weapon modding
- weapon components
- weapon slots
- weapon bones
- muzzle component
- magazine well
- magazine prefab
- ammo config
- ballistics
- ballistic table
- penetration
- tracer projectile
- deployment
- bipod
- obstruction
- zeroing
- dispersion
- optic
- PIP scope
- reticle
- collimator
- suppressor
- attachment slot
- attachment config class
- weapon stats manager
- arsenal
- entity catalog
- crate filling
- action context
- ActionsManagerComponent debug

## Verification

Before accepting weapon work:

- Asset/import: verify model orientation, object naming, colliders, material assignments, layer presets, skeleton/hierarchy, slots/snap points, textures, and imported sockets.
- Prefab: verify base/child inheritance, inventory item display/preview, action contexts, weapon behavior, muzzle, magazine, ammo, deployment, obstruction, zeroing, dispersion, AI properties, sound/effects, and stats manager.
- Attachments: verify attachment type compatibility, pivot/child pivot alignment, attach/detach, obstruction, stats changes, muzzle effects, sound switching, localization, and inventory display.
- Optics/collimators: verify ADS alignment, sight points, eye point, reticle, scope/PIP/collimator behavior, parallax, brightness, and runtime-only collimator behavior.
- Ammo/magazines: verify magazine compatibility, reload, ammo use, tracer behavior, ballistic behavior, damage/penetration, and AI selection.
- Catalog/arsenal/crates: verify the weapon, magazines, ammo, and attachments appear in the intended faction or faction-less lists with correct item type/mode/cost.
- Runtime: test in a real game session, not only in Workbench. Include dedicated-server or multiplayer verification for gameplay-affecting behavior.
- API: rerun query commands for every uncertain class/method/attribute before changing scripts.

## Official Wiki Links

- Weapon Creation: https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Creation
- Weapon Creation/Asset Preparation: https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Creation/Asset_Preparation
- Weapon Creation/Prefab Configuration: https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Creation/Prefab_Configuration
- Weapon Modding: https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Modding
- Weapon Components: https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Components
- Weapon Slots And Bones: https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Slots_And_Bones
- Weapon Optic Creation: https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Optic_Creation
- Weapon Suppressor Creation: https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Suppressor_Creation
- Weapon Collimator Creation: https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Collimator_Creation
- Weapon Stats-Modifing Attachments: https://community.bistudio.com/wiki/Arma_Reforger:Weapon_Stats-Modifing_Attachments

## Usefulness Score

Score: `92/100`

- Wiki coverage: `28/30`
  - All ten owned weapon wiki pages are represented with official URLs, workflow ownership, section coverage, structured record coverage, and exclusions.
  - Dense pages are condensed into operational guidance rather than copied; no known owned page is missing.
  - Minor deduction because exact screenshot-only details are represented as editor surface guidance, not reproduced visually.
- Operational detail: `14/15`
  - Preserves weapon asset, prefab, ammo, magazine, attachment, suppressor, optic, collimator, stat modifier, catalog, and testing workflows.
  - Minor deduction because exact UI field order can still vary by Workbench version and must be verified in the editor.
- API lookup usefulness: `15/15`
  - API-sensitive areas have concrete lookup keys and query commands for symbols, files, examples, inheritance, and snippets.
- Example grounding: `9/10`
  - Official weapon samples and raw game-source example families are named and routed.
  - Minor deduction because source bodies are intentionally not embedded.
- Codex task usefulness: `14/15`
  - A Codex task can route from "create/modify weapon/attachment" to workflow, query command, sample family, and verification loop.
  - Minor deduction because very deep animation/audio authoring intentionally routes to other references.
- Context efficiency: `8/10`
  - Dense and navigable without broad API dumps or copied wiki bodies.
  - Minor deduction because weapon prefab configuration is inherently broad and requires careful section scanning.
- Verification guidance: `4/5`
  - Includes Workbench, asset import, runtime, arsenal/catalog, attachment, and multiplayer/dedicated-server checks.
  - Minor deduction because exact project-specific validation commands are not knowable from the reference alone.

Category-fit check:
- Source family complete: pass. Weapon creation, asset preparation, prefab configuration, modding, components, slots/bones, optics, suppressors, collimators, and stat modifiers are represented.
- No owned page missing: pass. Every owned primary wiki page appears in `Source Inventory` and `Official Wiki Links`.
- Split boundary justified: pass. Generic asset import, generic prefab/configs, generic lifecycle, gear/inventory, animation, and audio are explicitly routed elsewhere.
- Cross-links present: pass through named owner references and follow-up keywords.
- Task route clear: pass. Create weapon, modify weapon, add suppressor, add optic, add collimator, add stat modifier, and verify ammo/magazine routes are covered.

Missed coverage and exclusions:
- No owned primary wiki page was skipped.
- Screenshot-only details are not embedded; their operational meaning is preserved.
- Exact API signatures and source code bodies are intentionally excluded and must be pulled through `scripts/query-reforger-data.py`.
- Weapon animation/audio deep authoring and character gear inventory are intentionally deferred to their owning references.
