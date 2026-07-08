# Server Hosting, Startup, And Runtime

## When To Read

Read this reference when a task touches server launch, dedicated hosting, server JSON configuration, startup parameters, RCON, A2S, player-hosted servers, Linux server setup, SteamCMD, Docker, server management commands, session saves, server-side validation, or runtime checks for mods and scenarios.

Use this as the primary owner for:

- building or reviewing a server configuration file;
- deciding which startup parameter to use for server launch;
- listing or selecting scenario IDs for server config;
- configuring A2S, RCON, max FPS, mods, crossplay, persistence, join queues, and operating flags;
- running or validating dedicated-server behavior separately from local hosted/editor behavior;
- routing server-related API and example lookup.

Do not use this reference as the owner for replication semantics, project publishing, scenario authoring, or diagnostics UI details. Those belong to the multiplayer, addon/workshop, scenario/game-mode, and diagnostics references.

## Source Inventory

Wiki ownership:

- Primary wiki topics/categories: Server Config, Startup Parameters, Server Hosting, Server Management, Server Area Code.
- Secondary/cross-reference topics: multiplayer replication verification, addon packaging, Game Master/scenario content, diagnostics/profiling, Workbench packing/publishing startup parameters.

Wiki pages reviewed:

- Server Config - https://community.bistudio.com/wiki/Arma_Reforger:Server_Config - status: covered - reason: primary owner for server JSON fields, ports, A2S, RCON, game section, mods, game properties, persistence, operating settings, template, and example shape.
- Startup Parameters - https://community.bistudio.com/wiki/Arma_Reforger:Startup_Parameters - status: covered - reason: primary owner for executable launch parameters, with Workbench-only parameters included only where they affect server/runtime workflows.
- Server Hosting - https://community.bistudio.com/wiki/Arma_Reforger:Server_Hosting - status: covered - reason: primary owner for dedicated server, player-hosted server, BattlEye, config launch, Linux, SteamCMD, LinuxGSM, and Docker setup routes.
- Server Management - https://community.bistudio.com/wiki/Arma_Reforger:Server_Management - status: covered - reason: primary owner for admin roles, permissions, commands, and custom RCON command caveats.
- Server Area Code - https://community.bistudio.com/wiki/Arma_Reforger:Server_Area_Code - status: covered - reason: short source for official server area-code meanings.

Wiki sections covered:

- Server Config: Summary; Root; `bindAddress`; `bindPort`; `publicAddress`; `publicPort`; `a2s`; `rcon`; `game`; `operating`; `supportedPlatforms`; `mods`; `gameProperties`; `persistence`; `databases`; `storages`; `disableNavmeshStreaming`; `joinQueue`; Template; Example.
- Startup Parameters: General mod/profile/world parameters; Window `forceUpdate`; Workbench parameters where relevant to server validation or packaging routes; Hosting parameters; Network Tuning; Debug server-affecting parameters; Profiling `checkInstance`.
- Server Hosting: Dedicated Server; BattlEye; startup parameters; config file usage; player-hosted server; Linux server; SteamCMD; bash scripts; LinuxGSM; Docker setup.
- Server Management: Administrator Roles; Permissions; login/logout; roles; restart; shutdown; kick; ban; id; players; custom RCON commands.
- Server Area Code: area code table for official server names.

Structured wiki records:

- Tables reviewed/included: Server Config default ports, RCON permissions, supported platforms, mission header; Startup Parameters Workbench module and minidump tables where relevant; Server Management permissions; Server Area Code table.
- Procedures reviewed/included: public address setup, fast validation notes, persistence database/storage routing, navmesh streaming, BattlEye setup, SteamCMD setup, bash script setup, LinuxGSM, Docker setup.
- Admonitions reviewed/included: bind/public address cautions, port cautions, one-scenario limitation, RCON password rules, RCON disconnect note, supported-platform warnings, BattlEye config warning, max FPS resource warning, Docker certificate/platform cautions, ban command dedicated-server requirement.
- Code blocks reviewed/included: server config template/example shape, scenario ID examples, persistence examples, startup parameter examples, server management command examples.
- Media reviewed: server hosting mod-list and setup screenshots were treated as UI evidence, not copied.

