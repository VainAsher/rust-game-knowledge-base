---
id: rust-monuments-loot
title: "Rust Monuments and Loot"
version: 1.0.0
status: frozen
confidence: Medium
category: Game Mechanics
topic: "Monuments and loot"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-building-raiding-foundation, rust-server-administration-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation, rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence, rust-server-convars-reference, rust-plugin-development-hooks, rust-update-timeline-2026, rust-farming-food, rust-vehicles, rust-wipes-map-generation, rust-moderation-anti-cheat, rust-carbon-vs-oxide]
tags: [monuments, loot, keycards, fuses, heavy-fuse, power-plant, safe-zone, outpost, puzzles, oil-rig]
game_build_checked: "Livestock Update (1 October 2026)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-monuments-loot |
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

This deep-dive goes beyond the monument overview in rust-game-mechanics-foundation. It covers how the Facepunch wiki groups monuments (safe zone, small, large), what the three keycards and the Electric Fuse are, how the 2026 power-grid work (Heavy Fuses, the Power Plant, Monument Blockers, Powergrid loot rooms) changed monument progression, and what individual monuments are known for.

The official Facepunch material is strong on the 2026 changes and on item data, but it does not publish a per-monument tier table or monument loot tables. The tier-by-card ladder comes only from a community guide that gives no build number, and the only official tier list is from 2018. Overall confidence is Medium: item and devblog facts are primary, monument tiering is community-derived.

# Key Facts

- The Facepunch wiki sorts monuments into safe zone, small and large groups; the safe-zone group is Bandit Camp, Outpost, Fishing Village, Large Fishing Village, Large Barn and Ranch [1].
- Green, Blue and Red Keycards cannot be crafted, repaired, recycled or researched; they despawn after 20 minutes, 40 minutes and 1 hour respectively [2][3][4].
- Green Keycards drop from scientists at a stated 36.3% chance (1-2 cards) for most scientist variants, per the wiki loot table [2].
- The Electric Fuse is recyclable, stacks to 10 and despawns after 40 minutes; the wiki lists its loot sources by percentage [5].
- From August 2026 the Power Plant takes Heavy Fuses to power an island grid; the Livestock Update added Powergrid loot rooms at monuments that unlock with enough Heavy Fuses [6][7].
- Monument Blockers (September 2026) slow early access at monuments with red keycard puzzle rooms; unbroken blockers start to decay after 24 hours [8].
- A per-monument tier table (card, radiation, loot) exists only in a community guide with no build number *(assessed as community-derived)* [13].

# Scope

Covered: monument categories, safe zones, keycards, fuses and Heavy Fuses, the 2026 power-grid system, puzzle mechanics from the official 2018 devblog (flagged as historical), and what monuments are known for, on vanilla PC servers, checked against the Livestock Update of 1 October 2026. Not covered: per-monument loot tables (no primary source publishes them, see Open Questions), raiding mechanics (rust-raiding-costs-defence), vehicles (rust-vehicles), farming and food (rust-farming-food), map generation (rust-wipes-map-generation), modded servers and consoles.

# Definitions

- **Monument:** a larger, build-protected area with buildings and entities that players visit for loot, recycling, trading or combat [1].
- **Safe zone:** a monument where hostile actions make you a target for NPCs and turrets [1].
- **Keycard:** Green, Blue or Red access item used at locked puzzle rooms [2][3][4].
- **Heavy Fuse:** a fuse loaded into special fuse boxes at the Power Plant to power the island grid [6].
- **Powergrid loot room:** a locked room at a monument that opens once enough Heavy Fuses power the grid [7].
- **Monument Blocker:** an obstacle added to monuments with red keycard puzzle rooms [8].

# Core Mechanics

