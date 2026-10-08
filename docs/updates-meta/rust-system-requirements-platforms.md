---
id: rust-system-requirements-platforms
title: "Rust System Requirements and Platforms"
version: 1.0.0
status: frozen
confidence: Medium
category: Game Updates & Meta
topic: "PC requirements, platforms and editions"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-updates-meta-foundation, rust-moderation-anti-cheat, rust-server-convars-reference, rust-server-performance, rust-update-timeline-2026, rust-game-modes]
tags: [system-requirements, platforms, windows, macos, linux, console, secure-boot, tpm, steam]
game_build_checked: "October 2026 update (Livestock Update, 1 Oct 2026)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-system-requirements-platforms |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Game Updates & Meta |
| Region | Global |
| Game build checked | October 2026 update (Livestock Update, 1 Oct 2026) |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This document records what Facepunch and Double Eleven publish about what hardware and platforms Rust runs on: the Steam store minimum and recommended specifications for Windows and macOS, the stated status of Linux, the TPM and Secure Boot requirement that servers can opt in to, and the console edition as a separate product.

Document-level confidence is Medium. The specifications come from the Steam page and the Facepunch wiki, both first-party, but the Steam page was read through a summarising fetch tool, the wiki page is marked as long out of date, and the TPM and Secure Boot rollout beyond opt-in servers has no dated global requirement in any source opened.

# Key Facts

- The Steam page lists a Windows minimum of Windows 11 64-bit, Ryzen 5 1400 or Core i5-6600, 12 GB RAM, GTX 1060 / RX 470 / Arc A580, DirectX 11 and 45 GB storage [1].
- The recommended Windows spec is Ryzen 7 3700X or i7-6700K, 16 GB RAM, RTX 3060 / RX 6600 XT / Arc B580, DirectX 12, with an SSD required [1].
- macOS minimum and recommended specs are listed separately and require an Apple M1 (recommended M1 Pro, Max or Ultra) and macOS Monterey (12) [1].
- The Steam page lists no Linux requirements, and the Facepunch wiki says the game is not natively supported on Linux [1][2].
- Servers can require TPM and Secure Boot; as of Spring Clean (2 Apr 2026) Facepunch said only about 60% of players had the features enabled [3][4].
- Facepunch states its end goal is to make the requirement global, with no date given [3][5].
- Rust Console Edition is developed and published by Double Eleven for PS5 and Xbox Series X|S, with no cross-platform progress transfer [6].

# Scope

Covers the PC client (Steam, Windows and macOS), Linux client status, the TPM and Secure Boot requirement for connecting to secure servers, and the console edition as a separate product. Build checked: October 2026 update. Dedicated-server hardware is covered in rust-server-performance; anti-cheat and server-side convars in rust-moderation-anti-cheat and rust-server-convars-reference. Console gameplay and wipes are only noted where they differ in product terms.

# Definitions

- **TPM 2.0:** a hardware or firmware security module; Facepunch's devblogs refer to "TPM and Secure Boot" and "TPM 2.0" [3][4].
- **Secure Boot:** a firmware setting; Facepunch describes the requirement as applying to Windows PCs [3].
- **Secure tag:** server-browser tag shown on servers that require TPM and Secure Boot for every player [3].
- **Console Edition:** the PS5 and Xbox Series X|S version, developed and published by Double Eleven [6].

# Core Mechanics

**PC specification.** The Steam page lists separate Windows and macOS requirement blocks. Windows is "64-bit processor and operating system" required, with an SSD "highly recommended" at minimum and "required" at recommended [1]. The Facepunch wiki's installation page repeats the same Windows figures and recommends verifying game files through Steam if files are corrupt [2].

**Operating systems.** The Steam page lists Windows and macOS requirement tabs and no Linux tab [1]. The wiki states "Rust is currently available for Windows and macOS" and "The game is not natively supported on Linux at this time" [2]. Rust is sold exclusively through Steam per the wiki [2]. The Steam page also states the game uses kernel-level anti-cheat (Easy Anti-Cheat) and needs agreement to a third-party EULA [1].