Game-data/API evidence:

- Queries run:
  - `py -3 scripts\query-reforger-data.py files server --limit 8`
  - `py -3 scripts\query-reforger-data.py examples game-mode --limit 8`
  - `py -3 scripts\query-reforger-data.py files ServerInfo --limit 8`
  - `py -3 scripts\query-reforger-data.py files RCON --limit 8`
  - `py -3 scripts\query-reforger-data.py files GameMode --limit 8`
- Symbols/methods/attributes verified: server browser files, `ServerInfo`, server hosting UI, game-mode examples, server chat/RPC-adjacent source routes.
- Examples/snippets reviewed: query output for server browser/hosting UI, `ServerInfo`, game-mode examples, and world-system/game-mode source routes.

Samples and source examples:

- Official sample folders reviewed as available layout signals: `SampleMod_Main`, `SampleMod_NewFaction`, `SampleMod_WorkbenchPlugin`, and other sample roots where scenario or mod layout can affect server startup.
- Game-source example families reviewed: server browser, server hosting UI, `ServerInfo`, game mode, world systems, and related game-mode component examples.

Coverage gaps:

- Replication authority/proxy/owner behavior is intentionally excluded and owned by `multiplayer-replication-and-authority.md`.
- Addon publishing and Workshop packaging are intentionally excluded and owned by `mod-projects-addons-workshop.md`.
- Scenario Framework, Game Master, factions, and mode authoring are intentionally excluded and owned by future scenario/game-master references.
- Diagnostics UI/profiling workflows are intentionally excluded and owned by `diagnostics-testing-and-performance.md`; this reference only notes launch and server logging parameters needed for runtime validation.

## Wiki Source Coverage

Server Config is the source of truth for server JSON shape.

Core server ports:

- Default public game traffic uses UDP port `2001`.
- A2S server query uses UDP port `17777` when enabled/configured.
- RCON uses UDP port `19999` by default when configured.
- Port forwarding must match the public address/port clients use to reach the server, not just the local bind address.

Root server fields:

- `bindAddress` controls which local network interface the server socket binds to. It is normally omitted or left empty so the server can bind to all IPv4 interfaces.
- `bindPort` controls the local UDP port for the server socket. It is normally omitted so it follows `publicPort`, unless specific forwarding needs require otherwise.
- `publicAddress` is the address registered with the backend for clients to connect to. If omitted or empty, automatic public address detection is used.
- `publicPort` is the UDP port registered with the backend. If the machine has the public IP directly, it should match `bindPort`; behind forwarding it should match the forwarded external port.
- IPv6 is not supported for this server binding workflow.

A2S:

- A2S is the Steam server query protocol route.
- The A2S address is required inside the A2S section and can restrict queries to a network interface.
- The A2S port is a UDP port, defaulting to `17777`, used for Steam query requests.

RCON:

- RCON is UDP-based remote console access.
- RCON address restricts which interface the RCON socket binds to.
- RCON port defaults to `19999`.
- RCON password is required for RCON to start, cannot contain spaces, and must be at least three characters long.
- RCON client permission can be `admin` or `monitor`; admin can perform state-changing commands, monitor is limited to non-mutating server-state commands.
- RCON does not immediately drop disconnected clients; the server keeps the connection until timeout.

Game section:

- `name` identifies the server in server browser contexts.
- `password` protects player access.
- `passwordAdmin` supports in-game admin login.
- `admins` can designate server admins.
- `scenarioId` points to a scenario `.conf` resource path.
- Use the `listScenarios` startup parameter to obtain valid scenario paths.
- Only one scenario can be defined where the wiki documents no mission rotation.
- `maxPlayers`, `visible`, `crossPlatform`, and `supportedPlatforms` affect who can join and see the server.
- Prefer the crossplay field when it expresses the desired platform policy; leave lower-level platform arrays undefined unless the exact platform list is required.

