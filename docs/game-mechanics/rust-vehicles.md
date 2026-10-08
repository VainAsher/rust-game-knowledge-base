---
id: rust-vehicles
title: "Rust Vehicles"
version: 1.0.0
status: frozen
confidence: Medium
category: Game Mechanics
topic: "Vehicles and transport"
market: "Global"
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-building-raiding-foundation, rust-server-administration-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation, rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence, rust-server-convars-reference, rust-plugin-development-hooks, rust-update-timeline-2026, rust-monuments-loot, rust-farming-food, rust-wipes-map-generation, rust-moderation-anti-cheat, rust-carbon-vs-oxide]
tags: [vehicles, boats, naval, helicopter, horse, modular-car, fuel, decay, deep-sea]
game_build_checked: "Livestock Update (1 October 2026)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-vehicles |
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

This document goes deeper than the mechanics foundation on land, water and air transport in Rust: how each vehicle class is obtained, what fuels it, how it decays, and how 2026 updates changed it, especially the Naval Update's player-built boats and Deep Sea [2][3]. Boats are the best-documented area because Facepunch published detailed 2026 changelists for them [2][3][5].

Confidence is Medium. The 2026 boat, fuel and decay-change claims rest on Facepunch devblogs, but Facepunch's wiki pages for the older vehicles (minicopter, scrap helicopter) are placeholders [18][19]. Their base health, fuel burn and decay values therefore come from dated community sources (2019 and 2020) and are flagged as possibly stale [21][22].

# Key Facts

- Player-built boats arrived with the Naval Update: place a Boat Building Station in water, then use a Boat Building Plan and boat blocks [2].
- Boat engines run on low grade fuel and burn it fast; sails, anchors, cannons, planks and ramps are the other parts [2].
- Shipshape (5 March 2026) raised the boat decay delay from 12 to 24 hours and cut decay duration from 18 to 12 hours; a boat counts as used only when steering input is received [3].
- The Boat Building Station crafts for 200 Wood and 1 Tarp at Workbench Level 1, and the Boat Building Plan for 20 Wood [11][12].
- At Bandit Camp the Air Wolf air-vehicle vendor will not sell until the helipad is repaired each wipe (Livestock, 1 Oct 2026) [1].
- The Deep Sea is reached by sailing toward the map edge in a strong boat; RHIBs can no longer enter it since 5 March 2026 [2][3].
- Horses need no fuel (they eat food) per a June 2026 community guide [20].
- Modular-car decay figures (about 8 hours outside, 36 inside) are from a 2020 community post and not re-verified on this build [21].

# Scope

Covered: land (modular car, horse, snowmobile and motorbike mentions), water (rowboat, RHIB, kayak, submarine, player-built boats, PT Boat), air (minicopter, scrap transport helicopter, hot air balloon, attack helicopter), fuel and decay, acquisition. Vanilla PC Rust only, checked against the Livestock Update (1 October 2026). Not covered: combat stats (see rust-combat-damage-model), monument loot (see rust-monuments-loot), plugin-side vehicle hooks (see rust-plugin-development-hooks), trains beyond passing mentions.

# Definitions

- **Boat Building Station** — deployable placed in water to build or edit a player boat [2][11].
- **Deep Sea** — offshore, time-limited zone reached by sailing toward the map edge [2].
- **DPV** — diver propulsion vehicle, listed on the wiki as item `skidoo` [5].
- **Low grade fuel** — the common fuel item for boats, cars and helicopters [10][20].
- **Air Wolf** — air-vehicle vendor NPC at Bandit Camp [1].
- **HAB** — hot air balloon; armoured variants exist [9].

# Core Mechanics

**Evidence layer.**

## Water

- The first player-controlled vehicle was the powered rowboat (Vehicle Update, 5 April 2018): one driver plus three passengers, low grade fuel, a small bow storage box, and decay if left outside [10].
- Player-built boats (Naval Update, February 2026): build with a Boat Building Station placed in water, the Boat Building Plan and boat-specific blocks. Components are steering wheel (helm with a built-in lock and settable code), sails, engines, anchors, cannons, planks and ramps [2].
- Engines run on low grade fuel and burn it fast; engine and sail placement affects handling, and both can be reversed from the radial menu. Without an anchor a boat may drift to shore [2].
- Standard deployables can be placed on boats if they work on the Tugboat; Deploy and Edit mode places a Boat Building Station around an existing boat and is unavailable in the Deep Sea [2]. Tugboat spawns were disabled [2].
- Since 5 March 2026 electricity, industrial and water IO items work on boats; auto turrets, SAM sites, windmills, CCTV, seismic sensors, hanging lights and door controllers are blocked [3]. Repeated cannon hits can slow a player boat to 30% of maximum speed [3].
- Boats with flat bows take much more drag, and boat-shaped hulls are faster than box-shaped ones (May 2026) [5].
- The Deep Sea PT Boat is slower than the RHIB and uses more fuel but is stronger, with two turrets (dual .50 cal and single .50 cal) reloaded with 5.56 rifle ammo. Scientist-crewed RHIBs and PT Boats can be cleared and stolen [2].
- The kayak seats two and requires a Paddle [13]. A Small Boat Engine crafts from 50 Low Grade Fuel, 5 High Quality Metal and 2 Gears at Workbench Level 2 [14].

