---
id: rust-economy-trading
title: "Rust Economy and Trading"
version: 1.0.0
status: frozen
confidence: Medium
category: Items & Crafting
topic: "Economy, scrap and trading"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-items-crafting-foundation, rust-monuments-loot, rust-turrets-deployables, rust-vehicles, rust-farming-food, rust-server-convars-reference, rust-update-timeline-2026, rust-game-modes, rust-raiding-costs-defence, rust-electricity-logic]
tags: [economy, scrap, vending-machine, recycler, marketplace, shops, trading, safe-zone]
game_build_checked: "Livestock Update, 1 October 2026 (wiki pages undated)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-economy-trading |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Items & Crafting |
| Region | Global |
| Game build checked | Livestock Update, 1 October 2026 [1]; Rust Wiki pages carry no build stamp |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

Rust has no formal currency. Scrap is described by the wiki as "often used as a currency", and it is also the research and workbench input [9]. Trade happens through four systems: player-run vending machines, NPC vendors that pay or charge scrap at safe-zone monuments, a drone marketplace that delivers from vending machines for a scrap fee, and, since July 2026, rentable shops at the Apartment Complex [3][5][12]. Recyclers convert items back into raw materials and so set the floor price of components [10][11].

The design intent and mechanics come from Facepunch devblogs, but most numbers (recycler efficiency, scrap drop tables, vending cost) come from undated wiki pages, and NPC buy and sell price tables could not be sourced at all. Confidence is Medium: Facepunch sources cover the systems, while current values rest on wiki pages that one Facepunch post already contradicts [2][10].

# Key Facts

- Scrap stacks to 1,000, despawns after 20 minutes on the ground, and cannot be crafted, repaired, recycled or researched [9].
- The drone marketplace at Bandit Camp and Outpost charges a 20 scrap delivery fee per trade (Softcore update, 4 February 2021); delivery can take up to five minutes [5].
- Items sold to NPC vending machines for scrap use dynamic pricing: each item starts the wipe at 50% less value and can rise by an extra 100% if none are sold (5 December 2024) [4].
- Rentable shops (Common Ground, 2 July 2026) need at least 12 hours of rent to open, can be taken over after 6 hours at 2x cost, and drones cannot reach them [3].
- A Vending Machine crafts from 20 High Quality Metal and 3 Gears at Workbench Level 1 per the wiki [8], matching the cost cut in Devblog 180 [7].
- Green recycler efficiency fell to a 50% baseline in Power Trip (6 August 2026); the wiki Recycler page still says 60%, so it is stale on that point [2][10].
- The Safe Zone Recycler is listed at 40% yield and 8 seconds per item [11].
- The Livestock Update (1 October 2026) added a Stable vendor that buys animals and wool and a "vendor bartering mechanic" that the post does not explain [1].

# Scope

Covers vanilla PC Rust: scrap sources and sinks, player vending machines, NPC vendors, the drone marketplace, rentable shops, and recyclers (including safe-zone recyclers). Excludes console, modded shops and economy plugins (see rust-modding-plugins-foundation), Rust+ app features, the Facepunch Steam item store, and detailed per-item NPC prices, which were not available from a citable source. Checked against the Livestock Update of 1 October 2026 [1].

# Definitions

- **Scrap** — dropped currency-like item used for research, workbench use, and trading [9].
- **Vending machine** — a player-deployed shop where the owner sets sell orders and buyers pay from their inventory [8][13].
- **NPC vendor** — an NPC vending machine at a safe-zone monument that trades goods for scrap [4][12].
- **Marketplace** — drone-delivery terminals at Bandit Camp and Outpost [5].
- **Rentable shop** — a rented stall at the Apartment Complex [3].
- **Recycler** — a station that breaks items into component materials at a stated efficiency [2][10].
- **Safe zone** — a monument area covered by turrets where hostile acts are punished; see rust-monuments-loot [12].

# Core Mechanics

**Evidence layer.**

**Scrap as currency and input.** The wiki describes scrap as used at Research Tables and Workbenches and "often used as a currency" [9]. It is not craftable and comes from loot: barrels give 2, Basic Crates 3, Military Crates 8, Elite Crates 25, Airdrops 140-160 at 55.6%, and scientists 8-24 at 36.3% [9]. It is also an ingredient for items including Gears (100) and Research Table (20) [9]. Helicopter shredding at the Junkyard pays scrap by type and health: 200 for a Minicopter, 300 for a Scrap Transport Helicopter and 500 for an Attack Helicopter (Polish and Progress, 5 December 2024) [4].

