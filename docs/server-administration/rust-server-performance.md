---
id: rust-server-performance
title: "Rust Server Performance"
version: 1.0.0
status: frozen
confidence: Medium
category: Server Administration
topic: "Server performance and hardware"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-server-administration-foundation, rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-building-raiding-foundation, rust-modding-plugins-foundation, rust-updates-meta-foundation, rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence, rust-server-convars-reference, rust-plugin-development-hooks, rust-update-timeline-2026, rust-monuments-loot, rust-farming-food, rust-vehicles, rust-wipes-map-generation, rust-moderation-anti-cheat, rust-carbon-vs-oxide, rust-electricity-logic, rust-turrets-deployables, rust-wildlife-npcs, rust-server-permissions-rcon, rust-game-modes]
tags: [performance, hardware, tickrate, gc, entities, profiler]
game_build_checked: "October 2026 update (Livestock Update, 1 Oct 2026)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-server-performance |
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

This deep-dive goes below the overview in rust-server-administration-foundation and covers what Facepunch documents about running a Rust server fast: hardware and operating-system requirements, the profiler and measurement commands, the performance-related convars Facepunch has named in devblogs, and what recent updates changed in server threading, allocation and entity networking.

Confidence is Medium. The hardware floor, the profiler and the devblog convars are first-party. But Facepunch's wiki gives no CPU figure, no entity-count limit, and no documentation of tick rate, garbage-collection or save-interval convars in any page opened for this document. Those topics rest on hosting-provider articles, which are labelled practitioner evidence and conflict with each other. Checked against the October 2026 update [5].

# Key Facts

- Facepunch's wiki lists 12 GB free RAM (more for a 6k map), 15 GB free disk (SSD/NVMe highly preferred) and Windows, Linux or OSX, and says these values "are not fixed and highly depend on the use case and population of the server" [1].
- The wiki states no CPU figure, only that more players need a faster CPU [1].
- The server has a built-in profiler enabled with the `-enableProfiler` launch argument; leaving it enabled slightly decreases performance [2].
- `UsePlayerUpdateJobs` defaults to 2 since the Spring Clean update, with level 3 experimental [4].
- Livestock budgets NPC processing per frame, so NPCs react slower under load instead of the server slowing down [5].
- Practitioner guides disagree on the fps and tick values to use and on the GC buffer convar name, and none of those settings was found in Facepunch documentation *(assessed)* [10][11][12].

# Scope

Covers PC dedicated servers (Windows and Linux) running vanilla or modded, checked against the October 2026 update. Hardware, operating system, measurement, tick and frame-rate convars, garbage collection, saving, entity load and the update history of server optimisations. Not covered: general convar listings (rust-server-convars-reference), plugin-specific profiling (rust-plugin-development-hooks, rust-carbon-vs-oxide), hosting-provider pricing and console editions.

# Definitions

- **Server FPS** — the server's frame rate, readable with the `fps` command on the server [3].
- **`fps.limit`** — maximum frame rate; the `sv` prefix targets the server [3].
- **Garbage collection (GC)** — automatic memory reclamation in the Unity runtime; allocation pressure on it is a stated Facepunch concern [6].
- **Entity** — any networked object such as buildings, deployables, NPCs and vehicles; see rust-building-raiding-foundation.
- **Practitioner evidence** — advice from hosting providers, not Facepunch.

# Core Mechanics

**Requirements.** The wiki's Requirements list is an OS "based on Windows, Linux or OSX", 12 GB free RAM ("6k map will use more") and 15 GB free disk with SSD/NVMe highly preferred; it links two third-party RAM calculators and stresses the values are not fixed [1]. Map size (`+server.worldsize`, 1000 to 6000) raises disk and memory need, and more players (`+server.maxplayers`) need a faster CPU [1]. The Linux console is not interactive, so an RCON client or a screen session is needed [1].

**Networking threading.** The wiki notes the query port was changed in the 2 February 2023 update to support the new multi-threaded networking, described as a performance benefit [1].

