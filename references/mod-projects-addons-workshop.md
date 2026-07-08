# Mod Projects, Addons, And Workshop

## When To Read

Read this when the task is about creating, opening, launching, packaging, publishing, updating, removing, or troubleshooting an Arma Reforger addon project.

Use this reference for:

- creating a new Workbench project/addon;
- adding the base Arma Reforger project or addon dependencies to Workbench Launcher;
- choosing a local project location;
- understanding `.gproj` ownership, dependency GUIDs, and sample project layout;
- opening a project with additional addons or presets;
- publishing, updating, or removing a Workshop mod;
- interpreting packaging/publishing failures;
- deciding whether a problem belongs to project setup, Workshop publishing, or a neighboring reference.

Do not use this as the primary source for:

- dedicated server startup/config fields: read `server-hosting-startup-and-runtime.md`;
- Resource Manager editor usage outside project dependencies: read `resource-manager-file-types-and-editors.md`;
- asset import, weapon, vehicle, animation, audio, UI, or terrain workflows after the project exists: read the narrow workflow owner;
- exact scripting APIs: use `scripts/query-reforger-data.py`.

## Source Inventory

Wiki ownership:
- Primary wiki topics/categories: project/addon setup, `.gproj` project registration, addon dependency visibility, Workshop publishing, Workshop user-facing behavior, packaging checks, development executable compatibility.
- Secondary/cross-reference topics: Directory Structure for layout orientation only; Game Identity for Bohemia account and Workshop publishing identity only; Startup Parameters only by route, not owned here.

Wiki pages reviewed:
- Mod Project Setup - https://community.bistudio.com/wiki/Arma_Reforger:Mod_Project_Setup - status: covered - reason: primary owner for Workbench Launcher setup, project creation, opening projects, dependencies, presets, and setup troubleshooting.
- Mod Publishing Process - https://community.bistudio.com/wiki/Arma_Reforger:Mod_Publishing_Process - status: covered - reason: primary owner for Publish Project UI, Workshop metadata fields, bundling behavior, update/remove flows, and publishing failures.
- Workshop - https://community.bistudio.com/wiki/Arma_Reforger:Workshop - status: covered - reason: primary owner for Workshop usage, in-game actions, version retention, storage/download behavior, and Workshop debug define.
- Development Executables - https://community.bistudio.com/wiki/Arma_Reforger:Development_Executables - status: partial - reason: included only for project/debug executable compatibility; Diag Menu details belong to `diagnostics-testing-and-performance.md`, server runtime belongs to `server-hosting-startup-and-runtime.md`.
- Directory Structure - https://community.bistudio.com/wiki/Arma_Reforger:Directory_Structure - status: partial - reason: included only for addon layout orientation; domain folders are owned by their narrow references.
- Game Identity - https://community.bistudio.com/wiki/Arma_Reforger:Game_Identity - status: partial - reason: included only for Bohemia account/Game Identity publishing implications; scripting identity lookup belongs to API/query output and runtime/server references.

