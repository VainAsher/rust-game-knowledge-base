---
id: rust-game-mechanics-foundation
title: "Rust Game Mechanics: Foundation"
version: 1.0.0
status: frozen
confidence: Medium
category: Game Mechanics
topic: "Core survival loop"
market: "Global"
document_type: foundation
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-items-crafting-foundation, rust-building-raiding-foundation, rust-server-administration-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation]
tags: [survival, health, hunger, thirst, radiation, temperature, comfort, bleeding, respawn, wipe, monuments]
game_build_checked: "Livestock Update (1 October 2026)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-game-mechanics-foundation |
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

This document is an overview of the core survival loop in Rust (Facepunch Studios, PC): the vital statistics a character must manage (health, hunger, thirst), the environmental pressures (radiation, cold and heat), the helpers (comfort, healing items), the failure states (bleeding, wounded, death), respawn through sleeping bags, the effect of server wipes on progression, and a first look at monuments. Deeper treatment belongs in later deep-dive documents.

The most recent Facepunch update at the time of checking is the Livestock Update of 1 October 2026 [1][2], whose notes list no change to health, hunger, thirst, temperature or respawn mechanics [2]. Item-level numbers come from the Facepunch wiki [3][4][5][6][7][8][9]. Threshold values for hunger, thirst and wounded recovery come only from a community guide [13], so the document-level confidence is Medium: several thresholds have no primary source, and sources conflict on one value.

# Key Facts

- The latest Facepunch news post at the time of checking is the Livestock Update, dated Thursday 1 October 2026 [1][2].
- That update lists no changes to health, hunger, thirst, temperature or respawn mechanics [2].
- Water gives Hydration +30 over 5 seconds and Radiation -5 over 4 seconds on the wiki (checked against the 1 October 2026 build) [5].
- A Large Medkit removes 100 bleeding and, if carried in the toolbar, guarantees recovery from the wounded state [7].
- A Sleeping Bag sets a respawn point for you or an assigned player, with a long cooldown that the wiki does not quantify [4].
- Forced wipes land on the first Thursday of the month with Facepunch's monthly update, and blueprints are not automatically reset [14].
- Monuments are grouped by a community guide into tiers by keycard and radiation, and the Outpost and Bandit Camp are safe zones [15].

# Scope

Covered: the single-character survival loop on vanilla PC servers, as an overview: vital stats, radiation, temperature, comfort, bleeding and wounded, death and respawn, the effect of wipes on progression, the PvP/PvE loop and monuments at overview level. Not covered: building and raiding, crafting trees, server configuration, plugins and the patch history (see the sibling documents). Modded servers and console editions are excluded. Facts were checked against the Livestock Update (1 October 2026).

# Definitions

- **Wounded:** a state entered when a non-lethal hit takes health to zero; the player crawls and may recover or be revived [13].
- **Comfort:** a beneficial effect from being near comfort items [13].
- **Forced wipe:** the monthly wipe that accompanies Facepunch's update [14].
- **Monument:** a pre-generated map landmark with loot and NPCs [15].

# Core Mechanics

**Evidence layer.** Figures marked community-sourced come from a single guide dated 11 June 2026 that states no game build [13].

**Vital stats.** The Facepunch wiki lists consumables as changing hydration, calories and healing over time; for example Water gives Hydration +30 and Healing over time +5, each over 5 seconds [5], and a Can of Beans gives Calories +100, Healing over time +4 and Hydration +25 [8]. A community guide states that a character is dehydrated when hydration falls below about 25, causing slow health and movement-speed loss, and that empty hunger causes steady health loss [13].

**Radiation.** Radiation is picked up in certain areas such as monuments, and higher-tier radiation can still pass through a Hazmat Suit, which gives 50% radiation protection according to a community guide [13]. Anti-Radiation Pills lower radiation and can dehydrate you [6]. Water slightly lowers radiation [5]. A Geiger Counter is a tool item [9]. The Livestock Update fixed Oil Rig radiation starting before the locked crate is looted [2].

**Temperature.** The community guide gives only qualitative cues: nights are colder, snow biomes are harsh, and a wet character gets colder [13]. It gives no numeric temperature thresholds [13]. A Camp Fire "provides warmth and light, and you can cook with it" [10].

