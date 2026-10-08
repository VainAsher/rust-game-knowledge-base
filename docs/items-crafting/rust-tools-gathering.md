---
id: rust-tools-gathering
title: "Rust Tools and Gathering"
version: 1.0.0
status: frozen
confidence: Medium
category: Items & Crafting
topic: "Tools and gathering"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-items-crafting-foundation, rust-game-mechanics-foundation, rust-server-administration-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation, rust-server-convars-reference, rust-update-timeline-2026, rust-combat-damage-model, rust-weapons-ammo, rust-wildlife-npcs, rust-monuments-loot, rust-farming-food, rust-clothing-armour]
tags: [tools, gathering, pickaxe, hatchet, ore-nodes, recycler, hotspot, chainsaw, jackhammer]
game_build_checked: "Livestock Update, 1 October 2026 (wiki item pages undated; Power Trip, 6 August 2026, for recyclers)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-tools-gathering |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Items & Crafting |
| Region | Global |
| Game build checked | Livestock Update, 1 October 2026 [1]; Power Trip, 6 August 2026 [2]; Rust Wiki item pages carry no build stamp |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This document goes deeper than rust-items-crafting-foundation on the tools players use to collect resources: the rock, the stone and metal hatchets and pickaxes, the salvaged axe and icepick, the chainsaw and the jackhammer. It records what each tool costs, which targets it can harvest, the wiki's gather figures, how ore nodes and the hotspot minigame work, and what the recycler returns when a tool is broken down.

The headline limit is that no Facepunch page opened states the resource yield per hit. The wiki lists a "Gather Damage" and a "Bonus" figure per target but does not explain them, so this document reports them as published and does not convert them into resources per swing. The foundation's gather-rate gap therefore stays open. Confidence is Medium: item data and recycler efficiency come from first-party sources, but the wiki pages are undated and the gather columns are undefined.

# Key Facts

- Ore nodes come in three types, stone, sulfur and metal, and are found around cliffs and rock formations [4].
- The hotspot minigame (Devblog 170, 27 July 2017) raises a hit to 150% and consecutive hits to 300%, but Facepunch states it does not increase the total resources in a node [3][4].
- Wiki "Gather Damage" per target: Rock 5 (ore) and 10 (tree); Stone Pickaxe 16 (ore); Pickaxe 30 (ore); Salvaged Icepick 50 (ore); Jackhammer 25 (ore); Stone Hatchet 20 (tree); Hatchet 30 (tree); Salvaged Axe 50 (tree); Chainsaw 30 (tree) [5][6][7][8][9][10][11][12][13].
- The Jackhammer is not craftable and not researchable; the wiki lists airdrops and locked crates as loot sources [13].
- Since Power Trip (6 August 2026), green recyclers run at 50% efficiency, restoring to 60% with sufficient Power Plant power, and a single red recycler at the Power Plant runs at 75% only at maximum power [2].
- Ore nodes and woodpiles can no longer spawn in safe zones, because they could only be harvested with a rock and piled up, draining the global spawn population [2].
- Vanilla Rust has no built-in gather-rate multiplier convar according to one hosting guide; multipliers need a plugin such as GatherManager *(community source)* [20].

# Scope

Covers vanilla PC Rust: hand tools for gathering, the three ore node types, the hotspot minigame, the ore and wood items nodes give, the recycler's effect on tools, and the admin-only quarry's status. Excludes console, modded recipes, weapon use of these tools in combat (see rust-combat-damage-model), animal harvesting detail (see rust-wildlife-npcs), and server gather-rate plugins beyond a note. Checked against the Livestock Update of 1 October 2026 [1].

# Definitions

- **Ore node** — a stone, sulfur or metal rock formation harvested with a pickaxe-class tool [4].
- **Hotspot** — a shimmering weak point on an ore node that boosts yield per hit [3][4].
- **Gather Damage / Bonus / Condition Loss** — the three columns the Rust Wiki prints per target; the wiki does not define the first two [5][8].
- **Recycler** — a station that converts items into components at a percentage of their value [14][15].
- **Safe Zone Recycler** — the protected recycler at Outpost and Bandit Camp, also called the yellow recycler [2][15].

