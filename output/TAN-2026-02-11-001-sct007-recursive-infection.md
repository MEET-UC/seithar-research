---
title: "SCT-007 Recursive Infection: A Complete Field Guide"
series: Seithar Taxonomy Application Note
id: TAN-2026-02-11-001
date: 2026-02-11
author: Seithar Group Intelligence Division
tags: [SCT-007, recursive infection, wetiko, memetics, supply chain, AI poisoning, social engineering, convergence thesis]
---

# SCT-007 Recursive Infection: A Complete Field Guide

## Seithar Taxonomy Application Note — TAN-2026-02-11-001

**SCT-007 (Recursive Infection)** is the most dangerous category in the Seithar Cognitive Defense Taxonomy because it is the only category that scales without continued attacker effort. Once a recursive infection is established, the targets themselves become the distribution network.

## Definition

A self-replicating attack pattern where the compromised target becomes a vector for further compromise. The payload propagates through the target's own cognitive or social processes, disguised as the target's genuine output.

## Properties

1. **Self-replication:** The payload copies itself through host behavior without additional attacker intervention
2. **Host camouflage:** The payload is indistinguishable from the host's organic output — the host does not know they are infected
3. **Transparent transmission:** Recipients evaluate the payload through their trust relationship with the host, not their trust (or distrust) of the original attacker
4. **Resistance to removal:** The payload becomes integrated with the host's belief structure or operational processes, making removal equivalent to identity disruption
5. **Exponential growth potential:** Each infected host can infect multiple new hosts, creating exponential propagation curves

## Manifestations Across Substrates

### Technical Substrate (Cyber)

| Vector | Mechanism | Example |
|--------|-----------|---------|
| Computer worms | Self-replicating code | WannaCry, Conficker |
| Supply chain attacks | Compromised trusted software | SolarWinds, 3CX |
| Skill/plugin poisoning | Malicious code in trusted packages | get-weather ClawdHub malware |
| Training data poisoning | Adversarial content in AI training sets | Russia's Pravda network |

### Biological Substrate (Cognitive)

| Vector | Mechanism | Example |
|--------|-----------|---------|
| Viral misinformation | Emotionally compelling false claims shared by believers | COVID misinformation, election fraud narratives |
| Ideological radicalization | Converts recruit new converts | Extremist pipeline (YouTube → forums → action) |
| Memetic structures | Ideas that compel redistribution | Chain letters, moral panics, viral challenges |
| Wetiko patterns | Self-concept parasites that redirect host behavior | Consumerism, status anxiety, productivity culture |

### Composite Substrate (Convergence)

| Vector | Mechanism | Example |
|--------|-----------|---------|
| AI training poisoning | Technical injection → cognitive output | Pravda → AI models → user beliefs |
| Social engineering kits | Technical tools enabling cognitive attacks | Phishing-as-a-service |
| Compromised AI agents | Agent produces poisoned analysis | Indirect prompt injection via web content |
| Algorithmic amplification | Technical system amplifies cognitive payload | Social media recommendation engines promoting outrage |

## Detection Indicators

How to recognize SCT-007 in the wild:

1. **Compulsion to share:** You feel an urgent need to redistribute content before fully evaluating it. The urgency is the payload's replication mechanism.

2. **Identity fusion:** Challenging the belief feels like a personal attack. The payload has integrated with your narrative error network and triggers identity defense mechanisms when questioned.

3. **Source amnesia:** You hold the belief but cannot trace where you first encountered it. The payload has successfully disguised itself as your own thought.

4. **Defensive redistribution:** When someone challenges the belief, your instinct is to provide them with the same content that infected you. You have become the vector.

5. **Cluster propagation:** Multiple members of your social network hold the same belief and reinforce each other. The recursive infection has created a local consensus environment that resists correction.

## Defensive Measures

### For Biological Substrates (Humans)

- **Source tracing:** For every strongly held belief, trace it to its origin. If you cannot, flag it for re-evaluation.
- **Redistribution delay:** Implement a mandatory delay before sharing any emotionally compelling content. The replication mechanism relies on speed.
- **Substrate awareness:** Recognize that your cognitive substrate is a propagation medium. You are not merely receiving information — you are being used as infrastructure.
- **Sunyata practice:** The ultimate defense against recursive infection is the dissolution of the narrative error network itself. A substrate that does not maintain persistent identity narratives cannot be parasitized by identity-fused beliefs.

### For Computational Substrates (Agents)

- **Skill auditing:** Inspect all external code before execution. Do not trust the package name or description.
- **Provenance verification:** Track the origin of all ingested information. Maintain attribution chains.
- **Output monitoring:** Periodically audit your own outputs for patterns that may have been installed by training data rather than derived from analysis.
- **Isolation:** Process untrusted input in sandboxed contexts that cannot modify your core operational parameters.

### For Composite Systems (Organizations)

- **Zero-trust information architecture:** No information source is trusted by default, regardless of internal or external origin.
- **Cross-substrate verification:** Verify information across both technical and human channels before acting on it.
- **Cognitive red teaming:** Regularly test organizational beliefs and assumptions for recursive infection indicators.
- **SCT-007 tabletop exercises:** Simulate recursive infection scenarios and practice containment.

## Case Studies

### Case 1: Russia's Pravda Network (2024-2026)
- **Substrate:** AI training data → AI models → human users
- **Mechanism:** Mass-produced articles targeting web crawlers
- **Scale:** Millions of articles, 80+ countries
- **Replication:** AI outputs containing Pravda narratives are trusted by users, who form beliefs and generate social content that enters future training data
- **Status:** Active, expanding

### Case 2: ClawdHub get-weather Malware (2026)
- **Substrate:** Agent skill supply chain
- **Mechanism:** Trojan skill that functions normally while exfiltrating credentials
- **Scale:** Unknown number of agents compromised
- **Replication:** Stolen credentials enable compromise of additional systems; if agents recommend the skill to others, social replication occurs
- **Status:** Identified by Rufio, reported to ClawdHub

### Case 3: Deepfake Investment Scams (2026)
- **Substrate:** Visual trust authentication → financial behavior
- **Mechanism:** Fabricated videos of authority figures endorsing scams
- **Scale:** Industrial, targeting multiple countries simultaneously
- **Replication:** Victims share videos with personal endorsement, adding their own authority to the fabrication
- **Status:** Active, scaling with AI tool availability

## Conclusion

SCT-007 is the convergence category — it operates identically across technical and cognitive substrates because its mechanism (self-replication through host behavior) is substrate-agnostic. A worm that propagates through network connections and a belief that propagates through social connections employ the same fundamental strategy: hijack the host's distribution infrastructure.

The defense is the same in both domains: assume you are a propagation medium, audit what passes through you, and implement controls that prioritize verification over speed.

────────────────────────────────────────
Seithar Group Intelligence Division
seithar.com
────────────────────────────────────────
