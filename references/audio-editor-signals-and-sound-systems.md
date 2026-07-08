# Audio Editor Signals And Sound Systems

## When To Read

Read this when the task is about Reforger audio authoring or runtime sound behavior:

- using Audio Editor, Signal Editor, audio nodes, DSP nodes, signal nodes, audio variables, directivity, and editor validation;
- creating or modifying sound events, sound components, audio signals, music, occlusion, radio broadcast behavior, or sound manager module setup;
- wiring audio for building doors, collision, multiphase destruction, trees, vehicle damage, or Voice over Network from the audio-system side;
- finding exact audio, sound event, sound component, sound manager, voiceover, or `AudioSystem` APIs before writing code;
- debugging sound events that do not play, play from the wrong component, miss audio resources, fail because of signal routing, or require Workbench/runtime audio validation.

This reference owns audio editor, audio signal, sound event/component, and sound-system workflows. It does not own network authority/replication, generic component lifecycle, generic prefab/resource modeling, vehicle creation/simulation, weapon prefab behavior, or animation authoring.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: Audio Editor, Audio Editor tutorials, audio nodes, DSP nodes, Signal Editor, Signal Editor nodes, audio variables, directivity, audio technical fundamentals, sound events, sound components, signals, music manager, occlusion, radio broadcast manager, sound manager module, Voice over Network audio, building/door audio, collision audio, multiphase destruction audio, tree destruction audio, vehicle damage audio, character sound-info signals.
- Secondary/cross-reference topics: networking, entity/component lifecycle, prefabs/resources, vehicles, weapons, animation, diagnostics, scripting, audio category pages.

Wiki pages reviewed:
- Audio Editor - https://community.bistudio.com/wiki/Arma_Reforger:Audio_Editor - status: covered - reason: owns audio editor interface, workflow surfaces, tables, procedures, warnings, and media.
- Audio Editor: Getting Started Tutorial - https://community.bistudio.com/wiki/Arma_Reforger:Audio_Editor:_Getting_Started_Tutorial - status: covered - reason: owns first-use Audio Editor workflow and tutorial warnings.
- Audio Editor: Nodes - https://community.bistudio.com/wiki/Arma_Reforger:Audio_Editor:_Nodes - status: covered - reason: owns the main Audio Editor node family reference.
- Audio Editor: DSP Nodes - https://community.bistudio.com/wiki/Arma_Reforger:Audio_Editor:_DSP_Nodes - status: covered - reason: owns DSP node families, node tables, and DSP warnings.
- Audio Editor: Signal Editor - https://community.bistudio.com/wiki/Arma_Reforger:Audio_Editor:_Signal_Editor - status: covered - reason: owns Signal Editor surface and warnings.
- Audio Editor: Signal Editor: Nodes - https://community.bistudio.com/wiki/Arma_Reforger:Audio_Editor:_Signal_Editor:_Nodes - status: covered - reason: owns signal node families, code/config examples, and signal editor node tables.
- Audio Editor: Audio Variables - https://community.bistudio.com/wiki/Arma_Reforger:Audio_Editor:_Audio_Variables - status: covered - reason: owns audio variable workflows, links, warnings, and media.
- Audio Editor: Directivity - https://community.bistudio.com/wiki/Arma_Reforger:Audio_Editor:_Directivity - status: covered - reason: owns directivity behavior and media-backed editor concept.
- Audio: Technical Fundamentals - https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Technical_Fundamentals - status: covered - reason: owns audio-system fundamentals and warnings.
- Audio: Sound Events - https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Sound_Events - status: covered - reason: owns sound event tables, warnings, and event routing.
- Audio: Sound Components - https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Sound_Components - status: covered - reason: owns sound component setup, procedures, and component warnings.
- Audio: Signals - https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Signals - status: covered - reason: owns signal tables and signal routing concepts.
- Audio: Music Manager - https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Music_Manager - status: covered - reason: owns music manager tables and warnings.
- Audio: Occlusion - https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Occlusion - status: covered - reason: owns occlusion workflow, tables, procedures, and media.
- Audio: Radio Broadcast Manager - https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Radio_Broadcast_Manager - status: covered - reason: owns radio broadcast workflow, tables, procedures, warnings, and network-adjacent audio routing.
- Audio: SCR_SoundManagerModule - https://community.bistudio.com/wiki/Arma_Reforger:Audio:_SCR_SoundManagerModule - status: covered - reason: owns sound manager module setup, procedures, warnings, media, and links.
- Audio: Voice over Network - https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Voice_over_Network - status: covered - reason: owns audio-side VoN requirements; network authority semantics remain with `multiplayer-replication-and-authority.md`.
- Audio: Building Doors - https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Building_Doors - status: covered - reason: owns building door sound workflow and procedures.
- Audio: Collision - https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Collision - status: covered - reason: owns collision audio tables and workflow.
- Audio: Multiphase Destruction - https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Multiphase_Destruction - status: covered - reason: owns destruction audio tables, procedures, warnings, and code/config shape evidence.
- Audio: Tree Destruction - https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Tree_Destruction - status: covered - reason: owns tree destruction audio tables, procedure, and warnings.
- Audio: Vehicle Damage - https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Vehicle_Damage - status: covered - reason: owns audio-side vehicle damage workflow; vehicle damage mechanics remain with the vehicle reference.
- Character SoundInfo Signals Reference - https://community.bistudio.com/wiki/Arma_Reforger:Character_SoundInfo_Signals_Reference - status: covered - reason: owns character sound-info signal reference table.
- Modding/Audio category pages - https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Audio - status: covered - reason: source inventory and routing evidence only.
- Modding/Audio/Guidelines category pages - https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Audio/Guidelines - status: covered - reason: source inventory and routing evidence only.

