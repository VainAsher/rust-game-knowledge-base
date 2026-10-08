---
id: rust-combat-damage-model
title: "Rust Combat and Damage Model"
version: 1.0.0
status: frozen
confidence: Medium
category: Game Mechanics
topic: "Combat and damage"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-building-raiding-foundation, rust-server-administration-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation, rust-weapons-ammo, rust-raiding-costs-defence, rust-server-convars-reference, rust-plugin-development-hooks, rust-update-timeline-2026]
tags: [combat, damage, headshot, armour, clothing, melee, bleeding, explosives, fall-damage]
game_build_checked: "Livestock Update (1 October 2026)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-combat-damage-model |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Game Mechanics |
| Region | Global |
| Game build checked | Livestock Update (1 October 2026) |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This deep-dive extends the survival overview in rust-game-mechanics-foundation by explaining how damage is dealt and reduced in Rust: per-ammunition base damage and headshot multipliers, how clothing and armour reduce damage by damage type and body area, how melee compares with ranged fire, how bleeding is generated and treated, and what is and is not sourced for explosions and falls. Values were read from the Facepunch Rust Wiki item pages on 2026-10-08, when the Livestock Update (1 October 2026) was the latest update [1].

Document confidence is Medium. Per-item numbers come from Facepunch's own wiki, but the wiki pages omit several mechanics: there is no sourced hit-zone table beyond the headshot multiplier, no sourced fall-damage formula, and no sourced explosion damage numbers. The bleeding formula comes from a single community article that states no build [18]. Those gaps are listed in Open Questions rather than filled from memory.

# Key Facts

- The Facepunch wiki lists a headshot multiplier of x2 for 5.56 rifle ammunition, pistol ammunition and the Salvaged Sword, x1.5 for Hunting Bow arrows, and x1 to x2 for shotgun ammunition depending on type (checked against the Livestock Update) [3][6][7][8][9].
- Clothing lists the body parts it protects, and damage is reduced according to which body part was hit; clothing does not change hitbox size [2].
- Protection is expressed per damage type: the Metal Facemask lists Projectile 50%, Melee 70% and Explosion 50% for the head slot only [11], and the Hazmat Suit lists 30% projectile, 30% melee and 30% explosion across the full body [13].
- Some clothing has negative protection: the Road Sign Jacket lists Cold -34% [12].
- The Bandage lists Bleeding -50 and Instant Health +5 [14].
- The Livestock Update lists no change to bleeding or fall damage; it did raise the Water Wheel's melee protection and change attack-helicopter armour plates [1].
- No Facepunch source opened for this document gives a fall-damage formula or explosion damage numbers *(assessed from the pages checked; see Open Questions)*.

# Scope

Covered: player-versus-player and player-versus-NPC damage on vanilla PC servers: headshot multipliers, protection values of selected clothing and armour, melee versus ranged stats, bleeding, and what is known about explosive and fall damage. Not covered: weapon-by-weapon rankings and attachments (see rust-weapons-ammo), structure damage and raid costs (see rust-raiding-costs-defence), and server convars that change damage (see rust-server-convars-reference). Modded servers and console are excluded. Facts were checked against the Livestock Update (1 October 2026).

# Definitions

- **Headshot multiplier:** the factor listed on a weapon's wiki page for head hits [3].
- **Protection:** a per-damage-type percentage listed on a clothing item page [11][12][13].
- **Hit area:** the body part struck, determined by a player collision mesh that does not change with clothing [2].
- **Bleeding:** a status value that causes damage over time [18].
- **Slot and layer:** a clothing item occupies a body slot on the Clothing or Armor layer, for example the Metal Facemask in the Head slot on both layers [11].

# Core Mechanics

**Evidence layer.** The hit-area design is from a Facepunch devblog written before the current build, so it is cited as design intent; the numbers come from current wiki pages.

**Hit areas and clothing.** Devblog 117 describes the replacement of mesh-based hitboxes. Previously the exact player model and clothing meshes were colliders, so metal hits did less damage than skin or cloth and results were effectively random in firefights. Under the new system clothing lists the body parts it protects, damage is reduced based on which body part was hit, gloves can add to overall protection, and the struck body part comes from a player collision mesh that does not change with clothing [2]. The same post says per-weapon body-part multipliers were being added, giving the example of higher headshot multipliers for sniper rifles and lower ones for shotguns, and that the direction was undecided [2]. The current wiki headshot values differ by weapon, which is consistent with that design [3][7][8].

