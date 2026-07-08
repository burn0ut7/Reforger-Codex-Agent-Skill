# Multiplayer, Replication, And Authority

## When To Read

Read this reference when a task depends on multiplayer correctness: replicated components, authority checks, client/server communication, replicated properties, RPCs, Join In Progress behavior, streaming relevance, `RplSave`/`RplLoad`, or Voice over Network setup.

Use this as the primary owner for:

- deciding whether code runs on server authority, proxy, owner proxy, or local-only state;
- choosing between replicated properties, RPCs, and explicit save/load state;
- checking whether a broadcast or RPC can reach a streamed-out proxy;
- planning dedicated-server and multi-client verification;
- routing exact `RplProp`, `RplRpc`, `RplComponent`, and `BaseRplComponent` API lookup.

Do not use this reference as the owner for general class syntax, general component lifecycle, server configuration files, or audio authoring details. Those topics belong to the scripting, entity lifecycle, server runtime, and audio references.

## Source Inventory

Primary wiki owner:

- Multiplayer Scripting: server/client model, replication roles, replication states, streaming, RPC, `RplProp`, `RplRpc`, `RplSave`/`RplLoad`, codec requirements, and examples.

Partial wiki owner:

- Audio: Voice over Network: only the network-relevant requirements for VoN components, direct/radio VoN, radio manager presence, radio item components, ACP stream setup, and related class routing. Full audio editor and sound-system behavior stays with the audio reference.

Game-data lookup evidence reviewed:

- exact `RplProp` attribute lookup;
- exact `RplRpc` attribute lookup;
- exact `RplComponent` class lookup;
- exact `BaseRplComponent` class lookup;
- replicated component task lookup;
- replication examples lookup;
- `RplDocs`, `RplSave`, and `RplLoad` file lookups.

Example source families reviewed through query output:

- `scripts/GameLib/replication/RplDocs.c`
- `scripts/Game/Network/RplTestComponent.c`
- deployable inventory item replication examples
- firing range target save/load examples
- wave respawn, campaign, building, and melee replication examples

Coverage exclusions:

- Server startup parameters, hosting files, RCON, A2S, and deployment checks are owned by `server-hosting-startup-and-runtime.md`.
- Generic entity creation, component creation, event masks, and activeness are owned by `entities-components-and-lifecycle.md`.
- Script structure, logging, user actions, and general event patterns are owned by `script-events-actions-and-patterns.md`.
- Full VoN audio graph, sound event authoring, and signal design are owned by `audio-editor-signals-and-sound-systems.md`.

## Wiki Source Coverage

The Multiplayer Scripting source is covered as the source of truth for the network model and replication behavior.

Network model:

- Reforger multiplayer follows a server/client architecture.
- Clients connect to a server.
- Clients do not communicate directly with each other for gameplay state. Client-to-client gameplay effects must be mediated by the server or by replicated state.
- The server is the central machine that can own authoritative state and distribute it to clients.

Replication roles:

- Authority is the source of truth for a replicated entity.
- A proxy is a representation of an authority-owned entity on another machine.
- A proxy receives network updates from the authority. It is not the authority and cannot send authoritative updates about itself.
- Owner is a special proxy concept and must not be treated as a synonym for authority.
- A client-created entity that is not known by the server cannot be used for server-wide broadcast behavior because the server cannot route state for an entity it does not know.

Replication states:

- Loadtime state is tied to initial world data and deterministic insertion. Server and clients must agree on the initial world state after map load.
- Runtime state covers entities created during play and replicated after startup.
- Local runtime state may exist only on a client. Other machines do not receive proxies for that local-only entity.
- Replication state override can be used for special cases, but child entities spawned during initialization must be attached to their parent as part of the spawn process.
- Loadtime entities with active server authority should not be streamed out in ways the replication system does not support.

Join In Progress:

- JIP requires late joiners to receive enough current state to represent the multiplayer world correctly.
- Do not rely on unreplicated local variables, transient client-only setup, or visual-only effects for state that must survive a late join.
- State that matters after joining late should be represented through replicated properties, save/load state, runtime-spawn replication, or an explicit server-to-client update pattern.

Streaming and relevance:

