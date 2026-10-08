---
id: rust-raiding-costs-defence
title: "Rust Raiding Costs and Base Defence"
version: 0.1.0
status: in-review
confidence: Low
category: Building & Raiding
topic: "Raid costs and defence"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-building-raiding-foundation, rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-server-administration-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation, rust-combat-damage-model, rust-weapons-ammo, rust-server-convars-reference, rust-plugin-development-hooks, rust-update-timeline-2026]
tags: [raiding, raid-cost, structure-health, explosives, upkeep, softcore, offline-raiding, defence]
game_build_checked: "Livestock Update, 1 October 2026 (HP and damage tables from a 22 September 2026 build via a third party)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-raiding-costs-defence |
| Version | 0.1.0 |
| Status | in-review |
| Confidence | Low |
| Category | Building & Raiding |
| Region | Global |
| Game build checked | Livestock Update, 1 October 2026 [1]; HP and damage tables from a 22 September 2026 build per a third party [9] |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This deep-dive goes below the foundation document into what it costs to break a base and what defends one: structure and door hit points by tier, explosive damage and sulfur cost, how many explosives each wall or door takes, the upkeep rules that keep a base alive, and the protections that exist in vanilla Rust. The only vanilla protection found in Facepunch sources is the Softcore raid window and TC raid-blocking system added in July 2026 [3], plus the upkeep grace after a TC is destroyed [5].

Confidence is Low. The Facepunch wiki item pages do not list hit points or damage [6][7][8], so the numeric tables come from third-party raid charts that say they were derived from server files or live game data [9][10][11] and that disagree with each other in places. Anything that disagrees is shown side by side and also listed in Open Questions.

# Key Facts

- From a third-party table said to come from the 22 September 2026 server files: wood wall 250 HP, stone 500, sheet metal 1,000, armoured 2,000 [9].
- The same source gives C4 as 550 explosion damage, rocket as 275 explosion plus 75 blunt, and satchel as 75 explosion plus 200 blunt plus 200 stab [9].
- Sulfur to craft: C4 2,200, rocket 1,400, satchel 480; three independent third-party pages agree [9][10][11].
- Third-party charts put a stone wall at 2 C4 (about 4,400 sulfur) and a sheet metal wall at 4 C4 (8,800 sulfur) from the hard side [9][10].
- C4 crafts from 20 explosives, 5 cloth and 2 tech trash at Workbench Level 3 [6]; the satchel from 4 beancan grenades, 1 rope and 1 small stash at Workbench Level 1 [8].
- Facepunch's wiki gives decay timers after upkeep runs out (twig 1 hour to armoured 12 hours), and a destroyed TC burns up to 24 hours of upkeep to hold a base for 24 hours [5].
- Since 2 July 2026, Softcore servers default to raids only 6 PM to 9 PM server time, and a TC at least 1 hour old blocks raids on walls, floors, roofs, doors and ladder hatches outside that window [3].
- No vanilla offline-raid protection was found in Facepunch sources; offline protection on normal servers appears only as plugins [13] *(assessed from absence of evidence)*.

# Scope

Covered: structure and door HP by tier, explosive damage and craft cost, explosive counts per target, upkeep and decay as they affect defence, and offline-raid and raid-window mechanics. Vanilla PC Rust on the build named above. Modded plugin behaviour is mentioned only as a contrast. Console excluded. Not covered: weapon stats and ammo (see rust-weapons-ammo), the general damage model (see rust-combat-damage-model), and full convar listings (see rust-server-convars-reference). Overview material is in the parent, rust-building-raiding-foundation.

# Definitions

- **Hard side / soft side:** the outer face of a wall or door versus the interior-facing face, which takes less explosive damage; the soft side is described as the face with the X-shaped braces [9].
- **Raid cost (sulfur):** the raw sulfur needed to craft the explosives used, a standard way third parties compare options [9][10].
- **Honeycomb:** layered walls that multiply the cost of raiding through one side [10].
- **Softcore raid window:** a scheduled period in which raiding is allowed on Softcore servers [3].
- **Group upkeep tax:** the player-count based surcharge on TC upkeep [2].

# Core Mechanics

**Why counts are not simple division.** C4 is listed at 550 explosion damage but a 500 HP stone wall is listed as needing 2 C4 [9]. The source does not explain the gap; damage falls off with distance, with C4 at full damage at 0 m and zero at 4 m [9]. Treat the per-target counts as the figure to use and the damage numbers as context [9].