Wiki sections covered:
- Mod Project Setup > Prerequisites - sectionId: `https-community-bistudio-com-wiki-arma-reforger-mod-project-setup-ccd3b8ccbf-1-p-244b69b70f` - coverage: full.
- Mod Project Setup > Workbench Launcher Setup - sectionId: `https-community-bistudio-com-wiki-arma-reforger-mod-project-setup-ccd3b8ccbf-2-w-912653a6b3` - coverage: full.
- Mod Project Setup > Workbench Launcher Setup > Preparing Data - sectionId: `https-community-bistudio-com-wiki-arma-reforger-mod-project-setup-ccd3b8ccbf-3-w-bb2f904e7a` - coverage: full.
- Mod Project Setup > Workbench Launcher Setup > Preparing Data > Adding Arma Reforger Project - sectionId: `https-community-bistudio-com-wiki-arma-reforger-mod-project-setup-ccd3b8ccbf-4-w-07d99db36f` - coverage: full.
- Mod Project Setup > Workbench Launcher Setup > Preparing Data > Adding Other Existing Projects - sectionId: `https-community-bistudio-com-wiki-arma-reforger-mod-project-setup-ccd3b8ccbf-5-w-59363a6b67` - coverage: full.
- Mod Project Setup > Project Creation - sectionId: `https-community-bistudio-com-wiki-arma-reforger-mod-project-setup-ccd3b8ccbf-6-p-b7f592100e` - coverage: full.
- Mod Project Setup > Managing Projects > Launching Project - sectionId: `https-community-bistudio-com-wiki-arma-reforger-mod-project-setup-ccd3b8ccbf-7-m-adad6ac9df` - coverage: full.
- Mod Project Setup > Managing Projects > Launching Project > With Mods - sectionId: `https-community-bistudio-com-wiki-arma-reforger-mod-project-setup-ccd3b8ccbf-8-m-677da24bd1` - coverage: full.
- Mod Project Setup > Managing Projects > Launching Project > With Mods > Presets - sectionId: `https-community-bistudio-com-wiki-arma-reforger-mod-project-setup-ccd3b8ccbf-9-m-ec596fe6a3` - coverage: full.
- Mod Project Setup > Managing Projects > Removing Projects - sectionId: `https-community-bistudio-com-wiki-arma-reforger-mod-project-setup-ccd3b8ccbf-10--a1c1681002` - coverage: full.
- Mod Project Setup > Managing Projects > Projects View - sectionId: `https-community-bistudio-com-wiki-arma-reforger-mod-project-setup-ccd3b8ccbf-11--24b29cc377` - coverage: full.
- Mod Project Setup > Experimental Branch - sectionId: `https-community-bistudio-com-wiki-arma-reforger-mod-project-setup-ccd3b8ccbf-12--a2a393a8c5` - coverage: full.
- Mod Project Setup > Troubleshooting - sectionIds: `https-community-bistudio-com-wiki-arma-reforger-mod-project-setup-ccd3b8ccbf-13--7e9f046b8f`, `https-community-bistudio-com-wiki-arma-reforger-mod-project-setup-ccd3b8ccbf-14--bdbb8140f5`, `https-community-bistudio-com-wiki-arma-reforger-mod-project-setup-ccd3b8ccbf-15--6adb8e8641`, `https-community-bistudio-com-wiki-arma-reforger-mod-project-setup-ccd3b8ccbf-16--2991486f82` - coverage: full.
- Mod Publishing Process > Publication, Interface, Publishing Process, Update, Removing mod, CLI Parameters, Troubleshooting - sectionIds: `https-community-bistudio-com-wiki-arma-reforger-mod-publishing-process-4ff4838a6-931c28b004`, `https-community-bistudio-com-wiki-arma-reforger-mod-publishing-process-4ff4838a6-c6e493459c`, `https-community-bistudio-com-wiki-arma-reforger-mod-publishing-process-4ff4838a6-23aad40aa2`, `https-community-bistudio-com-wiki-arma-reforger-mod-publishing-process-4ff4838a6-c6f0957032`, `https-community-bistudio-com-wiki-arma-reforger-mod-publishing-process-4ff4838a6-62d21b34c6`, `https-community-bistudio-com-wiki-arma-reforger-mod-publishing-process-4ff4838a6-d77fa95ee4`, `https-community-bistudio-com-wiki-arma-reforger-mod-publishing-process-4ff4838a6-21f21f53cb`, `https-community-bistudio-com-wiki-arma-reforger-mod-publishing-process-4ff4838a6-860186de17`, `https-community-bistudio-com-wiki-arma-reforger-mod-publishing-process-4ff4838a6-4b57f25456`, `https-community-bistudio-com-wiki-arma-reforger-mod-publishing-process-4ff4838a6-3a503abf33`, `https-community-bistudio-com-wiki-arma-reforger-mod-publishing-process-4ff4838a6-4ddd697b35`, `https-community-bistudio-com-wiki-arma-reforger-mod-publishing-process-4ff4838a6-7884be9f58`, `https-community-bistudio-com-wiki-arma-reforger-mod-publishing-process-4ff4838a6-80f260c782` - coverage: full.
- Workshop > Page, Usage, Interface, Actions, Development - sectionIds: `https-community-bistudio-com-wiki-arma-reforger-workshop-d7c785e7f5-1-page-a68e077fa5` through `https-community-bistudio-com-wiki-arma-reforger-workshop-d7c785e7f5-17-developme-0bcb09f1f4` - coverage: full.
- Development Executables > Page - sectionId: `https-community-bistudio-com-wiki-arma-reforger-development-executables-3d50e861-6e88a99d8e` - coverage: partial; project/debug executable compatibility only.
- Directory Structure > Page - sectionId: `https-community-bistudio-com-wiki-arma-reforger-directory-structure-606dfb6bf8-1-a3f24613c6` - coverage: partial; layout categories relevant to addon roots only.
- Game Identity > Definitions - sectionId: `https-community-bistudio-com-wiki-arma-reforger-game-identity-acab19c6e3-2-defin-a06fc97150` - coverage: partial; publishing identity only.

Structured wiki records:
- Tables reviewed/included: Mod Project Setup project type table; Mod Publishing Process field table; Workshop report-feedback table; Directory Structure table summarized only for layout route; Game Identity linking table summarized only for publishing identity implications.
- Procedures reviewed/included: adding base Arma Reforger project; scanning existing projects; creating a new project; opening/removing projects; opening with additional addons/presets; publishing/updating/removing Workshop items.
- Admonitions reviewed/included: OneDrive/write-permission warnings; missing dependency behavior; empty dependency remediation; read-only project causes; Workshop version retention; Workshop report misuse; packaged-source irreversibility; rights/license warning; owner-account warning; console storage/download limits; Diag executable compatibility.
- Code blocks reviewed/included: packaging error signatures, missing terrain-artifact warnings, Workshop processing failure, Workshop timeout, Workshop debug define command, default addon download directory.
- Media reviewed: Workbench launcher screens, Scan for Projects, Open project, Open with additional addons, publishing login/interface/category screenshots, Workshop tile states. Media is referenced by behavior only; images are not copied.

