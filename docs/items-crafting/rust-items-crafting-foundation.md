---
id: rust-items-crafting-foundation
title: "Rust Items and Crafting: Foundation"
version: 1.0.1
status: frozen
confidence: Medium
category: Items & Crafting
topic: "Resources, crafting and blueprints"
market: Global
document_type: foundation
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-research-blueprints, rust-game-mechanics-foundation, rust-building-raiding-foundation, rust-server-administration-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation]
tags: [items, crafting, blueprints, workbench, scrap, resources]
game_build_checked: "Livestock Update, 1 October 2026 (wiki pages undated)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-items-crafting-foundation |
| Version | 1.0.1 |
| Status | frozen |
| Confidence | Medium |
| Category | Items & Crafting |
| Region | Global |
| Game build checked | Livestock Update, 1 October 2026 [1]; Rust Wiki item pages carry no build stamp |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This document is the entry point for how Rust turns raw resources into items. It covers gathered resources, crafting, the three workbench tiers, the blueprint and research system, scrap, and the wiki's item categories. It is an overview. Weapon, ammunition and component deep-dives are separate documents.

The core loop is documented by Facepunch: items are locked unless a blueprint is known, workbenches gate tiers, and scrap pays for research [3]. Workbench levels 2 and 3 need blueprint fragments [2], and since the Pivot or Die update of 6 November 2025 workbench crafting costs no scrap, the tech tree tax is gone and all blueprints were wiped once [16]. Scrap-cost detail is in rust-research-blueprints. Confidence is Medium: the system design rests on Facepunch devblogs, but exact costs come from Rust Wiki item pages that carry no build date, and the October 2026 update was checked only for relevance [1].

# Key Facts

- Items are locked except default blueprints; a research bench turns a found item plus scrap into a blueprint with no chance of failure (devblog of 2017) [3].
- Workbenches come in three tiers, must be built in order, and let you craft anything at or below their tier; a higher bench than the item requires crafts faster [3].
- Workbench Level 1 costs 500 Wood and 100 Metal Fragments per the wiki [5].
- Since 2 October 2025, Workbench Level 2 requires 5 Basic Blueprint Fragments and Level 3 requires 5 Advanced Blueprint Fragments [2].
- 20 Basic Blueprint Fragments convert into 1 Advanced Blueprint Fragment [2].
- Pivot or Die (6 November 2025) removed scrap crafting costs from workbenches, removed the tech tree tax, greatly reduced scrap research costs and wiped all blueprints; Blueprint Fragment requirements were unchanged [16]. See rust-research-blueprints.
- The wiki lists Research Table research at 60 Scrap and states the blueprint is known by default; research is only needed for a physical blueprint for the Industrial Crafter [8].
- The Livestock Update of 1 October 2026 added milk, wool and food recipes but does not mention scrap, research or workbench systems [1].

# Scope

Covers the vanilla PC game: resource items, the crafting menu and workbench gating, research and the workbench tech tree, scrap, and the wiki's item category list. Excludes console, modded recipes, server convars (see rust-server-administration-foundation and rust-modding-plugins-foundation), and per-weapon or per-component detail. Checked against the Livestock Update of 1 October 2026 [1].

# Definitions

- **Blueprint** — an item that teaches a specific recipe [10].
- **Scrap** — a currency-like resource used at the research table and workbench [9].
- **Workbench tier** — Level 1, 2 or 3, gating which recipes are craftable [3].
- **Blueprint fragments** — Basic and Advanced fragments, ingredients for Workbench Levels 2 and 3 [11][12].
- **Research table** — a deployable that converts an item plus scrap into a blueprint [8][10].

# Core Mechanics

**Evidence layer.**

**Locked items and blueprints.** Since Devblog 180 (5 October 2017) all items except default blueprints are locked. Players start with default blueprints such as campfires, furnaces, workbenches and storage [3]. Repairing an item also requires its blueprint [3].