**Explosive damage.** The listed profiles are C4 550 explosion; rocket 275 explosion and 75 blunt (full at 1 m, zero at 3.8 m); satchel 75 explosion, 200 blunt and 200 stab; beancan 15 explosion, 50 blunt and 50 stab [9]. The Facepunch wiki pages for C4, satchel and the armoured door do not publish damage or HP; they give recipes, recycling and loot sources only [6][7][8].

**Soft side.** The interior face takes less damage, so fewer explosives are needed. One source gives beancans on a stone wall as 46 from the soft side instead of 64 [9]; another says the soft side takes "roughly half" the explosives without counts [10]. Most calculators default to the hard side [10].

**Weakest-path principle.** Per the charts, the cheapest breach point sets a base's real cost. A sheet metal wall is listed at 4 C4 and a sheet metal door at 1 C4 [9]. A wooden door can be defeated by fire or melee, or one satchel [10].

**Upkeep.** The TC draws a fraction of build cost every 24 hours; the wiki gives no percentages [5]. A 2017 devblog set the fraction by base size (10% for 1 to 15 blocks, up to 33% above 75 blocks) and made it convar-configurable [4]. The September 2026 group tax adds 2% per player for players 5 to 10 and 4% each beyond, capped at 300% [2]. Treat the 2017 percentages as historical only [4].

**Decay and grief protection.** After a material runs out in the TC, parts made of it decay on the timers in Reference Data [5]. A destroyed TC holding resources eats up to 24 hours of upkeep so the base does not decay for 24 hours, designed so a raided player does not lose their base [5]. Raiders can take over the base with their own doors [5].

**Softcore raid windows and raid blocking.** In the Common Ground update (2 July 2026), Softcore raids default to 6 PM to 9 PM server local time. Outside windows, a TC projects a raid-blocking system covering players inside its radius: walls, floors, roofs, doors and ladder hatches cannot be raided. Deployables and an unprotected TC can still be attacked, and the TC must be at least 1 hour old [3]. A third party adds that outside the window explosive and projectile damage on core building parts is blocked while twig, high external walls and gates, and melee stay vulnerable [9]; this was not confirmed against Facepunch text.

**Offline raiding on normal servers.** The Tool Cupboard wiki page does not use the term [5]. Offline protection appears as server plugins: one limits the number of offline raids per player or team per day and per wipe [13]. That is configuration of individual servers, not a vanilla rule [13].

# Reference Data

Third-party tables are from a build dated 22 September 2026 [9] unless stated; the Livestock Update (1 October 2026) did not list structure HP or explosive damage changes [1]. Counts are hard-side.

| Target | HP [9] | C4 [9] | Rockets [9] | Satchels [9] |
|--------|--------|--------|-------------|--------------|
| Wood wall | 250 | 1 | 2 | 3 |
| Stone wall | 500 | 2 | 4 | 10 |
| Sheet metal wall | 1,000 | 4 | 8 | 23 |
| Armoured wall | 2,000 | 8 | 15 | 46 |
| Wooden door | 200 | 1 | 1 | 2 |
| Sheet metal door | 250 | 1 | 2 | 4 |
| Garage door | 600 | 2 | 3 | 9 |
| Armoured door | 1,000 | 3 | 5 | 15 |
| Ladder hatch / armoured ladder hatch | 250 / 1,000 | 1 / 3 | 2 / 5 | 4 / 15 |
| High external wood or stone wall | 500 | 2 | 3 (wood) / 4 (stone) | 6 (wood) / 10 (stone) |
| Metal window bars | 500 | 2 | 4 | 12 |
| Strengthened glass window | 350 | 2 | 3 | 9 |
| Tool Cupboard | 100 | 1 | 1 | 1 |

Another chart dated 4 June 2026 (stated as current for the June 2026 build) gives overlapping but different values: wood wall satchels 4, stone wall satchels 8, armoured door 800 HP and 3 C4, garage door 600 HP and 3 rockets [10].

| Explosive | Sulfur to craft | Source |
|-----------|-----------------|--------|
| Timed Explosive Charge (C4) | 2,200 | [9][10][11] |
| Rocket | 1,400 | [9][10][11] |
| Satchel Charge | 480 | [9][10][11] |
| Beancan Grenade | 120 in [9][11] against 60 in [10] | conflict |
| Explosive 5.56 ammo (per round) | 25 | [9][10][11] |
| Incendiary rocket | 610 in [10] against 300 in [11] | conflict |

