# Project Status

- **Phase:** Clusters 1-5 built (6 foundations + 24 depth docs), 8 Oct 2026. Game build checked: Livestock Update (1 Oct 2026).
- **Documents:** 30. Twenty-seven frozen at v1.0.0 (Medium confidence); three held at v0.1.0 / in-review, Low confidence (raiding-costs, wildlife-npcs, teams-clans). `rust-raiding-costs-defence` is held at v0.1.0 / in-review, Low confidence.
- **Also held:** `rust-teams-clans` (clan cap, ranks and vanilla team size community-only; only Facepunch figure is softcore max 4 from a 2021 post).
- **Also held:** `rust-wildlife-npcs` (all health values community-only, patrol heli health conflicts 9895.6 vs ~10,000).
- **Why raiding-costs held:** every HP, damage and explosive-count figure is third-party and unverified; sources conflict (e.g. armoured door 1,000 vs 800 HP). Needs a human decision: freeze as Low, or find in-game data.
- **Next:** remaining depth docs per category; review volatile values after the 5 Nov 2026 update. Mandatory Halloween update 22 Oct 2026 18:00 BST (per Facepunch Livestock post).
- **Not published.** No GitHub repo or Pages until explicitly authorised.

## Known gaps

- Combat: fall damage, explosion damage to players, non-head hit-zone multipliers, armour stacking unsourced.
- Weapons: magazine size, fire rate, pellet counts mostly unsourced; wiki stats undated.
- Raiding: structure HP, per-door costs, upkeep fractions, vanilla offline protection (see hold above).
- Convars: gather-rate and EAC settings have no Facepunch source.
- Plugins: conflicting-hook-return resolution, lang API, Carbon hook counts unverified.
- Foundations (frozen v1.0.0) still carry their own Open Questions; the timeline doc adds Jan and Feb 2026 that the updates foundation omits.

## Cluster 3 gaps

- Monuments: no per-monument loot tables or current card-tier table from a primary source; several wiki monument pages 404.
- Farming: no growth times, yields or genetics numbers; livestock yields unpublished.
- Vehicles: base stats for minicopter, scrap heli, modular car, horse come from 2019/2020 community posts.
- Wipes: no explicit full-wipe definition or default world size/seed on Facepunch pages.
- Anti-cheat: no EAC configuration published; encryption convar naming discrepancy.
- Carbon licence conflict: project site says MIT, repo says GPL-3.0 (doc follows the repo). No independent performance benchmark.

## Cluster 4 gaps and follow-ups

- Possible correction to the frozen server-admin foundation: its table gives query port 28017, but the new permissions doc derives 28016 from the wiki formula (rcon.port default inferred = server.port 28015). Needs a live-server check, then a v1.0.1 revision if confirmed.
- Electricity: small battery differs between wiki (15 rW / 400 rWm) and Nov 2019 devblog (10 / 150); wire limits and generator fuel burn unsourced.
- Turrets: no range/health/damage on any Facepunch page; targeting rules from one community guide.
- Performance: tickrate, gc and saveinterval convars are practitioner-only and conflict between guides.
- Game modes: official availability of Hardcore conflicts (wiki says shut Nov 2023, devblog says returned Aug 2025); Oct 2026 mode rules unchecked.
- Permissions: which commands each auth level can run, and the April 2026 RCON connection-limit convar names, unsourced.

## Cluster 5 gaps and follow-ups

- Frozen `rust-server-convars-reference` lists `relationshipmanager.maxteamsize`; the teams worker could not verify that name from an opened source. Re-check and revise (v1.0.1) if wrong.
- Recycler: wiki shows 60%/40% outputs but Power Trip says green 50% (60% powered), red 75%. Tools and economy docs treat the wiki as stale; verify in game.
- Gather-rate gap NOT closed: no primary source defines the wiki's gather damage/bonus columns or resources per hit.
- Economy: NPC buy/sell price tables, rentable shop costs, vending machine HP and order cap unsourced.
- Skins: cosmetic-only rule rests on 2015 devblogs; creator revenue share not in any official source (deliberately omitted).
- Fishing: no bait values, catch odds, rod durability or overfishing timers; fish trap and village wiki pages 404.
- Clothing: stacking maths of layers not stated; several garments unsourced.