**TPM and Secure Boot.** The Shipshape devblog (5 Mar 2026) introduced the option for servers to require TPM and Secure Boot; a server-wide convar enforces it for everyone and earns the Secure tag, while a per-player convar does not add the tag [3]. The post gave adoption as over 80% with TPM hardware and just under 60% with Secure Boot enabled, said players can check compatibility with Windows commands, and said hardware from roughly the last eight years is likely to support it [3]. Spring Clean reported about 1 cheater per 63 players on the six secure servers against 1 per 42 on regular servers, and about 60% of players with the features enabled, and said Facepunch did not want to alienate players [4]. Livestock (1 Oct 2026) said servers were introduced in March, strongly recommended enabling the features if hardware supports them, and described a reduced cheater presence [5]. Only Windows is discussed; the posts say nothing about Linux or Mac [3][5].

**Console edition.** Double Eleven's FAQ says the edition is available for PlayStation 5 and Xbox Series X|S, is published and developed by Double Eleven, has no physical copies, and does not support cross-platform progress transfer [6]. Its wipe schedule is separate from PC: weekly servers wipe Thursdays 6 PM UTC and monthly servers on the last Thursday of the month at 6 PM UTC [6].

# Reference Data

Steam store requirements, checked 2026-10-08 against the October 2026 update [1].

| Item | Windows minimum | Windows recommended |
|------|-----------------|---------------------|
| OS | Windows 11 64-bit [1] | Windows 11 64-bit [1] |
| CPU | AMD Ryzen 5 1400 or Intel Core i5-6600 [1] | AMD Ryzen 7 3700X or Intel Core i7-6700K [1] |
| RAM | 12 GB [1] | 16 GB [1] |
| GPU | Radeon RX 470, GeForce GTX 1060 or Intel Arc A580 [1] | Radeon RX 6600 XT, GeForce RTX 3060 or Intel Arc B580 [1] |
| DirectX | 11 [1] | 12 [1] |
| Storage | 45 GB [1] | 45 GB, SSD required [1] |

| Item | macOS minimum | macOS recommended |
|------|---------------|-------------------|
| OS | macOS Monterey (12) [1] | macOS Monterey (12) [1] |
| CPU / GPU | Apple M1 [1] | Apple M1 Pro / Max / Ultra [1] |
| RAM | 12 GB [1] | 16 GB [1] |
| Storage | 45 GB [1] | 45 GB [1] |

| Platform | Status | Source |
|----------|--------|--------|
| Windows | Supported | [1][2] |
| macOS | Supported | [1][2] |
| Linux (client) | No requirements listed; not natively supported | [1][2] |
| PS5, Xbox Series X/S | Separate Console Edition by Double Eleven | [6] |

| TPM / Secure Boot datapoint | Value | Source |
|-----------------------------|-------|--------|
| Players with TPM hardware | over 80% (5 Mar 2026) | [3] |
| Players with Secure Boot enabled | just under 60% (5 Mar 2026) | [3] |
| Players with the features enabled | about 60% (2 Apr 2026) | [4] |
| Cheaters, secure vs regular servers | about 1 in 63 vs 1 in 42 | [4] |

# Version & Patch Notes

- 5 Mar 2026 (Shipshape): opt-in TPM and Secure Boot requirement for servers [3].
- 2 Apr 2026 (Spring Clean): secure-server results and adoption update [4].
- 4 Jun 2026 (Built Different): Unity 6 upgrade listed in the changelist; the known-issues note says Unity 6 changed mouse input processing and recommends a polling rate below 1000 Hz [7].
- 1 Oct 2026 (Livestock): Rust Render Pipeline migration with a toggle in the experimental tab for the first month; secure server expansion [5].
- Volatile: the specifications and the opt-in status may change with any monthly update.

# Common Pitfalls

- Assuming Linux is a supported client because Rust dedicated servers run on Linux; the wiki says the game client is not natively supported [2]. Server OS support is in rust-server-performance.
- Assuming the Secure Boot requirement is global; the sources describe it as opt-in per server or per player [3][4].
- Treating the wiki installation page as authoritative over the Steam page; the wiki page is marked "Updated: A Long Time Ago" [2].
- Assuming console shares PC wipes or progress; Console Edition has its own FAQ, schedule and no cross-progress transfer [6].