Mods:

- The server config can list mods that clients must download and activate on join.
- Mod entries include mod ID, name, version, and required status.
- Workshop/mod manager output can be used to produce a JSON-ready mod list, but verify the final server config and client join behavior.
- Server mod setup is runtime hosting behavior. Publishing the mod itself belongs to the addon/workshop reference.

Game properties:

- View distance and grass distance fields control server-side visual/range limits exposed through server configuration.
- `fastValidation` validates client-loaded map entities/components against initial server state. Public internet servers should keep fast validation enabled; disabling it can provide more mismatch detail but is not the normal public-server setting.
- `networkViewDistance` affects network range behavior and must be validated under real player distance/load.
- BattlEye can be configured from server properties and may also interact with BattlEye config files.
- Third-person and VoN UI/direct speech/cross-faction flags are server policy settings and must be tested in multiplayer.
- `missionHeader` fields affect how mission metadata is exposed.

Persistence:

- Persistence can be configured through `autoSaveInterval`, `saveRetention`, `loadSessionSave`, `keepSessionSave`, `hiveId`, `databases`, and `storages`.
- `databases` are named overrides or additions to system-provided database configs.
- A database `preset` points to a database config resource.
- Database `options` are type-specific key/value settings.
- `storages` are named storage overrides.
- A storage `database` must refer to a database name declared in the database set or the default main database.
- Session-save startup parameters and config properties must agree with the intended persistence behavior.

Operating settings:

- `lobbyPlayerSynchronise` affects lobby/player synchronization behavior.
- `disableCrashReporter` changes crash reporting.
- `disableNavmeshStreaming` can load full navmesh data into memory, improving some server AI responsiveness at the cost of memory footprint.
- `disableServerShutdown`, `disableAI`, `playerSaveTime`, `aiLimit`, `slotReservationTimeout`, and `joinQueue` are server-operating policy and performance controls.
- `joinQueue.maxSize` limits queued joins.

Startup Parameters is the source of truth for executable launch flags.

General launch parameters:

- `-addons` loads mod IDs on game start. IDs can come from `.gproj` GUIDs/project IDs or subdirectory names, with GUIDs preferred.
- `-addonsDir` adds directories searched for mods. Use explicit stable paths in real server scripts.
- `-profile` selects the profile directory.
- `-world` loads a world on startup for game executables, but Workbench uses its own load parameter.
- `-cfg` chooses a user engine settings config.
- `-forceUpdate` keeps the application updating while out of focus, which matters for editor/runtime validation flows.
- `-scrDefine` defines script preprocessor symbols and works with client, server, and Workbench executables.

Workbench-related parameters with server relevance:

- `-gproj` selects an addon project and avoids the Workbench project picker.
- `-packAddon` and `-publishAddon` are packaging/publishing routes; this reference only notes them because server validation often happens after packing. Full ownership remains with the addon/workshop reference.
- `-wbModule` selects Workbench module behavior for automated workflows.
- `-diagMenu`, script validation, world editor force-save, navmesh generation, and resource-manager build parameters are validation helpers when preparing server-ready content; their full workflows belong to diagnostics, Workbench, terrain, or resource references.

Hosting parameters:

- `-config` points a server executable at a JSON server config.
- `-maxFPS` caps server FPS and is strongly recommended for dedicated servers so the server does not consume all available resources.
- `-server` launches a local server and loads a selected world; when `-server` is used, `-config` is ignored.
- `-listScenarios` prints scenario `.conf` paths to logs.
- `-loadSessionSave` loads the latest or a specified previous session save.
- `-keepSessionSave` preserves completed playthrough save data on the end screen.
- `-logStats` writes server performance statistics, optionally at a millisecond interval.
- `-logVoting` adds voting-system logging.
- `-playerLimits` limits player counts by faction key.

Network tuning and debug parameters:

- Network tuning parameters apply to server executables and should be changed only when the server behavior being tuned is understood and measured.
- `-disableAI` disables AI world initialization and ticking.
- `-disableNavmeshStreaming` disables navmesh streaming, optionally scoped by navmesh project list in newer behavior.
- `-checkInstance` enables script VM allocation logging and belongs mainly to profiling validation.

Server Hosting is the source of truth for running server builds.

- A dedicated server runs without a local game instance and processes game information plus network synchronization.
- Stable and experimental server app IDs are documented by the wiki; verify the intended branch before updating a host.
- BattlEye config can customize RCON port/password, but existing BattlEye config content must not be erased.
- Missing BattlEye game/master port settings can cause kick messages.
- `-config` targets the server JSON file.
- `-maxFPS` should generally be set to a practical cap such as the documented 60-120 range.
- `-server` starts a local server from a world and ignores `-config`.
- Player-hosted servers are listen servers started from the game UI and are PC-only.
- Linux setup can use SteamCMD, helper scripts, LinuxGSM, or Docker.
- Docker setup must account for the container IP and host/network registration behavior; otherwise clients can fail to connect.

Server Management is the source of truth for in-game and RCON-admin command behavior.

- A server administrator can be the player hosting the server, a logged-in admin using `passwordAdmin`, or a voted-in admin.
- Permission tables distinguish logged admin, voted admin, player, RCON admin, and RCON monitor rights.
- Commands include `login`, `logout`, `roles`, `restart`, `shutdown`, `kick`, `ban`, `id`, and `players`.
- `restart` restarts the running scenario while keeping clients connected.
- `shutdown` stops the server and disconnects clients.
- `kick` ejects a player by player ID but does not prevent rejoin.
- `ban` uses subcommands such as create/remove/list and requires player IDs; dedicated-server caveats apply.
- Custom BI RCON commands are not standard RCON commands and use a distinct command prefix.

Server Area Code is the source of truth for official server area codes.

- Official servers use short region/city codes.
- Covered examples include Europe/Frankfurt and United States/Los Angeles, Miami, New York, San Francisco, Washington DC, plus Asia-Pacific Singapore, Tokyo, and Sydney.

## Terms And Concepts

- Dedicated server: server executable without a local player/game instance.
- Listen server: player-hosted server with a local player.
- Server config: JSON-like server configuration data consumed by server startup.
- Startup parameter: command-line flag passed to a game, server, or Workbench executable.
- A2S: Steam server query protocol endpoint.
- RCON: remote console protocol for issuing server commands.
- Public address: address advertised to clients/backends.
- Bind address: local network interface address used by the server socket.
- Public port: externally reachable port clients use.
- Bind port: local port the server socket uses.
- Scenario ID: scenario `.conf` resource path used by server config.
- Crossplay: platform acceptance policy for PC/Xbox/PlayStation where supported.
- Persistence: save/load system for session state.
- Database preset: persistence database config resource.
- Storage: named persistence storage route.
- Join queue: queue for players waiting to join.
- BattlEye: anti-cheat/server protection integration.
- Max FPS: server frame cap; important for resource control.
- Server area code: official server region/city code.

## Workbench / Resource / Data Surfaces

Server runtime surfaces:

- server JSON config file;
- server executable startup parameters;
- profile directory;
- mod/addon directories and IDs;
- scenario `.conf` resource path;
- persistence database config resources;
- log files used by `listScenarios`, voting logs, and stats logs;
- BattlEye server config;
- RCON client/command surface;
- server browser/A2S query surface;
- dedicated server host environment.

Cross-reference surfaces:

- Addon packing and publishing are controlled by Workbench parameters but are owned by `mod-projects-addons-workshop.md`.
- Replication correctness is verified on dedicated server but authored from `multiplayer-replication-and-authority.md`.
- Game mode, scenario, faction, and task content is launched by server config but authored from scenario/game-master references.
- Profiling, diagnostic menus, and deep performance tools are owned by `diagnostics-testing-and-performance.md`.

## Required Workflows

Dedicated server config workflow:

1. Decide whether the server is public, private, crossplay, modded, persistent, and visible.
2. Choose the public game port, A2S port, and RCON port.
3. Leave bind/public address fields empty unless the host has specific network-interface or forwarding requirements.
4. Use `listScenarios` to confirm the scenario `.conf` path before setting `scenarioId`.
5. Add server name, access passwords, admin password/admin list, max player count, visibility, and platform policy.
6. Add required mods with correct IDs, names, versions, and required flags.
7. Configure game properties such as validation, view distances, BattlEye, VoN UI/policy flags, and persistence.
8. Configure operating controls such as AI limits, navmesh streaming, join queue, and shutdown behavior.
9. Launch with `-config`.
10. Verify join, mod download, scenario load, RCON/A2S, persistence, and dedicated-server logs.

Scenario path workflow:

1. Run the server executable with `-listScenarios` when scenario IDs are uncertain.
2. Read the scenario `.conf` resource path from logs.
3. Put that path into `scenarioId`.
4. Keep only one active scenario in server config where mission rotation is not supported.
5. Verify the selected scenario loads on the target server branch.

Modded server workflow:

1. Confirm the mod IDs from project metadata or Workshop/mod manager.
2. Use `-addons` and `-addonsDir` for local pre-upload testing only when appropriate.
3. Use server config `mods` for client-required download/activation on join.
4. Validate client join from a clean client profile when testing required mods.
5. Verify server logs for mod load failures, version mismatches, and missing dependencies.

Persistence workflow:

1. Decide whether session saves should load automatically.
2. Configure `autoSaveInterval`, `saveRetention`, `loadSessionSave`, and `keepSessionSave`.
3. Configure database overrides only when default persistence behavior is insufficient.
4. Ensure storage names refer to valid configured database names.
5. Test save, shutdown, restart, and rejoin.

RCON/admin workflow:

1. Configure RCON address, port, password, max clients, and permission.
2. Ensure the password has no spaces and is at least three characters.
3. Choose `admin` only for clients that need state-changing commands.
4. Use `players` and `id` to identify targets.
5. Use `kick`, `ban create`, `ban remove`, and `ban list` with command-specific validation.
6. Test custom RCON commands separately from standard RCON behavior.

Linux hosting workflow:

1. Install or update the dedicated server through the chosen route: SteamCMD, helper scripts, LinuxGSM, or Docker.
2. Confirm branch/app selection before deployment.
3. Configure server JSON and startup parameters.
4. Expose/forward game, A2S, and RCON ports as intended.
5. If using Docker, ensure the registered public address/port does not resolve to an unreachable container-only address.
6. Run a real client connection test.

## Configuration Fields And Tables

Default server ports:

- `2001` UDP: public game traffic, required for ordinary hosting.
- `17777` UDP: A2S query port, optional depending on server query needs.
- `19999` UDP: RCON port, optional depending on remote console needs.

Root fields:

- `bindAddress`: local interface binding; usually empty/default.
- `bindPort`: local UDP socket port; usually follows `publicPort`.
- `publicAddress`: externally reachable address registered with backend.
- `publicPort`: externally reachable UDP game port.
- `a2s`: Steam query settings.
- `rcon`: remote console settings.
- `game`: server gameplay/session settings.
- `operating`: server operating behavior.

A2S fields:

- `address`: required bind address for A2S socket.
- `port`: UDP port for A2S, default `17777`.

RCON fields:

- `address`: required bind address for RCON socket.
- `port`: UDP RCON port, default `19999`.
- `password`: required to start RCON, no spaces, minimum three characters.
- `maxClients`: maximum simultaneous RCON clients, default/range documented by wiki.
- `permission`: `admin` or `monitor`.
- `blacklist` / `whitelist`: access control lists where configured.

Game fields:

- `name`
- `password`
- `passwordAdmin`
- `admins`
- `scenarioId`
- `maxPlayers`
- `visible`
- `crossPlatform`
- `supportedPlatforms`
- `modsRequiredByDefault`
- `mods`

