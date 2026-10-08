---
id: rust-skins-cosmetics
title: "Rust Skins and Cosmetics"
version: 1.0.0
status: frozen
confidence: Medium
category: Game Updates & Meta
topic: "Skins and cosmetics"
market: Global
document_type: deep-dive
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [rust-updates-meta-foundation, rust-clothing-armour, rust-economy-trading, rust-server-administration-foundation, rust-moderation-anti-cheat, rust-modding-plugins-foundation]
tags: [skins, cosmetics, workshop, item-store, dlc, server-guidelines]
game_build_checked: "October 2026 update (Livestock Update, 1 Oct 2026)"
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rust-skins-cosmetics |
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

This document explains how Rust skins and cosmetics reach players: community creators build skins with the Steam Workshop tooling, Facepunch selects some for the game, and players obtain them through crates, the Steam marketplace, the Steam item store, the in-game store and DLC packs. It also records what Facepunch has said about skins being cosmetic, and the server-hosting guidelines on paid content. It gives no price or investment advice.

Document-level confidence is Medium. The founding statements and the current server guidelines are first-party Facepunch sources, but the key policy statements on cosmetic-only skins date from 2015, and no single current Facepunch page defines the cosmetic-only rule. Prices, rarity, and the store's current catalogue were deliberately not collected.

# Key Facts

- In a 20 August 2015 devblog Facepunch said of Workshop skins: "these are just skins, they don't offer any differing properties" [1].
- In July 2015 Facepunch said "The items we're adding are cosmetic, and we're not charging for them" about its first inventory items, which were awarded by playtime [2].
- Skins are made by community creators through the Steam Workshop; since October 2016 an integrated in-game workshop publishes to Steam on "Publish" [3][4].
- Creators must accept the Contributor Agreement before items can be visible or added to the game; Facepunch weighs quality, community votes and presentation [5].
- A permanent in-game store launched on 18 November 2021; its items cannot be traded on Steam or resold on the Steam Community Market [6].
- The Facepunch server guidelines (last updated 15 July 2025) forbid granting Facepunch DLC to players who have not validly purchased it, and forbid bypassing ownership checks [7].
- The October 2026 update added a Plague Doctor Hazmat Suit DLC and made all ladder hatches Workshop-skinnable [8].

# Scope

Covers PC Rust (Steam): how skins are created and selected, how players obtain cosmetics, what Facepunch has said about cosmetic-only status, and the server-side policy on cosmetic and DLC content. Build checked: October 2026 update. Excludes prices, market values, trading advice, console editions, and the full current catalogue of skins and DLC packs.

# Definitions

- **Skin:** an alternate appearance for an existing item or deployable. In 2015 Facepunch described Workshop skins as having no "differing properties" [1].
- **Workshop skinnable:** an item that the Workshop tooling lets creators reskin; the October 2026 update added all ladder hatches [8].
- **Facepunch DLC:** per the server guidelines, paid content packs such as building skins, decor packs, hazmat skins and instruments, plus approved in-game purchases [7].
- **Contributor Agreement:** the agreement a creator must accept before items become publicly visible or eligible for the game [5].

# Core Mechanics

**Creation.** In July 2015 the Workshop SDK let players create skins, initially limited to t-shirts and trousers, and Facepunch said items would go in if they were not "a terrible meme, someone else's IP" and fit Rust's style [3]. By August 2015 jackets, a snow jacket, a boonie hat and a balaclava were also skinnable [1]. In October 2016 an integrated in-game workshop let creators edit skins in-game; clicking "Publish" generated an icon and uploaded to the Steam Workshop [4].

**Selection.** The Workshop FAQ says creators must accept the Contributor Agreement; when two submissions are similar, the team considers overall quality, community votes and presentation; creators without a prior approved item may get priority; and community conduct can affect decisions [5]. The Facepunch wiki guidance says items should "look dirty and worn", skins must stay within the tier of the item (a burlap item that looks like metal may be rejected as it could be mistaken for armour), text lowers the chance of acceptance, and items with few skins are good targets [9]. That wiki page is marked as last updated "A Long Time Ago" [9].

