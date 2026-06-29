# Networking Multiplayer Replication

## When to read this reference

Read before writing or reviewing multiplayer logic, replicated state, RPCs, server/client branches, owner actions, Join In Progress behavior, streaming behavior, replicated spawning/despawning, or movement of shared gameplay entities.

## Search terms

`Replication`, `RplComponent`, `BaseRplComponent`, `authority`, `proxy`, `owner`, `RplProp`, `RplRpc`, `RpcAsk`, `RpcDo`, `Replication.BumpMe`, `Join In Progress`, `JIP`, `streaming`, `RplLoad`, `RplSave`, `RplChannel`, `RplRcver`, `RplCondition`

## Source authority summary

The multiplayer scripting wiki page defines network roles, replication states, RPC/RplProp patterns, streaming, JIP, and codec behavior. Extracted API data verifies `RplRpc`, `RplProp`, `BaseRplComponent`, `GenericEntity.Rpc`, `GenericComponent.Rpc`, and serialization signatures. Samples are secondary unless they show a project-specific base class.

## Network architecture

Arma Reforger uses a classical server-client architecture:

- There is one server. Multiplayer game state is destroyed if the server loses connection; server role does not transfer.
- Clients communicate with the server, not directly with each other.
- In single-player, the local machine is considered a player-hosted server.
- Proper multiplayer code should generally work in single-player and vice versa.
- A server can be dedicated or player-hosted/listen.
- Distributed server and Arma 3 headless client patterns are not Reforger patterns.

Dedicated server caveat from docs: some components and classes inheriting from them are not instantiated on a dedicated server, including camera-handler, debug-shoot, motor-exhaust-effect, and base sound component families. Do not assume camera, local player, UI, sound, or visual-only components exist on a dedicated server.

## Authority, proxy, and owner

Write code around roles:

- Authority: the reference entity on the machine that created/owns the authoritative state. For mission objects this is usually the server.
- Proxy: local representation of an authority on another machine. It receives updates and generally should not mutate authoritative state.
- Owner: an additional role, not authority. One machine can own an entity and has limited elevated rights, commonly to send owner-to-authority RPCs.

Critical rule: authority is set when an entity is created and cannot be transferred. Ownership can be transferred; authority cannot.

For a server-created entity:

- The server hosts the authority.
- Other machines receive proxies.
- The authority can give/take ownership.

For a client-created entity:

- The client hosts the authority.
- The server is unaware of the entity.
- The entity is not replicated to other machines.
- Its methods cannot later be broadcast to everyone because other machines have no proxy/authority reference.

## Replication states

Replication distinguishes loadtime, runtime, and local runtime items.

Loadtime items:

- Usually world-placed entity instances such as buildings or street signs.
- Do not require prefab for spawning.
- Must be deterministic on server and clients.
- Initial world state must match; mismatch can produce "inconsistent item table" and disconnect with JIP error.
- May stay out of sync for a long time until relevance/streaming decides a client needs current state.
- Complete removal on authority is replicated unconditionally.
- Streaming out while authority still exists on server is documented as undefined behavior and must be avoided.

Runtime items:

- Created during session by systems such as game mode or Game Master.
- Require prefab for spawning.
- May only be inserted on the server when they should replicate.
- Proxies may or may not exist on a client depending on relevance/streaming.

Local runtime items:

- Created on a client during a session.
- Useful for local predicted effects, such as a client immediately spawning a rocket effect before server state streams.
- Do not require prefab for spawning.
- Exist only on that client; no proxies on server or other clients.

State override caveat:

- `Rpl State Override` can make a hierarchy behave as runtime during insertion.
- Child entities spawned during initialization must be attached as part of the spawning process.
- Spawning first and attaching later can insert the child separately and can defeat runtime override, creating undefined loadtime behavior.

## Streaming, relevance, and Join In Progress

Streaming creates, updates, and deletes proxies based on relevance. A far-away car may not exist on a client's machine until the client becomes relevant to it. When streamed in, the proxy is created and synchronized with the authority. While the proxy exists, it receives state updates and can send/receive RPCs.

Broadcast trap: an RPC broadcast only reaches machines that currently have the proxy streamed in. It is not "all connected clients" if some clients do not have the entity.

Owner exception: the owner entity is always present on its machine while ownership remains.

Join In Progress uses the same streaming/synchronization principles. Replicated properties and `RplSave`/`RplLoad` matter for late joiners.

## RPC method workflow

RPC uses `Rpc(method, p0, p1, ...)` on `GenericEntity`/`GenericComponent` to queue a network-friendly method call. The target method's `[RplRpc]` attribute determines where it executes.

Convention from docs:

- `RpcAsk_`: owner asks the authority to do something.
- `RpcDo_`: authority tells owner/proxies to do presentation or follow-up work.
- Do not call RPC methods from `EOnInit`; the docs say this is unsupported due to initialization order.
- RPC order between two machines is guaranteed, but network batching/sending may group calls.

