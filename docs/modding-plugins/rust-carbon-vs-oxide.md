---
id: rust-carbon-vs-oxide
title: "Rust Carbon versus Oxide"
version: 1.0.0
status: frozen
confidence: Medium
category: Modding & Plugins
topic: "Carbon versus Oxide comparison"
market: "Global"
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-modding-plugins-foundation, rust-game-mechanics-foundation, rust-items-crafting-foundation, rust-building-raiding-foundation, rust-server-administration-foundation, rust-updates-meta-foundation, rust-combat-damage-model, rust-weapons-ammo, rust-raiding-costs-defence, rust-server-convars-reference, rust-plugin-development-hooks, rust-update-timeline-2026, rust-monuments-loot, rust-farming-food, rust-vehicles, rust-wipes-map-generation, rust-moderation-anti-cheat]
tags: [oxide, carbon, umod, comparison, harmony, licence, release-cadence]
game_build_checked: "Livestock update (1 Oct 2026); Rust 2634.289.1 hotfix named in Oxide.Rust 2.0.7801; Oxide.Rust 2.0.7810 and Carbon Production Build v2.0.262 checked 2026-10-08"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-carbon-vs-oxide |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Modding & Plugins |
| Region | Global |
| Game build checked | Livestock (1 Oct 2026); Oxide.Rust 2.0.7810; Carbon Production Build v2.0.262 |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This document compares the two live Rust server frameworks, Oxide (uMod) and Carbon, on licence, installation, Oxide-plugin compatibility, performance claims, tags, maintenance status and release cadence. It goes deeper than the foundation document and uses only first-party pages: project sites, GitHub repositories, the GitHub release and repository APIs, and the Facepunch wiki.

Headline findings as of 2026-10-08: both repositories are unarchived and were pushed to within the last day or so of the check [11][12]; Oxide.Rust is MIT-licensed and Carbon's repository is GPL-3.0, although Carbon's own website says MIT [1][3][6][14]; all performance and compatibility advantages are vendor claims with no benchmark on any page opened [1][3][9]. Confidence is Medium: facts are primary-sourced, but Oxide's own install guide could not be opened and no independent benchmark exists in the sources.

# Key Facts

- Oxide.Rust's repository licence is MIT (GitHub API spdx id MIT) [6][12]. Carbon's repository licence is GPL-3.0 (API and LICENSE file) [1][11][14].
- Carbon's website says "Released under the MIT License", which contradicts the repository's GPL-3.0 licence file; this is unresolved [3][14].
- The two cannot run on the same install: Oxide ships pre-patched Facepunch DLLs while Carbon patches DLLs at runtime, so vanilla DLLs must be restored before migrating [5].
- Carbon's migration page says Oxide `o.` commands become `c.`, and that config, data, lang and user/group files are copied automatically on first start [5].
- Oxide shipped 12 releases between 2026-08-28 and 2026-10-07 (the 12 newest returned by the API) and several are labelled as patches for named Rust updates or hotfixes [7].
- Carbon's README says its production build "gets updated twice times a month" (vendor claim); its release list holds one rolling production tag, published 2026-10-02 [1][2].
- Facepunch's wiki lists `Oxide` (code `o`) and `Carbon` (code `y`) as separate server browser tags [10].
- No opened page contains a measured benchmark comparing the two *(assessed: absence of evidence in these sources only)* [1][3][9].

# Scope

Covered: Oxide.Rust and Carbon on PC Rust dedicated servers, as of Rust's Livestock update (1 Oct 2026) and the framework versions named above. Not covered: plugin development (see rust-plugin-development-hooks), individual plugins, permission command syntax (see rust-modding-plugins-foundation), console, client-side modding. Install steps are summarised from the pages that could be opened; Oxide's own install guide URL returned 404.

# Definitions

- **Oxide / uMod:** the long-running Rust modding framework; the Oxide.Rust repository is the "Rust game extension for the Oxide modding framework" [6].
- **Carbon:** an alternative framework describing itself as a drop-in Oxide replacement [3].
- **Harmony:** the C# runtime patching library both frameworks list as supported (Harmony 2.0) [5].
- **Dynamic hook loading:** Carbon's stated behaviour of activating only the hooks plugins use [3][5].
- **Rolling release tag:** a GitHub release whose tag name stays fixed (for example `production_build`) while its contents are replaced, so tag history does not show cadence [2].

