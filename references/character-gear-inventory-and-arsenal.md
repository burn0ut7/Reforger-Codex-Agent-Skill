# Character Gear Inventory And Arsenal

## When To Read

Read this when the task is about wearable character equipment and player inventory exposure:

- creating headgear, helmets, vests, or wearable variants;
- preparing wearable gear meshes, skeletons, skinning, colliders, game materials, and item variants;
- configuring `BaseLoadoutClothComponent`, `InventoryItemComponent`, `ClothNodeStorageComponent`, protective colliders, armor damage/pass-through, slots, variants, and arsenal entries;
- routing exact inventory, headgear, cloth/loadout, arsenal, entity catalog, or equipment API lookups;
- debugging gear that does not follow the character, does not collide/protect correctly, cannot be stored, does not appear in arsenal, or has broken inventory preview.

This reference owns character gear and wearable inventory workflows. It does not own generic asset import, generic prefab/config rules, generic component lifecycle, weapon/magazine/ammo setup, or animation authoring.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: Character Gear Creation, headgear creation, headgear asset preparation, headgear prefab configuration, vest creation, vest asset preparation, vest prefab configuration.
- Secondary/cross-reference topics: asset import, prefab/config modeling, entity/component lifecycle, weapon setup, animation, arsenal/entity catalog, inventory scripting.

Wiki pages reviewed:
- Character Gear Creation - https://community.bistudio.com/wiki/Arma_Reforger:Character_Gear_Creation - status: covered - reason: source family router for headgear and vest workflows.
- Character Gear Creation/Headgear - https://community.bistudio.com/wiki/Arma_Reforger:Character_Gear_Creation/Headgear - status: covered - reason: headgear tutorial goal, structure, and step ownership.
- Character Gear Creation/Headgear/Asset Preparation - https://community.bistudio.com/wiki/Arma_Reforger:Character_Gear_Creation/Headgear/Asset_Preparation - status: covered - reason: owned headgear mesh, rigging, skinning, collider, game material, item variant, import, and material workflow.
- Character Gear Creation/Headgear/Prefab Configuration - https://community.bistudio.com/wiki/Arma_Reforger:Character_Gear_Creation/Headgear/Prefab_Configuration - status: covered - reason: owned headgear prefab, loadout cloth, inventory, arsenal, and troubleshooting workflow.
- Character Gear Creation/Vest - https://community.bistudio.com/wiki/Arma_Reforger:Character_Gear_Creation/Vest - status: covered - reason: vest tutorial goal, structure, and step ownership.
- Character Gear Creation/Vest/Asset Preparation - https://community.bistudio.com/wiki/Arma_Reforger:Character_Gear_Creation/Vest/Asset_Preparation - status: covered - reason: owned vest mesh, skinning, collider/protection, material, plate, variant, collection, batch export, and import workflow.
- Character Gear Creation/Vest/Prefab Configuration - https://community.bistudio.com/wiki/Arma_Reforger:Character_Gear_Creation/Vest/Prefab_Configuration - status: covered - reason: owned vest prefab, cloth loadout, inventory/storage, protection, pass-through, variant, slots, arsenal, and testing workflow.

Wiki sections covered:
- Character Gear Creation: headgear and vest tutorial map.
- Headgear: tutorial goal, add new helmet, structure preparation, creation steps.
- Headgear asset preparation: mesh preparation, character orientation/reference model, rigging, importing skeleton, skinning, transfer weights, manual skinning, simple skinning, weight painting, armature modifier, colliders, collider parenting/relations, material research, game material creation, layer preset, item variant, model import, material preparation.
- Headgear prefab configuration: prefab creation, `BaseLoadoutClothComponent`, inventory configuration, arsenal addition, testing/diag, helmet not moving with character, helmet collider issues, cannot store helmet in inventory.
- Vest: tutorial goal, add new vest, structure preparation, creation steps.
- Vest asset preparation: mesh preparation, rigging, skinning, transfer weights, skinning tweaks, armature modifier, colliders, plate setup, material research, material type/density/thickness/kinetic protection, game material creation, layer preset, splitting model, collections, batch FBX export, item variant, model import.
- Vest prefab configuration: prefab creation, `BaseLoadoutClothComponent`, inventory configuration, protection configuration, damage pass-through, variants, equipment part prefab, vest variant, slots, arsenal addition, testing/diag.

