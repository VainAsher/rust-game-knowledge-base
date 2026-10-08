---
id: rust-research-blueprints
title: "Rust Research and Blueprints"
version: 1.0.0
status: frozen
confidence: Medium
category: Items & Crafting
topic: "Research table and blueprint costs"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-items-crafting-foundation, rust-updates-meta-foundation, rust-game-mechanics-foundation, rust-economy-trading, rust-monuments-loot, rust-tools-gathering, rust-wipes-map-generation, rust-world-events, rust-base-building-mechanics]
tags: [research, blueprints, workbench, tech-tree, scrap, fragments]
game_build_checked: "Livestock Update, 1 October 2026 (wiki pages undated)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-research-blueprints |
| Version | 1.0.0 |
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

This deep-dive extends rust-items-crafting-foundation on one question: what it costs, in scrap, to unlock items through the research table and the workbench tech tree, and what happened to those costs after the Meta Shift update. The Facepunch chain is Meta Shift (2 October 2025), which added fragments and cut Workbench 2 and 3 scrap costs without numbers [2], then Pivot or Die (6 November 2025), which removed scrap from workbench crafting entirely, cut research costs by rarity and wiped all blueprints [3].

That closes the foundation's open question: Workbench Level 2 and Level 3 now cost no scrap to craft [3][6][7]. Confidence is Medium. The rarity-based research costs and the November wipe are Facepunch primary [3], but per-item numbers come from undated wiki pages, and the wiki's workbench tech-tree prices do not obviously match the devblog's reduced figures (see Open Questions).

# Key Facts

- Workbench Level 2 and Level 3 no longer require scrap to craft: the Pivot or Die changelog says scrap crafting costs were removed from workbenches [3], and the wiki recipes list no scrap [6][7].
- Pivot or Die (6 November 2025) set research scrap costs by rarity: Common 15 (was 20), Uncommon 30 (was 75), Rare 60 (was 125), Very Rare 120 (was 500) [3].
- It also removed the tech tree tax and wiped all blueprints and all servers [3].
- Wiki Research Table costs in the sampled items match those rarity tiers: 15, 60 and 120 Scrap [11][12][14][15].
- A research table is crafted for 200 Metal Fragments and 20 Scrap at Workbench Level 1 [8].
- Researching a Workbench Level 2 or 3 blueprint costs 30 Scrap, and the blueprint is known by default [6][7][8].
- The Livestock Update (1 October 2026) changelist mentions only a cooking workbench fix and a blueprint button optimisation, with no research cost change [1].

# Scope

Covers the research table, the workbench tech tree, scrap costs per rarity tier, blueprint learning, and blueprint loss through wipes, in vanilla PC Rust. Excludes console, modded recipes and plugin-altered costs (see rust-modding-plugins-foundation), server convars (see rust-server-convars-reference and rust-wipes-map-generation), and the fragment sourcing detail already in rust-items-crafting-foundation. Checked against the Livestock Update, 1 October 2026 [1].

# Definitions

- **Research table** — deployable where an item plus scrap yields a blueprint [8][9].
- **Tech tree** — per-workbench list of items unlocked directly for scrap [9].
- **Tech tree tax** — a scrap surcharge on tech tree unlocks at higher bench tiers, removed 6 November 2025 [3][18].
- **Blueprint wipe** — removal of learned blueprints, forced on all servers at the 6 November 2025 update [3].

# Core Mechanics

**Evidence layer.**

**Two routes to learn an item.** Since Devblog 180 (5 October 2017), items are locked except default blueprints. A found item taken to a research bench becomes a blueprint with no chance of failure, and the blueprint can be studied to learn the recipe permanently or traded [4]. Devblog 185 (9 November 2017) added a workbench Experiment UI that spends scrap on a random blueprint for that tier, avoiding ones already learned [5]. The wiki says each workbench has a tech tree for targeting a specific item [9].

**Cost depends on rarity.** The wiki states the research cost varies by item rarity or quality, and each tech tree item has its own cost [9]. Facepunch gave the four rarity-tier scrap values in the Pivot or Die changelog [3] (table below).

**The table does not check.** The research table does not stop you researching an item you already know, so scrap can be wasted [9].

**Workbench crafting and scrap.** Devblog 180 said building workbenches takes significant scrap, without figures [4]. Pivot or Die removed scrap crafting costs from workbenches; scrap now goes to unlocks [3]. Wiki recipes for Levels 2 and 3 list metal fragments, High Quality Metal and blueprint fragments, not scrap [6][7].

**Learning workbench blueprints.** Workbench 2 and 3 are known by default; research is needed only to obtain a physical blueprint for the Industrial Crafter, at 30 Scrap each [6][7].