Game-data/API evidence:
- Queries run:
  - `py -3 scripts\query-reforger-data.py files gproj --limit 10`
  - `py -3 scripts\query-reforger-data.py files addon --limit 10`
  - `py -3 scripts\query-reforger-data.py files Workshop --limit 10`
- Symbols/methods/attributes verified: none required for normal project setup. Workshop/game identity API claims are intentionally not embedded; exact API lookups must be run before writing scripts.
- Examples/snippets reviewed: query output showed addon/Workshop UI and generated Workshop API records, useful as follow-up routes but not as authoring workflow authority.

Samples and source examples:
- Official sample folders reviewed: `SampleMod_Main`, `SampleMod_ModdedScript`, `SampleMod_WorkbenchPlugin`, `SampleMod_NewWeapon`, `SampleMod_ModdedWeapon`, `SampleMod_NewCar`, `SampleMod_ModdedCar`, `SampleMod_NewCharacter`, `SampleMod_NewFaction`, `SampleMod_NewProp`, `SampleMod_AnimationWorkshop`, `SampleMod_CinematicTutorial`, `SampleMod_Replacement`.
- Raw game-source example families reviewed: addon UI search results, Workshop file search results, Workbench dedicated server plugin route from query output.

Coverage gaps:
- Missing, excluded, or intentionally deferred source: server startup parameters, Resource Manager detailed options, File Types full extension table, Diag Menu details, individual domain sample workflows.
- Reason and impact: those are owned by narrower references. This file includes only the routing facts needed to set up, open, package, and publish a project without forcing Codex to read unrelated workflow owners.

## Wiki Source Coverage

This reference owns the project lifecycle around an addon:

1. Workbench must know where the base Arma Reforger data project is.
2. Dependencies must be visible to Workbench before a project can load reliably.
3. A new project is created from Workbench Launcher and stored in a writable non-cloud location.
4. Project dependencies are stored by addon/project identity, not by visible name alone.
5. The project can be launched alone, launched with extra addons, or launched with preset addon sets.
6. Publishing is done from Workbench after the project is bundled.
7. The packaged Workshop artifact is not the same thing as editable source.
8. Published mods are updated by opening the source project, changing data/metadata, bundling, and publishing a new version.
9. Removing a Workshop mod is permanent and should be treated as destructive.
10. Workshop user behavior affects testing: users can subscribe, download through server join, enable/disable, favorite, report, remove, and inspect downloads.

The wiki detail preserved here is operational. It includes setup order, field meanings, metadata limits, account/identity rules, dependency failure behavior, package behavior, console limits, and known error signatures.

## Terms And Concepts

- Addon/project: the editable mod project opened in Workbench. It has a project file ending in `.gproj`.
- Base Arma Reforger project: the official data project that Workbench needs before addon creation or editing. The wiki identifies this as `ArmaReforger.gproj`.
- Project list: Workbench Launcher's user-profile project registry. Removing a project from this list does not delete the project files.
- Dependency: another project/addon required by the current project. A missing dependency prevents reliable project loading. Dependencies are one-way.
- Additional addons: addons launched with the project for testing but not necessarily declared as project dependencies.
- Preset: a saved selection of additional addons in Workbench Launcher. The wiki states there are eight selectable presets shared by all addons listed in the launcher.
- `.gproj`: the project descriptor. Official samples show `GameProject` blocks with `ID`, `GUID`, `TITLE`, `Dependencies`, and platform `Configurations`.
- GUID: the identity used in dependency references and Workshop/source recovery workflows. A visible name is not enough for dependency troubleshooting.
- Source files: editable project data.
- Packaged files/package: bundled distribution output for Workshop. The wiki states packaged files are compressed, indexed, encrypted, and cannot be turned back into source.
- Working Dir: the temporary/output directory for bundled publish output. Do not set it to the editable addon directory.
- Contributor: a Bohemia account email invited to publish updates for a mod.
- Visibility: Workshop audience setting: Public, Private, Unlisted, or Test.
- Stable Workshop vs Experimental Workshop: separate backends. Experimental-published mods are not visible on stable and stable-published mods are not visible on experimental.
- Diag executable: a client/server/Workbench executable variant compatible with Workbench debugging tools.

## Workbench / Resource / Data Surfaces

Workbench Launcher surfaces:

- `Add Existing`: add a known project file, including the base Arma Reforger data project.
- `Scan for Projects`: scan a folder and add multiple existing addon projects, commonly dependencies.
- `Create New`: create a new addon project.
- Project tile/list item `Open`: open a project in Workbench.
- Project context menu `Open with Addons`: open a project with additional addons for testing.
- Project context menu `Remove from List`: remove the project entry from Workbench Launcher without deleting files.
- Cog menu: switch Workbench Launcher between list and grid project views.

