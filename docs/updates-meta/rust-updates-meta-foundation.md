---
id: rust-updates-meta-foundation
title: "Rust Updates and Meta: Foundation"
version: 1.0.0
status: frozen
confidence: Medium
category: Game Updates & Meta
topic: "Update cadence and release history"
market: Global
document_type: foundation
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-building-raiding-foundation, rust-server-administration-foundation, rust-modding-plugins-foundation]
tags: [updates, wipe, force-wipe, devblog, branches, staging, game-modes, release-history]
game_build_checked: "October 2026 update (Livestock Update, 1 Oct 2026)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-updates-meta-foundation |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Game Updates & Meta |
| Region | Global |
| Game build checked | October 2026 update (Livestock Update, 1 Oct 2026) |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This document explains how Rust ships updates: a major content update on the first Thursday of each month, announced by a Facepunch devblog, with the official force wipe tied to that release. It covers how to read a devblog, which Steam branches exist for testing, how game modes such as softcore differ from vanilla, platform and licence facts, and a timeline of the eight most recent monthly updates (March to October 2026) read directly from Facepunch.

Document-level confidence is Medium. The monthly cadence and the devblog contents are directly verified from primary Facepunch sources. The exact force-wipe hour, the console edition's current schedule, and the purpose of non-staging branches rest on a community wiki, secondary reporting, or could not be confirmed.

# Key Facts

- Each of the eight monthly devblogs from March to October 2026 is dated the first Thursday of its month [1][2][3][4][5][6][7][8][9].
- The Facepunch wiki states the default wipe schedules (monthly, weekly, biweekly) "align with force wipes" and gives the monthly default as the first Thursday of the month at 19:00 London time [11].
- The latest verified update is the "Livestock Update" of 1 October 2026 [2]; by the same pattern the next would fall on 5 November 2026 *(assessed)*.
- Server owners can test unreleased builds with SteamCMD `app_update 258550 -beta staging` or `-beta aux01` [12].
- Rust left Early Access on 8 February 2018 and is published by Facepunch Studios on Windows and macOS on Steam [13][14].
- Console editions are a separate product developed with Double Eleven, with PS5 and Xbox Series X/S versions released 26 June 2025 [14].
- None of the eight reviewed devblogs explicitly mentions a force wipe [2][3][4][5][6][7][8][9].

# Scope

Covers PC (Steam) Rust: update cadence, devblog reading, branches, game modes and server types at a conceptual level, platform and licence notes, and a recent-update timeline. Build checked: October 2026 update. Console edition is covered only as a separate product. Detailed mechanics, items, base building, server administration and modding live in sibling documents and are not restated.

# Definitions

- **Force wipe:** the monthly Facepunch release after which servers are expected to reset map and progress. The wiki treats default wipe schedules as aligned to it [11].
- **Devblog:** the monthly Facepunch news post on rust.facepunch.com describing an update and its changelist [1].
- **Staging / aux01:** optional Steam beta branches for testing unreleased builds [12].
- **Softcore / hardcore:** game modes referenced in the Common Ground update; softcore has a 2x gather multiplier and raid windows [5].

# Core Mechanics

**Cadence.** The Facepunch news index lists a devblog on the first Thursday of every month from March to October 2026 [1]. Wikipedia reports that after leaving Early Access the update cycle moved from weekly to monthly, citing PC Gamer [14]. The Facepunch wiki gives the default monthly wipe as the first Thursday at 19:00 London time and notes defaults align with force wipes [11].

**Reading a devblog.** Posts are titled with a theme name and dated; the page contains headline features, followed by a changelist (the "Breach and Clear" post is labelled the September Update Changelist, and "Power Trip" gives changelist 4044) [3][4]. Convar names and launch parameters appear inline, for example `vehicle.padrepairsrequired` [2], `antihack.parenthistory` [6], and the opt-in `-useNewNavmesh` parameter [3]. Experimental or opt-in features are flagged in the text, such as the Rust Render Pipeline toggle [2]. Wipe-relevant behaviour is usually stated in terms of "the wipe" rather than a dated force wipe [2][6]. Non-update news posts exist and are not devblogs, for example the Lunar New Year post [10].

**Branches.** The Facepunch wiki says beta branches let you test features not released to the public, using SteamCMD against app ID 258550, with `staging` and `aux01` as the documented examples; moving back requires specifying `public` [12]. The "Shipshape" post mentions data from an "EU Staging server" [9]. The purpose of aux01 beyond testing is not stated in the sources opened.

