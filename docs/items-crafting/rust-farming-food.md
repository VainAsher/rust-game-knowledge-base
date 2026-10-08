---
id: rust-farming-food
title: "Rust Farming and Food"
version: 1.0.0
status: frozen
confidence: Medium
category: Items & Crafting
topic: "Farming, food and cooking"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-items-crafting-foundation, rust-game-mechanics-foundation, rust-building-raiding-foundation, rust-server-administration-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation, rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence, rust-server-convars-reference, rust-plugin-development-hooks, rust-update-timeline-2026, rust-monuments-loot, rust-vehicles, rust-wipes-map-generation, rust-moderation-anti-cheat, rust-carbon-vs-oxide]
tags: [farming, food, cooking, planters, genetics, livestock, tea]
game_build_checked: "Livestock Update, 1 October 2026 (wiki pages undated)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-farming-food |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Items & Crafting |
| Region | Global |
| Game build checked | Livestock Update, 1 October 2026 [1]; Rust Wiki pages carry no build stamp |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This deep-dive covers how Rust food is produced and prepared: planters and plant genetics, the Cooking Workbench and its food and tea recipes, selected food stats, and the livestock products added by the Livestock Update of 1 October 2026. It goes deeper than rust-items-crafting-foundation, which only lists Food as a wiki category.

The Facepunch devblog confirms the livestock design (cows, sheep, genetics, milk, wool, the stable vendor, fencing) but gives almost no numbers [1]. Most numbers come from Rust Wiki pages that have no build date [2][3][4]. Confidence is Medium: the structure is primary-sourced, but values are undated and many gaps (growth times, crop yields, livestock gene mechanics) could not be sourced.

# Key Facts

- Each plant has six gene slots; the genes are G (growth), Y (yield), H (hardiness), W (water intake) and X (empty). W and X are the only bad genes [2].
- A Small Planter Box costs 100 Wood and 1 Tarp and holds 3 seeds [5].
- The Cooking Workbench requires Workbench Level 2 and costs 200 Metal Fragments, 200 Stones and 100 Wood [4].
- Pies and teas are mixed at the Cooking Workbench; pies take 30 s, bread 20 s, teas 5 s [4].
- The Livestock Update (1 October 2026) added cows and sheep with genetics, milk, wool, meat, bones, leather and a stable vendor [1].
- Milk refrigerated for 4 hours can be skimmed into Skimmed Milk and Cream; milk lengthens tea effects and cream increases their potency [1].
- Wool sales to the stable vendor are capped at 400 wool per trade and the vendor gives three offers [1].

# Scope

Covers vanilla PC Rust: planters, seeds and clones, plant genes, water supply for farms, the Cooking Workbench, food and tea recipes, sample food stats, and Livestock Update products. Excludes console, modded recipes and server convars (see rust-server-convars-reference and rust-plugin-development-hooks), and the hunger and thirst model itself (see rust-game-mechanics-foundation). Checked against the Livestock Update [1].

# Definitions

- **Gene** — one of six slots on a plant, letters G, Y, H, W, X [2].
- **Clone** — a copy of a plant that carries its genes, obtained from grown plants [3].
- **Planter** — a deployable that holds seeds, for example the Small Planter Box [5].
- **Cooking Workbench** — a deployable that mixes advanced food, tea, fuel and ammunition recipes [4].
- **Stable vendor** — NPC at a Stable who buys grown animals and wool [1].

# Core Mechanics

**Evidence layer.**

**Planting and genes.** Seeds drop from picking wild plants, for example corn, and can be planted in the ground or in a planter [7]. Planting in a planter with large quantities of water gives more produce and faster growth, though the wiki does not quantify this [7]. Each plant has six gene slots, assigned randomly when the seed is planted [2]. Planting several plants adjacent lets one plant's genes override others through crossbreeding [2].

**Genes.** G raises growth rate, Y raises yield, H raises resistance to bad temperatures and biomes, W raises water consumption and can make a plant unhealthy if it dominates, and X is an empty slot [2][3]. The wiki states the combinations GGGYYY and GGYYYY: the first gives higher production and 3 clones when cloned, the second slightly lower production and 4 clones [3].

**Water supply.** The wiki's Farming Basics describes sprinkler farms. Freshwater is supplied by a powered water pump to up to 4 sprinklers; salt water needs 2 pumps into a powered water purifier; a modular car water tanker can feed water barrels, each supporting up to 6 sprinklers [3]. A 3-planter layout fills at 5 mL and a 6-planter layout at 4 mL; in the 3-planter layout sprinklers must not see more than three planters [3].

