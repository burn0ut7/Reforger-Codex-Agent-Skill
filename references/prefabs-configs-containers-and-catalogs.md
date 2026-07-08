# Prefabs, Configs, Containers, And Catalogs

## When To Read

Read this reference when the task is about Reforger data modeling: prefab inheritance, prefab overrides, config classes, config object prefabs, component prefabs, `BaseContainer`, `ResourceName`, resource loading, prefab spawning, entity catalogs, catalog entry data, or wiring resource references into editable data.

Do not use this as the primary owner for Resource Manager editor controls, generic entity/component lifecycle, script language syntax, or domain-specific prefab recipes. Resource Manager owns the editor surfaces. Entity lifecycle owns runtime entity/component semantics. Weapon, vehicle, UI, animation, audio, terrain, server, and scenario references own their narrow prefab/config recipes.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: prefab concepts and operations, data moddability, config class creation, `BaseContainer` usage, entity catalog setup, prefab data routing, and config object/BaseContainer semantics.
- Secondary/cross-reference topics: Resource Manager Config Editor, Resource Manager file/editor surfaces, generic entity/component lifecycle, domain-specific weapon/vehicle/UI/asset prefab setup, and project packaging.

Wiki pages reviewed:
- Prefabs Basics - https://community.bistudio.com/wiki/Arma_Reforger:Prefabs_Basics - status: covered - reason: owns prefab glossary, entity/component/config object prefab types, prefab operations, instancing, inheritance, overrides, edit mode, unprefabing, duplicating, and apply-to-prefab workflows.
- Prefab Data - https://community.bistudio.com/wiki/Arma_Reforger:Prefab_Data - status: covered - reason: owns prefab-data requirements and code/example routing for entity/component class preparation.
- Data Modding Basics - https://community.bistudio.com/wiki/Arma_Reforger:Data_Modding_Basics - status: covered - reason: owns moddability rules, inherit/modify/replace distinctions, override and replace workflows, GUID requirements, script override notes, and Workbench generated-file warnings.
- Create a Config Class - https://community.bistudio.com/wiki/Arma_Reforger:Create_a_Config_Class - status: covered - reason: owns config class creation, class setup, root visibility, config file creation, and example route.
- BaseContainer Usage - https://community.bistudio.com/wiki/Arma_Reforger:BaseContainer_Usage - status: covered - reason: owns `BaseContainer` structure, inheritance, object arrays, create/read/update usage, config/entity-source/localization/meta-file cases, and update limitations.
- Entity Catalog - https://community.bistudio.com/wiki/Arma_Reforger:Entity_Catalog - status: covered - reason: owns catalog config structure, entity entries, entry classes, entry info, entry data, and catalog examples.
- Scripting: Config Object - https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Config_Object - status: partial - reason: this reference owns config object/BaseContainer decorators and editor visibility semantics; general language syntax remains in `enfusion-language-and-script-editor.md`.
- Resource Manager: Config Editor - https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Config_Editor - status: partial - reason: this reference names Config Editor only where data modeling requires it; full editor controls remain in `resource-manager-file-types-and-editors.md`.

Wiki sections covered:
- Prefabs Basics > Glossary > prefab, prefab root, prefab member, prefab instance, prefab instance member, entity prefab, component prefab, config object, config object prefab, prefab edit mode - coverage: represented as core concepts.
- Prefabs Basics > Prefabs operations > creating entity prefab, creating component prefab, creating config object prefab, instancing, adding/deleting entities, editing properties, opening prefab edit mode, creating inherited prefab, overriding, unprefabing, duplicating, changing class - coverage: represented as ordered workflows and failure modes.
- Data Modding Basics > Content Moddability Overview > can be inherited from, can be modified, can be replaced, moddability table and footnotes - coverage: represented as the decision model before changing base-game data.
- Data Modding Basics > Data manipulation > basics, inheriting, transfer to, duplicate to, override in, navigate to, replacing assets, replacing script, script `modded`/`override`/`super` notes - coverage: represented as override/replace workflows and warnings.
- Create a Config Class > creation, class, make it root, config file creation, example - coverage: represented as config class workflow and verification.
- BaseContainer Usage > structure, inheritance, object array, create, read, config, `IEntitySource`, localization, meta file, update, WorldEditorAPI - coverage: represented as typed container usage, persistence warning, and API lookup routes.
- Entity Catalog > catalog, entity entry, entry classes, entry info, entry data, examples - coverage: represented as catalog structure and query routes.
- Scripting: Config Object > Config Base Container Class > Attribute, BaseContainerProps - coverage: represented as decorator and naming-convention requirements.
- Resource Manager: Config Editor > search field, class, parent, values, array, slider, config prefab from config, inherited config file, filling by config - coverage: represented as cross-reference only.

