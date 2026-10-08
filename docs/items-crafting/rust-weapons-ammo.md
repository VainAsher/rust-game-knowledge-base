---
id: rust-weapons-ammo
title: "Rust Weapons and Ammunition"
version: 1.0.0
status: frozen
confidence: Medium
category: Items & Crafting
topic: "Weapons and ammo"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-items-crafting-foundation, rust-game-mechanics-foundation, rust-building-raiding-foundation, rust-server-administration-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation, rust-combat-damage-model, rust-raiding-costs-defence, rust-server-convars-reference, rust-plugin-development-hooks, rust-update-timeline-2026]
tags: [weapons, ammo, workbench, firearms, bows, damage]
game_build_checked: "Livestock Update, 1 October 2026 (wiki item pages undated)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-weapons-ammo |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Items & Crafting |
| Region | Global |
| Game build checked | Livestock Update, 1 October 2026 [1]; Rust Wiki item pages show "Updated: This Year" with no build stamp |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This deep-dive goes below the weapons overview in rust-items-crafting-foundation. It lists the main ranged weapons and ammunition types, the workbench level each needs, and the headline stats published on the Facepunch Rust Wiki item pages: craft cost, research cost, damage per ammo type, projectile velocity and headshot multiplier. It does not cover melee, explosives or the combat damage model, which belong to sibling documents.

The headline pattern is a tier ladder. Bows, the crossbow, the Waterpipe Shotgun and the Revolver need no more than Workbench Level 1; the Pump Shotgun, Thompson, Semi-Automatic Pistol and Python need Level 2; the Assault Rifle and Bolt Action Rifle need Level 3 [3][7][8][9][10][11][12][13][16][17]. Confidence is Medium: the numbers come from first-party wiki pages, but those pages carry no build date, and the Livestock Update (1 October 2026) lists no ammo or weapon damage changes [1].

# Key Facts

- Craftable firearms are gated by workbench level: Level 1 for the Revolver, Waterpipe Shotgun and Crossbow; Level 2 for the Pump Shotgun, Thompson, Semi-Automatic Pistol and Python; Level 3 for the Assault Rifle and Bolt Action Rifle [3][7][8][9][10][11][12][13][17].
- Ammo is gated too: Pistol Bullet needs Workbench Level 1, 5.56 Rifle Ammo and 12 Gauge Buckshot Level 2, HV and Explosive 5.56 Level 3 [4][5][6][19][20].
- Wiki-listed base damage per round: Assault Rifle 50, Bolt Action Rifle 80, Thompson 37.5, Python 55, Revolver 35, all with plain ammo of the matching family [3][13][12][8][7].
- Headshot multiplier is x2 for rifle and pistol rounds, x1.2 for buckshot, and x1.5 for arrows [3][7][10][16].
- The wiki shows two research routes per item: a Research Table price and a higher Workbench tech-tree price. The Assault Rifle shows 120 Scrap and 500 Scrap [3].
- The M249 is listed as not craftable, with Helicopter Crate and Bradley Crate drops [15]. The LR-300 page marks it neither craftable nor researchable [14].
- Livestock (1 October 2026) mentions only fixes touching the Crossbow, Minigun and similar items, with no stat changes [1].

# Scope

Covers vanilla PC Rust firearms, bows and the ammunition they use, with workbench tier, craft and research cost and per-ammo damage as listed on Facepunch wiki item pages. Excludes melee weapons, explosives and launchers (see rust-raiding-costs-defence), the damage and armour model (see rust-combat-damage-model), weapon attachments beyond brief mention, server convars (see rust-server-convars-reference) and plugin changes (see rust-plugin-development-hooks). Checked against the Livestock Update of 1 October 2026 [1]. Not every weapon is covered: SMG variants, the SKS, M39, Minigun, HMLMG, L96 and flare or event weapons appear only where an ammo page lists them.

# Definitions

