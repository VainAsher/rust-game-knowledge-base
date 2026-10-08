---
id: rust-wipes-map-generation
title: "Rust Wipes and Map Generation"
version: 1.0.0
status: frozen
confidence: Medium
category: Server Administration
topic: "Wipes and map generation"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-server-administration-foundation, rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-building-raiding-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation, rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence, rust-server-convars-reference, rust-plugin-development-hooks, rust-update-timeline-2026, rust-monuments-loot, rust-farming-food, rust-vehicles, rust-moderation-anti-cheat, rust-carbon-vs-oxide]
tags: [wipe, map, seed, worldsize, procgen, custom-maps]
game_build_checked: "October 2026 update (Livestock Update, 1 Oct 2026)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-wipes-map-generation |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Server Administration |
| Region | Global |
| Game build checked | October 2026 update (Livestock Update, 1 Oct 2026) |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This deep-dive goes below the overview in the server administration foundation. It covers how a Rust server wipe works at file level (map, blueprint and full wipes), the wipe timer and its schedule tags, the three inputs that define a procedural map (level, seed, world size), the JSON procedural-generation configuration, and how to host and change a custom map.

Confidence is Medium. Nearly every statement rests on Facepunch wiki pages, which are primary, but several pages are marked unfinished, the wiki states no defaults for world size or seed, and the wiki says nothing explicit about a "full wipe" procedure or a forced-wipe calendar date. Those gaps are listed under Open Questions. Checked against the October 2026 update [1].

# Key Facts

- A map wipe happens when the `.sav` file is replaced; a blueprint wipe additionally needs `player.blueprints` deleted [2].
- A forced wipe raises the protocol number in the save file name, so the server starts a new file [2].
- The wipe timer default is the first Thursday of each month at 19:00 Europe/London, which the wiki says aligns with forced wipes [3].
- Schedule tags `monthly`, `biweekly` and `weekly` are mutually exclusive within their group [4].
- A procedural map is defined by size (1000 to 6000), seed (0 to 2147483647) and map type; its file is `.map` named MapType.Size.Seed.map [5][6].
- Procedural-generation JSON settings apply only when a map is first generated; delete the `.map` file to regenerate [7].
- A custom map is served from `+server.levelurl`, which needs a direct, always-available download link [8].
- Facepunch provides no map editor; RustEdit and Rust Map Editor are community tools [9].

# Scope

Covers vanilla dedicated servers on PC: wipe mechanics and timing, world size and seed, procedural generation customisation, and custom map hosting, against the October 2026 build. Not covered: the full convar list (rust-server-convars-reference), what is on a map (rust-monuments-loot), plugin-driven wipe automation (rust-plugin-development-hooks), and patch history (rust-update-timeline-2026). Console editions are excluded. Building custom maps in an editor is described only at the level of what the wiki documents.

# Definitions

- **Map wipe** — replacing the `.sav` file so entities, buildings and deployables reset [2].
- **Blueprint (BP) wipe** — deleting `player.blueprints` so learned blueprints reset [2].
- **Forced wipe** — the wipe a new protocol version causes by changing the save file name [2].
- **Protocol number** — the number before a save file's extension [2].
- **Procedural map** — a map generated from size and seed rather than loaded from a file [6].
- **Custom map** — a pre-built `.map` file downloaded from a URL [6][8].
- **Tier / topology** — map terrain classification referenced by the procedural-generation percentages [7].

# Core Mechanics

**Wipe types at file level.** The `.sav` file holds map data, entities, player buildings and deployables, should share the map's name, and is backed up on each save. Forced wipes generally affect the `.sav` file because they only force a map wipe. To force a blueprint wipe, `player.blueprints` must also be deleted at the same time [2]. The wiki calls it "dangerous and ill-advised to just rename an old sav" to avoid a forced wipe [2]. The wiki does not define a separate "full wipe"; the combination of a new `.sav` and deleted `player.blueprints` is the closest documented equivalent *(assessed reading of [2])*.

**Other persistent files.** `player.deaths` stores death information, `player.states` stores death markers and the hostile timer, `player.tokens` stores per-player Rust+ pairing tokens (removing it forces re-pairing) and `sv.files` stores player signs and contact-system pictures. The page does not say which of these a wipe resets [2].