**Player vending machines.** Each machine has a front for buyers and a back for the owner, who stocks items and sets sell orders; payments land in the machine's storage [13]. That description dates from the February 2017 introduction, when the cap was 7 orders and the craft cost 50 HQM [13]; Devblog 180 later cut the cost to 20 HQM and 3 Gears and made it a default blueprint [7]. The wiki page confirms the current 20 HQM and 3 Gears cost and a 5 rW power input [8]. The May 2026 update redesigned the admin page, allowing orders to be set up from the built-in inventory, skins sold individually, and existing orders reordered [6]. Raiders who reach the rear panel can take the contents [8].

**Vending statistics.** Since 5 December 2024 owners can see transaction history, highest-revenue items, best sellers and customer stats; convars `vendingmachine.max_returned`, `vendingmachine.max_processed` and `vendingmachine.max_history` limit the queries and stored history, and machines show whether they are drone accessible [4].

**NPC vendors and dynamic pricing.** Safe-zone monuments such as the Outpost have vending machines selling resources and valuable items [12]. Scrap paid by NPC vending machines for items is dynamic: items start each wipe at 50% less value and can rise by up to an extra 100% when unsold [4]. Power Trip cut water-well vendor stock from 10 to 2 and lengthened restock from 2 to 10 minutes, leaving prices unchanged [2]. Livestock added a Stable vendor that buys grown cattle and sheep at a random offer based on gene quality (up to two re-rolls, then a 15 minute lockout) and buys wool, with the offer depending on the amount brought, up to 400 [1].

**Drone marketplace.** Introduced 4 February 2021 at Bandit Camp and Outpost, it lets a player choose a vending machine at a terminal and order from it for a 20 scrap fee, with delivery taking up to five minutes [5]. Orders can target any public vending machine and all NPC shops, but not machines outside open areas, and drones cannot be destroyed [5]. Terminals are locked to the buyer for 10 minutes [5]. The Livestock post states the marketplace needs power and that outages on low-population servers had blocked trade, so Heavy Fuses now last longer on servers of 10 or fewer players [1].

**Rentable shops.** At the Apartment Complex, a shop contract shows a non-refundable upfront scrap fee plus an hourly scrap rent, and at least 12 hours of rent is needed to open [3]. A shop can be taken over after 6 hours open at 2x cost (3x, 4x on later takeovers); the multiplier resets when rent runs out [3]. Shops are managed like vending machines but drones cannot access them [3]. The former owner has 24 hours to retrieve items, and the master key opens shops [3].

**Recyclers.** The wiki Recycler page lists 60% yield and 5 seconds per item [10]. Power Trip states the green recycler baseline is now 50%, rising to 60% with enough power-plant power, with duration falling from 5 s to 4.5 s at maximum power; a red recycler at the Power Plant gives 75% at maximum power only; yellow (safe-zone) recyclers are unchanged [2]. The Safe Zone Recycler page lists 40% and 8 seconds, at Outpost and Bandit Camp [11]. The vending machine item page lists recycling outputs of 12 HQM for the standard recycler and 8 HQM for the safe-zone one [8].

# Reference Data

**Evidence layer.** Wiki values are undated; Facepunch rows show their post date.