- Streaming limits which entities exist on which machines.
- Relevance determines whether a remote entity matters enough to be present for a player.
- If an entity proxy is not streamed on a machine, a broadcast to that entity cannot reach that machine because the entity does not exist there.
- Broadcast behavior must be designed with relevance and streaming in mind, especially for far-away entities or state that should be globally visible.
- Operation order matters when creating, streaming, and messaging replicated entities. Verify order-sensitive logic in multiplayer, not only in local Workbench play.

RPC:

- RPCs are methods marked for remote execution.
- `RplRpc` controls channel, receiver, condition, and optional custom condition behavior.
- RPC calls still depend on valid network routing and receiver presence.
- Use exact game-data lookup before writing an RPC annotation or `Rpc(...)` call.

Replicated properties:

- `RplProp` marks a property for replication on an entity or component.
- It supports group, on-replicated callback name, script context, replication condition, and custom condition routing.
- Use an `OnRpl` callback pattern only after verifying the exact callback requirements from game-data examples.
- Scripted class values used in replicated properties may require codec support.

Network modding and codec behavior:

- Scripted classes marked for replication need codec methods so the network layer can serialize and deserialize values correctly.
- Codec logic must know the valid value range and encode it with the minimum practical number of bits.
- The same conceptual data must be written and read in the same order.

`RplSave` and `RplLoad`:

- `RplSave` writes state for replication save/load behavior.
- `RplLoad` reads that state.
- Read order and written order must match.
- The number of bits read and written must match.
- Choosing too many bits wastes bandwidth; choosing too few corrupts or truncates values.
- Health-like bounded values should use a bit count that covers the known range, then verify with real gameplay state.

Voice over Network network slice:

- An entity must have `VoNComponent` to send or receive Voice over Network.
- Direct speech and radio VoN are separate flows.
- Radio VoN requires a radio manager entity in the game world.
- Sender and receiver need radio items with radio components for radio VoN routing.
- ACP setup for VoN depends on expected sound event names and a stream node with the expected stream identifier.
- Sound events, signals, and audio variables are network-relevant only where they support VoN routing. Full audio graph design belongs to the audio reference.

## Terms And Concepts

- Server: the central multiplayer machine that clients connect to and that commonly owns authoritative gameplay state.
- Client: a player machine connected to the server.
- Authority: the machine that owns the true replicated state for an entity.
- Proxy: a remote representation of an authority-owned entity.
- Owner: a special proxy role; not the same thing as authority.
- Replication: movement of state from authority to other machines.
- Loadtime state: initial world state that must match deterministically after map load.
- Runtime state: replicated state created during play.
- Local runtime state: client-only state with no remote proxies.
- JIP: Join In Progress, where a late-joining client must receive enough current state to enter an ongoing session correctly.
- Streaming: entity presence filtering across machines.
- Relevance: the rule that decides whether an entity is important enough to be streamed to a machine.
- Broadcast: sending network information to more than one receiver; still constrained by streaming and entity presence.
- RPC: remote procedure call, used to request method execution across machines.
- `RplProp`: attribute for replicated properties.
- `RplRpc`: attribute for RPC methods.
- `RplSave` / `RplLoad`: explicit replicated state serialization hooks.
- Codec: script-side serialization support for replicated scripted values.
- VoN: Voice over Network.

## Workbench / Resource / Data Surfaces

Primary surfaces:

- `RplComponent` or a derived replication component on entities that participate in entity replication.
- `BaseRplComponent` for lower-level replication component behavior.
- `RplProp` attributes on fields that need replicated state.
- `RplRpc` attributes on methods that should execute remotely.
- `RplSave` and `RplLoad` overrides or hooks for custom replicated state persistence.
- Game-source replication examples for exact patterns.
- Dedicated server plus at least one client for runtime verification.

VoN surfaces:

- `VoNComponent` on entities that send or receive voice.
- Radio manager entity present in the game world for radio VoN.
- Radio item setup with radio components for sender and receiver.
- ACP/sound-event stream setup for VoN audio routing.

Boundary surfaces:

- Component creation and event masks are covered in `entities-components-and-lifecycle.md`.
- Server JSON/config/startup fields are covered in `server-hosting-startup-and-runtime.md`.
- Audio graph authoring is covered in `audio-editor-signals-and-sound-systems.md`.

