---
id: rust-world-events
title: "Rust World Events"
version: 1.0.0
status: frozen
confidence: Medium
category: Game Mechanics
topic: "Cargo ship, airdrops and map events"
market: "Global"
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-game-mechanics-foundation, rust-wildlife-npcs, rust-monuments-loot, rust-vehicles, rust-combat-damage-model, rust-updates-meta-foundation, rust-update-timeline-2026, rust-server-convars-reference, rust-raiding-costs-defence]
tags: [events, cargo-ship, airdrop, supply-signal, patrol-helicopter, bradley, chinook, satellite-crash]
game_build_checked: "Livestock Update (1 October 2026)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-world-events |
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

This deep-dive covers Rust's server-driven world events: the Cargo Ship, airdrops and the Supply Signal, the Chinook locked-crate event, the Patrol Helicopter, the Bradley APC and the Satellite Crash event added in 2026. It goes deeper than rust-game-mechanics-foundation and leaves NPC statistics to rust-wildlife-npcs.

Mechanics and loot tables come from Facepunch devblogs and the Facepunch wiki, so they are primary. But most spawn timings are stated only in devblogs from 2015 to 2018 and no current-build value was found for them. The Livestock Update of 1 October 2026 contains one cargo ship fix and no airdrop, Bradley, helicopter or Chinook change [1]. The document is rated Medium: mechanics are well sourced, current timers are not.

# Key Facts

- The Cargo Ship fills with loot on spawn, refreshes it every 10 minutes for up to three rounds, and departs after 50 minutes by default; the refresh timing and duration were configurable per the 2018 devblog [6].
- Since April 2024 the ship docks at a harbour, and from May 2024 at both harbours if they exist, before leaving [7][8].
- The Livestock Update (1 October 2026) lists one cargo ship fix and no airdrop, helicopter, Bradley or Chinook change [1].
- The Airdrop container has 14 slots and a 40-entry loot table on the wiki, checked against the Livestock build [13].
- The Chinook event delivers a locked crate that needs a timed hack; damage to the computer slows it [9].
- Power Trip (6 August 2026) added a Satellite Crash event and Airfield terminals that raise airdrop rate and call a Chinook resupply [3].
- Breach and Clear (3 September 2026) improved save/load of Patrol Helicopter, Bradley, cargo and satellite events [2].
- No current-build Facepunch figure was found for how often the Patrol Helicopter or an airdrop spawns (see Open Questions).

# Scope

Covered: Cargo Ship, airdrops, Supply Signal, Chinook locked crate, Patrol Helicopter, Bradley APC and the Satellite Crash event, on vanilla PC servers, checked against the Livestock Update (1 October 2026). Not covered: NPC health and weapons (see rust-wildlife-npcs), fixed-monument loot (rust-monuments-loot), vehicles (rust-vehicles), seasonal cosmetic events, and Twitch Drops promotions, which are not in-game world events [1]. Oil Rig is mentioned only where a 2026 fix touches it.

# Definitions

- **Server event:** a periodic, server-spawned occurrence rather than a fixed monument; Facepunch applies this term to the Cargo Ship, Patrol Helicopter and Chinook [5][9][10].
- **Locked crate:** a crate that must be hacked with a timer before opening [9].
- **Supply Signal:** a purple smoke grenade used to mark a spot for an airdrop [14].
- **Loot round:** a Cargo Ship refill of its crates [6].

# Core Mechanics

**Evidence layer.** Dates reflect when Facepunch described the behaviour; only the Livestock Update statement is tied to the checked build.

