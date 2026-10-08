---
id: rust-turrets-deployables
title: "Rust Turrets and Defensive Deployables"
version: 1.0.0
status: frozen
confidence: Medium
category: Building & Raiding
topic: "Turrets and deployables"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-building-raiding-foundation, rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-server-administration-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation, rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence, rust-server-convars-reference, rust-plugin-development-hooks, rust-update-timeline-2026, rust-monuments-loot, rust-farming-food, rust-vehicles, rust-wipes-map-generation, rust-moderation-anti-cheat, rust-carbon-vs-oxide, rust-electricity-logic, rust-wildlife-npcs, rust-server-permissions-rcon, rust-server-performance, rust-game-modes]
tags: [auto-turret, shotgun-trap, flame-turret, sam-site, barricade, locks, traps, deployables, power]
game_build_checked: "Livestock Update, 1 October 2026"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-turrets-deployables |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Building & Raiding |
| Region | Global |
| Game build checked | Livestock Update, 1 October 2026 [1] |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This deep-dive covers the defensive deployables that sit on top of the base layer described in the foundation document: the auto turret, shotgun trap, flame turret, SAM site, snap trap, landmine, floor spikes, the barricade family, the two alarms and the two lock types. For each it records crafting cost, workbench level, power draw and ammunition where the Facepunch wiki gives them, and the recent patch changes that touched them. Raid costs and structure hit points are left to rust-raiding-costs-defence.

The headline is that the Facepunch item pages give recipes and some power figures but no range, health or damage for any of these items, so those values are listed as unsourced rather than guessed. Confidence is Medium: recipes, power figures and patch history are primary and tied to the checked build, but targeting behaviour, ammo capacities and the SAM site's roles come from a single community guide that states no game version.

# Key Facts

- The auto turret costs 10 high quality metal, 1 CCTV camera and 1 targeting computer at Workbench Level 2, draws 10 rW, and searches a 180-degree arc facing the player who placed it [7].
- The shotgun trap costs 500 wood, 250 metal fragments, 2 gears and 2 rope at Workbench Level 1 and is loaded with handmade shells [8].
- The flame turret costs 200 metal fragments, 2 empty propane tanks and 1 gears at Workbench Level 1 and requires low grade fuel [9].
- The wiki lists the SAM site as not craftable, drawing 25 rW and using SAM ammo [10][11].
- A Tool Cupboard authorises its owner for flame and shotgun traps; the wiki words this as traps "that require TC privilege" [25].
- The September 2026 update made SAM sites better at shooting down hostile drones [2]; the October 2026 Livestock Update let remotely controlled turrets hit reactive targets and overhauled sandbag barricades [1].
- No item page opened for this document lists range, health or damage for a turret, trap or barricade [7][8][9][10][13][14][15][18][19][20].

# Scope

Covered: the auto turret, shotgun trap, flame turret, SAM site, snap trap, landmine, wooden floor spikes, wooden, stone, barbed wooden, metal and sandbag barricades, the tin can and smart alarms, and the code and key locks, on vanilla PC Rust at the Livestock Update (1 October 2026). Power and ammo are given only where a source states them.

Not covered: explosive costs and structure HP (see rust-raiding-costs-defence), the electrical circuit system in general (see rust-electricity-logic), weapon and ammo stats (see rust-weapons-ammo), wildlife and NPC turrets (see rust-wildlife-npcs) and plugin behaviour on modded servers. Console is excluded.

# Definitions

- **rW:** the unit the wiki uses for power draw on an item's electrical section [7][10][22].
- **Building privilege (TC privilege):** authorisation granted through a Tool Cupboard, which the wiki ties to flame and shotgun traps [25].
- **Peacekeeper / Attack All:** the two auto turret targeting modes as described by one community guide (green and red laser) [26].

# Core Mechanics

