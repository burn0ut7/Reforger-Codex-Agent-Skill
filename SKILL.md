---
name: reforger
description: Build, review, and modify Arma Reforger mods and Enfusion Script code. Use for Arma Reforger scripting, Workbench, entities/components, replication/multiplayer, resources, prefabs, configs, scenarios, Game Master, terrain/world editor, weapons, vehicles, animation, audio, server config, Workshop packaging, and Reforger API lookup.
---

# Arma Reforger Modding Skill

Use this skill for Arma Reforger and Enfusion Script work. Start by routing the task to the smallest relevant reference, read that reference before implementing or answering, then verify exact APIs in `references/api-main.md` or `references/api-extended.md` before giving code that depends on signatures.

## Routing

- Script basics, modules, logging, Remote Console, modded classes: `references/scripting-core.md`
- Enfusion language syntax and data types: `references/scripting-language.md`
- Entities, components, event masks, lifecycle, transforms: `references/entity-component-lifecycle.md`
- Multiplayer, authority, replication, RPC, join-in-progress: `references/networking-multiplayer-replication.md`
- Resources, prefabs, configs, catalogs, UI layouts: `references/resources-prefabs-configs.md`
- Workbench plugins, editor tools, debugging: `references/workbench-tools-debugging.md`
- Scenario Framework, Game Master, editable entities: `references/scenario-framework-game-master.md`
- Terrain, World Editor, navmesh, world layout: `references/terrain-world-editor.md`
- Weapons, vehicles, props, animation, audio: `references/assets-weapons-vehicles-animation-audio.md`
- Server config, startup parameters, packaging: `references/server-runtime-packaging.md`
- Official sample selection and reusable patterns: `references/examples-patterns.md`
- Frequent implementation recipes: `references/common-task-recipes.md`
- High-frequency API signatures: `references/api-main.md`
- Extended generated API index: `references/api-extended.md`

## Operating Rules

- Prefer data, prefab, config, and Workbench workflows before adding script.
- Treat multiplayer as authority-first: clients request, authority validates and mutates state, replicated state is explicit.
- Do not assume local-player APIs are valid on dedicated servers.
- For assets, inspect the closest official sample pattern before inventing structure.
- For Workbench plugins, use editor/plugin APIs; do not mix them with runtime gameplay assumptions.
- For API-sensitive answers, cite the reference file used and keep exact signatures aligned with the generated API index.
- For nontrivial tasks, read the topical reference and `references/common-task-recipes.md`; for unfamiliar assets or layouts, also read `references/examples-patterns.md`.
- If a reference does not contain enough detail to answer safely, say what is missing and verify against `references/api-extended.md` or the project files before inventing behavior.

## Answer Protocol

- Classify the task as script-first, data-first, editor-first, server-first, asset-first, or mixed.
- Name the reference files used when the answer depends on Reforger-specific behavior.
- Include required Workbench, prefab, config, server, or packaging steps alongside code.
- State residual verification: compile, Workbench save/reopen, Resource Manager check, host/client test, dedicated-server launch, or Workshop/package check as relevant.

## Review Bias

When reviewing Reforger code or content, look first for lifecycle misuse, missing `super` calls in overrides, unregistered or uncleared event masks, client-side authority changes, unresolved resources, prefab/config/catalog omissions, and scripts solving problems that should be data-driven.