| Item or system | Value | Source and date | Ref |
|----------------|-------|-----------------|-----|
| Scrap stack, despawn | 1,000; 20 min | Wiki, undated | [9] |
| Marketplace delivery fee | 20 scrap per trade | Softcore update, 4 Feb 2021 | [5] |
| Marketplace delivery time, lock | Up to 5 min; terminal locked 10 min | Softcore update, 4 Feb 2021 | [5] |
| NPC scrap sale price | Starts -50%, up to +100% extra if unsold | Polish and Progress, 5 Dec 2024 | [4] |
| Junkyard shred payout | 200 / 300 / 500 scrap (Mini / Scrap Heli / Attack) | Polish and Progress, 5 Dec 2024 | [4] |
| Vending Machine craft | 20 HQM, 3 Gears; Workbench 1; 30 s | Wiki, undated; cost matches Devblog 180 | [7][8] |
| Vending Machine repair | 15 Metal Fragments + 4 HQM (Repair Bench) | Wiki, undated | [8] |
| Vending Machine recycle (standard / safe zone) | 12 HQM / 8 HQM, plus Gears | Wiki, undated | [8] |
| Green recycler | 50% baseline, 60% at power | Power Trip, 6 Aug 2026 | [2] |
| Red recycler | 75%, maximum power only | Power Trip, 6 Aug 2026 | [2] |
| Safe Zone Recycler | 40%, 8 s per item | Wiki, undated | [11] |
| Shop: minimum rent to open | 12 hours | Common Ground, 2 Jul 2026 | [3] |
| Shop takeover | After 6 h open; 2x, then 3x, 4x | Common Ground, 2 Jul 2026 | [3] |
| Shop item retrieval | 24 hours | Common Ground, 2 Jul 2026 | [3] |
| Water well vendor stock / restock | 2 (was 10) / 10 min (was 2) | Power Trip, 6 Aug 2026 | [2] |
| Animal vendor re-rolls, lockout | 2 re-rolls; 15 min | Livestock, 1 Oct 2026 | [1] |
| Wool offer cap | 400 per sale | Livestock, 1 Oct 2026 | [1] |
| Scrap loot: Elite / Military / Basic crate / barrel | 25 / 8 / 3 / 2 | Wiki, undated | [9] |

The upfront and hourly scrap amounts for rentable shops are not stated in the sources opened [3].

# Version & Patch Notes

**Evidence layer.**

| Date | Update | Change | Ref |
|------|--------|--------|-----|
| 9 Feb 2017 | Vending machines added | Front and back, 7 sell orders, 50 HQM + 3 Gears | [13] |
| 5 Oct 2017 | Devblog 180 | Vending machine default blueprint; cost to 20 HQM; side access exploit fixed | [7] |
| 4 Feb 2021 | Softcore Gamemode Update | Drone marketplace at Bandit Camp and Outpost, 20 scrap fee | [5] |
| 5 Dec 2024 | Polish and Progress | Dynamic NPC scrap pricing; vending statistics; Junkyard shredding payouts | [4] |
| 7 May 2026 | Upgrade hard, raid harder | Vending machine UI refresh | [6] |
| 2 Jul 2026 | Common Ground | Rentable shops; vending machine auto-sorting support | [3] |
| 6 Aug 2026 | Power Trip | Green recycler to 50%; red recycler; water well vendor stock cut | [2] |
| 1 Oct 2026 | Livestock | Stable vendor, wool trading, vendor bartering, marketplace power note | [1] |

Volatile: recycler efficiency, NPC prices, drone fee and shop rent.

# Common Pitfalls

- Trusting the wiki Recycler page: it says 60% and 5 s, while Power Trip moved the green baseline to 50% [2][10].
- Treating 2017 vending guides as current: order caps and cost have since changed [7][13].
- Expecting drones to reach any machine: those outside open areas, and rentable shops, are unreachable [3][5].
- Leaving a marketplace purchase uncollected: the terminal is only locked to you for 10 minutes [5].
- Storing valuables in a shop or machine: the master key unlocks shops, and raiders reaching a machine's rear panel can take its contents [3][8].
- Selling repeatedly to NPCs and expecting steady prices: the dynamic price falls with sales [4].

# Interactions & Related Systems

- Scrap is the research and workbench input; see rust-items-crafting-foundation [9].
- Safe-zone monuments, the Apartment Complex and Power Plant are covered in rust-monuments-loot; power from Heavy Fuses feeds recyclers and the marketplace [1][2].
- Helicopters and other vehicles are bought and shredded for scrap; see rust-vehicles [4].
- Livestock vendors connect to rust-farming-food [1].
- Recycler yields on deployables are tabulated in rust-turrets-deployables; vending machines need a power input, see rust-electricity-logic [8].
- Vending history convars: see rust-server-convars-reference [4].
- Softcore and Hardcore rules differ; see rust-game-modes [5].
- Update dates: rust-update-timeline-2026.

# Assessed Guidance

**Judgement layer.**

## Guidance 1 — Recheck recycler numbers in game before planning scrap income

- **Guidance:** Do not use the wiki's 60% green recycler figure; verify efficiency in game and assume it varies with Power Plant output.
- **Evidence basis:** Power Trip changed the baseline to 50% while the wiki page is undated and still lists 60% [2][10].
- **Confidence:** Medium. The contradiction is documented, but which value is live was not tested in game.
- **So what:** Recycling plans and yield tables copied from older guides will overstate returns.

