---
id: rust-building-raiding-foundation
title: "Rust Building and Raiding: Foundation"
version: 1.0.0
status: frozen
confidence: Medium
category: Building & Raiding
topic: "Building system, upkeep and raiding"
market: Global
document_type: foundation
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-server-administration-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation]
tags: [building, tool-cupboard, upkeep, decay, raiding, locks, explosives]
game_build_checked: "Livestock Update, 1 October 2026"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-building-raiding-foundation |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Building & Raiding |
| Region | Global |
| Game build checked | Livestock Update, 1 October 2026 [1] |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This document gives an overview of how bases work in Rust: the Tool Cupboard (TC) and building privilege, upkeep and decay, doors and locks, a short tour of deployables, and the fundamentals of raiding with explosives and siege tools. It is a foundation: it explains the shape of the systems and points to deeper documents rather than listing every value.

The headline is that a base must be kept supplied through its TC or it decays, that the monthly updates keep changing the upkeep rules (a group upkeep tax arrived in September 2026), and that raid costs change with balance passes. Confidence is Medium: the mechanics come from the Facepunch wiki and devblogs, but the wiki's Tool Cupboard page is undated, hit-point tables were not obtainable from an openable source, and offline-raiding behaviour could not be sourced.

# Key Facts

- A Tool Cupboard costs 1000 wood to craft; without one a base decays and other players can build on it [2].
- Upkeep is a per-24-hour payment drawn from the TC inventory; with no resources in the TC, decay begins immediately [2].
- The wiki lists decay timers after the matching material runs out: twig 1 hour, wood 3 hours, stone 5 hours, metal 8 hours, armoured 12 hours (wiki page undated; check in game) [2].
- From the September 2026 update, TCs add a group upkeep tax: the first 4 players pay none, the next 6 add 2% each, later players 4% each, capped at 300% [3].
- Code locks use a four-digit code and cost 100 metal fragments; key locks cost 75 wood [4][5].
- A Timed Explosive Charge (C4) is crafted from 20 explosives, 5 cloth and 2 tech trash at Workbench Level 3 [6].
- The latest update checked, the Livestock Update (1 October 2026), made no upkeep change but fixed a battering ram bug that hit TCs through walls [1].

# Scope

Covered: building tiers as terminology and decay tiers, the TC and building privilege, upkeep and decay, doors and locks, a deployables overview, and raiding fundamentals at overview level. Vanilla PC Rust on the build named above; modded servers and console are excluded. Not covered: per-structure hit points, full raid-cost tables, base design theory, and server convar tuning (see the sibling documents).

# Definitions

- **Tool Cupboard (TC):** the deployable that grants building privilege and holds upkeep resources [2].
- **Building privilege:** authorisation to build and pick up deployables within the TC area [2].
- **Upkeep:** the periodic resource payment, a fraction of build cost, drawn from the TC [2].
- **Honeycomb:** multiple layers of walls placed to make raiding through that side more expensive [7].
- **Airlock:** two or more opposing doors within a single foundation [7].
- **Footprint:** the layout of a base's foundations [7].

# Core Mechanics

**Building privilege.** Placing a TC authorises the placer. Authorised players can build and pick up deployables in the radius and can set off flame and shotgun traps; others press E at the TC to authorise, and an authorised player can deauthorise by holding E. Anyone with access can hold E to clear every authorised player [2]. The privilege area is projected from the connected foundations, not from the TC position [2]. Unauthorised players can still place twig floors and wooden ladders, shown as an orange "BUILDING BLOCKED" outline; other placements show red [2]. Separate buildings each need their own TC coverage [2].

**Upkeep.** Upkeep is a per-24-hour payment, a fraction of the build cost, taken from the TC inventory. Walls, foundations, ceilings, roofs, doors and window pieces contribute; items inside the base such as sleeping bags do not. A stone base with sheet metal doors consumes only stone and metal fragments. Remaining protection time shows in the TC inventory [2]. High external walls add no upkeep and are protected within a TC's radius; small "external" TCs can cover walls outside the main radius [2].

**Decay.** Once a material runs out in the TC, parts made of it decay: twig after 1 hour, wood 3 hours, stone 5 hours, metal 8 hours, armoured 12 hours. Decay starts at the outermost exposed layers and works inward, and only parts of the exhausted material decay [2]. A destroyed TC holding resources consumes up to 24 hours of upkeep, protecting the base for 24 hours from that point [2].

**Group upkeep tax.** Since the September 2026 update, TCs add an upkeep tax based on the number of players in the base. Counted players are those authorised on the TC or a code lock (guest codes included) plus those deauthorised from either in the last 24 hours. Server owners can adjust or disable it through ConVars in the Decay class [3].

**Doors and locks.** The code lock opens with a four-digit code [4]. The key lock is placed on a door and keys can be shared with friends [5]. The armoured door is described as an extremely strong door with a hatch to see and shoot out of [8]. Doors are one input to base design alongside honeycomb and airlock layouts [7].

