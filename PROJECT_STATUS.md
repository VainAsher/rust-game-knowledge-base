# Project Status

- **Phase:** Release 1 complete, 8 Oct 2026. Six foundations plus thirty depth documents, all frozen. Game build checked: Livestock Update (1 Oct 2026).
- **Documents:** 36. Four are at v1.0.1 (items-crafting foundation, server-administration foundation, server-convars-reference, server-permissions-rcon); the rest v1.0.0. Confidence: 32 Medium, 4 Low (raiding-costs-defence, wildlife-npcs, teams-clans, plugin-marketplaces).
- **Low-confidence documents** are frozen with their conflicts and community-only sourcing stated openly; none has a Facepunch source for its core figures.
- **Next review:** after the 22 Oct 2026 mandatory update and the 5 Nov 2026 monthly update (inferred date).

## Revisions in v1.0.1 (8 Oct 2026)

- Items foundation: updated for Pivot or Die (6 Nov 2025): tech-tree tax removed, workbench scrap crafting cost removed, blueprint wipe. Workbench 2/3 research cost of 30 scrap rests on undated wiki pages.
- Server-administration foundation: query port row corrected from 28017 to 28016 per the wiki formula (server.queryport = 1 + higher of server.port or rcon.port). rcon.port default of 28015 still unverified on a live server.
- Convars reference: `relationshipmanager.maxteamsize` confirmed on the Facepunch Server Gamemodes wiki (Softcore: team size 4); no Facepunch source for the vanilla default.
- Permissions doc: open item about the query port tidied.

## Known gaps (all documented in each document's Open Questions)

- Structure HP, explosive damage, per-piece upkeep fractions, vanilla offline protection: no Facepunch source (only the 20% upkeep for high external walls and the 10-33% range, from Power Trip).
- Wildlife/NPC/Bradley/heli health: community-only, with a 9895.6 vs ~10,000 heli conflict and a Bradley 500 vs 1000 health discrepancy by date.
- Clans: member cap, ranks, `clan.maxmembercount` community-only. Vanilla team size 8 community-only.
- uMod licence and monetisation norms: unverified (umod.org returns 403; web archive unavailable). Codefling fee percentage unstated.
- Event spawn intervals, tier HP (2017), stability %, gather rates, recycler outputs (wiki 60/40% vs Power Trip 50/60/75%), NPC trade prices.
- Server monetisation policy was read via a summarising fetch; read facepunch.com/legal/servers directly before relying on it.
- Link checker: api.github.com is warn-only (60/h unauthenticated limit).
