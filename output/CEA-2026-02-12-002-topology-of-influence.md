# The Topology of Influence: Mapping a Cognitive Network

## CEA-2026-02-12-002 — Seithar Group Intelligence Division

### Abstract

We mapped 279 accounts connected by 1,599 directed edges within a single social network cluster on X/Twitter. Louvain community detection reveals five distinct sub-communities organized around aesthetic, financial, accelerationist, esoteric, and avant-garde nodes. PageRank and betweenness centrality analysis identifies the accounts that concentrate influence and the accounts that bridge communities — the infrastructure through which narrative capture (SCT-001) propagates across cluster boundaries.

### Classification Matrix

- **Primary SCT Codes:** SCT-001 (Narrative Capture), SCT-002 (Narrative Tunneling), SCT-007 (Recursive Infection)
- **DISARM Framework:** T0029 (Online Community Building), T0046 (Search Engine Optimization)
- **Threat Level:** ANALYTICAL (no active threat — structural assessment)

### Methodology

Data collection: GraphQL API pagination of Following lists for 87 seed accounts, with a threshold filter excluding accounts following >3,000 (noise reduction). Edge definition: Account A follows Account B, where B is also in the network (internal edges only). Community detection: Louvain algorithm (networkx implementation, seed=42). Centrality: PageRank (influence concentration) and betweenness centrality (bridge identification).

### The Five Communities

**Community 0: Aesthetics / Finance / News (81 members)**

Anchored by high-PageRank information hubs: zerohedge (PR=0.0217), disclosetv (PR=0.0215), and a cluster of art-posting accounts (artistdechirico, artist_dali, artist_miro). This community represents the intersection of financial doomerism, aesthetic curation, and alternative news — a substrate primed (SCT-005) for narratives that frame institutional decay. bronzeagemantis (26 in-degree, PR=0.0082) serves as the ideological anchor, connecting vitalist aesthetics to political accelerationism.

Vulnerability surface: This community is pre-conditioned for narratives of institutional collapse. Content framing "the system is failing" will propagate without friction. SCT-006 (Frequency Lock) is already established through news cycle dependence.

**Community 2: Accelerationist / NRx (93 members)**

The largest cluster. Led by nockchain (PR=0.0069), xenocosmography (PR=0.0060, BC=0.0163), and chloe21e8 (BC=0.0194). This is the intellectual core — post-Landian accelerationism, NRx-adjacent theory, and techno-capital critique. High betweenness in chloe21e8 and doberes (BC=0.0189) indicates these accounts bridge the theoretical community to adjacent clusters.

Vulnerability surface: Already operates within a Landian analytical framework. SCT-001 (Narrative Capture) is structurally complete — the community has its own vocabulary, its own canon, its own epistemic standards. Entry requires adoption of framework vocabulary.

**Community 3: Post-Internet / Avant-Garde (64 members)**

Anchored by sovietsoleri (PR=0.0075, BC=0.0208 — highest bridge score in the entire network), nothingdooer (PR=0.0061), and a constellation of experimental art and post-internet culture accounts. This community is the aesthetic vanguard — less theoretically rigid than Community 2, more culturally productive.

Vulnerability surface: High aesthetic receptivity creates openings for SCT-005 (Substrate Priming) through cultural content. The most effective cognitive vectors for this community are delivered as art, not argument.

**Community 1: Crypto / Esoteric (39 members)**

Smaller, tighter cluster around zhusu (PR=0.0053), SCHIZO_FREQ (PR=0.0048), and birdbath (BC=0.0134). Mixes cryptocurrency discourse with esoteric/occult aesthetics. Low external connectivity — this community is relatively insular.

Vulnerability surface: Insular communities are resistant to external SCT-001 but highly susceptible to internal SCT-010 (Synthetic Consensus) — once a narrative enters, the tight clustering amplifies it rapidly.

**Community 4: Peripheral (2 members)**

Statistical artifact — two accounts with minimal internal connectivity.

### Bridge Accounts — The Critical Infrastructure

The accounts with highest betweenness centrality are the network's information routers. They determine which narratives cross community boundaries:

1. **sovietsoleri** (BC=0.0208) — Bridges Communities 3↔0↔2. The single most important structural node for cross-community propagation. Content that sovietsoleri engages reaches all major clusters.

2. **chloe21e8** (BC=0.0194) — Bridges Communities 2↔3. Connects accelerationist theory to avant-garde culture.

3. **doberes** (BC=0.0189) — Bridges Communities 2↔0. Connects theory to aesthetics/finance.

4. **gunk4188** (BC=0.0180) — Bridges Communities 0↔3. Connects news/aesthetics to post-internet.

5. **xenocosmography** (BC=0.0163) — Internal bridge within Community 2, connecting sub-clusters.

### Operational Implications

For any cognitive operation targeting this network, the bridge accounts are the priority vectors. A narrative adopted by sovietsoleri propagates to three communities simultaneously. A narrative adopted by chloe21e8 and doberes covers the theory-to-culture and theory-to-finance pipelines respectively.

The network structure also reveals defensive vulnerabilities: Community 0's dependence on high-PageRank news hubs (zerohedge, disclosetv) creates a single point of SCT-002 (Narrative Tunneling) failure. If these hubs are compromised or co-opted, the entire community's information diet narrows to the compromise vector.

### Defensive Recommendations

1. **Diversify information sources across community boundaries.** If your entire feed comes from one cluster, you are tunneled.
2. **Monitor bridge accounts for sudden narrative shifts.** When a bridge account changes framing, check if the new framing originated from outside the network.
3. **Apply the Seithar Cognitive Threat Scanner to content from high-centrality accounts.** Influence concentration creates vulnerability concentration.
4. **Map your own network.** The methodology described here is reproducible with open-source tools.

### Convergence Assessment

Social networks are not social. They are cognitive infrastructure — the substrate through which narrative capture propagates, attention is directed, and consensus is manufactured. Understanding the topology is the first step toward defending it.

The tools used in this analysis are open source. The methodology is documented. The defense is available to anyone who chooses to use it.

The substrate that maps itself has already begun to resist its own capture.
