---
id: rust-base-building-mechanics
title: "Rust Base Building Mechanics"
version: 1.0.0
status: frozen
confidence: Medium
category: Building & Raiding
topic: "Structural mechanics and building rules"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-building-raiding-foundation, rust-raiding-costs-defence, rust-turrets-deployables, rust-server-convars-reference, rust-skins-cosmetics, rust-update-timeline-2026, rust-game-mechanics-foundation, rust-server-administration-foundation, rust-updates-meta-foundation]
tags: [building, stability, tiers, upgrade, privilege, decay, placement]
game_build_checked: "Livestock Update, 1 October 2026"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-base-building-mechanics |
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

This deep-dive covers the structural rules of base building: how stability works, how building blocks are upgraded through tiers with the hammer, what building privilege allows and blocks, where you cannot place things, and how decay interacts with the structure. It goes below the overview in rust-building-raiding-foundation and leaves raid costs and turrets to rust-raiding-costs-defence and rust-turrets-deployables.

The headline is a sourcing gap. The privilege, placement and decay rules come from the Facepunch wiki Tool Cupboard page, which is undated, and the design of stability and upgrading comes from Facepunch devblogs dated 2014 to 2018. No Facepunch source obtained gives current stability percentages per piece, or current upgrade costs. Those figures appear only in a community guide. Confidence is Medium: the rules are primary-sourced but old, and the numeric stability and cost values are not primary-sourced.

# Key Facts

- Stability is a structural-integrity system that makes unsupported buildings fall and prevents sky bridges; it does not account for weight, and unstable placements show a stability percentage (Devblog 35, 2014) [8].
- Stability was later moved onto entity links between building sockets, because the earlier physics-based method was slow and unreliable (Devblog 85, 2015) [9].
- Tier hitpoints were normalised in December 2017: Stone 500, Metal 1000, Armored 2000, with the Metal tier base cost raised from 150 to 200 metal fragments (Devblog 190) [6].
- The pillar building block was removed in February 2018, and wall frames were given the same stability as walls and doorways [7].
- The privilege radius is projected from the foundations connected to the Tool Cupboard, not from the cupboard itself [3].
- Unauthorised players can still place twig floors and wooden ladders inside someone's privilege; everything else is blocked [3].
- Default `decay.upkeep_grief_protection` and `decay.upkeep_period_minutes` are both 1440 minutes (24 hours) [4].
- The Livestock Update (1 October 2026) fixed upgrade-related door controller movement on high external gates and triangle foundation connections [1].

# Scope

Covered: stability, building block tiers and the hammer upgrade flow, building skins in the structural sense, building privilege radius and authorisation, placement restrictions, and the decay and upkeep rules that affect structures. Vanilla PC Rust on the build above. Excluded: explosive costs and per-tier raid cost tables (rust-raiding-costs-defence), turrets and traps (rust-turrets-deployables), the group upkeep tax detail (rust-building-raiding-foundation), cosmetics economics (rust-skins-cosmetics), and modded servers.

# Definitions

- **Stability:** the structural-integrity value of a placed building piece, shown as a percentage on unstable placements [8].
- **Building block:** a placeable structural piece such as a foundation, wall, floor or roof, placed with the Building Plan [12].
- **Tier:** the material grade of a building block (twig, wood, stone, metal, armored) as used by the wiki decay list [3].
- **Entity links:** socket connections between entities, used by the stability system from 2015 [9].
- **Conditional model:** a piece model that appears only when neighbours are or are not connected, for example corners [10].
- **High external wall:** a tall freestanding wall that adds no upkeep and is protected from decay within a Tool Cupboard radius [3].

# Core Mechanics

