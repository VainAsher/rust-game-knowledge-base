---
id: rust-modding-plugins-foundation
title: "Rust Modding and Plugins: Foundation"
version: 1.0.0
status: frozen
confidence: Medium
category: Modding & Plugins
topic: "Oxide/uMod and Carbon frameworks"
market: "Global"
document_type: foundation
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-building-raiding-foundation, rust-server-administration-foundation, rust-updates-meta-foundation]
tags: [oxide, umod, carbon, plugins, modding, permissions, codefling]
game_build_checked: "Rust 2634.289.1 (2 Oct 2026 hotfix) per Oxide.Rust release 2.0.7801; Carbon v2.0.262 and Oxide.Rust 2.0.7810 checked 2026-10-08"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-modding-plugins-foundation |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Modding & Plugins |
| Region | Global |
| Game build checked | Rust 2634.289.1 (Oct 2026 hotfix); Carbon v2.0.262; Oxide.Rust 2.0.7810 |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

Rust servers are modded through third-party frameworks that load C# plugins. The two live frameworks are Oxide (the uMod project, MIT licensed) and Carbon (GPL-3.0, billed as a drop-in Oxide replacement) [1][3][5]. Both were actively releasing on 2026-10-08: Oxide.Rust tag 2.0.7810 on 2026-10-07 and Carbon "Production Build v2.0.262" on 2026-10-02 [2][4].

This document covers what each framework is, how they differ, installation and the permission model, plugin sources and monetisation, and how the Rust server browser classifies modded servers. Confidence is Medium: framework status is primary-sourced, but the uMod licence rules, any explicit Facepunch policy on modded servers and the Oxide install guide pages could not be opened, so those parts rest on indirect sources or are flagged as open questions.

# Key Facts

- Oxide.Rust is a public GitHub repository under the MIT licence, with active development on the `develop` branch [3]. Its newest release seen was tag 2.0.7810, published 2026-10-07 [4].
- An earlier Oxide.Rust release, 2.0.7801 (2026-10-02), is described as a patch for the "October 2nd Rust hotfix #3 (2634.289.1)" [4].
- Carbon is a mod loader built on C# and Harmony with a permission system, user system and in-game GUI, licensed GPL-3.0 [1]. Its latest release seen was "Production Build v2.0.262", published 2026-10-02 [2].
- Carbon states it is fully compatible with Oxide plugins and keeps the same folder and plugin structure [1][5].
- Carbon maps its branches to Rust branches: `main` to public, `experimental` usually to release, `production` to public (or release on wipe day), with staging and aux branches described as extremely unstable [1].
- The Facepunch wiki lists `Modded`, `Oxide` and `Carbon` as server browser tags set through the `server.tags` convar [8].
- Codefling is a marketplace listing many paid Rust plugins, plus maps, prefabs and tools; some plugins are free [12].

# Scope

Covered: Oxide/uMod and Carbon on Rust dedicated servers (PC), installation overview, permissions, plugin sourcing, licensing norms as far as verifiable, and server-browser classification. Not covered: writing plugins, individual plugin reviews, console, and client-side modification. Build checked: Rust 2634.289.1 era (October 2026). Server operations belong in rust-server-administration-foundation.

# Definitions

- **Oxide / uMod:** the long-standing Rust modding framework; its docs are at docs.oxidemod.com [7][10].
- **Carbon:** an alternative mod loader, self-updating, using Harmony [1].
- **Plugin:** a C# file placed in the framework's plugins folder (`oxide/plugins` for Oxide) [7].
- **Permission:** a dotted string such as `coolplugin.use` granted to users or groups [11].
- **Server browser tag:** a short code set in `server.tags`; Modded, Oxide and Carbon are compressed to `z`, `o`, `y` [8].

# Core Mechanics

**Frameworks.** Oxide is described by the Facepunch wiki as a modding framework letting owners install plugins that change gameplay, such as items, crafting recipes and player behaviour [7]. Carbon describes itself as a self-updating, lightweight mod loader using the latest C# and Harmony, with a permission system, user system and in-game GUI [1].

