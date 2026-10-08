---
id: rust-plugin-marketplaces
title: "Rust Plugin Marketplaces and Licensing"
version: 1.0.0
status: frozen
confidence: Low
category: Modding & Plugins
topic: "Plugin sources, licences and marketplaces"
market: "Global"
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-modding-plugins-foundation, rust-carbon-vs-oxide, rust-plugin-development-hooks, rust-server-administration-foundation, rust-updates-meta-foundation, rust-server-permissions-rcon, rust-moderation-anti-cheat, rust-server-monetisation-guidelines]
tags: [codefling, umod, marketplace, licence, refunds, warranty, plugins, supply-chain]
game_build_checked: "Livestock update (1 Oct 2026); Rust 2634.289.1 hotfix era. Marketplace policy pages read 2026-10-08 (policies are not tied to a Rust build)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-plugin-marketplaces |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Low |
| Category | Modding & Plugins |
| Region | Global |
| Game build checked | Livestock update (1 Oct 2026); marketplace policies read 2026-10-08 |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This document goes deeper than the modding foundation on where Rust server plugins come from and on what the marketplaces themselves say about licences, payment, refunds, support and review. The best-documented marketplace is Codefling: its own policy pages state refund, warranty, creator-obligation and curation rules [2][3][4][5][6]. The uMod site, the long-standing free plugin directory, returned HTTP 403 to every direct fetch, so uMod's approval, licence and monetisation rules could not be verified here. This is not legal advice.

Confidence is Low. Codefling claims rest on first-party policy pages and are solid for that one site, but uMod is unread, the other paid sites could not be characterised from their own pages, and the only independent view of the wider market is a single hosting-provider guide. This document does not claim that any named marketplace has hosted a malicious plugin; it records only what named sources say about review and risk.

# Key Facts

- Codefling states that creators must make their product licence available before purchase and state limits such as server counts, modifications and redistribution [4].
- Codefling's refund policy says digital purchases are "generally final once a download has been completed", with exceptions for significant unresolved defects, material differences from the description and duplicate or incorrect charges [3].
- Every Codefling file carries a six-month warranty from purchase; Codefling+ purchases get two further years, 30 months in total [5].
- Codefling creators must provide updates and support for paid content for at least six months after first sale [4].
- Codefling's upload guidelines require creators to choose a licence they have the right to apply, forbid DRM, remote kill switches, silent update checks and hidden commands, and say creators handle refund inquiries [16].
- Codefling curators check submissions for malware, harmful code and security issues, but state that approval "is not a guarantee that every defect or risk has been found" [6].
- Oxide's developer guidelines tell plugin authors not to include backdoors, spyware, intentional memory leaks or data miners, and to keep plugins updated after Oxide and game updates [8].
- A hosting provider's 2026 guide lists most free plugins as coming from uMod, and lists paid items from Codefling and chaoscode.io [10].
- Plugins cover the Oxide and Carbon frameworks, which are licensed MIT and GPL-3.0 respectively; those licences cover the frameworks, not individual plugins [11][12].

# Scope

Covered: where plugins are obtained, what the opened marketplace policy pages say about licences, payment, refunds, warranty, support, updates and review, and risks only as documented by named sources. Server-owner view, PC dedicated servers running Oxide or Carbon. Not covered: legal advice or interpretation of any licence, plugin quality reviews, writing plugins (see rust-plugin-development-hooks), the framework comparison (see rust-carbon-vs-oxide), and how a server may charge players (see rust-server-monetisation-guidelines). Policies were read on 2026-10-08 and can change without a Rust patch.

# Definitions

- **Marketplace:** a site where creators list plugins, maps or tools for sale or download. Codefling describes its role as letting creators monetise their work [2].
- **Curation:** Codefling's review of submitted files against its upload guidelines [6].
- **Warranty (Codefling):** a time-limited promise covering significant defects that stop a file performing its advertised functions [5].
- **Product licence:** the creator's own terms for a listing, which Codefling requires to be visible before purchase [4].

# Core Mechanics

**Plugin sources.** A hosting-provider guide published in 2026 sorts popular plugins by source: free plugins such as Vanish, Rust Kits and Gather Manager from uMod; ZombieHorde at $10 from chaoscode.io; and Raidable Bases split into a free base version on uMod and paid premium and prefab base packs on Codefling [10]. That guide calls uMod "the official home of the Oxide ecosystem" and is sold alongside server hosting, so it is not a neutral source [10]. A request to chaoscode.io returned a permanent redirect to rusthq.com, a page titled "RustHQ - Rust Marketplace & Community"; nothing further was readable [13].