**Measurement.** `fps` returns the current frames per second on client or server; `fps.limit` sets the maximum frame rate, with the `sv` prefix for the server; `perf 0` to `perf 6` show stats, with RAM usage at level 3, invokes at 5 and tasks at 6; `benchmark` runs a simulation of many parts of the game [3]. The profiler starts with `-enableProfiler`. `profile.perfsnapshot [delay] [name] [frames]` records 1 to 10 frames; `profile.perfsnapshot_stream` records until a buffer of up to 256 MB fills. Recording can noticeably slow the server, a snapshot must finish saving before another starts or the server can crash, and snapshots are saved as `.json.gz` in the `profiler` folder, openable in Perfetto [2].

**Threaded player updates.** In Spring Clean Facepunch set `UsePlayerUpdateJobs` to 2 by default, with the 0 and 1 modes slated for removal; level 3 is experimental and uses UniTask to reduce allocations and parallelise anti-hack and network streaming [4]. A later post says level 3 skips NetWrite preallocation and "can save 0.6ms on busy frames" [6]. Livestock lists a level 4 (experimental) fix for syncvar serialisation thread safety [5].

**Allocation and GC pressure.** The Built Different pool rewrite is described as "vital for avoiding creating pressure on the Garbage Collector"; it removed or amortised about 20 allocation sources on the server, and servers can revert the new lock-free pool with `pool.usemutexpool 1` [6]. Spring Clean added lazy allocation of Network.Group internals and dynamic minimum capacity for object work queues [4].

**Entity networking and processing.** Spring Clean networks entities in a large blocky circle rather than a square, with per-entity network ranges so small items load only when near [4]. Livestock processes only a subset of NPCs per frame up to a hardcoded time budget, parallelises vehicle ticking and reports navigation performance at least doubled [5]. Built Different caps the time of a single pathfinding query [6].

**Industrial and decay load.** The Industrial update added `server.conveyorMoveFrequency`, `server.industrialCrafterFrequency` and `server.maxItemStacksMovedPerTickIndustrial` [7]. Devblog 115 added `decay.tick` to scale decay to a server's wipe schedule, `maxflood` for the player-tick flood threshold, and `noclip_protection` mode 3 with `noclip_stepsize` and `noclip_maxsteps` [9].

**Historic baseline.** In 2015 Facepunch reported servers under 5 fps, traced to rigidbody use, `IsInvoking` and moving the player on every tick, with a feedback loop where a dropped frame rate could not recover [8].

**Practitioner layer (not Facepunch).** Hosting guides describe `server.tickrate` as read at startup with 30 to 60 as a range [10][12], `fps.limit` values (30 in one config table [11]; 30 to 60 [10]; 120 under a different name [12]), `gc.buffer` 256 [11], `server.saveinterval` 300 [11][12], restarts every 12 to 24 hours [12], and single-thread clock speed outweighing core count [10][13]. These are labelled hosting-provider advice.

# Reference Data

Checked against the October 2026 update [5] unless stated.

| Item | Value | Source | Class |
|------|-------|--------|-------|
| Free RAM | 12 GB (6k map more) | [1] | Primary |
| Free disk | 15 GB, SSD/NVMe highly preferred | [1] | Primary |
| OS | Windows, Linux or OSX | [1] | Primary |
| `server.worldsize` | 1000 to 6000 | [1] | Primary |
| CPU figure | none stated | [1] | Primary |
| Profiler launch argument | `-enableProfiler` | [2] | Primary |
| Snapshot frames | 1 to 10 (`perfsnapshot`); stream buffer capped 256 MB | [2] | Primary |
| `UsePlayerUpdateJobs` | default 2; 3 and 4 experimental | [4][5] | Primary |
| `pool.usemutexpool` | `1` reverts to mutex pool | [6] | Primary |
| `server.conveyorMoveFrequency` | default 5 s (Feb 2023 build) | [7] | Primary |
| `server.industrialCrafterFrequency` | default 5 s (Feb 2023 build) | [7] | Primary |
| `server.maxItemStacksMovedPerTickIndustrial` | default 12 (Feb 2023 build) | [7] | Primary |
| `decay.tick` | default interval 10 minutes (2016 changelog) | [9] | Primary |
| Server mesh stripping saving | about 600 MB runtime, 2.7 GB disk (Spring Clean) | [4] | Primary |
| `server.tickrate` | 30 to 60 suggested; read at startup | [10][12] | Practitioner |
| `fps.limit` | default 30 per one config table; other guides differ | [10][11][12] | Practitioner |
| `gc.buffer` | 256 (MB) per one config table; name disputed | [11] | Practitioner |
| `server.saveinterval` | 300 per two guides | [11][12] | Practitioner |
| Restart interval advice | 12 to 24 hours | [12] | Practitioner |