Resource Manager / Workbench surfaces:

- `Workbench > Publish Project`: opens the publishing interface for bundling and Workshop upload.
- `Workbench > Link`: logs into the Bohemia backend and links the current Steam account to the Bohemia account used for publishing.
- `Workbench > Check Pending Invitation`: used by contributors to accept publishing invitations.
- `Workbench > Remove from Workshop`: removes a published Workshop mod.
- Resource Manager Options > Dependencies: later place to change dependencies for an already created project; detailed Resource Manager options belong to `resource-manager-file-types-and-editors.md`.

Project/data surfaces:

- Base data project: `ArmaReforger.gproj`, located under the installed game data addon path according to the wiki.
- Default new-project location: under the user's Documents/My Games Arma Reforger Workbench addons area according to the wiki. Do not hardcode a local user path in generated mod content.
- Downloaded Workshop mods on PC: under the user's Documents/My Games Arma Reforger addons area by default; can be changed with the `addonDownloadDir` startup parameter. Startup parameter details belong to `server-hosting-startup-and-runtime.md`.
- Console Workshop storage: the wiki states console storage for mods is limited and the download location cannot be changed.

Sample `.gproj` layout signals:

- `SampleMod_Main` has a project descriptor with `ID`, `GUID`, `TITLE`, many dependency GUIDs, and `PC`, `HEADLESS`, `XBOX_ONE`, `XBOX_SERIES`, and `PS4` configurations.
- `SampleMod_WorkbenchPlugin` shows a project depending on the base game GUID and platform configurations.
- `SampleMod_NewWeapon` shows a project descriptor with a `WidgetManagerSettings` block under the PC configuration for string table/localization runtime mapping.

Do not infer final `.gproj` schema from this reference alone. Use samples for layout signals and Workbench for authoritative project editing.

## Required Workflows

### Prepare Workbench Launcher For Addon Work

1. Confirm Arma Reforger and Workbench are installed.
2. Start Workbench through Steam Tools or by launching the Workbench executable.
3. Ensure the base Arma Reforger data project is known to Workbench Launcher.
4. Prefer manual addition when automatic detection fails or the installation moved.
5. Use `Add Existing` and select the base `ArmaReforger.gproj`.
6. Confirm the Arma Reforger project appears in Workbench Launcher's project list.

If the base project is missing, addon creation and opening can fail in confusing ways. Fix project registration before debugging scripts or resources.

### Add Existing Addons Or Dependencies

1. In Workbench Launcher, use `+ Add Project`.
2. Choose `Scan for Projects`.
3. Select the folder containing addons that should be available as dependencies.
4. Confirm the scan.
5. Open or use those projects as dependencies.

Dependency visibility is recursive in practice: dependencies of dependencies must also be visible to Workbench. If a dependency GUID in a `.gproj` cannot be found in the project list, Workbench may open only the base Arma Reforger data and skip the mod.

### Create A New Addon Project

1. Open Enfusion Workbench Launcher.
2. Confirm the base Arma Reforger project is visible.
3. Click `Create New`.
4. Choose the modded project flow rather than editing vanilla data.
5. Enter a project name using allowed characters only: letters, numbers, spaces, dash, underscore, and dot.
6. Pick a location that is writable by the current Windows user.
7. Avoid OneDrive, similar cloud-synced folders, and protected system folders.
8. Choose dependencies. Arma Reforger data is the default required dependency for a Reforger mod.
9. Click `OK`.
10. Expect Resource Manager to open for the created project.
11. If `addon.gproj` is renamed, re-add the renamed project file to Workbench Launcher next time.

### Open A Project

Open a known project by:

- double-clicking the project tile or list entry; or
- right-clicking the project and selecting `Open`.

If the project opens without the selected mod loaded, check dependency visibility before changing code.

### Open A Project With Extra Addons

Use `Open with Addons` when an addon should be present for a test session but should not necessarily become a project dependency.

1. Right-click the project in Workbench Launcher.
2. Select `Open with Addons`.
3. In the additional addons menu, select the addon set.
4. Use presets when switching between repeatable addon test sets.

Do not confuse additional launch addons with declared dependencies. Dependencies are required for project load; additional addons are launch-time test context.

### Remove A Project From Workbench Launcher

Use `Remove from List` from the project context menu. This removes the launcher entry only. It does not delete project data.

### Publish A Project To Workshop

1. Confirm the project is working before publishing.
2. Confirm the publishing account is correct. If the mod was previously published, the current account must be owner or accepted contributor.
3. Use `Workbench > Link` to log into the Bohemia backend when needed.
4. Use `Workbench > Publish Project`.
5. Fill in the publishing interface fields.
6. Confirm the project has been bundled.
7. Click `Publish`.
8. Wait for bundling to create packed data, metadata/manifest data, copied media, and a zip ready for upload.
9. Review the popup showing upload size.
10. Confirm upload.