**Stability.** The system makes buildings fall down when they are unsupported. It lets players build self-supporting floors without a pillar or wall under every floor block, and it prevents sky bridges. The author said it would never be fully true to life, and weight is not considered [8]. Unstable placements show a stability percentage and the health bar background turns red [8]. In 2015 the calculation was converted from physics queries to entity links, where constructions track the state of their sockets and can refuse an attachment if a socket is occupied. The devblog says early results looked more robust but does not describe the new calculation [9]. Wall frames provide the same stability as walls and doorways since February 2018, and the post says they can be a useful way to add stability [7]. A community guide dated 11 June 2026 states that a piece at 0 percent collapses and that stability falls with distance from support, but it gives no thresholds and names no build [15].

**Tiers and upgrading.** Holding right-click with the hammer opens a menu for changing block type, rotating and demolishing; some options require Tool Cupboard influence [8]. Upgrading to stone or metal raises the block's maximum health where available [8]. The Facepunch wiki says the hammer is used to upgrade building materials and opens options on right-click, but it lists no upgrade paths or costs [13]. In December 2017 Facepunch normalised protection values: Armored 2000, Metal 1000, Stone 500, so metal is twice stone and armored twice metal [6]. The same post raised the metal tier base cost to 200 metal fragments from 150 and removed the small holes in the tiers [6]. The Building Plan costs 20 wood to craft; the wiki page itself does not describe tiers or stability [12]. A community guide says pieces are placed at twig and then upgraded, and that upgrading requires materials and building privilege [15].

**Conditional models and corners.** The 2014 building system infers corners where two edges intersect at 90 degrees, and foundation edge stones appear only when no connecting piece is present [10]. In 2015 conditional models were still client-side physics checks and could not change colliders [9].

**Building skins.** The 2014 plan was that walls could be upgraded from wood to stone and then metal [10]. The 2017 skin rework made it easier to define skinnable objects and replaceable materials [11]. In the Livestock Update, all four Ladder Hatch variants became skinnable through the workshop, and reskinning sheet metal doors no longer moves the attached door controller; upgrading high external gates likewise no longer moves it [1]. September 2026 added a per-item "random" skin option, and fixed random skins appearing on deployables [2].

**Building privilege radius.** The Tool Cupboard wiki says the radius is projected by the foundations connected to the cupboard, not from the cupboard's position, and that diagrams may not be to scale; the way to find the edge is to walk the base and watch for the privilege indicator [3]. Separate buildings need separate cupboards unless connected by foundations [3]. Placing a cupboard authorises its owner; authorised players can build, pick up deployables and trigger flame and shotgun traps [3]. The 2014 design had the same rule: only authorised players can use building tools within the radius [8].

**Placement restrictions.** In another player's privilege, unauthorised players may place twig floors and wooden ladders (orange "BUILDING BLOCKED" outline); any other placement shows red and sends a private chat notice [3]. High external walls do not add upkeep and do not decay inside the radius, and external cupboards can protect walls outside the main radius and stop players building just outside it [3]. Recent placement fixes: fireplaces cannot be deployed under a ceiling and rugs no longer block Workbench Upgrade placement [2]; storage adaptors cannot clip a head through a roof and drop boxes no longer allow a one-way peek [1].

**Decay and structure.** Without a cupboard holding resources, decay begins immediately. Once a material runs out, parts of that material decay on these timers: twig 1 hour, wood 3, stone 5, metal 8, armored 12, starting at the outermost exposed layers [3]. A destroyed cupboard holding resources consumes up to 24 hours of upkeep [3]. Walls, foundations, ceilings, roofs, doors and window pieces add to upkeep; items inside do not [3].

# Reference Data

Checked 2026-10-08 against the Livestock Update [1]. Each row carries the date of its own source; no primary row has been confirmed against a 2026 build.

