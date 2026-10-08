---
id: rust-game-modes
title: "Rust Game Modes and Server Types"
version: 1.0.0
status: frozen
confidence: Medium
category: Game Updates & Meta
topic: "Game modes and server types"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-updates-meta-foundation, rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-building-raiding-foundation, rust-server-administration-foundation, rust-modding-plugins-foundation, rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence, rust-server-convars-reference, rust-plugin-development-hooks, rust-update-timeline-2026, rust-monuments-loot, rust-farming-food, rust-vehicles, rust-wipes-map-generation, rust-moderation-anti-cheat, rust-carbon-vs-oxide, rust-electricity-logic, rust-turrets-deployables, rust-wildlife-npcs, rust-server-permissions-rcon, rust-server-performance]
tags: [game-modes, softcore, hardcore, primitive, vanilla, wipe-schedule, server-browser-tags, official-servers, community-servers]
game_build_checked: "October 2026 update (Livestock Update, 1 Oct 2026); mode pages read on 2026-10-08"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-game-modes |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Game Updates & Meta |
| Region | Global |
| Game build checked | October 2026 update (Livestock Update, 1 Oct 2026); mode pages read on 2026-10-08 |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

Rust servers differ along three independent axes: the game mode set by `server.gamemode` (vanilla, softcore, hardcore, primitive, plus test and placeholder modes), the wipe schedule (weekly, biweekly, monthly), and who runs the server (Facepunch or a community operator, with or without Oxide or Carbon). The Facepunch wiki lists the modes and the server browser tag groups; Facepunch devblogs from 2021, 2022, 2025 and July 2026 describe what each mode actually changes [1][2][3][4][5][6].

This answers the foundation's open question about modes beyond softcore and hardcore: the wiki lists primitive and weapontest, and the February 2025 devblog documents Primitive in detail [1][6]. Document confidence is Medium. Mode rules come from primary sources but from posts of different ages, and the current official availability of each mode could not be confirmed.

# Key Facts

- The wiki lists these working modes: vanilla, survival (same as vanilla), softcore, hardcore, weapontest and primitive; deathmatch, teamdm, onedeath, koth_solo and koth_team are marked "Placeholder: not working currently" [1].
- Server browser tags have mutually exclusive groups for wipe schedule (monthly, biweekly, weekly) and difficulty (vanilla, hardcore, softcore) [2].
- Default wipe schedules are monthly (first Thursday), weekly (every Thursday) and biweekly (first and third Thursday), all at 19:00 London time [7].
- Softcore in the Common Ground update (2 Jul 2026) has a 2x gather multiplier and default raid windows of 6 PM to 9 PM server time [5].
- Hardcore (August 2025 rules) hides the map without a compass, forbids crafting and researching firearms, multiplies ammo crafting cost by 5 and doubles upkeep [3].
- Facepunch's server guidelines allow community servers but forbid calling them "official" [8].
- Facepunch said in 2025 that such modes are not expected to stay popular for long, "usually just a couple of months" [3].

# Scope

Covers PC (Steam) Rust: `server.gamemode` modes, server browser tags, wipe schedule tags, and the official versus community versus modded distinction. Console is excluded. Build checked: October 2026 update. Per-mode numbers are stated with the post and date they come from, because most are not re-stated in the October 2026 devblog. Convar defaults and detailed raid maths live in rust-server-convars-reference and rust-raiding-costs-defence and are not restated.

# Definitions

- **Game mode:** the ruleset selected with `server.gamemode` at startup or `gamemode.set` at runtime [1].
- **Vanilla:** the default Rust ruleset; also a tag in the difficulty group [1][2].
- **Raid window:** in softcore, the daily period in which raiding is unrestricted [5].
- **Reclaim terminal:** softcore safezone terminal from which part of a dead player's inventory is recovered [1][4].
- **Server browser tag:** a short code in the server's tag list that the browser filters on [2].

# Core Mechanics

**Selecting a mode.** `server.gamemode <name>` sets the mode in the startup config and `gamemode.set <name>` sets it at runtime. The wiki warns not to switch modes mid-wipe, because this resets all players and their inventory [1].

**Vanilla.** The wiki describes vanilla as "Default Rust gameplay" and says not to set it explicitly; survival is the same ruleset under a different label [1]. The 2021 and 2022 devblogs both state that most servers remained regular vanilla Rust [4][9].

**Softcore.** Described by the wiki as "Vanilla gameplay but with some changes to make the game easier" [1]. At launch (4 Feb 2021): half of a dead player's inventory is recoverable at the death spot or a reclaim terminal at Bandit Town or the Outpost, reclaim items despawn after 2 hours, all players can spawn at either safezone, only a wounded player's contents may be viewed, and maximum team size is 4 [4]. Wiki convars set reclaim fractions: belt 0.5, main 0.5, wear 0 by default [1]. The Common Ground update (2 Jul 2026) added a 2x resource gather multiplier, raid windows (default 6 PM to 9 PM server time, same zone for everyone), and Tool Cupboard raid blocking outside windows, where a cupboard must be at least 1 hour old to block raids. Building blocks and doors cannot be raided outside the window, but deployables and unprotected cupboards can still be attacked. Owners received convars to tune this [5].