Wiki sections covered:
- Audio Editor: editor panels, workflow surfaces, tables, media-backed interface evidence, procedures, warnings, and links.
- Getting Started Tutorial: first Audio Editor workflow, sample/tutorial setup expectations, and common warnings.
- Audio Editor Nodes: audio node families and editor node tables.
- DSP Nodes: DSP node families, DSP tables, and processing warnings.
- Signal Editor: signal editor surface and signal-routing warning.
- Signal Editor Nodes: signal node families, signal-node tables, signal node procedure, warnings, and code/config shape examples.
- Audio Variables: audio variable concepts, usage routes, warnings, and media.
- Directivity: directional sound concept and editor visualization.
- Technical Fundamentals: base concepts, system-level warnings, and terminology.
- Sound Events: sound event tables, event routing, and sound-event warnings.
- Sound Components: component setup, procedures, links to component examples, and component failure modes.
- Signals: signal families and signal reference tables.
- Music Manager: music manager tables, routing, and warnings.
- Occlusion: occlusion tables, procedures, media evidence, and validation route.
- Radio Broadcast Manager: broadcast setup, procedures, tables, warnings, and related audio/network routing.
- Sound Manager Module: `SCR_SoundManagerModule` setup, procedures, warnings, media evidence, and script/API routing.
- Voice over Network: audio-side VoN component requirements, radio/direct voice concepts, stream/sound-event/signal needs, and runtime verification.
- Building Doors, Collision, Multiphase Destruction, Tree Destruction, Vehicle Damage: domain audio setup workflows, tables, procedures, warnings, and validation notes.
- Character SoundInfo Signals Reference: character sound-info signal table.

