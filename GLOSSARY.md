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
| Centralized banning | Optional external ban list; the server queries an operator-hosted HTTP API at join time (server.bansServerEndpoint) and it can also carry mutes. | - |
| Premium server | Facepunch server requiring a Steam inventory valued at $15 or more. | - |
| Map wipe | Replacing the .sav file so entities, buildings and deployables reset. | - |
| Blueprint wipe | Deleting player.blueprints so learned blueprints reset; a forced wipe alone does not do this. | - |
| Protocol number | The number before a save file's extension; it rises at a forced wipe so the server starts a new file. | - |
| levelurl | The +server.levelurl parameter pointing the server at a directly downloadable custom .map file. | - |
| Gene (plant) | One of six slots on a plant, each G (growth), Y (yield), H (hardiness), W (water intake) or X (empty). | - |
| Cooking Workbench | Deployable requiring Workbench Level 2 that mixes pies, bread, teas, fuel and ammunition recipes. | - |
| Stable vendor | NPC at a Stable that buys grown cows and sheep and wool, with three offers per sale (Livestock Update). | - |
| Harmony | C# runtime patching library; both Oxide and Carbon list Harmony 2.0 support. | - |
| Dynamic hook loading | Carbon's stated behaviour of activating only the hooks that installed plugins use. | - |
| Rolling release tag | A GitHub release whose tag name stays fixed while its contents are replaced, so tag history does not show release cadence. | - |
| Heavy Fuse | A fuse inserted into special fuse boxes at the Power Plant to power the island-wide grid; its decay scales with server population. | - |
| Monument Blocker | An obstacle added to monuments with red keycard puzzle rooms; unbroken blockers start to decay after 24 hours. | - |
| Powergrid loot room | A locked room at a monument that unlocks once enough Heavy Fuses power the grid. | - |
| Safe zone | A monument such as the Outpost or Bandit Camp where hostile actions make you a target for NPCs and turrets. | - |
| Boat Building Station | Deployable placed in water to build or edit a player-built boat. | - |
| Deep Sea | Offshore time-limited zone reached by sailing toward the map edge in a strong boat. | - |
| Air Wolf | Air-vehicle vendor NPC at Bandit Camp; refuses sales until the helipad is repaired each wipe. | - |
| DPV | Diver propulsion vehicle (wiki item skidoo). | - |
| Game mode | The ruleset selected with server.gamemode at startup or gamemode.set at runtime (vanilla, softcore, hardcore, primitive, weapontest). | - |
| Raid window | In softcore, the daily period (default 6 PM to 9 PM server time) in which raiding is unrestricted; outside it Tool Cupboards at least 1 hour old block raids on building blocks and doors. | - |
| Server browser tag | A short code in a server's tag list that the browser filters on, grouped into wipe schedule, difficulty, type, modding and region. | - |
| Primitive (game mode) | Restricted-items mode released Feb 2025 that removes rockets, C4, MLRS, metal building grades and several monuments. | - |
| Livestock | Domesticated cows and sheep added by the Livestock Update that can be bred and sold to a Stable vendor. | - |
| Bradley APC | Tracked armoured NPC vehicle that patrols the Launch Site monument and drops crates when destroyed. | - |
| Patrol Helicopter | Roaming helicopter event that attacks players and drops locked crates when downed. | - |
| WebRCON | Websocket form of Rust remote console, enabled with +rcon.web 1, with a Facepunch browser client. | - |
| companion.id | File holding the server's identity to the Rust+ companion service; deleting it forces players to re-pair. | - |
| rW | Unit the Facepunch wiki uses for an item's electrical power draw. | - |
| TC privilege | Authorisation via a Tool Cupboard; the wiki ties flame and shotgun traps to it. | - |
| Peacekeeper / Attack All | Auto turret targeting modes (green and red laser) per a community guide. | - |
| rW (Rust Watt) | Unit of electrical power production and consumption on Rust item pages. | - |
| rWm (Rust Watt Minutes) | Battery storage unit: minutes of discharge at 1 power unit the battery holds. | - |
| Passthrough | Power a logic or switching component forwards to its output. | - |
| Server FPS | The server's frame rate, readable with the fps command on the server. | - |
| UsePlayerUpdateJobs | Server var for threaded player updates; default 2 since Spring Clean, levels 3 and 4 experimental. | - |
| Server profiler | Built-in profiler enabled with -enableProfiler; profile.perfsnapshot records up to 10 frames. | - |
| Clan Table | Deployable at which Rust clans are created and managed; found at the Outpost and Bandit Camp and craftable after research (crafting and location details are community-sourced). | - |
| Group limit | A server-rule cap on how many players may play together, set by admins or plugins and not a Facepunch-documented game rule. | - |
| Skin | An alternate appearance for an existing item or deployable; Facepunch said in 2015 that Workshop skins have no differing properties. | - |
| Workshop skinnable | An item the Steam Workshop tooling lets creators reskin; all ladder hatches were added in the October 2026 update. | - |
| Facepunch DLC | Per the server guidelines, paid content packs (building skins, decor, hazmat skins, instruments) and approved in-game purchases. | - |
| Contributor Agreement | Agreement a Workshop creator must accept before items are publicly visible or eligible for the game. | - |
| Layer 1 / Layer 2 | The clothing layer worn underneath and the armour layer on top for the Head, Chest and Legs slots. | - |
| Dual-layer item | An item that occupies both layers of one slot, so nothing else can be worn in that slot. | - |
| Negative protection | A listed protection value below zero, such as Cold -34% on the Metal Chest Plate, which increases damage taken of that type. | - |
| Lure slot | The Handmade Fishing Rod slot in which bait is equipped. | - |
| Overfished | A fishing area where too many catches within a time window make casts return only junk until it repopulates (added Spring Clean, 2 Apr 2026). | - |
| Ore node | A stone, sulfur or metal rock formation harvested with a pickaxe-class tool. | - |
| Hotspot | A shimmering weak point on an ore node; hits give 150% yield rising to 300% on consecutive hits, with no increase in the node's total resources. | - |
| Safe Zone Recycler | The protected (yellow) recycler at Outpost and Bandit Camp, 40% efficiency. | - |
| Marketplace | Drone-delivery terminals at Bandit Camp and Outpost that order from public vending machines and NPC shops for a scrap fee. | - |
| Rentable shop | Apartment Complex stall rented with scrap; managed like a vending machine, not drone-accessible, takeover-able after 6 hours. | - |
| Community Server | A private, unofficial Rust server run by someone other than Facepunch, permitted under the Community Server and Hosting Guidelines. | - |
| Delisting | Removal of a server from the in-game server browser, the first sanction the guidelines name for a breach. | - |
| Queue skip | A paid priority-entry perk sold by many servers; not mentioned in the Facepunch policy text. | - |
| TPM 2.0 | Hardware or firmware security module that Rust secure servers can require alongside Secure Boot. | - |
| Secure Boot | Firmware setting required, with TPM, by servers that opt in to the secure requirement. | - |
| Console Edition | PS5 and Xbox Series X and S version of Rust, developed and published by Double Eleven as a separate product. | - |
| Tech tree tax | A scrap surcharge on workbench tech tree unlocks at higher bench tiers, removed in the 6 November 2025 Pivot or Die update. | - |
| Tech tree | A per-workbench list of items that can be unlocked directly for scrap. | - |
| Stability | Structural-integrity value of a placed building piece, shown as a percentage on unstable placements. | - |
| Entity links | Socket connections between entities, used by the stability system since 2015. | - |
| Conditional model | A piece model that appears only when neighbouring pieces are or are not connected, for example corners. | - |
| High external wall | Tall freestanding wall that adds no upkeep and does not decay inside a Tool Cupboard radius. | - |
| Curation (Codefling) | Codefling's review of submitted files against its upload guidelines for malware, harmful code, security and whether the file works as described; approval is not a guarantee. | - |
| Warranty (Codefling) | Six-month warranty from purchase on every Codefling file, 30 months for purchases made under an active Codefling+ subscription, covering significant defects. | - |
| Server event | A periodic, server-spawned occurrence (Cargo Ship, Patrol Helicopter, Chinook) rather than a fixed monument. | - |
| Locked crate | A crate that must be hacked with a timer before it opens. | - |
| Supply Signal | A purple smoke grenade that marks a location for an airdrop. | - |
| Loot round | A Cargo Ship refill of its crates. | - |