**Auto turret.** The wiki describes it as an item that engages moving targets it has line of sight to, requiring a projectile weapon and matching ammunition. It draws 10 rW and has outputs for Has Target, Low Ammo and No Ammo. It searches a 180-degree arc facing the player at placement [7]. A community guide adds that the turret does not read the Tool Cupboard, so each turret is authorised individually, and that Peacekeeper mode treats everyone as friendly until they act hostile while Attack All fires at anyone unauthorised; it also says settings need building privilege and the turret powered off [26]. That guide gives no game version [26]. Patch notes show turrets attached to a burst-fire gun (the M16A2) use burst fire since 2 July 2026 [3], and a fix stopped turrets hitting a player's shield after it broke on 4 June 2026 [4].

**Shotgun trap.** A trap triggered by movement, placed near doorways and loaded with handmade shells [8]. Handmade shells are listed as ammo with multiple projectiles [12]. The Tool Cupboard wiki says authorisation covers traps that require TC privilege, naming flame and shotgun traps [25]. The community guide says the trap fires at unauthorised players when a TC is in range and at everyone otherwise, needs no power, and cites roughly two shells per second and a 384-shell reserve as commonly quoted figures; none of that is on the wiki item page [26].

**Flame turret.** The wiki describes an automated turret that requires low grade fuel and sprays flames when triggered [9]. The community guide states a fuel capacity of up to 500, a roughly 90-degree frontal cone, and that it needs no power [26]. The wiki page gives no fuel use, range or damage [9].

**SAM site.** Requires 25 electricity, takes power in and passes the remainder through, uses SAM ammo, and has Has Target, Low Ammo and No Ammo outputs plus an Invert Mode input [10]. The SAM ammo page says the missile "contains a rudimentary guidance system" [11]. The community guide describes an attacker mode against unauthorised player-piloted air vehicles and a defender mode against MLRS rockets, and says about three sites are needed against a 12-rocket barrage [26]. September 2026 notes say the site is now much better at destroying hostile drones [2].

**Ground traps.** The snap trap is a metal trap that can injure or kill when stepped on and can be picked up after triggering [18]. The landmine can be disarmed by a friend if you stand on it [19]. Wooden floor spikes slow and hurt anyone walking over them [20]. None of the three pages lists a damage value [18][19][20].

**Barricades.** The wooden barricade hurts players and animals that run into it [13]. The barbed wooden barricade and the metal barricade both damage and slow players [15][16]. The stone and sandbag barricades are described as protective barricades [14][17]. The Livestock Update overhauled sandbags into a stackable deployable with a lower crafting cost, and sandbag barricades found in loot now come as a stack of 4 [1]. No page lists barricade health [13][14][15][16][17].

**Alarms.** The tin can alarm clatters loudly when disturbed [21]; in May 2026 it became riggable with explosives and similar items [5]. The smart alarm sends a phone notification when powered, draws 1 rW and passes power through [22]; since October 2026 it can be placed on top of other deployables [1].

**Locks.** The code lock is "an electronic lock" opened by a four-digit code [23]. The key lock is placed on a door and a key can be crafted for friends [24]. Players authorised on a code lock, including guest-code access, count toward the group upkeep tax for the base [2].

# Reference Data

Recipes were read from the Facepunch wiki on 2026-10-08, against the Livestock Update [1]. Wiki item pages are undated ("Updated: This Year" at best), so treat as volatile. "Not stated" means the page opened for this document does not give the value.

