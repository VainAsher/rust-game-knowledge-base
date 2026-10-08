---
id: rust-plugin-development-hooks
title: "Rust Plugin Development and Hooks"
version: 1.0.0
status: frozen
confidence: Medium
category: Modding & Plugins
topic: "Plugin development"
market: "Global"
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-modding-plugins-foundation, rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-building-raiding-foundation, rust-server-administration-foundation, rust-updates-meta-foundation, rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence, rust-server-convars-reference, rust-update-timeline-2026]
tags: [oxide, umod, carbon, plugins, hooks, permissions, csharp, development]
game_build_checked: "Rust 2634.289.1 (2 Oct 2026 hotfix #3) as named in Oxide.Rust 2.0.7801 notes; Oxide.Rust 2.0.7810 and Carbon Production Build v2.0.262 checked 2026-10-08; docs read 2026-10-08"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-plugin-development-hooks |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Modding & Plugins |
| Region | Global |
| Game build checked | Rust 2634.289.1 (Oct 2026 hotfix); Oxide.Rust 2.0.7810; Carbon v2.0.262 |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

A Rust Oxide plugin is a single C# source file (`.cs`) that the framework compiles at runtime. It holds one public class in the `Oxide.Plugins` namespace, inheriting from `RustPlugin` (or `CovalencePlugin` for game-agnostic plugins), decorated with an `[Info]` attribute for name, author and version [1][2]. Behaviour is added by writing hook methods the framework calls on game events, by registering commands, and by registering permissions [1][2][4][5]. Settings live in a JSON config file in `oxide/config`, persistent state in JSON data files in `oxide/data`, and translated messages in `oxide/lang/<code>/<Plugin>.json` [7][16][17][18].

Carbon, the alternative loader, documents the same plugin shape: `RustPlugin` in `Oxide.Plugins` for Oxide-compatible plugins, and `CarbonPlugin` in `Carbon.Plugins` for Carbon-only plugins [19]. Where Carbon differs (hook dispatch, extra command attributes, config folder name) this document labels the difference only where a Carbon page states it [20][21][23]. Confidence is Medium: structure and API are primary-sourced from the framework docs, but several pages are thin (no signatures on the core permission library page, no description on some hook pages), and the Oxide docs say nothing on how conflicting hook return values from several plugins are resolved.

# Key Facts

- Oxide plugins are distributed as `.cs` files; extensions are `.dll` files [1][2].
- The main class is public, lives in `Oxide.Plugins` and inherits `RustPlugin` for Rust-only plugins [2]. The plugin guidelines say the file name should match the main class name in PascalCase [8].
- Metadata is `[Info("Name", "Author", "1.0.0")]` plus an optional `[Description("...")]` [2][4][8].
- Lifecycle order is Init, Loaded, OnServerInitialized, then (on shutdown) Shutdown and Unload [3].
- For hooks documented with return behaviour, a non-null return overrides default behaviour and null lets it proceed (`CanLootEntity`); many hooks list "No return behavior" [12][13][14][15].
- Oxide's hook index grouped hooks into 38 categories on 2026-10-08, the largest being Player (155), Entity (102), Item (64) and Vehicle (52) [11].
- Permissions are registered with `permission.RegisterPermission(name, this)`, and the documented convention is `pluginname.permission` in lowercase [5][8].
- Carbon says its folder and plugin structure matches Oxide, but Oxide's `config` folder becomes `configs` and commands use a `c.` prefix instead of `o.` [23][28].

# Scope

Covered: structure and APIs of server-side C# plugins for Rust on Oxide (uMod) and Carbon: class and attributes, lifecycle, hooks and their return semantics, commands, permissions API, config, data files and localization files, development environment, and official authoring guidelines. Build: Oxide.Rust 2.0.7810 and Carbon v2.0.262 era (Rust 2634.289.1, October 2026).

Not covered: installing frameworks and the admin-side permission commands (see rust-modding-plugins-foundation), individual plugin reviews, the Rust game systems hooks touch (see rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence), console and client modification, and Carbon module/UI libraries beyond a mention.

# Definitions