Before publishing, verify rights and licensing for every uploaded asset. Treat Workshop Terms of Service and intellectual property checks as a release gate, not a post-publish cleanup task.

### Update An Existing Workshop Mod

1. Open the source project in Workbench.
2. Apply data or metadata changes.
3. Fill in `Change Notes`.
4. Publish again.

The wiki states that description, visibility, picture, and similar Workshop information changes still need bundling first, then publishing as a new version.

### Remove A Workshop Mod

Use `Workbench > Remove from Workshop` from Resource Manager.

Treat this as destructive. The wiki states removal is irreversible and permanent. If only local testing state is wrong, do not use Workshop removal.

### Recover Enough Identity To Remove A Lost-Source Workshop Mod

If source files are lost, the wiki describes two routes:

- download the mod in the game Workshop, open it in Workbench, then remove it; or
- create a minimal addon project with the known GUID from the web Workshop URL, add it as a project, open it, and remove it from Workshop.

This is only a removal path. It is not a source recovery path because packaged files cannot be extracted back into editable source.

## Configuration Fields And Tables

Project creation fields and constraints:

| Field/surface | Required behavior |
| --- | --- |
| Project name | Use only letters, numbers, spaces, dash, underscore, and dot. |
| Project location | Use a writable local folder. Avoid OneDrive/cloud sync and protected folders. |
| Dependencies | Include required projects/addons. Missing dependencies prevent correct load. Arma Reforger data is the default dependency for Reforger mods. |
| Project file | `addon.gproj` may be renamed, but the renamed file must be re-added to Workbench Launcher. |
| Project list profile | Workbench project list is stored in the user profile; different `-profile` values can maintain different project sets. |

Publishing interface fields:

| Field | Meaning and constraints |
| --- | --- |
| Project Name | Workshop display name. Maximum 30 characters. |
| Working Dir | Directory where the bundled project is stored. Do not use the editable addon directory. Default is under the user's Documents/My Games publishing area. |
| Preview Image | Workshop preview image. Maximum 2 MB. JPG or PNG. |
| Screenshots | Gallery images. Maximum 2 MB each. JPG or PNG. |
| Contributors | Bohemia account emails allowed to publish updates. Separate emails by comma, space, or newline. Original author controls contributor list and removal. Contributors must accept invitations from Workbench. |
| Category | One or more Workshop categories. At least one is required. |
| Tags | Space-separated search tags. |
| License | One of the official Arma public licenses or a custom license. A custom license requires `license.txt` in the addon root. |
| Version | Format is `major.minor.bugfix`. Increment for updates except workshop-information-only fixes. Version numbers can go up to 32000. |
| Visibility | Public, Private, Unlisted, or Test. Unlisted is hidden from search but can still be used on dedicated servers and downloaded. |
| Summary | Short Workshop preview text. Maximum 1024 characters. |
| Description | Full Workshop description. Maximum 5000 characters. |
| Change Notes | Update summary. Maximum 30000 characters. |

Publishing package behavior:

| Package behavior | Practical effect |
| --- | --- |
| Packed data is created | Distribution data is prepared from source. |
| Backend metadata is stored | Publishing-related manifest data is generated. |
| Pictures are copied | Preview images, screenshots, and mission previews are included. |
| Zip is prepared | Upload artifact is generated for Workshop. |
| Source files are ignored | `.meta`, `.txa`, and `.txo` are excluded; route to the File Types owner for the full extension list. |
| Compression is applied | Deflate compression is used, with `.anm`, `.data`, `.edds`, `.et`, `.nmn`, `.wav`, and `.xob` excluded from compression. |
| Encryption is applied | Packaged files are not editable source. |

Workshop user-facing actions:

| Action | Use |
| --- | --- |
| Download | Subscribe/download from tile center, Mod Details, or controller shortcut. Same action can cancel download. |
| Enable/Disable | Toggle whether a downloaded mod is active. |
| Like/Dislike | Vote from Mod Details. |
| Add to Favorites | Mark a Workshop item as favorite. |
| Remove | Delete the mod from the local machine. |
| Report | Report valid content/functionality problems. Do not report for dislike or wrong reasons. |
| View Downloads | Inspect past/current downloads. |
| Downloaded Tab | Manage downloaded mods similarly to other mods. |

Directory layout orientation:

- `Scripts` contains game and Workbench script files. Use scripting references and query tools before editing APIs.
- `Configs` contains configuration files, including Workbench utility config and domain config families.
- `Prefabs` contains configuration-like prefab data and roughly mirrors `Assets`, but not one-to-one.
- `Publishing` contains installation information.
- `UI`, `Sounds`, `Anims`, `Assets`, `Worlds`, `Terrains`, and `Missions` route to their narrow workflow references.

## Procedures And Ordered Steps

Project setup checklist:

1. Install Arma Reforger.
2. Install Workbench.
3. Launch the game once if relying on automatic registration, but do not trust automatic detection if the install moved.
4. In Workbench Launcher, manually add the base `ArmaReforger.gproj` when in doubt.
5. Scan dependency addon folders so required projects are visible.
6. Create the new project in a writable non-cloud local folder.
7. Set dependencies at creation time.
8. Open the project and confirm the selected addon loaded, not only base Arma Reforger data.
9. Keep source files backed up before publishing.

Dependency troubleshooting checklist:

1. Read the Workbench Log Console error.
2. If the error names a missing addon dependency GUID, search for that GUID in known local addon `.gproj` files.
3. If it is a Workshop addon, append the GUID to the Workshop web URL to identify it.
4. Add the missing project to Workbench Launcher with `Add Existing` or `Scan for Projects`.
5. Repeat for dependencies of dependencies.
6. If the dependency entry is empty, open the affected `.gproj` in a text editor and remove the empty entry from `Dependencies`.
7. Reopen the project and confirm the selected addon loads.

Read-only project checklist:

1. Check whether the project is inside OneDrive or another cloud-synced directory.
2. Check whether the project is inside the downloaded Workshop mods folder.
3. Move/unlock the editable source project before continuing.
4. Do not build a workflow around editing downloaded packaged Workshop data.

Publishing checklist:

1. Confirm the source project is working in Workbench.
2. Confirm login to the correct Bohemia account.
3. Confirm ownership or contributor permission for updates.
4. Confirm Workshop fields: category, version, visibility, summary, description, change notes, images, contributors, license.
5. Confirm asset rights and license before upload.
6. Confirm the Working Dir is not the editable addon folder.
7. Publish from Workbench.
8. Review bundle/upload prompts and console log output.
9. After upload, verify the Workshop page and in-game download path as needed.

Update checklist:

1. Open the editable source project.
2. Apply changes.
3. Update version/change notes when appropriate.
4. Re-bundle/publish.
5. Verify the updated Workshop item and runtime behavior.

Workshop debug-version checklist:

1. Use this only when testing specific Workshop versions.
2. Launch with the `WORKSHOP_DEBUG` script define.
3. Select the specific Workshop mod version from the added combo box.
4. Route startup parameter details to `server-hosting-startup-and-runtime.md`.

## Warnings And Failure Modes

- Do not create projects in OneDrive or similar cloud-synced folders. The wiki states such projects can fail to load.
- Do not create projects in protected folders such as Program Files. Use a location where the current Windows user has write permission.
- Do not place the publish Working Dir in the editable addon directory.
- Do not treat packaged Workshop files as recoverable source. Packaged files cannot be extracted back into source files.
- Do not publish content unless all required rights and license conditions are satisfied.
- Do not share Bohemia and Steam credentials for collaboration. Use Contributors instead.
- Do not assume stable and Experimental Workshop are the same backend. They are separate.
- Do not assume a mod published to Experimental is visible in stable, or the reverse.
- Do not remove a Workshop mod unless permanent deletion is intended.
- Do not report Workshop items for invalid reasons; misuse can lead to Workshop sanctions.
- Do not debug executable compatibility by mixing non-Diag and Diag environments. Non-Diag executables cannot connect to Diag environments or Workbench debugging tools.
- Do not use default Workbench with Experimental branch data unless the tool/data version matches.
- Do not assume Workbench loaded the selected mod just because it opened. Missing dependency GUIDs can cause Workbench to skip the mod and load only Arma Reforger data.
- Do not ignore dependencies of dependencies. They must also be visible in the Workbench project list.
- Do not use downloaded Workshop mod storage as the editable project location.
- Console Workshop downloads have storage and speed constraints; do not design test expectations around unlimited console mod storage.
- Workshop keeps previous versions, but the wiki states only the last 50 versions are kept.

Known setup/publishing failure signatures and responses:

| Symptom | Likely cause | Response |
| --- | --- | --- |
| Arma Reforger project not found in Workbench Launcher | Base data project is not registered | Add the base `ArmaReforger.gproj` through `Add Existing`. |
| Log says addon dependency GUID cannot be added | Dependency project is missing from Workbench project list | Find the GUID locally or on Workshop, then add that dependency and its dependencies. |
| Dependency is empty | Bad dependency removal/editing | Remove the empty dependency entry from `Dependencies` in the `.gproj`. |
| Project is read-only | Cloud sync or downloaded Workshop folder | Move/unlock source; keep editable projects outside cloud/download package storage. |
| Failed to load metafile of mission config image / cannot copy image | Mission config image points to an `.edds` without available source image | Ensure mission config images point to `.edds` files whose source images exist. |
| You are not the owner of the asset | Wrong Steam/Bohemia account for initial upload or no contributor permission | Use the original owner account or contributor workflow. |
| Sound map, Topology map, Navmesh missing | Terrain-related publish warning | Ignore for non-terrain mods; for terrain mods verify 2D map and navmesh workflows in terrain/world references. |
| Addon processing failed on Workshop side | Empty mod or backend processing problem | Confirm the mod contains content; if content exists, treat as backend-side failure and retry/report with error UID. |
| Workshop timeout with backend 524 | Workshop/backend timeout | Retry later. |