# Core Mechanics

**Evidence layer.**

**Nodes.** The wiki names three ore node types: stone, sulfur and metal, mostly around cliffs, mountains and rock formations [4]. Harvesting yields ore items: Stones (stack 1000), Metal Ore (stack 1000) and Sulfur Ore (stack 1000), which the wiki lists as gathered from node sources [16][17][18]. Metal ore and sulfur ore are smelted in furnaces into Metal Fragments and Sulfur [16][18].

**Hotspot minigame.** Devblog 170 introduced a shimmering hotspot on nearby ore. Hitting one boosts gathering to 150%, each successive hit raises it, up to 300%, and a miss resets the bonus [3]. Facepunch states you do not earn more resources overall, but you harvest the node faster [3]. The devblog says hotspots are affected by sunlight and are invisible at night, and the wiki adds that they need illumination [3][4]. The Ore nodes wiki page is marked "Updated: A Long Time Ago", so current behaviour was not confirmed beyond these statements [4].

**Tool tiers.** Tools split into starter tools (Rock, Stone Hatchet, Stone Pickaxe, no workbench), Level 1 metal tools (Hatchet, Pickaxe), Level 2 salvaged tools (Salvaged Axe, Salvaged Icepick, Chainsaw) and the non-craftable Jackhammer [5][6][7][8][9][10][11][12][13]. Within the wiki's gather columns, each tier's Gather Damage figure is higher than the previous tier for its target, for example ore 5, 16, 30 and 50 for Rock, Stone Pickaxe, Pickaxe and Salvaged Icepick [5][7][9][11].

**Specialisation.** Per the wiki tables, hatchet-class tools list a Tree target, pickaxe-class tools list an Ore target, and the Rock lists both [5][6][7][8][9][10][11]. The wiki's Stone Pickaxe description says it harvests stone, metal ore and sulfur ore, but its table lists only one "Ore" row [5].

**Gather columns.** Each target row carries Gather Damage, Bonus and Condition Loss [5]. In every row opened, Bonus is one fifth of Gather Damage on Ore rows and one tenth on Tree and Flesh rows (for example Pickaxe ore 30 and 6, Hatchet tree 30 and 3) [5][7][8][9][11]. The wiki does not say what Bonus is, so its meaning is not asserted here.

**Fuel tools.** The Chainsaw requires Low Grade Fuel to run; no consumption rate is listed [12]. The Jackhammer's description says it can be refilled at a Workbench; no fuel figure is listed [13].

**Recycling tools.** Tools can be recycled: the Hatchet returns 60 Wood and 45 Metal Fragments at a Recycler and 40 Wood and 30 Metal Fragments at a Safe Zone Recycler [8]. Recyclers returned 100% of each listed output on the item pages [8]. The Recycler wiki page gives 60% yield at 5 seconds per item at monuments; the Safe Zone Recycler page gives 40% at 8 seconds per item at Outpost and Bandit [14][15]. Power Trip changed green recyclers to 50% by default, 60% with sufficient Power Plant power, with the cycle shortening from 5 s to 4.5 s at maximum power, and added a 75% red recycler [2]. Yellow recyclers were unchanged [2].

**Quarry.** The Mining Quarry wiki page says the item is admin-only and not available in normal gameplay; it lists no fuel or yield [19].

**Livestock.** The 1 October 2026 update lets livestock be harvested for meat, bones and leather like other animals, and sheep for wool [1].

# Reference Data

**Evidence layer.** Rust Wiki item pages, undated ("Updated: This Year"); read 2026-10-08. Recycler columns reflect the item pages' 100% outputs and are likely pre-Power Trip for green recyclers (see Open Questions).