- **Hook:** a function called by the game or by Oxide to define what happens on a game event [1].
- **Info attribute:** the metadata attribute carrying plugin name, author and version [2][4].
- **Covalence plugin:** a game-agnostic plugin deriving from `CovalencePlugin`, versus a `RustPlugin` for Rust only [2].
- **Data file:** JSON persistence in `oxide/data`, distinct from the admin-edited config in `oxide/config` [7][17].
- **Harmony patch:** a runtime method patch installed with `[AutoPatch]` plus `[HarmonyPatch]`, available in both frameworks' docs [4][20].

# Core Mechanics

**Plugin file and class.** A plugin is one `.cs` file compiled at runtime; the beginner guide names both file and class `MyFirstPlugin`, uses the `Oxide.Plugins` namespace, and derives from `RustPlugin` [2]. The guidelines state the file name "should match the name of your main class and use PascalCase" [8]. Carbon's first-plugin page uses the file-scoped namespace form (`namespace Oxide.Plugins;`) for Oxide-compatible plugins [19]. Compile errors appear in the server console after the file is uploaded [2].

**Development environment.** Oxide's guide names Visual Studio, Visual Studio Code and JetBrains Rider as IDE options, and lists `Oxide.Core.dll`, `Oxide.Rust.dll`, `Assembly-CSharp.dll` and `UnityEngine.dll` as the references to add [10]. Its best-practices page recommends Git source control (excluding binaries, logs and local config), testing, and documenting installation, commands and configuration [9]. For Carbon, the developer docs describe a local Windows development server built from the Carbon.QuickStart files, with an optional debugger set in `doorstop_config.ini` [25].

**Attributes.** `[Info("Name", "Author", "1.0.0")]`: the name uses spaces between words, the second argument is the developer or maintainer, and the version is three-part [4]. `[Description]` is a brief summary [4]; the guidelines recommend it for documentation [8]. Further documented attributes: `[ChatCommand]`, `[ConsoleCommand]`, `[Command]` (covalence), `[Permission]`, `[PluginReference]`, `[OnlinePlayers]`, `[HookMethod("HookName")]` and `[AutoPatch]`; comment directives `//Requires: PluginName` (plugin will not start if the required plugin is missing) and `//Reference: AssemblyName` [4].

**Lifecycle.** Per Oxide's lifecycle page: `Init` runs first, before dependencies are available, and an exception there stops initialisation; `Loaded` runs after Init and before registration, and is where asynchronously loaded config and localisation can be read through the `Config` object; `OnServerInitialized` runs near the end of boot, and still runs locally on a runtime reload; `Shutdown` runs only if the game provider supports Advanced Hooks; `Unload` runs when the plugin manager unloads the plugin. `OnConfigChanged` can override default config monitoring during hotloading [3]. The beginner guide registers permissions in `Init` [2][5]; the hook page shows `OnServerInitialized(bool serverInitialized)` is called with `true` after startup and with `false` on hot-loaded plugins when the server is already initialised [13].

**Hooks.** Hooks are methods whose name and parameters match a documented hook; the framework calls them when the event fires [1][2]. Each hook has its own page at `/hooks/<category>/<HookName>` giving signature, description where present, return behaviour and the engine call site [11][12]. For `CanLootEntity(BasePlayer player, WorldItem instance)`, the page states that returning a non-null value overrides default behaviour and returning null lets it proceed [12]. Other documented hooks list "No return behavior" (`OnServerInitialized`, `OnUserPermissionGranted`, `OnPlayerConnected`) [13][14][15]. `OnUserPermissionGranted` fires only when the permission is newly added to the user's data [14]. Hook names often come in pairs (for example `OnOvenStart`/`OnOvenStarted`), which is an inference from names, not stated by the index [11].

**Commands.** Rust plugins use `[ChatCommand("name")]` with `(BasePlayer player, string command, string[] args)` and `[ConsoleCommand("name")]` with `(ConsoleSystem.Arg arg)`; covalence plugins use `[Command]` with an `IPlayer` [4]. `[Permission("perm.name")]` restricts a command to holders of that permission [4]. The guidelines ask for lowercase underscore command names such as `my_command` [8].

