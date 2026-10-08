---
id: rust-clothing-armour
title: "Rust Clothing and Armour"
version: 1.0.0
status: frozen
confidence: Medium
category: Items & Crafting
topic: "Clothing and armour"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-items-crafting-foundation, rust-game-mechanics-foundation, rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence, rust-monuments-loot, rust-skins-cosmetics, rust-tools-gathering]
tags: [clothing, armour, armor, protection, hazmat, heavy-plate, radiation, cold, crafting]
game_build_checked: "Livestock Update, 1 October 2026 (wiki pages undated)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-clothing-armour |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Items & Crafting |
| Region | Global |
| Game build checked | Livestock Update, 1 October 2026 (wiki pages undated) |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This deep-dive extends rust-items-crafting-foundation with the wearable side of the game: the slot and layer model, per-item protection percentages, the cold penalty carried by metal gear, radiation protection, and the workbench, ingredient and research costs listed on Facepunch wiki item pages. Values were read on 2026-10-08, when the Livestock Update (1 October 2026) was the latest update [1]. Combat results are covered in rust-combat-damage-model and are not repeated here.

Document confidence is Medium. Every per-item number comes from a Facepunch wiki item page, but those pages are undated, do not state body areas, and do not say how stacked items combine numerically; the wiki only says both stacked items contribute their stats [2]. Warmth is not a separate stat on the pages opened, only a Cold protection percentage.

# Key Facts

- Head, Chest and Legs each have two layers (Layer 1 clothing, Layer 2 armour); Hands and Feet take one item each; full-body suits replace every slot [2].
- Some items occupy both layers of a slot, so nothing else fits there: Metal Facemask, Coffee Can Helmet, Heavy Plate Jacket, Heavy Plate Pants [2].
- The Heavy Plate set lists 75 to 90% projectile and 70 to 80% melee protection with 100% explosion, but Cold of -67% (jacket), -17% (pants) and -16% (helmet) [5][6][7].
- The Hazmat Suit lists Radiation 50% and Cold 50% with 30% projectile, melee and explosion, and needs Workbench Level 2 [8].
- Wood armour and the Hide Vest are known by default and need no workbench [16][17][18].
- No clothing or armour value change is listed in the Livestock Update changelog [1].
- Armour and cold protection trade off: metal pieces carry negative Cold values *(assessed from the tables below)*.

# Scope

Covered: clothing slots and layers, protection values and craft requirements for a selected set of wiki-listed items, radiation and cold protection, and repair and research costs, on vanilla PC servers at the Livestock Update. Not covered: how damage is calculated in combat (see rust-combat-damage-model), weapons (rust-weapons-ammo), skins (rust-skins-cosmetics), and items not opened for this document, including the Snow Jacket, Bone Armor, Arctic Suit, Wetsuit, gloves and boots, whose stats were not read. Modded servers and console are excluded.

# Definitions

- **Layer 1 / Layer 2:** the clothing layer worn underneath and the armour layer on top, for Head, Chest and Legs [2].
- **Dual-layer item:** an item occupying both layers of one slot [2].
- **Protection:** a percentage per damage type listed on an item page, such as Projectile, Melee, Bite, Radiation, Cold and Explosion [3][5].
- **Negative protection:** a listed value below zero, for example Cold -34% [4].

# Core Mechanics

**Evidence layer.**

**Slots and layers.** The Facepunch wiki states that Head, Chest and Legs each have two layers. Head Layer 1 holds hats and bandanas, Layer 2 helmets and face masks; Chest Layer 1 holds shirts and hoodies, Layer 2 jackets and plate carriers; Legs Layer 1 holds pants and shorts, Layer 2 kilts and plate legs. Hands and Feet hold one item each [2].

**Stacking.** One item per layer may be worn, so two items per slot, for example a Hoodie with a Road Sign Jacket or Pants with a Road Sign Kilt. The wiki says both stacked items contribute their stats and that Layer 1 provides comfort and cold resistance while Layer 2 provides projectile and melee protection, but it gives no numbers for how contributions combine [2]. A community guide dated 11 June 2026 repeats that "both layers contribute their stats" [19]. Item pages are not fully consistent with that generalisation: the Hoodie (Layer 1) lists Projectile 20% and Melee 15% [9], and the Jacket is listed on the Armor layer with Cold 40% [10].

**Dual-layer and multi-slot items.** The wiki lists the Metal Facemask and Coffee Can Helmet (Head), Heavy Plate Jacket and Snow Jacket (Chest) and Heavy Plate Pants (Legs) as occupying both layers. Bone Armor covers Chest and Legs plus Hands and Feet; the Wetsuit takes Chest and Legs Layer 1 only; the Chicken Costume takes Chest and Legs Layer 2 only [2]. The Hazmat Suit and Arctic Suit are full-body and exclude all other clothing [2]. The Hazmat Suit page lists slot and layer as Full Body [8].

