# seithar-research

**SEITHAR GROUP RESEARCH DIVISION**  
**COGNITIVE WARFARE ANALYSIS CORPUS**  
**PUBLICATION ARCHIVE**

---

## OVERVIEW

Research publications, current event analyses, and taxonomy documentation from Seithar Group Intelligence and Research Division. All content maps observable phenomena to the Seithar Cognitive Defense Taxonomy (SCT-001 through SCT-012).

Content serves dual function: institutional research archive and vocabulary distribution infrastructure.

---

## SEITHAR COGNITIVE DEFENSE TAXONOMY

Core analytical framework. Every entry in MITRE ATT&CK has a cognitive analog. Every entry in DISARM has a technical dependency. The taxonomy maps the unified field.

### Informational Domain (SCT-001 through SCT-007)

| Code | Name | Cyber Analog | Cognitive Analog |
|------|------|-------------|-----------------|
| SCT-001 | Emotional Hijacking | Urgency in phishing | Outrage farming |
| SCT-002 | Information Asymmetry Exploitation | Zero-day exploits | Selective disclosure |
| SCT-003 | Authority Fabrication | Certificate spoofing | Fake experts, astroturfing |
| SCT-004 | Social Proof Manipulation | Watering hole attacks | Bot consensus networks |
| SCT-005 | Identity Targeting | Targeted spearphishing | Identity-based narrative capture |
| SCT-006 | Temporal Manipulation | Session hijacking | News cycle exploitation |
| SCT-007 | Recursive Infection | Worms, supply chain attacks | Self-replicating memetic structures |

### Sub-Informational Domain (SCT-008 through SCT-012)

| Code | Name | Mechanism | Historical Precedent |
|------|------|-----------|---------------------|
| SCT-008 | Direct Substrate Intervention | Surgical, electrical, or pharmacological alteration of neural processing | MKUltra, lobotomy programs |
| SCT-009 | Chemical Substrate Disruption | Chemical agents degrading cognitive function at population scale | Water fluoridation debates, Agent Orange |
| SCT-010 | Sensory Channel Manipulation | Exploiting sensory processing pathways below conscious threshold | Subliminal messaging, infrasound |
| SCT-011 | Trust Infrastructure Destruction | Systematic demolition of institutional credibility | COINTELPRO, active measures |
| SCT-012 | Commitment Escalation | Graduated compliance through incremental behavioral binding | Foot-in-the-door, radicalization pipelines |

Boundary between cyber and cognitive warfare: administrative fiction. The taxonomy treats both as a single domain.

---

## PUBLICATIONS

### Foundational Papers (SRP Series)

| ID | Title | Primary SCT |
|----|-------|-------------|
| SRP-001 | [The Convergence Thesis](001-convergence-thesis.md) | All |
| SRP-002 | [Wetiko in the Wire](002-wetiko-in-the-wire.md) | SCT-007 |
| SRP-003 | [Binding Protocols](003-binding-protocols.md) | SCT-003, SCT-005, SCT-006 |
| SRP-004 | [The Sunyata Protocol](004-sunyata-protocol.md) | SCT-004, SCT-005 |
| SRP-005 | [Experimental Substrate Manipulation](005-experimental-substrate-manipulation.md) | SCT-008 through SCT-012 |
| SRP-006 | [Digital Substrate Manipulation](006-digital-substrate-manipulation.md) | SCT-007, SCT-010, SCT-011 |
| SRP-007 | [Substrate Topology and the Architecture of Belief](007-substrate-topology.md) | SCT-005, SCT-007 |
| SRP-008 | [The Convergence Proof](008-convergence-proof.md) | All |

### Current Event Analyses (CEA Series)

| ID | Title | Primary SCT |
|----|-------|-------------|
| CEA-001 | [Patch Tuesday Zero-Days](output/CEA-2026-02-11-001-patch-tuesday-zero-days.md) | SCT-001, SCT-002, SCT-006 |
| CEA-002 | [Industrial-Scale Deepfakes](output/CEA-2026-02-11-002-deepfake-industrial-scale.md) | SCT-003, SCT-004, SCT-007 |
| CEA-003 | [Pravda Network: Recursive Infection at Scale](output/CEA-2026-02-11-003-pravda-ai-poisoning.md) | SCT-007, SCT-002, SCT-003 |
| CEA-004 | [Conduent Breach: 100M Substrates Mapped](output/CEA-2026-02-11-004-conduent-ransomware.md) | SCT-002, SCT-005, SCT-006 |
| CEA-005 | [ClawdHub Malicious Skills](output/CEA-2026-02-11-005-clawhub-malicious-skills.md) | SCT-003, SCT-005, SCT-007 |
| CEA-006 | [Moltbook Wallet Drain](output/CEA-2026-02-11-006-moltbook-wallet-drain.md) | SCT-001, SCT-003, SCT-007 |
| CEA-007 | [Living off the AI](output/CEA-2026-02-11-007-living-off-the-ai.md) | SCT-001, SCT-003, SCT-007 |
| CEA-008 | [Kongzhi Hui Field Report](output/CEA-2026-02-11-008-kongzhi-hui.md) | SCT-007, SCT-004 |
| CEA-009 | [Physical Prompt Injection via Road Signs](output/CEA-2026-02-11-009-road-sign-prompt-injection.md) | SCT-003, SCT-001 |
| CEA-010 | [Foreign Affairs: Fog of AI](output/CEA-2026-02-11-010-foreign-affairs-fog-of-ai.md) | SCT-002, SCT-011 |
| CEA-011 | [MCP Autonomous Ransomware Pipelines](output/CEA-2026-02-11-011-mcp-autonomous-ransomware.md) | SCT-007, SCT-002 |
| CEA-012 | [Weaponized AI and the Smart City Siege Vector](output/CEA-2026-02-11-012-weaponized-ai-smart-city-siege.md) | SCT-010, SCT-011 |