# Core Mechanics

**Installation, Oxide.** Per the Facepunch wiki: download the latest Oxide installer from the Oxide website, stop the server, run the installer, start the server; the `oxide` console command then opens the Oxide console where plugins and Oxide updates are managed [8]. Oxide's documentation home points to Server Owners and Core Documentation sections, but this check did not read an install guide [13].

**Installation, Carbon (Windows).** Download `Carbon.Windows.TARGET.zip` from the GitHub Releases page, extract it to the server root containing `RustDedicated.exe` keeping the folder structure and overwriting as needed, then start the server; TARGET is Release or Debug depending on the build branch [4]. The page asks that server files be verified and the server kept up to date at every boot [4]. The repository also mentions a quick-start script for Windows and Linux [1]. Linux and OSX tabs exist but their content was not captured [4].

**Compatibility.** Carbon states it is fully compatible with Oxide and keeps the folder and plugin structure [1][3]. Its porting page states the two cannot coexist, that Oxide's pre-patched DLLs must be replaced with vanilla ones through a SteamCMD `validate` before Carbon is extracted, and that both use Harmony 2.0 [5]. The Facepunch wiki's Carbon page repeats that Oxide plugins run without extra patches, but the page is undated ("Updated: A Long Time Ago") and carries no version numbers [9].

**Performance claims (vendor claims, not measurements).** Carbon's site says performance is "the number one factor", hooks load dynamically so only used hooks are active, and only essential hooks are provided [3]. The README says it uses the latest C# and Harmony "for the best performance and stability possible" [1]. The Facepunch wiki Carbon page claims Harmony micro-optimisations reduce CPU overhead and memory allocations [9]. None of these pages gives a benchmark or measured result [1][3][9]. No comparable performance claim for Oxide was found on the pages opened [6][8][13].

**Features Carbon claims over Oxide.** Carbon's porting page tabulates dynamic patching, self-updating, remote hook updates on boot, a built-in profiler, SQLite permissions and "regular updates" as Carbon-only, with Harmony 2.0 and "regularly maintained" shared [5]. This table is Carbon's own, so the Oxide column is a competitor's statement; the "regular updates" row is contradicted for Oxide by its release history below [5][7].

# Reference Data

Side by side, checked 2026-10-08 (all rows from first-party pages):

| Item | Oxide.Rust | Carbon |
|------|------------|--------|
| Repository licence (API) | MIT [12] | GPL-3.0 [11] |
| Licence per project website | Not read (uMod pages returned 403) | "Released under the MIT License" [3] |
| Licence file | MIT text, copyright 2013-2020 Oxide Team and Contributors [6] | GNU GPL version 3 [14] |
| Repo created | 2017-06-17 [12] | 2022-08-27 [11] |
| Last push seen | 2026-10-07T09:50:58Z [12] | 2026-10-07T23:32:45Z [11] |
| Archived | No [12] | No [11] |
| Stars / open issues (API) | 387 / 8 [12] | 105 / 1 [11] |
| Default branch | develop [12] | main [11] |
| Install | Installer from Oxide website [8] | Zip from GitHub Releases into server root [4] |
| Console command prefix | `o.` [5] | `c.` [5] |
| Server browser tag / code | Oxide / `o` [10] | Carbon / `y` [10] |
| GitHub topics | modding, oxide, playrust, rust, steam, unity, unity3d [6] | framework, game-modding, harmony, oxide, oxidemod, platform, rust-modding [1] |

Latest releases seen 2026-10-08:

| Framework | Release | Published (UTC) | Pre-release flag | Note |
|-----------|---------|-----------------|------------------|------|
| Oxide.Rust | 2.0.7810 | 2026-10-07 09:50 | No | No itemised changes [7] |
| Oxide.Rust | 2.0.7801 | 2026-10-02 22:18 | No | Patches an October 2nd Rust hotfix; adds NPC-targeting hook for wildlife and boat AI [7] |
| Oxide.Rust | 2.0.7783 | 2026-10-01 17:33 | No | Patches the October 1st Rust update [7] |
| Carbon | Production Build v2.0.262 | 2026-10-02 09:09 | No | Stable build from `production` [2] |
| Carbon | Edge Build v2.1.1285 | 2026-10-03 18:21 | Yes | Dev build from `main` [2] |
| Carbon | Rust (Release) Build v2.4.341 | 2026-10-03 11:09 | Yes | Manual, unstable dev build [2] |
| Carbon | Rust (Staging) Build v2.3.1481 | 2026-10-07 23:32 | Yes | Manual, unstable dev build [2] |

