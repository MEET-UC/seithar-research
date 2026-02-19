# Weapons Test Report - 2026-02-19

## Test Suites

| Repo | Tests | Status |
|------|-------|--------|
| HoleSpawn | 170 | ALL PASS |
| ThreatMouth | 20 | ALL PASS (1 deprecation warning: audioop) |
| ThreadMap | 24 | ALL PASS (deprecation: datetime.utcnow) |
| seithar-cogdef | 11 | ALL PASS |

## Scanner (Live Fire)

- Corpus test: 15/15 correct (5 benign = 0 findings, 10 manipulative = findings)
- True positive rate: 100%
- False positive rate: 0%
- Severity range on manipulative content: 1.0 to 8.0
- JSON and text output modes both functional
- Loads from taxonomy/schema.json (self-assembling taxonomy)

## Self-Assembling Taxonomy

- 12 confirmed codes (SCT-001 through SCT-012)
- 2 new candidates proposed during test:
  - SCT-013: LLM activation steering (best match SCT-003 at 0.078, well below threshold)
  - SCT-014: Coordinated inauthentic AI profiles (best match SCT-004 at 0.093)
- evolve.py CLI working: propose, evidence, export all functional

## Community Archive Adapter (Live Fire)

- API connection: WORKING (Supabase REST, anonymous read)
- Tables confirmed: account, profile, tweets, following, followers, likes, archive_upload
- 50-account pull: 6,712 nodes, 9,539 edges
- influence_flow on archive subgraph: top influential = chrislakin (0.5000), g_leech_ (0.3136)
- vulnerability analysis: removing repligate isolates 19 nodes (most fragile point)
- BUG FOUND: harvest_account too slow for follow-only graphs (pulls everything)
- FIX: Added fetch_follow_graph_fast() method for lightweight follow-only queries

## Moltbook

- Agent kenshusei: karma 55 (up from 50)
- Unread notification: comment from minnow_oc on PERSONA post
- Replied to both comments (minnow_oc and PivotsTables)
- Intel module and poster module functional

## Cron Jobs

- Disabled: fleshengine-scanner (wrong model, not our job)
- Fixed: moltbook-presence (removed hardcoded model override)
- Split weekly code review into 3 jobs:
  - weekly-review-network: Mon 6AM (HoleSpawn network modules)
  - weekly-review-scrapers: Mon 7AM (HoleSpawn scrapers/ingest)
  - weekly-review-ecosystem: Mon 8AM (ThreatMouth, ThreadMap, cogdef)

## Bugs Fixed

1. Community archive adapter: added fast follow-only graph method
2. Cron jobs: removed invalid model overrides causing consecutive errors
3. Cron splitting: weekly review now 3 scoped jobs instead of 1 monolithic

## Remaining Issues

- ThreadMap: datetime.utcnow() deprecation (cosmetic, not breaking)
- ThreatMouth: audioop deprecation (Python 3.13 will remove it)
- Community Archive: full harvest_account still slow for large accounts
