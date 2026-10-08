---
id: rust-server-monetisation-guidelines
title: "Rust Server Monetisation and Hosting Guidelines"
version: 1.0.0
status: frozen
confidence: Medium
category: Server Administration
topic: "Facepunch community server guidelines"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-server-administration-foundation, rust-skins-cosmetics, rust-moderation-anti-cheat, rust-modding-plugins-foundation, rust-economy-trading, rust-server-permissions-rcon, rust-carbon-vs-oxide, rust-updates-meta-foundation]
tags: [monetisation, guidelines, dlc, donations, sanctions, hosting]
game_build_checked: "October 2026 update (Livestock Update, 1 Oct 2026); policy text dated 15 July 2025"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-server-monetisation-guidelines |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Server Administration |
| Region | Global |
| Game build checked | October 2026 update (Livestock Update, 1 Oct 2026); policy text dated 15 July 2025 |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This document reads Facepunch's Community Server and Hosting Guidelines for people who run Rust servers. It covers what the policy says about charging players, donations, cosmetics, server currency and adverts, the rule about Facepunch DLC, the duty not to pose as official, and the stated consequences of a breach. It is a reading of the policy, not legal advice; only the live page is authoritative.

Confidence is Medium. The permitted methods, the DLC rules and the sanctions come straight from Facepunch's own page and are well sourced. But several things people ask about are not in the policy at all: there is no pay-to-win definition, no logo or trademark clause, and no rules aimed at hosting companies. Where this document discusses those gaps it relies on community writing and says so.

# Key Facts

- The guidelines were last updated 15 July 2025 and are the page the Administration foundation already points to [1].
- Facepunch says servers may be monetised, with five examples: a fee or subscription, donations, cosmetic items, effects or enhancements, a server currency, and adverts, sponsorships or product placements [1].
- Players who validly bought Facepunch DLC must be able to access it on all servers, and servers may not give Facepunch DLC to non-owners or bypass ownership checks [1].
- Servers may restrict non-Facepunch content such as custom or Workshop content [1].
- A server must be clearly unofficial and must not pretend to be Facepunch [1].
- Breach may lead to delisting from the server browser or other sanctions; serious or repeated breach may lead to a game ban [1].
- The text read for this document does not contain the words pay-to-win, logo, trademark or reseller, and "hosting" appears only in the page title [1].
- The claim that queue skip is the only permitted monetisation appears in a store vendor blog [4] and is not supported by the policy's own list [1] *(assessed)*.

# Scope

Covers the Facepunch policy as it applies to Rust PC community servers, as read on 8 October 2026. Plugin sales are touched on only through Facepunch's separate Modding Guidelines [2]. Not covered: payment processor terms, store platform rules, consumer law, tax, or the contract between a customer and a hosting company. For admin mechanics see rust-server-administration-foundation; for cosmetics see rust-skins-cosmetics.

# Definitions

- **Community Server** — a private, unofficial server run by someone other than Facepunch [1].
- **Facepunch DLC** — paid Facepunch content, including approved in-game purchases, which owners must be able to use on any server [1].
- **Delisting** — removal from the in-game server browser, the first sanction the policy names [1].
- **Queue skip** — a paid priority-entry perk sold by many servers; not mentioned in the policy text [1][3].

# Core Mechanics

**Permission to run servers.** The policy permits private, unofficial and community servers provided the operator follows the guidelines, labels the server fairly to players and obeys the law [1].

**Monetisation.** Under the question "Am I allowed to monetise my Servers" the answer is yes "for example" by a single fee or subscription, donations, "cosmetic items, effects or enhancements", the operator's own server currency, and adverts, sponsorships or product placements [1]. The list is introduced as examples [1]; a practitioner reading treats it as illustrative rather than exhaustive [3].

**DLC.** Three rules apply. Facepunch DLC bought validly must be accessible on all servers. Non-Facepunch content, including custom or Steam Workshop content, may be restricted. A server may not grant Facepunch DLC to players who have not bought it. Servers set up to test game mechanics may temporarily grant or restrict Facepunch DLC for testing only [1].