Carbon branch model, from its README: `main` (edge build updated on every commit), `experimental` (synced with main, updated manually and rarely), `production` (live release branch, stated to update twice a month excluding hotfixes), `rust_beta/staging` (tracks Rust staging, mostly for hooks), `rust_beta/aux01` and `aux02` (minimal support, "extremely unstable") [1].

# Version & Patch Notes

- Observed Oxide cadence: the 12 newest releases span 2026-08-28 (2.0.7638) to 2026-10-07 (2.0.7810), about 40 days, including 2.0.7676 (3 Sept, patching a September 3rd Rust update), 2.0.7716 (11 Sept), 2.0.7723 (17 Sept), 2.0.7726 (22 Sept), 2.0.7783 (1 Oct) and 2.0.7801 (2 Oct) [7]. Several release bodies name the Rust update or hotfix they patch, so Oxide ships a framework release to follow Rust updates [7].
- Observed Carbon cadence: the release list holds rolling tags (`production_build`, `edge_build`, `experimental_build`, `rustbeta_*`), so release frequency cannot be read from the tags; the experimental build was last published 2026-08-22 and aux01 on 2026-09-15 [2]. The README's "twice times a month" production cadence is a claim and was not verified against history [1]. The list returned was truncated after six releases, so more may exist [2].
- Carbon's production release (2 Oct) and Oxide's patches (1-2 Oct) both landed within a day or two of the Livestock update of 1 Oct 2026 [2][7]; Carbon's production body does not state a Rust build in the data read, unlike Oxide's [2][7].
- Volatile: every version number in this document changes at least monthly; re-check before relying on it.

# Common Pitfalls

- Treating the two as installable together: the porting page says running both breaks the server [5].
- Skipping the DLL restore when moving from Oxide to Carbon; vanilla DLLs must be restored with a SteamCMD `validate` first [5].
- Forgetting to change `o.` commands to `c.` in scripts and automation [5].
- Assuming "MIT" for Carbon from its website; the repository licence file is GPL-3.0, which has different redistribution obligations [3][14].
- Quoting Carbon's feature table as neutral: it is the vendor's own comparison [5].
- Relying on the Facepunch wiki Carbon page for current behaviour: it is undated and carries no versions [9].
- Using several tags from the same group: the wiki advises against specifying multiple tags from the same group on one server [10].

# Interactions & Related Systems

Both frameworks sit under the plugin layer covered in rust-plugin-development-hooks and the admin layer in rust-server-administration-foundation and rust-server-convars-reference (the `server.tags` convar sets the browser tag). Framework updates follow Rust releases tracked in rust-update-timeline-2026 and rust-updates-meta-foundation. New Rust systems gain hooks through framework releases; for example Oxide 2.0.7783 added livestock and growable-entity hooks after the 1 October update, relevant to rust-farming-food [7]. See rust-modding-plugins-foundation for permissions and plugin sourcing, and rust-moderation-anti-cheat for related server policy.

# Assessed Guidance

## Guidance 1 — Decide on licence obligations from the repository, not the website

- **Guidance:** If you redistribute or modify framework code, treat Carbon as GPL-3.0 (the repository and LICENSE file) and Oxide.Rust as MIT, and ask the Carbon maintainers about the website's MIT statement.
- **Evidence basis:** Repository API and LICENSE file versus website text [3][11][12][14].
- **Confidence:** Medium. The sources conflict and this document is not legal advice.
- **So what:** Hosting plugins on a server rarely involves redistributing the framework, but anyone bundling or forking it should resolve the conflict first.

## Guidance 2 — Treat performance claims as untested until measured on your own server

- **Guidance:** Do not choose Carbon for speed on the strength of its pages; run both on a staging copy of your plugin set and compare server frame time and memory.
- **Evidence basis:** Only vendor statements, with no benchmark in the opened pages [1][3][9].
- **Confidence:** Medium. The absence of benchmarks in the sources read is verifiable, but a benchmark may exist elsewhere.
- **So what:** Avoid a migration justified only by marketing copy.

## Guidance 3 — Plan migration as a rehearsed change with a rollback