**Monument groups.** The wiki's Map page says monuments are larger build-protected areas that players visit for loot, recycling, trading or combat, and splits them into three groups [1]. Safe zone: Bandit Camp, Outpost, Fishing Village, Large Fishing Village, Large Barn, Ranch. Small: Abandoned Supermarket, Abandoned Cabins, Lighthouse, Mining Outpost, Oxums Gas Station, Quarry. Large: Airfield, Abandoned Military Base, Arctic Research Base, Giant Excavator Pit, Harbor, Junkyard, Launch Site, Large Oil Rig, Oil Rig, Underwater Lab, Military Tunnels, Power Plant, Satellite Dish, Sewer Branch, The Dome, Train Yard, Water Treatment Plant [1]. The same page says the Harbor is where the Cargo Ship stops to drop locked crates, and that the three ocean monuments are good component sources [1]. The page describes only a few monuments in detail [1].

**Safe zones.** The wiki states that in safe-zone monuments you can trade with NPCs, hostile actions make you a target for NPCs and turrets, and players can only be hurt by other players outside the zones [1]. The Outpost has a safe zone spanning the whole monument, sentry turrets inside and around it, two entrances plus underground tunnels, vending machines, a drone shop, and stations including a Workbench Level 1, Research Table, Oil Refinery, Recycler, Barbecue and Repair Bench [10]. The Power Trip devblog stopped ore nodes and woodpiles spawning in safe zones and left the yellow (safe zone) recyclers unchanged [6]. A community guide adds that turrets enforce the rule, so drawing a weapon is unwise [13].

**Keycards.** Each of the three cards stacks to 1 and cannot be crafted, repaired, recycled or researched [2][3][4]. The wiki describes Green as low-level clearance for basic areas and Blue as medium-level clearance [2][3]; Red is described as high clearance for top-level areas [4]. Wiki Green Keycard loot data lists scientists (1-2 cards, 36.3%), Road Scientist (1 card, 23.6%), and Peacekeeper Scientist and Bandit Guard (1 card, 16.7%) [2]. The Blue and Red pages give no loot sources [3][4]. The community guide describes a ladder in which each card opens rooms whose reward includes the next card [13].

**Fuses.** The Electric Fuse is described as unreliable and allows electrical passthrough for a limited time [5]. It drops from Tech Parts 1 (1-2 items, 26.5%), several crate types (14.3% each) and various scientists (4.7% each), among other sources [5]. It recycles into 24 scrap in a Recycler and 16 scrap in a Safe Zone Recycler, both stated at 100% chance [5]. The Safe Zone Recycler returns 40% of recyclable material value at 8 seconds per item [11]. The community guide says many puzzles need power: find a fuse, insert it and flip switches in the right order [13].

**Power Plant and Heavy Fuses (Power Trip, August 2026).** Heavy Fuses are found as loot and inserted into special fuse boxes at the Power Plant; running it powers the island-wide grid [6]. Power affects recyclers: green recyclers outside safe zones run at 50% efficiency rising to 60% with sufficient power, and cycle time drops from 5 to 4.5 seconds at maximum power; a new red recycler at the Power Plant gives 75% and works only at maximum power [6]. The devblog also added another loot room reachable only with sufficient power [6].

**Player-maintained monuments (August 2026).** Per the same devblog: the Abandoned Supermarket freezer gives steady chilled food while powered; Water Treatment Plant pipes stay empty until the plant is maintained; Oxum's Gas Station garage door and car lift work when powered; Airfield Control Tower terminals raise air drop frequency or enable a Chinook crate drop and drain over time [6]. At Launch Site a Satellite Control Computer lets players crash a satellite, which spills loot crates [6]. On the two oil rigs, a switch (available once the Power Plant runs) pumps crude to the Dome for 20 minutes on the Large rig and at half that rate on the Small rig; both on gives 1.5x crude [6].

**Monument Blockers and the marketplace (September 2026).** Blockers appear on monuments with red keycard puzzle rooms; heavy ones need significant damage and do not respawn, a handful can be destroyed by melee, and any not destroyed within 24 hours start to decay [8]. The drone marketplace needs the Power Plant: its battery rises slowly with 4 or more active fuses, accepts purchases at 50%, and does not drain while at least one fuse is inserted [8].