**Codefling listing model.** Codefling's front page lists plugins, maps, monuments, prefabs, bases, tools, Discord bots and graphics; each listing shows a price or free marker, seller and rating, and notes dependencies such as Oxide or Carbon [1]. Support is commonly routed to the seller, often via the seller's Discord [1]. A Raid Limits listing carries a "sold as is" wording, showing sellers can attach their own terms [1].

**Licences.** Codefling's registration terms do not set licence terms [7]. Its creator terms require each creator to publish a licence before purchase and state limits on use; licence changes apply only to future purchases, and withdrawing a product or closing an account does not cancel existing buyer licences [4]. Its curation policy tells buyers to check the licence themselves and does not list licence review as a curator check [6]. Creators keep ownership and grant Codefling a non-exclusive licence to host, distribute and promote the content [4].

**Payment and creator rules.** Codefling deducts a sales fee before crediting a creator wallet, but the creator page does not state the percentage; payouts are requested, not automatic, and may be delayed for identity checks, fraud investigation, refunds or chargebacks [4]. Creators must not offer content cheaper elsewhere and must not steer Codefling buyers to buy elsewhere [4].

**Refunds.** Undownloaded purchases are not automatically refundable; after download, refunds may be considered for significant unresolved defects, material differences from the description, duplicate or incorrect charges, or exceptional circumstances; change of mind normally does not qualify [3]. No fixed refund window in days is stated [3]. A refund does not authorise redistribution [3].

**Warranty and support.** The warranty runs six months from purchase, extends to 30 months for purchases made under an active Codefling+ subscription, and continues if the author leaves or stops supporting the file [5]. Buyers contact the author first, then submit a claim if there is no response, the issue stays unresolved or the file appears abandoned [5]. Codefling may assign a new maintainer to an abandoned file, with future proceeds going to that maintainer [4]. Creators must provide updates and support for at least six months after first sale [4].

**Upload guidelines.** Codefling's upload guidelines tell creators to choose a licence they have the right to apply, make its terms available and follow third-party licences; forks need significant changes [16]. Files must not require external licence keys or activation servers, and analytics, tracking, silent update checks and remote kill switches are prohibited [16]. Destructive actions must be documented and need server-owner confirmation, no backdoors or hidden commands are allowed, reviewers may request source code, and mostly AI-generated files are generally not accepted [16]. Creators must list dependencies and extra costs before purchase and are responsible for support and refund inquiries [16].

**Review and removal.** Curators look for malware, harmful code and security issues and test whether a file works as described; some trusted creators can publish before review finishes; a badge shows whether a file has been reviewed [6]. Later versions and later changes to the game, frameworks or dependencies are not covered by an earlier review [6]. A file deemed unacceptable is removed and pre-curation buyers are refunded, but removal does not remove the file from a buyer's server [6].

**Service listings.** Codefling also lists custom-development services. Its page says it does not evaluate, test or guarantee external providers and will not intervene in disputes between customer and provider [9]. One example listing excludes unauthorised code changes and third-party plugin issues from support [9].

**Disclaimer.** Codefling advises users to read instructions and back up data and configuration before installing or updating files, and limits its responsibility for third-party content to the extent permitted by law [14].

**Authoring norms from the framework.** Oxide's plugin guidelines say developers should avoid code that could harm the server or players, including backdoors, spyware, intentional memory leaks and data miners, and should tell users if adapting to an update will take time [8]. Its best-practice guide advises validating input and keeping dependencies updated, and says nothing on plugin licensing [15].

# Reference Data

Codefling policy summary, all read 2026-10-08 and subject to change [3][4][5][6]:

| Topic | What the page says | Source |
|-------|--------------------|--------|
| Refund after download | Generally final; exceptions for defects, mismatch, duplicate charge | [3] |
| Refund window | Not stated as a number of days | [3] |
| Warranty | 6 months from purchase; 30 months with Codefling+ at purchase | [5] |
| Creator support duty | At least 6 months after first sale | [4] |
| Licence disclosure | Required before purchase, including server count, modification and redistribution limits | [4] |
| Sales fee | Deducted, percentage not stated | [4] |
| Payout | Requested by creator; no withdrawal fee | [4] |
| Upload rules | Own licence disclosed; no DRM, kill switches or silent update checks; dependencies and extra costs listed | [16] |
| Curation checks | Malware, harmful code, security, works as described; licence not listed | [6] |
| Disputes with service providers | Codefling will not intervene | [9] |

