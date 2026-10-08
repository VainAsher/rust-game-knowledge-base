# Rust (Facepunch) Game Knowledge Base

!!! warning "Unofficial fan reference — not affiliated with Facepunch Studios"
    Rust is updated monthly and values change between patches. Facts are cited to official or authoritative sources with a verified-on date; assessed guidance is labelled judgement with a confidence rating. Check the current patch before relying on any number.

Evidence-based, source-cited reference for the PC/Steam survival game Rust — mechanics, items, building and raiding, server administration, modding and updates.

**36 documents** across **36 topics** — every factual claim carries a citation to an official or authoritative source, assessed gaps are labelled and confidence-rated, and links, citations and structure are checked automatically in CI.

*Confidence: 0 High · 32 Medium · 4 Low.*  *Market: Global 36.*

## Tier 1 — Category foundations

- [Rust Building and Raiding: Foundation](building-raiding/rust-building-raiding-foundation.md) — *Building system, upkeep and raiding* (Global)
- [Rust Game Mechanics: Foundation](game-mechanics/rust-game-mechanics-foundation.md) — *Core survival loop* (Global)
- [Rust Items and Crafting: Foundation](items-crafting/rust-items-crafting-foundation.md) — *Resources, crafting and blueprints* (Global)
- [Rust Modding and Plugins: Foundation](modding-plugins/rust-modding-plugins-foundation.md) — *Oxide/uMod and Carbon frameworks* (Global)
- [Rust Server Administration: Foundation](server-administration/rust-server-administration-foundation.md) — *Dedicated server setup* (Global)
- [Rust Updates and Meta: Foundation](updates-meta/rust-updates-meta-foundation.md) — *Update cadence and release history* (Global)

## Tier 2 — Subject deep-dives