**Permissions API (Oxide).** Register in `Init` with `permission.RegisterPermission("epicstuff.use", this)`; check with `permission.UserHasPermission("playerID", "epicstuff.use")` or `player.HasPermission(...)` on an `IPlayer`; group management includes `CreateGroup(name, title, rank)`, `GrantGroupPermission`, `RevokeGroupPermission`, `GetGroupPermissions(group, includeParents)`, `AddUserGroup` and `UserHasGroup` [5]. The beginner guide passes `player.UserIDString` to `UserHasPermission` [2]. The core library page confirms `RegisterPermission` makes a permission available for assignment to players and groups, and that `CreateGroup` attaches group title and rank [6].

**Config, data and lang files.** Config lives in `oxide/config/<PluginName>.json` and is the admin-edited layer; data lives in `oxide/data` and is plugin-managed; language files are `oxide/lang/<code>/<Plugin>.json` [7][16][17][18]. A data file is opened with `Interface.Oxide.DataFileSystem.GetFile(Name)`, returning a `DynamicConfigFile` with `ReadObject<T>()`, `WriteObject(obj)` and `Clear()` [7]. Classes are serialised with Newtonsoft.Json; `[JsonProperty(PropertyName=...)]` sets a readable key, `[JsonIgnore]` excludes runtime fields, and `ObjectCreationHandling.Replace` on lists prevents default entries accumulating on every restart [7]. The beginner guide implements config through `LoadConfig`, `LoadDefaultConfig`, `GetDefaultConfig` and `SaveConfig` [2]. The Oxide docs do not describe how plugin code registers messages; admin-facing notes only describe the file layout, `{0}`/`{1}` placeholders and Rust text tags [18].

**Carbon plugin shape.** Carbon documents the same layout for Oxide-compatible plugins and a Carbon-only variant: namespace `Carbon.Plugins`, base class `CarbonPlugin` [19]. Carbon's hook system differs internally: it calls hooks by numeric ID through `HookCaller.CallStaticHook` rather than `Interface.CallHook` with a name string [20]. Its owner-facing comparison says Carbon only runs hooks that loaded plugins need, while Oxide "fires all hooks all the time" (Carbon's wording) [23]. Carbon's hooks reference marks hooks not flagged Static or Patch as applied dynamically when a plugin subscribes [24]. Carbon adds command restriction attributes `[Group]`, `[AuthLevel(n)]` and `[Cooldown(ms)]` beside `[Permission]`, plus `[ProtectedCommand]` [21].

# Reference Data

Plugin skeleton elements (docs read 2026-10-08):

| Element | Oxide-compatible form | Source |
|---------|-----------------------|--------|
| Namespace | `Oxide.Plugins` | [2][19] |
| Base class | `RustPlugin` (Rust) or `CovalencePlugin` (game-agnostic) | [2] |
| Metadata | `[Info("Name", "Author", "1.0.0")]`, optional `[Description]` | [4][19] |
| Hook method | `private void OnServerInitialized()` style | [13][19] |
| Config file | `oxide/config/<Plugin>.json` | [16] |
| Data files | `oxide/data/` (subfolder per plugin recommended) | [7][17] |
| Lang file | `oxide/lang/<code>/<Plugin>.json` | [7][18] |

Lifecycle sequence [3]:

| Order | Step | Notes |
|-------|------|-------|
| 1 | `Init` | Before dependencies available; exception rolls back |
| 2 | `Loaded` | Read async config/localisation via `Config` |
| 3 | `OnServerInitialized` | Boot nearly complete; runs on hot reload too |
| 4 | `Shutdown` | Only with Advanced Hooks support |
| 5 | `Unload` | After hook routing disabled |

Documented hook examples (Oxide hook pages, 2026-10-08):

| Hook | Signature | Return behaviour | Source |
|------|-----------|------------------|--------|
| `CanLootEntity` | `object CanLootEntity(BasePlayer, WorldItem)` | Non-null overrides default; null proceeds | [12] |
| `OnServerInitialized` | `void OnServerInitialized(bool)` | None | [13] |
| `OnUserPermissionGranted` | `void (string playerId, string permission)` | None | [14] |
| `OnPlayerConnected` | `void (BasePlayer)` | None | [15] |

Oxide hook index category counts (2026-10-08) [11]:

| Category | Hooks | Category | Hooks |
|----------|-------|----------|-------|
| Player | 155 | Server | 46 |
| Entity | 102 | Structure | 33 |
| Item | 64 | Weapon | 25 |
| Vehicle | 52 | Permission | 13 |