**Research.** A looted item is taken to a research bench and scrap is paid to create a blueprint; the devblog states there is no percentage chance of failure [3]. The wiki states the scrap cost depends on the item's rarity or quality, that blueprints also drop in crates and barrels, and that the table does not check whether you already know the recipe, so scrap can be wasted [10]. Once researched, a blueprint can be studied to permanently learn the recipe [3].

**Workbench experimentation.** Devblog 185 (9 November 2017) added an Experiment UI where scrap produces a random blueprint for that tier that avoids ones already learned [4]. The wiki also notes each workbench has a tech tree for targeting a specific item instead of relying on random drops [10]. Pivot or Die removed the "tech tree tax" and cut research scrap costs by rarity [16]; see rust-research-blueprints for the figures. The experiment UI was not re-verified against the current build.

**Workbench tiers.** There are three tiers, each requiring the previous tier to craft [3]. Standing near an active workbench lets you craft anything at that tier and below, and crafting is much faster when the bench tier exceeds the item's requirement [3]. Wiki craft times show this: the Research Table takes 30 s at Level 1, 15 s at Level 2, and 7 s at Level 3 [8].

**Fragment gate.** From the Meta Shift update (2 October 2025), Level 2 and 3 workbenches need 5 Basic and 5 Advanced Blueprint Fragments respectively, a stated soft gate pushing players to monuments [2]. The same update says scrap crafting costs for levels 2 and 3 were greatly reduced [2]. Pivot or Die (6 November 2025) then removed scrap crafting costs from workbenches entirely while leaving fragment requirements unchanged [16]; the wiki recipes for Levels 2 and 3 list no scrap [6][7]. Its changelog speaks of "Workbenches" generally and does not name Levels 2 and 3 [16].

**Blueprint wipe.** Pivot or Die wiped all blueprints and all servers on 6 November 2025 [16]; see rust-research-blueprints for wipe behaviour.

**Resources.** Wood is collected from trees and is an ingredient in many recipes [13]. Metal ore and sulfur ore are smelted in furnaces into metal fragments and sulfur [14][15]. Scrap is not craftable and is obtained from loot such as crates, barrels, airdrops and scientists [9]. The October 2026 update added livestock products (milk, wool, meat, bones, leather) as new harvestable resources [1].

**Item categories.** The Rust Wiki groups items into Weapons, Construction, Items, Resources, Attire, Tools, Medical, Food, Ammo, Traps, Components, Electrical, Fun and Misc [17].

# Reference Data

**Evidence layer.** Values are from Rust Wiki item pages, which show no build stamp (the Workbench 2 and 3 pages read "Updated: This Year"), so treat them as current to October 2026 but unconfirmed against a specific patch [5][6][7].

| Item | Craft cost | Requires | Craft time | Research cost | Source |
|------|-----------|----------|------------|---------------|--------|
| Workbench Level 1 | 500 Wood, 100 Metal Fragments | none | 30 s none, 15 s L1, 7 s L2/L3 | 60 Scrap | [5] |
| Workbench Level 2 | 500 Metal Fragments, 20 High Quality Metal, 5 Basic Blueprint Fragments | Workbench L1 | 45 s L1, 22 s L2, 11 s L3 | 30 Scrap | [6] |
| Workbench Level 3 | 1,000 Metal Fragments, 100 High Quality Metal, 5 Advanced Blueprint Fragments | Workbench L2 | 1 min L2, 30 s L3 | 30 Scrap | [7] |
| Research Table | 200 Metal Fragments, 20 Scrap | Workbench L1 | 30 s L1, 15 s L2, 7 s L3 | 60 Scrap | [8] |

