---
id: rust-teams-clans
title: "Rust Teams and Clans"
version: 1.0.0
status: frozen
confidence: Low
category: Game Mechanics
topic: "Teams, clans and social systems"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-game-mechanics-foundation, rust-game-modes, rust-server-convars-reference, rust-turrets-deployables, rust-raiding-costs-defence, rust-update-timeline-2026, rust-moderation-anti-cheat, rust-building-raiding-foundation]
tags: [teams, clans, clan-table, authorization, tool-cupboard, softcore, maxteamsize, chat]
game_build_checked: "October 2026 update (Livestock Update, 1 Oct 2026); pages read on 2026-10-08. Clan data is from the Common Ground update (2 Jul 2026) and community write-ups, not re-verified in-game."
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-teams-clans |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Low |
| Category | Game Mechanics |
| Region | Global |
| Game build checked | October 2026 update (Livestock, 1 Oct 2026); Common Ground (2 Jul 2026) for clans |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

Rust has two social grouping systems: the long-standing team, and the clan system added by the Common Ground update on 2 July 2026. Facepunch documents how teams are created and what they share, and its softcore post gives the only Facepunch-stated team cap (4, which also bounds Tool Cupboard and Autoturret authorisation in that mode). Facepunch's Common Ground post describes clans, the Clan Table, a clan chat channel and the hardcore exclusion [1][2][3].

Most numbers that players ask about are not in a Facepunch source I could open. The default vanilla team size, the clan member cap, clan permissions and cross-server behaviour come only from community write-ups. Document confidence is therefore Low.

# Key Facts

- Teams are created from a button at the bottom left of the inventory screen, invited by pressing E near a player, and accepted via "join team". Members see each other on the map, share markers and have team chat [2].
- Softcore servers cap teams at 4, and Facepunch states this includes the number of people who can authorise at a Tool Cupboard or on an Autoturret (softcore launch post, 4 Feb 2021) [1].
- Clans are described by Facepunch as "a more advanced version of teams where you can have more members with different roles/permissions", with a separate chat channel and announcement text, managed at Clan Tables [3].
- The clan system is disabled in hardcore mode [3].
- Tool Cupboard authorisation is per player: the placer is authorised automatically and others press E at the cupboard [4].
- Two community guides give a default team size of 8; one names the convar `relationshipmanager.maxteamsize` (0 disables teams). Facepunch's Server Gamemodes wiki also names that convar for changing the maximum team and auth size under Softcore settings [10]; the Teams and Useful Commands wiki pages state neither the convar nor a default team size [9][6][2].
- A community guide gives a clan cap of 100 and a convar `clan.maxmembercount` defaulting to 100; this is not Facepunch-confirmed [7].

# Scope

Covers PC (Steam) Rust: team creation and limits, clan features, sharing and authorisation of cupboards, locks and turrets, team and clan chat, and server-level group-size limits as Facepunch documents them. Console is excluded. Build checked: October 2026 update. Plugin-based clan systems (Oxide and Carbon) and admin group-limit rules are mentioned only to flag that they can override native behaviour. Mode differences are in rust-game-modes and convars in rust-server-convars-reference.

# Definitions

- **Team:** the in-game party of players created from the inventory screen [2].
- **Clan:** the Common Ground clan system, managed at a Clan Table [3].
- **Clan Table:** the deployable at which clans are created and managed [3].
- **Group limit:** a server rule capping how many players may play together; an admin policy, not a Facepunch-documented game rule [6].

# Core Mechanics

**Teams.** Create a team with the button at the bottom left of the inventory. Invite by standing near a player until the "invite to team" prompt shows and pressing E. The invitee accepts with "join team". Members see each other on the map, share markers and chat in team chat. Team chat shares a location with global text chat and Tab switches between them. The wiki page states no size limit and does not mention voice [2].

**Softcore team cap.** Softcore launched on 4 Feb 2021 with a maximum team size of 4, which Facepunch says includes the number of people who can authorise at a Tool Cupboard or on an Autoturret [1]. The Common Ground post does not restate this value [3].