**Cargo Ship.** Introduced in 2018 as the CCSC Lazarus, a periodic server event that "will trigger every two to four in-game days" and patrols about 200 metres offshore [5]. Players board by boat and mount a ladder; two codelocked crates are hacked after clearing the defending Scientists, turret-style Scientists never move, and the whole server can see the ship on the map [5]. A radiation alarm warns that the cargo is unstable and it is time to leave [5]. A later 2018 devblog changed it to loot rounds: on spawn, 1 Locked Crate, 1 Elite Crate, 4 Military Crates and 4 Regular Crates appear, including below deck; loot respawns every 10 minutes for three rounds, a horn signals each new round, and the ship departs after 50 minutes [6]. In April 2024 harbour docking arrived: the ship picks the first harbour it passes and docks once, cranes load containers onto the deck, and docking attempts one loot refresh, with no further loot once all three rounds are used [7]. In May 2024 it was changed to dock at both harbours if they exist, containers spawn when the approach starts, and the map shows whether it has docked [8]. Event save/load was improved in September 2026 [2].

**Airdrops.** The wiki describes the Supply Signal as purple smoke marking a location for an airdrop [14]. Airdrop loot was made to guarantee more good items and less junk in the April 2018 vehicle update [9], and in 2017 was set to always drop two weapons plus ammo and two armour pieces [12]. Power Trip adds a smaller Airfield terminal which, when charged, raises the rate at which airdrops fall across the map; it slowly loses charge [3]. The wiki does not state an airdrop interval [13].

**Chinook locked crate.** A periodic server event that appears offshore and flies to a drop zone at most Tier 1 and above monuments, orbits to neutralise threats, then releases a locked crate [9]. Pressing use starts the timer; damaging the computer slows it, and all maps show an icon for locked supply crates [9]. Power Trip also lets a charged larger Airfield terminal call a Chinook resupply crate near the airfield tarmac [3].

**Patrol Helicopter.** Devblog 78 (2015) said one spawns offshore every 48 to 72 in-game hours and patrols between monuments [10]. Waves of Change (April 2024) randomises attack-run values, adds an orbit phase, scores invisible zones by damage taken and makes it flee no-go zones [7]. Meta Madness (May 2024) makes it try to crash at a nearby non-safe-zone monument on death, flee when a player quickly removes 30% of its HP, and target players on boats, cargo and trains [8]. Its crash drops a Helicopter Crate [16].

**Bradley APC.** Added to Launch Site in August 2017, with a main cannon and coaxial machine gun and slim initial loot [11], and to Materials Extraction (Hapis) in November 2017 [12]. Waves of Change lets Scientists deploy from it, at Launch Site and on roads at the end of the month [7]. Meta Madness spawns them in stages: 2 at 80% health, 4 more at 60%, 6 more at 40% [8]. The admin command bradley.quickrespawn respawns the Launch Site Bradley [18].

**Satellite Crash.** Added in Power Trip: a Satellite Control Computer at Launch Site is powered and aimed, the satellite descends visibly to all players, and spills crates that must cool before looting [3]. The post gives no counts or timers [3].

# Reference Data

Checked 2026-10-08, Livestock build, wiki values unless stated.

| Event or container | Value | Source |
|--------------------|-------|--------|
| Airdrop (supply_drop) | 14 slots, 40-item table | [13] |
| Airdrop top rows | Pistol Bullet 15-48 at 94.2%; Scrap 140-160 at 55.6%; Satchel Charge at 49.0%; LR-300 at 3.8% | [13] |
| Bradley Crate | 7 slots; MLRS Rocket 1-4 at 100%; Targeting Computer 52.4%; Auto Turret 4.8% | [15] |
| Helicopter Crate | 1 slot, 40-item table; 5.56 Rifle Ammo 8-120 at 27.7%; M249 10.0% | [16] |
| Cargo Ship Scientist | 6 slots, 211-item table; Pistol Bullet 15 at 51.9%; Supply Signal 0.4% | [17] |
| Supply Signal | stack 1, despawn 1 hour, not craftable | [14] |
| Cargo Ship start loot | 1 Locked, 1 Elite, 4 Military, 4 Regular crate (2018) | [6] |
| Cargo loot rounds | every 10 min, 3 rounds, 50 min stay (2018 defaults) | [6] |
| Bradley scientist stages | 2 at 80%, 4 at 60%, 6 at 40% HP (May 2024) | [8] |
| Heli flee trigger | 30% HP removed quickly (May 2024) | [8] |
| patrolhelicopterai.flee_damage_percentage | 1 or over disables the flee mechanic | [7] |
| patrolhelicopterai.use_danger_zones | enables or disables no-go and aggro zones | [7] |
| patrolhelicopterai.monument_crash | admins can disable monument crashing | [8] |
| CargoShip.loot_rounds, loot_round_spacing_minutes, event_duration_minutes | named as the 2018 controls | [6] |
| heli.call, heli.calltome | admin commands to start the heli event | [18] |