**Modes and server types.** The "Common Ground" update documents Softcore changes (2x resource gather multiplier, scheduled raid windows defaulting to 6 PM to 9 PM server time with Tool Cupboard raid blocking outside them) and notes the clan system is disabled in hardcore mode [5]. The wiki's server page lists a "Gamemodes" topic under server hosting [15]. Community servers set their own wipe timing; the wiki exposes `wipeDayofWeek`, `wipeHourofDay`, `wipeTimezone` and cron overrides for the in-game wipe timer [11].

**Platform and licence.** Steam lists Facepunch Studios as developer and publisher, with a release date of 8 February 2018 and Windows and macOS support [13]. Early Access began December 2013 and ended 8 February 2018 [14]. The Steam page does not state an Early Access status, only a user tag [13]. Console editions for PS4 and Xbox One launched 21 May 2021 with Double Eleven; PS5 and Xbox Series X/S early access began 19 June 2025 with full release 26 June 2025; the PS4/Xbox One versions were delisted 29 May 2025 and their servers shut in October 2025 [14].

# Reference Data

Verified update timeline (all from Facepunch devblogs, accessed 2026-10-08; build checked is each post itself).

| Date | Update | Headline content | Source |
|------|--------|------------------|--------|
| Thu 5 Mar 2026 | Shipshape | Boat building fixes, Deep Sea changes, longer daylight, Secure server tag | [9] |
| Thu 2 Apr 2026 | Spring Clean | Armoured Ladder Hatch, Water Wheel, tech tree multi-unlock, overfishing, new F1 menu | [8] |
| Thu 7 May 2026 | Upgrade hard, raid harder | Workbench upgrades, Mortar, server browser regions | [7] |
| Thu 4 Jun 2026 | Built Different | New player model, Unity 6 upgrade, new navmesh (opt-in), M16A2 | [6] |
| Thu 2 Jul 2026 | Common Ground | Apartment Complex, Softcore updates, Clan System | [5] |
| Thu 6 Aug 2026 | Power Trip | Power Plant, powerline poles, satellite crash event, new demo UI | [4] |
| Thu 3 Sep 2026 | Breach and Clear | Monument Blockers, upkeep group scaling, HQM node | [3] |
| Thu 1 Oct 2026 | Livestock Update | Cows and sheep, Biofuel Generator, Powergrid loot rooms, Rust Render Pipeline | [2] |

Wipe timer defaults (Facepunch wiki, checked 2026-10-08) [11]:

| Schedule | Default |
|----------|---------|
| Monthly | First Thursday, 19:00 London time [11] |
| Weekly | Every Thursday, 19:00 [11] |
| Biweekly | First and third Thursday [11] |
| Default day / hour / timezone | Thursday (4) / 19 / Europe/London [11] |

# Version & Patch Notes

- Dec 2013: Early Access launch on Steam [14].
- 8 Feb 2018: full release; update cycle moves from weekly to monthly [14].
- 21 May 2021: PS4/Xbox One console release; 26 Jun 2025 PS5/Xbox Series X/S full release [14].
- Jun 2026: Unity 6 upgrade and a new navmesh, disabled by default [6]; Jul 2026: Jobs 3 becomes default, Jobs 2 slated for removal in August [5].
- Aug 2026: SetFlag slated for removal with the September wipe, dated 3 Sep 2026 [4].
- Oct 2026: Rust Render Pipeline toggle available in experimental settings for the first month [2]. Volatile: experimental toggles and opt-in launch parameters change month to month.

# Common Pitfalls

- Treating the wiki's 19:00 London default as the publication time of each update: it is a wipe-timer default, not a statement of when each update is published [11].
- Assuming all servers wipe monthly: the wiki describes weekly and biweekly schedules as ordinary configurations [11].
- Forgetting that Oxide reinstalls are needed after each server update, and that running SteamCMD at startup reverts files to vanilla [12].
- Assuming the Steam store page documents an Early Access phase; it does not [13].
- Assuming console follows the PC cadence; Double Eleven develops it separately [14].

# Interactions & Related Systems

Each monthly update changes systems covered elsewhere: see rust-game-mechanics-foundation, rust-items-crafting-foundation and rust-building-raiding-foundation (for example upkeep group scaling in September [3]), rust-server-administration-foundation (wipe timer and branches [11][12]) and rust-modding-plugins-foundation (deprecations such as SetFlag, community UI components [4], Oxide reinstallation [12]).

# Assessed Guidance

## Guidance 1 — Plan around the first Thursday and re-verify details each month