## Guidance 2 — Treat NPC scrap sales as a spread-out income, not a repeat one

- **Guidance:** Sell varied items across the wipe rather than dumping one type repeatedly.
- **Evidence basis:** Dynamic pricing starts at -50% and rises up to +100% only when an item is unsold [4].
- **Confidence:** Medium. The mechanism is primary, but the exact curve is not published in the sources opened.
- **So what:** Players who sell the same item repeatedly earn less per unit.

## Guidance 3 — Use the marketplace for safety, but collect immediately

- **Guidance:** Order via drone when travel is risky, and stay at the terminal to collect.
- **Evidence basis:** Drones cannot be destroyed and the terminal locks to you for 10 minutes [5].
- **Confidence:** Medium. Facepunch states the design aim, but the post is from 2021 and later behaviour was only partly rechecked.
- **So what:** A 20 scrap fee buys a protected transfer, with a time limit to claim it.

## Guidance 4 — Price rentable shops against rent plus takeover risk

- **Guidance:** Only open a shop if sales will cover the upfront fee and at least 12 hours of rent, and keep valuables out.
- **Evidence basis:** Fee, rent, 6 hour takeover and master key access are stated [3].
- **Confidence:** Low. The scrap amounts are not published in sources opened, so profitability is unquantified.
- **So what:** Treat shops as a small-scale convenience until costs are confirmed in game.

# Open Questions

- Exact scrap prices of NPC buy and sell orders; no citable Facepunch table was found.
- Upfront and hourly scrap cost of Apartment Complex shops [3].
- Whether the 20 scrap marketplace fee is unchanged since 2021; a Rustafied recap reportedly says the fee varies by order, but it was not opened.
- Whether the wiki Recycler (60%) and Safe Zone Recycler (40%) pages match the live build, and the yellow recycler value after Power Trip [2][10][11].
- What the Livestock "vendor bartering mechanic" does [1].
- Whether a destroyed vending machine drops its contents fully or partly in the current build; no opened source settles it.
- Vending machine HP and order cap today.

# References

**Primary Sources**

- [1] **Facepunch** — *Livestock Update*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [2] **Facepunch** — *Power Trip*. https://rust.facepunch.com/news/power-trip. Accessed 2026-10-08.
- [3] **Facepunch** — *Common Ground*. https://rust.facepunch.com/news/common-ground. Accessed 2026-10-08.
- [4] **Facepunch** — *Polish and Progress*. https://rust.facepunch.com/news/polish-and-progress. Accessed 2026-10-08.
- [5] **Facepunch** — *Softcore Gamemode Update*. https://rust.facepunch.com/blog/softcore-gamemode-update/. Accessed 2026-10-08.
- [6] **Facepunch** — *Upgrade hard, raid harder*. https://rust.facepunch.com/news/upgrade-hard-raid-harder. Accessed 2026-10-08.
- [7] **Facepunch** — *Devblog 180*. https://rust.facepunch.com/news/devblog-180. Accessed 2026-10-08.
- [8] **Facepunch Rust Wiki** — *Vending Machine*. https://wiki.facepunch.com/rust/item/vending.machine. Accessed 2026-10-08.
- [9] **Facepunch Rust Wiki** — *Scrap*. https://wiki.facepunch.com/rust/item/scrap. Accessed 2026-10-08.
- [10] **Facepunch Rust Wiki** — *Recycler*. https://wiki.facepunch.com/rust/Recycler. Accessed 2026-10-08.
- [11] **Facepunch Rust Wiki** — *Safe Zone Recycler*. https://wiki.facepunch.com/rust/Safe_Zone_Recycler. Accessed 2026-10-08.
- [12] **Facepunch Rust Wiki** — *Outpost*. https://wiki.facepunch.com/rust/Outpost. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- [13] **Rustafied** — *Vending Machines: How they work* (9 February 2017). https://www.rustafied.com/updates/2017/2/9/vending-machines-how-they-work. Accessed 2026-10-08.

**Further Reading**

- See the Further Reading section below.

# Further Reading

- Rustafied, Update package incoming (4 February 2021): https://www.rustafied.com/updates/2021/2/4/update-incoming

# Related Documents

- rust-items-crafting-foundation
- rust-monuments-loot
- rust-turrets-deployables
- rust-vehicles
- rust-farming-food
- rust-server-convars-reference
- rust-update-timeline-2026
- rust-game-modes
- rust-raiding-costs-defence
- rust-electricity-logic

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