**Powergrid loot rooms (October 2026).** The Livestock devblog lists monuments with new rooms: Airfield, Ferry Terminal, Harbour 1, Harbour 2, Junkyard, Launch Site, Military Tunnels, Nuclear Missile Silo, Radtown, Sewer Branch, Trainyard and Water Treatment Plant [7]. The post lists Ferry Terminal twice, so the unique count is 12 although 13 entries appear [7]. Rooms are locked until enough Heavy Fuses power the grid; harder monuments need more; no per-monument fuse counts are given [7].

**Heavy Fuse decay.** Power Plant heavy fuse decay scales with server population: 4x longer at 10 or fewer players, normal at 100 or more; the convars are `powergrid.fusedecaylowpop`, `fusedecayhighpop` and `fusedecaylowpopscale` [7]. The post also moved the small heavy fuse box at the Power Plant so it is reachable from outside through a broken window [7].

**Puzzle design (2018, historical).** The Puzzle Update introduced Entity I/O circuits (generator, switch, timed switch, splitter, AND, OR, card reader, wheel switch, push button) and linked monuments into a path of rising difficulty [12]. It stated cards were found in puzzles, usually the final loot room, with 10 uses each, and electric fuses lasted 180 seconds [12]. These 2018 values are not confirmed for the current build.

# Reference Data

**Item data, checked against the Facepunch wiki on 2026-10-08 (Livestock Update era):**

| Item | Stack | Despawn | Craft/repair/recycle/research | Source |
|------|-------|---------|-------------------------------|--------|
| Green Keycard | 1 | 20 min | No to all | [2] |
| Blue Keycard | 1 | 40 min | No to all | [3] |
| Red Keycard | 1 | 1 hour | No to all | [4] |
| Electric Fuse | 10 | 40 min | Recyclable only | [5] |

**Green Keycard drop sources (wiki, 2026-10-08):**

| Source | Cards | Chance | Source ref |
|--------|-------|--------|-----------|
| Scientist variants, RHIB Scientist, Patrol Boat Scientist | 1-2 | 36.3% | [2] |
| Road Scientist | 1 | 23.6% | [2] |
| Peacekeeper Scientist, Bandit Guard | 1 | 16.7% | [2] |

**Electric Fuse sources (wiki, 2026-10-08):**

| Source | Chance | Source ref |
|--------|--------|-----------|
| Tech Parts 1 (1-2 items) | 26.5% | [5] |
| Underwater Advanced, Brown, Wagon Brown, Underwater Labs Brown crates | 14.3% each | [5] |
| Underwater Lab Dweller, Tunnel Dweller (1-2 items) | 7.4% each | [5] |
| Various scientists (Bradley, Cargo Ship, Patrol, Oil Rig, Arena, others) | 4.7% each | [5] |
| Blue and Yellow Barrels | 1.4% each | [5] |

**Power grid values (devblogs):**

| Value | Figure | Build | Source |
|-------|--------|-------|--------|
| Green recycler efficiency | 50%, 60% at sufficient power | Power Trip, Aug 2026 | [6] |
| Red recycler (Power Plant) | 75%, max power only | Power Trip, Aug 2026 | [6] |
| Safe Zone Recycler | 40% return, 8 s per item | wiki, Oct 2026 | [11] |
| Large rig Dome pumping | 20 minutes; Small rig half rate; both 1.5x | Power Trip, Aug 2026 | [6] |
| Oil Rig crude start delay | 15 minutes | Livestock, Oct 2026 | [7] |
| Monument Blocker decay | after 24 hours undestroyed | Breach and Clear, Sep 2026 | [8] |
| Marketplace power | rises with 4+ fuses, buys at 50% | Breach and Clear, Sep 2026 | [8] |
| Heavy Fuse low-pop decay | 4x longer at 10 or fewer players | Livestock, Oct 2026 | [7] |

**Community tier table (no build stated, published 4 June 2026) [13]:**