- **Guidance:** Treat the first Thursday of each month as update and wipe day, and recheck the devblog for that month before relying on any value in this knowledge base.
- **Evidence basis:** Eight consecutive devblogs on first Thursdays [1][2][3][4][5][6][7][8][9]; wiki defaults aligned with force wipes [11].
- **Confidence:** High. The pattern is directly observed in primary sources for eight months and matches the wiki.
- **So what:** Players schedule wipe-day play for the first Thursday; admins plan mod updates the same day.

## Guidance 2 — Admins should pin the branch and expect plugin lag

- **Guidance:** Run the public branch for live servers, use staging or aux01 only on a test server, and delay the wipe-day launch until the framework you use has updated.
- **Evidence basis:** Branch commands and the Oxide reinstall warning [12]; the staging server reference [9].
- **Confidence:** Medium. The commands are documented but the stability of each branch is not stated in the sources opened.
- **So what:** A test server on staging catches plugin breakage before wipe day.

## Guidance 3 — Check the specific mode before quoting rates or rules

- **Guidance:** Do not assume vanilla values apply on softcore or modded servers; verify the mode first.
- **Evidence basis:** Softcore 2x gather and raid windows [5]; wipe timer configurable by hosts [11].
- **Confidence:** Medium. Mode behaviour is documented for softcore only; other modes were not verified.
- **So what:** Guides quoting vanilla numbers can be wrong on community servers.

# Open Questions

- The exact force-wipe hour for the October 2026 update was not confirmed from a Facepunch post; only the wiki default (19:00 London) was seen [11].
- Whether Facepunch publishes a formal definition of every beta branch (aux01 purpose) was not found [12].
- Console Edition's current 2026 update and wipe cadence could not be confirmed from an official source; reporting found was dated 2021 to 2022.
- Official dates for the Early Access start rely on Wikipedia citing PC Gamer [14], not a Facepunch page.
- The next update date (5 November 2026) is an inference from the pattern.

# References

Numbered contiguously from [1].

**Primary Sources**

- [1] **Facepunch** — *Rust news index*. https://rust.facepunch.com/news. Accessed 2026-10-08.
- [2] **Facepunch** — *Livestock Update (1 Oct 2026)*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [3] **Facepunch** — *Breach and Clear (3 Sep 2026)*. https://rust.facepunch.com/news/breach-and-clear. Accessed 2026-10-08.
- [4] **Facepunch** — *Power Trip (6 Aug 2026)*. https://rust.facepunch.com/news/power-trip. Accessed 2026-10-08.
- [5] **Facepunch** — *Common Ground (2 Jul 2026)*. https://rust.facepunch.com/news/common-ground. Accessed 2026-10-08.
- [6] **Facepunch** — *Built Different (4 Jun 2026)*. https://rust.facepunch.com/news/built-different. Accessed 2026-10-08.
- [7] **Facepunch** — *Upgrade hard, raid harder (7 May 2026)*. https://rust.facepunch.com/news/upgrade-hard-raid-harder. Accessed 2026-10-08.
- [8] **Facepunch** — *Spring Clean (2 Apr 2026)*. https://rust.facepunch.com/news/spring-clean. Accessed 2026-10-08.
- [9] **Facepunch** — *Shipshape (5 Mar 2026)*. https://rust.facepunch.com/news/shipshape. Accessed 2026-10-08.
- [10] **Facepunch** — *Lunar New Year 2026*. https://rust.facepunch.com/news/lunar-new-year-2026. Accessed 2026-10-08.
- [11] **Facepunch Rust Wiki** — *Server Wipe Timer*. https://wiki.facepunch.com/rust/Server-Wipe-Timer. Accessed 2026-10-08.
- [12] **Facepunch Rust Wiki** — *Creating a server*. https://wiki.facepunch.com/rust/Creating-a-server. Accessed 2026-10-08.
- [13] **Steam** — *Rust on Steam*. https://store.steampowered.com/app/252490/Rust/. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- [14] **Wikipedia** — *Rust (video game)*. https://en.wikipedia.org/wiki/Rust_(video_game). Accessed 2026-10-08.
- [15] **Facepunch Rust Wiki** — *Rust Wiki home page*. https://wiki.facepunch.com/rust/. Accessed 2026-10-08.

**Further Reading**

None.

# Further Reading

Facepunch news index for the latest devblog [1]; the wiki server-hosting pages for wipe and branch setup [11][12].

# Related Documents

- rust-game-mechanics-foundation
- rust-items-crafting-foundation
- rust-building-raiding-foundation
- rust-server-administration-foundation
- rust-modding-plugins-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, 100% links live). | Auto-approve mandate |