`RplRpc` signature retained from docs:

```c
void RplRpc(RplChannel channel, RplRcver rcver, RplCondition condition = RplCondition.None, string customConditionName = "")
```

`RplChannel`:

- `Reliable`: guaranteed delivery; more expensive, use carefully.
- `Unreliable`: can be overridden/dropped depending on order; suited for non-important or frequent updates such as positions.

`RplRcver`:

- `Server`: run on authority.
- `Owner`: run on owner.
- `Broadcast`: run on proxies only, not on authority; only streamed proxies receive it.

`RplCondition`:

- `None`: run in all cases.
- `OwnerOnly`: only owner machine.
- `NoOwner`: machines that are not owner.
- `Custom`: uses a named custom condition.

official-doc-example

```c
[RplRpc(RplChannel.Reliable, RplRcver.Server)]
protected void RpcAsk_Authority_Method(bool turningOn)
{
	if (turningOn == m_bIsTurnedOn)
		return;

	m_bIsTurnedOn = turningOn;
	Rpc(RpcDo_Broadcast_Method, turningOn);
	Rpc(RpcDo_Owner_Method);
}

[RplRpc(RplChannel.Reliable, RplRcver.Owner)]
protected void RpcDo_Owner_Method()
{
	Print("owner-side code");
}

[RplRpc(RplChannel.Reliable, RplRcver.Broadcast)]
protected void RpcDo_Broadcast_Method(bool turningOn)
{
	Print("proxy-side code");
}
```

## RplProp workflow

`[RplProp]` marks state to be replicated. Mutate replicated state on the authority. Do not locally set the proxy and expect broadcast; proxy-local changes create temporary state divergence until authority updates.

official-doc-example

```c
[RplProp(onRplName: "OnTurnedOnUpdated")]
protected bool m_bIsTurnedOn = false;

[RplRpc(RplChannel.Reliable, RplRcver.Server)]
protected void RpcAsk_Authority_Method(bool turningOn)
{
	if (turningOn == m_bIsTurnedOn)
		return;

	m_bIsTurnedOn = turningOn;
	SetLedLightColour();          // authority local update
	Replication.BumpMe();         // signal changed properties
}

protected void OnTurnedOnUpdated()
{
	SetLedLightColour();          // proxy update callback
}
```

Docs note that `OnTurnedOnUpdated` is called on proxies when replication updates the property; it is not called automatically on the authority in that example, so the authority updates its own presentation directly.

Operations order warning: loading order between `RplLoad` and member variable updates is not guaranteed and may change. Current order in docs: hierarchy creation, `RplLoad`, then member variable values in unguaranteed order triggering their `onRplName` methods.

## RplSave/RplLoad

Use `RplSave`/`RplLoad` for state that is not automatically represented by `RplProp` or when packing matters. Authority writes values in order; streamed proxy reads them in exactly the same order and checks each read.

official-doc-example

```c
override bool RplSave(ScriptBitWriter writer)
{
	writer.Write(m_iSoldierId, 32);
	writer.Write(m_iHealth, 7);
	writer.WriteBool(m_bHadLunch);
	writer.WriteString(m_sSoldierDogTag);
	return true;
}

override bool RplLoad(ScriptBitReader reader)
{
	if (!reader.Read(m_iSoldierId, 32))
		return false;
	if (!reader.Read(m_iHealth, 7))
		return false;
	if (!reader.ReadBool(m_bHadLunch))
		return false;
	if (!reader.ReadString(m_sSoldierDogTag))
		return false;
	return true;
}
```

Packing detail from docs: writing 7 bits for health is enough when the value cannot exceed 100 because 7 bits cover 0..127.

## Codec methods for custom replicated classes

When a scripted class is marked with `[RplProp]`, defining codec methods may be required for custom types. The network modding docs define:

- `Encode`: snapshot to compressed packet.
- `Decode`: packet to snapshot.
- `SnapCompare`: compare snapshots.
- `PropCompare`: compare current property memory to snapshot.
- `Extract`: instance to snapshot.
- `Inject`: snapshot to instance.

Use thresholds for float/vector properties to avoid creating too many snapshots due to tiny changes.

## BaseRplComponent and hierarchy caveats

Extracted API docs describe `BaseRplComponent` as a convenience wrapper around the replication node. During initialization it traverses the entity component hierarchy, collects replicated items, and registers them into the replication pipeline. It listens to hierarchy changes by default.

Important caveats:

- If something is spawned after `BaseRplComponent` `EOnInit`, it may not be registered automatically.
- Disabling self-insert makes the user responsible for `InsertToReplication`.
- Not every replicated entity can change hierarchy at will; replication node collections are immutable and careless changes can cause serious malfunction.
- Upon destruction it unregisters contents automatically.

