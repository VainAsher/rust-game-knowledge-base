---
id: rust-server-administration-foundation
title: "Rust Server Administration: Foundation"
version: 1.0.0
status: frozen
confidence: Medium
category: Server Administration
topic: "Dedicated server setup"
market: Global
document_type: foundation
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-building-raiding-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation]
tags: [server, steamcmd, rcon]
game_build_checked: "October 2026 update (Livestock Update, 1 Oct 2026)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-server-administration-foundation |
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

This document is the entry point for running a Rust dedicated server: installing it through SteamCMD, opening ports, choosing launch parameters, using `server.cfg`, generating a map, wiping on schedule, administering through RCON and auth levels, and staying inside Facepunch's server guidelines. It stays at overview depth and points to the Facepunch wiki pages that hold the detail.

Confidence is Medium. Most install, port, wipe and ban facts come from the Facepunch wiki and Facepunch's own guidelines and devblogs, which are primary. However, several wiki pages are old or thin (RCON, convar defaults and anti-cheat configuration are not documented in the pages read), so those areas are stated narrowly and flagged as open questions. Checked against the October 2026 update [8].

# Key Facts

- The Rust dedicated server is Steam app id 258550, installed with SteamCMD using an anonymous login [1].
- The game port is UDP 28015 by default, the query port is UDP and must differ from the game port, and RCON is TCP [1].
- `server.cfg` lives in `rust/server/server.identity/cfg/`, is read at startup, overrides command-line settings, and is never rewritten by the server [1].
- The default wipe schedule is the first Thursday of the month at 19:00 London time, aligned with Facepunch forced wipes [2].
- `ownerid` grants auth level 2 and `moderatorid` grants auth level 1 [7].
- Facepunch's Community Server and Hosting Guidelines (updated 15 July 2025) permit several monetisation methods but forbid granting Facepunch DLC to players who do not own it [3].
- Servers can require TPM 2.0 and Secure Boot; Facepunch reported fewer cheaters on its secure servers [9][8].
- A mandatory server and client update was announced for 22 October 2026 at 18:00 BST [8].

# Scope

Covers vanilla dedicated servers on PC (Windows and Linux) as documented by Facepunch, at overview level, against the October 2026 build. Not covered: console editions, Oxide/Carbon plugin installation (see rust-modding-plugins-foundation), in-game mechanics (rust-game-mechanics-foundation), crafting data (rust-items-crafting-foundation), building and raiding rules (rust-building-raiding-foundation) and patch history (rust-updates-meta-foundation). Hosting-provider panels and third-party tooling are out of scope.

# Definitions

- **SteamCMD** — Valve's command-line Steam client used to download the server files [1].
- **server identity** — a named folder holding one server's saves, config and admin files, so one install can run several servers [5].
- **Auth level** — admin permission tier: 2 owner, 1 moderator [7].
- **RCON** — remote console used to run server commands over the network [1].
- **Forced wipe** — Facepunch's monthly update-day wipe that a new protocol version makes necessary [2][5].

# Core Mechanics

**Install.** The server app id is 258550. The wiki gives the Linux form `./steamcmd.sh +force_install_dir ../rust +login anonymous +app_update 258550 validate +quit`. Omitting `+login` yields "No subscription". Beta branches are installed with `-beta <branch>` (for example `staging`). After testing a higher build, return to the `public` branch or delete the steamapps folder [1].

**Ports.** `server.port` (UDP, default 28015) and `server.queryport` (UDP) must both be open. If `queryport` is unset it defaults to one more than the higher of `server.port` or `rcon.port`, and it must differ from `server.port`. `rcon.port` is TCP and Rust+ also uses a TCP port; RCON and Rust+ ports are needed only if those features are wanted [1].

**Launch parameters and server.cfg.** Common launch arguments are `-batchmode`, `+server.port`, `+server.level "Procedural Map"`, `+server.seed`, `+server.worldsize`, `+server.maxplayers`, `+server.ip`, `+rcon.port`, `+rcon.password`, `+rcon.web 1` and `-logfile`. `server.cfg` takes the same settings without the `+`/`-` prefix, is read at start-up, overrides the command line, and is never edited by the server itself. Some variables (for example weather chance settings) can only be set once the server is running [1]. The command `server.writecfg` writes current convars to the cfg files [7].

**Map generation.** The wiki describes procedural maps with a seed (0 to 2147483647) and world size (the wiki suggests 1000 to 6000; larger maps need more disk and memory) [1]. Procedural maps are saved as `proceduralmap.SIZE.SEED.map` [5]. A JSON file loaded with `+world.configfile` can switch off roads, rivers, powerlines and underwater labs or blacklist/whitelist prefabs; it applies only when a map is first generated, so existing maps need the `.map` file deleted [4].