**Ranged damage.** The wiki lists damage per ammunition type on each weapon page, with a headshot multiplier. On the Assault Rifle, 5.56 Rifle Ammo, HV and Explosive list 50 damage and Incendiary lists 56, all with x2 [3]. On the Bolt Action Rifle and L96 pages the same four 5.56 types list 80 damage (89.6 Incendiary) with x2 [4][5]. On the Thompson, Pistol Bullet and HV Pistol Ammo list 37.5 and Incendiary lists 42, with x2 [6]. On the Pump Shotgun, 12 Gauge Slug lists 80 with x2, Buckshot 15 with x1.2, Incendiary Shell 15 with x1 and Handmade Shell 9 with x1.2; the page gives no pellet count, so a per-shot total cannot be derived from the wiki [7]. Hunting Bow arrows list Wooden 50, Bone 40, Fire 40 and High Velocity 40, all with x1.5 [8].

**Weapon modifiers.** The Assault Rifle page lists attachment effects: Gas Compression Overdrive (Damage +20%), Military Silencer (Damage -25%), Oil Filter Silencer and Soda Can Silencer (Damage -30%), and Muzzle Brake (Damage -15%) [3].

**Melee.** The Salvaged Sword lists Damage Total 50, Attack Rate 0.8, Headshot Multiplier 2, Range Max 1.5 and Attack Radius 0.3 [9]. The Stone Pickaxe lists Damage Total 17, Attack Rate 1.1, Headshot Multiplier 2, Range Max 1.5 and Attack Radius 0.3 [10]. Both pages also list gather figures against Flesh (Gather Damage 10) [9][10]; the pages do not explain how these relate to combat damage, so they are not interpreted here.

**Protection by damage type.** Clothing pages list percentages per damage type. Metal Facemask: Projectile 50%, Melee 70%, Bite 8%, Cold -4%, Explosion 50%, head only [11]. Road Sign Jacket: Projectile 20%, Melee 20%, Bite 40%, Cold -34%, chest on the Armor layer [12]. Hazmat Suit: Projectile 30%, Melee 30%, Bite 50%, Radiation 50%, Cold 50%, Explosion 30%, full body [13]. The pages opened do not state how multiple items combine, so stacking is not asserted here.

**Bleeding.** The Facepunch wiki lists the Bandage as Bleeding -50, Instant Health +5, Poison -2, and describes it only as healing yourself or a target [14]. A community article states that bleeding equals 20% of damage dealt, ticking 1 damage every 6 seconds until the total is applied, and that bandages or syringes stop it immediately; it gives no build and its related articles are dated December 2024 [18]. The two sources differ on whether a Bandage ends bleeding or subtracts a fixed 50, and the discrepancy is unresolved (see Common Pitfalls).

**Explosions.** The wiki gives crafting data only for the Timed Explosive Charge and Satchel Charge, with no damage figures [16][17]. The Rocket page describes "large splash damage" and gives only rocket counts for structures [15]. The Livestock Update added client prediction when throwing a grenade, C4 or satchel, which affects feel rather than damage [1].

**Falls.** A community FAQ states that fall damage exists and that over 20 damage produces an audible crunch; the page carries no date or build [19]. The Livestock Update lists no fall-damage change [1].

# Reference Data

Checked on 2026-10-08 against the Livestock Update unless stated. The wiki pages show values without stating a build [3].

| Weapon / ammo | Damage | Headshot multiplier | Source |
|---------------|--------|---------------------|--------|
| Assault Rifle, 5.56 / HV / Explosive | 50 | x2 | [3] |
| Assault Rifle, Incendiary 5.56 | 56 | x2 | [3] |
| Bolt Action Rifle, 5.56 / HV / Explosive | 80 | x2 | [4] |
| L96, 5.56 / HV / Explosive | 80 | x2 | [5] |
| Thompson, Pistol Bullet / HV | 37.5 | x2 | [6] |
| Pump Shotgun, 12 Gauge Slug | 80 | x2 | [7] |
| Pump Shotgun, Buckshot | 15 (listed value) | x1.2 | [7] |
| Pump Shotgun, Handmade Shell | 9 (listed value) | x1.2 | [7] |
| Hunting Bow, Wooden Arrow | 50 | x1.5 | [8] |
| Hunting Bow, Bone / Fire / HV Arrow | 40 | x1.5 | [8] |
| Salvaged Sword (melee) | 50, rate 0.8 | x2 | [9] |
| Stone Pickaxe (melee) | 17, rate 1.1 | x2 | [10] |

