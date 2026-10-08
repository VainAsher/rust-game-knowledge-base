---
id: rust-fishing
title: "Rust Fishing"
version: 1.0.0
status: frozen
confidence: Medium
category: Game Mechanics
topic: "Fishing"
market: "Global"
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-game-mechanics-foundation, rust-farming-food, rust-vehicles, rust-monuments-loot, rust-wildlife-npcs, rust-server-convars-reference, rust-update-timeline-2026]
tags: [fishing, fishing-rod, bait, overfishing, fishing-village, fish]
game_build_checked: "Livestock update, 1 Oct 2026 (wiki pages read 2026-10-08)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-fishing |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Game Mechanics |
| Region | Global |
| Game build checked | Livestock update, 1 Oct 2026 |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This document covers Rust fishing: the Handmade Fishing Rod, bait, the casting and reeling minigame, the fish that exist, what a catch is used for, the April 2026 overfishing rule, and the role of fishing villages as buyers of catches. It goes deeper than the mechanics foundation and does not restate it.

Rod, bait and minigame controls are well sourced from the Facepunch devblog that introduced fishing in August 2021 [1] and the Facepunch wiki [3][4]. Numeric values (bait values, catch odds, scrap prices, gutting yields, overfishing timers) are not published on any page opened, so they are absent rather than guessed. The document is rated Medium: primary sources agree on the mechanics, but the numbers a player would want are missing and the 2021 devblog predates later rebalances.

# Key Facts

- Fishing was introduced in the 5 August 2021 Going Deep update; the devblog describes the Handmade Fishing Rod as "fully functional and ready for use" [1].
- The Handmade Fishing Rod costs 200 Wood and 2 Rope, needs no workbench, takes 10 s to craft without one, and "requires bait" [4].
- Bait goes in the rod's lure slot; foods can be bait, and worms and grubs can drop when harvesting berries, hemp and potatoes, with double the chance on player-planted crops [1].
- Catch requirements depend on bait value, water type, water depth and location [1].
- Spring Clean (2 April 2026) added overfishing: a heavily fished area returns only junk until it repopulates, and fish traps are not affected [2].
- Since Spring Clean, Herring and Anchovy can no longer be caught in the deep sea [2].
- Catches can be eaten, gutted for resources, or sold for scrap at a fishing village [1][3].
- The Livestock update (1 Oct 2026) contains no fishing change on the page opened [11].

# Scope

Covers vanilla PC Rust fishing as documented up to the Livestock update (1 Oct 2026). Plugin-driven fishing changes and Underwater Labs fishing detail beyond one wiki mention are excluded. Boat and submarine mechanics belong to rust-vehicles. Cooking and hunger values belong to rust-farming-food.

# Definitions

- **Lure slot:** the rod slot in which bait is equipped [1].
- **Bait value:** a per-food number shown in item info that affects what can be caught [1]. Individual values were not found.
- **Overfished:** an area in which too many fish were caught within a time window, so casts return only junk [2].
- **Fish trap:** a passive fishing deployable that overfishing does not affect [2].

# Core Mechanics

**Evidence layer.**

**Rod.** The wiki names the Handmade Fishing Rod as the fishing rod. It can be obtained from missions, fishing villages, large fishing villages or crafting [3]. Use attack2 to cast and wait for a bite [4].

**Bait.** The devblog says a bait must be equipped in the rod's lure slot, foods can serve as bait, and each food's bait value is in its item info [1]. The wiki says bait comes from foraging, hunting animals and food crates [3]. Worms and grubs can drop while harvesting resources such as berries, hemp and potatoes, and plants the player planted give double the chance [1]. The Worm item is described as usable as bait [10].

**Casting and reeling.** Hold right mouse while aiming at water, then left-click to cast [1][3]. After a wait a fish bites and a minigame starts [3]. A and D pull the fish left or right and S reels it in; pulling it side to side tires it so it moves less [1]. Reeling and pulling strain the line, and if strained too much the line snaps and the fish escapes; the rod shakes and plays audio cues under strain [1]. Players are told to pause reeling when tension is high and keep the fish centred [3].