## Required Workflows

Authority-first workflow:

1. Decide which machine must own the true state.
2. Keep state mutations on authority unless the API and game-source examples prove a client request path is valid.
3. Use proxies for display and response to replicated state, not for authoritative mutation.
4. Treat owner-specific behavior separately from authority behavior.
5. Verify on a dedicated server because local play can hide authority mistakes.

Replicated property workflow:

1. Identify the state that must be visible on other machines.
2. Verify the exact field type and `RplProp` syntax with the query script.
3. Decide whether the property needs an on-replicated callback.
4. Decide whether mandatory/default replication group and condition behavior is correct.
5. If the value is a scripted class or complex type, verify codec requirements.
6. Test initial state, runtime changes, streaming in/out, and JIP.

RPC workflow:

1. Decide why a property replication path is not enough.
2. Verify `RplRpc` constructor parameters and receiver/channel values with the query script.
3. Confirm the sender is allowed to request the action.
4. Confirm the receiver can exist under streaming and relevance rules.
5. Keep authority validation server-side for gameplay-affecting requests.
6. Test server-to-client, client-to-server, and owner/proxy cases separately.

`RplSave` / `RplLoad` workflow:

1. List each field that must be saved.
2. Choose bit width based on the real value range.
3. Write values in one fixed order.
4. Read values in exactly the same order.
5. Read and write exactly the same bit counts.
6. Test with edge values, JIP, and streamed entities.

Streaming-aware workflow:

1. Decide whether the state must reach all players or only relevant players.
2. Check whether target entities exist as proxies on recipient machines.
3. Avoid assuming a broadcast reaches clients that have not streamed the entity.
4. Re-test after moving clients far enough to trigger relevance changes.

VoN network workflow:

1. Add or verify `VoNComponent` for entities that send or receive VoN.
2. For radio VoN, verify that a radio manager entity exists in the game world.
3. Verify sender and receiver radio item setup and radio components.
4. Verify ACP stream setup and expected sound event routing.
5. Test direct speech and radio transmission in multiplayer, not only in editor preview.

## Configuration Fields And Tables

`RplProp` lookup fields to verify:

- replication group;
- on-replicated callback name;
- script context;
- replication condition;
- custom condition method name.

`RplRpc` lookup fields to verify:

- channel;
- receiver;
- condition;
- custom condition method name.

Codec and save/load fields to preserve:

- encoded value type;
- allowed value range;
- bit count;
- write order;
- read order;
- fallback/default behavior for missing or out-of-range data.

Streaming and operations fields to reason about:

- entity creation state;
- current replication state;
- streamed-in or streamed-out presence;
- relevance to each player;
- whether proxy exists on the receiver;
- whether operation order can race with spawn, stream, or RPC delivery.

VoN setup fields to verify:

- `VoNComponent` presence;
- direct speech vs radio flow;
- radio manager entity presence;
- radio item with radio component on sender and receiver;
- ACP stream node identifier;
- sound event names expected by the VoN setup;
- audio signal and variable routes used by the VoN graph.

## Procedures And Ordered Steps

Before writing network code:

1. Read this reference and the closest workflow reference for the feature domain.
2. Query exact API symbols before writing annotations, method calls, or component inheritance.
3. Inspect a bounded game-source snippet near the closest example.
4. Implement the smallest change that keeps authority, proxy, owner, streaming, and JIP behavior explicit.
5. Run a multiplayer verification pass.

Before using `RplProp`:

1. Query `RplProp`.
2. Query examples for `rpl-prop`.
3. Find an example with a similar field type.
4. Check whether the example uses an on-replicated callback.
5. Check whether the field type needs custom codec behavior.

Before using `RplRpc`:

1. Query `RplRpc`.
2. Query examples for `rpc`.
3. Confirm receiver and channel values.
4. Confirm call direction and authority validation.
5. Test with at least two clients when receiver routing matters.

Before adding custom save/load:

1. Query files for `RplSave`.
2. Query files for `RplLoad`.
3. Inspect the smallest relevant snippet.
4. Write down the read/write order.
5. Test value limits and JIP.

## Warnings And Failure Modes