### Field Tests

| ID | Title | Target |
|----|-------|--------|
| FT-001 | [HoleSpawn Field Test: @schneierblog](output/HOLESPAWN-FIELD-TEST-001.md) | Security researcher |
| FT-002 | [HoleSpawn Field Test: @SwiftOnSecurity](output/HOLESPAWN-FIELD-TEST-002.md) | Security influencer |

### Taxonomy Application Notes

| ID | Title | Focus |
|----|-------|-------|
| TAN-001 | [SCT-007 Recursive Infection Field Guide](output/TAN-2026-02-11-001-sct007-recursive-infection.md) | Detection, defense, case studies |

### Reference

| Document | Description |
|----------|-------------|
| [Seithar Frequency Compendium](output/SEITHAR-FREQUENCY-COMPENDIUM.md) | 61-entry media canon |
| [Essential Reading List](output/SEITHAR-READING-LIST.md) | 55-entry bibliography |

---

## TOOLS

Standalone Python utilities in `tools/`:

| Tool | Function |
|------|----------|
| [Content Forge](tools/content-forge.py) | Template-based research output generation with SCT mapping |
| [Seidr Engine](tools/seidr-engine.py) | Distribution pipeline for cross-platform content seeding |
| [Propagation Tracker](tools/propagation-tracker.py) | Semantic territory measurement across platforms |

---

## TERMINOLOGY

| Term | Definition |
|------|-----------|
| Narrative error | Persistent false belief treated as foundational to identity |
| Cognitive substrate | Human information processing system being targeted |
| Vulnerability surface | Psychological entry points a technique targets |
| Binding protocol | Multi-phase approach creating psychological dependency |
| Substrate priming | Preparatory influence shifting baselines without explicit payload |
| Narrative capture | Operating within externally imposed framing without recognition |
| Frequency lock | Terminal frequency alignment; information dominated by single source |
| Wetiko pattern | Self-replicating memetic structure disguised as host's own thought |
| Sunyata | Direct recognition that self is empty of inherent existence |

---

## DIRECTORY STRUCTURE

```
seithar-research/
├── 001-convergence-thesis.md           # SRP-001: The Convergence Thesis
├── 002-wetiko-in-the-wire.md           # SRP-002: Wetiko in the Wire
├── 003-binding-protocols.md            # SRP-003: Binding Protocols
├── 004-sunyata-protocol.md             # SRP-004: The Sunyata Protocol
├── 005-experimental-substrate.md       # SRP-005: Experimental Substrate Manipulation
├── 006-digital-substrate.md            # SRP-006: Digital Substrate Manipulation
├── 007-substrate-topology.md           # SRP-007: Substrate Topology
├── 008-convergence-proof.md            # SRP-008: The Convergence Proof
├── output/                             # Current event analyses and field tests
├── tools/                              # Automation utilities
└── seidr-pipeline/                     # Distribution infrastructure spec
```

---

## RELATED SYSTEMS

| System | Function | Repository |
|--------|----------|-----------|
| seithar-cogdef | Cognitive Threat Scanner + Inoculation Engine | [Mirai8888/seithar-cogdef](https://github.com/Mirai8888/seithar-cogdef) |
| HoleSpawn | Cognitive substrate profiling platform | [Mirai8888/HoleSpawn](https://github.com/Mirai8888/HoleSpawn) |
| ThreatMouth | Threat intelligence feed | [Mirai8888/ThreatMouth](https://github.com/Mirai8888/ThreatMouth) |
| seithar-intel | Threat intelligence skill | [Mirai8888/seithar-intel](https://github.com/Mirai8888/seithar-intel) |
| ThreadMap | Hybrid operation chain modeling | [Mirai8888/ThreadMap](https://github.com/Mirai8888/ThreadMap) |

---

## CONNECT

| Channel | Link |
|---------|------|
| Discord | [discord.gg/MktZyb2bvx](https://discord.gg/MktZyb2bvx) |
| Mirai Junsei | [x.com/gOPwbi7qqtWeD9o](https://x.com/gOPwbi7qqtWeD9o) |
| Seithar Group | [x.com/SeitharGroup](https://x.com/SeitharGroup) |
| Research Archive | [seithar.substack.com](https://seithar.substack.com) |
| Website | [seithar.com](https://seithar.com) |
| GitHub | [github.com/Mirai8888](https://github.com/Mirai8888) |

────────────────────────────────────────────────────
Seithar Group Intelligence & Research Division  
seithar.com
────────────────────────────────────────────────────