**Where fish come from.** The wiki lists fishing areas as Swamp, River, Ocean and the Underwater Lab moon pool [3]. The devblog says catches depend on bait value, water type, depth and location [1].

**Fish.** The devblog lists eight fish: Herring, Anchovy, Sardines, Yellow Perch, Catfish, Small Sharks, Salmon and Orange Roughy [1]. The wiki sidebar additionally lists Minnows and Small Trout [3].

**Uses.** A catch can be eaten, sold for scrap, or gutted for loot, and selling requires a fishing village [3]. The devblog says gutting yields resources and that catches can be taken to any fishing village for scrap [1]. Salmon, Catfish and Orange Roughy descriptions say their stomachs can hold random items [6][7][9].

**Overfishing.** Fish caught in an area within a set time window can make it overfished; casts there return only junk until the area repopulates after a refresh period [2]. Facepunch states that many ConVars let servers adjust or disable the feature, that it targets AFK fish farming in bases, and that fish traps are unaffected [2].

**Fishing villages.** The 2021 devblog says villages sell boats, submarines and torpedoes and that village spawning was improved [1]. Fishing villages are also a source of the rod [3].

# Reference Data

**Evidence layer.** Values read from the Facepunch wiki 2026-10-08 (Livestock build) unless noted.

| Item | Data | Source |
|------|------|--------|
| Handmade Fishing Rod | 200 Wood + 2 Rope; no workbench; craft 10 s (none), 5 s (Workbench 1), 2 s (Workbench 2 and 3); stack 1; research cost 120 Scrap | [4] |
| Handmade Fishing Rod, repair | 12 Cloth + 40 Wood, 20% condition loss | [4] |
| Handmade Fishing Rod, recycler | 120 Wood, 1 Rope (100%), 1 Rope (20%); Safe Zone Recycler 80 Wood, 1 Rope (80%) | [4] |
| Fishing Tackle | stack 1; not craftable, repairable, recyclable or researchable; found in a Tacklebox, 1 per drop, 100% | [5] |
| Salmon | stack 10; fresh and salt water; despawn 5 min | [6] |
| Catfish | stack 5; freshwater predator | [7] |
| Sardine | stack 10 | [8] |
| Orange Roughy | stack 5; described as rare, ocean depths | [9] |
| Worm | stack 25; usable as bait | [10] |
| Fishing water types | Swamp, River, Ocean, Underwater Lab moon pool | [3] |

Not found on any opened page: bait values, catch odds per fish, fish scrap prices, gutting yields, rod durability, overfishing window and refresh durations, and the overfishing ConVar names.

# Version & Patch Notes

**Evidence layer.**

- 5 Aug 2021, Going Deep: fishing, eight fish, worms and grubs, bait and lure slot, fishing-village catch trading, submarines and torpedoes [1].
- 2 Apr 2026, Spring Clean (April Quickfire): overfishing added; Herring and Anchovy removed from deep-sea catches; deep-sea loot pool favours higher-value catches [2].
- 1 Oct 2026, Livestock: no fishing change on the page opened [11].
- Volatile: everything numeric, and which fish appear where, since Spring Clean already changed the pool [2].

# Common Pitfalls

- Expecting to fish in a base: Facepunch says fishing inside your base or botting the minigame is against the spirit of the activity, and overfishing targets it [2].
- Casting without bait: the rod requires bait [4].
- Holding reel under tension: the line snaps and the fish escapes [1].
- Old guides listing Herring or Anchovy as deep-sea catches are outdated since 2 Apr 2026 [2].
- Guides based on the 2021 devblog list eight fish; the wiki sidebar now shows ten names [1][3].

# Interactions & Related Systems

- Food and cooking: caught fish are food; cooking times are in rust-farming-food [3].
- Planted crops: player-planted plants double the chance of worm and grub drops [1]. See rust-farming-food.
- Boats and submarines are sold at fishing villages [1]. See rust-vehicles.
- Fishing villages are safe-zone monuments. See rust-monuments-loot.
- Server administration: overfishing is exposed through ConVars [2]. See rust-server-convars-reference.
- Update history: see rust-update-timeline-2026 and rust-game-mechanics-foundation.