# Version & Patch Notes

- 1 October 2026 (Livestock): per-frame NPC budget, parallel vehicle ticking, doubled navigation performance, a fix for leaked SyncVar buffers with parallel saves, and a level 4 jobs fix [5].
- Built Different (reported by a practitioner as 4 June 2026 [10]): pool rewrite, about 20 server allocation sources removed, `pool.usemutexpool` fallback, `UsePlayerUpdateJobs 3` NetWrite saving, pathfinding time cap [6].
- 2 April 2026 (Spring Clean): `UsePlayerUpdateJobs` default 2, server mesh stripping, entity network range changes, RCON and Rust+ connection-limit convars, a Linux ServerProfiler hotfix [4].
- 2 February 2023 (Industrial): industrial frequency convars and the query port change for multi-threaded networking [7][1].
- 16 June 2016 (Devblog 115) and 30 July 2015 (Devblog 71): decay.tick and flood/noclip convars; the 4 fps to 500 fps server fix [9][8].
- Volatile: every default above can change monthly; confirm on a running server with `find` [3].

# Common Pitfalls

- Leaving `-enableProfiler` on in production: Facepunch says it slightly decreases performance until the argument is removed [2].
- Starting a second snapshot before the first has saved can crash the server [2].
- Treating the wiki RAM figure as a fixed requirement; the page says it is not [1].
- Copying convar names from hosting guides, which disagree (`gc.buffer` versus `gc.buffercount`, `fps.limit` versus `server.fpslimit`) [10][11][12].
- Assuming a hosting plan tier is a sizing rule; plan RAM on provider pages is a product tier [10][13].

# Interactions & Related Systems

- Plugins add load that profiler snapshots can show; see rust-plugin-development-hooks and rust-carbon-vs-oxide [2].
- Map size and wipe cadence affect memory and file size; see rust-wipes-map-generation and rust-server-convars-reference [1].
- Entities from industrial, electricity and turret systems add per-tick work; see rust-electricity-logic and rust-turrets-deployables [7].
- NPC and animal load is budgeted per frame; see rust-wildlife-npcs [5].
- Anti-hack and network streaming are part of the threaded player update; see rust-moderation-anti-cheat and rust-server-permissions-rcon [4].
- Parent overview: rust-server-administration-foundation [1].

# Assessed Guidance

## Guidance 1 — Measure with the profiler before changing convars

- **Guidance:** Diagnose lag with `fps`, `perf` and a profiler snapshot, then change one setting at a time; remove `-enableProfiler` afterwards.
- **Evidence basis:** Facepunch documents these tools and their costs [2][3], and convar values elsewhere are disputed [10][11][12].
- **Confidence:** High. The tools and warnings are first-party documentation.
- **So what:** You find the actual cost instead of applying unverified hosting-guide numbers.

## Guidance 2 — Size for the wipe peak, not wipe day

- **Guidance:** Treat 12 GB RAM and 15 GB SSD as a floor and add headroom for a 6k map, high population or plugins, watching RAM with `perf 3`.
- **Evidence basis:** The wiki says the values are not fixed and that 6k maps use more [1]; `perf 3` shows RAM [3]; one provider says usage rises through a wipe [13].
- **Confidence:** Medium. The floor is first-party, but growth through a wipe is provider experience.
- **So what:** A server that is fine on wipe day can run short later in the wipe.

## Guidance 3 — Prefer a fast per-core CPU

- **Guidance:** Choose high single-thread speed over core count, while knowing parts of the server are now threaded.
- **Evidence basis:** Facepunch gives no CPU figure but documents threaded jobs and networking [1][4][6]; two providers say single-thread speed matters most [10][13].
- **Confidence:** Low. The CPU claim is provider opinion and threading has been changing.
- **So what:** Benchmark your own host rather than buying cores.