Mod entry fields:

- `modID`
- `name`
- `version`
- `required`

Game property fields:

- `serverMaxViewDistance`
- `serverMinGrassDistance`
- `fastValidation`
- `networkViewDistance`
- `battlEye`
- `disableThirdPerson`
- `VONDisableUI`
- `VONDisableDirectSpeechUI`
- `VONCanTransmitCrossFaction`
- `missionHeader`
- `persistence`

Persistence fields:

- `autoSaveInterval`
- `saveRetention`
- `loadSessionSave`
- `keepSessionSave`
- `hiveId`
- `databases`
- `storages`
- database `preset`
- database `options`
- storage `database`

Operating fields:

- `lobbyPlayerSynchronise`
- `disableCrashReporter`
- `disableNavmeshStreaming`
- `disableServerShutdown`
- `disableAI`
- `playerSaveTime`
- `aiLimit`
- `slotReservationTimeout`
- `joinQueue`
- `maxSize`

Startup parameters to route server work:

- `-config`
- `-maxFPS`
- `-server`
- `-listScenarios`
- `-loadSessionSave`
- `-keepSessionSave`
- `-logStats`
- `-logVoting`
- `-playerLimits`
- `-addons`
- `-addonsDir`
- `-profile`
- `-world`
- `-forceUpdate`
- `-scrDefine`
- `-disableAI`
- `-disableNavmeshStreaming`
- `-checkInstance`

Server management command surface:

- `login`
- `logout`
- `roles`
- `restart`
- `shutdown`
- `kick`
- `ban create`
- `ban remove`
- `ban list`
- `id`
- `players`
- custom BI RCON commands prefixed separately from standard commands.

## Procedures And Ordered Steps

Before changing a server config:

1. Identify whether the task changes connection, scenario, mod, persistence, operating, or admin behavior.
2. Read the corresponding field group in this reference.
3. Verify any exact game/source terms with query commands if scripts or APIs are involved.
4. Preserve existing unrelated config fields.
5. Make the smallest config change that satisfies the request.
6. Validate with a server launch and client join test.

Before launching a dedicated server:

1. Choose the server branch/app.
2. Place or generate the server config file.
3. Confirm the scenario path with `-listScenarios` if uncertain.
4. Set `-config`.
5. Set `-maxFPS`.
6. Open or forward game, A2S, and RCON ports as needed.
7. Launch the server.
8. Check logs for scenario, mod, persistence, BattlEye, and network errors.
9. Join from a client.

Before using `-server`:

1. Confirm the workflow is local world hosting rather than server JSON hosting.
2. Pass the world path directly.
3. Add `-addons` and `-addonsDir` only when local mod testing requires it.
4. Do not expect `-config` to apply at the same time.

Before enabling RCON:

1. Configure RCON address and port.
2. Set a password that satisfies the wiki constraints.
3. Choose `admin` or `monitor`.
4. Open/forward the RCON UDP port only as intended.
5. Test login and a harmless command before using state-changing commands.

Before enabling persistence:

1. Decide whether to load previous session saves.
2. Set save interval and retention.
3. Configure database/storage overrides only if the default system is insufficient.
4. Verify save generation.
5. Restart the server and verify load behavior.

Before using Docker:

1. Confirm the host OS/certificate path assumptions for the Docker setup.
2. Assign adequate CPU and memory resources.
3. Configure ports and public address behavior so clients do not receive an unreachable container address.
4. Launch with the intended config.
5. Test server browser visibility and direct join.

## Warnings And Failure Modes