**Saves and wipes.** The `.sav` file holds entities, buildings and deployables, and the protocol number in its name increases at a forced wipe so the server starts a new file; a blueprint wipe also requires deleting `player.blueprints` [5]. The wipe timer defaults to the first Thursday monthly at 19:00 London time, with weekly and biweekly options, controlled by `wipetimer.wipeDayofWeek`, `wipetimer.wipeHourofDay`, `wipetimer.wipeTimezone`, `wipetimer.wipeUnixTimestampOverride` and `wipetimer.wipeCronOverride`; the `PrintWipe` command shows the calculated schedule [2].

**Administration.** `users` lists players with Steam64 IDs; `ownerid <steamid> "<name>"` and `moderatorid <steamid> "<name>"` grant auth levels 2 and 1; `removeowner` revokes level 2; the player must reconnect to receive the level [1][7]. `kick` and `ban` (with optional duration such as `1M7d5m`) are available to admins [7]. An optional centralized ban list is enabled by pointing `server.bansServerEndpoint` at a self-hosted HTTP API; it blocks joins but does not kick players already online [6].

**Rules and anti-cheat.** Facepunch's guidelines allow a server fee or subscription, donations, cosmetics and enhancements, a server currency, and adverts or sponsorships. Facepunch DLC must be available to players who own it and must not be granted to those who do not; only test servers are excepted. Enforcement can include delisting, other sanctions or a game ban, and cheating, griefing or hacking are prohibited [3]. The guidelines name no specific anti-cheat tool [3]. Facepunch announced that servers can require TPM and Secure Boot [8][9].

# Reference Data

Checked against the October 2026 update [8] unless stated.

| Item | Value | Source |
|------|-------|--------|
| Server app id | 258550 | [1] |
| Game port | `server.port`, UDP, default 28015 | [1] |
| Query port | `server.queryport`, UDP, derived default (28017 with default ports) | [1] |
| RCON port | `rcon.port`, TCP (the wiki table says default equals `server.port`; see Open Questions) | [1] |
| Seed range | 0 to 2147483647 | [1] |
| World size | wiki suggests 1000 to 6000 | [1] |
| Minimum spec (wiki) | 12 GB free RAM, 15 GB free disk, SSD/NVMe preferred | [1] |
| server.cfg path | `rust/server/server.identity/cfg/server.cfg` | [1] |
| users.cfg example | `ownerid 76561198123456789 "TomSmith" ""` | [1] |
| Wipe default | first Thursday, 19:00 London; `wipetimer.wipeDayofWeek` 4, `wipetimer.wipeHourofDay` 19 | [2] |
| Banlist timeout | `server.bansServerTimeout` default 5 seconds | [6] |
| Ban failure mode | `server.bansServerFailureMode` 0 allow, 1 reject | [6] |
| Auth levels | owner = 2, moderator = 1 | [7] |
| Secure-server cheater rate | about 1 in 63 on secure vs 1 in 42 on regular (6-server pool, Apr 2026) | [9] |

# Version & Patch Notes

- 1 October 2026 (Livestock): RCON fix so one disconnect no longer drops other RCON connections; improved console compatibility on Linux and Windows terminals; new fuse-decay and helipad convars; a mandatory server and client update is scheduled for 22 October 2026 at 18:00 BST [8].
- 2 April 2026 (Spring Clean): added convars for RCON and Rust+ connection limits; `UsePlayerUpdateJobs` now defaults to 2; removed `global.legacymonumentnotifications`; Rust Relay is enabled with `-relayenabled`, `-relayurl` and `-relaytoken` [9].
- March 2026: servers gained the ability to require TPM and Secure Boot, as recalled in later posts [8][9].
- 15 July 2025: current Community Server and Hosting Guidelines [3].
- Volatile: convar names and defaults change with monthly updates; the Creating a server wiki page warns that its zip quick-install is from 2015 and that auto-update no longer exists [1].

# Common Pitfalls

- Omitting `+login anonymous` makes SteamCMD fail with "No subscription" [1].
- Running SteamCMD from a startup script reverts Oxide files to vanilla; Oxide must be reinstalled after each update [1].
- The server never writes `server.cfg`, so changes made at runtime are lost unless written with `server.writecfg` [1][7].
- Renaming an old `.sav` to dodge a forced wipe is called dangerous and ill-advised by the wiki [5].
- Map generation settings do not affect an existing map; delete the `.map` file to regenerate [4].
- Banning through the centralized list does not remove players already connected; use `kick` [6].
- Reducing Tier0 topology too far can leave a map with no spawn points [4].

# Interactions & Related Systems