- **Ammo family** — the ammunition group a weapon accepts: 5.56 Rifle, Pistol, 12 Gauge, Arrow [4][19][20][16].
- **Workbench level** — the tier needed to craft an item (see rust-items-crafting-foundation).
- **Tech tree price** — the Scrap cost of unlocking a recipe at a workbench, listed separately from the Research Table price [3].
- **Headshot multiplier** — the wiki column showing damage scaling on a head hit [3].
- **Velocity** — projectile speed in the wiki's units; drops with range for standard rounds [4].

# Core Mechanics

**Evidence layer.**

**Ammo families.** Each weapon accepts a fixed family. Rifle-calibre weapons take 5.56 Rifle Ammo in four variants: standard, HV, Explosive and Incendiary [3][13]. Pistol-calibre weapons (Revolver, Python, Semi-Automatic Pistol, Thompson) take Pistol Bullet, HV Pistol Ammo and Incendiary Pistol Bullet [7][8][9][12]. Shotguns take 12 Gauge Slug, Buckshot, Incendiary Shell and Handmade Shell [10][11]. Bows and the crossbow share Wooden, Bone, Fire and High Velocity arrows [16][17].

**Variant behaviour.** The wiki describes standard rifle and pistol ammo as losing velocity over distance with slightly reduced damage [4][19]. HV rifle ammo is described as faster, with less drop and slightly higher damage at long range [5]. Explosive rifle ammo explodes on contact for a small amount of fragmentation damage to nearby objects [6]. Per the Assault Rifle page, Incendiary 5.56 lists higher damage (56 versus 50) but lower velocity (225 versus 375), while Explosive lists the same damage as standard with lower velocity [3].

**Workbench gating.** Weapons list a required workbench level, and a higher bench shortens craft time: the Python takes 30 s at Level 2 and 15 s at Level 3 [8]; the Revolver takes 30 s, 15 s and 7 s at Levels 1, 2 and 3 [7].

**Two research prices.** Each item page lists a Research Table price and a "Tech Tree" price at its workbench. For the Revolver these are 30 and 125 Scrap [7]; for the Python 60 and 250 [8]; for the Bolt Action Rifle 120 and 500 [13]. The hunting bow, crossbow and wooden arrow pages state the recipe is known by default, so research is only needed for a physical blueprint for the Industrial Crafter [16][17][18].

**Loot-only weapons.** The M249 page lists the weapon as not craftable and not researchable, with loot from Helicopter and Bradley crates [15]. The LR-300 page lists no craft or research data [14].

# Reference Data

**Evidence layer.** All values from Rust Wiki item pages, accessed 2026-10-08. The pages carry no build stamp; treat them as current to the Livestock Update only as a working assumption [1].

| Weapon | Craft cost | Workbench | Research Table / tech tree (Scrap) | Source |
|--------|-----------|-----------|-----------------------------------|--------|
| Hunting Bow | 200 Wood, 50 Cloth | None | 120 (known by default) | [16] |
| Crossbow | 200 Wood, 75 Metal Fragments, 2 Rope | Level 1 | 30 (known by default) | [17] |
| Waterpipe Shotgun | 150 Wood, 75 Metal Fragments | Level 1 | 30 / 125 | [11] |
| Revolver | 125 Metal Fragments, 25 Cloth, 1 Metal Pipe | Level 1 | 30 / 125 | [7] |
| Python Revolver | 10 High Quality Metal, 3 Metal Pipe, 1 Metal Spring | Level 2 | 60 / 250 | [8] |
| Semi-Automatic Pistol | 4 High Quality Metal, 1 Metal Pipe, 1 Semi Automatic Body | Level 2 | 60 / 250 | [9] |
| Thompson | 100 Wood, 10 High Quality Metal, 1 Metal Spring, 1 SMG Body | Level 2 | 60 / 250 | [12] |
| Pump Shotgun | 15 High Quality Metal, 2 Metal Pipe, 1 Metal Spring | Level 2 | 60 / 250 | [10] |
| Assault Rifle | 200 Wood, 50 High Quality Metal, 4 Metal Spring, 1 Rifle Body | Level 3 | 120 / 500 (page ambiguous) | [3] |
| Bolt Action Rifle | 20 High Quality Metal, 3 Metal Pipe, 1 Metal Spring, 1 Rifle Body | Level 3 | 120 / 500 | [13] |
| LR-300 | Not listed (page marks not craftable) | n/a | Not researchable per page | [14] |
| M249 | Not craftable | n/a | Not researchable | [15] |

