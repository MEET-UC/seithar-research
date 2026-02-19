# Epistemic Garden / TheExGenesis - HoleSpawn Integration Scoping

**Date:** 2026-02-19
**Target:** https://github.com/TheExGenesis (Francisco Carvalho / Xiq)
**Purpose:** Identify concrete integration points with HoleSpawn's network analysis engine

---

## Repo Inventory

| Repo | Description | Language | Stars | Last Active |
|------|-------------|----------|-------|-------------|
| community-archive | Open tweet DB + API (Supabase). 17M+ crowdsourced tweets | TypeScript | Main project | Active |
| memetic-lineage | Idea lineage detector: tweet embedding clustering, quote-tweet lineage tracking | Python | 0 (fork) | Dec 2025 |
| new-birdseye | Tweet topic clustering powered by Community Archive | TypeScript | 0 (fork) | Jan 2026 |
| birdseye | Tweet topic clusters per account (Streamlit) | Python | 3 | Feb 2025 |
| serendipity | Surface deals from personal data | Python | 1 | Nov 2025 |
| embedding-atlas | Interactive embedding visualizations (fork of nomic-ai) | TypeScript | 0 (fork) | Dec 2025 |
| ca-top-qts | Top quoted tweets website ("tpot canon") | - | 0 | Nov 2025 |
| crm | Personal CRM | - | 0 | Dec 2025 |
| datamapplot | Data map visualizations (fork) | Python | 1 (fork) | Oct 2025 |

Forks of ML repos (whisper, trl, lm-evaluation-harness, etc.) are not relevant.

---

## Top 5 Integration Opportunities (Ranked by Value)

### 1. Community Archive Supabase API -> HoleSpawn Graph Builder

**Value: CRITICAL. This is the primary data source.**

The Community Archive exposes a public Supabase REST API with anonymous read access:

- **API Base:** `https://fabxmporizzqflnftavs.supabase.co`
- **Anon Key:** `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZhYnhtcG9yaXp6cWZsbmZ0YXZzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjIyNDQ5MTIsImV4cCI6MjAzNzgyMDkxMn0.UIEJiUNkLsW28tBHmG-RQDW-I5JNlJLt62CSk9D_qG8`

**DB Tables (confirmed from migrations and API docs):**

- `account` - username, account_id, created_at, display_name
- `profile` - bio, location, avatar_url
- `tweets` - tweet_id, account_id, full_text, created_at, retweet_count, favorite_count, reply_to_tweet_id, reply_to_user_id, reply_to_username
- `following` - account_id pairs (who follows whom)
- `follower` - account_id pairs (who is followed by whom)
- `tweet_urls` - tweet_id, expanded_url
- `quote_tweets` (view) - tweet_id, quoted_tweet_id, quoted_tweet_username (extracted from tweet_urls via regex on twitter.com/x.com status URLs)

**Per-user blob storage also available:** `https://fabxmporizzqflnftavs.supabase.co/storage/v1/object/public/archives/<username>/archive.json`

Returns JSON with: account, follower, following, profile, like, tweets.

**HoleSpawn Integration:**
- `graph_builder` can directly ingest the `following`/`follower` tables to build social graphs
- The `tweets` table with `reply_to_tweet_id` and `quote_tweets` view gives us reply chains and quote relationships, which map directly to influence_flow edges
- `created_at` timestamps on tweets enable temporal_analysis
- Write a Supabase client adapter for graph_builder that paginates through the REST API

**Concrete implementation:** A `CommunityArchiveSource` class that:
1. Fetches follower/following edges via Supabase REST (paginated, ~1000 rows/request)
2. Fetches quote_tweets view for idea propagation edges
3. Fetches tweet reply chains for conversation threading
4. Outputs nodes (accounts) and edges (follows, quotes, replies) in HoleSpawn's graph format

### 2. Memetic Lineage - Quote Tweet Propagation Analysis

**Value: HIGH. Direct overlap with HoleSpawn's influence_flow module.**

The `memetic-lineage` repo contains Python scratchpads that do exactly what HoleSpawn's influence tracking does, but from a different angle:

**Pipeline (from scratchpads/00_nov17_get_data.py and 01_nov18_threads.py):**

1. **Data source:** Parquet files with pre-computed tweet embeddings (1018-dimensional vectors from `CA_embeddings/embedding-queue/`)
2. **Dimensionality reduction:** UMAP (1018d -> 5d)
3. **Clustering:** KMeans (550 clusters) on UMAP space
4. **Thread reconstruction:** Walks `reply_to_tweet_id` chains upward to reconstruct full threads
5. **Quote counting:** Counts non-self-quotes per tweet, filters self-quotes by matching account_id

**Key data structures (from 01_nov18_threads.py):**
```
tweets DataFrame columns:
- tweet_id (int64)
- account_id (int64)
- username (string)
- full_text (string)
- created_at (datetime)
- reply_to_tweet_id (int64)
- quoted_tweet_id (int64)
- conversation_id (int64)
- favorite_count (int64)
- retweet_count (int64)
- quoted_count (int64, computed)
```

