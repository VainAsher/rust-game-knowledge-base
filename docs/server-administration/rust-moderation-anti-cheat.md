---
id: rust-moderation-anti-cheat
title: "Rust Moderation and Anti-Cheat"
version: 1.0.0
status: frozen
confidence: Medium
category: Server Administration
topic: "Moderation, bans and anti-cheat"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-server-administration-foundation, rust-server-convars-reference, rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-building-raiding-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation, rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence, rust-plugin-development-hooks, rust-update-timeline-2026, rust-monuments-loot, rust-farming-food, rust-vehicles, rust-wipes-map-generation, rust-carbon-vs-oxide]
tags: [moderation, bans, anti-cheat, eac, secure-server, centralized-banning]
game_build_checked: "October 2026 update (Livestock Update, 1 Oct 2026)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-moderation-anti-cheat |
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

This deep-dive covers how a Rust server operator polices a server: the console commands for admins and moderators, local bans, the centralized ban API, the secure-server state as Facepunch describes it, and the cheating clauses of Facepunch's server guidelines. It goes deeper than rust-server-administration-foundation and does not repeat the convar tables in rust-server-convars-reference.

Confidence is Medium. Command, ban API and guideline facts are first-party Facepunch text and are well supported. Facepunch deliberately discloses little about how Easy Anti-Cheat (EAC) detects cheats, so the anti-cheat picture is built from devblog statements only, and the secure-server statistics come from a small sample. Checked against the October 2026 update [9].

# Key Facts

- Admin commands `ban`, `banid`, `unban`, `kick`, `mute`, `moderatorid` and `ownerid` are documented on Facepunch's Useful Console Commands page [2].
- A kick lets the player rejoin immediately; a ban is what prevents rejoining [2].
- Centralized banning checks an HTTP API when a player joins, supports mutes as well as bans, and does not kick players already connected [1].
- Facepunch's guidelines state that cheating, griefing or hacking is strictly prohibited, and breaches can mean delisting, other sanctions or a game ban [3].
- The guidelines do not name EAC or any anti-cheat tool [3]; Facepunch devblogs do name EAC [7][10][11].
- Servers can opt in to requiring TPM and Secure Boot (announced 5 March 2026) [7]; Facepunch reported about 1 in 63 players as cheaters on its secure servers against 1 in 42 on regular servers [8].
- Facepunch reported 338,000+ total bans and 296,000+ permanent bans applied in 2025 [10].
- `server.listplayerreportcounts` lets admins see how many reports players have received (7 August 2025) [5].

# Scope

Covers vanilla Rust dedicated servers on PC: moderator tooling, banning, the centralized ban endpoint, Facepunch's stated secure-server and EAC position, and the guidelines on cheating. Not covered: plugin-based admin tools (see rust-modding-plugins-foundation and rust-plugin-development-hooks), the full convar table for secure servers (see rust-server-convars-reference), in-game combat rules (see rust-combat-damage-model), and any description of how cheats work or how EAC detects them, which Facepunch does not publish. Console editions are excluded.

# Definitions

- **Auth level** — admin tier: owner is level 2, moderator is level 1 [2][4].
- **Centralized banning** — an optional external ban list queried over HTTP at join time [1].
- **EAC** — Easy Anti-Cheat, the anti-cheat partner Facepunch names in its devblogs [10][11].
- **Secure server** — a server that meets Facepunch's secure criteria to appear in the client browser, including a minimum encryption level [6].
- **Secure tag** — browser tag for servers requiring TPM and Secure Boot for all players [7].
- **Premium server** — a Facepunch server that requires a Steam inventory valued at $15 or more [10].

# Core Mechanics

**Granting authority.** Run `users` to find a SteamID, then `ownerid` or `moderatorid`. The player must reconnect to receive the level, and the change saves automatically. Admins can also be written into `users.cfg` in the `server.identity/cfg/` folder, but only while the server is shut down [4]. `removeowner` and `removemoderator` revoke the levels [2].

**Command set.** `ban` takes a Steam64 ID, name, reason and optional duration written like `1M7d5m`; `banid` bans a Steam64 ID even when the player is not on the server; `unban` removes a ban; `bans` and `banlistex` list bans; `kick` removes a player who can rejoin immediately. `mute` and `unmute` act locally for a player and server-wide when used by an admin. `killplayer`, `resetstate`, `combatlog <Steam64ID>`, `players`, `playerlist`, `status` (includes IP address and time played) and `users` support investigations [2].

**Centralized banning.** The operator hosts the web service because Facepunch does not provide one. Setting `server.bansServerEndpoint` makes the server request `GET /api/rustBans/{steamID64}` when a player joins, adding a trailing `/` if the endpoint does not end in `/` or `=`. A 2xx response must carry JSON with `steamId`, `reason`, `expiryDate` (Unix timestamp; zero or negative is permanent) and `isMute`; 404 means not banned; any other status is a failure. `server.bansServerFailureMode` 0 lets players join on failure and 1 rejects them; `server.bansServerTimeout` defaults to 5 seconds. Changing these needs no restart, and bans do not kick connected players, so use `kick` for that [1].

