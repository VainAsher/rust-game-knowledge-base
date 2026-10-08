---
id: rust-server-permissions-rcon
title: "Rust Server Permissions and RCON"
version: 1.0.0
status: frozen
confidence: Medium
category: Server Administration
topic: "Permissions and RCON"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-server-administration-foundation, rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-building-raiding-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation, rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence, rust-server-convars-reference, rust-plugin-development-hooks, rust-update-timeline-2026, rust-monuments-loot, rust-farming-food, rust-vehicles, rust-wipes-map-generation, rust-moderation-anti-cheat, rust-carbon-vs-oxide, rust-electricity-logic, rust-turrets-deployables, rust-wildlife-npcs, rust-server-performance, rust-game-modes]
tags: [rcon, webrcon, auth-levels, rust-plus, companion-server]
game_build_checked: "October 2026 update (Livestock Update, 1 Oct 2026)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-server-permissions-rcon |
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

This deep-dive goes below the administration foundation on three linked topics: who may run admin commands (auth levels 2 and 1 and the commands that grant them), how remote administration works (RCON, its three launch settings, and the Facepunch websocket client), and how the Rust+ companion server is configured. It does not repeat install, wipe or ban material.

Confidence is Medium. The auth-level commands, RCON setting descriptions and the companion-server page are Facepunch wiki pages and are primary. Two things are weaker: the wiki has no dedicated RCON page, and the April 2026 RCON and Rust+ connection-limit convars are named only in general terms in the devblog. The foundation's open question on the `rcon.port` default is resolved here by two consistent primary statements, but with an inference flagged below. Checked against the October 2026 update [6].

# Key Facts

- `ownerid` grants auth level 2 (highest) and `moderatorid` grants level 1; `removeowner` and `removemoderator` revoke them, and the player must reconnect to receive a change [1][2].
- Admin identities persist in `users.cfg` in the server identity `cfg` folder, edited only while the server is shut down [1].
- `rcon.port` is TCP, `rcon.password` is the shared secret (the wiki says "Change this value!!!"), and `rcon.web` selects the connection method, with the wiki suggesting 1 [1].
- Facepunch's README says web RCON (websocket) is intended to become the default and the old RCON to be removed [5].
- Open question resolved (with inference): the wiki says `rcon.port` defaults to the value of `server.port` (28015) [1], and the companion-server page's default of 28082 is consistent only with an RCON default of 28015 [3] *(assessed inference)*.
- The Rust+ companion port defaults to the higher of game port or RCON port plus 67 (28082 with defaults), must be at least 10000, and `app.port` of -1 (written `+app.port 1-`) disables Rust+ [3].
- Spring Clean (April 2026) added RCON and Rust+ connection-limit convars; Livestock (October 2026) fixed one RCON disconnect dropping other RCON connections [4][6].

# Scope

Covers vanilla dedicated servers on PC: auth levels and the commands that manage them, RCON configuration and security posture, the websocket client, and the Rust+ companion server's settings. Not covered: plugin permission systems such as Oxide or Carbon groups (see rust-modding-plugins-foundation and rust-carbon-vs-oxide), bans and anti-cheat (rust-moderation-anti-cheat), install and ports in general (rust-server-administration-foundation), the full convar catalogue (rust-server-convars-reference) and console editions.

# Definitions

- **Auth level** — admin tier: 2 owner, 1 moderator [2].
- **RCON** — remote console over the network, configured by `rcon.port`, `rcon.password` and `rcon.web` [1].
- **WebRCON** — the websocket form of RCON, enabled with `+rcon.web 1`, with an open-source browser client from Facepunch [5].
- **Companion server** — the server-side endpoint the Rust+ phone app talks to [3].
- **companion.id** — a file holding the server's identity to Rust+ [3].

# Core Mechanics

**Granting and revoking levels.** From the server console (or through RCON), run `users` to find a Steam64 ID, then `ownerid <id> "<name>"` or `moderatorid <id> "<name>"`. The wiki says changes save automatically and the player must reconnect to get the level [1]. `ownerid` makes the player "the highest admin auth level (2)", `moderatorid` the "second highest admin auth level (1)", and `removeowner` and `removemoderator` remove them; all four require admin themselves [2]. For file-based management, `users.cfg` sits in `rust/server/server.identity/cfg/`, one line per admin in the form `ownerid 76561198123456789 "TomSmith" ""`, edited only with the server shut down [1].