| Raid cost example (hard side, C4 only) | Sulfur | Source |
|----------------------------------------|--------|--------|
| Stone wall (2 C4) | 4,400 | [10] |
| Sheet metal wall (4 C4) | 8,800 | [10] |
| Armoured wall (8 C4) | 17,600 | [10] |
| Sheet metal door (1 C4) | 2,200 | [10] |
| Three stone layers (6 C4) | 13,200 | [10] |

| Crafting inputs | Value | Source |
|-----------------|-------|--------|
| C4 | 20 explosives, 5 cloth, 2 tech trash; Workbench 3; 30 s craft; stack 10 | [6] |
| Satchel Charge | 4 beancan grenades, 1 rope, 1 small stash; Workbench 1; stack 10 | [8] |
| Armoured Door | 20 high quality metal, 5 gears; Workbench 3; repair 25 metal fragments and 10 HQM | [7] |

| Decay timer after material exhausted | Time | Source |
|--------------------------------------|------|--------|
| Twig | 1 hour | [5] |
| Wood | 3 hours | [5] |
| Stone | 5 hours | [5] |
| Metal | 8 hours | [5] |
| Armoured | 12 hours (HQM exhausted) | [5] |

| Upkeep and protection rule | Value | Source |
|----------------------------|-------|--------|
| Group tax, first 4 players | none | [2] |
| Players 5 to 10 | 2% each | [2] |
| Players beyond 10 | 4% each; cap 300% | [2] |
| Destroyed TC grace | up to 24 hours of upkeep consumed | [5] |
| Softcore raid window default | 6 PM to 9 PM server time | [3] |
| Minimum TC age to block raids (Softcore) | 1 hour | [3] |
| Decay convars | decay.scale 1, decay.upkeep true (no version stated) | [12] |

# Version & Patch Notes

- **December 2017, devblog 189:** introduced size-banded upkeep (10% to 33%), TC-stored upkeep and outside-in decay; its decay times (twig 1 h, wood 2 h, stone 3 h, metal 5 h, armoured 12 h) differ from the current wiki [4][5].
- **2 July 2026, Common Ground:** Softcore raid windows and TC raid blocking [3].
- **3 September 2026, Breach and Clear:** group upkeep tax [2].
- **1 October 2026, Livestock Update:** fixed the battering ram hitting TCs through walls; client prediction for grenades, C4 and satchels [1].
- Volatile: raid counts and HP shift with balance passes, and two third-party charts about three months apart already disagree on satchel counts and armoured door HP [9][10].

# Common Pitfalls

- Using soft-side counts for a hard-side wall or vice versa; calculators default to hard side [10].
- Trusting a chart that does not name its build; the two compared here differ on armoured door HP (1,000 against 800) [9][10].
- Overbuilding walls and leaving a cheap door; the weakest path sets the cost [9].
- Assuming vanilla Rust protects offline bases; protection found was plugin-based or Softcore-window based [3][13].
- Assuming Softcore protection covers everything: deployables and an unprotected TC are still attackable [3].
- Using 2017 upkeep percentages or decay times [4].

# Interactions & Related Systems

- Parent overview, upkeep and tax summary: rust-building-raiding-foundation [2][5].
- Damage types and falloff: rust-combat-damage-model [9].
- Explosive, rocket and ammo stats: rust-weapons-ammo [9].
- Decay and Softcore convars: rust-server-convars-reference [3][12].
- Offline-protection plugins and hooks: rust-plugin-development-hooks [13].
- Monthly changes: rust-update-timeline-2026 [1][2][3].
- Recipes and workbenches: rust-items-crafting-foundation [6][8].

# Assessed Guidance

## Guidance 1 — Make the cheapest entry point as expensive as the walls

- **Guidance:** Put your best door tier and any airlock on the shortest path to the TC rather than adding wall layers elsewhere.
- **Evidence basis:** A sheet metal door is listed at 1 C4 while a sheet metal wall is 4, and a honeycomb of three stone layers is 6 C4 [9][10].
- **Confidence:** Medium. The relative counts agree across two charts, but absolute numbers are third-party.
- **So what:** Spend resources on the weakest link first.

## Guidance 2 — Keep the TC stocked and expect it to be targeted