**Guidelines on cheating.** The Community Server and Hosting Guidelines (updated 15 July 2025) say cheating, griefing or hacking is strictly prohibited. Failure to comply may lead to delisting from the server browser or other sanctions, and serious or repeated breach may lead to a game ban. Community servers are at Facepunch's discretion, and the operator is responsible for the server [3]. The guidelines do not mention EAC [3].

**Secure-server state.** On 7 August 2025 Facepunch told operators to use the `-insecure` startup parameter instead of setting `server.secure` false, and added a minimum encryption requirement for appearing in the client browser [5]. On 4 September 2025 the minimum became level 2, which is already the default for dedicated servers, and `server.secure` was slated for removal [6]. On 5 March 2026 servers gained an opt-in requirement for TPM and Secure Boot, which Facepunch said lets EAC work better; servers requiring both for all players get a Secure tag, and per-account requirements use a separate convar without the tag [7]. Convar names and defaults are in rust-server-convars-reference.

# Reference Data

Checked against the October 2026 update [9] unless stated.

| Item | Value | Source |
|------|-------|--------|
| Owner / moderator auth level | 2 / 1 | [2] |
| Ban duration format | e.g. `1M7d5m` | [2] |
| Centralized ban endpoint convar | `server.bansServerEndpoint` | [1] |
| Failure mode | `server.bansServerFailureMode` 0 allow, 1 reject | [1] |
| Timeout | `server.bansServerTimeout`, default 5 s | [1] |
| Ban API 404 | player not banned | [1] |
| Admin report counts | `server.listplayerreportcounts` (added 7 Aug 2025) | [5] |
| Players with TPM hardware | over 80% (5 Mar 2026) | [7] |
| Players with Secure Boot enabled | just under 60% (5 Mar 2026); about 60% have both enabled (2 Apr 2026) | [7][8] |
| Facepunch secure servers at launch | six (EU 3, EU East 3, EU 14, EU Large 2, US West 3, US East 3) | [7] |
| Cheater rate, secure vs regular | about 1 in 63 vs 1 in 42 (Apr 2026, 6-server pool) | [8] |
| Total / permanent bans in 2025 | 338,000+ / 296,000+ | [10] |
| Premium server entry | Steam inventory valued at $15 or more | [10] |
| Bug bounty payout to date | over $300,000 (HackerOne) | [10] |

# Version & Patch Notes

- 16 November 2017 (Devblog 186): a bug in EAC's server code could trap the runtime in a zombie state where it processed no kicks for banned players and did not enable network encryption on new connections [11].
- 7 August 2025 (Harder Core): `-insecure` parameter, new encryption requirement for the browser, `server.listplayerreportcounts`, a flyhack false-kick fix [5].
- 4 September 2025 (Maintenance): minimum encryption level 2 for secure servers; `server.secure` removal [6].
- 1 January 2026 (Surviving 12 Years): 2025 ban totals; EAC efforts against recoil scripting [10].
- 5 March 2026 (Shipshape): opt-in TPM 2.0 and Secure Boot enforcement [7].
- 2 April 2026 (Spring Clean): first secure-server cheater figures; admin-tab mute button, console autocomplete for admins, RCON and Rust+ connection-limit convars [8].
- 1 October 2026 (Livestock): Facepunch ready to move more of its servers to secure mode; fix for EAC blocking crash dumps; RCON disconnect fix [9].
- Volatile: secure-server rollout and adoption figures change with each devblog.

# Common Pitfalls

- Expecting a ban to remove an online player: centralized bans only stop joins, so also run `kick` [1].
- Expecting `kick` to be a sanction: the kicked player can rejoin immediately [2].
- Setting `server.secure false`: Facepunch moved insecure servers to `-insecure` [5][6].
- Assuming the guidelines specify an anti-cheat tool: they do not mention EAC [3].
- Choosing a fail-closed ban API without a fast endpoint: failure mode 1 rejects players when the check fails, and Facepunch advises a fast API over a longer timeout [1].
- Editing `users.cfg` while the server runs: the wiki says that method works only when the server is shut down [4].

# Interactions & Related Systems

- Convars for secure servers, encryption and the Secure tag are tabulated in rust-server-convars-reference; the basics of auth levels and RCON sit in rust-server-administration-foundation [4].
- Plugins can add ban, mute and report workflows, which is covered under rust-modding-plugins-foundation and rust-plugin-development-hooks; the sources here do not describe them.
- Wipe timing and map settings are in rust-wipes-map-generation; patch chronology is in rust-update-timeline-2026 and rust-updates-meta-foundation [9].
- Flyhack detection is a server-side check that Facepunch has tuned (a false-kick fix on roof blocks) [5]; combat rules are in rust-combat-damage-model.

# Assessed Guidance

## Guidance 1 — Pair every ban with a kick and keep a written reason