| Item | Recipe | Workbench | Power | Ammo or fuel | Source |
|------|--------|-----------|-------|--------------|--------|
| Auto Turret | 10 HQM, 1 CCTV camera, 1 targeting computer | Level 2 | 10 rW | projectile weapon plus matching ammo | [7] |
| Shotgun Trap | 500 wood, 250 metal fragments, 2 gears, 2 rope | Level 1 | not stated | handmade shells | [8] |
| Flame Turret | 200 metal fragments, 2 empty propane tanks, 1 gears | Level 1 | not stated | low grade fuel | [9] |
| SAM Site | not craftable per wiki | none | 25 rW | SAM ammo | [10] |
| Snap Trap | 50 metal fragments, 1 gears | Level 1 | not stated | none | [18] |
| Landmine | 50 metal fragments, 30 gun powder | Level 2 | not stated | none | [19] |
| Wooden Floor Spikes | 150 wood | none | not stated | none | [20] |
| Wooden Barricade | 300 wood, 1 rope | none | not stated | none | [13] |
| Stone Barricade | 100 stones | none | not stated | none | [14] |
| Barbed Wooden Barricade | 300 wood, 50 metal fragments, 1 rope | Level 1 | not stated | none | [16] |
| Metal Barricade | 200 metal fragments, 2 metal blades | Level 2 | not stated | none | [15] |
| Sandbag Barricade | 100 stones, 10 cloth (page may predate the overhaul) | Level 1 | not stated | none | [17] |
| Tin Can Alarm | 100 wood, 30 metal fragments, 1 rope | Level 1 | not stated | none | [21] |
| Smart Alarm | 3 HQM, 1 tech trash | Level 2 | 1 rW | none | [22] |
| Code Lock | 100 metal fragments | none | not stated | none | [23] |
| Key Lock | 75 wood | none | not stated | none | [24] |

The sandbag page may predate the Livestock overhaul, which reduced the crafting cost without giving a new figure [1][17].

| Item | Recycler yield | Research Table cost | Source |
|------|----------------|---------------------|--------|
| Auto Turret | 6 HQM, 1 CCTV camera (60%), 1 targeting computer (60%) | 120 scrap | [7] |
| Shotgun Trap | 300 wood, 150 metal fragments, plus rope and gears | 60 scrap | [8] |
| Flame Turret | 120 metal fragments, 1 empty propane tank, 1 gears (60%) | 30 scrap | [9] |
| SAM Site | 30 HQM | not researchable | [10] |

| Ammo item | Facts | Source |
|-----------|-------|--------|
| Handmade Shell | 5 gun powder and 5 stones make 2; stack 64; 9 damage per pellet on the pump and double barrel shotguns | [12] |
| SAM Ammo | wiki page gives a description only | [11] |

| Value requested | Status |
|-----------------|--------|
| Range of auto turret, flame turret, SAM site, shotgun trap | not stated on any opened Facepunch page [7][8][9][10] |
| Health of turrets, traps and barricades | not stated [7][8][9][10][13][14][15] |
| Trap damage (snap trap, landmine, spikes) | not stated [18][19][20] |
| Auto turret ammo capacity | not stated; the community guide says it has changed across patches [26] |

# Version & Patch Notes

- **7 May 2026, Upgrade Hard, Raid Harder:** fixed a bug authorising a friend at a TC or turret with blocked visibility, fixed a too-bright flame turret deploy guide, made the Tin Can Alarm riggable [5].
- **4 June 2026, Built Different:** fixed auto turrets hitting a player's shield after it broke, and a turret not targeting a player mounted to a Chippy machine at some angles [4].
- **2 July 2026, Common Ground:** turrets with burst-fire guns use burst fire; Softcore says deployables can still be attacked while protected walls cannot [3].
- **6 August 2026, Power Trip:** fixed placing wooden and barbed wooden barricades; fixed the Rust+ camera not updating when controlling a turret [6].
- **3 September 2026, Breach and Clear:** SAM sites better at shooting down hostile drones; fixed auto turret part LODs; reduced homing launcher lock-on time [2].
- **1 October 2026, Livestock Update:** remotely controlled turrets can hit reactive targets; sandbag overhaul (stackable, cheaper to craft, stack of 4 in loot); smart alarms placeable on other deployables; option to change lock code on boat steering wheels [1].
- Volatile: auto turret behaviour changed in three of the last five monthly updates [2][3][4]; re-check recipes after each update.

# Common Pitfalls