| Clothing | Projectile | Melee | Explosion | Other | Area | Source |
|----------|-----------|-------|-----------|-------|------|--------|
| Metal Facemask | 50% | 70% | 50% | Bite 8%, Cold -4% | Head | [11] |
| Road Sign Jacket | 20% | 20% | not listed | Bite 40%, Cold -34% | Chest | [12] |
| Hazmat Suit | 30% | 30% | 30% | Bite 50%, Radiation 50%, Cold 50% | Full body | [13] |

| Healing / status item | Stated value | Source |
|-----------------------|--------------|--------|
| Bandage | Bleeding -50; Instant Health +5; Poison -2 | [14] |
| Bleeding rate (community, undated) | 20% of damage, 1 per 6 s | [18] |
| Rocket breach counts | Wood 2, Stone 4, Metal 8, Armored 15 | [15] |

# Version & Patch Notes

- Livestock Update (1 October 2026): Water Wheel melee protection raised "4-5x"; attack-helicopter armour plates now fall off by the side shot; client prediction for throwing grenade, C4 and satchel; no listed change to bleeding or fall damage [1].
- Devblog 117 introduced body-part-based clothing protection and weapon-specific body-part multipliers as work in progress; its date was not shown in the extract used here [2].
- Volatile: every number in Reference Data, since Rust is rebalanced in monthly updates [1].

# Common Pitfalls

- Treating the Bandage as a full cure. The wiki gives Bleeding -50 [14] while a community article says bandages stop bleeding immediately [18]; the conflict is unresolved.
- Assuming a wiki damage figure for shotgun buckshot is a per-shot total. The wiki gives no pellet count [7].
- Assuming clothing protection ignores damage type. An item can protect against projectiles and expose you to cold, for example the Road Sign Jacket's Cold -34% [12].
- Assuming the Bolt Action and L96 values differ by ammunition type. The wiki lists the same four 5.56 types at 80 on both pages [4][5].

# Interactions & Related Systems

Healing, radiation and the wounded state are covered in rust-game-mechanics-foundation. Weapon and ammunition comparison: rust-weapons-ammo. Explosive costs against structures: rust-raiding-costs-defence. Damage-related server settings: rust-server-convars-reference. Plugins hooking damage events: rust-plugin-development-hooks. Update history: rust-update-timeline-2026. Crafting of the armour items: rust-items-crafting-foundation [11][12][13].

# Assessed Guidance

## Guidance 1 — Match armour to the damage type you expect, not to a single protection number

- **Guidance:** Compare protection per damage type and body area before choosing gear, and weigh cold penalties for items such as the Road Sign Jacket.
- **Evidence basis:** Protection is listed per damage type and slot [11][12][13], and some items carry negative values [12].
- **Confidence:** Medium. The item values are primary, but how items stack is unsourced.
- **So what:** A head item with high melee and projectile protection covers only the head [11]; a chest item with low values and a cold penalty can be a poor trade [12].

## Guidance 2 — Treat wiki damage figures as base values, not outcomes

- **Guidance:** Use listed damage and headshot multipliers for relative comparison only.
- **Evidence basis:** Wiki pages list base damage and a multiplier [3][7], protection reduces damage by body area [2][11], and attachments change it [3].
- **Confidence:** Medium. The inputs are primary; the combined result is inference.
- **So what:** Do not expect a listed 50 damage to land as 50 against armoured targets.

## Guidance 3 — Carry more than one bleeding fix until the Bandage behaviour is settled

- **Guidance:** Do not rely on a single Bandage after heavy damage.
- **Evidence basis:** The wiki value is -50 [14], and the community article is the only source for the bleed formula [18].
- **Confidence:** Low. The two sources conflict and the formula is single-source.
- **So what:** Check the bleeding value in game after bandaging.

# Open Questions

