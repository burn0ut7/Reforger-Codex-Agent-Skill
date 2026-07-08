# Arma Reforger Codex Skill

A Codex skill for Arma Reforger modding, Enfusion Script, Workbench data, and Reforger API lookup.

## What

This skill gives Codex a Reforger-specific router and reference set. It helps an AI assistant understand where to look before giving advice or making code changes.

It is intended for:

- Learning Arma Reforger scripting and mod structure.
- Reviewing Enfusion Script and Reforger mod code.
- Explaining general Reforger concepts and workflows.
- Giving practical advice for entities, components, networking, prefabs, configs, Workbench, scenarios, terrain, assets, weapons, vehicles, audio, animation, servers, and Workshop packaging.
- Looking up APIs from extracted game script data instead of relying only on model memory.

It is not intended to blindly generate large amounts of SLOP code. The goal is grounded help: concepts, review, small correct changes, examples, and API-aware guidance.

## Why

Arma Reforger has a large API surface, a distinct scripting language, and documentation spread across game files, official wiki pages, generated API docs, and official samples. Game updates can change APIs and behavior.

This skill keeps Codex grounded in local, refreshable source data:

- Official Bohemia wiki/docs.
- Official Bohemia sample mods.
- Extracted Arma Reforger game script/API data.

`SKILL.md` stays compact and acts as the router. Detailed information lives in focused reference files that Codex opens only when needed.

## Install

Place this folder in your Codex skills directory.

On Windows, the usual location is:

```text
C:\Users\<you>\.codex\skills\reforger
```

The required skill file should be here:

```text
C:\Users\<you>\.codex\skills\reforger\SKILL.md
```

After that, start a new Codex session so the skill can be discovered.

## How To Use

Ask Codex to use the skill when working with Reforger:

```text
Use $reforger to review this ScriptComponent.
```

```text
Use $reforger to explain how replication should work for this action.
```

```text
Use $reforger to help create a small component that prints debug info.
```

Codex should read `SKILL.md` first, then open the relevant reference under `references/`. For uncertain APIs, it should check the topical reference first, then `references/api-main.md`, then `references/api-extended.md`.

## Optional: Regenerate

You can use the skill as-is. You do not need to regenerate it every time.

Regeneration is useful when Arma Reforger updates, the official docs change, or you want to rebuild the references from newer raw data.

Regeneration requirements:

- PowerShell for the included Windows refresh scripts.
- Python for the documentation/API helper scripts.
- Arma Reforger installed locally if you want to refresh extracted game data.
- Git if you want to refresh the official sample repository.

This skill is written for Codex, but the references and generation approach can be adapted for other AI agents with some tweaking.

The intended regeneration flow is:

1. Ask Codex to use this skill and follow `generation/design.md`.
2. Refresh raw data only if asked or if data is missing.
3. Pull game script/API data, wiki/docs data, and official samples as needed.
4. Build `references/api-extended.md` from all extracted APIs.
5. Use `generation/design.md` to rebuild the focused references and `SKILL.md`.
6. Review `generation/review.md` after generation.

Useful commands for raw data refresh:

```powershell
py -3 .\scripts\update-reforger-data.py --check
py -3 .\scripts\update-reforger-data.py --if-needed
py -3 .\scripts\update-reforger-data.py
py -3 .\scripts\update-reforger-wiki-docs.py
powershell -ExecutionPolicy Bypass -File .\scripts\update-reforger-samples.ps1
py -3 .\scripts\build-reforger-extended-api-reference.py
```

`--check` is non-mutating and reports whether remote game data changed. `--if-needed` skips refresh when the local game data already matches the upstream commit.

`generation/design.md` contains the full generation rules. `generation/review.md` is overwritten on each full generation run and summarizes what was created, refreshed, skipped, or needs review.

## Source Priority

When regenerating, sources are prioritized in this order:

1. Official wiki/docs as the source of truth.
2. Official Bohemia samples for concrete examples and layouts.
3. Extracted game API data for exact names, signatures, inheritance, and source paths.

Generated references are outputs, not source material for future generations.