- **Guidance:** When banning an online player, run the ban and then `kick`, and always supply a reason and duration.
- **Evidence basis:** Bans (including centralized ones) do not remove players already connected, and `kick` is the removal command [1][2]; the ban command accepts a reason and duration [2].
- **Confidence:** High. Both behaviours are stated on first-party wiki pages.
- **So what:** A ban alone can leave the offender playing until they disconnect.

## Guidance 2 — Treat centralized banning as shared infrastructure

- **Guidance:** Only run a centralized ban endpoint that is fast and monitored, and choose the failure mode deliberately.
- **Evidence basis:** The check happens at join time with a 5 second default timeout, failure mode 0 admits and 1 rejects players, and Facepunch advises fast APIs [1].
- **Confidence:** Medium. The mechanics are documented, but which mode suits a given community is a judgement.
- **So what:** Fail-open keeps a server joinable but lets banned players in during an outage; fail-closed does the reverse.

## Guidance 3 — Do not rely on secure mode alone to stop cheating

- **Guidance:** Treat TPM and Secure Boot enforcement as one deterrent alongside active moderation and reporting, and weigh the population cost.
- **Evidence basis:** Facepunch measured about 1 in 63 cheaters on secure servers against 1 in 42 on regular ones from only six servers, and said about 60% of players have the required features [8]; it described the effect as less than premium servers [8].
- **Confidence:** Medium. Primary source, but a small sample and an operator's own outcomes may differ.
- **So what:** Secure servers have fewer cheaters, not none, and fewer eligible players.

## Guidance 4 — Write your own rules with the guidelines in mind

- **Guidance:** Publish server rules that match the guidelines' prohibition on cheating, griefing and hacking, and do not present your server as official.
- **Evidence basis:** The guidelines prohibit them, make operators responsible for their servers, and allow delisting, sanctions or a game ban [3].
- **Confidence:** High. This restates Facepunch's own text; whether a rule suits your community is up to you.
- **So what:** Clear rules help justify bans and reduce exposure to sanctions.

# Open Questions

- The EAC-side configuration available to a server operator is not documented on any Facepunch page opened; Facepunch says it does not disclose anti-cheat methods in detail. A live server `find` output would show current convars.
- Harder Core refers to `secure.encryption` at least 1 while Maintenance refers to `server.encryption` 2; the naming difference is unexplained in the pages read, so confirm on a live server [5][6].
- Whether the Livestock plan to add more Facepunch secure servers has taken effect, and which servers, is not stated [9].
- Surviving 12 Years mentions a planned third-party anti-cheat layer that Facepunch has not detailed; the last 3,106 characters of that page were not read [10].
- The Centralized Banning wiki page gives no release date or version [1].
- No Facepunch source opened lists a ban appeals process; the Terms of Service were not opened.

# References

**Primary Sources**

- [1] **Facepunch Wiki** — *Centralized Banning*. https://wiki.facepunch.com/rust/centralized-banning. Accessed 2026-10-08.
- [2] **Facepunch Wiki** — *Useful Console Commands*. https://wiki.facepunch.com/rust/useful_commands. Accessed 2026-10-08.
- [3] **Facepunch Studios** — *Community Server and Hosting Guidelines* (updated 15 July 2025). https://facepunch.com/legal/servers. Accessed 2026-10-08.
- [4] **Facepunch Wiki** — *Creating a server*. https://wiki.facepunch.com/rust/Creating-a-server. Accessed 2026-10-08.
- [5] **Facepunch** — *Harder Core* (7 August 2025). https://rust.facepunch.com/news/harder-core. Accessed 2026-10-08.
- [6] **Facepunch** — *Maintenance* (4 September 2025). https://rust.facepunch.com/news/maintenance. Accessed 2026-10-08.
- [7] **Facepunch** — *Shipshape* (5 March 2026). https://rust.facepunch.com/news/shipshape. Accessed 2026-10-08.
- [8] **Facepunch** — *Spring Clean* (2 April 2026). https://rust.facepunch.com/news/spring-clean. Accessed 2026-10-08.
- [9] **Facepunch** — *Livestock Update* (1 October 2026). https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [10] **Facepunch** — *Surviving 12 Years* (1 January 2026). https://rust.facepunch.com/news/surviving-12-years. Accessed 2026-10-08.
- [11] **Facepunch** — *Devblog 186* (16 November 2017). https://rust.facepunch.com/news/devblog-186. Accessed 2026-10-08.

**Community & Practitioner Evidence**

None cited in this version.

**Further Reading**

- Facepunch news index: https://rust.facepunch.com/news

# Further Reading

The Facepunch news index at https://rust.facepunch.com/news for future anti-cheat posts, and the Facepunch wiki index at https://wiki.facepunch.com/rust/.

# Related Documents

- rust-server-administration-foundation
- rust-server-convars-reference
- rust-modding-plugins-foundation
- rust-plugin-development-hooks
- rust-update-timeline-2026
- rust-wipes-map-generation
- rust-combat-damage-model

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