- Do not let clients communicate gameplay state directly to other clients. Route gameplay state through the server or replicated state.
- Do not treat owner as authority. Owner is a special proxy concept.
- Do not mutate authoritative state from a proxy unless the exact API and example pattern prove the request path.
- Do not assume a client-created entity can be broadcast to everyone. If the server does not know the entity, the server cannot distribute it as shared state.
- Do not assume broadcast reaches machines where the entity is not streamed.
- Do not rely on local-only runtime state for JIP-critical gameplay.
- Do not let loadtime insertion differ between server and clients.
- Do not stream out unsupported loadtime authority cases.
- Do not spawn child entities during initialization without attaching them to the parent as part of the spawn process.
- Do not write and read different field orders in `RplSave` and `RplLoad`.
- Do not write and read different bit counts in `RplSave` and `RplLoad`.
- Do not use excessive bit counts without checking the expected value range.
- Do not mark scripted class values for replication without checking codec requirements.
- Do not validate replication only in local Workbench play. Dedicated-server and multi-client behavior can differ.
- Do not treat VoN as just audio authoring. Direct/radio voice also depends on network components, radio manager presence, and radio item setup.

## API Lookup Keys

Core replication:

- `RplComponent`
- `BaseRplComponent`
- `RplProp`
- `RplRpc`
- `RplGroup`
- `RplCondition`
- `RplChannel`
- `RplRcver`
- `RplRole`
- `RplSession`
- `RplSave`
- `RplLoad`
- `Rpc`
- `OnRpl`

Entity and component context:

- `IEntity`
- `GenericEntity`
- `GenericComponent`
- `ScriptComponent`
- `ScriptComponentClass`

VoN network routing:

- `VoNComponent`
- `BaseRadioComponent`
- `RadioManagerEntity`
- radio item classes
- sound event and stream-node related classes

Search terms:

- authority
- proxy
- owner
- replication state
- loadtime
- runtime
- local runtime
- Join In Progress
- streaming
- relevance
- broadcast
- codec
- network modding
- direct VoN
- radio VoN

## Game-Data Query Commands

Use exact lookup before writing API-sensitive code:

```powershell
py -3 scripts\query-reforger-data.py attribute RplProp --exact
py -3 scripts\query-reforger-data.py attribute RplRpc --exact
py -3 scripts\query-reforger-data.py symbol RplComponent --kind class --exact
py -3 scripts\query-reforger-data.py symbol BaseRplComponent --kind class --exact
```

Use task lookup for a bounded starting bundle:

```powershell
py -3 scripts\query-reforger-data.py lookup "make a replicated component"
```

Find implementation patterns:

```powershell
py -3 scripts\query-reforger-data.py examples replication --limit 8
py -3 scripts\query-reforger-data.py examples replication --subtopic authority --limit 8
py -3 scripts\query-reforger-data.py examples replication --subtopic rpc --limit 8
py -3 scripts\query-reforger-data.py examples replication --subtopic rpl-prop --limit 8
```

Find specific source families:

```powershell
py -3 scripts\query-reforger-data.py files RplDocs --limit 10
py -3 scripts\query-reforger-data.py files RplSave --limit 10
py -3 scripts\query-reforger-data.py files RplLoad --limit 10
```

Open bounded snippets only after choosing a specific result:

```powershell
py -3 scripts\query-reforger-data.py snippet scripts/GameLib/replication/RplDocs.c --line 1 --context 30
py -3 scripts\query-reforger-data.py snippet scripts/Game/Network/RplTestComponent.c --line 1 --context 30
py -3 scripts\query-reforger-data.py snippet scripts/Game/FiringRange/SCR_FiringRangeTarget.c --line 1 --context 30
```

Use JSON when another script or review pass needs structured output:

```powershell
py -3 scripts\query-reforger-data.py lookup "make a replicated component" --json
```

## Examples And Samples

Best game-source example routes:

- `RplDocs.c`: highest-value overview example for `RplProp`, `RplRpc`, authority/proxy terms, session callbacks, replication examples, and example components.
- `RplTestComponent.c`: compact runtime replication test component.
- deployable inventory item component examples: practical replicated state in gameplay components.
- firing range target examples: practical `RplSave`/`RplLoad` and bounded-value state.
- wave respawn timer, campaign network, building composition, and melee components: domain examples where replication interacts with gameplay systems.