## Authority-safe user action pattern

When a user action changes gameplay state:

1. Action runs where the interaction occurs, often owner/client-side.
2. Client/owner validates local intent only.
3. Owner calls `RpcAsk_...` to authority/server.
4. Authority validates state and mutates replicated data.
5. Authority calls `Replication.BumpMe()` or sends `RpcDo_...` presentation events as appropriate.
6. Proxies update presentation in `onRplName` handlers or `RpcDo_...`.

## API Notes

Use `api-main.md` for `BaseRplComponent`, `RplProp`, `RplRpc`, `OnRpl`, `RplRole`, `RplRcver`, `RplChannel`, `RplCondition`, `ScriptBitReader`, `ScriptBitWriter`, `GenericEntity.Rpc`, and `GenericComponent.Rpc`. Use `api-extended.md` for exact replication helper signatures and project-specific systems.

## Common Traps

- Branching only on server/client instead of authority/proxy/owner.
- Creating gameplay entities on a client and expecting the server to know about them.
- Mutating replicated state on a proxy.
- Calling RPC from `EOnInit`.
- Using broadcast when clients may not have the proxy streamed in.
- Forgetting `Replication.BumpMe()` after changing `RplProp` state when the pattern requires it.
- Spawning children after replication insertion or attaching them after spawn in a way that breaks hierarchy insertion.
- Assuming JIP receives non-replicated fields without `RplProp` or `RplSave`/`RplLoad`.

## Review Checklist

- Is authority/proxy/owner role stated?
- Is state mutation authority-side?
- Are RPC receiver/channel/condition values verified?
- Are streaming/JIP consequences covered?
- Are dedicated-server assumptions safe?
- Is multi-peer or dedicated-server test listed?

## Authority Detail

- Authority is the side allowed to make authoritative gameplay state changes for an entity.
- Proxy instances observe replicated state and should not independently mutate authoritative state.
- Ownership determines who may be allowed to request changes, but ownership is not the same as authority.
- Dedicated servers often have authority without local UI or player input context.
- Listen servers can hide authority mistakes because host and client are in one process.
- Always state which side receives input, which side validates, and which side mutates state.
- Validate requests server-side even when the client UI only exposes valid options.

## RPC Detail

- Use RPC for events and requests that need to cross machine boundaries.
- Use reliable RPC for important state-changing requests.
- Use unreliable RPC only when loss is acceptable.
- Receiver selection must match the communication path: client to server, server to owner, server to proxies, or broadcast.
- Do not call RPC before replication identity and streaming state are valid.
- Do not use RPC as persistent state for join-in-progress clients.
- Keep RPC payloads small and validate object/resource references.

## RplProp Detail

- Use `RplProp` for state that clients need to observe.
- Use `onRplName` callbacks for client-side reactions to changed replicated values.
- Call `Replication.BumpMe()` when the replication pattern requires explicit dirty marking after state mutation.
- Do not mutate replicated state on proxies and expect authority to accept it.
- Pack only the state that needs replication; avoid large or redundant fields.
- Consider custom save/load only when default property replication is insufficient.
- Test join-in-progress clients for persistent state.

## Streaming And Hierarchy Detail

- Replicated entities can stream in and out for clients.
- Broadcast RPC only reaches relevant streamed proxies.
- Children spawned after replication insertion can miss expected hierarchy replication if attached incorrectly.
- Spawn and attach replicated hierarchies through supported authoritative patterns.
- Do not assume a client has a referenced entity when an RPC arrives.
- Guard null entity references on clients.
- Treat hierarchy changes as multiplayer-sensitive even when they look local in editor tests.

## Dedicated Server Detail

- Dedicated server code has no local player UI context.
- Input handling belongs on clients; validated state changes belong on authority.
- Server logs are often the best evidence for authority-side execution.
- Client-only visual/audio feedback should be separated from server state changes.
- Server startup configs and addon load order can change whether classes/resources exist.
- Test at least host/client for interaction work and dedicated server for server-facing features.

## Multiplayer Review Detail

- Identify the entity that owns the replicated state.
- Identify who receives player input.
- Identify who validates the request.
- Identify who mutates state.
- Identify which clients need to see the result.
- Identify whether late joiners need the result.
- Identify whether the state belongs in `RplProp`.
- Identify whether the action belongs in `RplRpc`.
- Identify whether a visual-only effect can stay client-side.
- Identify whether resource references are available on server and clients.
- Identify whether the target entity may be streamed out.
- Identify whether the RPC receiver can legally receive the call.
- Identify whether the owner can change during gameplay.
- Identify whether authority transfer is possible.
- Identify whether dedicated server has all required non-UI code.
- Identify whether tests cover host/client and dedicated server where relevant.