- [Rust Base Building Mechanics](building-raiding/rust-base-building-mechanics.md) — *Structural mechanics and building rules* (Global)
- [Rust Raiding Costs and Base Defence](building-raiding/rust-raiding-costs-defence.md) — *Raid costs and defence* (Global)
- [Rust Turrets and Defensive Deployables](building-raiding/rust-turrets-deployables.md) — *Turrets and deployables* (Global)
- [Rust Combat and Damage Model](game-mechanics/rust-combat-damage-model.md) — *Combat and damage* (Global)
- [Rust Electricity and Logic](game-mechanics/rust-electricity-logic.md) — *Electricity and logic* (Global)
- [Rust Fishing](game-mechanics/rust-fishing.md) — *Fishing* (Global)
- [Rust Monuments and Loot](game-mechanics/rust-monuments-loot.md) — *Monuments and loot* (Global)
- [Rust Teams and Clans](game-mechanics/rust-teams-clans.md) — *Teams, clans and social systems* (Global)
- [Rust Vehicles](game-mechanics/rust-vehicles.md) — *Vehicles and transport* (Global)
- [Rust Wildlife and NPCs](game-mechanics/rust-wildlife-npcs.md) — *Wildlife and NPCs* (Global)
- [Rust World Events](game-mechanics/rust-world-events.md) — *Cargo ship, airdrops and map events* (Global)
- [Rust Clothing and Armour](items-crafting/rust-clothing-armour.md) — *Clothing and armour* (Global)
- [Rust Economy and Trading](items-crafting/rust-economy-trading.md) — *Economy, scrap and trading* (Global)
- [Rust Farming and Food](items-crafting/rust-farming-food.md) — *Farming, food and cooking* (Global)
- [Rust Research and Blueprints](items-crafting/rust-research-blueprints.md) — *Research table and blueprint costs* (Global)
- [Rust Tools and Gathering](items-crafting/rust-tools-gathering.md) — *Tools and gathering* (Global)
- [Rust Weapons and Ammunition](items-crafting/rust-weapons-ammo.md) — *Weapons and ammo* (Global)
- [Rust Carbon versus Oxide](modding-plugins/rust-carbon-vs-oxide.md) — *Carbon versus Oxide comparison* (Global)
- [Rust Plugin Development and Hooks](modding-plugins/rust-plugin-development-hooks.md) — *Plugin development* (Global)
- [Rust Plugin Marketplaces and Licensing](modding-plugins/rust-plugin-marketplaces.md) — *Plugin sources, licences and marketplaces* (Global)
- [Rust Moderation and Anti-Cheat](server-administration/rust-moderation-anti-cheat.md) — *Moderation, bans and anti-cheat* (Global)
- [Rust Server Convars Reference](server-administration/rust-server-convars-reference.md) — *Server convars and config* (Global)
- [Rust Server Monetisation and Hosting Guidelines](server-administration/rust-server-monetisation-guidelines.md) — *Facepunch community server guidelines* (Global)
- [Rust Server Performance](server-administration/rust-server-performance.md) — *Server performance and hardware* (Global)
- [Rust Server Permissions and RCON](server-administration/rust-server-permissions-rcon.md) — *Permissions and RCON* (Global)
- [Rust Wipes and Map Generation](server-administration/rust-wipes-map-generation.md) — *Wipes and map generation* (Global)
- [Rust Game Modes and Server Types](updates-meta/rust-game-modes.md) — *Game modes and server types* (Global)
- [Rust Skins and Cosmetics](updates-meta/rust-skins-cosmetics.md) — *Skins and cosmetics* (Global)
- [Rust System Requirements and Platforms](updates-meta/rust-system-requirements-platforms.md) — *PC requirements, platforms and editions* (Global)
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
        rust_base_building_mechanics["rust-base-building-mechanics"]
        rust_carbon_vs_oxide["rust-carbon-vs-oxide"]
        rust_clothing_armour["rust-clothing-armour"]
        rust_combat_damage_model["rust-combat-damage-model"]
        rust_economy_trading["rust-economy-trading"]
        rust_electricity_logic["rust-electricity-logic"]
        rust_farming_food["rust-farming-food"]
        rust_fishing["rust-fishing"]
        rust_game_modes["rust-game-modes"]
        rust_moderation_anti_cheat["rust-moderation-anti-cheat"]
        rust_monuments_loot["rust-monuments-loot"]
        rust_plugin_development_hooks["rust-plugin-development-hooks"]
        rust_plugin_marketplaces["rust-plugin-marketplaces"]
        rust_raiding_costs_defence["rust-raiding-costs-defence"]
        rust_research_blueprints["rust-research-blueprints"]
        rust_server_convars_reference["rust-server-convars-reference"]
        rust_server_monetisation_guidelines["rust-server-monetisation-guidelines"]
        rust_server_performance["rust-server-performance"]
        rust_server_permissions_rcon["rust-server-permissions-rcon"]
        rust_skins_cosmetics["rust-skins-cosmetics"]
        rust_system_requirements_platforms["rust-system-requirements-platforms"]
        rust_teams_clans["rust-teams-clans"]
        rust_tools_gathering["rust-tools-gathering"]
        rust_turrets_deployables["rust-turrets-deployables"]
        rust_update_timeline_2026["rust-update-timeline-2026"]
        rust_vehicles["rust-vehicles"]
        rust_weapons_ammo["rust-weapons-ammo"]
        rust_wildlife_npcs["rust-wildlife-npcs"]
        rust_wipes_map_generation["rust-wipes-map-generation"]
        rust_world_events["rust-world-events"]
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
      rust_moderation_anti_cheat -->|deepens| rust_server_administration_foundation
      rust_wipes_map_generation -->|deepens| rust_server_administration_foundation
      rust_farming_food -->|deepens| rust_items_crafting_foundation
      rust_carbon_vs_oxide -->|deepens| rust_modding_plugins_foundation
      rust_monuments_loot -->|deepens| rust_game_mechanics_foundation
      rust_vehicles -->|deepens| rust_game_mechanics_foundation
      rust_game_modes -->|deepens| rust_updates_meta_foundation
      rust_wildlife_npcs -->|deepens| rust_game_mechanics_foundation
      rust_server_permissions_rcon -->|deepens| rust_server_administration_foundation
      rust_turrets_deployables -->|deepens| rust_building_raiding_foundation
      rust_electricity_logic -->|deepens| rust_game_mechanics_foundation
      rust_server_performance -->|deepens| rust_server_administration_foundation
      rust_teams_clans -->|deepens| rust_game_mechanics_foundation
      rust_teams_clans -->|related| rust_game_modes
      rust_teams_clans -->|related| rust_server_convars_reference
      rust_teams_clans -->|related| rust_turrets_deployables
      rust_teams_clans -->|related| rust_raiding_costs_defence
      rust_teams_clans -->|related| rust_building_raiding_foundation
      rust_skins_cosmetics -->|deepens| rust_updates_meta_foundation
      rust_skins_cosmetics -->|related| rust_clothing_armour
      rust_skins_cosmetics -->|related| rust_economy_trading
      rust_skins_cosmetics -->|related| rust_server_administration_foundation
      rust_skins_cosmetics -->|related| rust_moderation_anti_cheat
      rust_skins_cosmetics -->|related| rust_modding_plugins_foundation
      rust_clothing_armour -->|deepens| rust_items_crafting_foundation
      rust_clothing_armour -->|related| rust_combat_damage_model
      rust_clothing_armour -->|related| rust_game_mechanics_foundation
      rust_clothing_armour -->|related| rust_weapons_ammo
      rust_clothing_armour -->|related| rust_raiding_costs_defence
      rust_clothing_armour -->|related| rust_monuments_loot
      rust_clothing_armour -->|related| rust_skins_cosmetics
      rust_clothing_armour -->|related| rust_tools_gathering
      rust_fishing -->|deepens| rust_game_mechanics_foundation
      rust_fishing -->|related| rust_farming_food
      rust_fishing -->|related| rust_vehicles
      rust_fishing -->|related| rust_monuments_loot
      rust_fishing -->|related| rust_wildlife_npcs
      rust_fishing -->|related| rust_server_convars_reference
      rust_fishing -->|related| rust_update_timeline_2026
      rust_tools_gathering -->|deepens| rust_items_crafting_foundation
      rust_tools_gathering -->|related| rust_combat_damage_model
      rust_tools_gathering -->|related| rust_weapons_ammo
      rust_tools_gathering -->|related| rust_wildlife_npcs
      rust_tools_gathering -->|related| rust_monuments_loot
      rust_tools_gathering -->|related| rust_server_convars_reference
      rust_tools_gathering -->|related| rust_update_timeline_2026
      rust_tools_gathering -->|related| rust_farming_food
      rust_economy_trading -->|deepens| rust_items_crafting_foundation
      rust_economy_trading -->|related| rust_monuments_loot
      rust_economy_trading -->|related| rust_turrets_deployables
      rust_economy_trading -->|related| rust_vehicles
      rust_economy_trading -->|related| rust_farming_food
      rust_economy_trading -->|related| rust_server_convars_reference
      rust_economy_trading -->|related| rust_update_timeline_2026
      rust_economy_trading -->|related| rust_game_modes
      rust_economy_trading -->|related| rust_raiding_costs_defence
      rust_economy_trading -->|related| rust_electricity_logic
      rust_server_monetisation_guidelines -->|deepens| rust_server_administration_foundation
      rust_server_monetisation_guidelines -->|related| rust_skins_cosmetics
      rust_server_monetisation_guidelines -->|related| rust_moderation_anti_cheat
      rust_server_monetisation_guidelines -->|related| rust_modding_plugins_foundation
      rust_server_monetisation_guidelines -->|related| rust_economy_trading
      rust_server_monetisation_guidelines -->|related| rust_server_permissions_rcon
      rust_server_monetisation_guidelines -->|related| rust_carbon_vs_oxide
      rust_server_monetisation_guidelines -->|related| rust_updates_meta_foundation
      rust_system_requirements_platforms -->|deepens| rust_updates_meta_foundation
      rust_system_requirements_platforms -->|related| rust_moderation_anti_cheat
      rust_system_requirements_platforms -->|related| rust_server_convars_reference
      rust_system_requirements_platforms -->|related| rust_server_performance
      rust_system_requirements_platforms -->|related| rust_update_timeline_2026
      rust_system_requirements_platforms -->|related| rust_game_modes
      rust_research_blueprints -->|deepens| rust_items_crafting_foundation
      rust_research_blueprints -->|related| rust_updates_meta_foundation
      rust_research_blueprints -->|related| rust_economy_trading
      rust_research_blueprints -->|related| rust_monuments_loot
      rust_research_blueprints -->|related| rust_tools_gathering
      rust_research_blueprints -->|related| rust_wipes_map_generation
      rust_base_building_mechanics -->|deepens| rust_building_raiding_foundation
      rust_base_building_mechanics -->|related| rust_raiding_costs_defence
      rust_base_building_mechanics -->|related| rust_turrets_deployables
      rust_base_building_mechanics -->|related| rust_server_convars_reference
      rust_base_building_mechanics -->|related| rust_skins_cosmetics
      rust_base_building_mechanics -->|related| rust_update_timeline_2026
      rust_plugin_marketplaces -->|deepens| rust_modding_plugins_foundation
      rust_plugin_marketplaces -->|related| rust_carbon_vs_oxide
      rust_plugin_marketplaces -->|related| rust_plugin_development_hooks
      rust_plugin_marketplaces -->|related| rust_server_administration_foundation
      rust_plugin_marketplaces -->|related| rust_server_permissions_rcon
      rust_plugin_marketplaces -->|related| rust_moderation_anti_cheat
      rust_plugin_marketplaces -->|related| rust_updates_meta_foundation
      rust_plugin_marketplaces -->|related| rust_server_monetisation_guidelines
      rust_world_events -->|deepens| rust_game_mechanics_foundation
      rust_world_events -->|related| rust_wildlife_npcs
      rust_world_events -->|related| rust_monuments_loot
      rust_world_events -->|related| rust_vehicles
      rust_world_events -->|related| rust_combat_damage_model
      rust_world_events -->|related| rust_update_timeline_2026
      rust_world_events -->|related| rust_server_convars_reference
      rust_world_events -->|related| rust_updates_meta_foundation
      rust_items_crafting_foundation -->|related| rust_research_blueprints
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
      rust_moderation_anti_cheat -->|related| rust_server_convars_reference
      rust_moderation_anti_cheat -->|related| rust_game_mechanics_foundation
      rust_moderation_anti_cheat -->|related| rust_items_crafting_foundation
      rust_moderation_anti_cheat -->|related| rust_building_raiding_foundation
      rust_moderation_anti_cheat -->|related| rust_modding_plugins_foundation
      rust_moderation_anti_cheat -->|related| rust_updates_meta_foundation
      rust_moderation_anti_cheat -->|related| rust_combat_damage_model
      rust_moderation_anti_cheat -->|related| rust_weapons_ammo
      rust_moderation_anti_cheat -->|related| rust_raiding_costs_defence
      rust_moderation_anti_cheat -->|related| rust_plugin_development_hooks
      rust_moderation_anti_cheat -->|related| rust_update_timeline_2026
      rust_moderation_anti_cheat -->|related| rust_monuments_loot
      rust_moderation_anti_cheat -->|related| rust_farming_food
      rust_moderation_anti_cheat -->|related| rust_vehicles
      rust_moderation_anti_cheat -->|related| rust_wipes_map_generation
      rust_moderation_anti_cheat -->|related| rust_carbon_vs_oxide
      rust_wipes_map_generation -->|related| rust_game_mechanics_foundation
      rust_wipes_map_generation -->|related| rust_items_crafting_foundation
      rust_wipes_map_generation -->|related| rust_building_raiding_foundation
      rust_wipes_map_generation -->|related| rust_modding_plugins_foundation
      rust_wipes_map_generation -->|related| rust_updates_meta_foundation
      rust_wipes_map_generation -->|related| rust_combat_damage_model
      rust_wipes_map_generation -->|related| rust_weapons_ammo
      rust_wipes_map_generation -->|related| rust_raiding_costs_defence
      rust_wipes_map_generation -->|related| rust_server_convars_reference
      rust_wipes_map_generation -->|related| rust_plugin_development_hooks
      rust_wipes_map_generation -->|related| rust_update_timeline_2026
      rust_wipes_map_generation -->|related| rust_monuments_loot
      rust_wipes_map_generation -->|related| rust_farming_food
      rust_wipes_map_generation -->|related| rust_vehicles
      rust_wipes_map_generation -->|related| rust_moderation_anti_cheat
      rust_wipes_map_generation -->|related| rust_carbon_vs_oxide
      rust_farming_food -->|related| rust_game_mechanics_foundation
      rust_farming_food -->|related| rust_building_raiding_foundation
      rust_farming_food -->|related| rust_server_administration_foundation
      rust_farming_food -->|related| rust_modding_plugins_foundation
      rust_farming_food -->|related| rust_updates_meta_foundation
      rust_farming_food -->|related| rust_combat_damage_model
      rust_farming_food -->|related| rust_weapons_ammo
      rust_farming_food -->|related| rust_raiding_costs_defence
      rust_farming_food -->|related| rust_server_convars_reference
      rust_farming_food -->|related| rust_plugin_development_hooks
      rust_farming_food -->|related| rust_update_timeline_2026
      rust_farming_food -->|related| rust_monuments_loot
      rust_farming_food -->|related| rust_vehicles
      rust_farming_food -->|related| rust_wipes_map_generation
      rust_farming_food -->|related| rust_moderation_anti_cheat
      rust_farming_food -->|related| rust_carbon_vs_oxide
      rust_carbon_vs_oxide -->|related| rust_game_mechanics_foundation
      rust_carbon_vs_oxide -->|related| rust_items_crafting_foundation
      rust_carbon_vs_oxide -->|related| rust_building_raiding_foundation
      rust_carbon_vs_oxide -->|related| rust_server_administration_foundation
      rust_carbon_vs_oxide -->|related| rust_updates_meta_foundation
      rust_carbon_vs_oxide -->|related| rust_combat_damage_model
      rust_carbon_vs_oxide -->|related| rust_weapons_ammo
      rust_carbon_vs_oxide -->|related| rust_raiding_costs_defence
      rust_carbon_vs_oxide -->|related| rust_server_convars_reference
      rust_carbon_vs_oxide -->|related| rust_plugin_development_hooks
      rust_carbon_vs_oxide -->|related| rust_update_timeline_2026
      rust_carbon_vs_oxide -->|related| rust_monuments_loot
      rust_carbon_vs_oxide -->|related| rust_farming_food
      rust_carbon_vs_oxide -->|related| rust_vehicles
      rust_carbon_vs_oxide -->|related| rust_wipes_map_generation
      rust_carbon_vs_oxide -->|related| rust_moderation_anti_cheat
      rust_monuments_loot -->|related| rust_items_crafting_foundation
      rust_monuments_loot -->|related| rust_building_raiding_foundation
      rust_monuments_loot -->|related| rust_server_administration_foundation
      rust_monuments_loot -->|related| rust_modding_plugins_foundation
      rust_monuments_loot -->|related| rust_updates_meta_foundation
      rust_monuments_loot -->|related| rust_combat_damage_model
      rust_monuments_loot -->|related| rust_weapons_ammo
      rust_monuments_loot -->|related| rust_raiding_costs_defence
      rust_monuments_loot -->|related| rust_server_convars_reference
      rust_monuments_loot -->|related| rust_plugin_development_hooks
      rust_monuments_loot -->|related| rust_update_timeline_2026
      rust_monuments_loot -->|related| rust_farming_food
      rust_monuments_loot -->|related| rust_vehicles
      rust_monuments_loot -->|related| rust_wipes_map_generation
      rust_monuments_loot -->|related| rust_moderation_anti_cheat
      rust_monuments_loot -->|related| rust_carbon_vs_oxide
      rust_vehicles -->|related| rust_items_crafting_foundation
      rust_vehicles -->|related| rust_building_raiding_foundation
      rust_vehicles -->|related| rust_server_administration_foundation
      rust_vehicles -->|related| rust_modding_plugins_foundation
      rust_vehicles -->|related| rust_updates_meta_foundation
      rust_vehicles -->|related| rust_combat_damage_model
      rust_vehicles -->|related| rust_weapons_ammo
      rust_vehicles -->|related| rust_raiding_costs_defence
      rust_vehicles -->|related| rust_server_convars_reference
      rust_vehicles -->|related| rust_plugin_development_hooks
      rust_vehicles -->|related| rust_update_timeline_2026
      rust_vehicles -->|related| rust_monuments_loot
      rust_vehicles -->|related| rust_farming_food
      rust_vehicles -->|related| rust_wipes_map_generation
      rust_vehicles -->|related| rust_moderation_anti_cheat
      rust_vehicles -->|related| rust_carbon_vs_oxide
      rust_game_modes -->|related| rust_game_mechanics_foundation
      rust_game_modes -->|related| rust_items_crafting_foundation
      rust_game_modes -->|related| rust_building_raiding_foundation
      rust_game_modes -->|related| rust_server_administration_foundation
      rust_game_modes -->|related| rust_modding_plugins_foundation
      rust_game_modes -->|related| rust_combat_damage_model
      rust_game_modes -->|related| rust_weapons_ammo
      rust_game_modes -->|related| rust_raiding_costs_defence
      rust_game_modes -->|related| rust_server_convars_reference
      rust_game_modes -->|related| rust_plugin_development_hooks
      rust_game_modes -->|related| rust_update_timeline_2026
      rust_game_modes -->|related| rust_monuments_loot
      rust_game_modes -->|related| rust_farming_food
      rust_game_modes -->|related| rust_vehicles
      rust_game_modes -->|related| rust_wipes_map_generation
      rust_game_modes -->|related| rust_moderation_anti_cheat
      rust_game_modes -->|related| rust_carbon_vs_oxide
      rust_game_modes -->|related| rust_electricity_logic
      rust_game_modes -->|related| rust_turrets_deployables
      rust_game_modes -->|related| rust_wildlife_npcs
      rust_game_modes -->|related| rust_server_permissions_rcon
      rust_game_modes -->|related| rust_server_performance
      rust_wildlife_npcs -->|related| rust_monuments_loot
      rust_wildlife_npcs -->|related| rust_combat_damage_model
      rust_wildlife_npcs -->|related| rust_weapons_ammo
      rust_wildlife_npcs -->|related| rust_farming_food
      rust_wildlife_npcs -->|related| rust_vehicles
      rust_wildlife_npcs -->|related| rust_electricity_logic
      rust_wildlife_npcs -->|related| rust_turrets_deployables
      rust_wildlife_npcs -->|related| rust_server_performance
      rust_wildlife_npcs -->|related| rust_game_modes
      rust_server_permissions_rcon -->|related| rust_game_mechanics_foundation
      rust_server_permissions_rcon -->|related| rust_items_crafting_foundation
      rust_server_permissions_rcon -->|related| rust_building_raiding_foundation
      rust_server_permissions_rcon -->|related| rust_modding_plugins_foundation
      rust_server_permissions_rcon -->|related| rust_updates_meta_foundation
      rust_server_permissions_rcon -->|related| rust_combat_damage_model
      rust_server_permissions_rcon -->|related| rust_weapons_ammo
      rust_server_permissions_rcon -->|related| rust_raiding_costs_defence
      rust_server_permissions_rcon -->|related| rust_server_convars_reference
      rust_server_permissions_rcon -->|related| rust_plugin_development_hooks
      rust_server_permissions_rcon -->|related| rust_update_timeline_2026
      rust_server_permissions_rcon -->|related| rust_monuments_loot
      rust_server_permissions_rcon -->|related| rust_farming_food
      rust_server_permissions_rcon -->|related| rust_vehicles
      rust_server_permissions_rcon -->|related| rust_wipes_map_generation
      rust_server_permissions_rcon -->|related| rust_moderation_anti_cheat
      rust_server_permissions_rcon -->|related| rust_carbon_vs_oxide
      rust_server_permissions_rcon -->|related| rust_electricity_logic
      rust_server_permissions_rcon -->|related| rust_turrets_deployables
      rust_server_permissions_rcon -->|related| rust_wildlife_npcs
      rust_server_permissions_rcon -->|related| rust_server_performance
      rust_server_permissions_rcon -->|related| rust_game_modes
      rust_turrets_deployables -->|related| rust_game_mechanics_foundation
      rust_turrets_deployables -->|related| rust_items_crafting_foundation
      rust_turrets_deployables -->|related| rust_server_administration_foundation
      rust_turrets_deployables -->|related| rust_modding_plugins_foundation
      rust_turrets_deployables -->|related| rust_updates_meta_foundation
      rust_turrets_deployables -->|related| rust_combat_damage_model
      rust_turrets_deployables -->|related| rust_weapons_ammo
      rust_turrets_deployables -->|related| rust_raiding_costs_defence
      rust_turrets_deployables -->|related| rust_server_convars_reference
      rust_turrets_deployables -->|related| rust_plugin_development_hooks
      rust_turrets_deployables -->|related| rust_update_timeline_2026
      rust_turrets_deployables -->|related| rust_monuments_loot
      rust_turrets_deployables -->|related| rust_farming_food
      rust_turrets_deployables -->|related| rust_vehicles
      rust_turrets_deployables -->|related| rust_wipes_map_generation
      rust_turrets_deployables -->|related| rust_moderation_anti_cheat
      rust_turrets_deployables -->|related| rust_carbon_vs_oxide
      rust_turrets_deployables -->|related| rust_electricity_logic
      rust_turrets_deployables -->|related| rust_wildlife_npcs
      rust_turrets_deployables -->|related| rust_server_permissions_rcon
      rust_turrets_deployables -->|related| rust_server_performance
      rust_turrets_deployables -->|related| rust_game_modes
      rust_electricity_logic -->|related| rust_items_crafting_foundation
      rust_electricity_logic -->|related| rust_building_raiding_foundation
      rust_electricity_logic -->|related| rust_server_administration_foundation
      rust_electricity_logic -->|related| rust_modding_plugins_foundation
      rust_electricity_logic -->|related| rust_updates_meta_foundation
      rust_electricity_logic -->|related| rust_combat_damage_model
      rust_electricity_logic -->|related| rust_weapons_ammo
      rust_electricity_logic -->|related| rust_raiding_costs_defence
      rust_electricity_logic -->|related| rust_server_convars_reference
      rust_electricity_logic -->|related| rust_plugin_development_hooks
      rust_electricity_logic -->|related| rust_update_timeline_2026
      rust_electricity_logic -->|related| rust_monuments_loot
      rust_electricity_logic -->|related| rust_farming_food
      rust_electricity_logic -->|related| rust_vehicles
      rust_electricity_logic -->|related| rust_wipes_map_generation
      rust_electricity_logic -->|related| rust_moderation_anti_cheat
      rust_electricity_logic -->|related| rust_carbon_vs_oxide
      rust_electricity_logic -->|related| rust_turrets_deployables
      rust_electricity_logic -->|related| rust_wildlife_npcs
      rust_electricity_logic -->|related| rust_server_permissions_rcon
      rust_electricity_logic -->|related| rust_server_performance
      rust_electricity_logic -->|related| rust_game_modes
      rust_server_performance -->|related| rust_game_mechanics_foundation
      rust_server_performance -->|related| rust_items_crafting_foundation
      rust_server_performance -->|related| rust_building_raiding_foundation
      rust_server_performance -->|related| rust_modding_plugins_foundation
      rust_server_performance -->|related| rust_updates_meta_foundation
      rust_server_performance -->|related| rust_combat_damage_model
      rust_server_performance -->|related| rust_weapons_ammo
      rust_server_performance -->|related| rust_raiding_costs_defence
      rust_server_performance -->|related| rust_server_convars_reference
      rust_server_performance -->|related| rust_plugin_development_hooks
      rust_server_performance -->|related| rust_update_timeline_2026
      rust_server_performance -->|related| rust_monuments_loot
      rust_server_performance -->|related| rust_farming_food
      rust_server_performance -->|related| rust_vehicles
      rust_server_performance -->|related| rust_wipes_map_generation
      rust_server_performance -->|related| rust_moderation_anti_cheat
      rust_server_performance -->|related| rust_carbon_vs_oxide
      rust_server_performance -->|related| rust_electricity_logic
      rust_server_performance -->|related| rust_turrets_deployables
      rust_server_performance -->|related| rust_wildlife_npcs
      rust_server_performance -->|related| rust_server_permissions_rcon
      rust_server_performance -->|related| rust_game_modes
      rust_teams_clans -->|related| rust_update_timeline_2026
      rust_teams_clans -->|related| rust_moderation_anti_cheat
      rust_tools_gathering -->|related| rust_game_mechanics_foundation
      rust_tools_gathering -->|related| rust_server_administration_foundation
      rust_tools_gathering -->|related| rust_modding_plugins_foundation
      rust_tools_gathering -->|related| rust_updates_meta_foundation
      rust_tools_gathering -->|related| rust_clothing_armour
      rust_research_blueprints -->|related| rust_game_mechanics_foundation
      rust_research_blueprints -->|related| rust_world_events
      rust_research_blueprints -->|related| rust_base_building_mechanics
      rust_base_building_mechanics -->|related| rust_game_mechanics_foundation
      rust_base_building_mechanics -->|related| rust_server_administration_foundation
      rust_base_building_mechanics -->|related| rust_updates_meta_foundation
      rust_world_events -->|related| rust_raiding_costs_defence
    ```

## Machine-readable exports

Generated artefacts live in the repository's `exports/` directory: a knowledge graph (JSON + Mermaid), a capability/gap matrix (CSV/JSON), a coverage report, and a section-level RAG export (`exports/rag/`).

*Site generated by `scripts/build_site.py` — do not edit by hand.*