**Wipe timer.** The timer is configured by `wipetimer.wipeDayofWeek` (0 Sunday to 6 Saturday, default 4), `wipetimer.wipeHourofDay` (default 19, decimals allowed), `wipetimer.wipeTimezone` (default Europe/London), `wipetimer.wipeUnixTimestampOverride` (exact time, overrides everything, ignored if in the past) and `wipetimer.wipeCronOverride` (custom cron expression). `PrintWipe` shows frequency, timezone, wipe time, time remaining and the next 10 occurrences [3].

**Schedule tags.** The wipe schedule group has three tags: monthly (`m`), biweekly (`b`) and weekly (`w`); tags within a group must not be combined [4]. Per the wipe timer page, monthly is the first Thursday of the month, weekly is every Thursday, and biweekly is the first and third Thursday, with a three-week gap in five-week months split into two plus one weeks, all at 19:00 London time [3]. The server-browser tag page lists no blueprint-wipe or map-size tags [4].

**Endgame events.** Events begin on the last day of the wipe cycle, 24 hours before the wipe by default; `eventschedulewipeoffset.event_hours_before_wipe` changes this and 0 disables them. They are the F-15E Strike Eagle flyover (no direct gameplay impact per the wiki) and Road Bradleys, whose count is WorldSize / 1000 * 2 [3].

**Level, seed and size.** `server.level "Procedural Map"` is the only map type the wiki documents; `server.seed` accepts 0 to 2147483647; `server.worldsize` is suggested at 1000 to 6000, and larger maps need more disk and memory [5]. The Map Data page gives the same ranges [6]. Generated maps are stored as `.map` files named MapType.Size.Seed.map in the `maps` folder [6]; the Getting Started page gives the procedural form `proceduralmap.SIZE.SEED.map` [2].

**Procedural generation customisation.** A JSON file in the `server.identity` folder is loaded with `+world.configfile "myConfig.txt"`. Settings apply only when a map is first generated. The four biome percentages are normalised to total 100 percent. Too little Tier0 topology can leave no spawn points, which kicks players for an InsideTerrain violation, and some monuments need specific tiers or biomes and may stop spawning. `Powerlines` does not cover small telephone poles along roads. `AboveGroundRails` only works on maps of size 4250. Use a prefab blacklist or whitelist, not both; matching is by substring [7].

**Custom maps.** Set `+server.levelurl [url]` and remove `+server.worldsize` and `+server.seed`. The host must be up 24/7 because players download from it, the link must be a direct download, and a `file:///` path works only for local testing [8]. Map data changes go through the Rust.World SDK [10]. Facepunch provides no map editor; RustEdit (community, some tools Patreon-gated) and Rust Map Editor (open-source, built on Unity) are community-made [9].

**Changing a custom map mid-wipe.** Shut the server down, change `server.levelurl`, rename the existing `.sav` to match the new map name (for example `MapVersion1.182.sav` to `MapVersion2.182.sav`), and leave the old `.map` in place. Terrain changes can leave trees, nodes and bases floating or buried, and entities added only in the second map do not load [11].

# Reference Data

Checked against the October 2026 update [1]. Defaults are as printed on the cited wiki pages.

| Setting | Default / range | Source |
|---------|-----------------|--------|
| `wipetimer.wipeDayofWeek` | 4 (Thursday); 0 to 6 | [3] |
| `wipetimer.wipeHourofDay` | 19; decimals allowed | [3] |
| `wipetimer.wipeTimezone` | Europe/London | [3] |
| `eventschedulewipeoffset.event_hours_before_wipe` | wiki says "within a hour" of the last day; 0 disables | [3] |
| `server.seed` | 0 to 2147483647 (default not stated) | [5] |
| `server.worldsize` | 1000 to 6000 suggested (default not stated) | [5] |
| WorldData `size` field default | 4500 (terrain size in Unity metres) | [6] |
| World serialization number | 10 | [6] |

Procedural-generation JSON defaults, as listed on the wiki [7]:

| Key | Default |
|-----|---------|
| PercentageTier0 / Tier1 / Tier2 | 0.3 / 0.3 / 0.4 |
| PercentageBiomeArid | 0.4 |
| PercentageBiomeTemperate | 0.15 |
| PercentageBiomeTundra | 0.15 |
| PercentageBiomeArctic | 0.3 |
| PercentageBiomeJungle | 0.5 |
| MainRoads, SideRoads, Trails, Rivers, Powerlines | true |
| AboveGroundRails, BelowGroundRails, UnderwaterLabs | true |
| PrefabBlacklist, PrefabWhitelist | empty |

The wiki notes that Jungle replaces 50 percent of the tier 0 biome and that its default was recently lowered and may change again [7]. The wiki example `{ "Trails": false, "PrefabBlacklist": [ "electrical_box_", "powerline_poles" ] }` removes trails and blocks matching prefabs, and a longer example approximates retired barren maps; blacklisting dynamic objects such as bushes causes constant console spam [7].

Custom-map hosting convars for maps without an ocean: `baseboat.generate_paths false` and `cargoship.event_enabled false`, plus optionally `ai.ocean_patrol_path_iterations 0` (static cargo ship) [11].

# Version & Patch Notes

- 1 October 2026 (Livestock): the Air Wolf helipad now starts each wipe in disrepair and stays repaired for that wipe, with `vehicle.padrepairsrequired` and `vehicle.setrepairablepads` available; 15k+ renderers were trimmed from the standard procedural world and a rare ocean "holes" generation bug was fixed. A mandatory server and client update is set for 22 October at 18:00 BST [1].
- Barren maps were retired in the December 2023 update, per the procedural generation wiki page [7].
- Volatile: the wiki says the Jungle percentage default may change again [7]; custom-map and hosting pages are marked unfinished [8][10].

# Common Pitfalls

- Editing the procedural-generation JSON and expecting an existing map to change; delete the `.map` file first [7].
- Lowering Tier0 too far, causing spawn-less terrain and InsideTerrain kicks [7].
- Reusing a filename for an updated custom map, which makes clients load the cached copy and show "World cache version mismatch" or "World File Outdated" [11].
- Hosting the map behind a page with a click-through button, a Discord message link, or a Dropbox link without `dl=1`; none give a direct download [8][11].
- Renaming an old `.sav` to dodge a forced wipe [2].
- Running a custom map with no accessible ocean, which can freeze loading until the cargo ship event is disabled [11].
- Expecting `AboveGroundRails` to take effect on a non-4250 map [7].

# Interactions & Related Systems

- The foundation covers install, ports and the overview of this topic: rust-server-administration-foundation [2][3].
- Full convar detail lives in rust-server-convars-reference; monuments that depend on tier or biome are covered in rust-monuments-loot [7].
- Endgame events and Road Bradleys scale with world size [3]; see rust-vehicles and rust-combat-damage-model for what they do in play.
- Wipe cadence follows Facepunch's monthly update schedule; see rust-update-timeline-2026 and rust-updates-meta-foundation [1][3].
- Blueprint wipes interact with crafting progression; see rust-items-crafting-foundation. Wipe length shapes raiding economics; see rust-raiding-costs-defence.
- Plugin frameworks must be reinstalled after updates and can automate wipe tasks; see rust-carbon-vs-oxide and rust-plugin-development-hooks.
- Custom-map prefab limits (networked entities cannot be rescaled, some elements fail stability checks, deployables decay) affect building play [10].

# Assessed Guidance

## Guidance 1 — Treat the default wipe timer as correct and change cadence by tag, not by hacking files

- **Guidance:** Keep the default timer and pick monthly, biweekly or weekly as the browser tag; use the override convars only for deliberate off-cycle wipes.
- **Evidence basis:** The wiki says the default aligns with forced wipes [3], tags are mutually exclusive [4], and renaming saves is discouraged [2].
- **Confidence:** High. All three statements are first-party Facepunch wiki text.
- **So what:** A schedule that matches the tag you advertise avoids player confusion and broken saves.

## Guidance 2 — Decide blueprint wipe policy explicitly at each wipe

