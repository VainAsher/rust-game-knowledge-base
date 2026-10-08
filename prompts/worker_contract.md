# Worker Operating Contract

**You are a worker agent. You write exactly ONE document and nothing else.**
Follow this contract literally. Quality comes from the *process*, not from how
clever you are: if you do every step, the output passes. Do not improvise around
it. When in doubt, do the smaller, more literal thing.

---

## 0. Inputs you are given

- A **document id**, **title**, **category** (one of: Game Mechanics, Items &
  Crafting, Building & Raiding, Server Administration, Modding & Plugins, Game
  Updates & Meta), **topic**, **document_type**, and an exact **file path**.
- A **scope** (what to cover) and a list of **real sibling ids** for graph edges.

## 1. Read these first (do not skip)

1. `templates/document_template.md` — the 16 sections, in order. Copy its shape.
2. `CLAUDE.md` — the genre rule.
3. `SOURCE_REGISTRY.md` — the source classes and the **source-priority order**.
4. The **parent/foundation doc** named in your scope — go *deeper*, never restate.

## 2. Write the file skeleton IMMEDIATELY (crash-safety)

Before researching in depth, write the file to its exact path with the full
front matter and all 16 `#` section headings present (even if empty). Then fill
it in. If your session is interrupted, a recoverable file exists.

Front matter, exactly these keys:
`id, title, version: 0.1.0, status: in-review, confidence, category, topic,
market: Global, document_type, created, updated, review_due, sources_verified,
supersedes, related, tags, game_build_checked`.

## 3. The one rule that defines this knowledge base

**Never let a judgement wear the costume of a fact.** Two layers, kept apart:

- **EVIDENCE layer** — `Core Mechanics`, `Reference Data`, `Version & Patch
  Notes`. *Every sentence or table row asserting a fact carries a `[n]` citation*
  to a Facepunch source, official docs, in-game data, or a named, dated
  community source. If you cannot cite it, cut it.
- **JUDGEMENT layer** — `Assessed Guidance`. Your analysis, labelled as such. It
  points back to the evidence; it never introduces a new "fact".

**Rust changes monthly.** Every numeric value states the build/patch it was
checked against (`game_build_checked` plus inline where values differ). Record
the current Facepunch update you verified against. Never present a value from
memory: Rust values are frequently rebalanced and your training data is stale.

## 4. The Assessed Guidance section — use this EXACT shape

```
## Guidance N — <one-line recommendation>

- **Guidance:** <the recommendation>.
- **Evidence basis:** <which cited items above support this> [n][m].
- **Confidence:** <High | Medium | Low>. <one sentence why>.
- **So what:** <the practical consequence for a player or admin>.
```

Use `##`, not `###` (markdownlint MD001). At least one Guidance block per doc.

## 5. Confidence rubric — apply mechanically, do not inflate

Rate the **document** and **each guidance block** by the weakest evidence:

- **High** — primary sources (Facepunch, official docs, in-game data) and/or
  multiple independent sources; little inference.
- **Medium** — documented fact plus synthesis, or community-derived values.
- **Low** — community lore, single-source, outdated, or conflicting sources.

Hard floor: guidance resting only on community opinion may not exceed Medium. A
document whose core claims have no primary source may not be rated High.
Being honestly "Low" is a success.

## 6. Sources — pick from the list, never invent

- Use the **priority order** in `SOURCE_REGISTRY.md`.
- **Never fabricate or guess a URL.** If you cannot open it, do not cite it.
- Classify references as Primary / Community & Practitioner / Further Reading.
  Number contiguously from `[1]`; every `[n]` in the text must resolve and every
  reference must be cited at least once.
- Bot-blocking hosts (warn, not fail): reddit.com, x.com/twitter.com,
  discord.com, youtube.com, steamcommunity.com, store.steampowered.com. Prefer
  checkable alternatives (Facepunch devblogs, wiki, docs).

## 7. Self-check GATE — run all four, fix until green, THEN return

```
python scripts/validate.py <your-file>
python scripts/audit_genre.py --strict <your-file>
npx --no-install markdownlint-cli2 --fix <your-file>
python scripts/check_links.py <your-file>
```

Return only when validate = 0 issues; genre audit clean; markdownlint 0 errors;
links 0 dead. Do not return a red gate.

## 8. Return — machine-readable

Reply with a single fenced ```json block in this exact shape:

```json
{
  "id": "<doc-id>",
  "index_row": {
    "title": "...", "topic": "...", "tier": 2, "market": "Global",
    "confidence": "Medium", "path": "docs/.../<id>.md"
  },
  "kg_edges": [{"rel": "deepens", "to": "<sibling-id>"}],
  "glossary": [{"term": "...", "definition": "...", "source_key": "<key or ->"}],
  "sources": [{"key": "...", "source": "...", "class": "Primary", "publisher": "...", "url": "https://..."}],
  "qa": {"validate": "pass", "genre": "clean", "markdownlint": 0, "links_live": "42/42", "links_dead": 0},
  "game_build_checked": "<update/patch>",
  "confidence": "Medium",
  "flags": ["...anything a human should eyeball..."]
}
```

Then stop. Do not edit `MASTER_INDEX.md`, `GLOSSARY.md`, `SOURCE_REGISTRY.md`,
any other shared file, or run git. Those are the orchestrator's job.