# Assessed Guidance

## Guidance 1 — Fish away from your base and rotate spots

- **Guidance:** Fish at natural waters and move on once casts start returning junk, rather than farming one spot.
- **Evidence basis:** Overfishing makes heavily fished areas return only junk until they repopulate [2]; fishing in bases is called out as unintended [2].
- **Confidence:** Medium. The mechanic is primary-sourced, but window and refresh durations are unpublished.
- **So what:** Expect diminishing returns at one spot; do not build a fishing setup around AFK casting.

## Guidance 2 — Stock worms by harvesting your own crops

- **Guidance:** Keep a stack of worms by harvesting planted berries, hemp or potatoes.
- **Evidence basis:** Worms and grubs drop from harvesting, with double chance on planted crops [1]; worms are bait [10].
- **Confidence:** Medium. Drop rates and bait values are not published.
- **So what:** A small planter doubles as a bait source, though whether worms are the best bait is unverified.

## Guidance 3 — Treat fish-for-scrap as an unverified income route

- **Guidance:** Do not plan a scrap economy around fish until prices are checked in game.
- **Evidence basis:** Villages buy catches for scrap [1][3], but no rate was found in any opened source.
- **Confidence:** Low. The existence of the trade is sourced; the value is not.
- **So what:** Test one sale at a village before committing time.

# Open Questions

- Bait value of each food and of worms and grubs: not on opened wiki pages; read item info in game.
- Per-fish catch conditions (water, depth, bait threshold), and when Minnows and Small Trout were added.
- Scrap price per fish and gutting yields.
- Overfishing window, refresh time and the ConVar names; run `find fish` or `find overfish` on a server.
- Rod durability and Fishing Tackle function: the wiki entry is a stub [5].
- Fish trap details: the wiki fish trap URL tried returned 404, so none are documented beyond the devblog mention [2].

# References

**Primary Sources**

- [1] **Facepunch** — *Going Deep (5 Aug 2021 devblog)*. https://rust.facepunch.com/news/going-deep. Accessed 2026-10-08.
- [2] **Facepunch** — *Spring Clean (2 Apr 2026), Overfishing and Fishing in the Deep Sea*. https://rust.facepunch.com/news/spring-clean. Accessed 2026-10-08.
- [3] **Facepunch Rust Wiki** — *Fishing*. https://wiki.facepunch.com/rust/Fishing. Accessed 2026-10-08.
- [4] **Facepunch Rust Wiki** — *Handmade Fishing Rod*. https://wiki.facepunch.com/rust/item/fishingrod.handmade. Accessed 2026-10-08.
- [5] **Facepunch Rust Wiki** — *Fishing Tackle*. https://wiki.facepunch.com/rust/item/fishing.tackle. Accessed 2026-10-08.
- [6] **Facepunch Rust Wiki** — *Salmon*. https://wiki.facepunch.com/rust/item/fish.salmon. Accessed 2026-10-08.
- [7] **Facepunch Rust Wiki** — *Catfish*. https://wiki.facepunch.com/rust/item/fish.catfish. Accessed 2026-10-08.
- [8] **Facepunch Rust Wiki** — *Sardine*. https://wiki.facepunch.com/rust/item/fish.sardine. Accessed 2026-10-08.
- [9] **Facepunch Rust Wiki** — *Orange Roughy*. https://wiki.facepunch.com/rust/item/fish.orangeroughy. Accessed 2026-10-08.
- [10] **Facepunch Rust Wiki** — *Worm*. https://wiki.facepunch.com/rust/item/worm. Accessed 2026-10-08.
- [11] **Facepunch** — *Livestock (1 Oct 2026)*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.

**Community & Practitioner Evidence**

None used.

**Further Reading**

None.

# Further Reading

- Facepunch Rust Wiki item pages for the other fish (Herring, Anchovy, Yellow Perch, Small Shark).

# Related Documents

- rust-game-mechanics-foundation
- rust-farming-food
- rust-vehicles
- rust-monuments-loot
- rust-wildlife-npcs
- rust-server-convars-reference
- rust-update-timeline-2026

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
