# Arma Reforger Codex Skill

A Codex skill for Arma Reforger modding, Enfusion Script, Workbench workflows, and source-backed Reforger API lookup.

This skill helps Codex answer and work on Reforger tasks without guessing from general game-engine memory. It gives Codex a compact router, focused references, and local game-data search so answers can be grounded in Reforger-specific source information.

## What It Helps With

Use this skill when you want Codex help with:

- Enfusion Script and Reforger mod code.
- Entities, components, lifecycle, user actions, and gameplay patterns.
- Multiplayer, authority, replication, RPCs, and dedicated-server concerns.
- Resources, prefabs, configs, catalogs, and Workbench-authored data.
- Scenario Framework, Game Master, factions, tasks, and game modes.
- Terrain, World Editor tools, navmesh, assets, weapons, vehicles, gear, UI, audio, animation, AI, servers, and Workshop packaging.
- Reviewing patches for Reforger API mistakes and incorrect engine assumptions.

The goal is practical help: explanations, reviews, small correct changes, source-backed examples, and API-aware guidance.

## Why It Exists

Arma Reforger has its own engine, scripting language, editor workflows, data model, and multiplayer rules. It is easy for a general AI model to accidentally lean on Unity, Unreal, C#, SQF, or Arma 3 assumptions.

This skill keeps Codex focused on Reforger by using:

- Curated runtime references for the major Reforger systems.
- Extracted game script data for exact API names, signatures, inheritance, and source locations.
- Bounded source snippets and examples when implementation patterns matter.
- Strict rules that push Codex to verify APIs before writing code.

## Key Features

- **Focused references**: 26 runtime references cover scripting, Workbench, resources, networking, scenarios, world tools, assets, weapons, vehicles, animation, audio, UI, AI, servers, and common task recipes.
- **Exact API lookup**: Codex can query extracted Reforger game data instead of relying on memory.
- **Source-backed examples**: Codex can find relevant game-source examples and bounded snippets before proposing API-sensitive code.
- **Piecemeal work strategy**: Complex tasks are broken into small verified slices instead of broad speculative rewrites.
- **API and idiom verification**: Generated code should verify meaningful Reforger API calls and common usage patterns, including helper calls.
- **Verification mindset**: The skill reminds Codex to call out anything that still needs Workbench, runtime, multiplayer, server, editor, packaging, or asset validation.

## Install

Place this skill folder in your Codex skills directory.

On Windows, a typical path is:

```text
C:\Users\<you>\.codex\skills\reforger
```

The skill file should be here:

```text
C:\Users\<you>\.codex\skills\reforger\SKILL.md
```

Start a new Codex session after installing so Codex can discover the skill.

## How To Use

Ask Codex to use the Reforger skill when working on Arma Reforger tasks:

```text
Use $reforger to review this ScriptComponent for API mistakes.
```

```text
Use $reforger to explain how replication should work for this user action.
```

```text
Use $reforger to help make a small component that spawns a prefab.
```

```text
Use $reforger to find the right Reforger API for a HUD widget.
```

Codex should read the skill, open the relevant references, search game data for exact APIs, inspect examples or snippets when needed, and then give a grounded answer or focused change.

## Updating Game Data

Most users can use the skill as-is. If the local Reforger game data is missing or stale, refresh only the raw game data with:

```powershell
py -3 scripts\update-reforger-data.py --if-needed
```

Normal skill use does not require live wiki access or running generation tools.

## What This Is Not

- Not a replacement for Workbench, in-game, multiplayer, dedicated-server, packaging, or asset validation.
- Not a bulk code generator.
- Not permission for Codex to skip API lookup.
- Not a general Unity, Unreal, C#, SQF, or Arma 3 assistant.
- Not dependent on live wiki scraping during normal use.

## For Contributors

The main runtime pieces are `SKILL.md`, `references/`, `raw/game-data/`, `scripts/query-reforger-data.py`, and `scripts/update-reforger-data.py`.

The deeper generation design is documented under `generation/` for contributors who are rebuilding the skill and references. End users do not need that workflow for normal use.