| Tool | Craft cost | Workbench | Gather Damage (target) | Condition loss | Source |
|------|-----------|-----------|------------------------|----------------|--------|
| Rock | 10 Stones | None | 5 ore, 10 tree, 10 flesh | 0.3 ore, 0.3 tree | [7] |
| Stone Hatchet | 200 Wood, 100 Stones | None | 20 tree, 10 flesh | 0.3 | [6] |
| Stone Pickaxe | 200 Wood, 100 Stones | None | 16 ore, 10 flesh | 0.3 ore, 1 flesh | [5] |
| Hatchet | 100 Wood, 75 Metal Fragments | Level 1 | 30 tree, 12 flesh | 0.3 tree, 1 flesh | [8] |
| Pickaxe | 125 Metal Fragments, 100 Wood | Level 1 | 30 ore, 5 flesh | 1 ore, 1 flesh | [9] |
| Salvaged Axe | 5 Metal Blade, 1 Metal Pipe | Level 2 | 50 tree, 15 flesh | 0.3 tree, 1 flesh | [10] |
| Salvaged Icepick | 5 Metal Blade, 1 Metal Pipe | Level 2 | 50 ore, 5 flesh | 0.3 ore, 0.5 flesh | [11] |
| Chainsaw | 6 Metal Blade, 5 High Quality Metal, 2 Gears | Level 2 | 30 tree, 2 flesh | 0.1 tree | [12] |
| Jackhammer | not craftable | n/a | 25 ore, 5 flesh | 0.2 ore, 0.5 flesh | [13] |

| Tool | Recycler output (page, 100% unless noted) | Safe Zone Recycler output | Source |
|------|-------------------------------------------|---------------------------|--------|
| Rock | 6 Stones | 4 Stones | [7] |
| Stone Hatchet / Stone Pickaxe | 120 Wood, 60 Stones | 80 Wood, 40 Stones | [5][6] |
| Hatchet | 60 Wood, 45 Metal Fragments | 40 Wood, 30 Metal Fragments | [8] |
| Pickaxe | 75 Metal Fragments, 60 Wood | 50 Metal Fragments, 40 Wood | [9] |
| Salvaged Axe / Icepick | 3 Metal Blade; 1 Metal Pipe (60%) | 2 Metal Blade; 1 Metal Pipe (40%) | [10][11] |
| Chainsaw | 3 HQM, 3 Metal Blade, 1 Gears; 1 Metal Blade (60%), 1 Gears (20%) | 2 HQM, 2 Metal Blade; 1 Gears (80%), 1 Metal Blade (40%) | [12] |
| Jackhammer | 36 Scrap, 3 Metal Blade; 1 Metal Pipe (60%) | 24 Scrap, 2 Metal Blade; 1 Metal Pipe (40%) | [13] |

| Item | Stack | Wiki "gathered from" amount | Source |
|------|-------|-----------------------------|--------|
| Stones | 1000 | 750 (source "Stones", type Ore) | [17] |
| Metal Ore | 1000 | 500 (source "Metal Ore", type Ore) | [16] |
| Sulfur Ore | 1000 | 200 (source "Sulfur Ore", type Ore) | [18] |

The "gathered from" amounts are printed without explanation; they are not asserted to be per-node totals or per-hit yields.

| Recycler | Efficiency | Cycle time | Source |
|----------|-----------|------------|--------|
| Yellow (safe zone) | 40% (wiki), unchanged by Power Trip | 8 s | [2][15] |
| Green (monuments) | 50% default, 60% with Power Plant power (Power Trip, 6 Aug 2026); wiki still reads 60% | 5 s, 4.5 s at maximum power | [2][14] |
| Red (Power Plant, one) | 75%, maximum power only | not stated | [2] |

Starter tool repair at a Repair Bench costs 20 Stones or 40 Wood for the Stone Pickaxe, each at 20% condition loss [5]; salvaged tools take 30 Metal Fragments and 1 High Quality Metal at 20% [10][11]. The Jackhammer takes 30 Metal Fragments and 1 High Quality Metal at 5% [13].