**Deployables overview.** The Facepunch wiki groups base-related items as doors and locks, barricades, walls and windows, and raiding tools [9]. The Livestock Update added animal gates and fences and allowed Smart Alarms to sit on other deployables [1]. The Tin Can Alarm can be rigged with grenades and similar items, and the Mortar was added as a raiding and anti-personnel deployable in May 2026 [10].

**Raiding fundamentals.** The wiki lists the satchel charge, timed explosive charge, explosives, beancan and F1 grenades, battering ram, siege tower, catapult and cannon as raiding items [9]. The satchel charge is described as useful for destroying wood and sheet metal doors [11]. The battering ram is a siege weapon for breaking through wooden and stone structures and must be repaired with high quality metal to keep functioning [12]. The Mortar fires shells of two types, one aimed at players and one at structures, fired without a visual guide [10]. Parts of a base whose TC has run dry decay on the timers above, which makes neglected bases weaker targets [2].

**Offline considerations.** The Tool Cupboard wiki page does not address offline behaviour [2]. Upkeep is a per-24-hour payment drawn from the TC, so stocked resources are what protect a base from decay; the page does not tie this to whether owners are online [2]. No Facepunch source on offline raid protection was opened for this document; see Open Questions.

# Reference Data

Values below were checked against the Facepunch wiki on 2026-10-08, alongside the Livestock Update (1 October 2026) [1]. Wiki pages are undated, so treat costs as volatile.

| Item | Cost or value | Workbench | Source |
|------|---------------|-----------|--------|
| Tool Cupboard | 1000 wood | not stated | [2] |
| Building Plan | 20 wood | none | [13] |
| Code Lock | 100 metal fragments | none | [4] |
| Key Lock | 75 wood | none | [5] |
| Armoured Door | 20 HQM, 5 gears | Level 3 | [8] |
| Satchel Charge | 4 beancan grenades, 1 rope, 1 small stash | Level 1 | [11] |
| Timed Explosive Charge | 20 explosives, 5 cloth, 2 tech trash | Level 3 | [6] |
| Battering Ram | 500 wood, 100 HQM, 2 sheet metal, 1 tarp | Level 2 | [12] |

| Decay stage | Time after material exhausted | Source |
|-------------|------------------------------|--------|
| Twig | 1 hour | [2] |
| Wood | 3 hours | [2] |
| Stone | 5 hours | [2] |
| Metal | 8 hours | [2] |
| Armoured | 12 hours | [2] |

| Group upkeep tax (September 2026) | Value | Source |
|-----------------------------------|-------|--------|
| Players with no tax | first 4 | [3] |
| Players 5 to 10 | +2% each | [3] |
| Players beyond 10 | +4% each | [3] |
| Cap | 300% | [3] |
| Example: 6 players / 12 players | +4% / +20% | [3] |

| Server convar | Default | Meaning | Source |
|---------------|---------|---------|--------|
| decay.scale | 1 | Multiplies decay rate; 0 stops decay | [15] |
| decay.upkeep | true | Whether TCs consume upkeep resources | [15] |

The convar source states no game version, so verify these in the live server console [15].

# Version & Patch Notes

- **May 2026, "Upgrade hard, raid harder" (7 May):** added the Mortar, made the Tin Can Alarm riggable, fixed an exploit that let explosives pass through walls and an authorisation override on destroyed TCs in Softcore [10].
- **June 2026, "Built Different" (4 June):** fixed mortars firing through walls and deployables and a battering ram null reference error [14].
- **September 2026, "Breach and Clear" (3 September):** introduced the group upkeep tax, monument blockers, reduced grenade stacks (F1, Bee, Molotov, Flashbang to 3; Beancan to 4), and let unlocked garage doors be picked up without building privilege [3].
- **October 2026, Livestock Update (1 October):** client prediction for grenades, C4 and satchels, a fix for a battering ram bug hitting TCs through walls, and fixes to triangle foundation connections and door controllers on upgraded gates [1].
- Volatile: raid-related items, explosive stack sizes and upkeep rules were each touched within the last five monthly updates [1][3][10][14].

# Common Pitfalls

- Treating the Tool Cupboard radius as a circle around the TC; the wiki says it is projected from connected foundations [2].
- Forgetting that separate buildings need separate TC coverage [2].
- Placing high external walls beyond TC range; wiki advice is to use external TCs so players cannot build just outside the radius [2].
- Assuming group size is free: guest code holders and recently deauthorised players still count toward the tax for 24 hours [3].
- Assuming fixed wiki upkeep figures hold; the Tool Cupboard page is marked as updated "A Long Time Ago" [2].

# Interactions & Related Systems

- Crafting costs, workbench levels and recycler yields: see rust-items-crafting-foundation (research and recycling are shown for each item on the wiki [4][11]).
- Core survival, combat and monument systems: see rust-game-mechanics-foundation (monument blockers appeared in September 2026 [3]).
- Decay and upkeep convars, group tax settings: see rust-server-administration-foundation [3][15].
- Plugin-driven raid or building rules on modded servers: see rust-modding-plugins-foundation.
- Monthly balance changes: see rust-updates-meta-foundation [1][3].

