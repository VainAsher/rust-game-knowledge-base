---
id: rust-wildlife-npcs
title: "Rust Wildlife and NPCs"
version: 0.1.0
status: in-review
confidence: Low
category: Game Mechanics
topic: "Wildlife and NPCs"
market: "Global"
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-game-mechanics-foundation, rust-monuments-loot, rust-combat-damage-model, rust-weapons-ammo, rust-farming-food, rust-vehicles, rust-electricity-logic, rust-turrets-deployables, rust-server-performance, rust-game-modes]
tags: [animals, wildlife, npc, scientists, bradley, patrol-helicopter, livestock]
game_build_checked: "Livestock Update (1 October 2026)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-wildlife-npcs |
| Version | 0.1.0 |
| Status | in-review |
| Confidence | Low |
| Category | Game Mechanics |
| Region | Global |
| Game build checked | Livestock Update (1 October 2026) |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This deep-dive covers the non-player creatures of Rust: wild animals, the scientist and guard NPCs, the Bradley APC and Patrol Helicopter events, and the livestock introduced by the Livestock Update of 1 October 2026. It goes deeper than rust-game-mechanics-foundation, which only mentions hostile scientists at monuments.

Facepunch's Livestock post is the only primary source for the current build and it covers livestock, critters and NPC navigation, not health values or drop tables [1]. Health figures come from one community bestiary [4] and one hosting-company guide [5], neither tied to a stated build. Document confidence is therefore Low.

# Key Facts

- The Livestock Update (1 October 2026) adds cows and sheep that produce dung, milk and wool, can be bred, and can be sold to a Stable vendor [1].
- With the new navmesh enabled, NPCs can enter player structures and respect doors opening and closing [1].
- Only a subset of NPCs is processed each frame, so overload makes NPCs react slower rather than costing server FPS [1].
- The wiki Bradley Crate has 7 slots and always contains 1-4 MLRS Rockets (100%) [2].
- A community bestiary lists Bradley at 1000 health and scientists between 115 and 300 health depending on type (not build-stamped) [4].
- Wolves gather in groups of up to 3 and deer in packs of up to 5, per a June 2021 report [6].
- Community sources disagree slightly on Patrol Helicopter health (see Reference Data) [4][5].

# Scope

Covered: wild animals, critters, livestock, scientist and guard NPCs, Bradley APC and Patrol Helicopter. Health and drops appear only where a source gives them. Not covered: monument loot (see rust-monuments-loot), weapon damage (rust-combat-damage-model), farming and cooking (rust-farming-food), turrets (rust-turrets-deployables). Vanilla PC servers only.

# Definitions

- **Livestock:** domesticated cows and sheep that can be bred and sold [1].
- **Critter:** decorative wildlife such as frogs and rabbits, heavily budgeted [1].
- **Scientist:** a hostile armed NPC found at monuments and roadsides [4].
- **Bradley APC:** a tracked armoured vehicle NPC patrolling Launch Site [5].
- **Patrol Helicopter:** a roaming helicopter event [5].

# Core Mechanics

**Livestock.** Cows and sheep both produce dung; cows produce milk and sheep wool; both yield meat, bones and leather when harvested [1]. They have genetics and needs and can be bred, though Facepunch says genes do not behave exactly like plant genes [1]. Grown animals can be sold to a Stable vendor; offers vary with gene quality, you can reject an offer twice more, after which the vendor refuses that animal for 15 minutes [1]. Wool is traded in with three offers, to a maximum of 400 wool per trade-in [1]. Milk refrigerated for 4 hours can be skimmed into Skimmed Milk and Cream [1]. New animal gate and fence deployables contain livestock [1].

**Critters.** Frogs, rabbits, squirrels, sea turtles, crabs and jellyfish appear in suitable biomes and are mostly set dressing under a tight budget [1].

**Wild animals.** A community bestiary describes bears, boars, wolves and stags as melee animals, chickens as passive, and sharks as ocean attackers that strike, retreat and circle [4]. Since the June 2021 AI overhaul all AI runs under one system, with wolves gathering in groups of up to 3 and deer in packs of up to 5 [6]. Pigs yield Raw Pork, 8 Flesh per pig on the wiki [3].

**Scientists and guards.** The bestiary lists scientists by location: Oil Rig heavy scientists with M249, Minigun, Spas-12 or Flamethrower, Outpost peacekeepers, and roadside and junkpile scientists with an M92 [4]. Keycard drops are covered in rust-monuments-loot.

**Navigation and performance.** NPCs use a new navmesh that lets them enter structures and respect doors [1]. Only a subset is processed per frame under a hardcoded time cap, and navigation performance was at least doubled since the previous patch [1].

**Bradley APC.** It patrols the paved roads of Launch Site, its only spawn, and is described as damaged only by explosives; it fires a machine gun and cannon at detected players and repairs itself if left alone for minutes [5]. Its kill drops 3 APC crates [5], and the wiki defines the Bradley Crate as a 7-slot container [2].

**Patrol Helicopter.** A roaming event roughly every 2 to 4 hours depending on server configuration; it attacks with machine-gun strafing and rockets, and downing both rotors destroys it [5]. Its crash site holds about 3 to 4 locked crates [5].

# Reference Data

Health values are community-sourced and not tied to a build; the Livestock Update (1 Oct 2026) published none [1].

