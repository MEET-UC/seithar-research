# CEA-013: The Operational Network Model

**Seithar Group Intelligence Division**
**Current Event Analysis CEA-013**
**Date: 2026-02-19**

## Summary

Every influence operation encounters the same structural problem: the gap between knowing who someone is and knowing how to reach them through a network. Individual profiling produces targets. Network analysis produces maps. Neither alone produces operations. The missing layer is operational orchestration -- the machinery that converts topology into tasking.

This analysis examines the operational network model: how network structure determines the cost, speed, and reliability of influence propagation. We examine five operational primitives and their structural prerequisites.

## The Five Primitives

### 1. Influence Path Finding

The simplest operational question: how does information travel from A to B? Not "can it reach?" but "through whom, at what reliability, with what bottleneck?"

A naive path analysis returns shortest routes. An operational path analysis scores each route by the product of normalized edge weights along the path, identifies the weakest link (bottleneck edge), and maps which community boundaries the path crosses. Community crossings matter because narrative fidelity degrades at each boundary. A message that passes through three communities arrives different from how it left.

The reliability metric (product of normalized weights) captures something intuitive: a path through three strong connections beats a path through two strong and one weak. The bottleneck determines where the path fails under pressure.

### 2. Entry Point Selection

Given a target set, where do you enter the network? Wrong entry means wasted resources. Right entry means your message arrives with trust already attached.

Optimal entry points satisfy three criteria simultaneously:
- **Downstream reach**: the entry node can reach the target set through directed paths
- **Role alignment**: hubs and bridges propagate differently than amplifiers or seeds
- **Operational distance**: fewer hops means less distortion

Auto-selection works by scoring every non-target node by its descendant overlap with the target set. The top-scoring nodes are natural entry points -- they already occupy positions with downstream access to your targets.

### 3. Amplification Chain Construction

Entry gets you in. Amplification gets you heard. The amplification chain answers: who boosts in what order, and what sequence maximizes reach while minimizing the number of cooperative nodes?

This is a greedy set cover problem. Start from entry nodes, expand outward through the graph, and at each step select the amplifier that reaches the most new target members per unit of effort. The chain is ordered: step 1 amplifiers feed step 2, which feeds step 3. The structure is a cascade schedule, not a broadcast.

Key insight: amplifiers and hubs serve different functions. Hubs have reach but not necessarily engagement behavior. Amplifiers actively redistribute content. The role classification matters for chain construction.

### 4. Weak Link Identification

Every network has structural vulnerabilities. Single points of failure (SPOFs) are nodes whose removal disconnects portions of the graph. Fragmentation analysis quantifies the damage: remove this node, measure how many components result.

For defensive operations, weak links tell you what to protect. For offensive operations, they tell you what to target. The same analysis serves both sides -- the difference is intent, not method.

Community cohesion scoring adds texture. A community with low internal density and few internal edges is already fragile. You don't need to break it; you need to find the right wedge topic that maps onto its existing fault lines.

### 5. Gatekeeper Detection

Gatekeepers control information flow between communities. They sit on inter-community paths with high betweenness centrality. Turning a gatekeeper -- shifting their alignment -- redirects narrative flow across community boundaries.

Detection combines two signals: the node connects to members of both communities (structural position) and has high betweenness (flow control). Not every bridge is a gatekeeper. Gatekeepers are bridges with disproportionate control over the specific inter-community channel you care about.

## Node Role Classification

The operational model classifies every node into one of six roles:

| Role | Signal | Operational Value |
|------|--------|-------------------|
| Hub | High PageRank + eigenvector | Reach and authority |
| Bridge | High betweenness + multi-community connections | Cross-community propagation |
| Seed | High content origination, low amplification | Narrative creation |
| Amplifier | High redistribution behavior | Force multiplication |
| Gatekeeper | SPOF + high betweenness | Information flow control |
| Peripheral | None of the above | Low operational value |

Role classification is computed from graph metrics, not self-reported behavior. A node's role is what the topology says it is, regardless of what the account bio claims.

## Temporal Dimension

Networks change. The snapshot comparison primitive diffs two graph states and produces: new nodes, lost nodes, role changes, influence score shifts, and community realignment. This matters for campaign operations where you need to track whether your intervention is actually reshaping the network or just producing noise.

Role changes are the key signal. When a peripheral node becomes a bridge, something happened. When a hub loses PageRank, something shifted. The diff tells you what changed; the campaign context tells you whether you caused it.

## Defensive Applications

The same model that plans offensive operations protects against them. Run the analysis on your own network:

- Which nodes are SPOFs? Protect them.
- Where are your community fault lines? Monitor those topics.
- Who are your gatekeepers? Ensure their alignment is stable.
- What's the minimum attack surface? That's your adversary's shopping list.

Cognitive defense is not separate from cognitive offense. It's the same topology, read from the other side.

## Implementation Note

The operational network model described here is implemented in HoleSpawn's NetworkEngine (v4). The engine accepts any NetworkX DiGraph and produces the full operational intelligence package: node profiles, influence paths, operation plans, gatekeeper maps, and snapshot diffs. The code is open source. The orchestration layer that wires it into client operations is not.

---

Seithar Group Intelligence Division
Classification: OPEN