**Server requirements.** The operator must make clear the server is unofficial; is responsible for compliance and for third parties using the server; must not run illegal activity, circumvent paid content, harm the games or players, infringe rights or carry malware; and must keep content and adverts suitable for the games' target audience. Cheating, griefing and hacking are prohibited. Operators may distribute their server but not the game or paid Facepunch content [1].

**Discretion and precedence.** Facepunch states that the ability to create, use and distribute servers is at its discretion and can be withdrawn, particularly to protect Facepunch or its games. The Terms of Service and Privacy Policy override the guidelines on conflict, and updates bind once posted [1].

**Enforcement.** The page says failure to comply "may result in delisting from the server browser or other sanctions", that serious or repeated breach may result in a game ban, and that a breach may also breach the Terms of Service [1].

**Related modding rules.** Facepunch's separate Modding Guidelines (last updated 28 August 2019) let a creator sell a mod they own and forbid presenting a mod as official [2].

# Reference Data

Checked against the policy text dated 15 July 2025, read on 2026-10-08 during the October 2026 update [1].

| Topic | What the policy says | Section (as read) | Source |
|-------|---------------------|-------------------|--------|
| Fee or subscription | Permitted example | Monetisation | [1] |
| Donations | Permitted example | Monetisation | [1] |
| Cosmetics, effects, enhancements | Permitted example; "enhancements" undefined | Monetisation | [1] |
| Server currency | Permitted example | Monetisation | [1] |
| Adverts, sponsorships, product placement | Permitted example | Monetisation | [1] |
| Owned Facepunch DLC | Must be accessible on all servers | DLC | [1] |
| Unowned Facepunch DLC | May not be granted; no bypassing ownership checks | DLC | [1] |
| Custom or Workshop content | May be restricted | DLC | [1] |
| Posing as official | Prohibited | Server requirements | [1] |
| Cheating, griefing, hacking, malware | Prohibited | Server requirements | [1] |
| Sanctions | Delisting or other sanctions; game ban for serious or repeated breach | Enforcement | [1] |
| Pay-to-win limits | Not stated | none | [1] |
| Logo or trademark use | Not stated (Modding Guidelines also silent on logos) | none | [1][2] |
| Hosting-company rules | Not stated beyond the page title | none | [1] |

# Version & Patch Notes

- The guidelines were last updated 15 July 2025 per the page [1].
- No change to the policy text was seen between that date and 8 October 2026; the page carries no changelog, so earlier versions are not available here [1].
- The Modding Guidelines are dated 28 August 2019 [2].
- Volatile: the guidelines say changes bind once posted, so re-read the live page before each review [1].

# Common Pitfalls

- Believing queue skip is the only legal product. A store vendor blog states this [4]; another practitioner article says the policy never mentions queues or priority [3]; the policy text read here lists broader examples [1].
- Skin plugins that apply Marketplace skins players do not own, particularly behind a paid rank, are described by one practitioner as the main DLC risk [3]. This sits against the no-granting-unowned-DLC rule [1].
- Restricting skins or items players legitimately bought. The policy requires owned DLC to stay accessible [1].
- Assuming the policy bans pay-to-win. It does not mention it [1]; "enhancements" is undefined, so a practitioner calls pay-for-advantage neither prohibited nor clearly endorsed [3].
- Assuming a hosting company's logo or branding rules come from this page. None appear [1].

# Interactions & Related Systems

- Cosmetic and skin mechanics, and what counts as owned content, are in rust-skins-cosmetics.
- Rank and perk delivery runs through plugin permission groups; see rust-server-permissions-rcon and rust-modding-plugins-foundation. A practitioner article recommends keying purchases on SteamID64 and handling expiry for subscriptions [3].
- Cheating and griefing bans, which the guidelines prohibit, are covered in rust-moderation-anti-cheat.
- In-game trade and currency design is in rust-economy-trading; a server currency is a permitted monetisation example [1].
- Plugin frameworks are covered in rust-carbon-vs-oxide; selling a plugin falls under the Modding Guidelines [2].

# Assessed Guidance