**Authorisation.** Whoever places a Tool Cupboard is authorised automatically, and others walk up and press E. An authorised player can deauthorise themselves by holding E, and anyone with access can clear the whole list. Authorisation grants building and pickup within the radius and access to privilege-gated traps [4]. A community guide adds that turrets keep their own authorisation list, that teammates are not authorised automatically, and that code locks are shared by entering the placer's code once, with a separate guest code [6]. The Facepunch Code Lock page opened here says only that it is an electronic lock with a four-digit code [5].

**Clans.** Per the Common Ground post, clans allow more members than teams, with roles and permissions, a separate clan chat channel and announcement text. They are created and managed at Clan Tables, clan names appear on nameplates, and nearby members' locations show on the map [3]. Community guide detail written before launch (June 2026): ranks are customisable with permissions including Set MOTD, Edit Banner, Access Logs, Invite, Kick, Promote and Demote; rank changes and invites need the player to be in range of a Clan Table; Clan Tables are at the Outpost and Bandit Camp and are craftable after researching at a Level 1 Workbench; clans are said to span servers and survive map wipes [7].

**Voice and chat.** The Facepunch wiki chat page could not be opened (404). The Common Ground changelog mentions voice-chat delay and computer-station voice fixes, and a fix for inviting players to a party in the in-game friends list [3]. No Facepunch source opened documents proximity or team voice rules.

# Reference Data

| Item | Value | Build / date | Source |
|------|-------|--------------|--------|
| Softcore max team size | 4, includes TC and Autoturret authorisers | Softcore launch, 4 Feb 2021 | [1] |
| Vanilla default max team size | 8 (two independent community guides; no Facepunch value found) | Guides dated 5 Mar and 11 Jun 2026 | [9][6] |
| Team size convar | `relationshipmanager.maxteamsize` (full name with prefix; convar name confirmed on the Facepunch Server Gamemodes wiki under Softcore settings [10]; 0 disables teams per the guide [9]) | Guide dated 5 Mar 2026; Facepunch wiki | [9][10] |
| Clan member cap | 100 (community claim) | Guide 28-30 Jun 2026 | [7] |
| Clan convar | `clan.maxmembercount`, default 100, local backend only (community claim) | Guide 28-30 Jun 2026 | [7] |
| Clan system in hardcore | Disabled | Common Ground, 2 Jul 2026 | [3] |
| Clan creation cost | Not stated | Guide 28-30 Jun 2026 | [7] |
| TC authorisation limit | Not stated on the wiki page | Oct 2026 | [4] |

# Version & Patch Notes

- 4 Feb 2021, Softcore update: team cap of 4 on softcore, including TC and Autoturret authorisation [1].
- 2 Jul 2026, Common Ground: clan system and Clan Tables added, disabled in hardcore, with changelog fixes for party invites and voice chat [3].
- Values are volatile. Rust rebalances monthly and no Facepunch post opened here restates team size after Common Ground [3].

# Common Pitfalls

- Assuming teammates are authorised on cupboards, turrets and locks. They are not [4][6].
- Treating community clan numbers (100 members, cross-server) as official. One community article notes Facepunch's own notes do not address cross-server persistence [8].
- Expecting clans in hardcore [3].

# Interactions & Related Systems

- Mode rules: the softcore cap and hardcore clan exclusion are in rust-game-modes [1][3].
- Convars: see rust-server-convars-reference for the team size convar, which lists the softcore value of 4 [1].
- Raiding and Tool Cupboards: Common Ground raid blocking depends on Tool Cupboards, covered in rust-raiding-costs-defence and rust-building-raiding-foundation [3].
- Turrets: authorisation lists are covered in rust-turrets-deployables [1].

# Assessed Guidance

## Guidance 1 — Authorise teammates on every device separately

