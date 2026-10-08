---
id: rust-electricity-logic
title: "Rust Electricity and Logic"
version: 1.0.0
status: frozen
confidence: Medium
category: Game Mechanics
topic: "Electricity and logic"
market: "Global"
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-building-raiding-foundation, rust-server-administration-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation, rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence, rust-server-convars-reference, rust-plugin-development-hooks, rust-update-timeline-2026, rust-monuments-loot, rust-farming-food, rust-vehicles, rust-wipes-map-generation, rust-moderation-anti-cheat, rust-carbon-vs-oxide, rust-turrets-deployables, rust-wildlife-npcs, rust-server-permissions-rcon, rust-server-performance, rust-game-modes]
tags: [electricity, power, battery, solar, wind-turbine, generator, wiring, logic-gates, timer, counter, memory-cell]
game_build_checked: "Livestock Update (1 October 2026); wiki item pages read 2026-10-08 (page-level build not stated)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-electricity-logic |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Game Mechanics |
| Region | Global |
| Game build checked | Livestock Update (1 October 2026); wiki item pages read 2026-10-08 |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This document goes deeper than the game mechanics foundation on Rust's electrical system: the power sources (solar panel, wind turbine, small generator), the rechargeable batteries, the wire tool, and the logic and switching components (switch, timer, counter, memory cell, AND, OR, XOR, RAND, blocker, splitter, branch, combiner). Values come from the Facepunch Rust Wiki item pages, which are first-party, and from Facepunch devblogs that record when behaviour changed.

Confidence is Medium. Item stats are Primary and consistent, but the wiki pages do not state which build they reflect, several mechanics (fuel burn rate, wire limits, power cost of most devices) are not on any page opened, and the wiki shows values that differ from the 2019 devblog (small battery), so some figures may lag the live game.

# Key Facts

- Three craftable power sources exist on the wiki pages checked: the Large Solar Panel (20 rW) [1], the Wind Turbine (150 rW) [2] and the Small Generator (40 rW, fuelled by Low Grade Fuel) [3].
- The Large, Medium and Small Rechargeable Batteries list 24000, 9000 and 400 rWm capacity and 100, 50 and 15 rW output respectively [4][5][6].
- Solar output depends on sun intensity and the panel's angle to the sun [1]; wind turbine output varies with wind speed [2].
- Since the April 2024 devblog, logic gates no longer need power; active components such as turrets, sensors and lights still do [24].
- The Auto Turret lists 10 rW consumption [21]; the HBHF Sensor lists 1 rW [20].
- The Wire Tool is known by default and costs 2 High Quality Metal [7].
- Several logic parts (timer, counter, memory cell, AND, OR, XOR) craft from Metal Fragments only [8][9][10][11][12][13].

# Scope

Covers power generation, storage, wiring and logic components in vanilla Rust (PC) as documented on the Facepunch wiki and devblogs. It does not cover turrets and other deployables in depth (see rust-turrets-deployables), industrial automation, or plugin-based electrical behaviour. Build checked: Livestock Update, 1 October 2026 (the wiki pages themselves do not state a build).

# Definitions

- **rW (Rust Watt):** the unit of electrical power production and consumption on item pages [1][4].
- **rWm (Rust Watt Minutes):** battery storage; the number of minutes of discharge at 1 power unit the battery holds [25].
- **Passthrough:** power that a component forwards to its output, for example the Timer passes power for a duration [8].
- **Control input:** a non-power input such as Toggle On, Set, Reset or Switch Off [8][10][15].

# Core Mechanics

**Power sources.** The Large Solar Panel produces 20 rW, with output depending on sun intensity and the panel's angle to the sun [1]. The Wind Turbine lists 150 rW and its description says the amount generated varies with wind speed [2]. The Small Generator is powered by Low Grade Fuel and outputs 40 power; it has Force Start and Force Stop control inputs [3]. The page does not give a fuel consumption rate [3].

**Batteries.** Capacity is measured in rWm, the minutes of discharge at 1 power unit [25]. The Large Battery lists 100 rW production and 24000 rWm capacity with a Fully Charged signal output [4]. The Medium Battery lists 50 rW and 9000 rWm; its page says it needs a minimum charge of 5 seconds to discharge, charges at a rate depending on power input with a maximum 80 percent efficiency, and can be wired in series [5]. The Small Battery lists 15 rW and 400 rWm [6]. The 2018 devblog states that batteries must have at least 5 seconds of juice to begin discharging and that batteries were fixed to wire in series [26].