## Land

- Modular cars are assembled from a chassis plus modules; engine parts come in five types and three quality tiers (Low, Medium, High) [17]. Modules include engine, cockpit, passenger, storage, taxi, flatbed, camper and fuel tank variants [17].
- The Engine Vehicle Module crafts for 100 Metal Fragments and 3 High Quality Metal at Workbench Level 2 [15].
- Per the 2020 launch post: three chassis sizes, five engine parts required, higher part tiers make the car faster and more fuel efficient, and modules carry separate health [21]. A June 2026 guide gives module slots of small 2, medium 3, large 4 [20].
- Horses are claimed in a stable with a saddle (hold E and select Claim); the single saddle is not craftable [16]. Per a community guide horses are tamed in the wild or bought from a stable and need food, not fuel [20].

## Air

- Livestock (1 Oct 2026): the Bandit Camp Air Wolf helipad starts each wipe in disrepair and the vendor refuses sales until players repair it with hammer hits; it then stays repaired for the wipe [1].
- Minicopter costs 750 scrap and the scrap transport helicopter 1,250 scrap from the Air Wolf, or can be crafted from a blueprint, per a June 2026 community guide [20].
- The hot air balloon has an altimeter (April 2026) and armoured variants with staged armour loss (September 2026) [4][9].

## Fuel and decay

- Boat decay (Shipshape): delay 24 hours, then 12 hours of decay; a boat counts as used only with steering input [3]. The decay timer saves across restarts since September 2026 [9].
- Livestock added a Biofuel Generator that turns organic matter into low grade fuel, stirred by hand about every 30 minutes [1]. Dome crude pumps are covered under Version & Patch Notes [8][9].

# Reference Data

**Evidence layer.** Values are as checked on 2026-10-08 unless dated otherwise.

| Item | Value | Source / build |
|------|-------|----------------|
| Boat Building Station craft | 200 Wood, 1 Tarp, Workbench 1, 30 s | [11] wiki, Oct 2026 |
| Boat Building Plan craft | 20 Wood, Workbench 1, 15 s | [12] wiki, Oct 2026 |
| Boat Building Plan research | 120 Scrap on wiki; reduced per Breach and Clear | [12][9] |
| Kayak craft | 200 Wood, 75 Metal Fragments, 50 Cloth, Workbench 1 | [13] wiki, Oct 2026 |
| Small Boat Engine craft | 50 Low Grade Fuel, 5 HQM, 2 Gears, Workbench 2 | [14] wiki, Oct 2026 |
| Engine Vehicle Module craft | 100 Metal Fragments, 3 HQM, Workbench 2 | [15] wiki, Oct 2026 |
| Player boat decay | 24 h delay, 12 h duration | [3] Mar 2026 |
| Cannon slowdown floor | 30% of max speed | [3] Mar 2026 |
| Attack heli cockpit armour falls | left 80% (680hp), right 70% (595hp), front 60% (510hp) | [9] Sep 2026 |
| Armoured HAB armour falls | left 90% (2250hp), right 80% (2000hp), back 70% (1750hp), front 60% (1500hp); equip takes 3 s | [9] Sep 2026 |
| Dome fuel pump storage | 1,000 crude (was 10,000) | [9] Sep 2026 |
| Minicopter and scrap heli price (Air Wolf) | 750 and 1,250 scrap | [20] community, Jun 2026 |
| Minicopter fuel burn | about 30 low grade per minute | [20] community, Jun 2026 |
| Scrap heli (2019 launch) | about 28 low grade per minute, 500 tank, 1000 HP, 3 h outside decay | [22] community, 2019, likely stale |
| Modular car decay (2020) | about 8 h outside, 36 h inside | [21] community, 2020, likely stale |
| Vehicle Lift (2020) | 1000 Metal Fragments, 10 HQM, 3 Gears; 175 scrap to buy | [21] community, 2020, likely stale |
| Admin convars | `vehicle.padrepairsrequired`, `vehicle.setrepairablepads` (0 or 1) | [1] Oct 2026 |

# Version & Patch Notes

**Evidence layer.**

