---
id: rust-server-convars-reference
title: "Rust Server Convars Reference"
version: 1.0.0
status: frozen
confidence: Medium
category: Server Administration
topic: "Server convars and config"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-server-administration-foundation, rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-building-raiding-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation, rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence, rust-plugin-development-hooks, rust-update-timeline-2026]
tags: [convars, server, decay, rcon, secure]
game_build_checked: "October 2026 update (Livestock Update, 1 Oct 2026)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-server-convars-reference |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Server Administration |
| Region | Global |
| Game build checked | October 2026 update (Livestock Update, 1 Oct 2026) |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This reference lists the server convars that Facepunch itself documents or names, grouped by purpose: startup and world, decay and upkeep, Rust+ companion, secure-server and encryption, tags and gamemodes, and recent devblog additions. It goes deeper than rust-server-administration-foundation by giving names, defaults and effects row by row, and by resolving the foundation's open question on secure-server convars.

Confidence is Medium. Every row comes from a Facepunch wiki page or devblog, but Facepunch publishes no complete convar list, many pages are marked as old or work in progress, and several defaults are simply not stated. Gather-rate convars and the RCON connection-limit convar names were not found on any Facepunch page and are listed as gaps rather than guessed. Checked against the October 2026 update [6].

# Key Facts

- Facepunch's wiki documents only a handful of decay convars: `decay.scale` (default 1), `decay.upkeep_period_minutes` (default 1440) and `decay.upkeep_grief_protection` (default 1440) [1].
- `server.useServerWideRequiredSystemConfig` requires TPM and Secure Boot for all players and earns the Secure browser tag; `server.usePerPlayerRequiredSystemConfig` enforces per player and does not earn the tag [8].
- `server.secure` was removed on 4 September 2025; insecure servers now pass `-insecure` at startup, and a secure server needs `server.encryption` set to 2 [9][10].
- `app.port` defaults to the larger of game port or RCON port plus 67 (28082 with default ports), must be 10000 or higher, and `-1` disables Rust+ [3].
- `rcon.port` is TCP and `server.queryport` is UDP and must differ from `server.port` [5].
- `UsePlayerUpdateJobs` has defaulted to 2 since the April 2026 update [7].
- No Facepunch page opened for this document lists a gather-rate convar or any default for one *(gap, see Open Questions)*.
- The Useful Console Commands page says it is a work in progress and last updated "A Long Time Ago" [1].

# Scope

Covers vanilla dedicated-server variables on PC that appear on Facepunch wiki pages or Facepunch devblogs, checked against the October 2026 update. Convars are set on the command line with a `+` prefix or in `server.cfg` without it, or discovered via `find` in the server console [5]. Not covered: Oxide/Carbon plugin configuration (see rust-modding-plugins-foundation and rust-plugin-development-hooks), client-only convars, third-party host panels, and community-maintained convar dumps, which were not used.

# Definitions

- **Convar** — a console variable or command that configures the server; set at launch, in `server.cfg`, or at runtime [5].
- **Upkeep** — resources a Tool Cupboard consumes to protect a base from decay [2].
- **Secure tag** — server-browser tag shown only when TPM and Secure Boot are enforced for all players [8].
- **Companion server** — the Rust+ listener configured with the `app.*` convars [3].

# Core Mechanics

**Setting convars.** Launch arguments use `+name value`; `server.cfg` in `server/<identity>/cfg/` takes the same settings without the prefix. For settings not in the wiki table the page suggests the `find` console command, for example `find image` [5]. The foundation document covers file locations and precedence.

**Decay and upkeep.** A Tool Cupboard pays upkeep, described as a fraction of the resources used to build, per 24 hours. With no resources in a cupboard, decay starts immediately. Decay starts at the outermost exposed pieces and moves inward, and if one upkeep material runs out only parts of that material decay [2]. After upkeep runs out, the wiki gives full-decay times: twig 1 hour, wood 3 hours, stone 5 hours, metal 8 hours, armoured 12 hours. A destroyed cupboard that held resources consumes up to 24 hours of upkeep, protecting the base for that long [2]. The tool-cupboard page names no convars and carries no build date [2]; the console-commands page supplies the three decay convars [1]. Vehicle decay is separate: minicopter, attack and transport helicopters have their own inside and outside decay timers [1].