| Ammo | Craft cost (yield) | Workbench | Research Table / tech tree (Scrap) | Stack | Source |
|------|-------------------|-----------|-----------------------------------|-------|--------|
| Pistol Bullet | 10 Metal Fragments, 5 Gun Powder (4) | Level 1 | 30 / 125 | 128 | [19] |
| 5.56 Rifle Ammo | 10 Metal Fragments, 5 Gun Powder (3) | Level 2 | 60 (reading ambiguous) / 250 | 128 | [4] |
| 12 Gauge Buckshot | 5 Metal Fragments, 10 Gun Powder (2) | Level 2 | 30 / 250 | 64 | [20] |
| HV 5.56 Rifle Ammo | 10 Gun Powder, 10 Metal Fragments (3) | Level 3 | 60 / 500 | 128 | [5] |
| Explosive 5.56 Rifle Ammo | 20 Gun Powder, 10 Metal Fragments, 10 Sulfur (2) | Level 3 | 60 / 500 | 128 | [6] |
| Wooden Arrow | 25 Wood, 10 Stones (2) | None | 120 (known by default) | 64 | [18] |

Damage per round with standard ammo of the matching family (damage / velocity / headshot multiplier), wiki values:

| Weapon | Standard ammo damage | Velocity | Headshot | Source |
|--------|---------------------|----------|----------|--------|
| Assault Rifle | 50 | 375 | x2 | [3] |
| Bolt Action Rifle | 80 | 656.2 | x2 | [13] |
| LR-300 | 40 | 562.5 | not stated | [14] |
| Thompson | 37.5 | 300 | x2 | [12] |
| Semi-Automatic Pistol | 40 | 300 | x2 | [9] |
| Python Revolver | 55 | 300 | x2 | [8] |
| Revolver | 35 | 300 | x2 | [7] |
| Pump Shotgun (Buckshot) | 15 | 225 | x1.2 | [10] |
| Pump Shotgun (Slug) | 80 | 225 | x2 | [10] |
| Hunting Bow (Wooden Arrow) | 50 | 50 | x1.5 | [16] |
| Crossbow (Wooden Arrow) | 60 | 75 | x1.5 | [17] |

Variant effects on the Assault Rifle: HV 5.56 keeps damage at 50 with velocity 450; Incendiary 56 damage at 225; Explosive 50 at 225 [3]. On the Bolt Action Rifle, HV velocity is 787.5 [13]. The wiki lists Revolver Incendiary at 39.2 damage [7], Python Incendiary at 61.6 [8], and the Thompson Incendiary at 42 [12].

Other listed facts: Assault Rifle repair costs 13 High Quality Metal and 40 Wood [3]; the Revolver holds 8 rounds per its description [7]; the Python is described as a six-shooter [8]. The Assault Rifle page lists no base magazine size or fire rate [3].

# Version & Patch Notes

**Evidence layer.**

| Date | Update | Weapon or ammo relevance | Source |
|------|--------|--------------------------|--------|
| 2 Oct 2025 | Meta Shift | Ammunition now shows an anti-vehicle damage stat, removed from the "lethality" calculation; projectile-invalid fixes for slow projectiles such as arrows and shotgun bullets; medieval weapon cost cuts | [2] |
| 1 Oct 2026 | Livestock | Crossbow arrow rotation fix in the viewmodel; Minigun ammo counter fix inside containers; no listed damage or ammo stat changes | [1] |