- 5 Apr 2018, Vehicle Update: powered rowboat, first player vehicle; Chinook event [10].
- 2019: scrap transport helicopter (community post, details "may change") [22]. 2 Jul 2020: modular vehicles [21].
- Feb 2026, Naval Update: player-built boats, PT Boat, refreshed RHIB, Deep Sea AI patrols, Floating City docks, Tugboat spawns off [2].
- 5 Mar 2026, Shipshape: boat decay and usage changes, deployables, RHIBs barred from Deep Sea, a Boat Building Station on each island, hazmat 5% to 30% and fullmetal 25% to 50% protection against naval scientists [3].
- 2 Apr 2026, Spring Clean: balloon altimeter, engine UI shows missing car parts, boat fixes [4].
- 7 May 2026: flat-bow drag, Floating City boat vendor sells modular boat parts and a cheaper DPV and no longer sells kayaks or torpedoes, Deep Sea loot and scientist-boat guns reduced [5].
- 4 Jun 2026: `antihack.parenthistory` improves hit validation on balloons and boats; wire isolation fix on boats [6].
- 2 Jul 2026: garage door no longer destroys vehicles; fuel tanks connectable; DPV fuel bar fix [7].
- 6 Aug 2026: vehicle emoji; Oxum's Gas Station car lift; Fishing Village sells Kayaks and Paddles directly; Chinook resupply crate at Airfield; Dome crude pumping and Tanker module drain; armoured balloon health persists across restart [8].
- 3 Sep 2026: modular car handling rework with CTRL handbrake; vehicle pooling; boat fuel interaction driver-only; decay timer saved across restarts; heli and balloon armour staged loss [9].
- 1 Oct 2026, Livestock: Air Wolf helipad repair requirement, boat steering wheel lock code change, Biofuel Generator, horses drop less dung, vehicle physics parallel ticking [1].
- Volatile: all boat and Deep Sea values changed within weeks of release; treat as perishable.

# Common Pitfalls

- Facepunch's wiki pages for the minicopter and scrap helicopter repair items are placeholders ("MC repair dummy"), so do not treat them as stat sources [18][19].
- The Shipshape page gives conflicting Deep Sea network range figures (620 m in the text, 640 m in the changelist) [3].
- Old decay times (8 h outside, 3 h for helicopters) come from 2019 and 2020 posts and may no longer apply [21][22].
- Fishing Village now sells Kayaks and Paddles rather than blueprints, while the Floating City vendor no longer sells kayaks, so older guides mislead [5][8].
- RHIBs cannot enter the Deep Sea after March 2026, whereas the original Naval devblog lists the RHIB among Deep Sea boats [2][3].

# Interactions & Related Systems

- Deep Sea combat and naval scientists link to rust-combat-damage-model and rust-weapons-ammo (5.56 ammo for PT Boat turrets) [2].
- Helicopters, Chinook crates and the Air Wolf connect to rust-monuments-loot [1][8].
- Fuel supply (Biofuel Generator, Dome crude) links to rust-farming-food for organic inputs and rust-wipes-map-generation for per-wipe resets [1][8].
- Raiders can use boats and balloons against bases: see rust-raiding-costs-defence; hit validation: rust-moderation-anti-cheat [6].
- Admin convars and plugin hooks: rust-server-convars-reference, rust-plugin-development-hooks, rust-carbon-vs-oxide [1].
- Update chronology: rust-update-timeline-2026.

# Assessed Guidance

**Judgement layer.**

## Guidance 1 — Move or dock boats each session and recheck decay after restarts

- **Guidance:** Treat a player boat as safe from decay only for about a day of no steering input, then limited to 12 hours of decay, so move or dock it each session.
- **Evidence basis:** Decay delay and use definition [3]; timer persistence fix [9].
- **Confidence:** High. Primary Facepunch changelists, though numbers may be rebalanced.
- **So what:** Do not rely on an anchored, idle boat holding through a long absence.

## Guidance 2 — Do not trust pre-2026 community decay and fuel figures for cars and helicopters

- **Guidance:** Verify minicopter, scrap heli and car decay in game before planning around them.
- **Evidence basis:** Only 2019 and 2020 community sources give the numbers [21][22]; the wiki pages are placeholders [18][19].
- **Confidence:** Low. No primary source for current base values.
- **So what:** Admins and players should measure on their own server.

## Guidance 3 — Build boat hulls with a pointed bow

- **Guidance:** Prefer boat-shaped hulls over boxes for speed and fuel economy.
- **Evidence basis:** Drag changes [5]; engines burn fuel fast [2].
- **Confidence:** Medium. Direction is documented, magnitude is not.
- **So what:** A flat bow costs speed, and speed is the engine's main use for escape or pursuit.