# Version & Patch Notes

- Sept 2015, Devblog 78: Patrol Helicopter introduced [10].
- Aug 2017, Devblog 174: Bradley APC added to Launch Site [11]; Nov 2017 Hapis [12].
- 2018: Cargo Ship [5], loot rounds [6], Chinook event [9].
- Apr and May 2024: harbour docking, heli zones, Bradley stages [7][8].
- 2 July 2026, Common Ground: fix for bots and sleepers streaming out when the cargo ship moves [4].
- 6 Aug 2026, Power Trip: Satellite Crash, Airfield terminals; cargo and heli markers no longer sent to Rust+ [3].
- 3 Sept 2026, Breach and Clear: improved save/load of oil rigs, cargo, patrol heli, Bradley and satellite events; supply drop LOD fixes [2].
- 1 Oct 2026, Livestock: fixed parent-history antihack causing invincibility on the cargo ship; attack heli armour plates fall off by side hit; hackable crates no longer give excess clan points [1].
- Volatile: all timers, spawn rates and loot tables.

# Common Pitfalls

- Treating 2018 defaults (50 minutes, 10-minute rounds) as current; no 2026 source confirms them [6].
- Looting late: once docking has used a refresh and all three rounds have happened, the ship cannot spawn more loot [7].
- Keeping containers across harbours: containers already placed on the ship are deleted on approach to the next harbour [8].
- Assuming the Twitch Drops "Rust Isles" notice is an in-game event; it is not [1].
- Assuming Rust+ still shows event markers; Power Trip stopped sending cargo and heli markers [3].

# Interactions & Related Systems

NPC stats, scientists and animals: rust-wildlife-npcs [17]. Fixed monument loot and the Launch Site: rust-monuments-loot [3]. Explosive damage for Bradley and the heli: rust-combat-damage-model. Heli-based vehicles: rust-vehicles [1]. Convar listings: rust-server-convars-reference [18]. Update chronology: rust-update-timeline-2026 and rust-updates-meta-foundation [1].

# Assessed Guidance

## Guidance 1 — Treat all event timers as server-specific and verify them

- **Guidance:** Do not plan around a fixed spawn interval; check the server's own settings or observe a cycle.
- **Evidence basis:** Interval values date from 2015 and 2018 devblogs [5][10], and a community guide says heli frequency depends on configuration [19].
- **Confidence:** Medium. The age of the sources is documented; the practical advice is judgement.
- **So what:** Admins should state event settings in the server description; players should not rely on a wiki number.

## Guidance 2 — Loot the Cargo Ship early and know your rounds

- **Guidance:** Arrive before the first horn and plan for the docking refresh rather than waiting for a late round.
- **Evidence basis:** Three rounds, 10-minute spacing, a docking refresh and an end-of-loot rule are described in devblogs [6][7].
- **Confidence:** Medium. The mechanics are primary but their defaults may have changed.
- **So what:** Fewer wasted trips and less exposure to the contested harbour.

## Guidance 3 — Expect Bradley to bring reinforcements