| Resource | Stack size | Notes | Source |
|----------|-----------|-------|--------|
| Scrap | 1000 | Despawns 20 min on ground; not craftable | [9] |
| Wood | 1000 | From trees; Workbench L1 uses 500 | [13] |
| Metal Ore | 1000 | Smelts to Metal Fragments | [14] |
| Sulfur Ore | 1000 | Smelts to Sulfur | [15] |
| Blueprint | 1000 | Despawns 5 min | [10] |
| Basic Blueprint Fragment | 100 | 10% from Military Crate, Underwater Advanced Crate, Road Scientist | [11] |
| Advanced Blueprint Fragment | 100 | 2 from each Locked Crate; 10% for 1 from Elite Crate | [12] |

Selected scrap yields (wiki, undated): Elite Crate 25, Military Crate 8, Barrels 2 each, Airdrop 140-160 at 55.6% [9].

# Version & Patch Notes

**Evidence layer.**

| Date | Update | Change | Source |
|------|--------|--------|--------|
| 5 Oct 2017 | Devblog 180 | Workbenches and blueprints added; items locked except defaults; repairs require blueprint | [3] |
| 9 Nov 2017 | Devblog 185 | Workbench Experimentation; some research costs reduced one tier | [4] |
| 2 Oct 2025 | Meta Shift | Fragment requirement for Workbench L2/L3; level 2/3 scrap costs greatly reduced | [2] |
| 6 Nov 2025 | Pivot or Die | Scrap removed from workbench crafting; tech tree tax removed; research costs cut; all blueprints wiped | [16] |
| 1 Oct 2026 | Livestock | New livestock resources and recipes; no research or workbench change mentioned | [1] |

Volatile: all costs, craft times, research costs and drop rates. Meta Shift stated a Part 2 was planned for the December update [2]; Pivot or Die (November 2025) is a follow-up whose changes are recorded here [16]. Anything shipped in December 2025 was not checked.

# Common Pitfalls

- Researching a recipe you already know wastes scrap, because the table does not check [10].
- Workbench tiers cannot be skipped; each requires the previous tier [3].
- Older numbers go stale: the wiki Workbench 2 and 3 pages list no scrap in the craft cost, consistent with Pivot or Die removing scrap from workbench crafting, so guides listing scrap there (or a tech tree tax) predate 6 November 2025 [16][6][7].
- Research only yields a physical blueprint for the Industrial Crafter, because workbench and Research Table blueprints are known by default [5][6][7][8][10].

# Interactions & Related Systems

- Fragments are sourced from monuments, so the crafting gate feeds into exploration and PvP risk [2]; see rust-game-mechanics-foundation.
- Workbench and tool cupboard wood costs link to base building; see rust-building-raiding-foundation [13].
- Recipe costs can be altered by server settings and plugins; see rust-server-administration-foundation and rust-modding-plugins-foundation. This document does not verify specific convars.
- Monthly patches rebalance recipes; see rust-updates-meta-foundation [1][2].
- Blueprints can be placed in an Industrial Crafter to automate crafting [10].

# Assessed Guidance

**Judgement layer.**

## Guidance 1 — Treat every wiki cost as provisional until checked in game

- **Guidance:** Verify recipe, research and fragment numbers in the in-game crafting and tech tree before planning an economy.
- **Evidence basis:** Wiki pages are undated while Meta Shift and Pivot or Die changed workbench costs, research costs and fragments [2][16][6][7].
- **Confidence:** Medium. The reasoning is sound but depends on wiki staleness, which is inferred.
- **So what:** Quote costs with a build date and recheck after each first-Thursday update.

## Guidance 2 — Plan fragment collection before the Level 2 and 3 workbenches

- **Guidance:** Treat Basic fragments as the early bottleneck and Advanced fragments as a monument-run goal.
- **Evidence basis:** Fragment sources are monuments and crates, and conversion is 20 Basic to 1 Advanced [2][11][12].
- **Confidence:** Medium. Sources are primary, but the strategic framing is judgement.
- **So what:** Small groups should budget monument time, not just scrap, for progression.

# Open Questions