**Wiring.** The Wire Tool connects electrical objects: aim at an object, click an input or output handle, then click another object's handle; holding right mouse clears or cancels a connection [7]. The page does not state connection limits [7].

**Switching and logic.** Each component below is described by its wiki page.

- **Switch:** inputs Power In, Switch On, Switch Off; output Power Out [15].
- **Button:** a simple electric button with Power In and Power Out [22].
- **Timer:** passes power through for a duration; inputs Power In and Toggle On [8].
- **Counter:** inputs Power In, Increment, Decrement, Clear; output Passthrough, which allows passthrough when a target is reached [9].
- **Memory Cell:** a 1-bit storage component; Set stores 1, Reset stores 0, Toggle flips the state, and it has an Output and an Inverted Output [10].
- **AND Switch:** passes power only when both inputs receive power, with the passthrough amount the greater of the two sources [11].
- **OR Switch:** passthrough amount is the greater of either power source [12].
- **XOR Switch:** passes power only if exactly one input receives power [13].
- **RAND Switch:** each time the Set input receives power it rolls true or false to allow passthrough [17].
- **Blocker:** prevents passthrough while power is received on its Block Passthrough input [14].
- **Splitter:** splits a signal into 3; the output amount is the input divided by the number of output slots in use [16].
- **Electrical Branch:** branches power off a main line by a set amount, with Branch Out and Power Out [18].
- **Root Combiner:** combines two root electrical sources into one signal; it can be wired in series but cannot be used with components that do not produce energy [19].
- **Sensors:** the Pressure Pad allows power to flow while a player stands on it [23]; the HBHF Sensor's passthrough equals the number of humans detected in a 10 m radius [20].

# Reference Data

Values from Facepunch Rust Wiki item pages, read 2026-10-08 (Livestock Update era; the pages do not state a build).

| Item | Production / capacity | Workbench | Cost | Source |
|------|----------------------|-----------|------|--------|
| Large Solar Panel | 20 rW | 1 | 5 High Quality Metal, 1 Tech Trash | [1] |
| Wind Turbine | 150 rW | 2 | 500 Wood, 10 High Quality Metal, 3 Gears, 3 Sheet Metal | [2] |
| Small Generator | 40 rW | 2 | 5 High Quality Metal, 2 Gears | [3] |
| Large Battery | 100 rW, 24000 rWm | 2 | 10 High Quality Metal, 2 Tech Trash | [4] |
| Medium Battery | 50 rW, 9000 rWm | 2 | 5 High Quality Metal, 1 Tech Trash | [5] |
| Small Battery | 15 rW, 400 rWm | 1 | 5 High Quality Metal | [6] |
| Wire Tool | n/a | 1 | 2 High Quality Metal | [7] |

| Component | Workbench | Cost | Source |
|-----------|-----------|------|--------|
| Switch | 1 | 100 Metal Fragments | [15] |
| Timer | 1 | 75 Metal Fragments | [8] |
| Blocker | 1 | 75 Metal Fragments | [14] |
| OR Switch | 1 | 100 Metal Fragments | [12] |
| XOR Switch | 1 | 100 Metal Fragments | [13] |
| Splitter | 1 | 100 Metal Fragments | [16] |
| Electrical Branch | 1 | 75 Metal Fragments | [18] |
| Root Combiner | 1 | 75 Metal Fragments | [19] |
| Button | 1 | 75 Metal Fragments | [22] |
| Pressure Pad | 1 | 150 Wood, 1 Gears, 1 Metal Spring | [23] |
| AND Switch | 2 | 100 Metal Fragments | [11] |
| Counter | 2 | 75 Metal Fragments | [9] |
| Memory Cell | 2 | 75 Metal Fragments | [10] |
| RAND Switch | 2 | 75 Metal Fragments | [17] |
| HBHF Sensor | 2 | 75 Metal Fragments | [20] |

Consumption values listed on wiki pages: Auto Turret 10 rW [21]; HBHF Sensor 1 rW [20]. The Button and Pressure Pad pages list a "Power Production" of 2 rW and 1 rW respectively, which the pages do not explain [22][23].

Historical battery spec (7 November 2019): Small 150 rWm and 10 output, Medium 9000 rWm and 50 output, Large 24,000 rWm and 100 output [25].

# Version & Patch Notes