**Obtaining.** The Workshop FAQ says players get skins by crafting crates from items in their inventory or by buying items on the marketplace, that skins are released in limited runs, and that they are removed from the store after a long time on sale or after earning enough revenue and may then appear in crates [5]. Artists do not receive money from crates or the marketplace, and the team does not sell crates directly [5]. In August 2015 Facepunch said players must unlock Workshop items in game before crafting them [1]. A 2021 launch post describes a permanent store selling premium cosmetics and skins year round [6]. The October 2026 update says the Plague Doctor Hazmat Suit "can be purchased in-game or from the Rust Steam item store" [8].

**Store trading rules.** Items from the permanent store cannot be traded on Steam or resold on the Steam Community Market and "hold no resale monetary value"; Facepunch said this was to differentiate them from earlier items and that it would keep the policy under review [6].

**Cosmetic-only statement.** The August 2015 devblog says Workshop skins are "just skins, they don't offer any differing properties" and advises "If you're in any kind of doubt - don't buy them, they're just cosmetics" [1]. The wiki rule against skins resembling higher-tier items exists because they could be mistaken for armour [9].

**Server-side.** The guidelines require servers to give unrestricted access to validly purchased Facepunch DLC, and forbid granting DLC to non-owners, bypassing ownership checks or artificially enabling DLC; test servers may temporarily restrict or grant DLC for testing only [7]. Servers may restrict custom or Steam Workshop content that Facepunch does not sell or gate, may charge a single fee or subscription, and may sell cosmetic items, effects or enhancements [7].

# Reference Data

Facepunch statements and rules, by source and date (checked 2026-10-08, build: Livestock Update).

| Topic | Statement | Date of source | Source |
|-------|-----------|----------------|--------|
| Cosmetic only | Workshop skins do not offer "any differing properties" | 20 Aug 2015 | [1] |
| Early items | Cosmetic, free, awarded by playtime | 16 Jul 2015 | [2] |
| Workshop SDK | Initially t-shirts and trousers | 30 Jul 2015 | [3] |
| In-game workshop | "Publish" uploads to Steam Workshop | 20 Oct 2016 | [4] |
| Permanent store | Launched; items not tradeable or resellable | 18 Nov 2021 | [6] |
| Server guidelines | No DLC for non-owners; no ownership bypass | 15 Jul 2025 | [7] |
| Ladder hatches | All variants skinnable | 1 Oct 2026 | [8] |
| Sandbag rework | "All Sandbag skins are supported across all variations" | 1 Oct 2026 | [8] |
| Plague Doctor Hazmat Suit | DLC; buyable in-game or in Steam item store | 1 Oct 2026 | [8] |

# Version & Patch Notes

- 16 Jul 2015: first cosmetic inventory items, awarded by playtime; no community clothing accepted yet [2].
- 30 Jul 2015: Workshop SDK opens for t-shirts and trousers [3].
- 20 Aug 2015: plan to sell Workshop skins in game; skins stated to be cosmetic only [1].
- 20 Oct 2016: integrated in-game workshop in development on the prerelease branch, described as a heavy work in progress [4].
- 18 Nov 2021: permanent in-game store launches [6].
- 15 Jul 2025: server guidelines last updated, binding once posted [7].
- 1 Oct 2026: ladder hatches skinnable, sandbag skins supported across variations, store loads assets on demand, Plague Doctor Hazmat Suit DLC [8]. Volatile: the catalogue of DLC and store items changes with events and sales.

# Common Pitfalls

- Assuming every cosmetic-looking item is cosmetic. The Facepunch wiki lists the Hoodie with protection values (for example Cold 34%), so clothing items carry stats, whereas skins are reskins of an item [10]. The wiki page does not say whether its colour variants are skins or differ in stats [10].
- Citing 2015 devblogs as current store policy. They describe the Workshop model of that time, and the 2021 post says store trading rules remain under review [1][6].
- Assuming creators are paid by crates or marketplace sales. The FAQ says they are not [5].
- Assuming servers may unlock paid content for everyone. The guidelines forbid this outside test servers [7].
- Assuming Facepunch's wiki skin-acceptance page is a rulebook: it is advice, and omits submission steps and revenue terms [9].

# Interactions & Related Systems