- Plugins and frameworks (Oxide, Carbon) must be reinstalled after updates and are covered in rust-modding-plugins-foundation [1].
- Monthly forced wipes follow Facepunch's update cadence; see rust-updates-meta-foundation [2][8].
- Map seed and size shape monument and terrain layout; see rust-game-mechanics-foundation and rust-building-raiding-foundation for how that affects play [4].
- Server-side convars can alter item and vehicle behaviour, for example helipad repair and fuse decay [8]; see rust-items-crafting-foundation.

# Assessed Guidance

## Guidance 1 — Keep the wipe schedule at its default unless you have a reason

- **Guidance:** Leave the wipe timer on the default first-Thursday 19:00 London schedule and use the override convars only for deliberate off-cycle wipes.
- **Evidence basis:** The wiki says the default aligns with forced wipes and rarely needs changing [2], and the save filename protocol changes at forced wipes [5].
- **Confidence:** High. Both statements are first-party Facepunch documentation.
- **So what:** A schedule that disagrees with the forced wipe invites a mid-cycle wipe or a broken save.

## Guidance 2 — Re-check launch arguments and convars after every monthly update

- **Guidance:** After each update, read the devblog server section and re-test launch arguments and `server.cfg` before opening the server to players.
- **Evidence basis:** Convars were added, changed and removed in consecutive updates [8][9], and the install page flags outdated content [1].
- **Confidence:** Medium. The pattern is documented, but how often a given setting breaks is inference.
- **So what:** Reading the notes avoids silent behaviour changes and covers the announced 22 October mandatory update [8].

## Guidance 3 — Decide monetisation and DLC policy before launch

- **Guidance:** If you sell anything, keep to the listed methods and never unlock Facepunch DLC for non-owners.
- **Evidence basis:** The guidelines list permitted methods and the DLC prohibition, with enforcement up to a game ban [3].
- **Confidence:** High. The source is Facepunch's own legal text, though only the live page is authoritative.
- **So what:** Breaching it risks delisting or bans for the operator.

## Guidance 4 — Weigh secure mode and set a strong RCON password

- **Guidance:** Evaluate TPM and Secure Boot requirements as a cheat deterrent, accepting that a share of players cannot meet them, and never leave the placeholder RCON password.
- **Evidence basis:** Facepunch's figures show fewer cheaters on secure servers but only about 60% of players qualifying [9]; the wiki tells admins to change the RCON password [1].
- **Confidence:** Medium. The cheater figure comes from a six-server sample reported by Facepunch.
- **So what:** Stricter entry trades population for fewer cheaters.

# Open Questions

- The convars that enable secure mode and EAC settings (`server.secure` and similar) were not found on a Facepunch page opened for this document; resolve from the March 2026 devblog or a live server's `find` output.
- The RCON default port: the wiki table says it equals `server.port`, which sits oddly with the separate TCP/UDP description; verify on a running server.
- The Rust+ port number is not stated on the page read.
- A dedicated wiki page for RCON/WebRCON and a full convar list were not located.

# References

**Primary Sources**

- [1] **Facepunch Wiki** — *Creating a server*. https://wiki.facepunch.com/rust/Creating-a-server. Accessed 2026-10-08.
- [2] **Facepunch Wiki** — *Server Wipe Timer*. https://wiki.facepunch.com/rust/server-wipe-timer. Accessed 2026-10-08.
- [3] **Facepunch Studios** — *Community Server and Hosting Guidelines* (updated 15 July 2025). https://facepunch.com/legal/servers. Accessed 2026-10-08.
- [4] **Facepunch Wiki** — *Procedural Generation Customization*. https://wiki.facepunch.com/rust/procedural_generation_customization. Accessed 2026-10-08.
- [5] **Facepunch Wiki** — *Getting started with your rust server*. https://wiki.facepunch.com/rust/Getting-Started_w-Server. Accessed 2026-10-08.
- [6] **Facepunch Wiki** — *Centralized Banning*. https://wiki.facepunch.com/rust/centralized-banning. Accessed 2026-10-08.
- [7] **Facepunch Wiki** — *Useful Console Commands*. https://wiki.facepunch.com/rust/useful_commands. Accessed 2026-10-08.
- [8] **Facepunch** — *Livestock Update* (1 October 2026). https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [9] **Facepunch** — *Spring Clean* (2 April 2026). https://rust.facepunch.com/news/spring-clean. Accessed 2026-10-08.

**Community & Practitioner Evidence**

None cited in this version.

**Further Reading**

- Facepunch wiki index: https://wiki.facepunch.com/rust/

# Further Reading

The Facepunch wiki server-hosting section (custom maps, server browser tags, gamemodes, DNS records, Rust+ server) and the Facepunch news index at https://rust.facepunch.com/news.

# Related Documents

- rust-game-mechanics-foundation
- rust-items-crafting-foundation
- rust-building-raiding-foundation
- rust-modding-plugins-foundation
- rust-updates-meta-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, 100% links live). | Auto-approve mandate |