- Do not set `bindAddress`, `bindPort`, or `publicAddress` casually. The defaults are often safer unless the host has a clear network-interface or forwarding requirement.
- Public address and public port must describe how clients reach the server, not just how the executable binds locally.
- IPv6 is not supported by the documented binding workflow.
- A2S and RCON are separate UDP endpoints from the public game port.
- RCON will not start without a valid password.
- RCON passwords cannot contain spaces and must be at least three characters long.
- RCON monitor permission cannot perform state-changing commands.
- Only one scenario can be defined where the wiki states no mission rotation.
- `-server` ignores `-config`; do not combine them expecting config-driven launch behavior.
- Dedicated servers should use an FPS cap; otherwise the server can consume excessive resources.
- `fastValidation` should remain enabled for public internet servers unless debugging a specific mismatch.
- Disabling navmesh streaming can increase memory usage significantly.
- Docker/container networking can register an address that clients cannot reach unless configured deliberately.
- BattlEye config changes must append or preserve required existing settings.
- Missing BattlEye game/master port settings can trigger kick behavior.
- Ban commands have dedicated-server caveats and require correct player ID handling.
- Player-hosted servers are PC-only.
- Server config that loads mods must be tested with a clean client join path.
- Dedicated-server behavior must be validated separately from local hosted or editor runs.

## API Lookup Keys

Server/browser/runtime:

- `ServerInfo`
- `ServerBrowser`
- `ServerHostingUI`
- `ServerCatalogueApi`
- `ServerWorkshopData`
- `RoomJoinData`
- `BackendCallback`
- `GameMode`
- `BaseGameMode`
- `SCR_BaseGameMode`

Config/runtime search terms:

- server
- RCON
- A2S
- server config
- scenarioId
- maxFPS
- listScenarios
- persistence
- loadSessionSave
- keepSessionSave
- BattlEye
- joinQueue
- ServerInfo
- ServerBrowser
- GameMode

## Game-Data Query Commands

Use these for source-backed routing and exact symbol checks when server work touches scripts or game-source examples:

```powershell
py -3 scripts\query-reforger-data.py files server --limit 8
py -3 scripts\query-reforger-data.py examples game-mode --limit 8
py -3 scripts\query-reforger-data.py files ServerInfo --limit 8
py -3 scripts\query-reforger-data.py files RCON --limit 8
py -3 scripts\query-reforger-data.py files GameMode --limit 8
```

Use snippets only after choosing a specific query result:

```powershell
py -3 scripts\query-reforger-data.py snippet scripts/Game/generated/ServerInfo.c --line 1 --context 20
py -3 scripts\query-reforger-data.py snippet scripts/Game/UI/Menu/ServerBrowser/ServerHosting/ServerHostingUI.c --line 1 --context 30
py -3 scripts\query-reforger-data.py snippet scripts/GameLib/WorldSystemsDocs.c --line 1 --context 30
```

Use JSON when another tool or audit pass needs structured results:

```powershell
py -3 scripts\query-reforger-data.py files ServerInfo --limit 8 --json
```

Do not use game-data query output as a replacement for the server wiki field rules. The query script verifies game-source symbols and example routes; the wiki remains source truth for server config fields and startup parameters.

## Examples And Samples

Best query-routed game-source example routes:

- `ServerInfo` generated files: exact server-info symbols and online/server data shape.
- Server browser UI files: server list, filtering, join callback, and hosting UI behavior.
- Game-mode examples: useful when server config or startup tasks need to route to scenario/game-mode source, but not source truth for server JSON fields.
- World systems docs: useful for game-mode/world-system example routing.

Official sample status:

- Official samples are layout signals only for this reference.
- `SampleMod_Main` can help confirm general mod layout used by server startup tests.
- `SampleMod_NewFaction` can help when server config launches faction/game-mode related content, but faction authoring is owned elsewhere.
- `SampleMod_WorkbenchPlugin` is not a server runtime source; use it only when server validation is part of a Workbench automation task.

No sample is treated as primary source for server config or startup parameter field meanings. The wiki owns those meanings.

## Follow-Up Keywords

- dedicated server
- listen server
- player-hosted server
- server JSON
- server config
- startup parameters
- `-config`
- `-server`
- `-maxFPS`
- `-listScenarios`
- scenario ID
- public address
- bind address
- port forwarding
- A2S
- RCON
- BattlEye
- crossplay
- supported platforms
- required mods
- persistence
- session save
- join queue
- navmesh streaming
- Linux server
- SteamCMD
- LinuxGSM
- Docker
- admin roles
- ban command
- custom RCON commands
- server area code