**Blueprint loss.** Facepunch sources reviewed describe no loss on death; Devblog 180 does not mention a death penalty [4]. Loss occurs through wipes: Pivot or Die wiped all blueprints and servers [3]. Rustafied reports monthly forced blueprint wipes on official servers, citing a social post, and the same article calls it an undated edit [18]. The Facepunch devblog itself does not commit to monthly wipes [3].

**Scrap supply.** Scrap is not craftable; it comes from loot, for example Elite Crate 25 and Military Crate 8, Locked Crate 140-160 at 33.3% [10].

# Reference Data

**Evidence layer.** Research and tech tree values from Rust Wiki item pages (undated, "Updated: This Year") unless stated; rarity table from Facepunch [3].

| Rarity | Scrap before Pivot or Die | Scrap after (6 Nov 2025) | Source |
|--------|--------------------------|--------------------------|--------|
| Common | 20 | 15 | [3] |
| Uncommon | 75 | 30 | [3] |
| Rare | 125 | 60 | [3] |
| Very Rare | 500 | 120 | [3] |

Sampled items (checked 8 October 2026):

| Item | Workbench needed | Research Table (Scrap) | Wiki tech tree (Scrap) | Source |
|------|------------------|------------------------|------------------------|--------|
| Salvaged Sword | Level 1 | 15 | 125 at Level 1 | [11] |
| Semi-Automatic Pistol | Level 2 | 60 | 250 at Level 2 | [17] |
| Python Revolver | Level 2 | 60 | 250 at Level 2 | [12] |
| Pump Shotgun | Level 2 | 60 | 250 at Level 2 | [13] |
| Auto Turret | Level 2 | 120 | 250 at Engineering Workbench | [16] |
| Metal Facemask | Level 3 | 120 | 500 at Level 3 | [15] |
| AK47 | Level 3 | 120 | 500 at Level 3 | [14] |

Workbench and table items (wiki, undated):

| Item | Craft cost | Research Table (Scrap) | Source |
|------|-----------|------------------------|--------|
| Research Table | 200 Metal Fragments, 20 Scrap (Workbench 1) | 60 | [8] |
| Workbench Level 2 | 500 Metal Fragments, 20 HQM, 5 Basic Blueprint Fragments (Workbench 1) | 30 | [6] |
| Workbench Level 3 | 1,000 Metal Fragments, 100 HQM, 5 Advanced Blueprint Fragments (Workbench 2) | 30 | [7] |

Resolved: Workbench Level 2 and 3 scrap crafting cost is zero per the changelog [3] and recipes [6][7].

# Version & Patch Notes

**Evidence layer.**

| Date | Update | Change | Source |
|------|--------|--------|--------|
| 5 Oct 2017 | Devblog 180 | Items locked; research at bench, no failure chance; workbench tiers | [4] |
| 9 Nov 2017 | Devblog 185 | Experiment UI; eight items' research cost cut one tier | [5] |
| 2 Oct 2025 | Meta Shift | Fragments gate Level 2 and 3; their scrap costs greatly reduced; no numbers; Part 2 planned for December | [2] |
| 6 Nov 2025 | Pivot or Die | Scrap removed from workbench crafting; research costs cut by rarity; tech tree tax removed; all blueprints wiped | [3] |
| 1 Oct 2026 | Livestock | No research or cost change in the changelist lines found | [1] |

Volatile: every scrap figure. Rustafied noted at the time that the November values were still subject to testing [18].

# Common Pitfalls

- Older guides quote the 20/75/125/500 research costs or a 10%/20% tech tree tax; both predate 6 November 2025 [3][18].
- Researching a known recipe wastes scrap [9].
- Treating the wiki "Workbench tech tree" figure as the cheap route: the sampled figures (125 to 500) are larger than the Research Table figures (15 to 120) [11][14].
- Assuming monthly blueprint wipes apply to every server; Facepunch said most servers did not wipe blueprints, and the wipe was forced once [3].

# Interactions & Related Systems

- Fragment sources and the L2/L3 gate: see rust-items-crafting-foundation [2]; monument loot in rust-monuments-loot.
- Scrap as currency and purchases: see rust-economy-trading [10].
- Blueprint and map wipes: see rust-wipes-map-generation [3].
- Gathering tools unlocked via research: see rust-tools-gathering.
- Version history across updates: see rust-updates-meta-foundation.
- Building the workbench bases rely on: see rust-base-building-mechanics.

# Assessed Guidance

**Judgement layer.**

## Guidance 1 — Prefer the research table over the tech tree when you hold the item