**Hardcore.** The wiki describes it as vanilla "with lots of features disabled or limited" [1]. The original post (26 Aug 2022) removed contact system, compass, crawling, global chat, Rust+, team system, map, MLRS and safe zones; added 100 m local chat and a limit of 5 sleeping bags and beds; made blueprints wipe monthly; and launched 10 official servers [9]. The "Harder Core" post (August 2025) said hardcore was returning with changes: fog of war on the map, map position hidden unless a compass is on the belt, firearms cannot be crafted or researched (found weapons can be repaired), ammunition crafting costs up 5x, respawn cooldowns of 15 minutes (sleeping bags) and 10 minutes (beds), and doubled upkeep [3]. The compass item exists in all modes, but the map and UI changes apply only to hardcore [3]. The clan system is disabled in hardcore [5].

**Primitive.** Released with the February 2025 update (article dated 6 Feb 2025), framed as high-tech knowledge being lost. It removes rockets, C4 and the MLRS, metal and armoured building grades and armoured doors, the facemask and metal chest plate, four monuments (Oil Rig, Missile Silo, Excavator, Underwater Labs), the underground train, Scientist NPCs (vendors remain), the patrol helicopter, cargo ship and Bradley events, and the minicopter, scrap transport helicopter and attack helicopter. Sulfur nodes spawn at half rate, tech tree tax is doubled, and wild horse spawns are doubled [6].

**Other modes.** Weapontest is "For test purposes. Made for testing weapon changes" [1].

**Wipe schedule tags.** Monthly, biweekly and weekly are server browser tags; the wiki defines their default times [2][7]. A host can override the day, hour, timezone, a Unix timestamp or a cron expression [7].

**Type tags.** Beyond difficulty, the browser has type tags: pve, roleplay, creative, minigame, training (combat training), battlefield, broyale (battle royale), builds, tut (tutorial) and premium; modding tags are modded, Oxide and Carbon; regions are NA, SA, EU, WA, EA, OC and AF. The wiki advises against several tags from the same group on one server because searches may fail to match [2].

**Official versus community.** Facepunch lets anyone run private, unofficial or community servers, allows monetisation, and instructs operators not to call a server "official" [8]. The 2025 browser changes describe horizontal Play tab server-type tabs starting at "Official", sorting by mode and showing queue sizes [3]. Servers must meet a minimum encryption level to be treated as secure, and insecure servers need the `-insecure` startup parameter [10].

# Reference Data

Values are taken from the posts named in the Source column; the October 2026 devblog was not checked for mode changes.

| Mode | Key differences | Source and date |
|------|-----------------|-----------------|
| vanilla / survival | Default ruleset | Wiki, read 2026-10-08 [1] |
| softcore | 2x gather, raid windows 6-9 PM, team max 4, reclaim fractions 0.5/0.5/0 | [5] Jul 2026; [4] Feb 2021; [1] |
| hardcore | Fog of war, compass-gated map, no firearm crafting, 5x ammo cost, 2x upkeep, no clans | [3] Aug 2025; [5] |
| primitive | No rockets/C4/MLRS, no metal grades, 4 monuments removed, half sulfur | [6] Feb 2025 |
| weapontest | Weapon change testing | [1] |
| deathmatch, teamdm, onedeath, koth_solo, koth_team | Placeholder, not working | [1] |

| Tag group | Values (exclusive where stated) | Source |
|-----------|--------------------------------|--------|
| Wipe schedule (exclusive) | monthly, biweekly, weekly | [2] |
| Difficulty (exclusive) | vanilla, hardcore, softcore | [2] |
| Modding | modded, Oxide, Carbon | [2] |

| Schedule | Default (London time) | Source |
|----------|-----------------------|--------|
| Monthly | First Thursday, 19:00 | [7] |
| Weekly | Every Thursday, 19:00 | [7] |
| Biweekly | First and third Thursday, 19:00; in five-week months the 3-week gap is split 2+1 | [7] |

# Version & Patch Notes

- 4 Feb 2021: Softcore introduced with 10 new servers [4].
- 26 Aug 2022: Hardcore introduced with 10 official servers [9].
- November 2023: wiki states Facepunch shut down its official Hardcore servers and expects no further updates [1].
- 6 Feb 2025: Primitive released [6].
- 7 Aug 2025: Hardcore returns with fog of war and rule changes [3].
- 4 Sep 2025: hardcore tech tree display and map-reveal command fixes; secure encryption minimum of 2 and `-insecure` flag [10].
- 2 Jul 2026: Softcore gather multiplier and raid windows; clans disabled in hardcore [5].
- Volatile: all mode rules; Facepunch states modes tend to be short-lived [3].

# Common Pitfalls