## Verification

Minimum server config verification:

- Launch the server with the intended startup parameters.
- Confirm the config file is loaded.
- Confirm the scenario loads.
- Confirm only the intended scenario is configured.
- Confirm ports are reachable from a client network path.
- Confirm server browser visibility when `visible` and public hosting require it.
- Confirm A2S query behavior if enabled.
- Confirm RCON login and permission behavior if enabled.
- Confirm client join with required mods.
- Confirm platform/crossplay behavior with intended clients.
- Confirm BattlEye behavior when enabled.
- Confirm VoN UI/direct/cross-faction policy behavior when those flags matter.

Minimum persistence verification:

- Create state that should persist.
- Trigger save behavior.
- Restart the server.
- Load previous session data.
- Confirm save retention and keep/load options behave as configured.

Minimum dedicated-server verification:

- Test on the dedicated server executable, not only player-hosted or editor runs.
- Join with at least one external client.
- Review logs for mod, scenario, network, persistence, and script errors.
- Check server FPS/resource use after setting `-maxFPS`.
- Test AI/navmesh settings on the target terrain if `disableAI`, `aiLimit`, or `disableNavmeshStreaming` changes.

Residual verification note:

- Wiki and query output can identify correct fields, launch flags, and source routes. They do not prove the host network, firewall, branch, mod versions, save database, or dedicated-server runtime are correct. Those must be validated on the actual target server.

## Official Wiki Links

- Server Config: https://community.bistudio.com/wiki/Arma_Reforger:Server_Config
- Startup Parameters: https://community.bistudio.com/wiki/Arma_Reforger:Startup_Parameters
- Server Hosting: https://community.bistudio.com/wiki/Arma_Reforger:Server_Hosting
- Server Management: https://community.bistudio.com/wiki/Arma_Reforger:Server_Management
- Server Area Code: https://community.bistudio.com/wiki/Arma_Reforger:Server_Area_Code

## Usefulness Score

Score: 95/100

Scoring breakdown:

- Wiki coverage: 30/30. All owned primary pages are represented: Server Config, Startup Parameters, Server Hosting, Server Management, and Server Area Code. Field groups, tables, procedures, warnings, code-example shapes, and official URLs are preserved structurally.
- Operational detail: 15/15. The reference includes concrete server JSON fields, startup flags, launch workflows, RCON/admin commands, persistence setup, Linux/Docker routes, and verification order.
- API lookup usefulness: 14/15. Server runtime is mostly config/wiki-driven, but game-data query commands cover server files, `ServerInfo`, RCON search, game-mode examples, and snippets where source lookup is useful.
- Example grounding: 8/10. Official samples are only layout signals; game-source examples route through server/browser/game-mode searches. This is correct for the topic, but less example-heavy than scripting references.
- Codex task usefulness: 15/15. Codex can configure a server, choose launch flags, route scenario IDs, validate RCON/A2S/mods/persistence, and know when to query game data without guessing.
- Context efficiency: 8/10. Server Config and Startup Parameters are large field surfaces, so the reference is dense. It avoids full dumps and keeps exact source lookup in query commands.
- Verification guidance: 5/5. Dedicated-server, player join, ports, mods, persistence, BattlEye, A2S/RCON, platform, and runtime resource checks are explicit.

Missed coverage and cap review:

- No owned primary wiki page is omitted.
- Startup Parameters contains many Workbench-only parameters. This reference includes server/runtime-relevant ones and routes full Workbench/tool workflows to their owners, so no missed-coverage cap applies.
- Server Config field groups are represented without copying the full template or example body, so no dump or context-efficiency failure applies.
- Replication, packaging, diagnostics, and scenario authoring are excluded by design and cross-linked to their owning references.
- No automatic failure applies: server JSON fields, startup parameters, dedicated-server validation, official links, query commands, examples/no-example rationale, and split boundaries are all present.
