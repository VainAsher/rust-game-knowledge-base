---
id: rust-update-timeline-2026
title: "Rust Update Timeline 2026"
version: 1.0.0
status: frozen
confidence: Medium
category: Game Updates & Meta
topic: "2026 update timeline"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-updates-meta-foundation, rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-building-raiding-foundation, rust-server-administration-foundation, rust-modding-plugins-foundation, rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence, rust-server-convars-reference, rust-plugin-development-hooks]
tags: [updates, timeline, devblog, 2026, monthly-update, naval, livestock]
game_build_checked: "October 2026 update (Livestock Update, 1 Oct 2026)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-update-timeline-2026 |
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

This deep-dive lists every 2026 Facepunch update from January to October, month by month, with the release date, the update name and its headline changes, each row cited to the official devblog. It goes beyond the parent foundation by adding January and February 2026 (which the foundation's table omits) and by recording specifics per update such as convars, numbers and deprecations.

Document-level confidence is Medium. Every dated row rests on a primary Facepunch post opened on 2026-10-08. The next-update entry is an inference from the monthly pattern and is labelled as such. The January devblog was read only in part (the last roughly 3,000 characters of the page were not read) [3].

# Key Facts

- Facepunch's 1 January 2026 devblog states the plan for 2026: monthly updates on the first Thursday of each month, with some months planned to have little or no content [3].
- Ten Facepunch posts dated January to October 2026 are devblogs or update posts: Surviving 12 Years (1 Jan), Naval Update (5 Feb), Shipshape (5 Mar), Spring Clean (2 Apr), Upgrade hard, raid harder (7 May), Built Different (4 Jun), Common Ground (2 Jul), Power Trip (6 Aug), Breach and Clear (3 Sep) and Livestock Update (1 Oct) [1][2].
- The Naval Update shipped 5 February 2026 and introduced player-built boats and the Deep Sea [5].
- The Unity 6 upgrade shipped with the 4 June 2026 update [10].
- The Livestock Update of 1 October 2026 is the latest verified update and introduced cows, sheep and the Rust Render Pipeline toggle [14].
- The Livestock devblog states a mandatory server and client update on 22 October 2026 at 18:00 BST (Halloween Update) [14].
- The next first-Thursday update would fall on 5 November 2026 *(assessed inference, not announced)*.

# Scope

Covers PC (Steam) Rust official Facepunch updates dated 1 January to 8 October 2026, taken from the Facepunch news index and devblogs. It lists headline changes only; full changelists are in the linked posts. Community Update 268 is used only for the timing statement it makes. Non-update news posts (for example Lunar New Year, 17 February) are noted but not treated as updates [6]. Console edition and community or modded server schedules are out of scope. Build checked: October 2026 update.

# Definitions

- **Devblog:** a Facepunch news post that describes an update and usually carries a changelist [1].
- **Monthly update:** the Facepunch release planned for the first Thursday of each month [3].
- **Changelist label:** the named changelist inside a post, for example "Naval Cleanup" for Shipshape [7].
- **Inference:** a statement derived from a pattern in cited dates rather than stated by Facepunch.

# Core Mechanics

**Evidence layer.** The 2026 release rhythm, as stated and observed:

- **Stated plan.** The 1 January 2026 devblog sets out monthly updates on the first Thursday of each month plus regular fixes and holiday events, and warns that some months would have little or no content. It also states that servers were wiped as of the new year [3].
- **Observed dates.** The Facepunch news index lists update posts on 5 Feb, 5 Mar, 2 Apr, 7 May, 4 Jun, 2 Jul, 6 Aug, 3 Sep and 1 Oct 2026, each a Thursday and each the first Thursday of its month [1][2]. The 1 January post was itself published on a Thursday and was a recap rather than a content update [3].
- **Pre-announcement.** Community Update 268 (22 January 2026) said the Naval Update was "coming with the February wipe" and invited players to test on the staging branch [4].
- **Mid-month mandatory update.** The Livestock devblog states a Halloween Update on 22 October 2026 as a mandatory server and client update, so not every required update falls on the first Thursday [14].
- **Wipes.** The 1 January post says servers were wiped as of the new year [3]. The March, April, May, June, July, August and October devblogs opened for this document do not state a force-wipe date as such; they describe wipe-relative behaviour (for example the Deep Sea not opening right after a wipe [7]).

# Reference Data

**Evidence layer.** Month-by-month 2026 timeline. Each row was read from the cited Facepunch post on 2026-10-08; the build checked is the post itself.

| Month | Date | Update | Headline changes | Source |
|-------|------|--------|------------------|--------|
| Jan | Thu 1 Jan 2026 | Surviving 12 Years (devblog, 2025 recap) | Recap of 2025 and 2026 plans: monthly first-Thursday updates, Naval update on 5 Feb, apartment complex, new player models, cows and sheep, third-party anticheat layer; changelist 4031 (2025 Recap); servers wiped for the new year | [3] |
| Feb | Thu 5 Feb 2026 | Naval Update | Player-built boats via Boat Building Station, Deep Sea region (building disabled, no respawns, opens and closes intermittently), tropical islands, four floating-city variants, Ghost Ships, PT Boat, new scientist AI, five naval missions, server-performance budgets (ovens 0.25 ms per frame) | [5] |
| Mar | Thu 5 Mar 2026 | Shipshape (Naval Cleanup changelist) | About 20 minutes more daylight, boat-building edit-mode fixes, Deep Sea initial loot fill about 70% of previous, boat decay delay 12 to 24 hours, naval scientist hazmat protection 5% to 30%, `server.useServerWideRequiredSystemConfig` adds a Secure tag (TPM 2.0 and Secure Boot) | [7] |
| Apr | Thu 2 Apr 2026 | Spring Clean (April Quickfire changelist) | Armoured Ladder Hatch, Water Wheel, tech tree multi-unlock, overfishing, new F1 console UI, plant ripeness 14 to 24 hours, `UsePlayerUpdateJobs 2` default, Easter egg hunt to 16 April | [8] |
| May | Thu 7 May 2026 | Upgrade hard, raid harder (May Update changelist) | Nine workbench upgrades, Mortar, Tin Can Alarm throwable rigging, Vending Machine UI refresh, MaxMind-based server browser regions, Windows Server 2019 or Windows 10 21H1 minimum due to Unity 6 | [9] |
| Jun | Thu 4 Jun 2026 | Built Different | New player model and rig, Unity 6 upgrade, M16A2 (loot-only burst rifle), Ballistic Armour and BDU, new navmesh opt-in via `-useNewNavmesh`, `antihack.parenthistory` hit validation, `UsePlayerUpdateJobs 3` savings | [10] |
| Jul | Thu 2 Jul 2026 | Common Ground | Apartment Complex monument with rentable rooms and shops, Softcore changes (2x gather, raid windows default 6 PM to 9 PM), Clan System (disabled in Hardcore), Jobs 3 becomes default | [11] |
| Aug | Thu 6 Aug 2026 | Power Trip | Power Plant and island grid with Heavy Fuses, powerline poles, Satellite Crash event, Dome pumping, balance changes (High Wall upkeep, Blowpipe cost), `UsePlayerUpdateJobs 4` experimental, `SetFlag` slated for removal on 3 Sep, Demo UI 2 via `demo.newui` | [12] |
| Sep | Thu 3 Sep 2026 | Breach and Clear | Monument Blockers, upkeep group scaling (first 4 players untaxed, cap 300%), drone marketplace tied to Power Plant, HQM nodes, Medical Honey Bandage, Attack Heli and Armoured HAB panel armour, BVH physics broadphase | [13] |
| Oct | Thu 1 Oct 2026 | Livestock Update (October Patch) | Cows and sheep with Stable vendor, milk and cream recipes, Biofuel Generator, Powergrid loot rooms at 13 monuments, sandbag rework, Rust Render Pipeline experimental toggle, six more Secure Facepunch servers | [14] |

Other dated 2026 Facepunch posts:

| Date | Post | Content | Source |
|------|------|---------|--------|
| Thu 22 Jan 2026 | Community Update 268 | Naval Update "coming with the February wipe"; staging test invitation; Homebrew 4 Twitch Drops 5 to 15 Feb | [4] |
| Tue 17 Feb 2026 | Lunar New Year 2026 | Year of the Horse items and sale; no update or wipe information | [6] |
| Thu 22 Oct 2026 (announced) | Halloween Update | Mandatory server and client update, 18:00 BST, announced in the Livestock post | [14] |

# Version & Patch Notes

**Evidence layer.** Threads that run across several 2026 updates, each read from the cited posts:

- **Naval line.** Naval Update (5 Feb) [5], then Shipshape fixes and tuning in March (Deep Sea loot, boat decay, scientist armour) [7], then reduced Deep Sea loot and fewer scientist-boat guns in May [9].
- **Server jobs line.** `UsePlayerUpdateJobs 2` default in April [8]; levels 0 and 1 code removed in May, with 3 experimental [9]; Jobs 3 default in July with Jobs 2 deprecated for August removal [11]; Jobs 2 removed and Jobs 4 experimental in August [12].
- **Unity 6.** Windows Server 2016 and Windows 8 dropped in the May post because of the Unity 6 upgrade [9]; the upgrade shipped in the June update [10].
- **Anticheat Secure servers.** Secure tag convars in March [7]; April post reports about 1 in 63 players flagged on Secure servers versus 1 in 42 on regular servers [8]; six more Secure Facepunch servers in October [14].
- **Power grid line.** Power Plant and Heavy Fuses in August [12]; drone marketplace dependence in September [13]; loot rooms and fuse-decay convars in October [14].
- **Navmesh.** Opt-in launch parameter in June [10]; testing on some Facepunch servers in September [13].
- **Volatile.** Experimental toggles (Rust Render Pipeline, `demo.newui`, Jobs 4, new navmesh) change month to month [10][12][13][14].

# Common Pitfalls

- Treating Surviving 12 Years as a content update. Facepunch's own January post is a recap and 2026 plan with a changelist labelled 2025 Recap [3].
- Omitting February. The Naval Update was the first major 2026 content release and is dated 5 February, not March [5]. A table starting at Shipshape misses it [1][7].
- Assuming Lunar New Year (17 February) is a game update. The post lists cosmetic items and a sale and says nothing about an update or wipe [6].
- Assuming every required update lands on the first Thursday. The Halloween Update is announced for 22 October [14].
- A source discrepancy inside Shipshape: Deep Sea network range is given as 620 m in the patch notes and 640 m in the changelog [7]. Quote both rather than choosing.

# Interactions & Related Systems

Each update row changes systems covered in sibling documents. See rust-updates-meta-foundation for cadence and branches (this document deepens it), rust-game-mechanics-foundation and rust-items-crafting-foundation for items and animals (Livestock [14]), rust-building-raiding-foundation and rust-raiding-costs-defence for upkeep, Monument Blockers and the Mortar [9][13], rust-combat-damage-model and rust-weapons-ammo for the M16A2 and armour changes [10][13], rust-server-administration-foundation and rust-server-convars-reference for convars such as `antihack.parenthistory` [10], and rust-modding-plugins-foundation and rust-plugin-development-hooks for `SetFlag` removal and Community UI additions [12]. rust-update-timeline-2026 is a sibling-level reference for all of them.

# Assessed Guidance

## Guidance 1 — Expect the next content update on Thursday 5 November 2026, but confirm it

- **Guidance:** Plan for a monthly update on the first Thursday of November (5 November 2026) after the 22 October Halloween Update, and treat the date as unconfirmed until Facepunch posts it.
- **Evidence basis:** Nine consecutive first-Thursday update posts from February to October [1][2]; the stated monthly plan [3]; the announced 22 October Halloween Update [14].
- **Confidence:** Medium. The pattern is solid, but the January post warned some months may be light and Facepunch has not announced November.
- **So what:** Admins schedule mod and wipe preparation for 5 November while watching the news index, and players treat the date as likely rather than guaranteed.

## Guidance 2 — Read experimental toggles as short-lived

- **Guidance:** Do not build long-term server configuration on features flagged experimental or opt-in in a given month.
- **Evidence basis:** Jobs levels moved from experimental to default within months [9][11][12]; the Rust Render Pipeline toggle is stated to last the first month [14]; the navmesh was opt-in in June and still being tested in September [10][13].
- **Confidence:** Medium. The pattern is documented across several posts, but whether each feature ships is unknown.
- **So what:** Re-check the devblog each month before relying on an experimental convar.

# Open Questions

- Facepunch has not announced a November 2026 update; the 5 November 2026 date is inference only [1][14].
- The last roughly 3,000 characters of the Surviving 12 Years page were not read, so the January changelist may hold further items [3].
- The exact force-wipe hours for each 2026 update were not stated in the devblogs opened; the wiki default is covered in the parent document.
- Whether a 22 October Halloween Update carries a wipe or content beyond the seasonal event is not stated [14]; resolve by reading that post when published.
- Older pages of the news index (page 3 onward) and any Dec 2025 posts were not needed here and were not examined beyond the page 2 listing [2].

# References

Numbered contiguously from [1].

**Primary Sources**

- [1] **Facepunch** — *Rust news index*. https://rust.facepunch.com/news. Accessed 2026-10-08.
- [2] **Facepunch** — *Rust news index, page 2*. https://rust.facepunch.com/news/2. Accessed 2026-10-08.
- [3] **Facepunch** — *Surviving 12 Years (1 Jan 2026)*. https://rust.facepunch.com/news/surviving-12-years. Accessed 2026-10-08.
- [4] **Facepunch** — *Community Update 268 (22 Jan 2026)*. https://rust.facepunch.com/news/community-update-268. Accessed 2026-10-08.
- [5] **Facepunch** — *Naval Update (5 Feb 2026)*. https://rust.facepunch.com/news/naval. Accessed 2026-10-08.
- [6] **Facepunch** — *Lunar New Year 2026 (17 Feb 2026)*. https://rust.facepunch.com/news/lunar-new-year-2026. Accessed 2026-10-08.
- [7] **Facepunch** — *Shipshape (5 Mar 2026)*. https://rust.facepunch.com/news/shipshape. Accessed 2026-10-08.
- [8] **Facepunch** — *Spring Clean (2 Apr 2026)*. https://rust.facepunch.com/news/spring-clean. Accessed 2026-10-08.
- [9] **Facepunch** — *Upgrade hard, raid harder (7 May 2026)*. https://rust.facepunch.com/news/upgrade-hard-raid-harder. Accessed 2026-10-08.
- [10] **Facepunch** — *Built Different (4 Jun 2026)*. https://rust.facepunch.com/news/built-different. Accessed 2026-10-08.
- [11] **Facepunch** — *Common Ground (2 Jul 2026)*. https://rust.facepunch.com/news/common-ground. Accessed 2026-10-08.
- [12] **Facepunch** — *Power Trip (6 Aug 2026)*. https://rust.facepunch.com/news/power-trip. Accessed 2026-10-08.
- [13] **Facepunch** — *Breach and Clear (3 Sep 2026)*. https://rust.facepunch.com/news/breach-and-clear. Accessed 2026-10-08.
- [14] **Facepunch** — *Livestock Update (1 Oct 2026)*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.

**Community & Practitioner Evidence**

None.

**Further Reading**

None.

# Further Reading

The Facepunch news index for the latest devblog [1]; the parent document rust-updates-meta-foundation for cadence, branches and wipe-timer defaults.

# Related Documents

- rust-updates-meta-foundation
- rust-game-mechanics-foundation
- rust-items-crafting-foundation
- rust-building-raiding-foundation
- rust-server-administration-foundation
- rust-modding-plugins-foundation
- rust-combat-damage-model
- rust-weapons-ammo
- rust-raiding-costs-defence
- rust-server-convars-reference
- rust-plugin-development-hooks

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