- Assuming a TC covers every turret: one community guide says each auto turret must be authorised individually [26], while the wiki ties only flame and shotgun traps to TC privilege [25].
- Expecting the SAM site to be craftable: the wiki marks it not craftable and lists only repair and recycle data [10].
- Copying range, damage or health figures from videos: none of the opened Facepunch pages publish them [7][8][9][10].
- Forgetting that deployables can still be attacked when a Softcore raid-block protects walls [3].
- Assuming a recipe is current: wiki pages are undated and the sandbag recipe predates its overhaul [1][17].
- Counting guests as free on a code lock: guest-code holders add to the upkeep tax [2].

# Interactions & Related Systems

- Power and wiring for turrets and SAM sites: see rust-electricity-logic; the figures here are only the draw [7][10][22].
- Explosive costs against doors and walls, and Softcore raid windows: see rust-raiding-costs-defence [3].
- Authorisation, TC privilege and upkeep: see rust-building-raiding-foundation [2][25].
- Turret ammunition and weapon stats: see rust-weapons-ammo; handmade shell damage is listed on its wiki page [12].
- Air vehicles that SAM sites target: see rust-vehicles [26].
- Scientist and NPC turrets that appear in loot tables: see rust-wildlife-npcs.
- Server-side limits on deployables and entity counts: see rust-server-performance and rust-server-convars-reference.

# Assessed Guidance

## Guidance 1 — Treat turret and trap ranges and damage as unknown until tested on the live build

- **Guidance:** Do not plan a defence around range, damage or health numbers quoted from memory or videos; test placement and coverage on the current update.
- **Evidence basis:** None of the Facepunch item pages for the turret, traps, SAM site or barricades states those values [7][8][9][10][13], and turret behaviour was patched in three recent updates [2][3][4].
- **Confidence:** Medium. The absence is verified on the pages opened, but the values may exist in game data not checked.
- **So what:** Budget time for in-game testing after each monthly update.

## Guidance 2 — Verify authorisation on each turret separately

- **Guidance:** After placing auto turrets, check each one's authorisation list rather than assuming the TC covers it.
- **Evidence basis:** A community guide says turrets do not read the TC [26]; the wiki's TC authorisation text names only flame and shotgun traps [25]; a May 2026 fix concerned authorising a friend at a TC or turret [5].
- **Confidence:** Medium. The turret claim rests on one undated community guide.
- **So what:** A teammate missing from a turret list is a likely cause of friendly-fire incidents.

## Guidance 3 — Count power headroom before wiring turrets and a SAM site on one supply

- **Guidance:** Add the draws (10 rW per auto turret, 25 rW for a SAM site, 1 rW per smart alarm) before choosing a generator and battery setup.
- **Evidence basis:** The wiki lists those draws [7][10][22].
- **Confidence:** High. The figures are on Facepunch pages for the checked build; the wiring design itself is not covered here.
- **So what:** An under-supplied circuit leaves defences unpowered.

# Open Questions

- Range, health and damage for every item above were not found on a Facepunch source; in-game data or a dated devblog would resolve it.
- The wiki lists the SAM site as not craftable; how players obtain it in the current build was not verified.
- The shotgun trap and flame turret are described by one community guide as needing no power; the wiki pages do not show an electrical section, but this was not confirmed in game.
- Auto turret ammo capacity, targeting modes and the SAM site's attacker and defender modes rest on one community guide with no stated version [26].
- The new sandbag recipe after the Livestock overhaul was not obtained.
- Whether the wiki recipes for the shotgun trap and flame turret match the live build is unverified because the pages are undated.

# References

**Primary Sources** — Facepunch devblogs and wiki.