**Protection is per damage type, not warmth.** Item pages list Cold as a protection percentage; no separate warmth value was found on any page opened [3][4][8][9]. Metal and plate items list negative Cold, while cloth items list positive Cold [4][5][9][11].

**Radiation.** Most items list small Radiation protection (3 to 7%); the Hazmat Suit lists 50% [8][9][14][15][18]. The radiation levels of monuments are outside this document; see rust-monuments-loot and rust-game-mechanics-foundation.

**Crafting, research and repair.** Each page lists a recipe, a required workbench with craft times per level, Research Table cost and Workbench Tech Tree cost, and a Repair Bench cost with 20% condition loss for repairable items [3][4][5][8]. The Hoodie and Wood Chestplate pages list Repairable as False [9][16]. Wood armour and Hide Vest pages state that the blueprint is known by default [16][17][18].

# Reference Data

**Evidence layer.** Checked 2026-10-08 against the Livestock Update. Slot and layer as stated on each page; "n/s" means not stated on the page. Columns are Projectile, Melee, Bite, Radiation, Cold and Explosion percentages; a dash means the page lists no value.

| Item | Slot (layer) | Proj | Melee | Bite | Rad | Cold | Expl | Source |
|------|--------------|------|-------|------|-----|------|------|--------|
| Hide Vest | Chest (Clothing) | 15 | 15 | 34 | 3 | 20 | - | [18] |
| Hoodie | Chest (Clothing) | 20 | 15 | 23 | 5 | 34 | - | [9] |
| Jacket | Chest (Armor) | 15 | 20 | 27 | 5 | 40 | - | [10] |
| Pants | Legs (Clothing) | 15 | 15 | 3 | 5 | 8 | - | [11] |
| Wood Chestplate | n/s | 10 | 40 | 20 | 5 | - | 30 | [16] |
| Wood Armor Pants | Legs (Armor) | 10 | 40 | 5 | 5 | - | 30 | [17] |
| Riot Helmet | Head (Armor) | 25 | 80 | 13 | 5 | 6 | 50 | [15] |
| Coffee Can Helmet | Head (Clothing and Armor) | 35 | 50 | 8 | 5 | - | 50 | [14] |
| Metal Facemask | Head (Clothing and Armor) | 50 | 70 | 8 | - | -4 | 50 | [3] |
| Road Sign Jacket | Chest (Armor) | 20 | 20 | 40 | - | -34 | - | [12] |
| Road Sign Kilt | Legs (Armor) | 20 | 20 | 10 | - | -8 | - | [13] |
| Metal Chest Plate | Chest (Armor) | 25 | 20 | 13 | - | -34 | - | [4] |
| Heavy Plate Helmet | Head (Armor) | 90 | 80 | 13 | 7 | -16 | 100 | [7] |
| Heavy Plate Jacket | Chest (Clothing and Armor) | 75 | 70 | 47 | 7 | -67 | 100 | [5] |
| Heavy Plate Pants | Legs (Clothing and Armor) | 75 | 70 | 12 | 7 | -17 | 100 | [6] |
| Hazmat Suit | Full Body | 30 | 30 | 50 | 50 | 50 | 30 | [8] |

Heavy Plate extras: Jacket Movement Speed Reduction 0.2, Blocks Aiming 1, Weight 10 [5]; Pants Movement Speed Reduction 0.1 [6]; Helmet Movement Speed Reduction 0.1, Weight 10, described as offering "reduced vision and movement speed" [7].

