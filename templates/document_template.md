---
id: kebab-case-unique-id
title: "Human-Readable Title"
version: 0.1.0
status: draft            # draft | in-review | approved | frozen | superseded
confidence: Medium       # High | Medium | Low  (see confidence rubric below)
category: Game Mechanics # Game Mechanics | Items & Crafting | Building & Raiding | Server Administration | Modding & Plugins | Game Updates & Meta
topic: "Radiation & Monuments"
market: "Global"         # kept as the region field; Rust is global
document_type: foundation   # foundation | deep-dive | reference-table | how-to | meta
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08   # Rust patches monthly (first Thursday): review ~monthly for volatile topics
sources_verified: 2026-10-08
supersedes: null
related: []              # list of related document ids
tags: []
game_build_checked: ""   # Rust build/patch the facts were checked against, e.g. "Oct 2026 update"
---

<!--
  GENRE = reference. The cardinal rule: NEVER let a judgement wear the
  costume of a fact.
    • Core Mechanics, Reference Data and Version & Patch Notes are the EVIDENCE
      layer — every factual sentence/row carries a [n] citation to a working link.
    • Assessed Guidance is the JUDGEMENT layer — labelled advice, each block
      carrying Evidence basis / Confidence / So what.
  Rust changes every month. Every number (damage, HP, cost, rate, convar
  default) must say which build it was checked against. If you can't cite it, cut it.
  Keep the section order below; the QA validator enforces it.

  Confidence rubric (document-level `confidence:` field):
    High   — rests on primary sources (Facepunch, in-game data, official server
             docs) and/or multiple independent sources; little inference.
    Medium — mix of documented fact and community-derived/synthesised values.
    Low    — largely community lore, single-source, or sources conflict/outdated.
-->

# Document Control

| Field | Value |
|-------|-------|
| Document ID | kebab-case-unique-id |
| Version | 0.1.0 |
| Status | draft |
| Confidence | Medium |
| Category | Game Mechanics |
| Region | Global |
| Game build checked | *e.g. Oct 2026 update* |
| Owner | Rust KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

Two short paragraphs: what this document covers and the headline facts. State
the document-level confidence and why.

# Key Facts

- 4–8 most important, decision-useful facts, each cited [1].
- Mark anything that is judgement rather than cited fact as *(assessed)*.

# Scope

What is and is not covered; which game modes (vanilla, modded, console excluded
unless stated) and which build.

# Definitions

Document-specific terms. Prefer the shared `GLOSSARY.md`.

# Core Mechanics

**Evidence layer — cite everything.** How the system works, from primary
sources [1]. Do not editorialise.

# Reference Data

**Evidence layer — cite everything.** Tables of values (damage, HP, costs,
timers, convars, config keys) with source and build for each [2].

# Version & Patch Notes

**Evidence layer.** When this behaviour was introduced or changed, per
Facepunch devblogs/changelogs [3]. Flag values known to be volatile.

# Common Pitfalls

Documented mistakes and misconceptions, attributed to a source (wiki, forum
thread, devblog) [4].

# Interactions & Related Systems

How this system interacts with others, cited. Link related KB documents by id.

# Assessed Guidance

**Judgement layer — label it.** Repeat the block below per item. Use a `##`
heading (not `###`) and keep the three bold bullets — `scripts/audit_genre.py`
enforces them. Never present guidance as a cited fact.

## Guidance 1 — <one-line recommendation>

- **Guidance:** <the recommendation, in one or two sentences>.
- **Evidence basis:** <which cited items above support this> [1][2].
- **Confidence:** <High | Medium | Low>. <one sentence why; guidance resting only on community opinion cannot exceed Medium>.
- **So what:** <the practical consequence for a player or admin>.

# Open Questions

What remains unverified or contested, and what would resolve it.

# References

Cite every factual claim. Number contiguously from [1]; every number must
resolve here and be cited in the text.

**Primary Sources** — Facepunch devblogs/changelogs, official docs, in-game data.

- [1] **Source name** — *Document title*. URL. Accessed 2026-10-08.

**Community & Practitioner Evidence** — wiki, forums, community databases.

- [2] **Site** — *Page title*. URL.
- [3] **Facepunch** — *Devblog / changelog title*. URL. Accessed 2026-10-08.
- [4] **Community site** — *Thread or page title*. URL.

**Further Reading**

# Further Reading

Non-cited but useful background.

# Related Documents

Links to related knowledge-base documents (by id).

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