**Comfort and regeneration.** Per the community guide, a Campfire roughly doubles the health regeneration tick, a Campfire or running Furnace raises comfort to about 50%, and a chair or Bear Skin Rug can raise it to 100%. Comfort heals only while hunger and hydration are above their low thresholds [13].

**Bleeding, wounded, death.** The Bandage has Instant Health +5 and Bleeding -50 [11]. The Large Medkit removes 100 bleeding, gives +100 healing over time, and guarantees recovery from the wounded state when in the toolbar [7]. Per the guide, wounded recovery takes about 45 seconds before a roll, with a base chance of about 20% and about 45% with maxed food and hydration, and teammates can revive with a Large Medkit or Medical Syringe [13]. Fall damage never causes wounded [13].

**Respawn.** A Sleeping Bag is "a place to respawn, with a long cooldown", is craftable for 30 Cloth, and despawns as a dropped item after 20 minutes [4].

**Wipes and progression.** A forced wipe removes bases, loot and resources and generates a new procedural map; it does not automatically reset blueprints, and blueprint wipes are a server-by-server choice [14]. Facepunch's own wiki documents the scheduled wipe: default Thursday 19:00 London time, with monthly, biweekly or weekly tags [12].

**PvP/PvE loop and monuments (overview).** A community guide describes tiered monuments from Supermarket and Gas Station to Launch Site and Military Tunnels, a three-tier keycard ladder, and hostile NPC scientists and players competing for loot, with Outpost and Bandit Camp as safe zones [15].

# Reference Data

All rows were checked on 2026-10-08 against the Livestock Update unless stated.

| Item | Stated value | Source |
|------|--------------|--------|
| Water | Hydration +30 / 5 s; Healing +5 / 5 s; Radiation -5 / 4 s; Poison -3 / 3 s | [5] |
| Can of Beans | Calories +100; Healing +4; Hydration +25 | [8] |
| Anti-Radiation Pills | Hydration -5 / 5 s; Radiation -75 / 5 s | [6] |
| Bandage | Instant Health +5; Bleeding -50; Poison -2 | [11] |
| Large Medkit | Instant Health +10; Healing +100; Bleeding -100; Poison -10 | [7] |
| Sleeping Bag | 30 Cloth; despawn 20 min; long respawn cooldown (no number) | [4] |
| Camp Fire | 100 Wood; despawn 5 min | [10] |
| Dehydration threshold | below about 25 hydration (community, 11 Jun 2026) | [13] |
| Wounded | about 45 s, about 20% base, about 45% maxed (community, 11 Jun 2026) | [13] |
| Default wipe time | Thursday 19:00 London | [12] |

# Version & Patch Notes

- Livestock Update, 1 October 2026: no listed change to the core vitals; Oil Rig radiation fix; milk and cream extend and strengthen teas [2].
- Recent update names and dates from Facepunch: Breach and Clear (3 Sep 2026), Power Trip (6 Aug 2026), Common Ground (2 Jul 2026), Built Different (4 Jun 2026) [1].
- Volatile: all item values above, and monument tiers, which change in monthly updates [13][15].

# Common Pitfalls

- Anti-Radiation Pills dehydrate you. The Facepunch wiki gives Hydration -5 [6], whereas a community guide says -50 [13]; this conflict is unresolved.
- Assuming a forced wipe also resets blueprints; it does not automatically [14].
- Treating community monument tier tables as official; they are guide-authored [15].

# Interactions & Related Systems

Cooking and food, medical crafting and workbench trees: see rust-items-crafting-foundation. Bases, which hold sleeping bags and campfires: rust-building-raiding-foundation. Wipe configuration convars: rust-server-administration-foundation [12]. Plugins that alter metabolism: rust-modding-plugins-foundation. Update cadence: rust-updates-meta-foundation [1].

# Assessed Guidance

## Guidance 1 — Treat community threshold numbers as provisional and verify in game

- **Guidance:** Use the community thresholds (hydration about 25, wounded odds) as rough planning values only.
- **Evidence basis:** The thresholds come from a single guide with no stated build [13], and the pill hydration value conflicts with the Facepunch wiki [6].
- **Confidence:** Medium. Documented item values are primary, but thresholds are single-source.
- **So what:** Check the in-game HUD and the current wiki before building a strategy on exact figures.