- [1] **Facepunch** — *Livestock Update*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [2] **Facepunch** — *Breach and Clear*. https://rust.facepunch.com/news/breach-and-clear. Accessed 2026-10-08.
- [3] **Facepunch** — *Common Ground*. https://rust.facepunch.com/news/common-ground. Accessed 2026-10-08.
- [4] **Facepunch** — *Built Different*. https://rust.facepunch.com/news/built-different. Accessed 2026-10-08.
- [5] **Facepunch** — *Upgrade hard, raid harder*. https://rust.facepunch.com/news/upgrade-hard-raid-harder. Accessed 2026-10-08.
- [6] **Facepunch** — *Power Trip*. https://rust.facepunch.com/news/power-trip. Accessed 2026-10-08.
- [7] **Facepunch Wiki** — *Auto Turret*. https://wiki.facepunch.com/rust/item/autoturret. Accessed 2026-10-08.
- [8] **Facepunch Wiki** — *Shotgun Trap*. https://wiki.facepunch.com/rust/item/guntrap. Accessed 2026-10-08.
- [9] **Facepunch Wiki** — *Flame Turret*. https://wiki.facepunch.com/rust/item/flameturret. Accessed 2026-10-08.
- [10] **Facepunch Wiki** — *SAM Site*. https://wiki.facepunch.com/rust/item/samsite. Accessed 2026-10-08.
- [11] **Facepunch Wiki** — *SAM Ammo*. https://wiki.facepunch.com/rust/item/ammo.rocket.sam. Accessed 2026-10-08.
- [12] **Facepunch Wiki** — *Handmade Shell*. https://wiki.facepunch.com/rust/item/ammo.handmade.shell. Accessed 2026-10-08.
- [13] **Facepunch Wiki** — *Wooden Barricade*. https://wiki.facepunch.com/rust/item/barricade.wood. Accessed 2026-10-08.
- [14] **Facepunch Wiki** — *Stone Barricade*. https://wiki.facepunch.com/rust/item/barricade.stone. Accessed 2026-10-08.
- [15] **Facepunch Wiki** — *Metal Barricade*. https://wiki.facepunch.com/rust/item/barricade.metal. Accessed 2026-10-08.
- [16] **Facepunch Wiki** — *Barbed Wooden Barricade*. https://wiki.facepunch.com/rust/item/barricade.woodwire. Accessed 2026-10-08.
- [17] **Facepunch Wiki** — *Sandbag Barricade*. https://wiki.facepunch.com/rust/item/barricade.sandbags. Accessed 2026-10-08.
- [18] **Facepunch Wiki** — *Snap Trap*. https://wiki.facepunch.com/rust/item/trap.bear. Accessed 2026-10-08.
- [19] **Facepunch Wiki** — *Landmine*. https://wiki.facepunch.com/rust/item/trap.landmine. Accessed 2026-10-08.
- [20] **Facepunch Wiki** — *Wooden Floor Spikes*. https://wiki.facepunch.com/rust/item/spikes.floor. Accessed 2026-10-08.
- [21] **Facepunch Wiki** — *Tin Can Alarm*. https://wiki.facepunch.com/rust/item/tincan.alarm. Accessed 2026-10-08.
- [22] **Facepunch Wiki** — *Smart Alarm*. https://wiki.facepunch.com/rust/item/smart.alarm. Accessed 2026-10-08.
- [23] **Facepunch Wiki** — *Code Lock*. https://wiki.facepunch.com/rust/item/lock.code. Accessed 2026-10-08.
- [24] **Facepunch Wiki** — *Key Lock*. https://wiki.facepunch.com/rust/item/lock.key. Accessed 2026-10-08.
- [25] **Facepunch Wiki** — *Tool Cupboard, decay and building privilege*. https://wiki.facepunch.com/rust/the_tool_cupboard. Accessed 2026-10-08.

**Community & Practitioner Evidence** — hosting-provider guides.

- [26] **XGamingServer** — *Rust Base Defense Guide: Auto Turrets, SAM Sites and Traps* (11 June 2026, no game version stated). https://xgamingserver.com/blog/rust-base-defense-turrets-traps/. Accessed 2026-10-08.

**Further Reading**

- None cited.

# Further Reading

- The Facepunch Wiki electrical and traps sidebars list further items, such as the HBHF sensor and other turrets, not covered here [7].

# Related Documents

- rust-building-raiding-foundation
- rust-raiding-costs-defence
- rust-electricity-logic
- rust-weapons-ammo
- rust-wildlife-npcs
- rust-vehicles

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
