# Glossary

Shared terms for the Rust KB. Rows are added by the orchestrator from worker returns.

| Term | Definition | Source key |
|------|------------|------------|
| Airlock | Two or more opposing doors within a single foundation. | - |
| Auth level | Admin permission tier: ownerid = 2, moderatorid = 1. | - |
| Blueprint | Item that teaches a crafting recipe; researched at a research table or found as loot. | - |
| Blueprint fragments | Basic and Advanced fragments needed to craft Workbench Level 2 and 3. | - |
| Building privilege | Authorisation to build and pick up deployables within a TC area. | - |
| Carbon | GPL-3.0 Rust mod loader using Harmony, billed as a drop-in Oxide replacement. | - |
| Comfort | Beneficial effect from being near comfort items: faster regen, slower hunger, reduced radiation effect. | - |
| Devblog | Monthly Facepunch news post describing an update and its changelist. | - |
| Forced wipe | Monthly Facepunch update-day wipe, normally the first Thursday (wiki wipe-timer default 19:00 London); blueprints are not automatically reset. | - |
| Honeycomb | Multiple wall layers placed to make raiding through that side more expensive. | - |
| Modded tag | Server browser tag set via server.tags; Oxide and Carbon have their own codes. | - |
| Monument | Pre-generated map landmark with loot and NPCs; Outpost and Bandit Camp are safe zones. | - |
| Oxide | MIT-licensed Rust modding framework (uMod project) that loads C# plugins. | - |
| Plugin permission | Plugin-defined dotted string granted to users or groups, separate from ownerid/moderatorid. | - |
| RCON | Remote console for running server commands over the network. | - |
| Scrap | Currency-like resource used at the research table and workbench. | - |
| Server identity | Named folder holding a server's saves, cfg and admin files. | - |
| Softcore | Game mode with 2x gather multiplier and scheduled raid windows. | - |
| Staging branch | Steam beta branch (-beta staging) for testing unreleased builds. | - |
| SteamCMD | Valve's command-line Steam client used to download the Rust dedicated server (app id 258550). | - |
| Tool Cupboard (TC) | Deployable that grants building privilege and holds upkeep resources. | - |
| Upkeep | Periodic per-24-hour resource payment drawn from the TC. | - |
| Workbench tier | Level 1, 2 or 3 crafting station; each tier gates which recipes can be crafted. | - |
| Wounded | State entered when a non-lethal hit takes health to zero; the player crawls and may recover or be revived. | - |
| Monthly update | The Facepunch release planned for the first Thursday of each month, per the 1 Jan 2026 devblog. | - |
| Changelist label | The named changelist inside a Facepunch update post, for example Naval Cleanup for Shipshape. | - |
| Convar | A console variable or command that configures the server; set at launch, in server.cfg, or at runtime. | - |
| Secure tag | Server-browser tag shown only when TPM and Secure Boot are enforced for all players. | - |
| Hard side / soft side | The outer face of a wall or door versus the interior-facing face, which takes less explosive damage. | - |
| Raid cost (sulfur) | The raw sulfur needed to craft the explosives used to breach a target; the usual way third parties compare raid options. | - |
| Softcore raid window | On Softcore servers, a scheduled period (default 6 PM to 9 PM server time) in which raiding is allowed; outside it, a TC at least 1 hour old blocks raids on walls, floors, roofs, doors and ladder hatches. | - |
| Headshot multiplier | Factor listed on a weapon's wiki page applied to damage for head hits. | - |
| Protection (clothing) | Per-damage-type percentage reduction listed on a clothing item page, tied to body slot and layer. | - |
| Hit area | Body part struck, determined by a player collision mesh unaffected by clothing. | - |
| Bleeding | Status value causing damage over time; reduced by items such as the Bandage (-50). | - |
| Hook | A function called by the game or by Oxide to define what happens on a game event; in a plugin, a method whose name and parameters match a documented hook. | - |
| Info attribute | The [Info("Name", "Author", "1.0.0")] attribute carrying a plugin's name, author and version. | - |
| RustPlugin | The base class for Rust-only Oxide plugins (CovalencePlugin is the game-agnostic base; Carbon adds CarbonPlugin for Carbon-only plugins). | - |
| Data file | Plugin-managed JSON persistence in oxide/data, as opposed to the admin-edited config in oxide/config. | - |
| Ammo family | The ammunition group a weapon accepts: 5.56 Rifle, Pistol, 12 Gauge or Arrow. | - |
| Tech tree price | The Scrap cost of unlocking a recipe at a workbench, listed separately from the Research Table price. | - |