**Fertiliser.** The Composter produces fertiliser from compostable items [8].

**Cooking.** The Cooking Workbench cooks raw meats into cooked versions in 3.8 s (fish 2.5 s, horse 3.2 s) and mixes pies, bread and teas [4]. Teas come in tiers: four basic teas make one Advanced tea, and four Advanced make one Pure tea of the same type [4].

**Livestock.** Cows and sheep both produce dung; cows also give milk and sheep wool; animals can be harvested for meat, bones and leather [1]. Animals have genetics and needs and can be bred, but the devblog says genes "won't behave exactly like plants", so plant breeding techniques may not transfer [1]. Grown animals can be sold at a Stable for resources based on gene quality, with up to three offers; after rejecting the third, the vendor refuses that animal for 15 minutes [1]. Animal gates and fences contain livestock, and with the new navmesh NPCs can enter player structures [1]. The Biofuel Generator turns organic matter, including raw or spoiled meat, into Low Grade Fuel and needs stirring again after about 30 minutes [1].

**Milk chain.** Milk can be drunk as is; after 4 hours refrigerated it can be skimmed into Skimmed Milk and Cream [1]. New Creamy and Milky variants of most pure teas were added [1].

# Reference Data

**Evidence layer.** Wiki values are undated; treat as current to the October 2026 Livestock Update but unconfirmed [4][5][6][8].

| Item | Cost or stat | Source |
|------|--------------|--------|
| Small Planter Box | 100 Wood, 1 Tarp; research 15 Scrap; stack 10; holds 3 seeds | [5] |
| Composter | 200 Wood, 2 Tarp; research 120 Scrap | [8] |
| Cooking Workbench | 200 Metal Fragments, 200 Stones, 100 Wood; needs Workbench L2; research 30 Scrap | [4] |
| Corn seed | Stack 50 | [7] |

| Food | Calories | Hydration | Health effect | Stack | Source |
|------|----------|-----------|---------------|-------|--------|
| Hunters Pie | +80 | +15 | +2 instant; Bleed Resistance +0.75 for 15 min | 3 | [6] |
| Cooked Chicken | +40 | +3 | Healing Over Time +10 | 20 | [9] |
| Pumpkin | +80 | +30 | Healing Over Time +8 over 30 s | 20 | [10] |

| Cooking Workbench recipe | Ingredients | Time | Source |
|--------------------------|-------------|------|--------|
| Bread Loaf | Wheat x5 | 20 s | [4] |
| Pumpkin Pie | Wheat x3, Egg x3, Pumpkin | 30 s | [4] |
| Apple Pie | Wheat x3, Apple, Jar of Honey x2 | 30 s | [4] |
| Hunters Pie | Wheat x3, Egg x3, Mushroom x2, Potato x2, Cooked Deer Meat x2 | 30 s | [4] |
| Chicken Pie | Wheat x3, Egg x3, Corn x3, Cooked Chicken x3 | 30 s | [4] |

| Basic tea | Ingredients (berry colours) | Source |
|-----------|-----------------------------|--------|
| Healing | Red x4 | [4] |
| Max Health | Red x3, Yellow x1 | [4] |
| Anti-Rad | Red x2, Green x2 | [4] |
| Harvesting | Yellow x1, Green x3 | [4] |
| Cooling | White x2, Blue x2 | [4] |
| Warming | White x2, Yellow x2 | [4] |

Basic teas take 5 s each; other basic teas (Crafting Quality, Ore, Scrap, Wood) also exist [4].

# Version & Patch Notes

**Evidence layer.**

| Date | Update | Change | Source |
|------|--------|--------|--------|
| 1 Oct 2026 | Livestock | Cows, sheep, milk, skimmed milk, cream, wool, Beef and Mutton Meat, Shepherd's Pie, Beef Pie, creamy and milky teas, stable vendor, animal fences, Biofuel Generator; horses drop less dung | [1] |

The devblog gives no ingredient counts or yields for the new items, so those values are volatile and unsourced [1]. The next update listed by Facepunch is the Halloween Update on 22 October [1].

# Common Pitfalls

- Letting W (water) genes dominate makes a plant unhealthy [2].
- Putting too many planters in sprinkler line of sight in the 3-planter layout leaves them under-watered [3].
- Assuming plant breeding rules apply to livestock; Facepunch warns they do not behave the same [1].
- Rejecting the third vendor offer locks that animal out of sale for 15 minutes [1].
- Quoting recipe or stat numbers without a date, since wiki pages are unstamped [4][6].

