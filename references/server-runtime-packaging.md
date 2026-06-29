# Server Runtime Packaging

## When to read this reference

Read for dedicated server JSON, startup parameters, ports, RCON/A2S, scenario startup, mods/addons, validation, Workshop packaging, `.gproj`, logs, secrets, performance limits, and deployment verification.

## Search terms

`server config`, `fastValidation`, `maxFPS`, `bindAddress`, `bindPort`, `publicAddress`, `publicPort`, `a2s`, `rcon`, `scenarioId`, `passwordAdmin`, `mods`, `listScenarios`, `Workshop`, `.gproj`, `-nds`, `-streamingBudget`, `-logLevel`, `-createDB`

## Source authority summary

Server Config docs define JSON fields, ports, public hosting warnings, and case-sensitivity. Startup Parameters docs define runtime flags, debug flags, network tuning, logging, and profiling flags. Samples show addon project metadata and package layout. API data is only secondary for runtime code assumptions.

## Dedicated server JSON fundamentals

Arma Reforger server configuration uses JSON.

Important source warnings:

- Keep `fastValidation` true for public dedicated hosting.
- Limit max FPS with startup parameter `-maxFPS` to save performance.
- JSON parameter names are case-sensitive.
- Values are strings unless the docs say otherwise.
- Only one scenario can be defined; Arma Reforger does not support mission rotation in the documented server config.

Default hosting ports:

| Port | Protocol | Purpose |
| --- | --- | --- |
| 2001 | UDP | public game port |
| 17777 | UDP | A2S/Steam query port |
| 19999 | UDP | RCON port |

## Root network fields

- `bindAddress`: socket bind IP. Usually leave empty/missing so `0.0.0.0` is used. Set only for specific network interface needs. IPv6 is not supported.
- `bindPort`: UDP socket bind port, default 2001. Usually omit so it matches `publicPort`; set only for specific forwarding setups.
- `publicAddress`: public IP registered in backend. Usually omit/empty for auto-detection. Can use `local` to detect local network card address. IPv6 is not supported.
- `publicPort`: UDP port registered in backend. If the server has public IP, it should match `bindPort`; otherwise it is the forwarded UDP port.

Historical names such as `gameHostBindAddress` and related pre-0.9.8.73 names appear in docs; prefer current names unless supporting old versions.

## A2S and RCON

A2S:

- Steam query protocol.
- `address`: required bind address.
- `port`: number 1..65535, default 17777.

RCON:

- UDP-based remote console protocol.
- `address`: required bind IP.
- `port`: number 1..65535, default 19999.
- `password`: required for RCON to start; no spaces; at least 3 characters.
- `maxClients`: 1..16, default 16.
- RCON lacks client disconnect support; after client exit, server holds connection about 30 seconds before timeout.
- `permission`: `admin` can perform any command; `monitor` can only perform commands that do not change server state.
- `blacklist`: commands excluded from execution.
- `whitelist`: if defined, only listed commands can execute.

Secrets rule: never commit real `password`, `passwordAdmin`, tokens, or RCON credentials in examples or repositories.

## Game section fields

- `name`: server name, documented length 0..100 characters.
- `password`: password required to join.
- `passwordAdmin`: admin password for `#login`; does not support spaces.
- `admins`: identity IDs and/or Steam IDs. Listed admins can be checked by backend API and can login without password in supported versions. Docs note list limited to 20 unique IDs and priority queue only for IdentityId admins, not SteamId admins.
- `scenarioId`: path to scenario `.conf`. Use startup parameter `-listScenarios` to list available scenarios and obtain paths.

Scenario IDs include GUID-like prefixes and mission config paths. Do not guess them; list scenarios or inspect project mission configs.

## Server config skeleton

generated-pattern-from-docs

```json
{
  "bindAddress": "",
  "bindPort": 2001,
  "publicAddress": "",
  "publicPort": 2001,
  "a2s": {
    "address": "0.0.0.0",
    "port": 17777
  },
  "rcon": {
    "address": "0.0.0.0",
    "port": 19999,
    "password": "CHANGE_ME",
    "permission": "admin"
  },
  "game": {
    "name": "Example Server",
    "passwordAdmin": "CHANGE_ME",
    "scenarioId": "{SCENARIO_GUID}Missions/Scenario.conf",
    "playerCountLimit": 32
  }
}
```

Verify every field against current docs/project config before deployment; this skeleton is a shape, not a complete public config.

## Startup parameter highlights

Network tuning:

- `-nds N`: Network Dynamic Simulation diameter. `-nds 0` disables. Higher diameter increases networked view range but lowers server performance.
- `-nwkResolution N`: spatial map cell resolution in 100..1000m range. Smaller resolution reduces pop-in but lowers networked view range.
- `-rpl-timeout-ms N`: client/server timeout in milliseconds.
- `-staggeringBudget N`: stationary spatial map cells processed per tick. Too high can hurt server performance during spawn/teleport; too low increases time until clients stream relevant entities.
- `-streamingBudget N`: global streaming budget distributed between connections. Too high can hurt server performance; too low causes pop-in or slow stream-in.
- `-streamsDelta N`: limits amount of streams opened for a client based on difference between server-open and client-open streams.

Diag-only replication/debug flags:

- `-rpl-timeout-disable`: diag exe only; can cause server performance deterioration and memory crash if a connection stops responding.
- `-rpl-reconnect`: diag exe client only.
- `-rpl-vcons`: diag exe only.
- `-rpl-validation-rdb-disable`, `-rpl-validation-scr-disable`, `-rpl-validation-version-disable`, `-rpl-validation-devbin-disable`: diag-only validation disables; docs warn mismatch can cause undefined behavior.

AI/debug:

- `-AILimit N`: caps AI spawning. `<= 0` disables any possible AI. Applies to hosted and singleplayer scenarios and can break the experience.
- `-aiPartialSim N`: splits simulable AI into batches.
- `-disableAI`: disables AIWorld initialization/ticking.
- `-disableNavmeshStreaming`: disables navmesh streaming; newer versions support comma-separated navmesh project list.

Database/assets:

- `-createDB`: regenerates database after file directory changes/moved resources.
- `-disableShadersBuild`, `-generateShaders`: shader generation control.
- `-addonsVerify`: dedicated server only; verifies installed addons and shuts down/logs corrupt files.
- `-addonsRepair`: dedicated server only; repairs corrupt addons, shuts down if repair fails.

Logging:

- `-logLevel normal|warning|error|fatal`.
- `-logAppend`: do not empty logs on start.
- `-logsDir`: custom logs/profile directory target.
- `-logFS`: logs every file-system read/write; very demanding, debug only.
- `-log-rdb-checksum`, `-log-scr-checksum`: checksum debugging.
- `-keepNumOfLogs N`.
- `-logTime none|time|datetime`.
- `-VMErrorMode silent|log_only|full|fatal`.

Security:

- `-scriptAuthorizeAll`: disables security popups for `RunCmd`, `RunProcess`, `KillProcess`, and FileIO outside profile. Do not rely on this for normal users.

## Addon packaging checklist

For a modded server:

1. Confirm addon `.gproj` exists and has stable ID/name metadata.
2. Confirm all runtime resources are under addon project: configs, prefabs, worlds, scripts, UI, language, assets.
3. Confirm dependencies are declared and load order is compatible.
4. Confirm Workshop IDs/mod list match published addon versions.
5. Confirm server config `mods` section uses correct IDs/names/versions for the hosting workflow.
6. Confirm `scenarioId` points to packaged mission/scenario config.
7. Confirm no editor-only scripts are required at runtime.
8. Launch a local dedicated server or equivalent, watch logs, and test client join.

## Dedicated-server code assumptions

Runtime scripts should not assume:

- Local player exists.
- UI workspace exists.
- Camera/client-only components exist.
- Workbench editor APIs exist.
- Audio/visual-only components are instantiated.

Server-authoritative systems should run without client presentation components. Route UI/audio/visual behavior to clients/proxies.

## Workshop/publishing notes

Workshop packaging is metadata-sensitive:

- Preview image/thumbnail/localization should be present when expected.
- Dependencies must be declared.
- Visibility and backend login state matter.
- Published server addon versions must match client-required versions.
- Rollback plan should identify previous Workshop version/config and server logs.

## API Notes

Use docs and existing server config for JSON. Use `api-extended.md` for backend/admin/workshop APIs only when writing scripts. Use `networking-multiplayer-replication.md` for server/client authority logic.

## Common Traps

- Changing JSON field casing.
- Committing real admin/RCON passwords.
- Leaving `fastValidation` false for public hosting.
- Forgetting `-maxFPS` on public dedicated servers.
- Guessing `scenarioId`.
- Using loopback assumptions from editor testing for real server networking.
- Disabling replication/script/resource validation outside targeted diag debugging.
- Using client/UI/local-player code on dedicated server.

## Review Checklist