Framework licences (not plugin licences): Oxide.Rust MIT, Carbon repository GPL-3.0 per its LICENSE file [11][12].

Example sources and prices in one 2026 hosting guide: ZombieHorde $10 (chaoscode.io, last updated 05.03.2026); Raidable Bases prefab packs $20 (Tier 1) and $50 (Tier 2) on Codefling [10]. Prices are guide-reported, not checked on the sellers' pages.

# Version & Patch Notes

- Marketplace policies are not versioned with Rust. The Codefling pages read carry no dated change log in the text retrieved [3][4][5][6]. Codefling reserves the right to modify its registration terms at any time [7].
- Oxide's guidelines state that Oxide and game updates can break plugins [8]; the foundation records a framework patch following a Rust hotfix (see rust-modding-plugins-foundation). Curation does not carry forward to later game or framework changes [6].
- Latest Rust update checked: Livestock, 1 Oct 2026 (see rust-update-timeline-2026).

# Common Pitfalls

- Assuming curation is a safety guarantee: Codefling says approval is not a guarantee, and later versions are not covered [6].
- Assuming a refund is available after download: the policy says generally final [3].
- Assuming the framework licence covers a plugin: the MIT and GPL files are repository licences for the frameworks [11][12]; the plugin's own licence must be read on its listing [4][6].
- Assuming removal from a marketplace removes the file from your server: it does not [6].
- Treating one hosting provider's plugin list as neutral: the guide is from a seller of servers [10].
- Antivirus alerts on framework downloads appear in uMod forum threads, but this document could not open them (see Open Questions).

# Interactions & Related Systems

Plugin trust is part of server administration (rust-server-administration-foundation) and permissions (rust-server-permissions-rcon), because a plugin runs with the server's access. Frameworks and compatibility are in rust-modding-plugins-foundation and rust-carbon-vs-oxide; authoring detail is in rust-plugin-development-hooks. Anti-cheat and moderation context is in rust-moderation-anti-cheat. Selling items or ranks to players is a separate question, treated in rust-server-monetisation-guidelines. Rust updates that break plugins are tracked in rust-updates-meta-foundation.

# Assessed Guidance

## Guidance 1 — Read the creator's licence on the listing before buying, because curation does not check it

- **Guidance:** Before paying for a plugin, read the product licence on the listing and ask the creator about multi-server use, modification and redistribution if the licence is silent.
- **Evidence basis:** Creators must disclose licence limits before purchase [4]; the curation policy does not list licence review and tells buyers to check [6].
- **Confidence:** Medium. Both statements are first-party policy text, but they describe one marketplace only.
- **So what:** Keep a record of the licence text at the time of purchase, since changes apply only to future purchases [4].

## Guidance 2 — Test downloads on staging and keep backups, because review is not a guarantee

- **Guidance:** Install new or updated plugins on a staging server first and back up data and configuration, regardless of marketplace badges.
- **Evidence basis:** Codefling says approval is not a guarantee and does not cover later versions [6]; it advises backups before installing [14]; Oxide warns that updates can break plugins [8].
- **Confidence:** Medium. The reasoning is straightforward but the sources are vendor statements; no named incident is cited here.
- **So what:** A removed or flagged file can still be on your server, so you may need to undo its changes yourself [6].

## Guidance 3 — Claim refunds or warranty early and through the right channel

- **Guidance:** Report defects soon after purchase, contact the author first, and only then use the warranty claim route.
- **Evidence basis:** Refund policy asks for prompt contact [3]; the warranty runs from purchase date and requires author contact first [5].
- **Confidence:** Medium. Written procedure from one marketplace; outcomes in practice are not evidenced.
- **So what:** Collect version, errors and reproduction steps before the six months lapse [5].

## Guidance 4 — Do not generalise Codefling terms to other sites

- **Guidance:** Treat each marketplace as having its own refund, licence and support terms, and read them separately.
- **Evidence basis:** Codefling's rules are specific to its pages [3][4][5]; the other sources found give no comparable terms [10][13].
- **Confidence:** Low. This rests on absence of evidence for sites that could not be read.
- **So what:** Ask the seller for written terms when buying outside Codefling.