## Guidance 4 — Expect air vehicle access to depend on repairing the Bandit Camp helipad

- **Guidance:** On default settings, plan a group repair of the Air Wolf pad early in the wipe before counting on purchased helicopters.
- **Evidence basis:** Repair rule [1]; prices from [20].
- **Confidence:** Medium. The mechanic is primary, prices are community.
- **So what:** Admins wanting instant access can set the convars named in [1].

# Open Questions

- Current base health, fuel capacity and decay for the minicopter, scrap helicopter, modular car, snowmobile, rowboat, RHIB and submarine: no primary source opened; resolve from in-game data.
- Boat Building Plan research cost after the September reduction: the wiki still shows 120 Scrap [9][12].
- Boat engine fuel burn rate and tank sizes: not stated in [2].
- Horse health, speed and stable pricing: not found on a primary source.
- Whether current Air Wolf prices match the June 2026 guide.
- Deep Sea network range 620 m versus 640 m [3].

# References

**Primary Sources**

- [1] **Facepunch** — *Livestock Update*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [2] **Facepunch** — *Naval Update*. https://rust.facepunch.com/news/naval/. Accessed 2026-10-08.
- [3] **Facepunch** — *Shipshape*. https://rust.facepunch.com/news/shipshape. Accessed 2026-10-08.
- [4] **Facepunch** — *Spring Clean*. https://rust.facepunch.com/news/spring-clean. Accessed 2026-10-08.
- [5] **Facepunch** — *Upgrade hard, raid harder*. https://rust.facepunch.com/news/upgrade-hard-raid-harder. Accessed 2026-10-08.
- [6] **Facepunch** — *Built Different*. https://rust.facepunch.com/news/built-different. Accessed 2026-10-08.
- [7] **Facepunch** — *Common Ground*. https://rust.facepunch.com/news/common-ground. Accessed 2026-10-08.
- [8] **Facepunch** — *Power Trip*. https://rust.facepunch.com/news/power-trip. Accessed 2026-10-08.
- [9] **Facepunch** — *Breach and Clear*. https://rust.facepunch.com/news/breach-and-clear. Accessed 2026-10-08.
- [10] **Facepunch** — *Vehicle Update*. https://rust.facepunch.com/news/vehicle-update. Accessed 2026-10-08.
- [11] **Facepunch Rust Wiki** — *Boat Building Station*. https://wiki.facepunch.com/rust/item/boatbuildingstation. Accessed 2026-10-08.
- [12] **Facepunch Rust Wiki** — *Boat Building Plan*. https://wiki.facepunch.com/rust/item/boat.planner. Accessed 2026-10-08.
- [13] **Facepunch Rust Wiki** — *Kayak*. https://wiki.facepunch.com/rust/item/kayak. Accessed 2026-10-08.
- [14] **Facepunch Rust Wiki** — *Small Boat Engine*. https://wiki.facepunch.com/rust/item/smallengine. Accessed 2026-10-08.
- [15] **Facepunch Rust Wiki** — *Engine Vehicle Module*. https://wiki.facepunch.com/rust/item/vehicle.1mod.engine. Accessed 2026-10-08.
- [16] **Facepunch Rust Wiki** — *Single Horse Saddle*. https://wiki.facepunch.com/rust/item/horse.saddle.single. Accessed 2026-10-08.
- [17] **Facepunch Rust Wiki** — *Vehicle Parts Crate and components*. https://wiki.facepunch.com/rust/vehicle_parts. Accessed 2026-10-08.
- [18] **Facepunch Rust Wiki** — *MC repair*. https://wiki.facepunch.com/rust/item/minihelicopter.repair. Accessed 2026-10-08.
- [19] **Facepunch Rust Wiki** — *ScrapTransportHeliRepair*. https://wiki.facepunch.com/rust/item/scraptransportheli.repair. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- [20] **XGamingServer** — *Rust Vehicles Guide: Horses, Cars, Boats and Helis* (4 June 2026). https://xgamingserver.com/blog/rust-vehicles-guide-horses-cars-boats. Accessed 2026-10-08.
- [21] **Rustafied** — *Modular vehicles are here* (2 July 2020). https://www.rustafied.com/updates/2020/7/2/modular-vehicles-are-here. Accessed 2026-10-08.
- [22] **Rustafied** — *Meet the scrap transport helicopter* (2 September 2019). https://www.rustafied.com/updates/2019/9/2/meet-the-scrap-transport-helicopter. Accessed 2026-10-08.

**Further Reading**

None.

# Further Reading

None beyond the references above.

# Related Documents

- rust-game-mechanics-foundation (parent)
- rust-monuments-loot, rust-farming-food, rust-wipes-map-generation
- rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence
- rust-server-convars-reference, rust-update-timeline-2026

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