# Interactions & Related Systems

TPM and Secure Boot enforcement connects to the Easy Anti-Cheat context in rust-moderation-anti-cheat and the `server.use...RequiredSystemConfig` convars in rust-server-convars-reference. Update cadence and console history are in rust-updates-meta-foundation and rust-update-timeline-2026; mode differences in rust-game-modes.

# Assessed Guidance

## Guidance 1 — Check TPM and Secure Boot before joining secure-tagged servers

- **Guidance:** Players with supported hardware should enable TPM and Secure Boot, since a share of servers can refuse connections without them.
- **Evidence basis:** Opt-in server enforcement and the Secure tag [3]; Facepunch's strong recommendation to enable [5].
- **Confidence:** High. Stated directly by Facepunch in two devblogs.
- **So what:** Missing firmware settings can lock a player out of secure servers; hardware roughly eight years old or newer is likely to qualify [3].

## Guidance 2 — Treat the minimum spec as a floor and buy to the recommended one

- **Guidance:** Aim for the recommended Windows spec with an SSD for comfortable play.
- **Evidence basis:** Minimum and recommended figures and SSD wording [1][2].
- **Confidence:** Medium. The figures are first-party but real performance depends on settings and map, which no source quantifies.
- **So what:** 12 GB RAM and a GTX 1060 class card are the stated floor; expect longer loads without an SSD [1].

## Guidance 3 — Linux players should not rely on official client support

- **Guidance:** Assume no official Linux client support.
- **Evidence basis:** No Linux requirements on Steam and the wiki statement [1][2].
- **Confidence:** Medium. Absence of a listing is inferred, and compatibility-layer behaviour was not investigated.
- **So what:** Players on Linux should expect no first-party help and should check anti-cheat behaviour themselves.

# Open Questions

- Facepunch's support article on enabling TPM and Secure Boot returned HTTP 403 and was not read; its wording, including any phase-two global rollout date, is unverified.
- No devblog opened gives a date for a global Secure Boot and TPM requirement [3][4][5].
- The Steam page was read via a summarising tool; platform icons and any Linux or Steam Deck notes were not confirmed.
- Whether Windows 10 still runs the game is not stated; the specs list only Windows 11.
- Console history dates (2021 launch, 2025 PS5/Xbox Series X|S release, PS4/Xbox One delisting) are only secondary in the KB (see rust-updates-meta-foundation) and were not verified from Double Eleven here.
- The Double Eleven FAQ was cited from a version that redirected from /faqs to /faq; an alternative version reportedly limits Public Test Branch access to higher editions.

# References

**Primary Sources**

- [1] **Steam** — *Rust on Steam, System Requirements*. https://store.steampowered.com/app/252490/Rust/. Accessed 2026-10-08.
- [2] **Facepunch Rust Wiki** — *Buying and Installing Rust*. https://wiki.facepunch.com/rust/Purchase-and-Installation. Accessed 2026-10-08.
- [3] **Facepunch** — *Shipshape (5 Mar 2026)*. https://rust.facepunch.com/news/shipshape. Accessed 2026-10-08.
- [4] **Facepunch** — *Spring Clean (2 Apr 2026)*. https://rust.facepunch.com/news/spring-clean. Accessed 2026-10-08.
- [5] **Facepunch** — *Livestock Update (1 Oct 2026)*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [6] **Double Eleven** — *Rust Console Edition FAQ*. http://rust.double11.com/faq. Accessed 2026-10-08.
- [7] **Facepunch** — *Built Different (4 Jun 2026)*. https://rust.facepunch.com/news/built-different. Accessed 2026-10-08.

**Community & Practitioner Evidence**

None.

**Further Reading**

None.

# Further Reading

Facepunch news index for the latest devblog: https://rust.facepunch.com/news.

# Related Documents

- rust-updates-meta-foundation
- rust-moderation-anti-cheat
- rust-server-convars-reference
- rust-server-performance
- rust-update-timeline-2026
- rust-game-modes

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