# Open Questions

- uMod approval, licence and monetisation rules: umod.org returned HTTP 403 to every fetch attempted, in both passes (home, plugins, terms, approval guide, community threads). The foundation's open question on uMod licence and monetisation norms therefore remains unresolved. Search-result snippets mentioned an approval guide requiring a permissive open-source licence and forum threads on paid plugins, but those pages were not opened and are not cited.
- Whether the Oxide documentation has a community guidelines page covering licensing: the plugin-guidelines and best-practices pages opened do not [8][15].
- Codefling's sales fee percentage: the Creator Terms page (re-read on a second pass) and the upload guidelines [16] both say a fee is deducted without giving a number [4][16].
- Second-pass attempts on uMod: web.archive.org snapshots could not be fetched at all in this environment, and umod.org approval-guide and forum URLs again returned HTTP 403. The Oxide plugin-guidelines page carries only an MIT footer and nothing on paid plugins or approval [8]. A web search snippet (not an opened page) says uMod's approval guide requires an open-source licence, but this is uncited here and unverified.
- Terms for chaoscode.io, now redirecting to rusthq.com, and other paid sites: nothing readable [13].
- Whether any named marketplace has published an incident report about a malicious plugin: none opened.
- Whether Facepunch states any policy on third-party plugin sales: not researched in a source opened for this document.

# References

**Primary Sources**

- [1] **Codefling** — *Marketplace front page*. https://codefling.com/. Accessed 2026-10-08.
- [2] **Codefling** — *Legal index*. https://codefling.com/legal. Accessed 2026-10-08.
- [3] **Codefling** — *Refund Policy*. https://codefling.com/refunds. Accessed 2026-10-08.
- [4] **Codefling** — *Creator Terms*. https://codefling.com/creator. Accessed 2026-10-08.
- [5] **Codefling** — *Warranty Terms*. https://codefling.com/warranty. Accessed 2026-10-08.
- [6] **Codefling** — *Curation policy*. https://codefling.com/curation. Accessed 2026-10-08.
- [7] **Codefling** — *Registration Terms*. https://codefling.com/terms. Accessed 2026-10-08.
- [8] **Oxide** — *Plugin guidelines*. https://docs.oxidemod.com/guides/developers/plugin-guidelines. Accessed 2026-10-08.
- [9] **Codefling** — *Custom Rust plugin development service listing*. https://codefling.com/services/record/125-custom-rust-plugin-development-server-setup-support/. Accessed 2026-10-08.
- [11] **CarbonCommunity** — *Carbon LICENSE file (GPL-3.0)*. https://raw.githubusercontent.com/CarbonCommunity/Carbon/main/LICENSE. Accessed 2026-10-08.
- [12] **OxideMod** — *Oxide.Rust repository (MIT per GitHub)*. https://github.com/OxideMod/Oxide.Rust. Accessed 2026-10-08.
- [14] **Codefling** — *Disclaimer*. https://codefling.com/disclaimer. Accessed 2026-10-08.
- [15] **Oxide** — *Best practices*. https://docs.oxidemod.com/guides/developers/best-practices. Accessed 2026-10-08.
- [16] **Codefling** — *Upload Guidelines*. https://codefling.com/upload-guidelines. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- [10] **RespawnHost** — *Rust best plugins 2026*. https://respawnhost.com/de/wiki/games/rust/rust-best-plugins-2026/. Accessed 2026-10-08.
- [13] **RustHQ** — *RustHQ - Rust Marketplace & Community (redirect target of chaoscode.io)*. https://rusthq.com/. Accessed 2026-10-08.

**Further Reading**

See the Further Reading section below.

# Further Reading

- The uMod approval guide and community guidelines on umod.org, which could not be opened here.
- Codefling's Help Center and Support Center linked from its front page.

# Related Documents

- rust-modding-plugins-foundation
- rust-carbon-vs-oxide
- rust-plugin-development-hooks
- rust-server-administration-foundation
- rust-server-permissions-rcon
- rust-moderation-anti-cheat
- rust-updates-meta-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft; revision pass added Codefling upload guidelines [16], re-checked fee and uMod access. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen at Low confidence after a second research pass; core figures remain community or third-party sourced and are labelled as such. | Auto-approve mandate |