| Monument | Card | Radiation |
|----------|------|-----------|
| Supermarket, Gas Station | none | none to low |
| Mining Outpost, Junkyard | none | low |
| Satellite Dish, Dome, Sewer Branch | Green | low |
| Water Treatment, Train Yard, Airfield | Blue | medium |
| Power Plant | Blue | medium |
| Launch Site | Red | high |
| Military Tunnels | Red | high |
| Small and Large Oil Rig | Blue | low |
| Cargo Ship | roaming event, no tier | not stated |

Of these, only the Launch Site's three elite crates is a stated monument number in the guide [13]. The 2018 devblog's official tiers differ (for example, Junkyard as basic, Water Treatment as medium) and are historical [12].

# Version & Patch Notes

- **June 2018, The Puzzle Update:** introduced monument puzzles, cards and fuses with the I/O system [12].
- **2 July 2026, Common Ground:** added the Apartment Complex monument with rentable rooms and shops; its master key opens any occupied room for 5 minutes [9].
- **6 August 2026, Power Trip:** Power Plant, Heavy Fuses, red recycler, player-maintained monuments, Satellite Crash, Dome pumping [6].
- **3 September 2026, Breach and Clear:** Monument Blockers, drone marketplace power link; fixed boosting on a siege tower to skip the Launch Site red card puzzle; Gas Station cave loot now respawns after a restart [8].
- **1 October 2026, Livestock:** Powergrid loot rooms, population-scaled Heavy Fuse decay, and a fix so Oil Rig radiation no longer starts before the locked crate is looted [7].

Volatile: everything under power-grid values, fuse counts and card tiers, which have changed in each of the last three updates [6][7][8].

# Common Pitfalls

- Treating the community tier table as official; it carries no build and mixes sources [13].
- Using 2018 numbers (10 card uses, 180-second fuses) for the current game; the 2018 devblog is the only primary source for them [12].
- Assuming the Livestock rooms cover 13 monuments; the list repeats Ferry Terminal [7].
- Expecting the wiki Blue and Red Keycard pages to say where the cards come from; they do not [3][4].
- Assuming a safe zone protects you outside its boundary; the wiki says you can only be hurt by players outside these zones [1].

# Interactions & Related Systems

Power and fuses feed the recycler and drone marketplace (see rust-items-crafting-foundation and rust-raiding-costs-defence for scrap and raid costs) [6][8]. Monument Blockers tie into raiding-style damage (rust-building-raiding-foundation) [8]. Fuse decay convars belong with rust-server-convars-reference [7]. Cargo Ship and Harbor interplay is covered by rust-vehicles and the naval material in rust-update-timeline-2026 [1]. Wipe timing and map seeds that place monuments: rust-wipes-map-generation. Plugins altering loot use hooks such as those in rust-plugin-development-hooks. Anti-cheat concerns such as parent history on the Cargo Ship are in rust-moderation-anti-cheat [7]. Farming and the Supermarket freezer: rust-farming-food [6].

# Assessed Guidance

## Guidance 1 — Check the current update before relying on any tier list

- **Guidance:** Treat any monument tier list, including this document's community table, as provisional and confirm in game or in the latest devblog.
- **Evidence basis:** The only official tiers are from 2018 [12], the current tier table has no build [13], and three consecutive updates changed monument systems [6][7][8].
- **Confidence:** Medium. The change history is primary, but the advice is a judgement.
- **So what:** Do not plan a run around a card requirement you have not seen this wipe.

## Guidance 2 — Scientists are a documented Green Keycard source, so low-tier cards need not wait on puzzles

- **Guidance:** If you need a Green Keycard, fighting scientists is a documented route as well as puzzle rooms.
- **Evidence basis:** Wiki drop rates of 36.3% for most scientist variants [2]; the guide agrees green cards appear at starter monuments [13].
- **Confidence:** Medium. Rates are primary but depend on the live loot table, and the wiki has no Blue or Red source data.
- **So what:** Expect fights, not just puzzles, on the way to the first card.

## Guidance 3 — On low-population servers, expect Heavy Fuses to last longer