- Hit-zone multipliers other than headshot (chest, stomach, limbs): none found on the wiki pages opened. Resolve from in-game data.
- Fall damage formula: no Facepunch source found; only an undated community FAQ [19].
- Explosion damage to players for C4, satchel and rockets: the wiki pages opened give no damage numbers [15][16][17].
- How multiple clothing items combine their protection: not stated on the pages opened.
- Whether a Bandage removes all bleeding or subtracts 50 [14][18].
- Chest and leg armour beyond the three items listed, and attack-helicopter plate values.
- The publication date of Devblog 117 [2] and the build of the bleeding article [18].

# References

Numbered contiguously from [1].

**Primary Sources**

- [1] **Facepunch** — *Livestock Update*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [2] **Facepunch** — *Devblog 117*. https://rust.facepunch.com/news/devblog-117. Accessed 2026-10-08.
- [3] **Facepunch Rust Wiki** — *Assault Rifle*. https://wiki.facepunch.com/rust/item/rifle.ak. Accessed 2026-10-08.
- [4] **Facepunch Rust Wiki** — *Bolt Action Rifle*. https://wiki.facepunch.com/rust/item/rifle.bolt. Accessed 2026-10-08.
- [5] **Facepunch Rust Wiki** — *L96 Rifle*. https://wiki.facepunch.com/rust/item/rifle.l96. Accessed 2026-10-08.
- [6] **Facepunch Rust Wiki** — *Thompson*. https://wiki.facepunch.com/rust/item/smg.thompson. Accessed 2026-10-08.
- [7] **Facepunch Rust Wiki** — *Pump Shotgun*. https://wiki.facepunch.com/rust/item/shotgun.pump. Accessed 2026-10-08.
- [8] **Facepunch Rust Wiki** — *Hunting Bow*. https://wiki.facepunch.com/rust/item/bow.hunting. Accessed 2026-10-08.
- [9] **Facepunch Rust Wiki** — *Salvaged Sword*. https://wiki.facepunch.com/rust/item/salvaged.sword. Accessed 2026-10-08.
- [10] **Facepunch Rust Wiki** — *Stone Pickaxe*. https://wiki.facepunch.com/rust/item/stone.pickaxe. Accessed 2026-10-08.
- [11] **Facepunch Rust Wiki** — *Metal Facemask*. https://wiki.facepunch.com/rust/item/metal.facemask. Accessed 2026-10-08.
- [12] **Facepunch Rust Wiki** — *Road Sign Jacket*. https://wiki.facepunch.com/rust/item/roadsign.jacket. Accessed 2026-10-08.
- [13] **Facepunch Rust Wiki** — *Hazmat Suit*. https://wiki.facepunch.com/rust/item/hazmatsuit. Accessed 2026-10-08.
- [14] **Facepunch Rust Wiki** — *Bandage*. https://wiki.facepunch.com/rust/item/bandage. Accessed 2026-10-08.
- [15] **Facepunch Rust Wiki** — *Rocket*. https://wiki.facepunch.com/rust/item/ammo.rocket.basic. Accessed 2026-10-08.
- [16] **Facepunch Rust Wiki** — *Satchel Charge*. https://wiki.facepunch.com/rust/item/explosive.satchel. Accessed 2026-10-08.
- [17] **Facepunch Rust Wiki** — *Timed Explosive Charge*. https://wiki.facepunch.com/rust/item/explosive.timed. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- [18] **GamerBlurb** — *How Bleeding Works in Rust* (undated, related articles Dec 2024). https://gamerblurb.com/articles/how-bleeding-works-in-rust. Accessed 2026-10-08.
- [19] **Rustafied** — *Rust: Frequently Asked Questions from Legacy Players* (undated). https://www.rustafied.com/rust-experimental-frequently-asked-questions. Accessed 2026-10-08.

**Further Reading**

None.

# Further Reading

The Facepunch Rust Wiki pages for other clothing and armour items, and rust-weapons-ammo for weapon comparison.

# Related Documents

- rust-game-mechanics-foundation
- rust-items-crafting-foundation
- rust-building-raiding-foundation
- rust-server-administration-foundation
- rust-modding-plugins-foundation
- rust-updates-meta-foundation
- rust-weapons-ammo
- rust-raiding-costs-defence
- rust-server-convars-reference
- rust-plugin-development-hooks
- rust-update-timeline-2026

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