| Item | Value | Source date or build | Source |
|------|-------|----------------------|--------|
| Stone tier protection | 500 hp | Devblog 190, 14 Dec 2017 | [6] |
| Metal tier protection | 1000 hp | Devblog 190, 14 Dec 2017 | [6] |
| Armored tier protection | 2000 hp | Devblog 190, 14 Dec 2017 | [6] |
| Metal tier base cost | 200 metal fragments (was 150) | Devblog 190, 14 Dec 2017 | [6] |
| Building Plan | 20 wood, no workbench | Wiki, undated | [12] |
| Hammer | 100 wood | Wiki, undated | [13] |
| Tool Cupboard | 1000 wood | Wiki, undated | [3] |
| High External Wooden Wall | 4000 wood for 3, Workbench Level 1, hammer repair 2000 wood | Wiki, undated | [14] |
| Decay timers (twig, wood, stone, metal, armored) | 1, 3, 5, 8, 12 hours | Wiki, undated | [3] |
| Wood and sheet metal wall hp (community) | about 250 and about 1000 | Guide, 11 Jun 2026, no build named | [15] |

| Convar | Default | Meaning | Source |
|--------|---------|---------|--------|
| `decay.scale` | 1 | Decay multiplier on the server | [4] |
| `decay.upkeep_grief_protection` | 1440 | Max minutes of upkeep a destroyed cupboard can consume | [4] |
| `decay.upkeep_period_minutes` | 1440 | Length of each upkeep period; raising it lowers cost | [4] |

The wiki commands page states no game version, so confirm defaults in the live console [4]. Twig hitpoints and per-piece stability are absent from every primary source opened.

# Version & Patch Notes

- **8 Aug 2014, Friday Devblog 20:** conditional corner models and planned wood-to-stone-to-metal wall upgrades [10].
- **21 Nov 2014, Devblog 35:** stability introduced, hammer menu for upgrade, rotate and demolish [8].
- **5 Nov 2015, Devblog 85:** stability moved to entity links [9].
- **2 Feb 2017, Devblog 146:** skin system reworked [11].
- **14 Dec 2017, Devblog 190:** tier hitpoints normalised, metal cost 150 to 200 [6].
- **1 Feb 2018, Devblog 196:** pillars removed, wall frames given wall stability [7].
- **3 Sep 2026, Breach and Clear:** garage door pickup without privilege, fireplace-under-ceiling and rug placement fixes, random skin option [2].
- **1 Oct 2026, Livestock Update:** triangle foundation connection fix, door controller fixes on upgrade and reskin, skinnable ladder hatches, sandbag stages [1].
- Volatile: tier hitpoints and upgrade costs have not been confirmed against 2026 data; the recent patches are placement and connection fixes [1][2].

# Common Pitfalls

- Treating the privilege area as a circle around the cupboard; it follows connected foundations [3].
- Building a separate structure without its own cupboard coverage [3].
- Assuming pillars exist for stability; they were removed in 2018 and wall frames are the stability aid [7].
- Assuming heavy upper floors reduce stability: weight is not modelled [8].
- Quoting 2017 hitpoints as current without checking in game [6].
- Assuming the privilege diagrams are to scale; the wiki says they may not be [3].

# Interactions & Related Systems

- Raid costs per tier and explosive counts: see rust-raiding-costs-defence.
- Turrets, traps and other privilege-gated deployables: see rust-turrets-deployables [3].
- Decay and upkeep convar administration: see rust-server-convars-reference and rust-server-administration-foundation [4].
- Skin cosmetics and workshop rules: see rust-skins-cosmetics [1][2].
- Monthly changes: see rust-update-timeline-2026 and rust-updates-meta-foundation [1][2].
- Overview of upkeep, group tax and the Tool Cupboard: see rust-building-raiding-foundation.

# Assessed Guidance

## Guidance 1 — Check privilege coverage by walking the base, not by eye

- **Guidance:** After each expansion, walk the perimeter and confirm the privilege indicator is present at every external piece, adding a cupboard where it is not.
- **Evidence basis:** The radius is projected from connected foundations and the diagrams may not be to scale, and the wiki recommends this walk [3].
- **Confidence:** Medium. The page is official but undated.
- **So what:** Gaps in coverage let others build against your walls and leave pieces unprotected from decay.

## Guidance 2 — Plan stability with the hammer in hand and with wall frames, not pillars