- **Guidance:** Admins running small servers can lean on the population scaling and adjust the three convars if power phases feel wrong.
- **Evidence basis:** The Livestock devblog states 4x longer decay at 10 or fewer players and names the convars, with no defaults listed [7].
- **Confidence:** High. This is a direct Facepunch statement, though values may be retuned.
- **So what:** Read the default values from your own server before changing anything.

## Guidance 4 — Destroy or bypass Monument Blockers early in the wipe only if you can afford the noise

- **Guidance:** Blockers decay after 24 hours, so a patient group can wait rather than spend explosives.
- **Evidence basis:** Heavy blockers need significant damage and do not respawn, and undestroyed blockers decay after 24 hours [8].
- **Confidence:** Low. The trade-off is inference; Facepunch gives no HP or cost figures [8].
- **So what:** Compare the cost of damaging a blocker with the cost of waiting, once you have measured the HP yourself.

# Open Questions

- Per-monument loot tables and crate spawn rates: no primary source opened gives them; the wiki item pages give drop chances per item only [2][5].
- The current official card tier for each monument: not in any Facepunch page opened.
- Heavy Fuse counts needed per Powergrid loot room, Heavy Fuse duration and the convar default values: the devblogs give none [6][7].
- The Blue and Red Keycard loot sources: the wiki pages are empty [3][4].
- Individual wiki pages for Launch Site, Oil Rig, Military Tunnels and Bandit Camp returned 404 at the URLs tried, so their details rest on the community guide [13].
- Whether the Ferry Terminal repeat in the Livestock list hides a different monument.

# References

**Primary Sources**

- [1] **Facepunch Wiki** — *The Map (monuments)*. https://wiki.facepunch.com/rust/map. Accessed 2026-10-08.
- [2] **Facepunch Wiki** — *Green Keycard*. https://wiki.facepunch.com/rust/item/keycard_green. Accessed 2026-10-08.
- [3] **Facepunch Wiki** — *Blue Keycard*. https://wiki.facepunch.com/rust/item/keycard_blue. Accessed 2026-10-08.
- [4] **Facepunch Wiki** — *Red Keycard*. https://wiki.facepunch.com/rust/item/keycard_red. Accessed 2026-10-08.
- [5] **Facepunch Wiki** — *Electric Fuse*. https://wiki.facepunch.com/rust/item/fuse. Accessed 2026-10-08.
- [6] **Facepunch** — *Power Trip (6 Aug 2026)*. https://rust.facepunch.com/news/power-trip. Accessed 2026-10-08.
- [7] **Facepunch** — *Livestock Update (1 Oct 2026)*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [8] **Facepunch** — *Breach and Clear (3 Sep 2026)*. https://rust.facepunch.com/news/breach-and-clear. Accessed 2026-10-08.
- [10] **Facepunch Wiki** — *Outpost*. https://wiki.facepunch.com/rust/Outpost. Accessed 2026-10-08.
- [11] **Facepunch Wiki** — *Safe Zone Recycler*. https://wiki.facepunch.com/rust/Safe_Zone_Recycler. Accessed 2026-10-08.
- [12] **Facepunch** — *The Puzzle Update (8 June 2018)*. https://rust.facepunch.com/news/the-puzzle-update. Accessed 2026-10-08.
- [9] **Facepunch** — *Common Ground (2 Jul 2026)*. https://rust.facepunch.com/news/common-ground. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- [13] **XGamingServer** — *Rust Monuments Guide: Loot, Puzzles, Keycards & Fuses* (4 June 2026). https://xgamingserver.com/blog/rust-monuments-guide-loot-puzzles-keycards/. Accessed 2026-10-08.

**Further Reading**

See Further Reading below.

# Further Reading

The Facepunch wiki home page lists item pages for the Blue, Green and Red Keycards, the Electric Fuse and the Safe Zone Recycler: https://wiki.facepunch.com/rust/.

# Related Documents

rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-building-raiding-foundation, rust-server-administration-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation, rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence, rust-server-convars-reference, rust-plugin-development-hooks, rust-update-timeline-2026, rust-farming-food, rust-vehicles, rust-wipes-map-generation, rust-moderation-anti-cheat, rust-carbon-vs-oxide.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
