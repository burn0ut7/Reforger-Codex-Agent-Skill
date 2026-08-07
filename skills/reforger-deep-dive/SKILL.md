---
name: reforger-deep-dive
description: Forensically investigate one difficult Arma Reforger failure, design question, or comprehensive review and produce a read-only evidence dossier for a later implementation.
---

# Reforger Deep Dive

Run a forensic, read-only investigation. End with a causal evidence dossier; leave implementation to a separate `$reforger` invocation. This context boundary protects the investigation from rushing toward a fix.

Before the first Reforger MCP call, read the shared [MCP router](../reforger/references/mcp-router.md), [Wiki routes](../reforger/references/wiki-routes.md), and [evidence contract](../reforger/references/evidence-contract.md). Apply their authority, freshness, no-guess API, and evidence rules. Keep workspace files and live Workbench/editor state unchanged. Use diagnostic validation only when it directly distinguishes a hypothesis; keep reload, play control, saves, process lifecycle, and mutations outside this skill.

## Cost boundary

- Investigate one question or one tightly coupled failure cluster.
- Start with one evidence pass; expand only for a material unresolved contradiction.
- Preflight each relevant authority once. Follow one explicit retryable recovery; otherwise mark the row blocked immediately and use no substitute evidence source.
- Use no subagents when direct inspection can settle the question.
- Use at most two read-only subagents in one round when separate evidence tracks can run independently or a falsification pass could change the conclusion. Give each a bounded question and raw context. Keep synthesis in the primary agent.
- At twelve primary evidence calls or after the subagent round, checkpoint. Continue for one additional pass only when a named unresolved hypothesis has a specific next call capable of deciding it.
- Stop when every material hypothesis is supported, refuted, or blocked by a named unavailable authority.

## 1. Fix the forensic question

Record the reported symptom, expected invariant, observable failure condition, affected surfaces and runtime roles, requested deliverable, required authorities, and evidence that would change the user's decision. For a comprehensive review, select every applicable lens in one pass: API contract, lifecycle and ownership, authored data/editor state, multiplayer, and runtime behavior.

Complete this step when one checkable question defines the dossier's boundary.

## 2. Form competing hypotheses

Create a compact matrix:

| Hypothesis | Confirms it | Refutes it | Owning authority | Route | Status |
| --- | --- | --- | --- | --- | --- |

Include plausible alternatives that predict different observations. Assign Wiki concepts, Game Data declarations, workspace behavior, authored state, and live behavior only to their owning evidence sources. Delegate only distinct rows or one independent falsification pass.

Complete this step when each material hypothesis has a decisive observation and evidence route.

## 3. Collect decisive evidence

- Follow the narrowest route that can distinguish hypotheses before widening the search.
- Maintain an API ledger for every exact engine identifier discussed in a technical conclusion.
- Trace data, control flow, lifecycle, ownership, persistence, and runtime roles only where they can alter the diagnosis.
- Preserve conflicting observations instead of averaging them into a weak conclusion.
- Treat subagent conclusions as hypotheses and verify their cited evidence in the primary thread.

Complete this step when every matrix row has a disposition or an exact blocker.

## 4. Falsify the leading explanation

Seek the strongest counterexample, alternate lifecycle ordering, alternate owning surface, and—when relevant—authority/proxy or JIP observation. State what the leading explanation predicts and compare it with the retrieved evidence.

Complete this step when the leading mechanism explains all material observations and its viable competitors are refuted, or when the dossier explicitly remains inconclusive.

## 5. Deliver the evidence dossier

Return:

1. The diagnosis or decision, confidence, and one-sentence mechanism.
2. The symptom and invariant.
3. The completed hypothesis matrix.
4. A causal chain from trigger to observed result.
5. Wiki, Game Data, workspace, resource, compiler, and live citations for every material claim.
6. The verified API ledger when exact identifiers matter.
7. Unknowns, unavailable authorities, and the narrowest decisive experiment.
8. An implementation handoff containing the owning surfaces, preserved invariants, likely change boundary, and required validation—without code or live mutation.

Complete the skill when the dossier answers the original question or proves exactly why current evidence cannot answer it.