**RCON.** The wiki describes three launch settings. `rcon.port` is the port RCON clients connect to for admin control and uses TCP. `rcon.password` sets the remote administration password and carries the warning "Change this value!!!". `rcon.web` sets the remote connect method and the page suggests 1 [1]. Facepunch's `webrcon` project describes itself as game server RCON "using websockets"; for Rust, add `+rcon.web 1` and `+rcon.password <password>` to the launch command [5]. The client runs entirely in the browser with no backend, and saved passwords stay in the browser [5].

**Default port reasoning.** The wiki states `rcon.port` defaults to the same value as `server.port`, and gives 28015 as the `server.port` default [1]. The companion server page states its default is the game port plus 67 or the RCON port plus 67, whichever is higher, which is 28082 if ports are unchanged [3]. 28015 plus 67 is 28082, so an RCON default of 28016 would have produced 28083; the two pages therefore agree.

**Query port consequence.** `server.queryport` defaults to one more than the higher of `server.port` or `rcon.port` [1]. With both at 28015 that formula gives 28016, not the 28017 the foundation's table derived (see Open Questions).

**Rust+ companion server.** `app.info` shows the port and connection settings in use. `app.port` sets the listening port, must be 10000 or higher, and needs a restart. `app.listenip` selects the network interface in complex setups and `app.publicip` overrides the address the app connects to. The TCP port must be reachable from the internet and the server must reach companion-rust.facepunch.com for registration and push notifications [3]. At start-up the server runs a connectivity test; on failure it logs "Rust+ companion server connectivity test failed! Disabling Rust+ features." The test is rate limited to 10 checks per IP every 5 minutes [3]. Rust+ is disabled with `app.port` set to -1, written `+app.port 1-` on the command line because of parser conflicts [3].

**companion.id.** The file is the server's identity to Rust+. It should be kept with backups, never shared, reused on another server or deleted; deleting it generates a new identity that cannot be recovered, and breaking these rules can disable notifications and force players to re-pair [3].

# Reference Data

Checked against the October 2026 update [6] unless noted.

| Item | Value | Source |
|------|-------|--------|
| Owner level | 2, `ownerid <Steam64ID>`; revoke `removeowner` | [2] |
| Moderator level | 1, `moderatorid <Steam64ID>`; revoke `removemoderator` | [2] |
| Listing players | `users` (Steam64 ID and names) | [2] |
| Admin file | `rust/server/server.identity/cfg/users.cfg` | [1] |
| `rcon.port` | TCP; default equals `server.port` (28015) | [1] |
| `rcon.password` | shared secret; wiki says change it | [1] |
| `rcon.web` | connection method; wiki suggests 1 | [1] |
| Web client | Facepunch `webrcon`, MIT licence, browser-only | [5] |
| Companion default port | higher of game or RCON port, plus 67 (28082 default) | [3] |
| Companion minimum port | 10000 | [3] |
| Disable Rust+ | `+app.port 1-` (meaning -1) | [3] |
| Connectivity test rate limit | 10 checks per IP per 5 minutes | [3] |
| Companion host reached | companion-rust.facepunch.com | [3] |
| Other app commands | `app.info`, `app.listenip`, `app.publicip` | [3] |

# Version & Patch Notes

- 1 October 2026 (Livestock): "Fixed RCON disconnect messages sometimes causing other RCON connections to drop out" [6].
- 2 April 2026 (Spring Clean): "Added convars for server owners to configure RCON / Rust+ connection limits." The devblog gives neither names nor defaults [4].
- Volatile: convar names and defaults change monthly, and the companion page's minimum port has been edited between revisions, so read the live page [3].

# Common Pitfalls

- Leaving the placeholder RCON password: the wiki flags it with "Change this value!!!" [1].
- Not reconnecting after `ownerid` or `moderatorid`; the level only applies on a new connection [1].
- Hand-editing `users.cfg` while the server runs; the wiki says to edit it only when shut down [1].
- Setting `app.port` below 10000: the connectivity test fails and Rust+ is disabled [3].
- Running several instances behind one IPv4 address can exhaust the 10-per-5-minutes test limit [3].
- Deleting or copying `companion.id` between servers forces players to re-pair [3].