## Guidance 4 — Keep UsePlayerUpdateJobs at its default unless testing

- **Guidance:** Leave `UsePlayerUpdateJobs` at 2 and try levels 3 or 4 only on a test server.
- **Evidence basis:** Level 2 is the default and 3 and 4 are labelled experimental [4][5][6].
- **Confidence:** High. Facepunch labels the levels itself.
- **So what:** Experimental levels trade a small frame-time gain for stability risk.

## Guidance 5 — Treat tick, GC and save-interval advice as unverified

- **Guidance:** Verify any `server.tickrate`, `gc.*` or `server.saveinterval` change on a test server with `find` and `fps` before production.
- **Evidence basis:** No Facepunch page opened documents them, and providers conflict [10][11][12].
- **Confidence:** Low. The sources are one class and conflict.
- **So what:** You avoid a change that has no measured effect or that a later build ignores.

# Open Questions

- No Facepunch page opened documents `server.tickrate`, `gc.buffer` (or `gc.buffercount`, `gc.interval`, `gc.incremental`) or `server.saveinterval`; names, defaults and effects are practitioner-only. Resolve with `find` on a live Livestock server.
- `server.saveinterval` default is 300 per two guides [11][12]; a search snippet from another provider said 600 but that page could not be opened, so it is unresolved.
- `fps.limit` default (30 per [11]) is unconfirmed first-party.
- No official entity-count limit or per-player RAM formula was found.
- Facepunch gives no CPU guidance; the single-thread claim is practitioner-only.
- Industrial default values are from the 2023 build and need re-checking on the October 2026 build.

# References

**Primary Sources**

- [1] **Facepunch Wiki** — *Creating a server*. https://wiki.facepunch.com/rust/Creating-a-server. Accessed 2026-10-08.
- [2] **Facepunch Wiki** — *Profiler*. https://wiki.facepunch.com/rust/Profiler. Accessed 2026-10-08.
- [3] **Facepunch Wiki** — *Useful Console Commands*. https://wiki.facepunch.com/rust/useful_commands. Accessed 2026-10-08.
- [4] **Facepunch** — *Spring Clean* (2 April 2026). https://rust.facepunch.com/news/spring-clean. Accessed 2026-10-08.
- [5] **Facepunch** — *Livestock Update* (1 October 2026). https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [6] **Facepunch** — *Built Different*. https://rust.facepunch.com/news/built-different. Accessed 2026-10-08.
- [7] **Facepunch** — *Industrial Update* (2 February 2023). https://rust.facepunch.com/news/industrial-update. Accessed 2026-10-08.
- [8] **Facepunch** — *Devblog 71* (30 July 2015). https://rust.facepunch.com/news/devblog-71. Accessed 2026-10-08.
- [9] **Facepunch** — *Devblog 115* (16 June 2016). https://rust.facepunch.com/news/devblog-115. Accessed 2026-10-08.

**Community & Practitioner Evidence** (hosting-provider advice)

- [10] **XGamingServer** — *How do I Improve RUST Server Performance?* (first published 23 May 2021). https://xgamingserver.com/blog/how-do-we-improve-rust-server-performance/. Accessed 2026-10-08.
- [11] **XGamingServer** — *How to Configure Your Rust Dedicated Server (server.cfg)*. https://xgamingserver.com/docs/rust/server-config. Accessed 2026-10-08.
- [12] **HostHavoc** — *Rust server performance optimization* (24 February 2025). https://hosthavoc.com/blog/rust-server-performance-optimization. Accessed 2026-10-08.
- [13] **GameServerKings** — *How to Host a Rust Server* (7 August 2026). https://www.gameserverkings.com/knowledge-base/rust/how-to-host-a-rust-server/. Accessed 2026-10-08.

**Further Reading**

- Facepunch news index: https://rust.facepunch.com/news

# Further Reading

The Facepunch wiki Profiler page and the Facepunch news index for each month's server optimisation notes.

# Related Documents

- rust-server-administration-foundation
- rust-server-convars-reference
- rust-plugin-development-hooks
- rust-carbon-vs-oxide
- rust-wipes-map-generation
- rust-electricity-logic
- rust-turrets-deployables
- rust-wildlife-npcs

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