**Rust+ companion.** `app.port` sets the listening port and `-1` disables Rust+ (on the command line this is written `+app.port 1-` because of parser conflicts). The server must reach companion-rust.facepunch.com. `app.listenip` selects the NIC, `app.publicip` sets the address the app uses when `app.info` shows a wrong one, and `app.id` carries a warning not to change it [3].

**Secure servers and encryption.** From 5 March 2026 servers can opt in to requiring TPM and Secure Boot [8]. From 7 August 2025 an insecure server is started with `-insecure` rather than `server.secure false` [9]; on 4 September 2025 Facepunch removed `server.secure` and required `server.encryption` 2 for a server to count as secure [10]. The pages opened do not mention Easy Anti-Cheat settings [6][8][9][10].

**Tags and gamemodes.** `server.tags` takes a comma-separated list (example `weekly,vanilla,roleplay`), `server.pve` applies the PvE tag, up to four tags show at once, and tags in the same group should not be combined [11]. `server.gamemode` sets a gamemode at startup, empty meaning default gameplay [4].

# Reference Data

Checked against the October 2026 update unless stated. "Not stated" means the cited page gives no default.

**Startup and world** [5]

| Convar | Default | Effect |
|--------|---------|--------|
| `server.port` | 28015 (UDP) | Port players connect to |
| `server.queryport` | 1 + the greater of `server.port` or `rcon.port` (UDP) | Server-browser queries; must differ from `server.port` |
| `server.level` | Not stated | Map type; "Procedural Map" is the only option listed |
| `server.seed` | Not stated | Map seed, 0 to 2147483647 |
| `server.worldsize` | Not stated | Map size; wiki suggests 1000 to 6000 |
| `server.maxplayers` | Not stated | Maximum concurrent players |
| `server.hostname` | Not stated | Name in server list |
| `server.description` | Not stated | Text on connection window |
| `server.url` | Not stated | Website link |
| `server.headerimage` | Not stated | Server picture |
| `server.identity` | Not stated | Internal name and folder |

**RCON** [5]

| Convar | Default | Effect |
|--------|---------|--------|
| `rcon.port` | Equal to `server.port` per the wiki table (TCP) | Remote admin port |
| `rcon.password` | Not stated | RCON password; wiki says to change the example |
| `rcon.web` | Not stated (1 suggested) | RCON connection method |

**Decay and upkeep** [1]

| Convar | Default | Effect |
|--------|---------|--------|
| `decay.scale` | 1 | Multiplier for decay across the server |
| `decay.upkeep_period_minutes` | 1440 | Minutes one upkeep cost covers; higher is cheaper |
| `decay.upkeep_grief_protection` | 1440 | Maximum minutes of upkeep a destroyed cupboard can consume |
| `playerhelicopter.insidedecayminutes` | 2880 | Minutes for a player helicopter to decay from full health under a roof |
| `playerhelicopter.outsidedecayminutes` | 480 | Same, outdoors |

**Other documented defaults** [1][4]

| Convar | Default | Effect |
|--------|---------|--------|
| `hackablelockedcrate.requiredhackseconds` | 900 | Time to hack locked crates such as Oil Rig |
| `env.progesstime` | Not stated | Whether time advances (spelling as on the wiki) |
| `server.gamemode` | Empty | Startup gamemode |
| `gamemodesoftcore.reclaim_fraction_belt` | 0.5 | Hotbar fraction reclaimable at terminals |
| `gamemodesoftcore.reclaim_fraction_main` | 0.5 | Inventory fraction reclaimable |
| `gamemodesoftcore.reclaim_fraction_wear` | 0 | Armour fraction reclaimable |
| `relationshipmanager.maxteamsize` | Not stated | Maximum team size; Softcore uses 4 |

**Rust+ companion** [3]