## API Lookup Keys

Project creation and publishing are primarily Workbench and data workflows. Do not invent scripting APIs for them.

Use these lookup keys only when a task explicitly asks for script code around Workshop, backend identity, addon UI, or Workbench tooling:

- `Workshop`
- `WorkshopAsset`
- `WorkshopCatalogueApi`
- `SCR_WorkshopAddonManagerDialogs`
- `SCR_AddonLineBaseComponent`
- `SCR_WorkshopAddonBarComponent`
- `BackendApi`
- `GetLocalIdentityId`
- `GetPlayerIdentityID`
- `Workbench`
- `WorkbenchPlugin`
- `ResourceName`

Before writing any script that touches those names, verify exact signatures with `scripts/query-reforger-data.py`. This reference does not validate or embed their API signatures.

## Game-Data Query Commands

Use these commands from the repo root:

```powershell
py -3 scripts\query-reforger-data.py files gproj --limit 10
py -3 scripts\query-reforger-data.py files addon --limit 10
py -3 scripts\query-reforger-data.py files Workshop --limit 10
```

For Workshop script/API work:

```powershell
py -3 scripts\query-reforger-data.py symbol WorkshopAsset --exact
py -3 scripts\query-reforger-data.py symbol WorkshopCatalogueApi --exact
py -3 scripts\query-reforger-data.py files Workshop --generated-only --limit 20
py -3 scripts\query-reforger-data.py files AddonManager --handwritten-only --limit 20
```

For backend identity script/API work:

```powershell
py -3 scripts\query-reforger-data.py symbol BackendApi --exact
py -3 scripts\query-reforger-data.py method BackendApi GetLocalIdentityId --exact
py -3 scripts\query-reforger-data.py method BackendApi GetPlayerIdentityID --exact
```

For Workbench tool/plugin work:

```powershell
py -3 scripts\query-reforger-data.py symbol WorkbenchPlugin --kind class --exact
py -3 scripts\query-reforger-data.py examples workbench-plugin --limit 10
py -3 scripts\query-reforger-data.py files WorkbenchPlugin --limit 20
```

For source snippets after a query returns an exact file/line:

```powershell
py -3 scripts\query-reforger-data.py snippet <scripts/...file.c> --line <line> --context 30
```

Do not load broad schema/API dumps for this topic. Query exact symbols, files, or snippets.

## Examples And Samples

Official samples are layout signals for addon roots and `.gproj` structure. They are not substitutes for the wiki publishing workflow or current API lookup.

Sample project roots reviewed:

- `SampleMod_Main`: aggregate sample project with many dependency GUIDs.
- `SampleMod_ModdedScript`: script-modding project layout.
- `SampleMod_WorkbenchPlugin`: Workbench plugin project layout.
- `SampleMod_NewWeapon`: new weapon addon layout and localized PC configuration example.
- `SampleMod_ModdedWeapon`: modded weapon project layout.
- `SampleMod_NewCar`: new vehicle addon layout.
- `SampleMod_ModdedCar`: modded vehicle project layout.
- `SampleMod_NewCharacter`: character/gear addon layout.
- `SampleMod_NewFaction`: faction addon layout.
- `SampleMod_NewProp`: prop/asset addon layout.
- `SampleMod_AnimationWorkshop`: animation-focused addon layout.
- `SampleMod_CinematicTutorial`: cinematic/tutorial addon layout.
- `SampleMod_Replacement`: replacement-mod project layout.

Pattern facts from samples:

- Most sample roots contain a single project file named either `addon.gproj` or a sample-specific `.gproj`.
- The `GameProject` block includes an `ID`, `GUID`, `TITLE`, dependency GUIDs, and platform configurations.
- Dependencies are GUID-based. Do not assume the visible title is enough to repair dependency problems.
- Samples may include domain-specific data under `Assets`, `Configs`, `Prefabs`, `Scripts`, `Language`, or other folders. Route to the narrow domain reference before editing those contents.

Useful query routes:

```powershell
py -3 scripts\query-reforger-data.py files addon --limit 20
py -3 scripts\query-reforger-data.py files Workshop --limit 20
py -3 scripts\query-reforger-data.py examples workbench-plugin --limit 10
```

## Follow-Up Keywords

Use these as search/query terms when this reference is not enough:

- `addon.gproj`
- `GameProject`
- `GUID`
- `Dependencies`
- `Workbench Launcher`
- `Add Existing`
- `Scan for Projects`
- `Open with Addons`
- `Presets`
- `Publish Project`
- `Working Dir`
- `Contributors`
- `Change Notes`
- `Workshop`
- `WorkshopAsset`
- `WorkshopCatalogueApi`
- `AddonManager`
- `BackendApi`
- `Game Identity`
- `Bohemia Account`
- `Experimental Branch`
- `Diag executable`
- `WORKSHOP_DEBUG`
- `addonDownloadDir`
- `scrDefine`
- `missing dependency`
- `read-only project`
- `packaged files`
- `source files`