Structured wiki records:
- Tables reviewed/included: Data Modding Basics moddability table; Data Modding Basics data manipulation basics table; Entity Catalog catalog table; Entity Catalog entry classes table; Entity Catalog entry info table; Entity Catalog entry data examples table; Prefab Data code example table; Scripting: Config Object `Attribute` and `BaseContainerProps` tables.
- Procedures reviewed/included: config file creation; prefab operation steps; BaseContainer create/read/update flows; Data Modding inherit/override/replace flows; Entity Catalog setup and entry data flows.
- Admonitions reviewed/included: `BaseContainer` cannot be strongly referenced; typed `Get`/`Set` requirements; `Set` cannot create arbitrary properties; nested update paths are required; `IEntitySource` persistence requires the correct editor API path; `Attribute` and `BaseContainerProps` are required for Config Editor visibility; `configRoot` is required for root config creation; some data cannot be fully replaced; replacing Workbench-generated files is risky; prefab edit mode can discard unsaved world-editor state if handled carelessly; prefab override indicators matter.
- Code blocks reviewed/included: config object examples, BaseContainer read/update examples, prefab-data example, and Resource.Load routes were reviewed. Full source bodies are not copied here.
- Media reviewed: prefab operation screenshots and editor imagery were treated as workflow confirmation only; this runtime reference preserves the steps and concepts rather than depending on images.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts\query-reforger-data.py symbol ResourceName --exact`
  - `py -3 scripts\query-reforger-data.py method Resource Load --exact`
  - `py -3 scripts\query-reforger-data.py files BaseContainer --limit 10`
  - `py -3 scripts\query-reforger-data.py files EntityCatalog --limit 10`
  - `py -3 scripts\query-reforger-data.py examples resource-loading --subtopic resource-load --limit 8`
  - `py -3 scripts\query-reforger-data.py examples resource-loading --subtopic spawn-prefab --limit 8`
  - `py -3 scripts\query-reforger-data.py files ResourceNamePicker --limit 8`
  - `py -3 scripts\query-reforger-data.py files PrefabResource --limit 8`
- Symbols/methods/attributes verified as lookup routes: `ResourceName`, `Resource.Load`, `BaseContainer`, `BaseResourceObject`, `IEntitySource`, `IEntityComponentSource`, `ResourceNamePicker`, `PrefabResource`, `EntitySpawnParams`, `SpawnEntityPrefab`, `SCR_BaseEntityCatalogData`, entity catalog entry data classes, `Attribute`, `BaseContainerProps`, `NamingConvention`.
- Examples/snippets reviewed: resource loading, resource picker, prefab spawn, catalog spawner, arsenal/catalog data, and BaseContainer-generated API files were reviewed through query output.

Samples and source examples:
- Official sample folders reviewed: `SampleMod_Main`, `SampleMod_ModdedWeapon`, `SampleMod_NewCar`, `SampleMod_ModdedCar`, `SampleMod_NewCharacter`, `SampleMod_CinematicTutorial`, and `SampleMod_ModdedScript` as prefab/config/catalog layout signals only.
- Raw game-source example families reviewed through query output: game mode resource loading, prefab spawning, catalog entity spawners, arsenal entity catalog data, AI prefab lookup, editable entity prefab logic, and ResourceNamePicker use.

Coverage gaps:
- Missing, excluded, or intentionally deferred source: full Resource Manager editor operation, entity lifecycle semantics, component lifecycle/event masks, weapon prefab fields, vehicle compartment setup, UI layout behavior, terrain/world prefab tools, server config, and packaging.
- Reason and impact: those are source-heavy workflows with separate owners. This reference keeps generic prefab/config/data modeling so Codex can route to the right domain reference before applying domain-specific fields.

## Wiki Source Coverage

Prefabs are the core data reuse mechanism. A prefab stores a root object plus owned members and changed values, and prefab instances reuse or override that stored data. The wiki distinguishes entity prefabs, component prefabs, config object prefabs, prefab roots, prefab members, prefab instances, instance members, and prefab edit mode. Keep those distinctions clear before changing `.et`, `.ct`, `.conf`, or catalog data.

Prefab concepts:
- A prefab is reusable saved data, not just a copied object.
- A prefab root is the top object of the stored prefab.
- A prefab member is data owned by that prefab.
- A prefab instance is a placed or referenced use of a prefab.
- A prefab instance member belongs to a prefab instance and may carry local overrides.
- An entity prefab stores entity hierarchy and entity/component values.
- A component prefab stores reusable component configuration.
- A config object prefab stores reusable config-object data.
- Prefab edit mode is a special editing context for a prefab; treat it as a separate state from normal scene editing.

Prefab operations from the wiki:
- Creating an entity prefab requires a valid single-root hierarchy before saving the entity instance as a new prefab.
- Creating component prefabs starts from an entity with the required component selected, then saves component data as a `.ct` prefab.
- Creating config object prefabs stores reusable config object data for config workflows.
- Instancing entity prefabs can be done through drag/drop, copy/paste, or editor search/open behavior such as the F1 workflow.
- Instancing component and config object prefabs reuses stored component/config data rather than duplicating values manually.
- Adding entities to a prefab keeps hierarchy when child entities are present.
- Deleting entities from a prefab changes the stored prefab composition, not only one visible instance, when done in prefab context.
- Editing entity prefab properties can be done through prefab edit mode, inheritance, or apply-to-prefab style workflows.
- Editing component prefab properties changes reusable component data and must be distinguished from one entity instance override.
- Creating inherited prefabs can use drag/drop or an inherit-prefab option.
- Duplicating a prefab creates a separate data asset; inheritance keeps a relationship to the original.
- Unprefabing breaks the prefab relationship for that data.
- Changing class changes the underlying class for the prefab/object and must be treated as a structural change.
- Prefab overriding is tracked through property indicators; Codex must preserve whether a value is inherited, stored in the prefab, or overridden in an instance.

Data Modding Basics is the decision layer before changing existing game data:
- "Can be inherited from" means the new addon data can derive from the original and override only selected values.
- "Can be modified" means data can be changed through override-style mechanisms without replacing the whole file.
- "Can be replaced" means the original file can be replaced by another file with the same identity/relationship.
- Any file with a metadata file and unique GUID is potentially override/replace capable, but exact behavior depends on the asset type and table notes.
- Some asset families are always overridden and cannot be fully replaced.
- Script files with the same path in another addon are fully replaced, and script overrides may require `modded`, `override`, and `super` semantics. Use the script references before changing code.
- Behavior trees attempt to override each other rather than replace in the normal file-replacement sense.
- Replacing files outside Workbench can be risky because Workbench-generated files may be broken by hand edits.

Data manipulation workflows:
- Inheriting keeps a relationship to the original. Use inherit or transfer workflows when the desired change should track upstream data.
- Overriding edits or stores changed data for an asset in the addon. Use duplicate/override/navigate workflows for prefabs, layouts, and configs when supported.
- `Duplicate to...` is available only for prefabs, layouts, or configs and creates a separate copy.
- `Override in...` is available only for prefabs, layouts, or configs, and is unavailable if an override already exists in the working addon.
- Navigate-to-original, navigate-to-ancestor, and navigate-to-override options are context tools for existing override/replacement relationships.
- Replacing assets may require operations outside Workbench and should be reserved for cases where inheritance/override cannot express the desired change.
- Getting the file GUID matters for replacement workflows; preserve GUID intent and metadata relationships.

Config class creation:
- A config class must be declared so the Config Editor can create and edit config data.
- Root config visibility requires root configuration metadata, not just a script class existing.
- The config file creation workflow is separate from language syntax; use this reference for data modeling and `enfusion-language-and-script-editor.md` for syntax or decorator details.
- Config class examples are useful for shape, but exact API and attributes must be checked through query commands.

`BaseContainer` is the scripted access surface for structured data:
- Structure includes inheritance and object arrays.
- A `BaseContainer` itself cannot be strongly referenced in script.
- Reads must provide the correct target variable type. If a value requires `ResourceName`, provide `ResourceName`, not a plain string.
- `Get` must receive a variable of the correct type as its second argument.
- `Set` can update defined class properties, but cannot invent random new properties.
- Nested values require a defined path.
- `IEntitySource` persistence requires the correct editor API path; changing only the in-memory container is not enough for saved world or prefab data.
- The wiki includes separate read cases for config, entity source, localization, and metadata files; keep those cases distinct.

Config object decorators from the wiki:
- `Attribute` on member variables is required for values to be visible and editable in Config Editor.
- The minimum visible/editable member decorator is `Attribute()`.
- `BaseContainerProps` is required for a config object class to be visible and editable in Config Editor.
- A root config object requires `BaseContainerProps(configRoot: true)` for creation as a base object config.
- Classes inheriting from a decorated config class must also be decorated to be usable.
- Naming convention matters: GUID/name requirements affect how the config appears and whether it can be created/identified correctly.

Entity Catalog:
- Catalog config should own entity lists; do not edit faction lists directly when the catalog config is the intended source.
- Factionless catalogs list prefabs that do not belong to a specific faction.
- Catalog entries are config entries.
- Entity entry classes are specialized by entry purpose; the wiki examples are not an exhaustive or always-current list.
- Entry info stores display and descriptive data for a catalog entry.
- Entry data stores additional typed data that can be filtered or queried by catalog API.
- The catalog has an API route for retrieving entries with specific data; verify exact names and signatures through game-data queries before writing code.

Prefab Data:
- Entity and component class classes are required for entities and components.
- Prefab data examples are useful for routing but should not be copied as an API dump.
- Use query commands for `PrefabResource`, resource loading, and prefab spawning before writing code that consumes prefab data.

## Terms And Concepts

- Prefab: reusable stored data asset.
- Prefab root: top object of a prefab.
- Prefab member: object or data owned by the prefab.
- Prefab instance: use of a prefab in another context.
- Prefab instance member: member belonging to an instance and potentially carrying overrides.
- Entity prefab: prefab containing entity hierarchy and component data.
- Component prefab: prefab containing reusable component data.
- Config object: structured config data object.
- Config object prefab: reusable config object data.
- Prefab edit mode: special editing context for modifying prefab data.
- Inherited prefab: prefab that derives from another prefab and overrides selected data.
- Override: stored difference from inherited source data.
- Replacement: full replacement relationship, usually more dangerous than inheritance or override.
- Metadata/GUID: identity data used by Workbench/resource systems for override/replacement relationships.
- `BaseContainer`: structured data access surface for containers/configs/resources.
- `ResourceName`: generated string-like resource reference type; verify exact use through query output.
- `PrefabResource`: resource-loaded prefab type route; verify exact use through query output.
- Entity Catalog: config-driven list of entity/prefab entries and associated metadata/data.
- Catalog entry data: typed data attached to catalog entries for filtering and behavior.

## Workbench / Resource / Data Surfaces

Primary data surfaces:
- `.et` entity prefab files for entity hierarchy and component values.
- `.ct` component prefab files for reusable component data.
- `.conf` config files for config classes, catalogs, and structured config data.
- Config object prefabs for reusable config-object data.
- Metadata files and GUIDs for identity, override, and replacement behavior.
- Entity Catalog config files for faction/factionless catalog entries and entry data.
- `BaseContainer`/container data for scripted read/update workflows.
- `ResourceName` fields for resource references.

Cross-reference surfaces:
- Resource Manager Config Editor shows class, parent, values, arrays, sliders, inherited config files, config prefabs, and filling-by-config controls. See `resource-manager-file-types-and-editors.md` for editor operation.
- Entity/component lifecycle, event masks, activeness, and runtime component semantics belong to `entities-components-and-lifecycle.md`.
- Script syntax, `modded`, `override`, `super`, and language-level decorator details belong to `enfusion-language-and-script-editor.md` and `script-events-actions-and-patterns.md`.
- Domain-specific prefab fields belong to narrow references such as weapons, vehicles, UI, animation, audio, terrain, scenario, or server runtime.

## Required Workflows

Choose inheritance, override, duplicate, or replace:
1. Identify whether the source data is a prefab, layout, config, script, catalog, or another resource type.
2. Check whether the data can be inherited from, modified, or replaced.
3. Prefer inheritance when the new data should continue tracking upstream defaults.
4. Prefer override when only selected values must differ in the addon.
5. Prefer duplicate only when a separate copy is intentional.
6. Use replacement only when inheritance/override cannot express the change and the GUID/metadata implications are understood.
7. For scripts, switch to script references before relying on `modded`, `override`, or `super`.

Create or modify an entity prefab:
1. Build or locate a valid entity hierarchy.
2. Ensure there is only one intended prefab root when creating a new entity prefab.
3. Save the entity instance as a new prefab.
4. Use prefab edit mode for prefab-level changes.
5. Use instance overrides only for changes meant to stay local to the instance.
6. Check property indicators before assuming a value is inherited or overridden.
7. Validate the prefab in Workbench, then validate the owning domain behavior.

Create or modify a component prefab:
1. Start from an entity with the required component.
2. Save the component data as a component prefab.
3. Instance the component prefab where reuse is needed.
4. Edit component prefab properties only when every consumer should inherit the change.
5. For runtime component behavior, switch to entity/component lifecycle and script references.

Create or modify a config object prefab:
1. Confirm the config object class is visible to Config Editor through the required decorators.
2. Confirm whether the class is root-creatable.
3. Create or inherit the config object prefab.
4. Edit only the intended fields.
5. Check inherited values and local overrides.
6. Validate the consuming system through the owning domain reference.

Create a config class:
1. Define the config object class with required config metadata.
2. Decorate editable fields so they appear in Config Editor.
3. Mark root config classes appropriately when they must be creatable as top-level config objects.
4. Create the config file through the config workflow.
5. Verify class, parent, and values in Config Editor.
6. Query exact attributes, decorators, and generated container APIs before writing script-dependent code.

Read structured data with `BaseContainer`:
1. Obtain the correct container source for the config, entity source, localization, or metadata case.
2. Do not attempt to strongly reference the `BaseContainer` itself as a member field.
3. Prepare a target variable of the exact expected type.
4. Call `Get` with the correct property/path and typed target variable.
5. Treat failed reads as type/path/source problems until proven otherwise.
6. Use `ResourceName` where required instead of a plain string.

Update structured data with `BaseContainer`:
1. Confirm the property already exists in the class.
2. Use the exact property path for nested values.
3. Use the correct value type.
4. Treat `Set` failure as a defined-property/type/path issue.
5. For entity source or prefab/world persistence, use the correct editor API path; in-memory edits alone may not save.
6. Reopen or revalidate the affected resource after saving.

Set up an Entity Catalog:
1. Create or locate the catalog config.
2. Add catalog entries as config entries, not as direct edits to faction lists when the catalog owns the list.
3. Choose entry classes that match the entry purpose.
4. Fill entry info for display/descriptive metadata.
5. Add entry data for typed behavior/filtering.
6. Verify exact catalog APIs through query before writing code that reads catalog entries.
7. Validate the catalog in the domain that consumes it, such as arsenal, faction, game mode, or spawner behavior.

Load or spawn resources from script:
1. Use this reference to identify the data type and expected resource field.
2. Query exact API for `ResourceName`, `Resource.Load`, `PrefabResource`, `EntitySpawnParams`, and spawn helpers.
3. Use example searches for resource loading and prefab spawning.
4. Inspect bounded snippets only after the query returns a specific file and line.
5. Validate in Workbench/runtime because query output proves API shape, not resource existence or gameplay correctness.

## Configuration Fields And Tables

Data Modding Basics fields/tables:
- Moddability table: use it as the first decision table for whether a source can be inherited, modified, or replaced.
- Footnotes matter: some asset types always override and cannot be fully replaced; script replacement has path-based behavior; behavior tree replacement behaves like override.
- Data manipulation basics: use metadata/GUID identity before attempting override or replacement.
- Override and duplicate menu availability: duplicate/override workflows apply to prefabs, layouts, or configs, and may be unavailable if an override already exists.

Prefab fields and indicators:
- Root/member/instance/member distinctions decide where the data is stored.
- Inherited values come from the parent/source prefab.
- Overridden values are stored in the child prefab or instance.
- Property indicators show whether a parameter is overridden in a prefab or in a scene instance.
- Apply-to-prefab style actions move an instance change into prefab data; use them only when the change should affect prefab consumers.

Config object fields:
- `Attribute` is required on member variables that must be visible and editable.
- `Attribute()` is the minimum member decorator route.
- `BaseContainerProps` is required on config object classes that must appear in Config Editor.
- `BaseContainerProps(configRoot: true)` is required for a root config object to be visible in the config creation process.
- Decorated inheritance matters: a class inheriting from a decorated class must also be decorated to be usable.
- Naming convention settings decide GUID/name behavior and display/identity rules.

`BaseContainer` fields and paths:
- Property name/path must match existing defined data.
- Nested values need explicit paths.
- Read target variables must have the correct type.
- `ResourceName` fields should be read/written as `ResourceName` when required.
- `Set` cannot add arbitrary new properties to the container.
- Entity-source edits need the correct persistence path.

Entity Catalog tables:
- Catalog table: defines catalog-level config structure and list ownership.
- Entity entry classes table: shows example entry classes by entry purpose; treat it as examples, not exhaustive truth.
- Entry info table: describes display/identity information attached to an entry.
- Entry data examples table: shows additional data patterns attached to entries.

Prefab Data:
- Entity and component class classes are required for all entities and components before prefab data can be used correctly.
- Use the code example as a shape reference only; verify current class names and signatures through query.

## Procedures And Ordered Steps

To decide whether to inherit, override, duplicate, or replace:
1. Identify the resource type and owner.
2. Check the moddability table category.
3. If inheritance is supported and the source should keep upstream updates, inherit.
4. If only selected values should differ, override.
5. If the asset should become independent, duplicate.
6. If the asset must fully take the original identity, replace and verify metadata/GUID requirements.
7. Re-check source ownership before touching scripts or generated files.

To create an inherited prefab:
1. Locate the source prefab.
2. Use the inherit-prefab workflow or drag/drop method documented by the wiki.
3. Save the inherited prefab in the addon data.
4. Edit only the intended values.
5. Check override indicators.
6. Validate parent/child behavior by reopening both source and child prefab.

To edit prefab instance values:
1. Determine whether the selected object is a prefab instance.
2. Check prefab instance/member indicators.
3. Change values only when local override is intended.
4. Use apply-to-prefab only when the changed value should become stored prefab data.
5. Reopen the prefab or instance to confirm where the change was stored.

To unprefab:
1. Confirm the prefab relationship is intentionally being removed.
2. Unprefab only the intended object/branch.
3. Verify the object no longer receives source prefab changes.
4. Use this sparingly because it breaks reuse and inherited updates.

To create a component prefab:
1. Select an entity with the required component.
2. Use the component prefab creation workflow.
3. Save the `.ct` data in the correct addon/resource area.
4. Instance the component prefab where reuse is needed.
5. Verify consumer entities and domain behavior.

To create a config object prefab:
1. Verify the class has required Config Editor metadata.
2. Confirm root creatability if a standalone config object is needed.
3. Create the config object prefab.
4. Fill fields with correct typed values.
5. Verify inheritance and overrides before use.

To create a config class:
1. Define the class.
2. Add required `BaseContainerProps` class metadata.
3. Add required `Attribute` metadata to editable fields.
4. Make it root when the config must be creatable from the config creation process.
5. Create the config file.
6. Open it in Config Editor and verify class, parent, and values.
7. Query exact current decorator and API names before writing code against it.

To work with `BaseContainer`:
1. Identify the container source type.
2. Use typed reads with the exact expected type.
3. Use typed updates only for defined properties.
4. Use explicit nested paths for non-root values.
5. Use editor API persistence for entity source/world/prefab changes.
6. Validate the saved resource, not only the in-memory result.

To build an Entity Catalog:
1. Create catalog config.
2. Add entries as config entries.
3. Choose entry classes by entry purpose.
4. Fill entry info.
5. Add entry data for filtering/behavior.
6. Use query lookup before calling catalog APIs in script.
7. Validate the consuming system, such as arsenal, faction, spawner, or game mode.

## Warnings And Failure Modes

- Do not confuse Resource Manager editor controls with data model ownership. This reference owns the data model; Resource Manager owns the editor surface.
- Do not make a duplicate when inheritance is needed. Duplicates will not track upstream changes like inherited data.
- Do not use replacement as the default. Replacement is more fragile than inheritance or override and may require metadata/GUID work outside normal editor flow.
- Do not edit Workbench-generated files by hand unless the workflow explicitly requires it; invalid generated data can break resources.
- Do not ignore prefab override indicators. A value can be inherited, overridden in a prefab, or overridden in a scene instance.
- Do not use apply-to-prefab when the change is meant to remain local to one instance.
- Do not unprefab as a shortcut for fixing inheritance confusion; it breaks the prefab relationship.
- Do not assume `BaseContainer.Get` works with the wrong target type. Typed reads must match the stored value.
- Do not assume a string can replace `ResourceName` where a `ResourceName` is required.
- Do not assume `BaseContainer.Set` can add new properties. The target property must already be defined by the class.
- Do not assume in-memory container edits persist to saved world or prefab data. Use the correct editor API path for persistent entity-source changes.
- Do not create config objects without required decorators if they need to be visible/editable in Config Editor.
- Do not edit faction lists directly when the catalog config owns the intended entity list.
- Do not trust wiki example entry class lists as exhaustive or current; verify exact game API and examples through query output.
- Do not copy sample prefab/config data blindly. Samples show layout patterns; current wiki workflows and query-verified APIs remain the authority.

## API Lookup Keys

Use these lookup keys when prefab/config/catalog work touches script/API behavior:
- Resource references and loading: `ResourceName`, `Resource.Load`, `Resource`, `ResourceNamePicker`, `PrefabResource`.
- Prefab spawning and entity creation routes: `EntitySpawnParams`, `SpawnEntityPrefab`, `IEntitySource`, `IEntityComponentSource`.
- Container/config data: `BaseContainer`, `BaseResourceObject`, `BaseContainerProps`, `Attribute`, `NamingConvention`, `ParamEnum`, `ParamEnumArray`.
- Entity catalog routes: `SCR_BaseEntityCatalogData`, `SCR_EntityCatalogLoadoutData`, `SCR_EntityCatalogIdentityItemData`, `SCR_EntityCatalogSupportStationResupplyData`, `SCR_EntityCatalogAmbientPatrolData`, `SCR_CatalogEntitySpawnerComponent`.
- Example families: resource loading, spawn prefab, resource picker config, catalog spawner, arsenal catalog data, editable entity prefab logic.

Do not assume any method signature from these names. Query exact symbol, method, inheritance, example, and snippet data before writing code.

## Game-Data Query Commands

Use exact API lookup for resource/container basics:

```powershell
py -3 scripts\query-reforger-data.py symbol ResourceName --exact
py -3 scripts\query-reforger-data.py method Resource Load --exact
py -3 scripts\query-reforger-data.py files BaseContainer --limit 10
py -3 scripts\query-reforger-data.py files PrefabResource --limit 8
```

Use catalog lookup before editing or reading catalog data from script:

```powershell
py -3 scripts\query-reforger-data.py files EntityCatalog --limit 10
py -3 scripts\query-reforger-data.py files SCR_BaseEntityCatalogData --limit 10
py -3 scripts\query-reforger-data.py files SCR_CatalogEntitySpawnerComponent --limit 10
```

Use example searches for loading and spawning:

```powershell
py -3 scripts\query-reforger-data.py examples resource-loading --subtopic resource-load --limit 8
py -3 scripts\query-reforger-data.py examples resource-loading --subtopic spawn-prefab --limit 8
py -3 scripts\query-reforger-data.py files ResourceNamePicker --limit 8
```

Use snippets only after a query result gives an exact file and line:

```powershell
py -3 scripts\query-reforger-data.py snippet scripts/Game/Components/Spawner/CatalogSpawner/SCR_CatalogEntitySpawnerComponent.c --line 1 --context 30
py -3 scripts\query-reforger-data.py snippet scripts/Game/GameMode/SCR_GameModeLastStand.c --line 1 --context 30
py -3 scripts\query-reforger-data.py snippet scripts/Core/generated/Containers/BaseContainer.c --line 1 --context 30
```

If a query is broad, narrow by exact symbol, owner, topic, subtopic, generated-only, or handwritten-only before opening snippets.

## Examples And Samples

Use examples as layout and pattern evidence:
- `SampleMod_Main`: representative config, entity catalog, mission/config, prefab, material, texture, terrain, and UI resource layout.
- `SampleMod_ModdedWeapon`: entity catalog, arsenal config, ammo config, weapon prefab, magazine prefab, and script-modification layout signal.
- `SampleMod_NewCar` and `SampleMod_ModdedCar`: vehicle prefab inheritance, config, editor placeable entity, and component-prefab layout signals.
- `SampleMod_NewCharacter`: character gear, arsenal config, entity catalog, and wearable prefab layout signal.
- `SampleMod_CinematicTutorial`: character prefab/resource layout signal.
- `SampleMod_ModdedScript`: script/project layout signal where data changes touch modded script behavior.

Use game-source examples through query output:
- Resource loading and prefab spawn examples show `ResourceName`, `Resource.Load`, `EntitySpawnParams`, `PrefabResource`, and spawn helper usage.
- Entity catalog examples show catalog entry data and typed entry use.
- Arsenal and inventory examples show catalog-backed item data, but domain behavior belongs to the gear/inventory reference.
- Editable entity examples show prefab/resource manipulation, but runtime entity/component lifecycle belongs to the lifecycle reference.

Do not copy sample bodies into this reference. Use sample layout for orientation, then verify exact API through query commands.

## Follow-Up Keywords

Prefab, entity prefab, component prefab, config object prefab, prefab root, prefab member, prefab instance, prefab instance member, prefab edit mode, inherited prefab, prefab override, unprefab, duplicate prefab, apply to prefab, Data Modding Basics, moddability table, inherit in, transfer to, duplicate to, override in, navigate to original, navigate to override, replace asset, GUID, metadata, Config Editor, config class, config object, `BaseContainer`, `BaseContainerProps`, `Attribute`, `NamingConvention`, `ResourceName`, `Resource.Load`, `PrefabResource`, `EntitySpawnParams`, `SpawnEntityPrefab`, Entity Catalog, catalog entry, entry info, entry data, factionless catalog.

## Verification

Before finalizing prefab/config/catalog work:
1. Confirm the task belongs to generic prefab/config/data modeling. If it is domain-specific, open the narrow domain reference.
2. Confirm whether the data should inherit, override, duplicate, or replace.
3. Confirm the resource type and ownership before editing.
4. Check prefab override indicators after changing prefab or instance values.
5. Reopen the prefab/config/catalog to verify where values were stored.
6. Check metadata/GUID implications for override or replacement workflows.
7. Query exact API before writing or reviewing code that uses resource loading, prefab spawning, containers, or catalogs.
8. For `BaseContainer`, test typed read/update paths and confirm persistence where saved data is expected.
9. For catalogs, validate the consuming system that reads the catalog.
10. State residual Workbench, runtime, multiplayer, or domain validation that was not possible.

## Official Wiki Links

- Prefabs Basics: https://community.bistudio.com/wiki/Arma_Reforger:Prefabs_Basics
- Prefab Data: https://community.bistudio.com/wiki/Arma_Reforger:Prefab_Data
- Data Modding Basics: https://community.bistudio.com/wiki/Arma_Reforger:Data_Modding_Basics
- Create a Config Class: https://community.bistudio.com/wiki/Arma_Reforger:Create_a_Config_Class
- BaseContainer Usage: https://community.bistudio.com/wiki/Arma_Reforger:BaseContainer_Usage
- Entity Catalog: https://community.bistudio.com/wiki/Arma_Reforger:Entity_Catalog
- Scripting: Config Object: https://community.bistudio.com/wiki/Arma_Reforger:Scripting:_Config_Object
- Resource Manager: Config Editor: https://community.bistudio.com/wiki/Arma_Reforger:Resource_Manager:_Config_Editor

## Usefulness Score

Score: 94/100

- Wiki coverage: 29/30. All owned prefab/config/container/catalog pages are named, represented, and linked. `Resource Manager: Config Editor` and `Scripting: Config Object` are intentionally partial because only their data-model pieces belong here.
- Operational detail: 15/15. The reference preserves prefab operations, data-modifiability decisions, config class setup, BaseContainer typed access, catalog setup, and ordered workflows.
- API lookup usefulness: 14/15. Exact lookup commands cover `ResourceName`, `Resource.Load`, `BaseContainer`, `PrefabResource`, Entity Catalog, resource loading, and prefab spawning. Exact signatures remain delegated to query output.
- Example grounding: 9/10. Official sample families and game-source query routes are included as layout/pattern evidence without copying bodies.
- Codex task usefulness: 14/15. Codex can route normal tasks like inheriting a prefab, overriding data, creating a config class, reading a container, loading/spawning a prefab, or wiring a catalog without guessing. Domain-specific field choices are intentionally cross-linked.
- Context efficiency: 9/10. The file is dense and owner-focused; it avoids Resource Manager/editor duplication and domain prefab duplication.
- Verification guidance: 4/5. Workbench, persistence, query, catalog, and domain validation are covered; some runtime checks remain delegated to future domain references.

Category-fit check:
- Source family complete: pass. Prefab, data moddability, config class, BaseContainer, Entity Catalog, Prefab Data, and config-object semantics are covered.
- No owned page missing: pass. Every owned primary page is listed in Source Inventory.
- Split boundary justified: pass. Resource Manager editor controls, entity lifecycle, and domain-specific prefab recipes are explicitly routed elsewhere.
- Cross-links present: pass. Nearby workflows point to the owning reference.
- Task route clear: pass. Codex can start from data-model intent, use the relevant workflow, then query exact APIs and domain examples.

Missed coverage and exclusions:
- Resource Manager Config Editor is partial by design; editor controls are owned by `resource-manager-file-types-and-editors.md`.
- General entity/component runtime semantics are excluded and routed to `entities-components-and-lifecycle.md`.
- Weapon, vehicle, UI, animation, audio, terrain, server, and scenario-specific prefab/config recipes are excluded to avoid duplicate ownership.