Structured wiki records:
- Tables reviewed/included: no table records were present in the indexed pages; field/config details are preserved from sections and procedures.
- Procedures reviewed/included: 30 indexed procedures across headgear and vest pages, covering structure, asset preparation, skinning, collider setup, material setup, prefab configuration, arsenal exposure, and testing.
- Admonitions reviewed/included: 52 indexed admonitions, including Workbench prerequisite notes, hierarchy/import caveats, bone/skinning warnings, collider/protection warnings, model reimport/runtime update caveats, inventory/storage caveats, and arsenal/config warnings.
- Code blocks reviewed/included: no code block records were present in the indexed pages.
- Media reviewed: workflow screenshots and diagrams were reviewed as editor-surface evidence, but runtime references do not depend on images.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts/query-reforger-data.py examples inventory --subtopic character-inventory --limit 8`
  - `py -3 scripts/query-reforger-data.py files CharacterInventory --limit 8`
  - `py -3 scripts/query-reforger-data.py files Inventory --limit 8`
  - `py -3 scripts/query-reforger-data.py files Arsenal --limit 8`
  - `py -3 scripts/query-reforger-data.py files BaseLoadoutClothComponent --limit 8`
  - `py -3 scripts/query-reforger-data.py files SCR_HeadgearInventoryItemComponent --limit 8`
- Symbols/methods/attributes verified as lookup keys: `BaseLoadoutClothComponent`, `BaseLoadoutClothComponentClass`, `InventoryItemComponent`, `SCR_HeadgearInventoryItemComponent`, `ScriptedInventoryStorageManagerComponent`, `SCR_ArsenalInventoryStorageManagerComponent`, `SCR_ArsenalItemListConfig`, `SCR_PlayerArsenalLoadout`, `SCR_EquipClothAction`.
- Examples/snippets reviewed: inventory storage manager, headgear inventory item component, arsenal inventory storage manager, AI inventory/arsenal usage, saline storage/inventory callback, cloth equip action, arsenal item list/config routes.

Samples and source examples:
- Official sample folders reviewed: `SampleMod_NewCharacter`; relevant arsenal/entity catalog routes from `SampleMod_Main`; inventory/catalog routes from weapon samples as cross-reference signals only.
- Raw game-source example families reviewed through query output: character inventory, headgear inventory item, arsenal inventory, inventory storage, cloth equip action, AI inventory/arsenal routes.

Coverage gaps:
- No owned primary wiki page was skipped.
- Generic FBX/model/material detail is intentionally routed to `asset-import-models-materials-and-props.md`; this reference preserves only gear-specific asset requirements.
- Generic prefab/config concepts are routed to `prefabs-configs-containers-and-catalogs.md`; this reference preserves wearable-gear prefab fields and workflows.
- Generic component lifecycle and script patterns are routed to `entities-components-and-lifecycle.md` and `script-events-actions-and-patterns.md`.
- Weapon, magazine, ammo, and attachment setup is routed to `weapons-prefabs-attachments-and-firearms.md`.
- Exact source bodies and API signatures are not embedded; use query commands before writing API-sensitive code.

## Wiki Source Coverage

Character gear creation is split into two official workflow families: headgear and vests. Both follow the same broad shape:

1. prepare a predictable source/resource structure;
2. prepare mesh, skeleton, skinning, colliders, materials, and item variant;
3. import and validate the model;
4. configure the wearable prefab and inventory behavior;
5. expose the item to arsenal/entity catalog routes;
6. test in Workbench/play mode and diagnose common failures.

Headgear source coverage:
- The headgear tutorial teaches FBX import, sockets/skeleton setup, and helmet configuration. It expects Workbench familiarity and routes to official samples.
- Structure is recommended even when not technically required, because automation plugins and navigation depend on predictable organization.
- Character gear orientation differs from many other assets because animation tooling expects a different orientation. Do not blindly rotate equipment; use the provided character/head reference model approach.
- Helmet positioning without references is fragile. Load a reference model and align the item before rigging or import.
- Rigging starts by importing skeleton and empty bones from the character weights template. The headgear source specifically calls out memory points/empty objects as required for animated in-game behavior.
- Skinning can use weight transfer or manual skinning. For simple helmets, the whole mesh can be assigned to the `Head` bone; chin straps or more complex elements may need `FacialJaw`, `Head`, `Neck`, or weight painting.
- The armature modifier links vertex groups to the skeleton. Verify by posing the armature and checking that the mesh follows.
- Helmet protection uses actual colliders. Collider shape should fit the helmet, stay simple, and avoid over-modeling thickness; exact-thickness colliders are not recommended.
- Colliders should be parented to the correct bone, either through Make Parent or Relations tab setup. If a collider appears at the wrong scale, check armature scale.
- Game material research matters for ballistic protection. The wiki route uses material density, thickness, and kinetic resistance instead of treating headgear protection as a visual property.
- Helmet collider layer preset should be `FireGeo`; assign a suitable or inherited game material.
- Create a separate item variant model for the dropped/on-ground item. The item variant does not need a skeleton and can use a simpler collider with an item-oriented layer preset.
- Import both worn and item models, use Register & Import as Model, enable skinning export, reimport when necessary, and verify expected bone/skinned-bone counts before prefab work.
- Material preparation includes assigning BCR/NMO textures and then handling headgear-specific visibility/preview behavior.

Headgear prefab coverage:
- Start from an appropriate headgear base: armored helmet base for helmets, generic headgear base for non-armored headgear, or duplicate an existing helmet when that is faster.
- Keep a base prefab with a base suffix when child variants will change materials or meshes.
- In `BaseLoadoutClothComponent`, enable physics/animated colliders while worn, assign item model, assign worn model, and set sound interaction behavior when the gear should make specific movement sounds.
- Inventory configuration uses `InventoryItemComponent`-style fields: display name, description, physical attributes such as weight, and preview/render attributes.
- Add headgear to arsenal through inventory item/entity catalog configuration; use the correct category/labels for headgear rather than copying weapon labels.
- Testing and diagnosis must cover whether the helmet follows the character, whether colliders/protection work, and whether it can be stored in inventory.

Vest source coverage:
- The vest tutorial follows the same create-structure -> asset preparation -> prefab configuration pattern but adds more protection and variant complexity.
- Vest mesh preparation uses character reference and rigging similar to headgear, but vests are more likely to need multiple bones, weight tweaks, and body-conforming skinning.
- The source notes that applying animation to a rotated vest in Blender can be problematic and that skinning may need follow-up after import. If the model does not update correctly after reimport, use play mode or reload game scripts.
- Vest colliders matter because armor protection uses real collision. Vests can have soft protective fabric and hard plates; model both where needed.
- Vest collider setup should usually use simple single-sided faces and material-defined thickness instead of thick real geometry, because thick colliders can clip through the character and break hit detection when close to the body.
- Plate setup may require multiple colliders attached to different spine bones. This improves body following but can introduce gaps or overlaps in fire geometry in some poses.
- Material research should cover material type, density, thickness, and kinetic protection. The vest source uses ESAPI/boron carbide style research as an example and links kinetic protection back to penetration/material data.
- Create inherited or duplicated game materials so particle effects, sounds, decals, density, thickness, and kinetic resistance remain coherent.
- Assign `FireGeo` layer preset and game material to protective colliders.
- Split vest models when variants need optional parts such as arm/groin protection. Use collection linking and batch FBX export to avoid duplicating shared mesh edits.
- Create item variants for vest-as-item presentation, similar to headgear.
- Import with skinning enabled, verify the full skeleton and skinned bones, and check imported model behavior before prefab setup.

Vest prefab coverage:
- Start from an armored vest base or duplicate an existing vest. Vests may be configured through `ClothNodeStorageComponent` or `InventoryItemComponent`, depending on inherited prefab and desired storage behavior.
- If additional elements such as pouches, arm protection, or groin protection exist, prepare separate equipment-part prefabs.
- In `BaseLoadoutClothComponent`, assign item model, worn model, physics-on-wear behavior, animated colliders, optional sound interaction, and slot data.
- Inventory configuration should prefer `ClothNodeStorageComponent` for vests with attached storage/pouches. Duplicated vanilla prefabs may need component replacement or migration.
- Protective items rely on colliders for protection. Since collider protection is binary, `SCR_ArmorDamageManagerComponent` is used to simulate blunt trauma/pass-through behavior.
- Damage pass-through reduces character resilience from hits stopped by armor. Multiple hits may cause unconsciousness without bleeding or injuries if armor plates stop the bullets.
- Since newer versions configure armored base prefabs with armor damage manager behavior, inheriting from the correct base can avoid missing protection configuration. If inheriting from another prefab, explicitly add/configure the missing manager.
- For variants, create equipment part prefabs first, then create vest child variants that include those equipment parts through `BaseLoadoutClothComponent` slots.
- Gear parts cannot necessarily be attached at runtime; the wiki workflow exposes variants as separate pickup/arsenal items instead.
- Add vest variants to arsenal/entity catalog lists with the correct clothing/vest item categories, item type, and arsenal data.
- Test in play mode and use diag routes to verify visibility, inventory, protection, attached parts, and colliders.

## Terms And Concepts

- Worn model: model shown on the character while equipped.
- Item model: model shown when the gear exists as an item, such as dropped or in item preview.
- Item variant: simplified or repositioned model prepared for ground/inventory representation.
- Protective collider: `FireGeo`/game-material collider used for hit/protection behavior.
- Game material: material resource carrying density, thickness, kinetic resistance, and related impact behavior.
- Skinning: vertex-to-bone weighting that lets gear follow character animation.
- Weight transfer: copying weights from an existing/reference character or gear mesh.
- Manual skinning: assigning vertex groups directly when transfer is not enough.
- Armature modifier: Blender modifier tying mesh vertex groups to the skeleton.
- `BaseLoadoutClothComponent`: wearable cloth/loadout component used to connect worn model, item model, physics/animated colliders, sound interaction, and slots.
- `InventoryItemComponent`: inventory item component route for display, physical attributes, and preview data.
- `ClothNodeStorageComponent`: vest-oriented storage route when gear has pouches/attached storage.
- Equipment part: separate prefab for optional gear pieces that can be included in a wearable variant.
- Protected hit zone: hit-zone/protection configuration used by armor setup.
- Armor damage/pass-through: blunt trauma simulation for hits stopped by protective colliders.
- Arsenal/entity catalog: data routes that make gear available to players, factions, crates, or arsenal systems.

## Workbench / Resource / Data Surfaces

- Blender/Enfusion Blender Tools: align gear to character references, import skeleton/empties, transfer or paint weights, parent colliders, assign game materials/layer presets, split vest variants, and batch export FBX collections.
- Resource Manager: register/import model resources, reimport models, inspect materials, open prefabs, and locate entity catalog or arsenal config resources.
- Prefab Edit Mode: configure `BaseLoadoutClothComponent`, `MeshObject`, `InventoryItemComponent`, `ClothNodeStorageComponent`, equipment part prefabs, slots, preview attributes, protection components, and inventory/arsenal metadata.
- Entity Catalog and Arsenal configs: add headgear, vests, and variants to the intended faction or faction-less item lists.
- Script Editor/API lookup: only for exact class/method verification or custom inventory/gear behavior; do not guess component API from memory.
- Play mode/runtime: final verification for gear following the character, colliders, storage, protection, arsenal visibility, and UI preview.

## Required Workflows

### Create Headgear

1. Use the headgear tutorial as the owning workflow.
2. Prepare a clean resource structure so automation and navigation work.
3. Align the model to a head/character reference rather than guessing orientation.
4. Import skeleton/empty bones from the character template source.
5. Skin the mesh:
   - use weight transfer for normal cases;
   - use simple `Head` assignment for quick/simple helmets;
   - use weight painting for straps or multi-bone influence;
   - add the armature modifier and verify pose movement.
6. Create protective collider geometry:
   - keep it simple;
   - fit helmet shape;
   - parent or relate it to the head bone;
   - assign `FireGeo` and game material.
7. Create or inherit a game material based on density, thickness, and kinetic resistance research.
8. Create an item variant for ground/inventory presentation.
9. Import/register worn and item models with skinning enabled, then check skeleton/skinned-bone results.
10. Create or duplicate a headgear prefab.
11. Configure `BaseLoadoutClothComponent`, `MeshObject`, inventory display/physical/preview fields, and arsenal/entity catalog entries.
12. Test in play mode: follows head, stores in inventory, appears in arsenal, colliders protect, preview looks correct.

### Create A Vest

1. Use the vest tutorial as the owning workflow.
2. Prepare model and reference setup like headgear, but expect more skinning and protection complexity.
3. Skin the vest to the character skeleton; use transfer weights and then revisit weight paint after import if needed.
4. Build protective colliders:
   - model soft and hard protection where appropriate;
   - prefer simple single-sided plate/fabric collider surfaces with material-defined thickness;
   - assign colliders to correct spine or body bones;
   - avoid geometry that clips or sits too close to the character body.
5. Research and create game materials for ballistic behavior: material type, density, thickness, kinetic protection.
6. Assign `FireGeo` and game materials to colliders.
7. Split optional vest parts into separate export collections when variants need add-ons.
8. Batch export FBX collections where useful.
9. Create item variant models for item/ground representation.
10. Import/register models with skinning enabled and verify skeleton/skinned-bone state.
11. Create base vest prefab from a suitable armored vest base or duplicate an existing vest.
12. Configure `BaseLoadoutClothComponent`, item/worn models, sound interaction, inventory/storage component, protection, and preview.
13. Configure `SCR_ArmorDamageManagerComponent` when needed for blunt trauma/pass-through behavior.
14. Create equipment part prefabs for optional pieces, then create vest variant child prefabs and add slots pointing to those parts.
15. Add the vest/variant to arsenal/entity catalog lists with correct item category and arsenal data.
16. Test inventory, preview, wearable fit, storage, protection, attached parts, arsenal visibility, and runtime behavior.

### Add Gear To Arsenal Or Catalog

1. Identify the correct faction or faction-less inventory item catalog/config.
2. Override or extend the catalog/config in the addon.
3. Add a new entity entry pointing to the gear prefab.
4. Add the correct arsenal data entry and item type/category:
   - headgear/head cover for helmets/headgear;
   - vest/waist for vest equipment;
   - avoid weapon labels and weapon-specific item modes.
5. Set display/preview/supply-related data as appropriate for the owning system.
6. Test in the intended arsenal/crate/faction context, not only by spawning the prefab manually.

### Debug Gear Failures

- Helmet or vest does not move with the character: check skeleton import, vertex groups, armature modifier, `BaseLoadoutClothComponent`, worn model assignment, and runtime reload/play mode.
- Colliders do not protect: check collider layer preset, game material, collider parenting/relations, protected hit zones, and armor damage manager setup.
- Gear cannot be stored: check inventory component, item model, physical attributes, storage/category compatibility, and entity catalog/arsenal item data.
- Vest add-on does not appear: check equipment part prefab, child variant, `BaseLoadoutClothComponent` slot, prefab field, and inherited parent skeleton setting.
- Item preview is wrong: check item model, preview render attributes, camera distance, and item variant model.
- Arsenal entry missing: check catalog/config override, section/category, entity prefab, arsenal data entry, and faction/faction-less target.

## Configuration Fields And Tables

The current wiki index has no table records for these pages, but the pages contain field and component details that must be preserved.

Headgear asset fields and checks:
- Character/head reference model alignment.
- Skeleton/empty import from character template.
- Vertex groups for simple or multi-bone skinning.
- Armature modifier target.
- Collider object, bone relation, layer preset, and game material.
- Material density, thickness, kinetic resistance, and inherited material behavior.
- Worn model and item variant model.
- Import settings, skinning export, skeleton count, and skinned-bone check.

Headgear prefab fields and checks:
- Base prefab choice: armored helmet base, generic headgear base, or existing helmet duplicate.
- `BaseLoadoutClothComponent`: physics-on-wear, animated colliders on wear, item model, worn model, sound interaction.
- `MeshObject`: object/model assignment.
- `InventoryItemComponent`: display name, description, physical weight, preview render attributes.
- Arsenal/entity catalog data: correct category and prefab route.

Vest asset fields and checks:
- Character reference and skinning source.
- Weight transfer and weight-paint correction.
- Plate/fabric collider setup.
- Material type, density, thickness, kinetic protection.
- Game material and layer preset.
- Export collections for variants.
- Batch FBX export targets.
- Item variant model.

Vest prefab fields and checks:
- Base prefab choice: armored vest base or existing vest duplicate.
- `BaseLoadoutClothComponent`: item model, worn model, physics/animated collider settings, sound interaction, slots.
- `ClothNodeStorageComponent` or `InventoryItemComponent`: storage and inventory behavior.
- `SCR_ArmorDamageManagerComponent`: pass-through/blunt-trauma behavior for protective items.
- Equipment part prefab: mesh/object, inventory/cloth configuration, inherited skeleton.
- Vest variant: display fields, preview render attributes, protected hit zones, slots, add-on prefab assignment.
- Arsenal/entity catalog data: vest/waist item type/category and faction or faction-less list.

## Procedures And Ordered Steps

- Headgear pipeline: structure -> align to reference -> import skeleton/empties -> skin -> add armature -> create protective colliders -> create game material -> assign `FireGeo` -> create item variant -> import/register models -> create prefab -> configure loadout cloth/inventory -> add to arsenal -> test.
- Vest pipeline: structure -> align to reference -> skin/weight transfer -> tweak weights -> create soft/hard colliders -> research material -> assign game material/layer -> split variants -> batch export -> create item variant -> import/register models -> create base prefab -> configure storage/protection -> create equipment parts/variant slots -> add to arsenal -> test.
- Arsenal pipeline: choose target catalog/config -> override/extend -> add entity prefab -> add arsenal data -> set item type/category -> test in intended faction/crate/arsenal context.
- Protection pipeline: collider setup -> material data -> protected hit-zone/armor manager setup -> play-mode hit/protection validation.
- Troubleshooting pipeline: verify imported model and skeleton first, then prefab component assignments, then catalog/arsenal data, then runtime/diag behavior.

## Warnings And Failure Modes

- Do not guess inventory, loadout, cloth, or arsenal APIs. Query exact game data before writing scripts.
- Structure is not always engine-mandatory, but the wiki recommends it because automation plugins and navigation depend on it.
- Character gear orientation differs from many other assets. Avoid old advice to rotate blindly; use current reference orientation and sample workflows.
- If imported sockets/empties/skeleton are missing, fix export/import hierarchy and skinning settings before compensating in the prefab.
- Protective gear uses actual colliders. Visual mesh alone does not provide protection.
- Thick or overly realistic vest colliders can clip into the body and break hit detection; use simpler collider surfaces and material-defined thickness where the wiki recommends it.
- Protective collider behavior is binary without additional damage manager behavior. Use armor damage/pass-through setup for blunt trauma behavior.
- Vest skinning may not update correctly after reimport until play mode or script reload is used.
- Runtime attachability of equipment parts is limited; expose preconfigured vest variants rather than assuming players can attach every part dynamically.
- Missing or incorrect catalog/arsenal data can make valid gear prefabs unavailable in actual gameplay.
- Inventory storage failures usually come from component/category/physical attribute/storage compatibility, not from the mesh alone.
- Dedicated server and multiplayer checks are still required for gameplay-relevant inventory, arsenal, and loadout behavior.

## API Lookup Keys

Use these as exact query keys, not embedded API truth:

- Wearable/loadout: `BaseLoadoutClothComponent`, `BaseLoadoutClothComponentClass`, `LoadoutAreaType`.
- Inventory: `CharacterInventory`, `InventoryItemComponent`, `InventoryStorageManagerComponent`, `ScriptedInventoryStorageManagerComponent`, `ScriptedInventoryOperationCallback`.
- Headgear: `SCR_HeadgearInventoryItemComponent`, `SCR_HeadgearInventoryItemComponentClass`.
- Arsenal: `SCR_ArsenalInventoryStorageManagerComponent`, `SCR_ArsenalItemListConfig`, `SCR_ArsenalItemDisplayData`, `SCR_EArsenalItemType`, `SCR_PlayerArsenalLoadout`.
- Equip/use flow: `SCR_EquipClothAction`, `SCR_InventoryAction`, `SCR_SalineStorageComponent`.
- Protection: `SCR_ArmorDamageManagerComponent`, protected hit zones, hit-zone related data.
- Resource/config routing: `ResourceName`, entity catalog entries, inventory item configs.

## Game-Data Query Commands

Run these before writing API-sensitive gear, inventory, or arsenal code:

```powershell
py -3 scripts/query-reforger-data.py examples inventory --subtopic character-inventory --limit 8
py -3 scripts/query-reforger-data.py files CharacterInventory --limit 8
py -3 scripts/query-reforger-data.py files Inventory --limit 8
py -3 scripts/query-reforger-data.py files Arsenal --limit 8
py -3 scripts/query-reforger-data.py files BaseLoadoutClothComponent --limit 8
py -3 scripts/query-reforger-data.py files SCR_HeadgearInventoryItemComponent --limit 8
```

Use exact symbol and inheritance checks when coding:

```powershell
py -3 scripts/query-reforger-data.py symbol BaseLoadoutClothComponent --kind class --exact
py -3 scripts/query-reforger-data.py symbol SCR_HeadgearInventoryItemComponent --kind class --exact
py -3 scripts/query-reforger-data.py files SCR_EquipClothAction --limit 8
py -3 scripts/query-reforger-data.py files SCR_ArsenalItemListConfig --limit 8
py -3 scripts/query-reforger-data.py files SCR_PlayerArsenalLoadout --limit 8
```

Use bounded snippets only after selecting an exact source file:

```powershell
py -3 scripts/query-reforger-data.py snippet scripts/Game/Inventory/Items/SCR_HeadgearInventoryItemComponent.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/Game/UserActions/SCR_EquipClothAction.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/Game/Components/Arsenal/SCR_ArsenalInventoryStorageManagerComponent.c --line 1 --context 30
```

## Examples And Samples

Official sample routes:
- `SampleMod_NewCharacter`: primary layout signal for character/gear workflows.
- `SampleMod_Main`: arsenal config and entity catalog layout signals.
- Weapon sample inventory/catalog routes: cross-reference only; weapon setup remains in `weapons-prefabs-attachments-and-firearms.md`.
- Cinematic character animation samples: cross-reference only; animation authoring remains in `animation-graphs-weapon-animation-and-export.md`.

Raw game-source examples surfaced by query:
- `SCR_HeadgearInventoryItemComponent` for headgear inventory item behavior.
- `ScriptedInventoryStorageManagerComponent` for scripted inventory storage manager route.
- `SCR_ArsenalInventoryStorageManagerComponent` and `SCR_ArsenalItemListConfig` for arsenal/inventory routing.
- `SCR_EquipClothAction` for cloth equip action flow.
- AI inventory and arsenal task files for scripted inventory and arsenal usage patterns.
- Storage/item examples such as saline storage for inventory callback and item insertion routes.

Do not copy sample or source bodies into runtime references. Use samples for layout, query output for exact file/line routes, and snippets only for bounded implementation context.

## Follow-Up Keywords

- character gear
- headgear
- helmet
- vest
- wearable equipment
- inventory
- arsenal
- entity catalog
- loadout cloth
- BaseLoadoutClothComponent
- InventoryItemComponent
- ClothNodeStorageComponent
- protective collider
- FireGeo
- game material
- density
- thickness
- kinetic resistance
- skinning
- transfer weights
- weight paint
- armature modifier
- item variant
- worn model
- item model
- equipment part
- vest variant
- protected hit zone
- armor damage manager
- damage pass-through
- preview render attributes
- gear storage

## Verification

Before accepting character gear work:

- Asset/import: verify orientation, reference alignment, skeleton/empty import, vertex groups, skinning/weights, armature modifier, colliders, game materials, layer presets, item variant, import settings, and skinned-bone state.
- Headgear: verify helmet follows the head, collider protection works, inventory storage works, item preview looks correct, and arsenal entry appears.
- Vest: verify vest follows body animation, plate/fabric colliders align through poses, armor damage/pass-through behavior works, optional equipment parts appear on variants, inventory storage works, and preview/camera distance is usable.
- Catalog/arsenal: verify the gear appears in the intended faction or faction-less arsenal/crate route with the correct item category and prefab.
- Runtime: test in play mode or game runtime, not only in prefab/resource view. Use diag routes for hit/protection/collider issues.
- API: run query commands for every uncertain class, method, attribute, inheritance, example, or snippet before changing scripts.
- Multiplayer/server: verify loadout, inventory, and arsenal behavior in multiplayer or dedicated-server context when the gear affects gameplay availability.

## Official Wiki Links

- Character Gear Creation: https://community.bistudio.com/wiki/Arma_Reforger:Character_Gear_Creation
- Character Gear Creation/Headgear: https://community.bistudio.com/wiki/Arma_Reforger:Character_Gear_Creation/Headgear
- Character Gear Creation/Headgear/Asset Preparation: https://community.bistudio.com/wiki/Arma_Reforger:Character_Gear_Creation/Headgear/Asset_Preparation
- Character Gear Creation/Headgear/Prefab Configuration: https://community.bistudio.com/wiki/Arma_Reforger:Character_Gear_Creation/Headgear/Prefab_Configuration
- Character Gear Creation/Vest: https://community.bistudio.com/wiki/Arma_Reforger:Character_Gear_Creation/Vest
- Character Gear Creation/Vest/Asset Preparation: https://community.bistudio.com/wiki/Arma_Reforger:Character_Gear_Creation/Vest/Asset_Preparation
- Character Gear Creation/Vest/Prefab Configuration: https://community.bistudio.com/wiki/Arma_Reforger:Character_Gear_Creation/Vest/Prefab_Configuration

## Usefulness Score

Score: `91/100`

- Wiki coverage: `28/30`
  - All seven owned character gear pages are represented with official URLs, workflow coverage, structured record coverage, and exclusions.
  - Procedures and warnings are preserved; no owned page is missing.
  - Minor deduction because image-only editor state is represented as operational guidance, not reproduced visually.
- Operational detail: `14/15`
  - Preserves headgear and vest asset preparation, prefab setup, inventory, protection, variant, arsenal, and testing workflows.
  - Minor deduction because exact Workbench field ordering may vary and must be verified in the editor.
- API lookup usefulness: `15/15`
  - Includes concrete query commands for inventory examples, character inventory, inventory, arsenal, cloth/loadout, and headgear routes.
- Example grounding: `9/10`
  - Names official sample routes and raw game-source example families.
  - Minor deduction because source/sample bodies are intentionally not embedded.
- Codex task usefulness: `14/15`
  - Routes common gear tasks from intent to workflow, query commands, sample routes, and validation.
  - Minor deduction because broad asset/material and animation authoring intentionally route to other references.
- Context efficiency: `7/10`
  - Dense and navigable without copied wiki dumps or broad API dumps.
  - Deducted because headgear and vest workflows are both detailed and share some repeated setup concepts.
- Verification guidance: `4/5`
  - Includes asset, prefab, inventory, protection, arsenal, runtime, and multiplayer/server checks.
  - Minor deduction because project-specific validation commands are not knowable from the reference alone.

Category-fit check:
- Source family complete: pass. Character gear, headgear, headgear asset/prefab, vest, and vest asset/prefab workflows are represented.
- No owned page missing: pass. Every owned primary wiki page appears in `Source Inventory` and `Official Wiki Links`.
- Split boundary justified: pass. Generic asset import, prefab/configs, lifecycle, weapons, and animation are explicitly routed elsewhere.
- Cross-links present: pass through named owner references and follow-up keywords.
- Task route clear: pass. Create headgear, create vest, add to arsenal/catalog, configure protection, debug inventory, and verify runtime routes are covered.

Missed coverage and exclusions:
- No owned primary wiki page was skipped.
- Table/code-block records were absent in the current wiki index for these pages.
- Screenshot-only details are not embedded; their operational meaning is preserved.
- Exact API signatures and source code bodies are intentionally excluded and must be pulled through `scripts/query-reforger-data.py`.