| Item | Ingredients | Workbench (craft time) | Research Table; Tech Tree scrap | Source |
|------|-------------|------------------------|----------------------------------|--------|
| Hide Vest | 10 Leather | none (30 s) | 120; known by default | [18] |
| Wood Chestplate | 250 Wood, 20 Cloth | none (30 s) | 30; known by default | [16] |
| Wood Armor Pants | 150 Wood, 15 Cloth | none (20 s) | 30; known by default | [17] |
| Pants | 40 Cloth, 1 Sewing Kit | Level 1 (30 s) | 30; 125 | [11] |
| Jacket | 50 Cloth, 2 Sewing Kit | Level 1 (30 s) | 15; 125 | [10] |
| Riot Helmet | 50 Metal Fragments, 10 Cloth | Level 1 (30 s) | 30; 125 | [15] |
| Hoodie | 40 Cloth, 1 Sewing Kit | Level 2 (30 s) | 30; 250 | [9] |
| Coffee Can Helmet | 60 Metal Fragments, 15 Cloth, 1 Sewing Kit | Level 2 (30 s) | 30; 250 | [14] |
| Road Sign Jacket | 20 Leather, 2 Road Signs, 2 Sewing Kit | Level 2 (30 s) | 30; 250 | [12] |
| Road Sign Kilt | 10 Leather, 1 Road Sign, 2 Sewing Kit | Level 2 (30 s) | 30; 250 | [13] |
| Heavy Plate Jacket | 4 High Quality Metal, 2 Sheet Metal | Level 2 (45 s) | 60; 250 | [5] |
| Heavy Plate Pants | 4 High Quality Metal, 1 Sheet Metal | Level 2 (45 s) | 60; 250 | [6] |
| Heavy Plate Helmet | 4 High Quality Metal, 1 Sheet Metal | Level 2 (45 s) | 60; 250 | [7] |
| Hazmat Suit | 8 High Quality Metal, 5 Tarp, 2 Sewing Kit | Level 2 (20 s) | 60; 250 | [8] |
| Metal Facemask | 50 Leather, 15 High Quality Metal, 6 Sewing Kit | Level 3 (45 s) | 120; 500 | [3] |
| Metal Chest Plate | 50 Leather, 18 High Quality Metal, 8 Sewing Kit | Level 3 (45 s) | 120; 500 | [4] |

Arithmetic from the table: the three Heavy Plate pieces together list 12 High Quality Metal and 4 Sheet Metal *(sum of [5][6][7])*.

Repair Bench examples, each with 20% condition loss: Hazmat Suit 108 Cloth and 2 High Quality Metal [8]; Metal Facemask 24 Cloth, 10 Leather, 3 High Quality Metal [3]; Heavy Plate Jacket 80 Metal Fragments and 1 High Quality Metal [5].

# Version & Patch Notes

**Evidence layer.**

- Livestock Update (1 October 2026): the changelog lists a Plague Hazmat Suit skin, an oil rig radiation start fix, and attack-helicopter armour plate behaviour, with no stated change to general clothing, Heavy Plate, wood armour, temperature or cold [1].
- Wiki item pages carry no build or date, so each value is "as shown on 2026-10-08" [3][5].
- Volatile: a June 2026 community guide warns Facepunch tweaks values most months, and its figures for Hazmat and Heavy Plate match the wiki pages read here [19][5][8].

# Common Pitfalls

- Wearing metal with no warm Layer 1 item in a cold biome. Metal and plate items list negative Cold [4][5], and the community guide advises backing them with warm Layer 1 clothing [19].
- Trying to wear a shirt under a Heavy Plate Jacket or a hat under a Metal Facemask. These occupy both layers [2].
- Expecting the Hazmat Suit to be a combat suit. It lists 30% projectile and melee [8].
- Assuming percentages add. The wiki says both layers contribute but gives no formula [2].
- Planning repairs for every item. The Hoodie and Wood Chestplate list Repairable False [9][16].

# Interactions & Related Systems

Damage dealt to armoured targets, hit areas and headshots: rust-combat-damage-model, which already lists Metal Facemask, Road Sign Jacket and Hazmat values and which this document extends. Crafting infrastructure, scrap and research: rust-items-crafting-foundation [3]. Radiation sources and survival: rust-game-mechanics-foundation and rust-monuments-loot. Ammunition: rust-weapons-ammo. Explosive protection values of 100% on Heavy Plate [5] interact with raiding tactics; see rust-raiding-costs-defence. Cosmetic skins on clothing: rust-skins-cosmetics.

# Assessed Guidance

## Guidance 1 — Pair every metal or plate piece with warm Layer 1 clothing in cold areas

- **Guidance:** Treat Cold as a cost of armour and choose Layer 1 items to offset it.
- **Evidence basis:** Metal Chest Plate -34, Road Sign Jacket -34, Heavy Plate Jacket -67 versus Hoodie +34 [4][12][5][9]; layers both contribute [2].
- **Confidence:** Medium. Values are primary; the net temperature result is not sourced.
- **So what:** Check your cold status in game after changing gear.

## Guidance 2 — Choose Hazmat for radiation and Heavy Plate for fights, not one for both

- **Guidance:** Use the Hazmat Suit when radiation is the threat and Heavy Plate when player damage is.
- **Evidence basis:** Hazmat Radiation 50%, Projectile 30% [8]; Heavy Plate Radiation 7%, Projectile 75 to 90% [5][6][7].
- **Confidence:** Medium. It rests on listed percentages; radiation intensity is not covered.
- **So what:** Hazmat occupies every slot, so you cannot add armour on top [2].

