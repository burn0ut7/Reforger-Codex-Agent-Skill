---
name: reforger-workbench-edit
description: Operate supported live Arma Reforger Workbench mutations through exact MCP routes for entities, components, prefabs, and shape geometry, with controlled confirmation, persistence, readback, and recovery.
---

# Reforger Workbench Edit

Run an explicitly requested live editor mutation as a low-freedom operation. Before the first Reforger MCP call, read the shared [MCP response protocol](../reforger/references/mcp-router.md#response-protocol), [Workbench mutation contract](../reforger/references/evidence-contract.md#workbench-mutation-contract), and [operator routes](references/operator-routes.md). The live tool catalogue and returned structured recovery remain authoritative.

## 1. Fix the transaction

Record the exact outcome, project/add-on/world, stable targets, destination or value, persistence boundary, destructive effects, and readback that will prove success. Resolve "this," "that," and "selected" through live selection inspection. Ask for direction when one stable target, destination, destructive scope, or persistence choice cannot be established.

Complete this step when the transaction names exact targets and one checkable after-state.

## 2. Establish preconditions

Inspect Workbench status, project context, editor state, active world/subscene/layer, play-session state, and relevant layer locks. Resolve each target through the matching read route in [operator-routes.md](references/operator-routes.md), then capture its before-state. Verify engine class names through Game Data and resource identities through the resource route before emitting them into mutation calls.

Complete this step when the intended project is active, the editor permits the operation, and every target identity and before-state is current.

## 3. Prepare one operation

Select one supported mutation route. Preserve exact identities, descriptors, revisions, and returned handoffs as evidence. Pass only fields accepted by the live input schema, copying every required opaque value unchanged. Calculate explicit coordinates, angles, scale, geometry, or values; use viewport, terrain, trace, or coordinate-conversion reads when placement depends on live space.

Complete this step when one tool call and its expected readback are fully determined from current evidence.

## 4. Preview, execute, and read back

For a preview-confirm route, call it without a token, inspect the proposed target/effect, then repeat it with the returned confirmation token unchanged. Execute one mutation at a time. Immediately use the route's named inspection tool to compare the exact effective after-state with the expected state.

On a stale identity, rejected descriptor, changed editor context, structured error, or readback mismatch, stop the transaction and follow the returned recovery. Use native undo only under the rollback conditions in [operator-routes.md](references/operator-routes.md).

Complete this step when the operation has matching readback or has been safely stopped with no later mutation attempted.

## 5. Continue and persist

Repeat preparation and readback for each remaining authorized operation. Keep the live write sequence in one primary agent; delegate only separable read-only API or resource research. Persist using the exact route for the owning surface. Account for tools that auto-save and for `workbench_save` saving all open tabs plus the named active world.

Complete this step when every authorized operation is read back and its requested persistence is independently confirmed.

## 6. Verify and report

Exercise the smallest requested editor or runtime behavior when feasible, inspect fresh scoped logs, and return any play session started for the test to edit mode. Report exact targets, before/after state, operations, confirmation tokens used, persistence results, undo/recovery actions, behavioral observations, logs, and manual checks as separate claims.

Complete the skill when effective state, persistence, and feasible behavior all match the transaction or a precise unsupported/blocked result is established.
