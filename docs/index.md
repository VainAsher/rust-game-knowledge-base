# Rust (Facepunch) Game Knowledge Base

!!! warning "Unofficial fan reference — not affiliated with Facepunch Studios"
    Rust is updated monthly and values change between patches. Facts are cited to official or authoritative sources with a verified-on date; assessed guidance is labelled judgement with a confidence rating. Check the current patch before relying on any number.

Evidence-based, source-cited reference for the PC/Steam survival game Rust — mechanics, items, building and raiding, server administration, modding and updates.

**6 documents** across **6 topics** — every factual claim carries a citation to an official or authoritative source, assessed gaps are labelled and confidence-rated, and links, citations and structure are checked automatically in CI.

*Confidence: 0 High · 6 Medium · 0 Low.*  *Market: Global 6.*

## Tier 1 — Category foundations

- [Rust Building and Raiding: Foundation](building-raiding/rust-building-raiding-foundation.md) — *Building system, upkeep and raiding* (Global)
- [Rust Game Mechanics: Foundation](game-mechanics/rust-game-mechanics-foundation.md) — *Core survival loop* (Global)
- [Rust Items and Crafting: Foundation](items-crafting/rust-items-crafting-foundation.md) — *Resources, crafting and blueprints* (Global)
- [Rust Modding and Plugins: Foundation](modding-plugins/rust-modding-plugins-foundation.md) — *Oxide/uMod and Carbon frameworks* (Global)
- [Rust Server Administration: Foundation](server-administration/rust-server-administration-foundation.md) — *Dedicated server setup* (Global)
- [Rust Updates and Meta: Foundation](updates-meta/rust-updates-meta-foundation.md) — *Update cadence and release history* (Global)

## Knowledge graph

??? note "Cross-reference graph (click to expand)"

    ```mermaid
    graph LR
      subgraph Tier1["Tier 1"]
        rust_building_raiding_foundation["rust-building-raiding-foundation"]
        rust_game_mechanics_foundation["rust-game-mechanics-foundation"]
        rust_items_crafting_foundation["rust-items-crafting-foundation"]
        rust_modding_plugins_foundation["rust-modding-plugins-foundation"]
        rust_server_administration_foundation["rust-server-administration-foundation"]
        rust_updates_meta_foundation["rust-updates-meta-foundation"]
      end
      rust_game_mechanics_foundation -->|related| rust_items_crafting_foundation
      rust_game_mechanics_foundation -->|related| rust_building_raiding_foundation
      rust_game_mechanics_foundation -->|related| rust_server_administration_foundation
      rust_game_mechanics_foundation -->|related| rust_modding_plugins_foundation
      rust_game_mechanics_foundation -->|related| rust_updates_meta_foundation
      rust_items_crafting_foundation -->|related| rust_building_raiding_foundation
      rust_items_crafting_foundation -->|related| rust_server_administration_foundation
      rust_items_crafting_foundation -->|related| rust_modding_plugins_foundation
      rust_items_crafting_foundation -->|related| rust_updates_meta_foundation
      rust_building_raiding_foundation -->|related| rust_server_administration_foundation
      rust_building_raiding_foundation -->|related| rust_modding_plugins_foundation
      rust_building_raiding_foundation -->|related| rust_updates_meta_foundation
      rust_server_administration_foundation -->|related| rust_modding_plugins_foundation
      rust_updates_meta_foundation -->|informs| rust_server_administration_foundation
      rust_updates_meta_foundation -->|informs| rust_modding_plugins_foundation
      rust_items_crafting_foundation -->|related| rust_game_mechanics_foundation
      rust_building_raiding_foundation -->|related| rust_game_mechanics_foundation
      rust_building_raiding_foundation -->|related| rust_items_crafting_foundation
      rust_server_administration_foundation -->|related| rust_game_mechanics_foundation
      rust_server_administration_foundation -->|related| rust_items_crafting_foundation
      rust_server_administration_foundation -->|related| rust_building_raiding_foundation
      rust_server_administration_foundation -->|related| rust_updates_meta_foundation
      rust_modding_plugins_foundation -->|related| rust_game_mechanics_foundation
      rust_modding_plugins_foundation -->|related| rust_items_crafting_foundation
      rust_modding_plugins_foundation -->|related| rust_building_raiding_foundation
      rust_modding_plugins_foundation -->|related| rust_server_administration_foundation
      rust_modding_plugins_foundation -->|related| rust_updates_meta_foundation
      rust_updates_meta_foundation -->|related| rust_game_mechanics_foundation
      rust_updates_meta_foundation -->|related| rust_items_crafting_foundation
      rust_updates_meta_foundation -->|related| rust_building_raiding_foundation
    ```

## Machine-readable exports

Generated artefacts live in the repository's `exports/` directory: a knowledge graph (JSON + Mermaid), a capability/gap matrix (CSV/JSON), a coverage report, and a section-level RAG export (`exports/rag/`).

*Site generated by `scripts/build_site.py` — do not edit by hand.*