Volatile: every damage, cost and research number above. The wiki gives no history for stats, so a change since the last patch cannot be ruled out from the wiki alone.

# Common Pitfalls

- Mixing up the two research prices. The Research Table price and the tech tree price differ by roughly a factor of four on these pages [7][8][13].
- Assuming a weapon is craftable. The M249 is not [15], and the LR-300 page lists no recipe [14].
- Expecting incendiary or explosive ammo to deal more total effect. On the Assault Rifle page Incendiary does 56 versus 50, but at 225 velocity against 375 [3].
- Reading shotgun damage as one number. The 15 shown for Buckshot is a per-listing figure; the wiki gives no pellet count [10].
- Quoting DPS across pages without checking: the wiki DPS for the same ammo differs by weapon (5.56 on the Assault Rifle 375.1 versus the Bolt Action Rifle 47.1) [4].

# Interactions & Related Systems

- Workbench tiers, scrap and blueprints are explained in rust-items-crafting-foundation; fragments gate Level 2 and 3 benches [2].
- Damage versus armour and structures is in rust-combat-damage-model; explosive costs in rust-raiding-costs-defence.
- Server settings and plugins can alter recipes and damage; see rust-server-convars-reference and rust-plugin-development-hooks. This document does not verify convars.
- Update-by-update history: rust-update-timeline-2026 and rust-updates-meta-foundation [1][2].
- Gun Powder, Metal Fragments and Sulfur are the shared ammo inputs [4][5][6][19][20]; see rust-game-mechanics-foundation for gathering.

# Assessed Guidance

**Judgement layer.**

## Guidance 1 — Treat Workbench Level 2 as the practical firearm threshold

- **Guidance:** For most players, aim for Workbench Level 2 first; it unlocks the Python, Semi-Automatic Pistol, Thompson, Pump Shotgun and the standard 5.56 and shotgun ammo.
- **Evidence basis:** Those items and ammo list Level 2 [4][8][9][10][12][20].
- **Confidence:** Medium. The gating is cited, but "practical" is a judgement about value.
- **So what:** Budget the Basic Blueprint Fragments for Level 2 before chasing rifle research [2].

## Guidance 2 — Do not buy rifle research before checking the ammo bench

- **Guidance:** Confirm you can craft the matching ammo at your bench level before paying for a rifle.
- **Evidence basis:** The Assault Rifle and Bolt Action Rifle need Level 3, while standard 5.56 needs Level 2 and HV or Explosive needs Level 3 [3][4][5][6][13].
- **Confidence:** Medium. Costs are first-party but undated.
- **So what:** A Level 3 rifle with no ammo supply is a poor spend of Scrap.

## Guidance 3 — Recheck every number after each first-Thursday update

- **Guidance:** Treat all figures here as a snapshot and re-verify in game before building a loadout or server economy.
- **Evidence basis:** Wiki pages carry no build stamp and Meta Shift changed ammo stat display [2][3].
- **Confidence:** Medium. Staleness risk is inferred, not shown.
- **So what:** Cite figures with a date and the Livestock build.

# Open Questions

- Magazine size and fire rate for most weapons: the Assault Rifle page lists neither [3]. In-game data or another Facepunch source is needed.
- Shotgun pellet counts: not listed on the Pump Shotgun page [10].
- LR-300 craft status: the page lists no recipe [14]; confirm in game.
- Which Research Table price applies where the Assault Rifle and 5.56 pages are ambiguous [3][4].
- Whether the Meta Shift Part 2 items affected weapons.
- Weapons not covered: SMG variants, SKS, M39, L96, Minigun, HMLMG, launchers.

# References

Cite every factual claim. Numbered contiguously from [1].

**Primary Sources**