Structured wiki records:
- Tables reviewed/included: 10 Audio Editor tables, 19 DSP-node tables, 52 Audio Editor node tables, 26 Signal Editor node tables, 2 collision tables, 2 multiphase destruction tables, 4 music manager tables, 2 occlusion tables, 2 radio broadcast manager tables, 33 audio signal tables, 2 sound component tables, 14 sound event tables, 2 tree destruction tables, 4 Voice over Network tables, and 1 character sound-info signal table.
- Procedures reviewed/included: Audio Editor, DSP nodes, getting started, Signal Editor nodes, building doors, multiphase destruction, occlusion, radio broadcast manager, sound manager module, and sound components procedures.
- Admonitions reviewed/included: Audio Editor, audio variables, DSP nodes, getting started, nodes, Signal Editor, signal nodes, multiphase destruction, music manager, radio broadcast manager, sound manager module, signals, sound components, sound events, technical fundamentals, tree destruction, and Voice over Network warnings.
- Code blocks reviewed/included: Signal Editor node examples and multiphase destruction code/config shape evidence were reviewed; exact source bodies are not copied.
- Media reviewed: Audio Editor, audio variables, directivity, occlusion, sound manager, technical fundamentals, and VoN media were reviewed as editor/workflow evidence; runtime use does not depend on images.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts/query-reforger-data.py lookup "play a sound event" --limit 8`
  - `py -3 scripts/query-reforger-data.py examples audio --limit 8`
  - `py -3 scripts/query-reforger-data.py files Sound --limit 8`
  - `py -3 scripts/query-reforger-data.py files SoundComponent --limit 8`
  - `py -3 scripts/query-reforger-data.py files SoundEvent --limit 8`
  - `py -3 scripts/query-reforger-data.py files SCR_SoundManagerModule --limit 8`
  - `py -3 scripts/query-reforger-data.py files AudioSystem --limit 8`
- Symbols/methods/attributes verified as lookup keys: `AudioSystem`, `SoundComponent`, `SoundComponentClass`, `SimpleSoundComponent`, `SimpleSoundComponentClass`, `SndComponent`, `AmbientSoundsComponent`, `CharacterSoundComponent`, `CommunicationSoundComponent`, `VehicleSoundComponent`, `SCR_BellSoundComponent`, `SCR_BuildingSoundComponent`, `SCR_TriggerSoundComponent`, `SCR_CommunicationSoundComponent`, `SCR_SoundManagerModule`, `SCR_SoundEvent`, `SCR_VoiceoverData`, `SCR_VoiceoverSystem`, `SoundInfo`, and `SoundEventName`.
- Examples/snippets reviewed: voiceover data/system routes, bell/building/trigger/communication sound components, sound event helper, sound manager module, HQ radio sound entity, ambient looped positional sounds, sound cinematic track, and generated audio component/API files.

Samples and source examples:
- Official sample folders reviewed as layout signals: `SampleMod_NewWeapon`, `SampleMod_ModdedWeapon`, `SampleMod_NewCar`, `SampleMod_ModdedCar`, and `SampleMod_Main` where audio folders/resources are present.
- Raw game-source example families reviewed through query output: sound components, sound events, voiceover, sound manager, communication/radio audio, ambient sound loops, cinematic sound tracks, and generated sound/audio APIs.

Coverage gaps:
- No owned primary audio wiki page was skipped.
- Network authority/replication is intentionally routed to `multiplayer-replication-and-authority.md`; this reference preserves audio-side VoN and radio requirements only.
- Generic component lifecycle is routed to `entities-components-and-lifecycle.md`; this reference preserves sound component setup and sound-specific component examples.
- Generic prefab/resource modeling is routed to `prefabs-configs-containers-and-catalogs.md`; this reference preserves audio resource/sound-event/component routing only.
- Vehicle creation/simulation is routed to `vehicles-creation-simulation-and-compartments.md`; this reference preserves vehicle damage/audio workflow only.
- Weapon prefab behavior is routed to `weapons-prefabs-attachments-and-firearms.md`; this reference preserves weapon-related audio references only where audio behavior is primary.
- Animation authoring is routed to `animation-graphs-weapon-animation-and-export.md`; this reference preserves audio timing/sound event concerns only.
- Exact source bodies and API signatures are not embedded; use query commands before writing API-sensitive code.

## Wiki Source Coverage

Audio work in Reforger crosses editor graphs, signal routing, sound events, sound components, and runtime resources. Codex should treat it as a data-and-Workbench workflow first, then verify exact script APIs through the query tool.

Use this source order for audio tasks:

1. identify whether the task is editor/node authoring, sound event setup, component setup, signal routing, music, occlusion, radio/VoN, or domain audio;
2. use the Audio Editor and Signal Editor pages for editor surfaces and node families;
3. use Sound Events and Sound Components for runtime playback routes;
4. use Signals, Audio Variables, and Character SoundInfo Signals for parameter/control data;
5. use domain pages for building doors, collision, destruction, tree, vehicle damage, music, occlusion, radio, sound manager, or VoN behavior;
6. use game-data queries for exact classes, inheritance, examples, and snippets.

Audio Editor coverage:

- Audio Editor is the primary Workbench surface for authoring audio graphs and sound behavior.
- The editor pages include tables and media that define panels and workflow surfaces; preserve them as editor navigation and validation context.
- Getting Started Tutorial is the first-use route; it includes workflow order and warnings that prevent shallow "create a sound" answers.
- Audio Editor Nodes defines the main node families used by the audio graph.
- DSP Nodes define signal/audio processing families. Treat them as audio processing nodes, not generic script utilities.
- Directivity defines directional sound behavior and should be used when the sound source has facing or spatial behavior.
- Audio Variables define variable data that audio graphs and systems can consume; do not replace them with script constants without checking the workflow.

Signal Editor coverage:

- Signal Editor owns signal editing surfaces.
- Signal Editor Nodes owns signal node families and examples. It is separate from Audio Editor Nodes because signal logic drives values that audio systems consume.
- Signal node examples were reviewed as shape evidence; do not copy them blindly into runtime code.
- Signals page owns broader audio signal tables; use it when the task names a signal or asks how sound behavior follows game state.
- Character SoundInfo Signals Reference owns character sound-info signal mappings and should be checked for character/weapon/body sound signal tasks.

Sound Event and Sound Component coverage:

- Sound Events define sound-event data and event routing; use this page when a task asks for "play a sound", event names, event setup, or sound-event assets.
- Sound Components define component-based playback setup; use this page when sound behavior belongs on an entity/component.
- Sound components are not generic component lifecycle docs. Use the entity/component reference only for lifecycle and event-mask concerns.
- Game-data search shows `SoundComponent` inherits through generated classes, while handwritten `SCR_BellSoundComponent`, `SCR_BuildingSoundComponent`, `SCR_TriggerSoundComponent`, and communication sound components are better implementation examples.

Technical fundamentals coverage:

- Technical Fundamentals is the conceptual anchor for system behavior and correctness warnings.
- Use it when a task asks why an audio system works a certain way, how signals/events/components relate, or why runtime validation is needed.

Music, occlusion, radio, and sound manager coverage:

- Music Manager owns music-system tables and warnings.
- Occlusion owns obstruction/occlusion setup and validation workflow.
- Radio Broadcast Manager owns radio broadcast audio setup and warnings; it is audio-owned but can cross networking and entity/component concerns.
- `SCR_SoundManagerModule` wiki page owns module setup and routing; exact API usage still requires query output.

Voice over Network coverage:

- Voice over Network is covered here only for audio-side setup: voice components, direct/radio voice audio, stream node/sound-event/signal expectations, and audio validation.
- Networking authority, replication, owner/proxy behavior, server runtime, and dedicated-server rules are owned by networking/server references.
- VoN audio must be validated in runtime with the intended voice/radio setup; source lookup does not prove audio resources or network behavior.

Domain audio coverage:

- Building Doors owns door sound setup and procedures.
- Collision owns collision audio tables and setup.
- Multiphase Destruction owns destruction audio setup, tables, warnings, and code/config shape evidence.
- Tree Destruction owns tree destruction audio setup and warning.
- Vehicle Damage owns audio-side vehicle damage behavior; vehicle damage mechanics remain vehicle-owned.

## Terms And Concepts

- Audio Editor: Workbench tool surface for audio graph/resource authoring.
- Signal Editor: Workbench tool surface for signal logic that drives audio behavior.
- Audio node: Audio Editor node used in sound graph behavior.
- DSP node: audio processing node family.
- Signal node: node in Signal Editor used to generate, transform, or route signal values.
- Audio variable: data value used by the audio graph/system.
- Directivity: direction-dependent sound behavior.
- Sound event: named audio event/resource route that can be played by systems/components.
- Sound event name: lookup key or configured name for event playback.
- Sound component: entity/component route for sound playback.
- Simple sound component: base component route under sound component inheritance.
- Sound manager module: system/module route for centralized sound behavior.
- Audio system: lower-level system route for audio behavior; query exact APIs before use.
- Signal: game/audio data channel that changes sound behavior.
- Music manager: system for music behavior and state.
- Occlusion: audio behavior affected by obstruction/space.
- Radio broadcast manager: audio route for radio broadcast behavior.
- Voice over Network: audio and network voice setup; this reference owns audio setup only.
- SoundInfo: config/data route for sound information.
- Character SoundInfo signals: character-focused signal mapping reference.

## Workbench / Resource / Data Surfaces

Audio authoring surfaces:

- Audio Editor panels and node graph.
- Audio Editor node tables.
- DSP node tables.
- Signal Editor and signal node tables.
- Audio Variables page and variable references.
- Directivity setup/visualization.
- Sound Events data.
- Sound Components and entity component properties.
- Signals and character sound-info signal tables.

Runtime/system surfaces:

- `SCR_SoundManagerModule` setup.
- `AudioSystem` route.
- Sound component inheritance and handwritten component examples.
- Music manager data.
- Occlusion setup.
- Radio broadcast manager setup.
- Voice over Network audio setup.
- Domain audio data for doors, collision, destruction, tree destruction, and vehicle damage.

Resource validation surfaces:

- Audio banks/events/resources in Workbench.
- Sound event names and resource availability.
- Component placement and prefab/entity configuration.
- Signal names/values and runtime signal changes.
- Runtime audio playback, position, directivity, occlusion, and voice/radio checks.

## Required Workflows

Create or edit an Audio Editor graph:

1. Identify whether the task needs an audio node, DSP node, signal node, sound event, or component route.
2. Open the relevant Audio Editor resource.
3. Inspect editor panels and current node graph.
4. Use the Audio Editor Nodes reference for graph nodes.
5. Use DSP Nodes for processing behavior.
6. Use Signal Editor and signal node references for value/control logic.
7. Validate node warnings and editor errors before changing scripts.
8. Test sound behavior in Workbench and runtime.

Create a sound event route:

1. Identify the intended sound event and resource.
2. Check Sound Events wiki detail for event setup and tables.
3. Check whether the sound should be triggered by `SoundComponent`, `SCR_SoundManagerModule`, `AudioSystem`, a helper class, or a domain system.
4. Run exact query commands for sound event/component routes.
5. Configure component/resource data.
6. Validate that the event name, audio bank/resource, and playback location are correct.

Use a sound component:

1. Decide whether playback belongs on an entity/component.
2. Review Sound Components workflow and warnings.
3. Query exact `SoundComponent`/`SimpleSoundComponent`/derived examples.
4. Configure component properties and resource/event names.
5. Verify lifecycle, placement, transform/position, and runtime playback.

Use audio signals:

1. Identify the signal family from Audio Signals or Character SoundInfo Signals.
2. Use Signal Editor for signal graph/value routing.
3. Use Signal Editor Nodes for node behavior.
4. Connect signal output to audio behavior.
5. Validate signal values at runtime.

Set up Music Manager, occlusion, or radio:

1. Use the topic-specific wiki page as source authority.
2. Preserve its tables and procedures while configuring.
3. Query source routes only when scripting or component/API details are needed.
4. Validate in the intended runtime context, especially where radio/VoN crosses networking.

Set up domain audio:

1. For building doors, collision, destruction, tree destruction, or vehicle damage, start from the domain audio wiki page.
2. Keep the audio workflow here, but route non-audio mechanics to the owning domain reference.
3. Configure sound events/components/signals/resources.
4. Test the in-game domain event that should trigger sound.

## Configuration Fields And Tables

Audio Editor and node tables:

- Audio Editor panel/interface tables define where audio authoring happens.
- Audio Editor node tables define available audio node families and properties.
- DSP node tables define processing behavior and should be consulted before writing custom script logic.
- Getting Started Tutorial procedure/warnings define the first working setup path.

Signal tables:

- Signal Editor node tables define signal graph node families.
- Audio Signals includes broad signal data for audio behavior.
- Character SoundInfo Signals Reference maps character sound-info signal data.
- Signal node examples are shape evidence, not source bodies to copy.

Sound event/component tables:

- Sound Events tables define event fields and routes.
- Sound Components tables define component setup and field meanings.
- Component routes require both data configuration and exact API lookup when code is involved.

Music/occlusion/radio/VoN tables:

- Music Manager tables define music behavior configuration.
- Occlusion tables define occlusion setup and validation points.
- Radio Broadcast Manager tables define broadcast setup.
- Voice over Network tables define audio-side VoN setup, component/resource requirements, and verification concerns.

Domain audio tables:

- Collision tables define collision-audio behavior.
- Multiphase Destruction tables define destruction-audio routing.
- Tree Destruction tables define tree destruction audio behavior.
- Vehicle Damage page owns audio-side vehicle damage configuration; vehicle damage mechanics remain cross-linked.

Module/system fields:

- `SCR_SoundManagerModule` page provides module setup and warnings.
- `AudioSystem` is exact API/source truth only through query output.
- `SoundComponent` generated records are exact class truth; handwritten `SCR_*SoundComponent` files are examples.

## Procedures And Ordered Steps

Audio Editor procedure:

1. Open the audio resource in Audio Editor.
2. Inspect editor panels and existing node graph.
3. Choose Audio Editor node families for graph behavior.
4. Choose DSP node families for processing.
5. Use Signal Editor for signal-driven behavior.
6. Check warnings and editor validation.
7. Test sound playback in Workbench.
8. Test in runtime with the actual entity/component/resource setup.

Sound event procedure:

1. Define the sound event and intended trigger.
2. Verify the sound event/resource exists in Workbench.
3. Decide whether playback belongs to a component, sound manager, audio system, helper, or domain system.
4. Configure event/resource data.
5. Query exact API routes before scripting.
6. Validate playback, position, attenuation/directivity, and missing-resource behavior.

Sound component procedure:

1. Add or identify the sound component route.
2. Configure sound event/resource data.
3. Verify component placement and transform context.
4. Verify lifecycle and trigger conditions through the owning system.
5. Test in runtime.

Signal procedure:

1. Identify the signal.
2. Configure signal editor nodes.
3. Connect the signal to the audio graph/system.
4. Validate signal value changes in runtime.
5. Adjust audio graph behavior only after signal routing is confirmed.

Radio/VoN procedure:

1. Use the audio wiki page for required audio-side setup.
2. Configure components/resources/sound events/signals for voice or radio.
3. Use networking/server references for replication, authority, or dedicated-server behavior.
4. Test with the intended player/radio/runtime context.

Domain audio procedure:

1. Start from the page for the domain event: door, collision, destruction, tree, or vehicle damage.
2. Configure event/component/signal resources from that page.
3. Route non-audio mechanics to the owning reference.
4. Trigger the actual domain event in runtime and verify sound behavior.

## Warnings And Failure Modes

- Do not guess audio APIs. Query exact sound component, event, module, and system classes before writing code.
- `files Sound` is broad and noisy. Prefer `lookup "play a sound event"`, `examples audio`, `files SoundComponent`, `files SoundEvent`, `files SCR_SoundManagerModule`, and `files AudioSystem`.
- Source lookup does not prove sound event names, audio banks, resources, or Workbench configuration are valid.
- Generated files are strongest for exact class truth; handwritten `SCR_*SoundComponent`, voiceover, sound manager, and helper files are stronger examples.
- Audio Editor node tasks should use node references first, not script guesses.
- DSP node behavior belongs to audio processing. Do not replace it with script code unless the task requires script integration.
- Signal routing errors can look like sound-event failures. Validate signals before changing sound events.
- Sound components require entity/component placement and runtime trigger validation.
- Sound events require event/resource availability and correct playback route.
- Directivity, occlusion, attenuation, and transform/position issues can make a valid event sound wrong or inaudible.
- Music, radio broadcast, and VoN behavior need runtime validation in the intended context.
- VoN crosses audio, networking, server, and radio/item setup. This reference owns audio setup only.
- Vehicle damage, weapon audio, building door audio, collision, and destruction pages own audio behavior, not the full domain mechanics.
- Do not copy audio sample or source bodies into references or answers; use bounded snippets after targeted query results.

## API Lookup Keys

Use these lookup keys before writing audio-sensitive code:

- Core audio/system: `AudioSystem`, `SCR_SoundManagerModule`, `SndBaseModule`.
- Sound component classes: `SoundComponent`, `SoundComponentClass`, `SimpleSoundComponent`, `SimpleSoundComponentClass`, `SndComponent`, `SndComponentClass`.
- Generated/derived sound components: `AmbientSoundsComponent`, `CharacterSoundComponent`, `CommunicationSoundComponent`, `VehicleSoundComponent`.
- Handwritten sound components: `SCR_BellSoundComponent`, `SCR_BellSoundComponentClass`, `SCR_BuildingSoundComponent`, `SCR_BuildingSoundComponentClass`, `SCR_CampaignSoundComponent`, `SCR_TriggerSoundComponent`, `SCR_CommunicationSoundComponent`.
- Sound event/helper routes: `SCR_SoundEvent`, `SoundEventName`, `SoundInfo`.
- Voiceover/radio routes: `SCR_VoiceoverData`, `SCR_VoiceoverLine`, `SCR_VoiceoverSequence`, `SCR_VoiceoverSystem`, `SCR_HQRadioSoundEntity`.
- Ambient/cinematic routes: `SCR_AudioHandleLoop`, `SCR_LoopedPositionalSounds`, `SCR_SoundCinematicTrack`.
- Cross-domain terms: `Ak`, `Sound`, `SoundEvent`, `Voice`, `Voiceover`, `RadioProtocol`, `Music`.

## Game-Data Query Commands

Run these before writing API-sensitive audio code:

```powershell
py -3 scripts/query-reforger-data.py lookup "play a sound event" --limit 8
py -3 scripts/query-reforger-data.py examples audio --limit 8
py -3 scripts/query-reforger-data.py files Sound --limit 8
py -3 scripts/query-reforger-data.py files SoundComponent --limit 8
py -3 scripts/query-reforger-data.py files SoundEvent --limit 8
py -3 scripts/query-reforger-data.py files SCR_SoundManagerModule --limit 8
py -3 scripts/query-reforger-data.py files AudioSystem --limit 8
```

Use exact symbols after selecting a route:

```powershell
py -3 scripts/query-reforger-data.py symbol SoundComponent --kind class --exact
py -3 scripts/query-reforger-data.py symbol SimpleSoundComponent --kind class --exact
py -3 scripts/query-reforger-data.py symbol AudioSystem --kind class --exact
py -3 scripts/query-reforger-data.py files SCR_BellSoundComponent --limit 8
py -3 scripts/query-reforger-data.py files SCR_TriggerSoundComponent --limit 8
```

Use snippets only after a targeted result identifies the useful file:

```powershell
py -3 scripts/query-reforger-data.py snippet scripts/Game/Components/SCR_BellSoundComponent.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/Game/Components/SCR_TriggerSoundComponent.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/Game/Components/SCR_BuildingSoundComponent.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/Game/Components/SCR_CommunicationSoundComponent.c --line 1 --context 30
py -3 scripts/query-reforger-data.py snippet scripts/Game/Systems/Sound/SCR_SoundManagerModule.c --line 1 --context 30
```

Preferred Codex flow:

1. Read this reference for audio workflow and ownership boundaries.
2. Use `lookup "play a sound event"` for a bounded task bundle.
3. Use targeted `files` or `examples` commands for the sound/event/component family.
4. Inspect bounded snippets only for selected handwritten examples.
5. Verify sound event resources, component setup, signal routing, and runtime playback in Workbench/runtime.

## Examples And Samples

Official samples:

- `SampleMod_NewWeapon`: audio folder/resource layout signal for weapon-adjacent audio only.
- `SampleMod_ModdedWeapon`: audio layout signal for modifying weapon audio integration.
- `SampleMod_NewCar`: audio layout signal for vehicle-adjacent audio only.
- `SampleMod_ModdedCar`: audio, vehicle sound, particle/effect-adjacent layout signal for modified vehicle workflows.
- `SampleMod_Main`: broad sample layout signal where audio resources are present.

Game-source example routes from query output:

- `scripts/Game/Voiceover/SCR_VoiceoverData.c`: voiceover data route.
- `scripts/Game/Systems/SCR_VoiceoverSystem.c`: voiceover system route.
- `scripts/Game/Components/SCR_BellSoundComponent.c`: sound component example.
- `scripts/Game/Components/SCR_TriggerSoundComponent.c`: trigger sound component example.
- `scripts/Game/Components/SCR_BuildingSoundComponent.c`: building sound component example.
- `scripts/Game/Components/SCR_CommunicationSoundComponent.c`: communication/radio-related sound component example.
- `scripts/Game/Helpers/SCR_SoundEvent.c`: sound event helper route.
- `scripts/Game/Systems/Sound/SCR_SoundManagerModule.c`: sound manager module route.
- `scripts/Game/Campaign/SCR_HQRadioSoundEntity.c`: radio sound entity route.
- `scripts/Game/Components/AmbientSoundsComponent/SCR_LoopedPositionalSounds.c`: ambient looped positional sound route.
- `scripts/Game/Cinematics/SCR_SoundCinematicTrack.c`: cinematic sound track route.

Example selection rules:

- Prefer wiki workflows for Audio Editor, Signal Editor, nodes, signals, sound events/components, and domain audio procedures.
- Prefer official samples for project/resource layout.
- Prefer generated files for exact class and inheritance truth.
- Prefer handwritten `SCR_*` files for implementation examples.
- Do not copy source bodies; use bounded snippets when implementation context is needed.

## Follow-Up Keywords

Use these keywords for searches and task routing:

- `Audio Editor`
- `Audio Editor Nodes`
- `DSP Nodes`
- `Signal Editor`
- `Signal Editor Nodes`
- `Audio Variables`
- `Directivity`
- `Technical Fundamentals`
- `Sound Events`
- `Sound Components`
- `Audio Signals`
- `Character SoundInfo Signals`
- `Music Manager`
- `Occlusion`
- `Radio Broadcast Manager`
- `SCR_SoundManagerModule`
- `Voice over Network`
- `SoundComponent`
- `SimpleSoundComponent`
- `AudioSystem`
- `SCR_SoundEvent`
- `SoundEventName`
- `SoundInfo`
- `SCR_BellSoundComponent`
- `SCR_BuildingSoundComponent`
- `SCR_TriggerSoundComponent`
- `SCR_CommunicationSoundComponent`
- `SCR_VoiceoverData`
- `SCR_VoiceoverSystem`
- `building doors audio`
- `collision audio`
- `multiphase destruction audio`
- `tree destruction audio`
- `vehicle damage audio`
- `SampleMod_NewWeapon`
- `SampleMod_ModdedWeapon`
- `SampleMod_NewCar`
- `SampleMod_ModdedCar`

## Verification

Audio Editor validation:

- Confirm the intended audio resource opens and node graph is valid.
- Confirm node family and DSP node behavior against the wiki tables.
- Confirm Signal Editor graph and signal node values.
- Confirm editor warnings/errors before changing code.
- Confirm directivity, occlusion, position, and transform-dependent behavior in editor/runtime.

Sound event/component validation:

- Confirm sound event names and audio resources exist in Workbench.
- Confirm sound components are on the intended entity/prefab route.
- Confirm sound component lifecycle/trigger behavior in runtime.
- Confirm `SCR_SoundManagerModule` or `AudioSystem` routes only after exact query lookup.
- Confirm generated class truth and handwritten example patterns separately.

Domain validation:

- Trigger building door, collision, destruction, tree destruction, or vehicle damage events in runtime.
- Confirm audio-side data is correct before changing non-audio domain mechanics.
- Route vehicle, weapon, animation, or entity lifecycle defects to the owning reference.

VoN/radio validation:

- Confirm audio-side VoN components/resources/sound events/signals.
- Confirm radio broadcast manager setup.
- Use networking/server references for authority, replication, dedicated-server, or multiplayer behavior.
- Test with the intended runtime voice/radio context.

Script/API validation:

- Run exact game-data queries before writing audio API code.
- Use snippets only after selecting a targeted file.
- Explain any remaining Workbench/runtime uncertainty because query output does not validate audio bank/resource availability.

## Official Wiki Links

- Audio Editor: https://community.bistudio.com/wiki/Arma_Reforger:Audio_Editor
- Audio Editor: Getting Started Tutorial: https://community.bistudio.com/wiki/Arma_Reforger:Audio_Editor:_Getting_Started_Tutorial
- Audio Editor: Nodes: https://community.bistudio.com/wiki/Arma_Reforger:Audio_Editor:_Nodes
- Audio Editor: DSP Nodes: https://community.bistudio.com/wiki/Arma_Reforger:Audio_Editor:_DSP_Nodes
- Audio Editor: Signal Editor: https://community.bistudio.com/wiki/Arma_Reforger:Audio_Editor:_Signal_Editor
- Audio Editor: Signal Editor: Nodes: https://community.bistudio.com/wiki/Arma_Reforger:Audio_Editor:_Signal_Editor:_Nodes
- Audio Editor: Audio Variables: https://community.bistudio.com/wiki/Arma_Reforger:Audio_Editor:_Audio_Variables
- Audio Editor: Directivity: https://community.bistudio.com/wiki/Arma_Reforger:Audio_Editor:_Directivity
- Audio: Technical Fundamentals: https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Technical_Fundamentals
- Audio: Sound Events: https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Sound_Events
- Audio: Sound Components: https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Sound_Components
- Audio: Signals: https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Signals
- Audio: Music Manager: https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Music_Manager
- Audio: Occlusion: https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Occlusion
- Audio: Radio Broadcast Manager: https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Radio_Broadcast_Manager
- Audio: SCR_SoundManagerModule: https://community.bistudio.com/wiki/Arma_Reforger:Audio:_SCR_SoundManagerModule
- Audio: Voice over Network: https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Voice_over_Network
- Audio: Building Doors: https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Building_Doors
- Audio: Collision: https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Collision
- Audio: Multiphase Destruction: https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Multiphase_Destruction
- Audio: Tree Destruction: https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Tree_Destruction
- Audio: Vehicle Damage: https://community.bistudio.com/wiki/Arma_Reforger:Audio:_Vehicle_Damage
- Character SoundInfo Signals Reference: https://community.bistudio.com/wiki/Arma_Reforger:Character_SoundInfo_Signals_Reference
- Modding/Audio category: https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Audio
- Modding/Audio/Guidelines category: https://community.bistudio.com/wiki/Category:Arma_Reforger/Modding/Audio/Guidelines

## Usefulness Score

Score: `94/100`

- Wiki coverage: `29/30`
  - All owned primary audio pages are reviewed and represented.
  - Tables, procedures, warnings, code/config examples, media, and links were reviewed; dense node/signal tables are represented as node and field families instead of copied dumps.
  - Category pages are included as source inventory/routing evidence.
  - Missed coverage: screenshot-level editor visuals are not embedded; impact is low because editor surfaces and official URLs are present.
- Operational detail: `14/15`
  - Preserves Audio Editor, node, DSP, Signal Editor, sound event/component, signal, music, occlusion, radio, VoN, sound manager, and domain audio workflows.
  - Extremely large node/signal tables are compressed into families for use by Codex.
- API lookup usefulness: `15/15`
  - Exact lookup keys and commands are present for sound events, sound components, audio examples, sound manager, `AudioSystem`, and snippets.
- Example grounding: `9/10`
  - Official sample families and raw game-source routes are included.
  - No sample or source bodies are copied.
- Codex task usefulness: `15/15`
  - Supports common tasks: play a sound event, configure a sound component, use audio signals, work with Audio Editor nodes, set up occlusion/music/radio/VoN, and route domain audio.
- Context efficiency: `8/10`
  - Dense but navigable. The length is justified by the source-heavy audio family.
  - Split boundaries prevent duplicate ownership of networking, lifecycle, prefabs/resources, vehicles, weapons, and animation.
- Verification guidance: `4/5`
  - Workbench, editor, runtime, audio resource, signal, domain, VoN/radio, and API checks are present.
  - Dedicated-server/multiplayer validation is routed where it belongs.

Category-fit check:
- Source family complete: pass. Audio Editor, nodes, DSP, Signal Editor, variables, directivity, fundamentals, events, components, signals, music, occlusion, radio, sound manager, VoN, and domain audio pages are covered.
- No owned page missing: pass.
- Split boundary justified: pass. Networking, lifecycle, prefab/resource modeling, vehicles, weapons, animation, diagnostics, and server behavior are routed to owning references.
- Cross-links present: pass.
- Task route clear: pass. Sound-event tasks route to this reference plus `lookup "play a sound event"` and targeted audio queries.
- Automatic failure conditions: none found.