| Convar | Default | Effect |
|--------|---------|--------|
| `app.port` | Larger of game port or RCON port, plus 67 (28082 with defaults) | Listen port; 10000 or higher; `-1` disables; restart needed |
| `app.listenip` | Not stated | Which NIC to listen on |
| `app.publicip` | Not stated | Address the Rust+ app connects to |
| `app.id` | Not stated | Do not change |

**Secure servers, encryption and tags**

| Convar or argument | Default | Effect | Source |
|--------------------|---------|--------|--------|
| `server.useServerWideRequiredSystemConfig` | Not stated | Requires TPM and Secure Boot for all players; earns Secure tag | [8] |
| `server.usePerPlayerRequiredSystemConfig` | Not stated | Per-player enforcement; no Secure tag | [8] |
| `server.encryption` | Not stated | Must be 2 for a server to be considered secure (from 4 Sep 2025) | [10] |
| `-insecure` | Off | Startup flag for insecure servers; replaces `server.secure` | [9][10] |
| `UsePlayerUpdateJobs` | 2 | Player update job level; 0 and 1 slated for removal, 3 experimental | [7] |
| `server.tags` | Not stated | Comma-separated browser tags | [11] |
| `server.pve` | Not stated | Applies PvE tag | [11] |

**Recent additions.** `vehicle.padrepairsrequired`, `vehicle.setrepairablepads`, `powergrid.fusedecaylowpop`, `powergrid.fusedecayhighpop`, `powergrid.fusedecaylowpopscale` (fuses last four times longer at 10 or fewer players, normal at 100 or more) and `paint.outlineinvert` were added in the October 2026 update, defaults not stated [6]. `global.legacymonumentnotifications` was removed in April 2026 [7]. CCTV convars `global.setcctvcameracode`, `global.addcctvcode`, `global.removecctvcode` and `global.clearcctvcodes` were added in September 2025 [10].

# Version & Patch Notes

- 1 October 2026 (Livestock): helipad and fuse-decay convars added; RCON disconnect fix; six Facepunch servers moved to TPM and Secure Boot; mandatory update 22 October 2026 at 18:00 BST [6].
- 2 April 2026 (Spring Clean): `UsePlayerUpdateJobs` default set to 2; convars added for RCON and Rust+ connection limits (names not given); `global.legacymonumentnotifications` removed [7].
- 5 March 2026 (Shipshape): opt-in TPM and Secure Boot requirement and the two `server.use...RequiredSystemConfig` convars [8].
- 4 September 2025 (Maintenance): `server.secure` removed; `server.encryption` 2 required for secure status [10].
- 7 August 2025 (Harder Core): `-insecure` startup parameter introduced [9].
- Volatile: all rows above; the console-commands and tool-cupboard pages are undated or marked old [1][2].

# Common Pitfalls

- Setting `server.secure false` no longer works; use `-insecure` [9][10].
- Setting `app.port` below 10000 makes Rust+ unreachable [3].
- Turning on `server.usePerPlayerRequiredSystemConfig` alone does not give the Secure tag [8].
- Combining several tags from one group can drop the server from tag searches [11].
- Treating the wiki decay pages as current: the cupboard page carries no build date [2].
- The RCON default port in the wiki table equals `server.port`, which is easy to misconfigure; confirm on a running server [5].

# Interactions & Related Systems

- Upkeep and decay settings change the cost of holding a base, which affects the raid economy in rust-raiding-costs-defence and rust-building-raiding-foundation [1][2].
- Secure-server requirements interact with who can join and with the population; see rust-server-administration-foundation [8].
- Plugin frameworks may add their own config; see rust-modding-plugins-foundation.
- Fuse and helipad convars touch items and vehicles; see rust-items-crafting-foundation [6].
- Monthly changes are tracked in rust-update-timeline-2026 and rust-updates-meta-foundation.

# Assessed Guidance

## Guidance 1 — Treat the wiki convar defaults as starting points and verify with `find`

- **Guidance:** Before relying on any default in this table, confirm the live value with the server console `find` command after each monthly update.
- **Evidence basis:** The console-commands page is work in progress and old [1], the wiki itself recommends `find` for unlisted settings [5], and convars change monthly [6][7].
- **Confidence:** Medium. The staleness of the pages is documented; how many defaults have drifted is not known.
- **So what:** Avoids trusting a stale default when tuning decay or ports.