- **Guidance:** Plan ammunition and cover for 12 extra Scientists across the fight, not just the APC.
- **Evidence basis:** Stage spawns at 80, 60 and 40% health [8], and the Bradley Crate lists rockets as guaranteed [15].
- **Confidence:** Medium. Stage thresholds are from May 2024 and not rechecked in 2026.
- **So what:** Solo attempts are costlier than the crate alone suggests.

# Open Questions

- Current spawn interval of the Patrol Helicopter: only a 2015 value [10] and a community figure [19] were found.
- Current airdrop interval, plane behaviour and the size of the Airfield terminal boost: not stated by sources opened.
- Disarm duration of the Chinook and Satellite crates: not stated.
- Whether the 2018 Cargo Ship defaults (50 minutes, three rounds) survive on the Livestock build.
- Bradley respawn delay on the current build; no Facepunch source was found.
- Oil Rig and Excavator events are outside this document's sources.

# References

**Primary Sources**

- [1] **Facepunch** — *Livestock Update*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [2] **Facepunch** — *Breach and Clear*. https://rust.facepunch.com/news/breach-and-clear. Accessed 2026-10-08.
- [3] **Facepunch** — *Power Trip*. https://rust.facepunch.com/news/power-trip. Accessed 2026-10-08.
- [4] **Facepunch** — *Common Ground*. https://rust.facepunch.com/news/common-ground. Accessed 2026-10-08.
- [5] **Facepunch** — *The Cargo Ship Update*. https://rust.facepunch.com/news/the-cargo-ship-update. Accessed 2026-10-08.
- [6] **Facepunch** — *The Hot Air Balloon Update*. https://rust.facepunch.com/news/the-hot-air-balloon-update. Accessed 2026-10-08.
- [7] **Facepunch** — *Waves Of Change*. https://rust.facepunch.com/news/waves-of-change. Accessed 2026-10-08.
- [8] **Facepunch** — *Meta Madness*. https://rust.facepunch.com/news/meta-madness. Accessed 2026-10-08.
- [9] **Facepunch** — *Vehicle Update* (5 April 2018). https://rust.facepunch.com/news/vehicle-update. Accessed 2026-10-08.
- [10] **Facepunch** — *Devblog 78* (17 September 2015). https://rust.facepunch.com/news/devblog-78. Accessed 2026-10-08.
- [11] **Facepunch** — *Devblog 174* (24 August 2017). https://rust.facepunch.com/news/devblog-174. Accessed 2026-10-08.
- [12] **Facepunch** — *Devblog 184* (2 November 2017). https://rust.facepunch.com/news/devblog-184. Accessed 2026-10-08.
- [13] **Facepunch Rust Wiki** — *Airdrop*. https://wiki.facepunch.com/rust/airdrop. Accessed 2026-10-08.
- [14] **Facepunch Rust Wiki** — *Supply Signal*. https://wiki.facepunch.com/rust/item/supply.signal. Accessed 2026-10-08.
- [15] **Facepunch Rust Wiki** — *Bradley Crate*. https://wiki.facepunch.com/rust/bradley-crate. Accessed 2026-10-08.
- [16] **Facepunch Rust Wiki** — *Helicopter Crate*. https://wiki.facepunch.com/rust/helicopter-crate. Accessed 2026-10-08.
- [17] **Facepunch Rust Wiki** — *Cargo Ship Scientist*. https://wiki.facepunch.com/rust/cargo-ship-scientist. Accessed 2026-10-08.
- [18] **Facepunch Rust Wiki** — *Useful Commands*. https://wiki.facepunch.com/rust/useful_commands. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- [19] **XGamingServer** — *Rust Bradley APC & Patrol Helicopter Guide* (11 June 2026). https://xgamingserver.com/blog/rust-bradley-patrol-helicopter-guide/. Accessed 2026-10-08.

**Further Reading**

None.

# Further Reading

The Facepunch news index for later cargo ship and helicopter changes.

# Related Documents

- rust-game-mechanics-foundation
- rust-wildlife-npcs
- rust-monuments-loot
- rust-vehicles
- rust-updates-meta-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