Official sample status:

- No dedicated official sample is treated as the primary source for replication semantics in this reference.
- Prefer game-source examples found through the query script for exact API and implementation patterns.
- Use official sample project layout only as a broad layout signal when a task also involves addon/project structure.

How to use examples:

1. Start with `RplDocs.c` for concept-to-code routing.
2. Use `RplTestComponent.c` for a smaller component-shaped pattern.
3. Move to a domain example only after matching the feature area.
4. Open bounded snippets around the relevant line instead of loading entire files.
5. Verify exact signatures separately with symbol, attribute, or method lookup.

## Follow-Up Keywords

- authority
- proxy
- owner
- dedicated server
- client request
- server validation
- replicated component
- replicated property
- RPC receiver
- reliable channel
- unreliable channel
- custom condition
- `OnRpl`
- `RplSave`
- `RplLoad`
- codec
- bit count
- JIP
- streaming relevance
- streamed out
- broadcast
- local runtime
- loadtime
- direct voice
- radio voice
- radio manager
- `VoNComponent`
- `BaseRadioComponent`

## Verification

Minimum verification for replicated gameplay:

- Run in multiplayer, not only local Workbench play.
- Test on a dedicated server when gameplay state, ownership, or persistence matters.
- Test at least one authority path and one proxy path.
- Test owner-specific behavior separately from authority behavior.
- Test JIP by joining after state has already changed.
- Test streaming by moving clients into and out of relevance range.
- Test that broadcasts do not silently fail for streamed-out recipients.
- Test `RplSave`/`RplLoad` edge values and bit counts.
- Test RPC receiver/channel behavior in both expected and invalid sender cases.

Minimum verification for VoN:

- Confirm `VoNComponent` exists on the speaking/listening entity.
- Confirm direct speech works without assuming radio setup.
- Confirm radio VoN has a radio manager entity and radio components on the required items.
- Confirm ACP stream setup and sound events are present.
- Test with at least two clients connected to the same server.

Residual verification note:

- Game-data lookup verifies API names and examples. It does not prove runtime correctness. Authority, streaming, JIP, save/load, and VoN behavior must be verified in the appropriate multiplayer runtime.

## Official Wiki Links

- Multiplayer Scripting: https://community.bistudio.com/wiki/Arma_Reforger:Multiplayer_Scripting
- Audio: Voice over Network: https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Voice_over_Network

## Usefulness Score

Score: 96/100

Scoring breakdown:

- Wiki coverage: 30/30. The primary Multiplayer Scripting page is represented across network model, roles, states, streaming, JIP, RPC, replicated properties, save/load, codec requirements, and examples. The Voice over Network page is represented only for network-specific setup, which matches this reference boundary.
- Operational detail: 15/15. Workflows include authority-first design, replicated property setup, RPC setup, save/load ordering, streaming-aware behavior, and VoN network setup.
- API lookup usefulness: 15/15. Exact commands are provided for `RplProp`, `RplRpc`, `RplComponent`, `BaseRplComponent`, task lookup, examples, files, snippets, and JSON output.
- Example grounding: 9/10. Game-source replication examples are routed clearly. Official samples are not treated as primary because the useful replication examples are in game source, not a dedicated sample set.
- Codex task usefulness: 15/15. A Codex run can route replicated components, RPCs, save/load state, streaming behavior, and VoN setup without guessing APIs.
- Context efficiency: 8/10. The reference is dense and keeps signatures in lookup output, but multiplayer correctness requires several warning sections to avoid unsafe shortcuts.
- Verification guidance: 5/5. Dedicated-server, multi-client, streaming, JIP, RPC, save/load, and VoN verification are explicit.

Missed coverage and cap review:

- No owned Multiplayer Scripting source family is intentionally omitted.
- Full audio authoring is excluded by design and cross-owned by the audio reference, so it does not cap this score.
- Server config/startup fields are excluded by design and cross-owned by the server runtime reference, so they do not cap this score.
- No automatic failure applies: authority/proxy/owner distinctions are explicit, multiplayer verification is explicit, official wiki links are present, query commands are present, examples are routed, and no broad API dump is embedded.