**Also ships:** `index_to_cluster_mapping.json` (8MB) mapping tweet indices to cluster IDs, and `top_quoted_tweets_all_time.txt` (141KB).

**HoleSpawn Integration:**
- Their quote-tweet lineage tracking is a subset of what influence_flow does. We can consume their cluster assignments as "topic labels" and overlay them on our influence graphs
- Their embedding parquet files (1018d vectors) could feed directly into our similarity-based edge construction
- The `count_quotes()` function is a simplified version of our influence scoring; we could replace it with our richer propagation model
- Their thread reconstruction (`get_thread_for_tweet()`) is useful utility code we could adapt

### 3. Birdseye - Per-Account Topic Clustering

**Value: MEDIUM. Provides pre-built topic models per user.**

Birdseye clusters a user's tweets into topics using embeddings + clustering. The original repo is a Streamlit app; new-birdseye is a TypeScript rewrite.

**Integration:**
- Topic cluster assignments per user could serve as node attributes in HoleSpawn graphs
- If we know what topics each user clusters into, we can build topic-specific influence subgraphs
- The deployed app at `https://theexgenesis--community-archive-birdseye-run.modal.run/` could be queried for per-user topic breakdowns

### 4. Follow Graph as Social Network Substrate

**Value: MEDIUM-HIGH. The follow graph is the backbone.**

The Community Archive stores follow/follower relationships. This is the raw social graph:
- Each `following` record is a directed edge (A follows B)
- Each `follower` record is a directed edge (B is followed by A)
- Combined with tweet interaction data (replies, quotes), this gives us a weighted multigraph

**HoleSpawn Integration:**
- Build the base social graph from follow edges
- Weight edges by interaction frequency (reply count, quote count between pairs)
- Run community detection on the weighted graph
- Use as substrate for all influence_flow and temporal_analysis computations

### 5. Embedding Atlas / DataMapPlot - Visualization Layer

**Value: LOW-MEDIUM. Visualization, not data.**

Francisco forked nomic-ai's embedding-atlas and lmcinnes' datamapplot. These are visualization tools for high-dimensional embeddings.

**Integration:**
- Could use embedding-atlas to visualize HoleSpawn's graph embeddings
- DataMapPlot for static visualizations of influence clusters
- Not a data integration, but a potential shared visualization pipeline

---

## Technical Specifics

### Data Formats

| Source | Format | Access Method |
|--------|--------|---------------|
| Community Archive DB | JSON via REST | Supabase REST API (GET with anon key) |
| Per-user archives | JSON blobs | Direct HTTP GET |
| Tweet embeddings | Parquet (1018d float vectors) | Not publicly hosted; need to request from Francisco or compute ourselves |
| Cluster mappings | JSON (index -> cluster_id) | In memetic-lineage repo |
| Top quoted tweets | Plain text | In memetic-lineage repo |

### Schema Compatibility

Community Archive's tweet schema maps cleanly to HoleSpawn:

| CA Field | HoleSpawn Concept |
|----------|-------------------|
| account_id | Node ID |
| tweet_id | Event ID |
| created_at | Timestamp (temporal_analysis) |
| reply_to_tweet_id | Directed edge (reply) |
| quoted_tweet_id | Directed edge (quote/propagation) |
| following/follower | Base graph edges |
| favorite_count | Engagement weight |
| retweet_count | Propagation signal |

### API Rate Limits

Supabase anon key gives read-only access. Default Supabase limits:
- 1000 rows per request (configurable with `limit` param)
- No documented rate limit on the anon key, but be respectful
- Pagination via `offset` or range headers

---

## Recommended Next Steps

1. **Write a `CommunityArchiveSource` adapter** for HoleSpawn's graph_builder. Start with the follow graph (simplest), then add quote-tweet edges. Estimated effort: 2-3 days.

2. **Request access to the tweet embeddings parquet files** from Francisco. These 1018d vectors would let us build similarity-based edges without recomputing embeddings. Reach out via the epistemic.garden Discord or Twitter (@exGenesis).

3. **Fork memetic-lineage and integrate** its quote-counting and thread-reconstruction logic into HoleSpawn's influence_flow module. The `count_quotes()` and `get_thread_for_tweet()` functions are immediately useful.

4. **Build a proof-of-concept** showing HoleSpawn's influence_flow running on Community Archive data. Specifically: pick a viral tweet, trace its quote-tweet propagation through the social graph, and visualize it. This would be compelling for collaboration.

5. **Propose a joint app** to Francisco for the Community Archive app ecosystem (documented in docs/apps.md). Something like "Influence Mapper" that shows how ideas propagate through the tpot community. This positions HoleSpawn as a Community Archive app and opens the door for deeper integration.

---

## Key Contacts

- **Francisco Carvalho (Xiq):** @exGenesis on Twitter, TheExGenesis on GitHub
- **Community Archive Discord:** Likely linked from https://www.community-archive.org/
- **DefenderOfBasic:** Active contributor building semantic search and toolkit on top of CA