## Guidance 3 — Early armour is cheap and workbench-free but narrow

- **Guidance:** Wood armour suits early melee fights; do not expect it to stop bullets.
- **Evidence basis:** Wood Chestplate Melee 40%, Projectile 10%, known by default [16][17].
- **Confidence:** Medium. Values primary; fight outcomes are inference.
- **So what:** Upgrade toward Road Sign or Heavy Plate once a workbench is available [5][12].

# Open Questions

- How the two layers' percentages combine numerically: the wiki says only that both contribute [2].
- Body areas covered by each item and the Wood Chestplate slot: not stated on the pages opened [16].
- Stats for Snow Jacket, Bone Armor, Arctic Suit, Wetsuit, gloves and boots: not opened.
- Warmth in degrees and the radiation-to-protection relationship: no Facepunch source found.
- Item durability (maximum condition): not on the pages opened.
- Whether Hazmat Suit variants differ from the base suit: the variant page URLs tried returned 404.

# References

**Primary Sources**

- [1] **Facepunch** — *Livestock Update*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [2] **Facepunch Rust Wiki** — *Clothing Slots*. https://wiki.facepunch.com/rust/Clothing_Slots. Accessed 2026-10-08.
- [3] **Facepunch Rust Wiki** — *Metal Facemask*. https://wiki.facepunch.com/rust/item/metal.facemask. Accessed 2026-10-08.
- [4] **Facepunch Rust Wiki** — *Metal Chest Plate*. https://wiki.facepunch.com/rust/item/metal.plate.torso. Accessed 2026-10-08.
- [5] **Facepunch Rust Wiki** — *Heavy Plate Jacket*. https://wiki.facepunch.com/rust/item/heavy.plate.jacket. Accessed 2026-10-08.
- [6] **Facepunch Rust Wiki** — *Heavy Plate Pants*. https://wiki.facepunch.com/rust/item/heavy.plate.pants. Accessed 2026-10-08.
- [7] **Facepunch Rust Wiki** — *Heavy Plate Helmet*. https://wiki.facepunch.com/rust/item/heavy.plate.helmet. Accessed 2026-10-08.
- [8] **Facepunch Rust Wiki** — *Hazmat Suit*. https://wiki.facepunch.com/rust/item/hazmatsuit. Accessed 2026-10-08.
- [9] **Facepunch Rust Wiki** — *Hoodie*. https://wiki.facepunch.com/rust/item/hoodie. Accessed 2026-10-08.
- [10] **Facepunch Rust Wiki** — *Jacket*. https://wiki.facepunch.com/rust/item/jacket. Accessed 2026-10-08.
- [11] **Facepunch Rust Wiki** — *Pants*. https://wiki.facepunch.com/rust/item/pants. Accessed 2026-10-08.
- [12] **Facepunch Rust Wiki** — *Road Sign Jacket*. https://wiki.facepunch.com/rust/item/roadsign.jacket. Accessed 2026-10-08.
- [13] **Facepunch Rust Wiki** — *Road Sign Kilt*. https://wiki.facepunch.com/rust/item/roadsign.kilt. Accessed 2026-10-08.
- [14] **Facepunch Rust Wiki** — *Coffee Can Helmet*. https://wiki.facepunch.com/rust/item/coffeecan.helmet. Accessed 2026-10-08.
- [15] **Facepunch Rust Wiki** — *Riot Helmet*. https://wiki.facepunch.com/rust/item/riot.helmet. Accessed 2026-10-08.
- [16] **Facepunch Rust Wiki** — *Wood Chestplate*. https://wiki.facepunch.com/rust/item/wood.armor.jacket. Accessed 2026-10-08.
- [17] **Facepunch Rust Wiki** — *Wood Armor Pants*. https://wiki.facepunch.com/rust/item/wood.armor.pants. Accessed 2026-10-08.
- [18] **Facepunch Rust Wiki** — *Hide Vest*. https://wiki.facepunch.com/rust/item/attire.hide.vest. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- [19] **XGamingServer** — *Rust Armor & Clothing Guide: Best Sets and Protection* (11 June 2026). https://xgamingserver.com/blog/rust-armor-clothing-guide/. Accessed 2026-10-08.

**Further Reading**

- None.

# Further Reading

The Facepunch Rust Wiki pages for clothing items not opened here (Snow Jacket, Bone Armor, Arctic Suit, gloves, boots).

# Related Documents

rust-items-crafting-foundation, rust-combat-damage-model, rust-game-mechanics-foundation, rust-weapons-ammo, rust-raiding-costs-defence, rust-monuments-loot, rust-skins-cosmetics, rust-tools-gathering.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