Command attributes [4][21]:

| Attribute | Scope | Signature | Framework |
|-----------|-------|-----------|-----------|
| `[ChatCommand]` | Chat | `(BasePlayer, string, string[])` | Oxide [4], Carbon [21] |
| `[ConsoleCommand]` | F1/terminal/RCon | `(ConsoleSystem.Arg)` | Oxide [4], Carbon [21] |
| `[Command]` | Chat and console | Oxide: `(IPlayer, string, string[])`; Carbon: `(BasePlayer, string, string[])` | Oxide [4], Carbon [21] |
| `[Group]`, `[AuthLevel]`, `[Cooldown]`, `[ProtectedCommand]` | Restrictions | n/a | Carbon docs only [21] |

Permission API calls [5][22]:

| Call | Oxide docs | Carbon docs |
|------|-----------|-------------|
| `RegisterPermission(name, plugin)` | Yes [5] | Yes; in `Init()` or `OnServerInitialized()` [22] |
| `UserHasPermission(id, name)` | Yes [5] | Yes [22] |
| `CreateGroup(name, title, rank)` | Yes [5] | Yes; returns false if exists [22] |
| `GetGroupPermissions(group, parents)` | Yes [5] | Yes [22] |
| `AddUserGroup` / `UserHasGroup` | Yes [5] | Not documented on the page [22] |

Naming rules from the Oxide plugin guidelines [8]: commands lowercase with underscores; permissions `pluginname.permission` with lowercase plugin name; locals camelCase; properties PascalCase; semantic versioning with the `[Info]` version updated on every change.

Carbon versus Oxide migration facts, as stated by Carbon [23]:

| Item | Carbon statement |
|------|------------------|
| Coexistence | Oxide and Carbon cannot run on the same install |
| Command prefix | `c.` instead of `o.` |
| Config folder | Oxide `config` becomes `carbon/configs` |
| Plugin source changes | Page does not describe any required |
| Permission storage | Carbon says it uses SQLite-based permissions |

# Version & Patch Notes

- Oxide.Rust 2.0.7801 (2026-10-02) is described as a patch for Rust's 2 October hotfix #3 (build 2634.289.1) and added `OnNpcTarget` hooks for WildlifeHazard and BoatAI; 2.0.7810 followed on 2026-10-07 with no listed changes [26].
- Carbon "Production Build v2.0.262" was published 2026-10-02 [27].
- Carbon says Harmony 2.0 is used by both frameworks: Carbon has always run it, and Oxide now uses it too [23]. The date Oxide adopted it was not stated.
- Hook counts and signatures track Rust and are volatile; the hook index is regenerated as the framework updates, so re-check pages before relying on a signature [11].

# Common Pitfalls

- Treating `Init` as safe for dependencies: the lifecycle page says dependencies are not available in `Init`, and an exception there rolls back compilation [3].
- Config overwritten on unload: some plugins save config when unloaded, so edits made while loaded can be lost; the admin guidance is to unload, edit, load [16].
- Default list entries piling up on restart unless `ObjectCreationHandling.Replace` is set [7].
- Missing `//Requires:` dependency: the plugin will not start [4].
- Returning a value from a hook with documented "No return behavior" has no documented effect; returning non-null from override-style hooks blocks default behaviour [12][13].
- Blocking the main thread with heavy computation or file I/O is called out as disrespectful to the server in the guidelines [8].
- Assuming Carbon and Oxide can be mixed: Carbon states they cannot coexist [23]. Carbon also says it needs unmodified Facepunch DLLs, so Oxide-patched files must be reverted [23].
- Typing `o.` commands on Carbon: they do not work, though aliases can be defined [23].

# Interactions & Related Systems

Hooks are the integration point to nearly every other KB system: combat and damage events (rust-combat-damage-model, rust-weapons-ammo), building and raiding (rust-raiding-costs-defence), item and crafting hooks such as `CanCraft` [11] (rust-items-crafting-foundation). Plugin configuration and convars intersect with rust-server-convars-reference. Framework status, installation and the admin permission commands are in rust-modding-plugins-foundation; Rust hotfix timing that forces framework patches is in rust-update-timeline-2026 and rust-updates-meta-foundation. Server-side behaviour changes by plugins are outside the vanilla mechanics in rust-game-mechanics-foundation.