- Resolved in 1.0.1: Workbench L2 and L3 cost no scrap to craft (Pivot or Die removed scrap crafting costs from workbenches [16]; the wiki lists none [6][7]). Their research cost is 30 scrap per the undated wiki pages [6][7]; Pivot or Die gives rarity-tier research figures but does not name these benches, so the 30 is not confirmed against a build.
- Whether any further Meta Shift changes shipped in December 2025 beyond Pivot or Die.
- Whether the Experiment UI is unchanged since 2017 [4].
- Gather rates per tool and node; not covered here.

# References

Cite every factual claim. Numbered contiguously from [1].

**Primary Sources**

- [1] **Facepunch** — *Livestock Update*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [2] **Facepunch** — *Meta Shift*. https://rust.facepunch.com/news/meta-shift/. Accessed 2026-10-08.
- [3] **Facepunch** — *Devblog 180*. https://rust.facepunch.com/news/devblog-180. Accessed 2026-10-08.
- [4] **Facepunch** — *Devblog 185*. https://rust.facepunch.com/news/devblog-185. Accessed 2026-10-08.
- [5] **Rust Wiki (Facepunch)** — *Workbench Level 1*. https://wiki.facepunch.com/rust/item/workbench1. Accessed 2026-10-08.
- [6] **Rust Wiki (Facepunch)** — *Workbench Level 2*. https://wiki.facepunch.com/rust/item/workbench2. Accessed 2026-10-08.
- [7] **Rust Wiki (Facepunch)** — *Workbench Level 3*. https://wiki.facepunch.com/rust/item/workbench3. Accessed 2026-10-08.
- [8] **Rust Wiki (Facepunch)** — *Research Table*. https://wiki.facepunch.com/rust/item/research.table. Accessed 2026-10-08.
- [9] **Rust Wiki (Facepunch)** — *Scrap*. https://wiki.facepunch.com/rust/item/scrap. Accessed 2026-10-08.
- [10] **Rust Wiki (Facepunch)** — *Blueprint*. https://wiki.facepunch.com/rust/item/blueprintbase. Accessed 2026-10-08.
- [11] **Rust Wiki (Facepunch)** — *Basic Blueprint Fragment*. https://wiki.facepunch.com/rust/item/basicblueprintfragment. Accessed 2026-10-08.
- [12] **Rust Wiki (Facepunch)** — *Advanced Blueprint Fragment*. https://wiki.facepunch.com/rust/item/advancedblueprintfragment. Accessed 2026-10-08.
- [13] **Rust Wiki (Facepunch)** — *Wood*. https://wiki.facepunch.com/rust/item/wood. Accessed 2026-10-08.
- [14] **Rust Wiki (Facepunch)** — *Metal Ore*. https://wiki.facepunch.com/rust/item/metal.ore. Accessed 2026-10-08.
- [15] **Rust Wiki (Facepunch)** — *Sulfur Ore*. https://wiki.facepunch.com/rust/item/sulfur.ore. Accessed 2026-10-08.
- [16] **Facepunch** — *Pivot or Die* (6 November 2025). https://rust.facepunch.com/news/pivot-or-die. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- [17] **Rust Wiki (Facepunch)** — *Rust Wiki home, item categories*. https://wiki.facepunch.com/rust/. Accessed 2026-10-08.

**Further Reading**

- See the Further Reading section below.

# Further Reading

- Rust Wiki, Research Paper: https://wiki.facepunch.com/rust/item/researchpaper

# Related Documents

- rust-research-blueprints
- rust-game-mechanics-foundation
- rust-building-raiding-foundation
- rust-server-administration-foundation
- rust-modding-plugins-foundation
- rust-updates-meta-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, 100% links live). | Auto-approve mandate |
| 1.0.1 | 2026-10-08 | Research Pipeline (virtual agent) | Added Pivot or Die (6 Nov 2025) [16]: scrap crafting removed from workbenches, tech tree tax removed, blueprint wipe; fixed stale Meta Shift-only statements; resolved Workbench 2/3 scrap Open Question; linked rust-research-blueprints. | Auto-approve mandate |