| NPC / animal | Health | Notes | Source |
|--------------|--------|-------|--------|
| Chicken | 25 | passive | [4] |
| Boar, Wolf, Stag, Shark | 150 | melee | [4] |
| Brown Bear | 325 | melee | [4] |
| Polar Bear | 420 | Arctic | [4] |
| Roadside / junkpile scientist | 115 | M92 | [4] |
| Tunnel / Underwater Dweller | 125 | listed values | [4] |
| Most monument scientists, Peacekeeper | 150 | LR-300, MP5A4 | [4] |
| Military Tunnel scientist | 175 | LR-300, MP5A4, Spas-12 | [4] |
| Bandit Camp guard | 250 | semi-auto and assault rifle | [4] |
| Heavy and NVGM scientists | 300 | Oil Rig, Missile Silo | [4] |
| Bradley APC | 1000 | explosives only | [4][5] |
| Patrol Helicopter | 9895.6 [4], about 10,000 [5] | rotors about 900 and 500 [5] | [4][5] |

Bradley Crate (wiki, 7 slots, checked 2026-10-08) [2]:

| Item | Amount | Chance |
|------|--------|--------|
| MLRS Rocket | 1-4 | 100% [2] |
| Targeting Computer | 1 | 52.4% [2] |
| 8x Zoom Scope, Burst Module, Extended Magazine, Weapon Lasersight | 1 each | 50% [2] |
| High Velocity Rocket | 3-6 | 17.5% [2] |
| Auto Turret | 1 | 4.8% [2] |

Livestock trade values: two further rejects then a 15 minute refusal; wool maximum 400 per trade-in; milk skimming after 4 hours refrigerated (Livestock Update) [1].

# Version & Patch Notes

- Livestock Update, 1 October 2026: cows and sheep, breeding, Stable vendor sales, fences and gates, NPC navmesh into structures, NPC per-frame budget, critters [1].
- June 2021: new bear, boar, stag and wolf models, unified AI, wolf and deer pack behaviour [6].
- Volatile: every health value in this document, and Bradley and heli respawn timers [4][5].

# Common Pitfalls

- Treating bestiary health as current; the page was last updated 22 Feb 2026 and states no build [4].
- Assuming guide spawn timers are fixed; the guide says helicopter frequency depends on server configuration [5].
- Expecting Bradley to take bullet damage; the guide says only explosives hurt it [5].
- Reading an old Bradley Crate figure; use the current wiki table [2].

# Interactions & Related Systems

Scientists drop keycards and fuses: rust-monuments-loot. Damage and armour: rust-combat-damage-model, rust-weapons-ammo. Meat, milk and cooking: rust-farming-food [3]. Bradley crates may contain Auto Turrets: rust-turrets-deployables [2]. NPC processing budget: rust-server-performance [1]. Horses and vehicles: rust-vehicles. Parent: rust-game-mechanics-foundation.

# Assessed Guidance

## Guidance 1 — Bring explosives, not bullets, for Bradley

- **Guidance:** Plan Bradley attempts around explosive ammunition and spare rockets.
- **Evidence basis:** The guide says only explosives damage Bradley and cites 4 to 7 High Velocity Rockets [5].
- **Confidence:** Low. Single non-Facepunch source with no build.
- **So what:** Test on your server before committing resources.

## Guidance 2 — Do not quote bestiary health as current

- **Guidance:** Treat all health numbers as approximate until read from the game.
- **Evidence basis:** Two community sources differ on heli health and neither states a build [4][5].
- **Confidence:** Medium. The disagreement itself is documented.
- **So what:** Admins and players should verify in game.

## Guidance 3 — Fence livestock and mind the vendor cooldown

- **Guidance:** Contain animals with the new gates and fences, and avoid rejecting offers repeatedly.
- **Evidence basis:** Facepunch documents fences and the 15 minute refusal after rejected offers [1].
- **Confidence:** Medium. Facts are primary, tactics are judgement.
- **So what:** Avoids losing a bred animal's sale window.

# Open Questions

- Current-build health for animals, scientists, Bradley and heli: no Facepunch source found.
- Animal drop tables: not found.
- Patrol Helicopter crate contents and targeting rules from an official source.
- Whether the livestock navmesh change alters scientist behaviour at monuments.
- Bradley respawn timer on the current build.

# References

**Primary Sources**

- [1] **Facepunch** — *Livestock Update*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [2] **Facepunch Rust Wiki** — *Bradley Crate*. https://wiki.facepunch.com/rust/bradley-crate. Accessed 2026-10-08.
- [3] **Facepunch Rust Wiki** — *Raw Pork*. https://wiki.facepunch.com/rust/item/meat.boar. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- [4] **Corrosion Hour** — *The RUST Bestiary, a Compendium* (14 June 2023, updated 22 Feb 2026). https://www.corrosionhour.com/rust-bestiary/. Accessed 2026-10-08.
- [5] **XGamingServer** — *Rust Bradley APC & Patrol Helicopter Guide* (11 June 2026). https://xgamingserver.com/blog/rust-bradley-patrol-helicopter-guide/. Accessed 2026-10-08.
- [6] **Rustafied** — *the contacts update* (3 June 2021). https://www.rustafied.com/updates/2021/6/3/the-contacts-update. Accessed 2026-10-08.

**Further Reading**

None.

# Further Reading

Facepunch wiki loot pages for scientist variants.

# Related Documents

- rust-game-mechanics-foundation
- rust-monuments-loot
- rust-combat-damage-model
- rust-farming-food
- rust-turrets-deployables

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