- Are ports, bind/public address, A2S, RCON, and secrets handled?
- Is scenario ID verified, not guessed?
- Are addon dependencies and Workshop IDs covered?
- Are startup parameters appropriate for server/diag/client context?
- Are logs and rollback/test-server steps listed?

## Server Config Detail

- Server JSON config controls network identity, game setup, scenario, mods, and administrative services.
- Bind address and public address are different concerns.
- Game port, query/A2S port, and RCON port must not be confused.
- Secrets and admin passwords should not be committed into public mod repos.
- Scenario IDs must be copied from known scenario resources or generated server config sources, not guessed from display names.
- Addon entries must include the correct Workshop identifiers and dependency expectations.
- Validate JSON syntax before trying to debug gameplay script.
- Keep a minimal known-good config for rollback.

## Startup Parameter Detail

- Startup parameters can enable server mode, point to config files, select profiles, and enable diagnostics.
- Client/editor diagnostic parameters are not always appropriate for dedicated servers.
- Script validation flags can be useful while developing but should be deliberate.
- Resource validation flags can expose missing dependencies early.
- Logging paths should be predictable for support and triage.
- Do not rely on Workbench launch assumptions when deploying a dedicated server.
- Keep command lines documented next to the config they use.

## Workshop Packaging Detail

- `.gproj` metadata defines addon identity and dependencies.
- Workshop upload depends on correct project metadata and included resources.
- Published addons must include resources that were available locally during testing.
- Dependency order matters when scripts/classes/resources come from other addons.
- Replacement mods should document what base-game resources they replace.
- Server mod lists must match the published addon IDs and required dependencies.
- Test a clean install or separate profile to catch missing local-only files.

## Dedicated Runtime Detail

- Dedicated servers have no local UI and no local player.
- Client-only code must not be required for server startup.
- Server logs are the primary evidence for load, script, resource, and scenario failures.
- Multiplayer interactions should be tested with separate client connections.
- Replication and authority bugs may not appear in editor preview.
- Server-side script errors can prevent scenario initialization before players join.
- Keep rollback packages or previous Workshop revisions available for live server recovery.

## API Notes

- Server tasks usually touch config/startup data, not gameplay APIs.
- Use `api-extended.md` when server-side script classes or game mode APIs are involved.
- Avoid local-player and UI APIs in dedicated server logic.
- Use replication APIs for state visible to clients.
- Use resource APIs defensively because server addon load order can expose missing dependencies.

## generated-pattern-from-docs: Server Smoke Test

```text
Validate JSON.
Start dedicated server with the target config.
Check addon load logs.
Check scenario load logs.
Join with one client.
Exercise the feature.
Restart and repeat after clearing local assumptions.
```

## Packaging Review Detail

- Check addon project metadata.
- Check addon dependencies.
- Check Workshop ID.
- Check Workshop revision if updating an existing publication.
- Check included resources.
- Check missing local-only files.
- Check replacement scope.
- Check server mod list.
- Check client mod list.
- Check dependency order.
- Check scenario resource availability.
- Check script module load.
- Check generated API or script validation errors.
- Check resource validation errors.
- Check log path and retention.
- Check rollback revision or backup package.
- Check clean install behavior.
- Check separate profile behavior.
- Check dedicated-server startup.
- Check client join.
- Check feature smoke test.
- Check restart behavior.
- Check RCON configuration if enabled.
- Check A2S/query visibility if public.
- Check firewall/NAT assumptions outside Workbench.

## Dedicated Code Review Detail

- Reject local-player assumptions.
- Reject UI-only dependencies in server logic.
- Reject client input handling on server-only paths.
- Keep authority mutation server-side.
- Keep visual/audio feedback client-side.
- Validate resources before spawning.
- Validate scenario IDs before deployment.
- Validate secrets are not committed.
- Validate diagnostic flags are intentional.
- Validate logs include enough context for remote triage.

## Deployment Failure Detail

- Server does not start: inspect executable path, startup parameters, and config path.
- Config rejected: validate JSON and required fields.
- Scenario missing: verify exact scenario ID.
- Addon missing: verify Workshop ID and dependency list.
- Client cannot join: inspect version/mod mismatch and network ports.
- Feature missing on server: inspect script module load and resource paths.
- Resource missing after publish: inspect included files and dependencies.
- RCON unavailable: inspect bind address, port, password, and firewall.
- Query invisible: inspect A2S/query configuration and public networking.
- Works after manual local copy only: inspect packaging and Workshop upload.
- Breaks after update: inspect revision, dependency changes, and rollback path.