# Assessed Guidance

## Guidance 1 — Keep the TC stocked for the material that decays first

- **Guidance:** Stock the TC with more than enough of every material your base uses, prioritising the lowest tier present, because each tier begins to decay on its own timer once its material runs out.
- **Evidence basis:** Upkeep is drawn from the TC and the per-tier decay timers are documented [2].
- **Confidence:** Medium. The wiki page is official but undated, and the upkeep rules changed in September 2026 [3].
- **So what:** Check the TC protection timer in game after each monthly update rather than trusting remembered numbers.

## Guidance 2 — Budget for the group upkeep tax before adding teammates

- **Guidance:** Keep the authorised and code-lock player count low, and remove stale guest codes, to avoid a larger upkeep bill.
- **Evidence basis:** The tax is based on players authorised on the TC or a code lock plus those deauthorised in the last 24 hours [3].
- **Confidence:** High. This comes directly from the Facepunch devblog, though server owners may change it [3].
- **So what:** On an unfamiliar server, ask whether the Decay ConVars were changed.

## Guidance 3 — Expect raid costs to drift and verify before planning

- **Guidance:** Use the wiki crafting costs only as a starting point; recheck explosives and tool costs each patch.
- **Evidence basis:** Explosive costs are documented per item [6][11][12], and raid-related items and fixes changed repeatedly in recent updates [1][3][10].
- **Confidence:** Medium. Costs are cited, but the wiki is undated and damage values were not obtained.
- **So what:** Do not plan a raid from a months-old guide.

# Open Questions

- Per-tier structure hit points and per-door explosive counts were not obtained from an openable, citable source; the community raid calculator returned HTTP 403. A future document should source them from in-game data.
- Whether vanilla Rust has any offline-raid protection mechanism was not verified; a Facepunch statement should be sought.
- The current upkeep fraction per tier is not on the Tool Cupboard wiki page and needs in-game data.
- Whether the wiki's decay timers match the live build is unverified because the page is undated.

# References

**Primary Sources** — Facepunch devblogs and wiki.

- [1] **Facepunch** — *Livestock Update*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [2] **Facepunch Wiki** — *Tool Cupboard, decay and building privilege*. https://wiki.facepunch.com/rust/the_tool_cupboard. Accessed 2026-10-08.
- [3] **Facepunch** — *Breach and Clear*. https://rust.facepunch.com/news/breach-and-clear. Accessed 2026-10-08.
- [4] **Facepunch Wiki** — *Code Lock*. https://wiki.facepunch.com/rust/item/lock.code. Accessed 2026-10-08.
- [5] **Facepunch Wiki** — *Key Lock*. https://wiki.facepunch.com/rust/item/lock.key. Accessed 2026-10-08.
- [6] **Facepunch Wiki** — *Timed Explosive Charge*. https://wiki.facepunch.com/rust/item/explosive.timed. Accessed 2026-10-08.
- [7] **Facepunch Wiki** — *Building terminology*. https://wiki.facepunch.com/rust/Building-terminology. Accessed 2026-10-08.
- [8] **Facepunch Wiki** — *Armored Door*. https://wiki.facepunch.com/rust/item/door.hinged.toptier. Accessed 2026-10-08.
- [9] **Facepunch Wiki** — *Rust wiki index*. https://wiki.facepunch.com/rust/. Accessed 2026-10-08.
- [10] **Facepunch** — *Upgrade hard, raid harder*. https://rust.facepunch.com/news/upgrade-hard-raid-harder. Accessed 2026-10-08.
- [11] **Facepunch Wiki** — *Satchel Charge*. https://wiki.facepunch.com/rust/item/explosive.satchel. Accessed 2026-10-08.
- [12] **Facepunch Wiki** — *Battering Ram*. https://wiki.facepunch.com/rust/item/batteringram. Accessed 2026-10-08.
- [13] **Facepunch Wiki** — *Building Plan*. https://wiki.facepunch.com/rust/item/building.planner. Accessed 2026-10-08.
- [14] **Facepunch** — *Built Different*. https://rust.facepunch.com/news/built-different. Accessed 2026-10-08.

**Community & Practitioner Evidence** — hosting-provider guides.

- [15] **XGamingServer** — *How to Change Decay & Upkeep on Your Rust Server*. https://xgamingserver.com/docs/rust/decay-settings. Accessed 2026-10-08.

**Further Reading**

- None cited.

# Further Reading

- The Facepunch Wiki index [9] lists barricade, wall, window and siege item pages for deeper study.

# Related Documents

- rust-game-mechanics-foundation
- rust-items-crafting-foundation
- rust-server-administration-foundation
- rust-modding-plugins-foundation
- rust-updates-meta-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, 100% links live). | Auto-approve mandate |