# Version & Patch Notes

**Evidence layer.**

| Date | Update | Change | Source |
|------|--------|--------|--------|
| 27 Jul 2017 | Devblog 170 | Ore minigame (hotspots) added | [3] |
| 6 Aug 2026 | Power Trip | Green recyclers 50% default, 60% with power; red recycler (75%) added; ore nodes and woodpiles no longer spawn in safe zones | [2] |
| 1 Oct 2026 | Livestock | Livestock and sheep harvesting; machete art refresh; no change to gather tools, nodes or the recycler listed | [1] |

Volatile: every cost, Gather figure and recycler efficiency. Wiki pages carry no build stamp [5].

# Common Pitfalls

- Treating the wiki's Gather Damage as resources per hit. The wiki does not define it [5].
- Expecting hotspots to add resources. Facepunch says they only speed harvesting [3].
- Using the wiki's 60% recycler figure for every green recycler. Power Trip made 50% the unpowered default [2][14].
- Looking for a vanilla gather-rate convar. One hosting guide says none exists and a plugin is needed [20]; see rust-server-convars-reference, which found none on a Facepunch page.
- Expecting to find the Mining Quarry as a player item. The wiki marks it admin-only [19].

# Interactions & Related Systems

- Resources feed crafting, workbenches and furnaces; see rust-items-crafting-foundation [16][18].
- Stone and metal tools are also melee weapons with their own damage totals; see rust-combat-damage-model [5][9].
- Livestock harvesting overlaps with animal resources; see rust-wildlife-npcs and rust-farming-food [1].
- Fragments and tools drop from monument crates and airdrops; see rust-monuments-loot [13].
- Server gather multipliers sit in plugins, see rust-modding-plugins-foundation and rust-server-administration-foundation [20].
- The recycler change is part of the 2026 timeline; see rust-update-timeline-2026 [2].

# Assessed Guidance

**Judgement layer.**

## Guidance 1 — Do not quote tool efficiency as resources per hit

- **Guidance:** Compare tools by tier and the wiki's figures only as relative indicators, and test yields in game.
- **Evidence basis:** The wiki gives undefined Gather Damage and Bonus columns and Facepunch gives no per-hit yield [3][5][9].
- **Confidence:** Medium. The absence of a per-hit figure is established from pages opened, not proved globally.
- **So what:** Treat any "N wood per hit" claim as unverified unless it shows its build and method.

## Guidance 2 — Learn the hotspot rhythm before upgrading tools

- **Guidance:** Practise chaining hotspot hits, since the bonus can reach 300% per hit on the same node.
- **Evidence basis:** Devblog 170 and the Ore nodes page state 150% rising to 300%, with a miss resetting it [3][4].
- **Confidence:** Medium. The mechanism is primary, but the page is old and the benefit in practice is inferred.
- **So what:** Good aim shortens each node visit, which reduces exposure time at open nodes.

## Guidance 3 — Check which recycler colour you are using

- **Guidance:** Compare recycler efficiency before dumping valuable items, and expect powered Power Plant machines to differ from the rest.
- **Evidence basis:** Power Trip lists 50%, 60% and 75% tiers, while wiki pages list 60% and 40% [2][14][15].
- **Confidence:** Medium. The update is primary, but the on-screen display and current state were not verified in game.
- **So what:** Recycle at the best available machine, and re-read the update notes after each patch.

# Open Questions

- Resources yielded per hit for each tool and node, and the meaning of Gather Damage and Bonus. No primary source opened defines them; resolve by in-game measurement or Facepunch source data. The items foundation's gather-rate gap is not closed.
- Whether the item pages' Recycler outputs reflect 60% or the 50% default after Power Trip.
- Whether Hotspot behaviour changed after 2017; the wiki page is marked "A Long Time Ago" [4].
- Chainsaw and Jackhammer fuel use and durability: not listed on their pages [12][13].
- Mining Quarry status, and any deployable quarry in normal play [19].
- Whether a vanilla gather-rate convar exists; the only source is a hosting guide [20].