- **Guidance:** Write down per wipe whether you delete `player.blueprints`, because a forced wipe alone does not reset blueprints.
- **Evidence basis:** Forced wipes generally affect only the `.sav`; a BP wipe needs the extra deletion [2].
- **Confidence:** Medium. The mechanic is documented, but the wiki gives no BP-wipe tag, so how players learn your policy is inference.
- **So what:** State the policy in the server description to avoid disputes.

## Guidance 3 — Generate and inspect the map before opening the server

- **Guidance:** Test a seed and world size on a private instance, then lock them; change procedural JSON only before first generation.
- **Evidence basis:** Config applies only at first generation [7], size affects resource needs [5], and overly sparse Tier0 can break spawning [7].
- **Confidence:** Medium. The constraints are documented; the advice to preview is a practice recommendation.
- **So what:** Avoids a mid-wipe regenerate that would force a wipe.

## Guidance 4 — Version every custom map file name and plan for no mid-wipe terrain edits

- **Guidance:** Use a new unique filename per map version, host on infrastructure you control, and avoid swapping maps mid-wipe.
- **Evidence basis:** Same-name caching causes client mismatch errors [11]; mid-wipe swaps leave floating objects and skip new entities [11]; the host must be always available [8].
- **Confidence:** High. Facepunch's FAQ documents each failure directly.
- **So what:** Fewer connection failures and no corrupted bases.

# Open Questions

- The wiki gives no defaults for `server.worldsize` and `server.seed`; verify on a running server. The WorldData default of 4500 is a file-format field, not necessarily the server default [6].
- No page read gives a calendar rule for the forced wipe beyond the wipe timer's statement that the default aligns with it; the Livestock post does not restate it [1][3].
- The wiki does not say which of `player.deaths`, `player.states`, `player.tokens` and `sv.files` should be cleared on a wipe [2].
- Whether `world.configstring` takes the same JSON inline is unconfirmed on the page [7].
- The `eventschedulewipeoffset` default is described only as "within a hour" [3].
- Custom-map and map-data pages are marked unfinished; the editor tool details are secondhand wiki summaries [8][9][10].

# References

**Primary Sources**

- [1] **Facepunch** — *Livestock Update* (1 October 2026). https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [2] **Facepunch Wiki** — *Getting started with your rust server*. https://wiki.facepunch.com/rust/Getting-Started_w-Server. Accessed 2026-10-08.
- [3] **Facepunch Wiki** — *Server Wipe Timer*. https://wiki.facepunch.com/rust/server-wipe-timer. Accessed 2026-10-08.
- [4] **Facepunch Wiki** — *Server Browser Tags*. https://wiki.facepunch.com/rust/server-browser-tags. Accessed 2026-10-08.
- [5] **Facepunch Wiki** — *Creating a server*. https://wiki.facepunch.com/rust/Creating-a-server. Accessed 2026-10-08.
- [6] **Facepunch Wiki** — *Map Data*. https://wiki.facepunch.com/rust/Map_Data. Accessed 2026-10-08.
- [7] **Facepunch Wiki** — *Procedural Generation Customization*. https://wiki.facepunch.com/rust/procedural_generation_customization. Accessed 2026-10-08.
- [8] **Facepunch Wiki** — *Hosting Custom Maps*. https://wiki.facepunch.com/rust/Hosting_a_custom_map. Accessed 2026-10-08.
- [9] **Facepunch Wiki** — *Map Editors*. https://wiki.facepunch.com/rust/Map_Editors. Accessed 2026-10-08.
- [10] **Facepunch Wiki** — *Custom Maps*. https://wiki.facepunch.com/rust/Custom_Maps. Accessed 2026-10-08.
- [11] **Facepunch Wiki** — *FAQ and Troubleshooting*. https://wiki.facepunch.com/rust/FAQ_and_Troubleshooting. Accessed 2026-10-08.

**Community & Practitioner Evidence**

None cited in this version.

**Further Reading**

- Facepunch wiki index: https://wiki.facepunch.com/rust/

# Further Reading

The Facepunch wiki pages on Terrain, Topology and Weather for custom map makers, and the Rust.World SDK on GitHub referenced by the Custom Maps page.

# Related Documents

- rust-server-administration-foundation
- rust-server-convars-reference
- rust-monuments-loot
- rust-update-timeline-2026
- rust-raiding-costs-defence
- rust-plugin-development-hooks

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