## Guidance 2 — Carry healing for both bleeding and the wounded state

- **Guidance:** Keep a Bandage for routine bleeding and a Large Medkit for the highest-risk fights.
- **Evidence basis:** The Bandage removes 50 bleeding [11]; the Large Medkit removes 100 bleeding and guarantees wounded recovery from the toolbar [7].
- **Confidence:** Medium. Item effects are wiki facts, while the tactical recommendation is judgement.
- **So what:** Fewer deaths in sustained fights, at the price of scarce Medkit materials.

## Guidance 3 — Plan progression around the wipe, and check the server's blueprint policy

- **Guidance:** Expect base and map loss monthly, and read each server's blueprint wipe rule before investing in research.
- **Evidence basis:** Forced wipes follow the monthly update and blueprints are not automatically reset [14][12].
- **Confidence:** Medium. The blueprint policy is described by a commercial guide, not by Facepunch.
- **So what:** Time big projects early in a wipe cycle.

# Open Questions

- Exact numeric temperature thresholds for cold and heat: not found on a source opened for this document; resolve from in-game data or an official Facepunch page.
- The numeric respawn cooldown of the Sleeping Bag.
- Which Anti-Radiation Pills hydration value is right (-5 [6] or -50 [13]).
- Facepunch's own statement on blueprint wipes at forced wipes.

# References

Numbered contiguously from [1].

**Primary Sources**

- [1] **Facepunch** — *Rust news*. https://rust.facepunch.com/news. Accessed 2026-10-08.
- [2] **Facepunch** — *Livestock Update*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [3] **Facepunch Rust Wiki** — *Rust Wiki home*. https://wiki.facepunch.com/rust/. Accessed 2026-10-08.
- [4] **Facepunch Rust Wiki** — *Sleeping Bag*. https://wiki.facepunch.com/rust/item/sleepingbag. Accessed 2026-10-08.
- [5] **Facepunch Rust Wiki** — *Water*. https://wiki.facepunch.com/rust/item/water. Accessed 2026-10-08.
- [6] **Facepunch Rust Wiki** — *Anti-Radiation Pills*. https://wiki.facepunch.com/rust/item/antiradpills. Accessed 2026-10-08.
- [7] **Facepunch Rust Wiki** — *Large Medkit*. https://wiki.facepunch.com/rust/item/largemedkit. Accessed 2026-10-08.
- [8] **Facepunch Rust Wiki** — *Can of Beans*. https://wiki.facepunch.com/rust/item/can.beans. Accessed 2026-10-08.
- [9] **Facepunch Rust Wiki** — *Geiger Counter*. https://wiki.facepunch.com/rust/item/geiger.counter. Accessed 2026-10-08.
- [10] **Facepunch Rust Wiki** — *Camp Fire*. https://wiki.facepunch.com/rust/item/campfire. Accessed 2026-10-08.
- [11] **Facepunch Rust Wiki** — *Bandage*. https://wiki.facepunch.com/rust/item/bandage. Accessed 2026-10-08.
- [12] **Facepunch Rust Wiki** — *Server Wipe Timer*. https://wiki.facepunch.com/rust/server-wipe-timer. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- [13] **XGamingServer** — *Rust Survival Guide: Radiation, Temperature, Comfort and Hydration* (11 June 2026). https://xgamingserver.com/blog/rust-radiation-temperature-survival-guide/. Accessed 2026-10-08.
- [14] **XGamingServer** — *When Is the Next Rust Wipe?* (4 June 2026). https://xgamingserver.com/blog/when-is-the-next-rust-wipe/. Accessed 2026-10-08.
- [15] **XGamingServer** — *Rust Monuments Guide: Loot, Puzzles, Keycards & Fuses* (4 June 2026). https://xgamingserver.com/blog/rust-monuments-guide-loot-puzzles-keycards/. Accessed 2026-10-08.

**Further Reading**

None.

# Further Reading

The Facepunch Rust Wiki item pages for teas, Hazmat Suit and Medical Syringe.

# Related Documents

- rust-items-crafting-foundation
- rust-building-raiding-foundation
- rust-server-administration-foundation
- rust-modding-plugins-foundation
- rust-updates-meta-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, 100% links live). | Auto-approve mandate |