- [1] **Facepunch** — *Livestock Update*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [2] **Facepunch** — *Meta Shift*. https://rust.facepunch.com/news/meta-shift/. Accessed 2026-10-08.
- [3] **Rust Wiki (Facepunch)** — *Assault Rifle*. https://wiki.facepunch.com/rust/item/rifle.ak. Accessed 2026-10-08.
- [4] **Rust Wiki (Facepunch)** — *5.56 Rifle Ammo*. https://wiki.facepunch.com/rust/item/ammo.rifle. Accessed 2026-10-08.
- [5] **Rust Wiki (Facepunch)** — *HV 5.56 Rifle Ammo*. https://wiki.facepunch.com/rust/item/ammo.rifle.hv. Accessed 2026-10-08.
- [6] **Rust Wiki (Facepunch)** — *Explosive 5.56 Rifle Ammo*. https://wiki.facepunch.com/rust/item/ammo.rifle.explosive. Accessed 2026-10-08.
- [7] **Rust Wiki (Facepunch)** — *Revolver*. https://wiki.facepunch.com/rust/item/pistol.revolver. Accessed 2026-10-08.
- [8] **Rust Wiki (Facepunch)** — *Python Revolver*. https://wiki.facepunch.com/rust/item/pistol.python. Accessed 2026-10-08.
- [9] **Rust Wiki (Facepunch)** — *Semi-Automatic Pistol*. https://wiki.facepunch.com/rust/item/pistol.semiauto. Accessed 2026-10-08.
- [10] **Rust Wiki (Facepunch)** — *Pump Shotgun*. https://wiki.facepunch.com/rust/item/shotgun.pump. Accessed 2026-10-08.
- [11] **Rust Wiki (Facepunch)** — *Waterpipe Shotgun*. https://wiki.facepunch.com/rust/item/shotgun.waterpipe. Accessed 2026-10-08.
- [12] **Rust Wiki (Facepunch)** — *Thompson*. https://wiki.facepunch.com/rust/item/smg.thompson. Accessed 2026-10-08.
- [13] **Rust Wiki (Facepunch)** — *Bolt Action Rifle*. https://wiki.facepunch.com/rust/item/rifle.bolt. Accessed 2026-10-08.
- [14] **Rust Wiki (Facepunch)** — *LR-300 Assault Rifle*. https://wiki.facepunch.com/rust/item/rifle.lr300. Accessed 2026-10-08.
- [15] **Rust Wiki (Facepunch)** — *M249*. https://wiki.facepunch.com/rust/item/lmg.m249. Accessed 2026-10-08.
- [16] **Rust Wiki (Facepunch)** — *Hunting Bow*. https://wiki.facepunch.com/rust/item/bow.hunting. Accessed 2026-10-08.
- [17] **Rust Wiki (Facepunch)** — *Crossbow*. https://wiki.facepunch.com/rust/item/crossbow. Accessed 2026-10-08.
- [18] **Rust Wiki (Facepunch)** — *Wooden Arrow*. https://wiki.facepunch.com/rust/item/arrow.wooden. Accessed 2026-10-08.
- [19] **Rust Wiki (Facepunch)** — *Pistol Bullet*. https://wiki.facepunch.com/rust/item/ammo.pistol. Accessed 2026-10-08.
- [20] **Rust Wiki (Facepunch)** — *12 Gauge Buckshot*. https://wiki.facepunch.com/rust/item/ammo.shotgun. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- None cited; all stat claims come from the first-party Facepunch wiki.

**Further Reading**

- See the Further Reading section below.

# Further Reading

- Rust Wiki, Weapon Mods comparison (referenced from the Thompson page; not opened).
- rust-items-crafting-foundation in this KB.

# Related Documents

- rust-items-crafting-foundation
- rust-game-mechanics-foundation
- rust-building-raiding-foundation
- rust-server-administration-foundation
- rust-modding-plugins-foundation
- rust-updates-meta-foundation
- rust-combat-damage-model
- rust-raiding-costs-defence
- rust-server-convars-reference
- rust-plugin-development-hooks
- rust-update-timeline-2026

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