# Interactions & Related Systems

- Install, ports and ban commands are in rust-server-administration-foundation; the full convar list is in rust-server-convars-reference.
- Plugin frameworks add their own permission layers on top of auth levels; see rust-modding-plugins-foundation, rust-carbon-vs-oxide and rust-plugin-development-hooks.
- Moderation workflow and anti-cheat: rust-moderation-anti-cheat. Server load and connection handling: rust-server-performance.
- Backup guidance for `companion.id` is on the companion page [3]; see also rust-wipes-map-generation.

# Assessed Guidance

## Guidance 1 — Grant owner level sparingly and prefer moderator for staff

- **Guidance:** Give level 2 only to the people who must run every command and use level 1 for routine staff.
- **Evidence basis:** The two levels and their revoke commands are documented [2]; the wiki sets no further tiers [1].
- **Confidence:** Medium. The levels are documented, but which commands each level can use is not stated on the pages read, so the least-privilege reasoning is inference.
- **So what:** Fewer owner accounts means fewer accounts whose compromise hands over the server.

## Guidance 2 — Treat the RCON password as a root credential and use WebRCON deliberately

- **Guidance:** Set a long, unique `rcon.password` before first launch, use `+rcon.web 1`, and restrict who can reach the RCON TCP port at the firewall.
- **Evidence basis:** The wiki warns to change the password and calls the port TCP [1]; Facepunch intends websocket RCON to replace the old protocol [5]; admin commands can be run through RCON [1][2].
- **Confidence:** Medium. The facts are primary but the firewall advice is judgement and the pages say nothing about transport encryption.
- **So what:** An exposed RCON port with a weak password gives an attacker full admin.

## Guidance 3 — Decide on Rust+ explicitly instead of leaving it half-working

- **Guidance:** Either open a TCP companion port of 10000 or higher and keep `companion.id` in backups, or disable Rust+ with `+app.port 1-`.
- **Evidence basis:** Failing the connectivity test disables Rust+ anyway and the identity file rules are listed [3].
- **Confidence:** High. Both options are described on the Facepunch page.
- **So what:** A deliberate choice avoids log errors, re-pairing and wasted ports.

# Open Questions

- Exact names and defaults of the April 2026 RCON and Rust+ connection-limit convars were not on any Facepunch page opened; resolve with the `find rcon` and `find app` console output on a live server.
- The `rcon.port` default is resolved from the wiki statement [1] plus the companion arithmetic [3], but no page states 28015 for RCON directly; confirm on a running server.
- The foundation's reference table gives the query port as 28017 with default ports, while the wiki formula [1] yields 28016 if RCON also defaults to 28015; the foundation's value needs a check on a live server.
- Which commands each auth level may run, and whether RCON clients are limited to a level, were not found on a primary page.
- The wiki has no dedicated RCON page and the websocket URL format is not documented in the pages opened.

# References

**Primary Sources**

- [1] **Facepunch Wiki** — *Creating a server*. https://wiki.facepunch.com/rust/Creating-a-server. Accessed 2026-10-08.
- [2] **Facepunch Wiki** — *Useful Console Commands*. https://wiki.facepunch.com/rust/useful_commands. Accessed 2026-10-08.
- [3] **Facepunch Wiki** — *Rust+ Companion Server*. https://wiki.facepunch.com/rust/rust-companion-server. Accessed 2026-10-08.
- [4] **Facepunch** — *Spring Clean* (2 April 2026). https://rust.facepunch.com/news/spring-clean. Accessed 2026-10-08.
- [5] **Facepunch** — *webrcon* (GitHub README). https://github.com/Facepunch/webrcon. Accessed 2026-10-08.
- [6] **Facepunch** — *Livestock Update* (1 October 2026). https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.

**Community & Practitioner Evidence**

None cited in this version.

**Further Reading**

- Facepunch wiki index: https://wiki.facepunch.com/rust/

# Further Reading

The Facepunch wiki pages above, and the in-game F1 console `find` command for live convar names.

# Related Documents

- rust-server-administration-foundation
- rust-server-convars-reference
- rust-moderation-anti-cheat
- rust-carbon-vs-oxide
- rust-plugin-development-hooks
- rust-server-performance

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
