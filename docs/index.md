# Rust (Facepunch) Game Knowledge Base

!!! warning "Unofficial fan reference — not affiliated with Facepunch Studios"
    Rust is updated monthly and values change between patches. Facts are cited to official or authoritative sources with a verified-on date; assessed guidance is labelled judgement with a confidence rating. Check the current patch before relying on any number.

Evidence-based, source-cited reference for the PC/Steam survival game Rust — mechanics, items, building and raiding, server administration, modding and updates.

**12 documents** across **12 topics** — every factual claim carries a citation to an official or authoritative source, assessed gaps are labelled and confidence-rated, and links, citations and structure are checked automatically in CI.

*Confidence: 0 High · 11 Medium · 1 Low.*  *Market: Global 12.*

## Tier 1 — Category foundations

- [Rust Building and Raiding: Foundation](building-raiding/rust-building-raiding-foundation.md) — *Building system, upkeep and raiding* (Global)
- [Rust Game Mechanics: Foundation](game-mechanics/rust-game-mechanics-foundation.md) — *Core survival loop* (Global)
- [Rust Items and Crafting: Foundation](items-crafting/rust-items-crafting-foundation.md) — *Resources, crafting and blueprints* (Global)
- [Rust Modding and Plugins: Foundation](modding-plugins/rust-modding-plugins-foundation.md) — *Oxide/uMod and Carbon frameworks* (Global)
- [Rust Server Administration: Foundation](server-administration/rust-server-administration-foundation.md) — *Dedicated server setup* (Global)
- [Rust Updates and Meta: Foundation](updates-meta/rust-updates-meta-foundation.md) — *Update cadence and release history* (Global)

## Tier 2 — Subject deep-dives