- **Guidance:** For a known target item, compare the Research Table cost with the tech tree cost on its wiki page and prefer the cheaper one.
- **Evidence basis:** Sampled wiki pages show the table at 15-120 Scrap against tree prices of 125-500 [11][14][15].
- **Confidence:** Medium. The comparison rests on undated wiki pages and a small sample; the table requires holding the item itself.
- **So what:** Keep a found item for the table instead of paying tree prices.

## Guidance 2 — Recheck costs at each monthly update

- **Guidance:** Treat all scrap numbers as provisional and recheck in game after each first-Thursday update.
- **Evidence basis:** Costs changed twice in two months (Meta Shift, Pivot or Die) and Livestock lines do not confirm values [1][2][3].
- **Confidence:** Medium. Pattern is documented, but future changes are not predictable.
- **So what:** Cite a date when sharing costs.

# Open Questions

- Do the wiki tech tree prices (125/250/500) reflect the post-November 2025 values? Pivot or Die gives only the four rarity figures and says tech tree tax was removed, and the sampled tree prices are not those figures [3][11][14].
- Did Meta Shift Part 2 ship in December 2025 or later? No Facepunch source was found [2].
- Are monthly forced blueprint wipes on official servers still in force? Only a Rustafied edit supports it [18].
- Exact Workbench 2 and 3 scrap cost before 6 November 2025 was never published [2].
- Whether any rarity value changed in 2026 updates other than Livestock; later changelists were not read.

# References

Cite every factual claim. Numbered contiguously from [1].

**Primary Sources**

- [1] **Facepunch** — *Livestock Update*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [2] **Facepunch** — *Meta Shift*. https://rust.facepunch.com/news/meta-shift/. Accessed 2026-10-08.
- [3] **Facepunch** — *Pivot or Die*. https://rust.facepunch.com/news/pivot-or-die. Accessed 2026-10-08.
- [4] **Facepunch** — *Devblog 180*. https://rust.facepunch.com/news/devblog-180. Accessed 2026-10-08.
- [5] **Facepunch** — *Devblog 185*. https://rust.facepunch.com/news/devblog-185. Accessed 2026-10-08.
- [6] **Rust Wiki (Facepunch)** — *Workbench Level 2*. https://wiki.facepunch.com/rust/item/workbench2. Accessed 2026-10-08.
- [7] **Rust Wiki (Facepunch)** — *Workbench Level 3*. https://wiki.facepunch.com/rust/item/workbench3. Accessed 2026-10-08.
- [8] **Rust Wiki (Facepunch)** — *Research Table*. https://wiki.facepunch.com/rust/item/research.table. Accessed 2026-10-08.
- [9] **Rust Wiki (Facepunch)** — *Blueprint*. https://wiki.facepunch.com/rust/item/blueprintbase. Accessed 2026-10-08.
- [10] **Rust Wiki (Facepunch)** — *Scrap*. https://wiki.facepunch.com/rust/item/scrap. Accessed 2026-10-08.
- [11] **Rust Wiki (Facepunch)** — *Salvaged Sword*. https://wiki.facepunch.com/rust/item/salvaged.sword. Accessed 2026-10-08.
- [12] **Rust Wiki (Facepunch)** — *Python Revolver*. https://wiki.facepunch.com/rust/item/pistol.python. Accessed 2026-10-08.
- [13] **Rust Wiki (Facepunch)** — *Pump Shotgun*. https://wiki.facepunch.com/rust/item/shotgun.pump. Accessed 2026-10-08.
- [14] **Rust Wiki (Facepunch)** — *Assault Rifle*. https://wiki.facepunch.com/rust/item/rifle.ak. Accessed 2026-10-08.
- [15] **Rust Wiki (Facepunch)** — *Metal Facemask*. https://wiki.facepunch.com/rust/item/metal.facemask. Accessed 2026-10-08.
- [16] **Rust Wiki (Facepunch)** — *Auto Turret*. https://wiki.facepunch.com/rust/item/autoturret. Accessed 2026-10-08.
- [17] **Rust Wiki (Facepunch)** — *Semi-Automatic Pistol*. https://wiki.facepunch.com/rust/item/pistol.semiauto. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- [18] **Rustafied** — *Meta shifts, BP wipe and box sorting* (30 October 2025). https://www.rustafied.com/updates/2025/10/30/meta-shifts-bp-wipe-and-box-sorting. Accessed 2026-10-08.

**Further Reading**

- See the Further Reading section below.

# Further Reading

- Rust Wiki, Research Paper: https://wiki.facepunch.com/rust/item/researchpaper

# Related Documents

- rust-items-crafting-foundation
- rust-updates-meta-foundation
- rust-economy-trading
- rust-monuments-loot
- rust-tools-gathering
- rust-wipes-map-generation
- rust-base-building-mechanics

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