Skins sit on top of items covered in rust-items-crafting-foundation and rust-clothing-armour; the tier-matching rule exists to avoid confusion with armour [9]. Server owners should read the DLC rules alongside rust-server-administration-foundation and rust-moderation-anti-cheat [7]. Plugins that change skins or sell cosmetics must stay within the guidelines [7]; see rust-modding-plugins-foundation. Trading and marketplace context is in rust-economy-trading. Update-by-update changes are tracked in rust-updates-meta-foundation [8].

# Assessed Guidance

## Guidance 1 — Treat skins as appearance only, but check clothing separately

- **Guidance:** Assume Workshop skins change appearance, not stats, but verify stats for clothing and attire items on the wiki.
- **Evidence basis:** Facepunch's 2015 statement [1]; the wiki Hoodie stats [10]; the tier-matching rule [9].
- **Confidence:** Medium. The statement is first-party but dated 2015, with no current restatement found.
- **So what:** Players can choose skins freely, yet should not assume a differently named clothing item has identical protection.

## Guidance 2 — Server owners should never unlock DLC for non-owners

- **Guidance:** Do not use plugins or settings that grant Facepunch DLC to players who have not bought it; sell only your own cosmetic content.
- **Evidence basis:** Server guidelines on ownership checks and cosmetic sales [7].
- **Confidence:** High. The rule is stated directly in the current first-party guidelines.
- **So what:** Avoid enforcement risk; read the guidelines page again after each revision.

## Guidance 3 — Treat store and trading rules as time-sensitive

- **Guidance:** Re-check the current store and marketplace rules before relying on any trading claim here.
- **Evidence basis:** 2021 store post said policy stays under review [6]; catalogue changes in the latest update [8].
- **Confidence:** Medium. Only the 2021 and 2026 posts were opened.
- **So what:** Do not infer current tradeability from a 2021 post.

# Open Questions

- No current Facepunch page was found that restates the cosmetic-only rule; resolving needs an official FAQ or terms page.
- Revenue share between Facepunch and creators was not found in any opened source. Community forum figures were not verified and are not used.
- The current full list of DLC packs and store items was not collected.
- Whether any skinned item has had gameplay-relevant behaviour (for example hitbox or visibility differences) is not covered by an opened source.
- Whether Steam marketplace skins are still sold as in 2021 was not confirmed.

# References

**Primary Sources**

- [1] **Facepunch** — *Devblog 74 (20 Aug 2015)*. https://rust.facepunch.com/news/devblog-74. Accessed 2026-10-08.
- [2] **Facepunch** — *Devblog 69 (16 Jul 2015)*. https://rust.facepunch.com/news/devblog-69. Accessed 2026-10-08.
- [3] **Facepunch** — *Devblog 71 (30 Jul 2015)*. https://rust.facepunch.com/news/devblog-71. Accessed 2026-10-08.
- [4] **Facepunch** — *Devblog 132 (20 Oct 2016)*. https://rust.facepunch.com/news/devblog-132. Accessed 2026-10-08.
- [5] **Facepunch Rust Wiki** — *Workshop FAQ*. https://wiki.facepunch.com/rust/Workshop_FAQ. Accessed 2026-10-08.
- [6] **Facepunch** — *Permanent Store (18 Nov 2021)*. https://rust.facepunch.com/news/permanent-store. Accessed 2026-10-08.
- [7] **Facepunch Studios** — *Community Server and Hosting Guidelines*. https://facepunch.com/legal/servers. Accessed 2026-10-08.
- [8] **Facepunch** — *Livestock Update (1 Oct 2026)*. https://rust.facepunch.com/news/livestock. Accessed 2026-10-08.
- [9] **Facepunch Rust Wiki** — *Getting Your Skin Accepted*. https://wiki.facepunch.com/rust/Getting_Skin_Accepted. Accessed 2026-10-08.
- [10] **Facepunch Rust Wiki** — *Hoodie*. https://wiki.facepunch.com/rust/item/hoodie. Accessed 2026-10-08.

**Community & Practitioner Evidence**

None used.

**Further Reading**

None.

# Further Reading

The Facepunch news index and the wiki Workshop pages for current submission guidance [5][9].

# Related Documents

- rust-updates-meta-foundation
- rust-clothing-armour
- rust-economy-trading
- rust-server-administration-foundation
- rust-moderation-anti-cheat
- rust-modding-plugins-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after green QA (validate, genre audit, markdownlint, links live). | Auto-approve mandate |
