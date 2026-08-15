# Official Wiki routes

Choose the narrowest route that covers the task. Search with the system noun plus operation or failure, inspect more than the top result, and read the matching section. These titles are query seeds; the retrieved Wiki revision is the evidence.

| Domain | Primary query seeds | Expand when needed |
| --- | --- | --- |
| Enforce language | `Enforce Script Syntax`, `Scripting Values`, `Scripting Keywords`, `Scripting Operators`, `Scripting Conventions` | Preprocessor, macros, config objects, JSON, serialization |
| OOP and modding | `Object Oriented Programming Basics`, `Object Oriented Programming Advanced Usage`, `Automatic Reference Counting` | Casting, templates, modded classes, load order, visibility, override |
| Quality and performance | `Scripting Best Practices`, `Scripting Do's and Don'ts`, `Scripting Performance`, `Script Profiling` | Diag Menu, Autotest Framework, FPS diagnostics |
| Entity/component lifecycle | `Entity Lifecycle`, `Entity Activeness`, `Event Handlers`, `Create a Component`, `Create an Entity` | Event masks, initialization, deletion, activation, ScriptInvoker |
| Multiplayer | `Multiplayer Scripting` | Authority, proxy, owner, RPC, RplProp, serialization, streaming, JIP, dedicated server |
| Resources and data | `Resource Usage`, `BaseContainer Usage`, `Prefab Data`, `Data Modding Basics`, `Prefabs Basics` | File types, directory structure, inheritance, container lifetime |
| Workbench and World Editor | `Workbench`, `Resource Manager`, `Script Editor`, `World Editor`, `Workbench Plugin`, `WorldEditorAPI Usage` | Editor-specific plugin and API pages |
| UI | `Layout Creation` | Widgets, dialogs, HUD, menus, localization, input |
| AI | `Behavior Editor`, `Behavior Editor Nodes` | AI debugging, navmesh, perception, waypoints |
| Scenarios and Game Master | `Scenario Framework`, `Task System Usage`, `Game Master` | Game modes, scenario hierarchy, runtime tasks |
| Terrain and worlds | `World Editor`, terrain, world, navmesh | Generators, layers, roads, splines, map data |
| Assets | Import plus the asset type | FBX, textures, materials, models, particles, destruction |
| Animation | Animation plus the system or asset | Animation Graph, IK, procedural animation |
| Audio | Audio plus the system or asset | Signals, sound shaders, projects, runtime playback |
| Weapons and vehicles | Concrete weapon or vehicle system | Components, simulation, turrets, damage, controls |
| Servers and release | Server config, hosting, startup, Workshop, publishing | Packaging, dependencies, versioning, moderation |

## Search discipline

1. Check `official_wiki_status` on first use, after failure, or when corpus availability is uncertain. Require `official_wiki_status.available` to be true.
2. Call `search_official_wiki` with a narrow phrase and compare matching headings and paths before selecting a result from `search_official_wiki.results`.
3. Pass `search_official_wiki.readInput` unchanged to `read_official_wiki`. Follow returned continuation data unchanged until the required section is complete.
4. Preserve `read_official_wiki.content`, `read_official_wiki.sourceUrl`, `read_official_wiki.relativePath`, exact lines, and revision when available.
5. Use Wiki examples to understand concepts and intended workflows. Resolve declaration-looking code through Game Data before emitting it.

For a broad system task, start with one route, identify adjacent authored or runtime surfaces from that evidence, then search only those routes. Avoid loading whole pages or catalogues when one section answers the question.