# Assessed Guidance

## Guidance 1 — Register permissions early and name them pluginname.action

- **Guidance:** Register every permission in `Init` (or `OnServerInitialized` on Carbon), use lowercase `pluginname.action` names, and gate commands with `[Permission]` rather than hand-written checks where possible.
- **Evidence basis:** Registration in `Init` and the naming convention are documented [2][5][8][22]; the `[Permission]` attribute is documented [4][21].
- **Confidence:** High. Several primary pages from both frameworks agree.
- **So what:** Admins can find and grant the permission with standard commands, and permissions do not collide across plugins.

## Guidance 2 — Keep Init minimal and defer cross-plugin work to OnServerInitialized

- **Guidance:** Do setup that needs other plugins or world state in `OnServerInitialized`, and handle both `true` and `false` values of its parameter so hot reloads behave.
- **Evidence basis:** Init runs before dependencies are available; OnServerInitialized runs on reload with `false` [3][13].
- **Confidence:** Medium. The lifecycle page is clear but the advice is a synthesis, and no primary page tests it.
- **So what:** Fewer load-order bugs when a plugin is reloaded on a live server.

## Guidance 3 — Separate config from data and guard against list accumulation

- **Guidance:** Put admin-tunable settings in the config and plugin-managed state in data files, and set `ObjectCreationHandling.Replace` on default lists.
- **Evidence basis:** Config/data split and the list behaviour [7][16][17].
- **Confidence:** High. Stated on official pages.
- **So what:** Admins edit the right file, backups cover `oxide/data`, and restarts do not duplicate default entries.

## Guidance 4 — Write for Oxide compatibility unless you need Carbon-only features

- **Guidance:** Use `RustPlugin` and `Oxide.Plugins` by default, and use `CarbonPlugin` or Carbon-only command attributes only when you accept losing Oxide portability.
- **Evidence basis:** Carbon documents both shapes and labels Carbon-only attributes [19][21]; Carbon says the plugin structure is the same [28].
- **Confidence:** Medium. Compatibility is the framework's own claim, and the docs do not test every attribute across both.
- **So what:** A single plugin file can serve servers on either framework; test on both before claiming support.

## Guidance 5 — Re-verify every hook signature against the current hook page before shipping

- **Guidance:** Treat a hook's signature and return behaviour as build-specific and check the hook page after each Rust update.
- **Evidence basis:** Oxide shipped a patch for a Rust hotfix and added new hooks the same day [26]; hook pages list the engine call site [12].
- **Confidence:** Medium. The release evidence is two observed releases.
- **So what:** Fewer silently dead hooks after a Rust update.

# Open Questions

- How Oxide or Carbon resolve conflicting return values when several plugins implement the same override-style hook: the Oxide pages opened state only the per-hook return text [12], and Carbon's page covers only its internal patch return handling [20]. Resolving it needs the framework core docs or source.
- Oxide docs gave no code signature for the core permission library methods [6], so signatures here come from the developer permissions guide [5].
- The `Description` attribute was not covered by the beginner guide [2]; its use is taken from the attributes and guidelines pages [4][8].
- Where the Oxide docs cover `LoadDefaultMessages` or `lang.RegisterMessages` for registering messages in code was not found; the localisation page covers files only [18].
- Carbon's hooks reference loaded no entries in the capture, so Carbon-specific hook counts are unverified [24].
- Whether Oxide and Carbon behave identically for every Oxide plugin attribute is unverified beyond Carbon's compatibility statement [28].

# References

**Primary Sources**