## Guidance 2 — Change decay with `decay.scale` first

- **Guidance:** To make a server more or less punishing about decay, adjust `decay.scale` before touching the upkeep period, and record any change in the server description.
- **Evidence basis:** `decay.scale` is the single documented multiplier, while the upkeep convars shift only cost timing and grief protection [1]; material decay times are documented separately [2].
- **Confidence:** Low. The ordering is inference, and the effect of the scale on each material time is not documented.
- **So what:** A single multiplier is easier to reason about and revert than three interacting values.

## Guidance 3 — Use server-wide secure enforcement only if you accept the population cost

- **Guidance:** Enable `server.useServerWideRequiredSystemConfig` only if reduced cheating matters more than losing players without TPM and Secure Boot.
- **Evidence basis:** Enforcement and the tag are documented [8], and Facepunch reported that roughly 60% of players have the features enabled [7].
- **Confidence:** Medium. The mechanism is first-party; the trade-off is judgement.
- **So what:** Expect a smaller pool of eligible players in return for the Secure tag.

# Open Questions

- **Gather rates:** no Facepunch page opened lists a gather-rate convar or default. Resolve with `find gather` on a live server or a Facepunch devblog that names one.
- **RCON limits:** Spring Clean says convars were added for RCON and Rust+ connection limits but does not name them [7].
- **Easy Anti-Cheat:** no Facepunch source opened states any EAC convar or setting.
- **Defaults not stated:** `server.encryption`, the two RequiredSystemConfig convars, `rcon.web`, and most world convars lack documented defaults.
- **RCON port default:** the wiki says it equals `server.port`; verify live [5].
- **Wipe and world-config convars** are covered in the foundation and not repeated here.

# References

**Primary Sources**

- [1] **Facepunch Wiki** — *Useful Console Commands*. https://wiki.facepunch.com/rust/useful_commands. Accessed 2026-10-08.
- [2] **Facepunch Wiki** — *Tool Cupboard, decay and building privilege*. https://wiki.facepunch.com/rust/the_tool_cupboard. Accessed 2026-10-08.
- [3] **Facepunch Wiki** — *Rust+ Server*. https://wiki.facepunch.com/rust/rust-companion-server. Accessed 2026-10-08.
- [4] **Facepunch Wiki** — *Server Gamemodes*. https://wiki.facepunch.com/rust/server-gamemodes. Accessed 2026-10-08.
- [5] **Facepunch Wiki** — *Creating a server*. https://wiki.facepunch.com/rust/Creating-a-server. Accessed 2026-10-08.
- [6] **Facepunch** — *Livestock Update* (1 October 2026). https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [7] **Facepunch** — *Spring Clean* (2 April 2026). https://rust.facepunch.com/news/spring-clean. Accessed 2026-10-08.
- [8] **Facepunch** — *Shipshape* (5 March 2026). https://rust.facepunch.com/news/shipshape. Accessed 2026-10-08.
- [9] **Facepunch** — *Harder Core* (7 August 2025). https://rust.facepunch.com/news/harder-core. Accessed 2026-10-08.
- [10] **Facepunch** — *Maintenance* (4 September 2025). https://rust.facepunch.com/news/maintenance. Accessed 2026-10-08.
- [11] **Facepunch Wiki** — *Server Browser Tags*. https://wiki.facepunch.com/rust/server-browser-tags. Accessed 2026-10-08.

**Community & Practitioner Evidence**

None cited in this version.

**Further Reading**

- Facepunch wiki index: https://wiki.facepunch.com/rust/

# Further Reading

The Facepunch wiki server pages (Creating a server, Server Wipe Timer, Centralized Banning) and the news index at https://rust.facepunch.com/news.

# Related Documents

- rust-server-administration-foundation
- rust-game-mechanics-foundation
- rust-items-crafting-foundation
- rust-building-raiding-foundation
- rust-modding-plugins-foundation
- rust-updates-meta-foundation
- rust-combat-damage-model
- rust-weapons-ammo
- rust-raiding-costs-defence
- rust-plugin-development-hooks
- rust-update-timeline-2026

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