- **6 December 2018:** electricity added, with 17 electrical components and the Wire Tool; original specs included Large Battery 100, Small Battery 10, Solar Panel 30 maximum and Windmill 100 [27].
- **13 December 2018:** solar panel output lowered to 20 and scaled by health; batteries given less capacity but higher charge efficiency, series wiring fixed, 5-second minimum charge to discharge [26].
- **7 November 2019:** batteries moved to rWm; the Medium Battery was added [25].
- **7 May 2020:** solar panels decay when placed outside building privilege [28].
- **4 April 2024:** power requirements removed from all logic gates; components align to walls [24].

Volatile: all rW and rWm values. The wiki Small Battery (15 rW, 400 rWm) differs from the 2019 devblog (10, 150 rWm) [6][25], so the numbers changed after that post; the date is not sourced.

# Common Pitfalls

- Treating old guides as current: the logic gates stopped needing power in April 2024 [24], so older wiring advice about gate power cost is outdated.
- Placing solar panels outside building privilege: they decay there [28].
- Expecting a combiner to merge anything: it works only with energy-producing sources [19].
- Expecting a battery to discharge immediately: it needs a minimum charge to begin [5][26].
- Expecting AND or OR to sum their inputs: both pass the greater of the two sources [11][12].

# Interactions & Related Systems

Electricity powers the Auto Turret [21]; see rust-turrets-deployables for turret behaviour and rust-raiding-costs-defence for defence costs. The wiki lists further electrical consumers such as the Electric Furnace, Electric Heater, Water Pump, Elevator and Industrial Conveyor [29]; their consumption values were not opened here. Workbench tiers gate crafting (see rust-items-crafting-foundation) and the parent system overview is in rust-game-mechanics-foundation.

# Assessed Guidance

## Guidance 1 — Pair solar or wind with a battery rather than wiring them straight to loads

- **Guidance:** Treat solar and wind as variable sources and put a battery between them and critical loads.
- **Evidence basis:** Solar output varies with sun and angle [1]; wind turbine output varies with wind speed [2]; batteries store energy in rWm [4][25].
- **Confidence:** Medium. The variability is cited, but the design recommendation is inference.
- **So what:** A base running turrets is less likely to lose power when output dips.

## Guidance 2 — Do not budget power for logic gates, but do for sensors and turrets

- **Guidance:** When estimating load, count active devices and ignore logic gates.
- **Evidence basis:** Gates lost power requirements in April 2024 [24]; turret and sensor consumption is listed [21][20].
- **Confidence:** Medium. The devblog is Primary but the wiki pages list no gate consumption, so the absence is inferred.
- **So what:** Smaller generators suffice for gate-heavy circuits.

## Guidance 3 — Verify numbers in game before building a large circuit

- **Guidance:** Check item inspect values in game after each monthly update.
- **Evidence basis:** Small Battery values differ between wiki and 2019 devblog [6][25]; wiki pages state no build.
- **Confidence:** High. The discrepancy itself is documented.
- **So what:** Avoid relying on remembered figures.

# Open Questions

- Low Grade Fuel burn rate for the Small Generator: not on the page [3].
- Wire tool connection limits and maximum wire length: not on the page [7].
- Power consumption of most devices (Electric Furnace, Heater, Water Pump, Elevator): not opened.
- Whether wind turbine output has a height or altitude dependence today; the 2018 devblog said stronger wind is likelier with altitude [27], not re-confirmed.
- When the Small Battery changed from 10 rW and 150 rWm to 15 rW and 400 rWm.
- Meaning of Power Production values on the Button and Pressure Pad pages [22][23].
- Which build the wiki item pages reflect.

# References

**Primary Sources** — Facepunch wiki pages and devblogs.