**Differences (Carbon's own claims).** Carbon says it provides only essential hooks so a server stays close to vanilla, loads only hooks that plugins use, supports hot reload of Harmony mods, has SQL permissions with custom serializers, and an in-game interface for installing and updating plugins [5]. These are vendor claims, not independent benchmarks.

**Installation overview.** Oxide: per the Facepunch wiki, stop the server, run the Oxide installer from the Oxide site, and restart; typing `oxide` in the server console reaches the Oxide console [7]. Oxide's docs home lists dedicated guides for Server Setup, Installing Oxide, Installing Plugins and Permissions [10]. Carbon: download the platform archive from GitHub Releases, extract it to the root of the Rust dedicated server (beside `RustDedicated.exe` on Windows), start the server, and keep server files updated and verified [2][6]. A QuickStart script for Windows and Linux also exists [1].

**Plugin installation.** Plugins are downloaded from the Oxide site or community sites and placed in the `oxide/plugins` folder [7]. Carbon states the same folder structure is retained [5].

**Permissions model.** A practitioner guide documents that uMod creates two groups automatically, `admin` and `default`, that users can be in several groups, and that group permissions supersede individual grants [11]. Each plugin defines its own permission names, so the plugin author's setup notes are authoritative [11].

# Reference Data

Framework status checked 2026-10-08:

| Item | Oxide.Rust | Carbon |
|------|------------|--------|
| Licence | MIT [3] | GPL-3.0 [1] |
| Latest release seen | 2.0.7810, 2026-10-07 [4] | Production Build v2.0.262, 2026-10-02 [2] |
| Rust build named in notes | 2634.289.1 in 2.0.7801 (2026-10-02) [4] | Not stated in release body [2] |
| Branch model | `develop` branch seen [3] | main, experimental, production, rust_beta staging, aux01, aux02 [1] |

Oxide permission commands (practitioner source, checked 2026-10-08; syntax may vary by version) [11]:

| Purpose | Command |
|---------|---------|
| List groups | `oxide.show groups` |
| Grant to group | `oxide.grant group admin coolplugin.use` |
| Grant to player | `oxide.grant user <name or STEAM64_ID> <permission>` |
| Revoke from group | `oxide.revoke group admin coolplugin.use` |
| Add player to group | `oxide.usergroup add <name or STEAM64_ID> group_name` |
| Create group | `oxide.group add supporters` |
| Set parent group | `oxide.group parent tier_2 tier_1` |
| Who has a permission | `oxide.show perm coolplugin.use` |

Server browser tags [8]:

| Tag | Compressed code |
|-----|-----------------|
| Modded | z |
| Oxide | o |
| Carbon | y |

Plugin sources: Oxide site and docs [7][10]; Codefling, a marketplace with categories Plugins, Maps, Monuments, Prefabs, Bases, Tools, Discord Bots, Customizations, Graphics and Extensions, with example paid listings at $9.99, $24.99 and $32.99 on the day checked [12]. Codefling's page does not state licence terms; some developers add their own "sold as is" disclaimers [12].

# Version & Patch Notes

- Oxide.Rust 2.0.7801 patched for the 2 October 2026 Rust hotfix (2634.289.1) and added OnNpcTarget hooks for WildlifeHazard and BoatAI [4]. The framework shipped its own update for a Rust hotfix.
- Oxide.Rust 2.0.7810 followed on 2026-10-07 with no listed changes [4].
- Carbon's production build v2.0.262 was published 2026-10-02 [2].
- Facepunch's Community Update #13 (14 October 2014) already described a "modded" section of the server browser, so the modded category predates both current frameworks [9].
- Release numbers change frequently; re-check before relying on them.

# Common Pitfalls

- Running both frameworks: they are alternative loaders for the same plugin structure [5]; do not assume they can coexist, and read Carbon's Oxide-porting page before migrating.
- Game updates outpacing the framework: the Oxide release history shows a framework patch was needed after a Rust hotfix [4]; a server updated through SteamCMD may be ahead of its framework.
- Assuming admin rank gives plugin access: plugin commands need explicit permissions [11].
- Combining tags from the same group on one server is discouraged by the wiki [8].

# Interactions & Related Systems

Plugins hook into gameplay areas covered by other documents: rust-game-mechanics-foundation, rust-items-crafting-foundation (custom items and recipes [7]), rust-building-raiding-foundation, and rust-server-administration-foundation (server.tags and convars [8]). Patch cadence and hotfix timing are covered in rust-updates-meta-foundation.

# Assessed Guidance

## Guidance 1 — Pick the framework by plugin set and licence, not by speed claims

- **Guidance:** Choose Oxide when you rely on the broad uMod ecosystem and want the MIT-licensed reference implementation; consider Carbon for its in-game GUI and branch tracking after testing your plugin set on a staging server.
- **Evidence basis:** Both are active and Oxide-plugin-compatible per the vendor [1][2][3][4][5].
- **Confidence:** Medium. Compatibility and performance claims come from Carbon's own pages, not independent tests.
- **So what:** Do not migrate a live wipe server without rehearsing every plugin.

## Guidance 2 — Check the framework release before updating Rust

- **Guidance:** Check the framework's latest release for the new Rust build before updating the game server, and expect hook breakage after big updates.
- **Evidence basis:** Oxide shipped a dedicated patch for a Rust hotfix [4]; Carbon ties branches to Rust branches [1].
- **Confidence:** Medium. Based on two observed release histories.
- **So what:** Schedule updates after the framework release and keep a rollback copy.

## Guidance 3 — Grant plugin permissions to groups, not individuals

- **Guidance:** Manage access through groups with parent inheritance, since group permissions supersede individual grants.
- **Evidence basis:** Practitioner guide on groups and precedence [11].
- **Confidence:** Medium. A single practitioner source, so it cannot exceed Medium.
- **So what:** Fewer stale per-player grants and easier audits.

## Guidance 4 — Read the licence on every paid plugin before buying

- **Guidance:** Treat the marketplace front page as not stating licence terms and ask the author about multi-server use and redistribution.
- **Evidence basis:** Codefling's front page gave no licence terms [12].
- **Confidence:** Low. Absence of terms on one page is weak evidence about the whole marketplace.
- **So what:** Avoid unintended licence breaches when running several servers.

# Open Questions

- Facepunch policy on modded servers: the wiki lists tags but gives no eligibility rule, and no opened Facepunch page states whether Oxide or Carbon servers must carry the Modded tag or how Official servers are defined [8]. A Facepunch server-hosting policy page would resolve this.
- uMod monetisation and licence rules: the uMod approval guide returned HTTP 403 and was not read, so norms for donations, paid plugins and licences are unverified.
- Oxide's own install and permission guide pages returned 404 or no detail, so command syntax is from a practitioner source [11].
- Whether Carbon release notes ever state supported Rust builds.

# References

**Primary Sources**

- [1] **CarbonCommunity** — *Carbon (GitHub README)*. https://github.com/CarbonCommunity/Carbon. Accessed 2026-10-08.
- [2] **CarbonCommunity** — *Latest release API: Production Build v2.0.262*. https://api.github.com/repos/CarbonCommunity/Carbon/releases/latest. Accessed 2026-10-08.
- [3] **OxideMod** — *Oxide.Rust (GitHub repository)*. https://github.com/OxideMod/Oxide.Rust. Accessed 2026-10-08.
- [4] **OxideMod** — *Oxide.Rust releases API (2.0.7810, 2.0.7801, 2.0.7788)*. https://api.github.com/repos/OxideMod/Oxide.Rust/releases. Accessed 2026-10-08.
- [5] **Carbon** — *Carbon for Rust (project site)*. https://carbonmod.gg/. Accessed 2026-10-08.
- [6] **Carbon** — *Installing Carbon*. https://carbonmod.gg/owners/installing-carbon. Accessed 2026-10-08.
- [7] **Facepunch Rust Wiki** — *Oxide*. https://wiki.facepunch.com/rust/oxide. Accessed 2026-10-08.
- [8] **Facepunch Rust Wiki** — *Server Browser Tags*. https://wiki.facepunch.com/rust/server-browser-tags. Accessed 2026-10-08.
- [9] **Facepunch** — *Community Update #13*. https://rust.facepunch.com/news/community-update-13. Accessed 2026-10-08.
- [10] **Oxide** — *Oxide documentation home*. https://docs.oxidemod.com/. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- [11] **Corrosion Hour** — *RUST uMod (Oxide) Permissions Guide*. https://www.corrosionhour.com/umod-permissions-guide/. Accessed 2026-10-08.
- [12] **Codefling** — *Rust plugins, maps and prefabs (marketplace front page)*. https://codefling.com/. Accessed 2026-10-08.

**Further Reading**

See the Further Reading section below.

# Further Reading

- Carbon owner documentation, including the Oxide porting page, via the Carbon site.
- Oxide Server Owners guides on docs.oxidemod.com.

# Related Documents

- rust-game-mechanics-foundation
- rust-items-crafting-foundation
- rust-building-raiding-foundation
- rust-server-administration-foundation
- rust-updates-meta-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, 100% links live). | Auto-approve mandate |
