---
name: reforger-deep-dive
description: Forensically investigate one difficult Arma Reforger failure, design question, or comprehensive review and produce a read-only evidence dossier for later implementation. Use for uncertain root causes, competing technical explanations, or cross-surface Reforger reviews.
---

# Reforger Deep Dive

Run a forensic, read-only investigation. End with a causal evidence dossier; leave implementation to a separate implementation request. This boundary prevents a difficult investigation from rushing toward a fix.

Before the first Reforger MCP call, read the shared [MCP router](../reforger/references/mcp-router.md), [Official Wiki routes](../reforger/references/wiki-routes.md), and [evidence contract](../reforger/references/evidence-contract.md). Apply their authority, freshness, no-guess API, and evidence rules. Keep workspace files and live editor state unchanged. Use `workbench_validate_scripts` only when native diagnostic evidence directly distinguishes a hypothesis; keep reload, play control, saves, process lifecycle, bridge maintenance, and mutation outside this skill.

If Workbench integration is disabled, perform no Workbench traffic and use only offline Wiki, Game Data, and workspace evidence. Record the unavailable live authority and its recovery without enabling it.

## Cost boundary

- Investigate one question or tightly coupled failure cluster.
- Start with one evidence pass; expand only for a material unresolved contradiction.
- Preflight each relevant authority once. Follow one explicit retryable recovery; otherwise mark that evidence blocked without substituting a weaker source.
- Use parallel read-only investigation only when independent evidence tracks or a falsification pass can change the conclusion. Keep synthesis in the primary investigation.
- At twelve primary evidence calls, checkpoint the matrix, cost, and remaining deciding routes. Continue while a named unresolved material hypothesis has a specific next call capable of deciding it.
- Stop when every material hypothesis is supported, refuted, or blocked by a named unavailable authority.

## 1. Fix the forensic question

Record the symptom, expected invariant, observable failure condition, affected surfaces and runtime roles, requested deliverable, required authorities, and evidence that would change the decision. For a comprehensive review, select each applicable lens in one pass: API contract, lifecycle and ownership, authored data/editor state, multiplayer, and runtime behavior.

Complete this step when one checkable question defines the dossier boundary.

## 2. Form competing hypotheses

Create a compact matrix:

| Hypothesis | Confirms it | Refutes it | Owning authority | Route | Status |
| --- | --- | --- | --- | --- | --- |

Include plausible alternatives that predict different observations. Assign Wiki concepts, Game Data declarations, workspace behavior, authored state, and live behavior only to their owning evidence sources.

Complete this step when each material hypothesis has a decisive observation and evidence route.

## 3. Collect decisive evidence

- Follow the narrowest route that distinguishes hypotheses before widening the search.
- Maintain an API ledger for every exact engine identifier used in a technical conclusion.
- Trace data, control flow, lifecycle, ownership, persistence, and runtime roles only where they can alter the diagnosis.
- Preserve conflicting observations instead of averaging them into a weak conclusion.
- Treat delegated conclusions as hypotheses and verify their cited primary evidence before synthesis.

Complete this step when every matrix row has a disposition or exact blocker.

## 4. Falsify the leading explanation

Seek the strongest counterexample, alternate lifecycle ordering, alternate owning surface, and, when relevant, authority/proxy or join-in-progress observation. State what the leading explanation predicts and compare it with the retrieved evidence.

Complete this step when the leading mechanism explains all material observations and viable competitors are refuted, or the dossier explicitly remains inconclusive.

## 5. Deliver the evidence dossier

Return:

1. The diagnosis or decision, confidence, and one-sentence mechanism.
2. The symptom and invariant.
3. The completed hypothesis matrix.
4. A causal chain from trigger to observed result.
5. Wiki, Game Data, workspace, resource, compiler, and live citations for every material claim.
6. The verified API ledger when exact identifiers matter.
7. Unknowns, unavailable authorities, and the narrowest decisive experiment.
8. An implementation handoff containing owning surfaces, preserved invariants, likely change boundary, and required validation, without code or live mutation.

Complete the skill when the dossier answers the original question or proves exactly why current evidence cannot answer it.