- Switching `server.gamemode` mid-wipe, which resets players and inventory [1].
- Setting several tags from one group, which can break tag searches [2].
- Assuming the wiki's November 2023 hardcore shutdown note is current: the August 2025 devblog says hardcore returned [1][3].
- Assuming softcore raid protection covers everything: deployables and unprotected cupboards remain attackable outside raid windows [5].
- Calling a community server "official" [8].

# Interactions & Related Systems

Mode rules touch many systems: raid windows interact with rust-raiding-costs-defence, hardcore ammo and firearm rules with rust-weapons-ammo, primitive monument and vehicle removals with rust-monuments-loot, rust-vehicles and rust-wildlife-npcs, and wipe tags with rust-wipes-map-generation. Modded servers change rules through Oxide or Carbon (rust-carbon-vs-oxide, rust-plugin-development-hooks); the 2x softcore gather rate is described by Facepunch as working as on modded servers [5]. Mode and convar settings are covered in rust-server-convars-reference. The release cadence is in rust-updates-meta-foundation and rust-update-timeline-2026.

# Assessed Guidance

## Guidance 1 — Read the server's tags and description before assuming any rules

- **Guidance:** Check the difficulty, wipe and modding tags, then the server description, before applying guide numbers to a server.
- **Evidence basis:** Tag groups [2]; mode differences [3][5][6]; softcore multiplier matching modded servers [5].
- **Confidence:** Medium. The tags and modes are documented, but tags are self-declared by operators.
- **So what:** A "vanilla" tagged server may still run plugins, and rates can differ from this KB's vanilla values.

## Guidance 2 — Admins should pick a mode at wipe start and tag accurately

- **Guidance:** Set `server.gamemode` before the first wipe boot, use one tag per group, and avoid "official" in naming.
- **Evidence basis:** Mid-wipe switch warning [1]; tag advice [2]; server guidelines [8].
- **Confidence:** High. All three come directly from Facepunch pages.
- **So what:** Avoids player resets, missed browser matches and delisting risk.

## Guidance 3 — Treat Hardcore and Primitive as temporary experiments

- **Guidance:** Do not plan a long-lived community around a Facepunch experimental mode without a fallback to vanilla.
- **Evidence basis:** "A couple of months" statement and shutdown note [3][1].
- **Confidence:** Medium. It is an inference from Facepunch's stated expectation and one wiki note.
- **So what:** Expect rule changes or removal; recheck the devblog monthly.

# Open Questions

- Whether Facepunch currently runs official softcore, hardcore or primitive servers could not be confirmed; the wiki's 2023 shutdown note conflicts with the 2025 return [1][3].
- The exact softcore raid-window convar names were not found in the sources opened [5].
- Whether the Common Ground update changed softcore team size or reclaim fractions from the 2021 and wiki values is not stated [1][4][5].
- Official weekly, biweekly and monthly rotation naming for Facepunch servers was not found; only the community tag definitions are documented [2][7].
- The 2021 softcore PvP damage reduction mentioned in search snippets was not found on the page opened [4].

# References

**Primary Sources**

- [1] **Facepunch Wiki** — *Server Gamemodes*. https://wiki.facepunch.com/rust/server-gamemodes. Accessed 2026-10-08.
- [2] **Facepunch Rust Wiki** — *Server Browser Tags*. https://wiki.facepunch.com/rust/server-browser-tags. Accessed 2026-10-08.
- [3] **Facepunch** — *Harder Core (August 2025)*. https://rust.facepunch.com/news/harder-core. Accessed 2026-10-08.
- [4] **Facepunch** — *Softcore Gamemode Update (4 Feb 2021)*. https://rust.facepunch.com/news/softcore-gamemode-update. Accessed 2026-10-08.
- [5] **Facepunch** — *Common Ground (2 Jul 2026)*. https://rust.facepunch.com/news/common-ground. Accessed 2026-10-08.
- [6] **Facepunch** — *Primitive (6 Feb 2025)*. https://rust.facepunch.com/news/primitive. Accessed 2026-10-08.
- [7] **Facepunch Rust Wiki** — *Server Wipe Timer*. https://wiki.facepunch.com/rust/server-wipe-timer. Accessed 2026-10-08.
- [8] **Facepunch Studios** — *Server guidelines*. https://facepunch.com/legal/servers. Accessed 2026-10-08.
- [9] **Facepunch** — *Hardcore Gamemode (26 Aug 2022)*. https://rust.facepunch.com/news/hardcore. Accessed 2026-10-08.
- [10] **Facepunch** — *Maintenance (4 Sep 2025)*. https://rust.facepunch.com/news/maintenance. Accessed 2026-10-08.

**Community & Practitioner Evidence**

None.

**Further Reading**

None.

# Further Reading

The wiki server gamemodes and browser tags pages for current lists [1][2].

# Related Documents

- rust-updates-meta-foundation
- rust-update-timeline-2026
- rust-server-convars-reference
- rust-raiding-costs-defence
- rust-wipes-map-generation
- rust-carbon-vs-oxide

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