## Verification

Project setup verification:

- Workbench Launcher lists the base Arma Reforger project.
- Workbench Launcher lists the addon project and all required dependencies.
- The addon opens in Workbench with the selected mod loaded, not just base Arma Reforger data.
- The project is outside cloud-synced folders and protected system folders.
- The `.gproj` has no empty dependency entries.
- Dependency GUIDs resolve to known local or Workshop projects.

Packaging verification:

- Project works in Workbench before publishing.
- Working Dir is not the editable addon root.
- Required Workshop fields are filled.
- Category is selected.
- Version and Change Notes are set appropriately for updates.
- Preview image and screenshots meet size/type limits.
- License choice is valid; custom license has `license.txt` in the addon root.
- Contributor list uses Bohemia account emails and invited contributors accept pending invitations.
- Console/log output has no packaging errors.

Workshop/runtime verification:

- Workshop item page appears with intended visibility.
- Downloaded mod can be enabled and launched.
- Server-side use of an Unlisted mod is tested if relying on Unlisted visibility.
- Terrain mods check 2D map, topology/sound map, and navmesh warnings in the terrain/world references.
- Multiplayer/server behavior is validated through the server and networking references, not inferred from successful publish.
- Diag debugging uses matching Diag client/server/Workbench environments.

Residual uncertainty to state in final answers:

- Workbench and Workshop backend behavior can fail outside script validation. Mention when a result still needs Workbench publish, backend upload, or in-game download verification.
- This reference does not guarantee scripting API signatures. State the query command used when API-sensitive code is written.

## Official Wiki Links

- Mod Project Setup: https://community.bistudio.com/wiki/Arma_Reforger:Mod_Project_Setup
- Mod Publishing Process: https://community.bistudio.com/wiki/Arma_Reforger:Mod_Publishing_Process
- Workshop: https://community.bistudio.com/wiki/Arma_Reforger:Workshop
- Development Executables: https://community.bistudio.com/wiki/Arma_Reforger:Development_Executables
- Directory Structure: https://community.bistudio.com/wiki/Arma_Reforger:Directory_Structure
- Game Identity: https://community.bistudio.com/wiki/Arma_Reforger:Game_Identity
- Startup Parameters: https://community.bistudio.com/wiki/Arma_Reforger:Startup_Parameters
- File Types: https://community.bistudio.com/wiki/Arma_Reforger:File_Types
- Intellectual Property: https://community.bistudio.com/wiki/Intellectual_Property
- Arma Reforger Workshop Terms: https://reforger.armaplatform.com/workshop-terms
- Workshop website: https://reforger.armaplatform.com/workshop

## Usefulness Score

Score: 94/100

- Wiki coverage: 29/30. All primary pages were reviewed and represented. Directory Structure, Game Identity, Development Executables, Startup Parameters, and File Types were intentionally partial or routed because their full workflows are owned elsewhere. Official wiki links are included. No primary owned page is missing.
- Operational detail: 15/15. The reference preserves launcher setup, project creation, dependency scanning, opening with addons/presets, publishing fields, packaging behavior, update/remove flows, and troubleshooting responses.
- API lookup usefulness: 13/15. Project/publishing work is mostly editor/data workflow, but script-adjacent Workshop, BackendApi, and Workbench lookup commands are provided. No API signatures are embedded.
- Example grounding: 9/10. Official sample roots and representative `.gproj` structure are covered. No source bodies are copied.
- Codex task usefulness: 14/15. Codex can route project setup, publish/update/remove, missing dependency, read-only project, and Workshop debug tasks without guessing. Domain content routes to narrow owners.
- Context efficiency: 9/10. Content is dense and scoped to project/addon/workshop lifecycle. Some partial cross-reference detail is included to prevent misrouting, but source ownership remains explicit.
- Verification guidance: 5/5. Includes Workbench, packaging, Workshop, server/multiplayer routing, and Diag executable validation.

Category-fit check:

- Source family complete: pass. Primary project setup, publishing, Workshop, and relevant executable compatibility pages are represented.
- No owned page missing: pass. Every owned primary page is listed in Source Inventory.
- Split boundary justified: pass. Server startup, Resource Manager details, Diag Menu, File Types, and domain asset workflows are explicitly routed elsewhere.
- Cross-links present: pass. Neighboring references are named for server runtime, Resource Manager, diagnostics, and domain workflows.
- Task route clear: pass. Common tasks route to one primary reference plus exact query commands when API-sensitive work begins.

Missed coverage/cap review:

- No owned primary wiki page was skipped.
- No primary setup/publishing workflow was reduced to a shallow summary.
- Publishing fields, requirements, warnings, and failure modes are preserved.
- Local raw paths and raw wiki dumps are not included.
- No automatic failure condition applies.