- [1] **Facepunch Rust Wiki** — *Large Solar Panel*. https://wiki.facepunch.com/rust/item/electric.solarpanel.large. Accessed 2026-10-08.
- [2] **Facepunch Rust Wiki** — *Wind Turbine*. https://wiki.facepunch.com/rust/item/generator.wind.scrap. Accessed 2026-10-08.
- [3] **Facepunch Rust Wiki** — *Small Generator*. https://wiki.facepunch.com/rust/item/electric.fuelgenerator.small. Accessed 2026-10-08.
- [4] **Facepunch Rust Wiki** — *Large Rechargeable Battery*. https://wiki.facepunch.com/rust/item/electric.battery.rechargable.large. Accessed 2026-10-08.
- [5] **Facepunch Rust Wiki** — *Medium Rechargeable Battery*. https://wiki.facepunch.com/rust/item/electric.battery.rechargable.medium. Accessed 2026-10-08.
- [6] **Facepunch Rust Wiki** — *Small Rechargeable Battery*. https://wiki.facepunch.com/rust/item/electric.battery.rechargable.small. Accessed 2026-10-08.
- [7] **Facepunch Rust Wiki** — *Wire Tool*. https://wiki.facepunch.com/rust/item/wiretool. Accessed 2026-10-08.
- [8] **Facepunch Rust Wiki** — *Timer*. https://wiki.facepunch.com/rust/item/electric.timer. Accessed 2026-10-08.
- [9] **Facepunch Rust Wiki** — *Counter*. https://wiki.facepunch.com/rust/item/electric.counter. Accessed 2026-10-08.
- [10] **Facepunch Rust Wiki** — *Memory Cell*. https://wiki.facepunch.com/rust/item/electrical.memorycell. Accessed 2026-10-08.
- [11] **Facepunch Rust Wiki** — *AND Switch*. https://wiki.facepunch.com/rust/item/electric.andswitch. Accessed 2026-10-08.
- [12] **Facepunch Rust Wiki** — *OR Switch*. https://wiki.facepunch.com/rust/item/electric.orswitch. Accessed 2026-10-08.
- [13] **Facepunch Rust Wiki** — *XOR Switch*. https://wiki.facepunch.com/rust/item/electric.xorswitch. Accessed 2026-10-08.
- [14] **Facepunch Rust Wiki** — *Blocker*. https://wiki.facepunch.com/rust/item/electric.blocker. Accessed 2026-10-08.
- [15] **Facepunch Rust Wiki** — *Switch*. https://wiki.facepunch.com/rust/item/electric.switch. Accessed 2026-10-08.
- [16] **Facepunch Rust Wiki** — *Splitter*. https://wiki.facepunch.com/rust/item/electric.splitter. Accessed 2026-10-08.
- [17] **Facepunch Rust Wiki** — *RAND Switch*. https://wiki.facepunch.com/rust/item/electric.random.switch. Accessed 2026-10-08.
- [18] **Facepunch Rust Wiki** — *Electrical Branch*. https://wiki.facepunch.com/rust/item/electrical.branch. Accessed 2026-10-08.
- [19] **Facepunch Rust Wiki** — *Root Combiner*. https://wiki.facepunch.com/rust/item/electrical.combiner. Accessed 2026-10-08.
- [20] **Facepunch Rust Wiki** — *HBHF Sensor*. https://wiki.facepunch.com/rust/item/electric.hbhfsensor. Accessed 2026-10-08.
- [21] **Facepunch Rust Wiki** — *Auto Turret*. https://wiki.facepunch.com/rust/item/autoturret. Accessed 2026-10-08.
- [22] **Facepunch Rust Wiki** — *Button*. https://wiki.facepunch.com/rust/item/electric.button. Accessed 2026-10-08.
- [23] **Facepunch Rust Wiki** — *Pressure Pad*. https://wiki.facepunch.com/rust/item/electric.pressurepad. Accessed 2026-10-08.
- [24] **Facepunch** — *Waves Of Change* (4 April 2024). https://rust.facepunch.com/news/waves-of-change. Accessed 2026-10-08.
- [25] **Facepunch** — *The Tree Fix Update* (7 November 2019). https://rust.facepunch.com/news/november-update. Accessed 2026-10-08.
- [26] **Facepunch** — *Season's Beatings* (13 December 2018). https://rust.facepunch.com/news/season-s-beatings. Accessed 2026-10-08.
- [27] **Facepunch** — *The Electric Anniversary* (6 December 2018). https://rust.facepunch.com/news/electric-anniversary. Accessed 2026-10-08.
- [28] **Facepunch** — *Night Vision Update* (7 May 2020). https://rust.facepunch.com/news/night-vision-update. Accessed 2026-10-08.
- [29] **Facepunch Rust Wiki** — *Rust Wiki home (electrical item index)*. https://wiki.facepunch.com/rust/. Accessed 2026-10-08.

**Community & Practitioner Evidence**

None cited.

**Further Reading**

See the Further Reading section.

# Further Reading

The other Electrical entries on the wiki home page [29], including the Laser Detector, Smart Switch and Storage Adaptor, are worth reading but were not opened here.

# Related Documents

- rust-game-mechanics-foundation
- rust-turrets-deployables
- rust-raiding-costs-defence
- rust-items-crafting-foundation
- rust-server-performance

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
