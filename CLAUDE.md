# CLAUDE.md — Rust Game Knowledge Base

Genre: **reference**. Subject: Rust (Facepunch Studios, PC/Steam). Audience: players and server admins. Region: global.

## Binding rules

1. **Evidence over model confidence.** Every fact cites an authoritative source with a working link. Judgement lives only in `Assessed Guidance`, labelled and confidence-rated.
2. **Rust changes monthly.** Every number states the build it was checked against. Never rely on model memory for values.
3. **One writer per file.** Workers write only their own document and never edit shared files or run git.
4. **Hard human gate** before generating a cluster, unless the user grants an auto-approve-on-green mandate.
5. **Freeze/version/release.** A fact change cuts a new version with a revision note, never a silent edit.
6. **Gates, all green before freezing:** `validate.py`, `audit_genre.py --strict`, markdownlint, `check_links.py` (orchestrator re-runs links independently).

Categories: Game Mechanics, Items & Crafting, Building & Raiding, Server Administration, Modding & Plugins, Game Updates & Meta.
Template: `templates/document_template.md` (16 sections). Worker contract: `prompts/worker_contract.md`.