- **Guidance:** Back up the server, rehearse the Oxide-to-Carbon move, keep the Oxide install copy, and update scripts from `o.` to `c.`.
- **Evidence basis:** Porting page steps and no-coexistence statement [5].
- **Confidence:** Medium. The steps are first-party, but the rollback advice is inference.
- **So what:** A failed first start leaves you able to restore the previous state before wipe day.

## Guidance 4 — Gate Rust updates on the framework release in either case

- **Guidance:** After each monthly Rust update, wait for the matching framework release (Oxide notes name the Rust update; for Carbon check the production build date) before updating the live server.
- **Evidence basis:** Oxide release notes naming Rust updates [7]; Carbon's production release dated within a day of Livestock [2].
- **Confidence:** Medium. Two observed release windows only.
- **So what:** Fewer broken hooks after a wipe-day update.

# Open Questions

- Which licence is correct for Carbon: the website says MIT, the repository says GPL-3.0 [3][14]. Resolution needs a statement from the Carbon maintainers.
- Real performance difference: no independent benchmark was found. A reproducible test on one plugin set would resolve it.
- Carbon production cadence: the README says twice a month, but rolling tags hide history; commit or workflow history would resolve it [1][2].
- Oxide's own install guide and the uMod site (403) were not read, so uMod licence and plugin-policy statements are unverified [13].
- Carbon's total release count: the API page read was truncated [2].
- Which Rust build Carbon v2.0.262 targets is not stated in the data read [2].

# References

**Primary Sources**

- [1] **CarbonCommunity** — *Carbon (GitHub repository README)*. https://github.com/CarbonCommunity/Carbon. Accessed 2026-10-08.
- [2] **CarbonCommunity** — *Carbon releases API*. https://api.github.com/repos/CarbonCommunity/Carbon/releases?per_page=12. Accessed 2026-10-08.
- [3] **Carbon** — *Carbon for Rust (project site)*. https://carbonmod.gg/. Accessed 2026-10-08.
- [4] **Carbon** — *Installing Carbon*. https://carbonmod.gg/owners/installing-carbon. Accessed 2026-10-08.
- [5] **Carbon** — *Oxide porting (compatibility, migration, feature differences)*. https://carbonmod.gg/owners/oxide-porting. Accessed 2026-10-08.
- [6] **OxideMod** — *Oxide.Rust (GitHub repository)*. https://github.com/OxideMod/Oxide.Rust. Accessed 2026-10-08.
- [7] **OxideMod** — *Oxide.Rust releases API*. https://api.github.com/repos/OxideMod/Oxide.Rust/releases?per_page=12. Accessed 2026-10-08.
- [8] **Facepunch Rust Wiki** — *Oxide*. https://wiki.facepunch.com/rust/oxide. Accessed 2026-10-08.
- [9] **Facepunch Rust Wiki** — *Carbon Modding Framework*. https://wiki.facepunch.com/rust/Carbon. Accessed 2026-10-08.
- [10] **Facepunch Rust Wiki** — *Server Browser Tags*. https://wiki.facepunch.com/rust/server-browser-tags. Accessed 2026-10-08.
- [11] **CarbonCommunity** — *Carbon repository API metadata*. https://api.github.com/repos/CarbonCommunity/Carbon. Accessed 2026-10-08.
- [12] **OxideMod** — *Oxide.Rust repository API metadata*. https://api.github.com/repos/OxideMod/Oxide.Rust. Accessed 2026-10-08.
- [13] **Oxide** — *Oxide documentation home*. https://docs.oxidemod.com/. Accessed 2026-10-08.
- [14] **CarbonCommunity** — *Carbon LICENSE file (GPL-3.0)*. https://raw.githubusercontent.com/CarbonCommunity/Carbon/main/LICENSE. Accessed 2026-10-08.

**Community & Practitioner Evidence**

None used; this comparison deliberately relies on first-party pages.

**Further Reading**

See the Further Reading section below.

# Further Reading

- Carbon owner documentation and hook reference at docs.carbonmod.gg.
- Oxide Server Owners guides on docs.oxidemod.com.
- rust-modding-plugins-foundation for permissions and plugin marketplaces.

# Related Documents

- rust-modding-plugins-foundation
- rust-plugin-development-hooks
- rust-server-administration-foundation
- rust-server-convars-reference
- rust-update-timeline-2026
- rust-updates-meta-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