- [1] **Oxide** — *Developers: Getting Started*. https://docs.oxidemod.com/guides/developers/getting-started. Accessed 2026-10-08.
- [2] **Oxide** — *My First Plugin*. https://docs.oxidemod.com/guides/developers/my-first-plugin. Accessed 2026-10-08.
- [3] **Oxide** — *Plugin lifecycle*. https://docs.oxidemod.com/guides/developers/plugin-lifecycle. Accessed 2026-10-08.
- [4] **Oxide** — *Attributes*. https://docs.oxidemod.com/guides/developers/attributes. Accessed 2026-10-08.
- [5] **Oxide** — *Developers: Permissions*. https://docs.oxidemod.com/guides/developers/permissions. Accessed 2026-10-08.
- [6] **Oxide** — *Core library: Permissions*. https://docs.oxidemod.com/core/libraries/permissions. Accessed 2026-10-08.
- [7] **Oxide** — *Data Storage*. https://docs.oxidemod.com/guides/developers/data-storage. Accessed 2026-10-08.
- [8] **Oxide** — *Plugin Guidelines*. https://docs.oxidemod.com/guides/developers/plugin-guidelines. Accessed 2026-10-08.
- [9] **Oxide** — *Best Practices*. https://docs.oxidemod.com/guides/developers/best-practices. Accessed 2026-10-08.
- [10] **Oxide** — *Development Environment*. https://docs.oxidemod.com/guides/developers/development-environment. Accessed 2026-10-08.
- [11] **Oxide** — *Hook Index*. https://docs.oxidemod.com/hooks/. Accessed 2026-10-08.
- [12] **Oxide** — *Hook: CanLootEntity*. https://docs.oxidemod.com/hooks/entity/CanLootEntity. Accessed 2026-10-08.
- [13] **Oxide** — *Hook: OnServerInitialized*. https://docs.oxidemod.com/hooks/server/OnServerInitialized. Accessed 2026-10-08.
- [14] **Oxide** — *Hook: OnUserPermissionGranted*. https://docs.oxidemod.com/hooks/permission/OnUserPermissionGranted. Accessed 2026-10-08.
- [15] **Oxide** — *Hook: OnPlayerConnected*. https://docs.oxidemod.com/hooks/player/OnPlayerConnected. Accessed 2026-10-08.
- [16] **Oxide** — *Configuring Plugins (server owners)*. https://docs.oxidemod.com/guides/owners/configure-plugins. Accessed 2026-10-08.
- [17] **Oxide** — *Data Files (server owners)*. https://docs.oxidemod.com/guides/owners/data-files. Accessed 2026-10-08.
- [18] **Oxide** — *Localization (server owners)*. https://docs.oxidemod.com/guides/owners/localization. Accessed 2026-10-08.
- [19] **Carbon** — *Creating Your First Plugin*. https://carbonmod.gg/devs/creating-your-first-plugin. Accessed 2026-10-08.
- [20] **Carbon** — *Creating Hooks*. https://carbonmod.gg/devs/creating-hooks. Accessed 2026-10-08.
- [21] **Carbon** — *Commands*. https://carbonmod.gg/devs/features/commands. Accessed 2026-10-08.
- [22] **Carbon** — *Permissions*. https://carbonmod.gg/devs/features/permissions. Accessed 2026-10-08.
- [23] **Carbon** — *Oxide Porting (migration)*. https://carbonmod.gg/owners/oxide-porting. Accessed 2026-10-08.
- [24] **Carbon** — *Hooks reference*. https://carbonmod.gg/references/hooks/. Accessed 2026-10-08.
- [25] **Carbon** — *Local Server Hosting (developer docs)*. https://carbonmod.gg/devs/local-server-hosting. Accessed 2026-10-08.
- [26] **OxideMod** — *Oxide.Rust releases API*. https://api.github.com/repos/OxideMod/Oxide.Rust/releases. Accessed 2026-10-08.
- [27] **CarbonCommunity** — *Carbon latest release API*. https://api.github.com/repos/CarbonCommunity/Carbon/releases/latest. Accessed 2026-10-08.
- [28] **Carbon** — *Carbon for Rust (project site)*. https://carbonmod.gg/. Accessed 2026-10-08.

**Community & Practitioner Evidence**

None cited. All claims rest on first-party framework documentation.

**Further Reading**

See the Further Reading section below.

# Further Reading

- Oxide Core documentation index: https://docs.oxidemod.com/core/
- Carbon developer docs sidebar lists features not covered here: Bridge, Vault, LUI, Modifiers and modules.

# Related Documents

- rust-modding-plugins-foundation
- rust-game-mechanics-foundation
- rust-items-crafting-foundation
- rust-building-raiding-foundation
- rust-server-administration-foundation
- rust-updates-meta-foundation
- rust-combat-damage-model
- rust-weapons-ammo
- rust-raiding-costs-defence
- rust-server-convars-reference
- rust-update-timeline-2026

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