- **Guidance:** Keep upkeep resources in the TC and expect raiders to look for it; a destroyed TC still buys a day of decay protection.
- **Evidence basis:** The Facepunch wiki describes the 24-hour grace and that raiders look for the TC [5].
- **Confidence:** Medium. Official page, but undated.
- **So what:** Do not rely on the 24-hour grace to survive an absence; restock after a raid.

## Guidance 3 — On vanilla servers, plan for no offline protection

- **Guidance:** Assume no offline protection unless the server advertises Softcore or a plugin.
- **Evidence basis:** No vanilla offline mechanism was found; only plugins and Softcore windows appear in sources [3][13].
- **Confidence:** Low. This rests on absence of evidence and community plugin pages.
- **So what:** Check server rules and tags before committing to a base location.

## Guidance 4 — Verify counts against the current build before a raid

- **Guidance:** Treat all numbers here as approximations and check an up-to-date calculator or an in-game test.
- **Evidence basis:** Two charts conflict and the Facepunch wiki gives no HP [7][9][10].
- **Confidence:** High. The conflict is directly visible in the cited sources.
- **So what:** Do not budget a raid from a stale chart.

# Open Questions

- Structure HP and explosive damage have no Facepunch source opened; they need in-game or server-file data. The third-party figures [9] claim server files but are unverified.
- Armoured door HP is 1,000 in [9] against 800 in [10]; satchel counts for wood and stone walls also differ.
- Current per-tier, per-piece upkeep fractions; the wiki gives none [5], and the only official percentages found are from 2017 [4].
- Whether the Softcore blocking details beyond the Facepunch text are accurate [9].
- Softcore raid-window convar names were not published in the update text [3].
- Whether vanilla Rust has any offline-raid protection outside Softcore.
- Beancan and incendiary rocket sulfur costs conflict across sources.

# References

**Primary Sources** — Facepunch devblogs and wiki.

- [1] **Facepunch** — *Livestock Update*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [2] **Facepunch** — *Breach and Clear*. https://rust.facepunch.com/news/breach-and-clear. Accessed 2026-10-08.
- [3] **Facepunch** — *Common Ground*. https://rust.facepunch.com/news/common-ground. Accessed 2026-10-08.
- [4] **Facepunch** — *Devblog 189 (7 December 2017)*. https://rust.facepunch.com/news/devblog-189. Accessed 2026-10-08.
- [5] **Facepunch Wiki** — *Tool Cupboard*. https://wiki.facepunch.com/rust/the_tool_cupboard. Accessed 2026-10-08.
- [6] **Facepunch Wiki** — *Timed Explosive Charge*. https://wiki.facepunch.com/rust/item/explosive.timed. Accessed 2026-10-08.
- [7] **Facepunch Wiki** — *Armored Door*. https://wiki.facepunch.com/rust/item/door.hinged.toptier. Accessed 2026-10-08.
- [8] **Facepunch Wiki** — *Satchel Charge*. https://wiki.facepunch.com/rust/item/explosive.satchel. Accessed 2026-10-08.

**Community & Practitioner Evidence** — third-party charts and plugin pages.

- [9] **GameServerKings** — *Rust Raid Chart (2026)*. https://www.gameserverkings.com/knowledge-base/rust/rust-raid-chart/. Accessed 2026-10-08.
- [10] **XGamingServer** — *Rust Raid Cost Chart*, 4 June 2026. https://xgamingserver.com/blog/rust-raid-cost-chart-how-much-c4-rockets/. Accessed 2026-10-08.
- [11] **Physgun** — *Rust Raid Calculator*. https://physgun.com/tools/rust-raid-calculator/. Accessed 2026-10-08.
- [12] **XGamingServer** — *How to Change Decay and Upkeep on Your Rust Server*. https://xgamingserver.com/docs/rust/decay-settings. Accessed 2026-10-08.
- [13] **Codefling** — *Offline Raid Limiter plugin*. https://codefling.com/plugins/offline-raid-limiter. Accessed 2026-10-08.

**Further Reading**

- None cited.

# Further Reading

- The parent foundation, rust-building-raiding-foundation, for the overview of upkeep and locks.

# Related Documents

- rust-building-raiding-foundation
- rust-game-mechanics-foundation
- rust-items-crafting-foundation
- rust-server-administration-foundation
- rust-modding-plugins-foundation
- rust-updates-meta-foundation
- rust-combat-damage-model
- rust-weapons-ammo
- rust-server-convars-reference
- rust-plugin-development-hooks
- rust-update-timeline-2026

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