- **Guidance:** After forming a team, authorise each teammate on the cupboard, each turret and each lock; do not rely on team membership.
- **Evidence basis:** Tool Cupboard authorisation is by pressing E [4]; Facepunch ties softcore team size to TC and turret authorisation [1]; community guide on turret and lock lists [6].
- **Confidence:** Medium. The cupboard rule is Facepunch-documented while the turret and lock detail is community.
- **So what:** Missing one turret can mean your own teammate is shot.

## Guidance 2 — Verify team and clan caps in-game before relying on them

- **Guidance:** Treat 8 (team) and 100 (clan) as unconfirmed and test on the target server, especially if it runs a clan plugin.
- **Evidence basis:** Values come only from community sources [6][7]; Facepunch gives only the softcore value of 4 [1].
- **Confidence:** Low. Single community sources, one written before launch.
- **So what:** Admins should read the actual convar rather than quote a guide.

# Open Questions

- Vanilla default team size (8): community-sourced only [9][6]. The convar name `relationshipmanager.maxteamsize` is confirmed on Facepunch's Server Gamemodes wiki (Softcore settings) [10], but the Teams, Useful Commands and Common Ground pages state no default. Confirm the default with the in-game console.
- Clan member cap, convar semantics, roles and cross-server persistence: the Common Ground post (rechecked 2026-10-08) names roles and permissions but gives no cap, rank names, convars or cross-server behaviour [3]. A search found no source for the `clan.maxmembercount` name beyond [7]; treat it as unverified.
- Whether softcore team size is still 4 after Common Ground [3].
- Proximity, team voice and clan chat rules: the Facepunch Chat wiki page was unreachable.
- Whether the TC authorisation list has a numeric cap in vanilla [4].
- Whether plugin clan systems override native team caps: only forum reports seen, not opened.

# References

**Primary Sources**

- [1] **Facepunch** — *Softcore Gamemode Update*. https://rust.facepunch.com/news/softcore-gamemode-update. Accessed 2026-10-08.
- [2] **Facepunch Rust Wiki** — *Teams*. https://wiki.facepunch.com/rust/Teams. Accessed 2026-10-08.
- [3] **Facepunch** — *Common Ground (2 Jul 2026)*. https://rust.facepunch.com/news/common-ground. Accessed 2026-10-08.
- [4] **Facepunch Wiki** — *The Tool Cupboard*. https://wiki.facepunch.com/rust/the_tool_cupboard. Accessed 2026-10-08.
- [5] **Facepunch Wiki** — *Code Lock*. https://wiki.facepunch.com/rust/item/lock.code. Accessed 2026-10-08.
- [10] **Facepunch Wiki** — *Server Gamemodes*. https://wiki.facepunch.com/rust/server-gamemodes. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- [6] **XGamingServer** — *Rust Teams & Clans Guide: Grouping Up and Sleeping Bags* (11 Jun 2026). https://xgamingserver.com/blog/rust-clans-teams-guide/. Accessed 2026-10-08.
- [7] **Corrosion Hour** — *RUST Clan System Guide* (28 Jun 2026, updated 30 Jun). https://www.corrosionhour.com/rust-clan-system-guide/. Accessed 2026-10-08.
- [8] **Guild Order** — *The Clan System and Its Limits* (updated Sept 2026). https://guildorder.com/games/rust/wiki/the-clan-system-and-its-limits. Accessed 2026-10-08.

- [9] **LOW.MS** — *Rust Server Configuration Guide: server.cfg, ConVars, and Settings* (5 Mar 2026). https://www.low.ms/knowledgebase/rust-server-settings-guide. Accessed 2026-10-08.

**Further Reading**

None.

# Further Reading

None beyond the references above.

# Related Documents

- rust-game-mechanics-foundation
- rust-game-modes
- rust-server-convars-reference
- rust-turrets-deployables
- rust-raiding-costs-defence

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft; revision pass added the community-named convar `relationshipmanager.maxteamsize` [9] and recorded rechecked Facepunch gaps. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen at Low confidence after a second research pass; core figures remain community or third-party sourced and are labelled as such. | Auto-approve mandate |