## Guidance 1 — Treat the DLC rule as the hard line and design around it

- **Guidance:** Never grant Facepunch DLC or Marketplace skins to non-owners and never lock owners out of DLC they bought; check any skin plugin for this before enabling it.
- **Evidence basis:** The policy states both DLC rules and names delisting and game bans as sanctions [1]; a practitioner identifies skin plugins as the main practical risk [3].
- **Confidence:** High. The rules are explicit first-party text; only the plugin risk is practitioner opinion.
- **So what:** Selling skin access behind a rank is the product most likely to cost you your listing.

## Guidance 2 — Do not rely on queue skip being the only allowed product

- **Guidance:** Plan your store against the policy's own list, not against vendor claims that only queue skip is allowed.
- **Evidence basis:** The policy lists five example methods [1]; one article says queue skip is typically the only option [4]; another says the policy never mentions it [3].
- **Confidence:** Medium. The policy text is clear but Facepunch has not publicly ruled on specific products.
- **So what:** You have wider latitude than some vendors say, but discretion lies with Facepunch [1].

## Guidance 3 — Define pay-to-win yourself and publish it

- **Guidance:** Because the policy neither defines nor bans pay-to-win, state publicly what your ranks and kits do, and keep gameplay advantages modest if you want player trust.
- **Evidence basis:** No pay-to-win text and an undefined "enhancements" [1]; a practitioner advises stating what ranks do [3]; the policy requires fair labelling [1].
- **Confidence:** Medium. The absence of a rule is documented, but the trust advice is community opinion.
- **So what:** Fair labelling is the only stated standard, so clear descriptions protect you against complaints and breach claims.

## Guidance 4 — Keep official-looking branding off your server

- **Guidance:** Do not use names, banners or descriptions that suggest the server is run by Facepunch; for any use of Facepunch logos, ask Facepunch's legal contact first.
- **Evidence basis:** The policy bars posing as Facepunch and is silent on logos [1]; the Modding Guidelines also bar presenting a mod as official [2].
- **Confidence:** Medium. The official-status rule is explicit; the logo advice is a cautious inference from silence.
- **So what:** Silence is not permission, and the policy lets Facepunch withdraw server permission at its discretion [1].

# Open Questions

- What does "enhancements" cover? Facepunch has not defined it in the text read; a statement from Facepunch would resolve it.
- Is there any Facepunch rule on logos, trademarks or use of game art on storefronts? None found in the guidelines or Modding Guidelines.
- Does Facepunch publish rules or an agreement for hosting providers? The page title says "Hosting" but the body read contains no provider-specific rules.
- How often are delisting and bans applied for monetisation breaches? No Facepunch enforcement data was found.
- Whether the policy changed between 15 July 2025 and today cannot be shown without a page history.

# References

**Primary Sources**

- [1] **Facepunch Studios** — *Community Server and Hosting Guidelines* (updated 15 July 2025). https://facepunch.com/legal/servers. Accessed 2026-10-08.
- [2] **Facepunch Studios** — *Modding Guidelines* (updated 28 August 2019). https://facepunch.com/legal/modding. Accessed 2026-10-08.

**Community & Practitioner Evidence**

- [3] **GameServerKings** — *Rust Server Monetisation: What Facepunch Actually Allows* (hosting vendor, published 19 August 2026). https://www.gameserverkings.com/knowledge-base/rust/server-monetisation/. Accessed 2026-10-08.
- [4] **PayNow** — *How to Monetize Your Rust Server* (store vendor, 10 December 2025). https://paynow.gg/blog/how-to-monetize-your-rust-server. Accessed 2026-10-08.

**Further Reading**

- See Related Documents.

# Further Reading

Re-read https://facepunch.com/legal/servers before every review; questions about the policy go to the legal contact the page names.

# Related Documents

- rust-server-administration-foundation
- rust-skins-cosmetics
- rust-moderation-anti-cheat
- rust-modding-plugins-foundation
- rust-economy-trading
- rust-server-permissions-rcon
- rust-carbon-vs-oxide
- rust-updates-meta-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