# Interactions & Related Systems

- Tea buffs and food calories feed the survival model; see rust-game-mechanics-foundation.
- Workbench Level 2 gating for the Cooking Workbench; see rust-items-crafting-foundation [4].
- Low Grade Fuel is both a Cooking Workbench mix and a Biofuel Generator output [1][4]; Cooking Workbench ammunition recipes link to rust-weapons-ammo [4].
- NPC animals entering player structures matters for base design; see rust-building-raiding-foundation [1].
- Food crates and loot sources are covered in rust-monuments-loot.
- Server-side growth or yield settings are not verified here; see rust-server-convars-reference.

# Assessed Guidance

**Judgement layer.**

## Guidance 1 — Aim for Y and G genes and avoid W when selecting clones

- **Guidance:** Prefer clones with a G and Y heavy gene set and discard W and X heavy plants.
- **Evidence basis:** The wiki describes G and Y as beneficial and W and X as the only bad genes [2][3].
- **Confidence:** Medium. Gene effects are primary-wiki sourced, but optimal ratios are not quantified.
- **So what:** A small farm of good clones saves labour compared with replanting random seeds.

## Guidance 2 — Treat livestock numbers as unknown until tested on your server

- **Guidance:** Do not plan a wool or milk economy from this document; test yields and recipes in game.
- **Evidence basis:** The devblog lists features but no quantities [1].
- **Confidence:** High. The absence of numbers is directly observable in the source.
- **So what:** Record observed yields with the date, and recheck after each monthly update.

## Guidance 3 — Use sprinkler layout rules from the wiki before scaling a farm

- **Guidance:** Start with the 3-planter layout for small farms and move to the 6-planter layout when scaling.
- **Evidence basis:** The wiki describes each layout's fill rate and line of sight constraint [3].
- **Confidence:** Medium. Layout advice is wiki-sourced and the wiki is undated.
- **So what:** Fewer dry planters and less rework.

# Open Questions

- Plant growth times, yields and temperature or light requirements: not stated on the pages checked [3][7].
- Composter inputs and fertiliser yield: the wiki page omits them [8].
- Livestock gene mechanics, feed needs, breeding rules, milk and wool yields and fence stats: not given in the devblog [1].
- Recipes and stats for Shepherd's Pie, Beef Pie and the creamy teas: no source found.
- Whether the 400-wool cap and 15-minute lockout have changed since launch.

# References

**Primary Sources**

- [1] **Facepunch** — *Livestock Update*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [2] **Facepunch Rust Wiki** — *Farming and Genetics*. https://wiki.facepunch.com/rust/Farming. Accessed 2026-10-08.
- [3] **Facepunch Rust Wiki** — *Farming Basics*. https://wiki.facepunch.com/rust/Farming_Basics. Accessed 2026-10-08.
- [4] **Facepunch Rust Wiki** — *Cooking Workbench*. https://wiki.facepunch.com/rust/item/cookingworkbench. Accessed 2026-10-08.
- [5] **Facepunch Rust Wiki** — *Small Planter Box*. https://wiki.facepunch.com/rust/item/planter.small. Accessed 2026-10-08.
- [6] **Facepunch Rust Wiki** — *Hunters Pie*. https://wiki.facepunch.com/rust/item/pie.hunters. Accessed 2026-10-08.
- [7] **Facepunch Rust Wiki** — *Corn Seed*. https://wiki.facepunch.com/rust/item/seed.corn. Accessed 2026-10-08.
- [8] **Facepunch Rust Wiki** — *Composter*. https://wiki.facepunch.com/rust/item/composter. Accessed 2026-10-08.
- [9] **Facepunch Rust Wiki** — *Cooked Chicken*. https://wiki.facepunch.com/rust/item/chicken.cooked. Accessed 2026-10-08.
- [10] **Facepunch Rust Wiki** — *Pumpkin*. https://wiki.facepunch.com/rust/item/pumpkin. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- None cited.

**Further Reading**

- See the Further Reading section below.

# Further Reading

- Rust Wiki home: https://wiki.facepunch.com/rust/

# Related Documents

- rust-items-crafting-foundation
- rust-monuments-loot
- rust-weapons-ammo
- rust-game-mechanics-foundation
- rust-server-convars-reference

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