- [Rust Raiding Costs and Base Defence](building-raiding/rust-raiding-costs-defence.md) — *Raid costs and defence* (Global)
- [Rust Combat and Damage Model](game-mechanics/rust-combat-damage-model.md) — *Combat and damage* (Global)
- [Rust Weapons and Ammunition](items-crafting/rust-weapons-ammo.md) — *Weapons and ammo* (Global)
- [Rust Plugin Development and Hooks](modding-plugins/rust-plugin-development-hooks.md) — *Plugin development* (Global)
- [Rust Server Convars Reference](server-administration/rust-server-convars-reference.md) — *Server convars and config* (Global)
- [Rust Update Timeline 2026](updates-meta/rust-update-timeline-2026.md) — *2026 update timeline* (Global)

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
      subgraph Tier2["Tier 2"]
        rust_combat_damage_model["rust-combat-damage-model"]
        rust_plugin_development_hooks["rust-plugin-development-hooks"]
        rust_raiding_costs_defence["rust-raiding-costs-defence"]
        rust_server_convars_reference["rust-server-convars-reference"]
        rust_update_timeline_2026["rust-update-timeline-2026"]
        rust_weapons_ammo["rust-weapons-ammo"]
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
      rust_update_timeline_2026 -->|deepens| rust_updates_meta_foundation
      rust_server_convars_reference -->|deepens| rust_server_administration_foundation
      rust_raiding_costs_defence -->|deepens| rust_building_raiding_foundation
      rust_combat_damage_model -->|deepens| rust_game_mechanics_foundation
      rust_plugin_development_hooks -->|deepens| rust_modding_plugins_foundation
      rust_weapons_ammo -->|deepens| rust_items_crafting_foundation
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
      rust_update_timeline_2026 -->|related| rust_game_mechanics_foundation
      rust_update_timeline_2026 -->|related| rust_items_crafting_foundation
      rust_update_timeline_2026 -->|related| rust_building_raiding_foundation
      rust_update_timeline_2026 -->|related| rust_server_administration_foundation
      rust_update_timeline_2026 -->|related| rust_modding_plugins_foundation
      rust_update_timeline_2026 -->|related| rust_combat_damage_model
      rust_update_timeline_2026 -->|related| rust_weapons_ammo
      rust_update_timeline_2026 -->|related| rust_raiding_costs_defence
      rust_update_timeline_2026 -->|related| rust_server_convars_reference
      rust_update_timeline_2026 -->|related| rust_plugin_development_hooks
      rust_server_convars_reference -->|related| rust_game_mechanics_foundation
      rust_server_convars_reference -->|related| rust_items_crafting_foundation
      rust_server_convars_reference -->|related| rust_building_raiding_foundation
      rust_server_convars_reference -->|related| rust_modding_plugins_foundation
      rust_server_convars_reference -->|related| rust_updates_meta_foundation
      rust_server_convars_reference -->|related| rust_combat_damage_model
      rust_server_convars_reference -->|related| rust_weapons_ammo
      rust_server_convars_reference -->|related| rust_raiding_costs_defence
      rust_server_convars_reference -->|related| rust_plugin_development_hooks
      rust_server_convars_reference -->|related| rust_update_timeline_2026
      rust_raiding_costs_defence -->|related| rust_game_mechanics_foundation
      rust_raiding_costs_defence -->|related| rust_items_crafting_foundation
      rust_raiding_costs_defence -->|related| rust_server_administration_foundation
      rust_raiding_costs_defence -->|related| rust_modding_plugins_foundation
      rust_raiding_costs_defence -->|related| rust_updates_meta_foundation
      rust_raiding_costs_defence -->|related| rust_combat_damage_model
      rust_raiding_costs_defence -->|related| rust_weapons_ammo
      rust_raiding_costs_defence -->|related| rust_server_convars_reference
      rust_raiding_costs_defence -->|related| rust_plugin_development_hooks
      rust_raiding_costs_defence -->|related| rust_update_timeline_2026
      rust_combat_damage_model -->|related| rust_items_crafting_foundation
      rust_combat_damage_model -->|related| rust_building_raiding_foundation
      rust_combat_damage_model -->|related| rust_server_administration_foundation
      rust_combat_damage_model -->|related| rust_modding_plugins_foundation
      rust_combat_damage_model -->|related| rust_updates_meta_foundation
      rust_combat_damage_model -->|related| rust_weapons_ammo
      rust_combat_damage_model -->|related| rust_raiding_costs_defence
      rust_combat_damage_model -->|related| rust_server_convars_reference
      rust_combat_damage_model -->|related| rust_plugin_development_hooks
      rust_combat_damage_model -->|related| rust_update_timeline_2026
      rust_plugin_development_hooks -->|related| rust_game_mechanics_foundation
      rust_plugin_development_hooks -->|related| rust_items_crafting_foundation
      rust_plugin_development_hooks -->|related| rust_building_raiding_foundation
      rust_plugin_development_hooks -->|related| rust_server_administration_foundation
      rust_plugin_development_hooks -->|related| rust_updates_meta_foundation
      rust_plugin_development_hooks -->|related| rust_combat_damage_model
      rust_plugin_development_hooks -->|related| rust_weapons_ammo
      rust_plugin_development_hooks -->|related| rust_raiding_costs_defence
      rust_plugin_development_hooks -->|related| rust_server_convars_reference
      rust_plugin_development_hooks -->|related| rust_update_timeline_2026
      rust_weapons_ammo -->|related| rust_game_mechanics_foundation
      rust_weapons_ammo -->|related| rust_building_raiding_foundation
      rust_weapons_ammo -->|related| rust_server_administration_foundation
      rust_weapons_ammo -->|related| rust_modding_plugins_foundation
      rust_weapons_ammo -->|related| rust_updates_meta_foundation
      rust_weapons_ammo -->|related| rust_combat_damage_model
      rust_weapons_ammo -->|related| rust_raiding_costs_defence
      rust_weapons_ammo -->|related| rust_server_convars_reference
      rust_weapons_ammo -->|related| rust_plugin_development_hooks
      rust_weapons_ammo -->|related| rust_update_timeline_2026
    ```

## Machine-readable exports

Generated artefacts live in the repository's `exports/` directory: a knowledge graph (JSON + Mermaid), a capability/gap matrix (CSV/JSON), a coverage report, and a section-level RAG export (`exports/rag/`).

*Site generated by `scripts/build_site.py` — do not edit by hand.*