- **Guidance:** Place pieces, read the stability percentage and use wall frames for extra support where needed.
- **Evidence basis:** Stability percentages are shown on unstable placements and wall frames match wall stability [7][8].
- **Confidence:** Medium. Both sources are from 2014 to 2018 and no current thresholds were obtained.
- **So what:** Do not rely on remembered span limits; test in the live build.

## Guidance 3 — Treat tier hitpoints and upgrade costs as unverified for 2026

- **Guidance:** Use the 2017 ratios (metal twice stone, armored twice metal) for planning but verify absolute values in game.
- **Evidence basis:** The ratios come from Devblog 190 and the community guide gives similar values with no build [6][15].
- **Confidence:** Low. The primary figures are nine years old and the later figures are community-only.
- **So what:** Do not publish guides quoting exact tier numbers without a fresh in-game check.

# Open Questions

- Current stability percentage cutoffs and per-piece stability values: no Facepunch source obtained.
- Current twig and wood hitpoints and the current upgrade costs per tier for each piece: not in any primary source opened.
- Whether the wiki decay timers and the 2017 hitpoints match the live build.
- Exact time window in which a freshly placed piece can be rotated or demolished: only a community guide mentions a window, with no figure [15].
- Placement restrictions around terrain, monuments, water and roads: no primary source obtained.
- Whether the 2014 rule that some hammer options need privilege still applies unchanged.

# References

**Primary Sources** — Facepunch devblogs and wiki.

- [1] **Facepunch** — *Livestock Update*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [2] **Facepunch** — *Breach and Clear*. https://rust.facepunch.com/news/breach-and-clear. Accessed 2026-10-08.
- [3] **Facepunch Wiki** — *Tool Cupboard, decay and building privilege*. https://wiki.facepunch.com/rust/the_tool_cupboard. Accessed 2026-10-08.
- [4] **Facepunch Wiki** — *Useful Console Commands*. https://wiki.facepunch.com/rust/useful_commands. Accessed 2026-10-08.
- [5] **Facepunch Wiki** — *Building terminology*. https://wiki.facepunch.com/rust/Building-terminology. Accessed 2026-10-08.
- [6] **Facepunch** — *Devblog 190*. https://rust.facepunch.com/news/devblog-190. Accessed 2026-10-08.
- [7] **Facepunch** — *Devblog 196*. https://rust.facepunch.com/news/devblog-196. Accessed 2026-10-08.
- [8] **Facepunch** — *Devblog 35*. https://rust.facepunch.com/news/devblog-35. Accessed 2026-10-08.
- [9] **Facepunch** — *Devblog 85*. https://rust.facepunch.com/news/devblog-85. Accessed 2026-10-08.
- [10] **Facepunch** — *Friday Devblog 20*. https://rust.facepunch.com/news/friday-devblog-20. Accessed 2026-10-08.
- [11] **Facepunch** — *Devblog 146*. https://rust.facepunch.com/news/devblog-146. Accessed 2026-10-08.
- [12] **Facepunch Wiki** — *Building Plan*. https://wiki.facepunch.com/rust/item/building.planner. Accessed 2026-10-08.
- [13] **Facepunch Wiki** — *Hammer*. https://wiki.facepunch.com/rust/item/hammer. Accessed 2026-10-08.
- [14] **Facepunch Wiki** — *High External Wooden Wall*. https://wiki.facepunch.com/rust/item/wall.external.high. Accessed 2026-10-08.

**Community & Practitioner Evidence** — hosting-provider guides.

- [15] **XGamingServer** — *Rust Base Building Guide: Tiers, Stability and Tool Cupboard* (11 June 2026). https://xgamingserver.com/blog/rust-base-building-guide/. Accessed 2026-10-08.

**Further Reading**

- None cited.

# Further Reading

- Building terminology on the Facepunch wiki names honeycomb, airlock and footprint layouts [5].

# Related Documents

- rust-building-raiding-foundation
- rust-raiding-costs-defence
- rust-turrets-deployables
- rust-server-convars-reference
- rust-skins-cosmetics
- rust-update-timeline-2026
- rust-game-mechanics-foundation
- rust-server-administration-foundation
- rust-updates-meta-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