# References

Numbered contiguously from [1].

**Primary Sources**

- [1] **Facepunch** — *Livestock Update*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [2] **Facepunch** — *Power Trip*. https://rust.facepunch.com/news/power-trip. Accessed 2026-10-08.
- [3] **Facepunch** — *Devblog 170*. https://rust.facepunch.com/blog/devblog170/. Accessed 2026-10-08.
- [4] **Rust Wiki (Facepunch)** — *Ore nodes*. https://wiki.facepunch.com/rust/Ore_nodes. Accessed 2026-10-08.
- [5] **Rust Wiki (Facepunch)** — *Stone Pickaxe*. https://wiki.facepunch.com/rust/item/stone.pickaxe. Accessed 2026-10-08.
- [6] **Rust Wiki (Facepunch)** — *Stone Hatchet*. https://wiki.facepunch.com/rust/item/stonehatchet. Accessed 2026-10-08.
- [7] **Rust Wiki (Facepunch)** — *Rock*. https://wiki.facepunch.com/rust/item/rock. Accessed 2026-10-08.
- [8] **Rust Wiki (Facepunch)** — *Hatchet*. https://wiki.facepunch.com/rust/item/hatchet. Accessed 2026-10-08.
- [9] **Rust Wiki (Facepunch)** — *Pickaxe*. https://wiki.facepunch.com/rust/item/pickaxe. Accessed 2026-10-08.
- [10] **Rust Wiki (Facepunch)** — *Salvaged Axe*. https://wiki.facepunch.com/rust/item/axe.salvaged. Accessed 2026-10-08.
- [11] **Rust Wiki (Facepunch)** — *Salvaged Icepick*. https://wiki.facepunch.com/rust/item/icepick.salvaged. Accessed 2026-10-08.
- [12] **Rust Wiki (Facepunch)** — *Chainsaw*. https://wiki.facepunch.com/rust/item/chainsaw. Accessed 2026-10-08.
- [13] **Rust Wiki (Facepunch)** — *Jackhammer*. https://wiki.facepunch.com/rust/item/jackhammer. Accessed 2026-10-08.
- [14] **Rust Wiki (Facepunch)** — *Recycler*. https://wiki.facepunch.com/rust/Recycler. Accessed 2026-10-08.
- [15] **Rust Wiki (Facepunch)** — *Safe Zone Recycler*. https://wiki.facepunch.com/rust/Safe_Zone_Recycler. Accessed 2026-10-08.
- [16] **Rust Wiki (Facepunch)** — *Metal Ore*. https://wiki.facepunch.com/rust/item/metal.ore. Accessed 2026-10-08.
- [17] **Rust Wiki (Facepunch)** — *Stones*. https://wiki.facepunch.com/rust/item/stones. Accessed 2026-10-08.
- [18] **Rust Wiki (Facepunch)** — *Sulfur Ore*. https://wiki.facepunch.com/rust/item/sulfur.ore. Accessed 2026-10-08.
- [19] **Rust Wiki (Facepunch)** — *Mining Quarry*. https://wiki.facepunch.com/rust/item/mining.quarry. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- [20] **XGamingServer** — *How to Change Gather Rates on Your Rust Server*. https://xgamingserver.com/docs/rust/gather-rates. Accessed 2026-10-08.

**Further Reading**

- See the Further Reading section below.

# Further Reading

- Rust Wiki, Ore nodes: https://wiki.facepunch.com/rust/Ore_nodes

# Related Documents

- rust-items-crafting-foundation
- rust-combat-damage-model
- rust-weapons-ammo
- rust-wildlife-npcs
- rust-monuments-loot
- rust-server-convars-reference
- rust-update-timeline-2026

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
