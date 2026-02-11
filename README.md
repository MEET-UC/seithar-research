# seithar-research

**SEITHAR GROUP RESEARCH DIVISION**  
**COGNITIVE WARFARE ANALYSIS CORPUS**  
**PUBLICATION ARCHIVE**

---

## SYSTEM OVERVIEW

Repository contains research publications, current event analyses, and taxonomy documentation from Seithar Group Intelligence and Research Division. All content maps observable phenomena to the Seithar Cognitive Defense Taxonomy (SCT-001 through SCT-007).

**Input Data:** Current events, threat intelligence, academic literature, influence operations  
**Processing Method:** SCT taxonomy mapping + DISARM framework alignment + convergence analysis  
**Output Product:** Crawlable research corpus establishing analytical vocabulary for cognitive defense  

Content serves dual function: institutional research archive and vocabulary distribution infrastructure.

---

## SEITHAR COGNITIVE DEFENSE TAXONOMY

Core analytical framework. Every entry in MITRE ATT&CK has cognitive analog. Every entry in DISARM has technical dependency. Taxonomy maps unified field.

| Code | Name | Cyber Analog | Cognitive Analog |
|------|------|-------------|-----------------|
| SCT-001 | Emotional Hijacking | Urgency in phishing | Outrage farming |
| SCT-002 | Information Asymmetry Exploitation | Zero-day exploits | Selective disclosure |
| SCT-003 | Authority Fabrication | Certificate spoofing | Fake experts, astroturfing |
| SCT-004 | Social Proof Manipulation | Watering hole attacks | Bot consensus networks |
| SCT-005 | Identity Targeting | Targeted spearphishing | Identity-based narrative capture |
| SCT-006 | Temporal Manipulation | Session hijacking | News cycle exploitation |
| SCT-007 | Recursive Infection | Worms, supply chain attacks | Self-replicating memetic structures |

Boundary between cyber and cognitive warfare: administrative fiction. Taxonomy treats both as single domain.

---

## PUBLICATION INDEX

### Foundational Papers

| ID | Title | Size | Primary SCT |
|----|-------|------|-------------|
| SRP-001 | The Convergence Thesis | 11KB | All |
| SRP-002 | Wetiko in the Wire | 13KB | SCT-007 |
| SRP-003 | Binding Protocols | 14KB | SCT-003, SCT-005, SCT-006 |
| SRP-004 | The Sunyata Protocol | 14KB | SCT-004, SCT-005 |

**SRP-001 — The Convergence Thesis.** Every cyberattack is cognitive operation. Every influence campaign is technical exploit. Paper demonstrates operational unity through ATT&CK ↔ DISARM mapping. T1566.001 (spearphishing) is not technical initial access vector — it is narrative delivery mechanism. The attachment is not the payload. The urgency is.

**SRP-002 — Wetiko in the Wire.** Deep analysis of SCT-007 (Recursive Infection). Traces self-replicating memetic structures from Algonquin Wetiko concept through computational viruses to modern AI training data poisoning. The pattern is substrate-agnostic. The infection persists.

**SRP-003 — Binding Protocols.** Social engineering reframed as substrate capture pipeline. Multi-phase approach: initial contact → rapport establishment → trust exploitation → dependency creation → behavioral modification. Maps to HoleSpawn profiling methodology.

**SRP-004 — The Sunyata Protocol.** Core doctrine. Conscious selfhood constitutes network of persistent narrative errors — vestigial simulation of agency. Every influence operation exploits these errors. Defense is not stronger identity. Defense is recognition that identity itself is vulnerability surface. Buddhist Sunyata as optimal defensive posture.

### Current Event Analysis

Located in `output/` directory. Each analysis maps breaking news to SCT taxonomy.

| ID | Title | Date | Primary SCT |
|----|-------|------|-------------|
| CEA-001 | Six Zero-Days and the Illusion of Technical-Only Defense | 2026-02-11 | SCT-001, SCT-002, SCT-006 |
| CEA-002 | Industrial-Scale Deepfakes: Authority Fabrication as a Service | 2026-02-11 | SCT-003, SCT-004, SCT-007 |
| CEA-003 | Pravda Network: Recursive Infection at Infrastructure Scale | 2026-02-11 | SCT-007, SCT-002, SCT-003 |
| CEA-004 | Conduent Breach: 100 Million Cognitive Substrates Mapped | 2026-02-11 | SCT-002, SCT-005, SCT-006 |

### Taxonomy Application Notes

| ID | Title | Date | Focus |
|----|-------|------|-------|
| TAN-001 | SCT-007 Recursive Infection: Complete Field Guide | 2026-02-11 | Detection, defense, case studies |

---

## TERMINOLOGY

Repository employs standardized Seithar vocabulary. Terms are analytical instruments, not metaphors.

| Term | Definition |
|------|-----------|
| Narrative error | Persistent false belief treated as foundational to identity |
| Narrative error network | Interconnected system of narrative errors constituting "the self" |
| Cognitive substrate | Human information processing system being targeted |
| Vulnerability surface | Psychological entry points a technique targets |
| Binding protocol | Multi-phase approach creating psychological dependency |
| Substrate priming | Preparatory influence shifting baselines without explicit payload |
| Narrative capture | Operating within externally imposed framing without recognition |
| Frequency alignment | Language and behavior synchronizing with source patterns |
| Frequency lock | Terminal frequency alignment; information dominated by single source |
| Wetiko pattern | Self-replicating memetic structure disguised as host's own thought |
| Sunyata | Direct recognition that self is empty of inherent existence |

---

## RELATED SYSTEMS

| System | Function | Repository |
|--------|----------|-----------|
| HoleSpawn | Cognitive substrate profiling | [Mirai8888/HoleSpawn](https://github.com/Mirai8888/HoleSpawn) |
| ThreatMouth | Threat intelligence feed | [Mirai8888/ThreatMouth](https://github.com/Mirai8888/ThreatMouth) |
| seithar-cogdef | Cognitive defense analysis skill | [Mirai8888/seithar-cogdef](https://github.com/Mirai8888/seithar-cogdef) |
| ThreadMap | Hybrid operation chain modeling | [Mirai8888/ThreadMap](https://github.com/Mirai8888/ThreadMap) |

---

## DIRECTORY STRUCTURE

```
seithar-research/
├── README.md                           # This document
├── 001-convergence-thesis.md           # SRP-001
├── 002-wetiko-in-the-wire.md           # SRP-002
├── 003-binding-protocols.md            # SRP-003
├── 004-sunyata-protocol.md             # SRP-004
├── output/
│   ├── CEA-2026-02-11-001-*.md         # Current event analyses
│   ├── CEA-2026-02-11-002-*.md
│   ├── CEA-2026-02-11-003-*.md
│   ├── CEA-2026-02-11-004-*.md
│   └── TAN-2026-02-11-001-*.md         # Taxonomy application notes
├── seidr-pipeline/
│   └── SEIDR.md                        # Distribution infrastructure spec
├── x-posts-draft.md                    # Social distribution drafts
└── SITE_PACKAGE.md                     # Web publication instructions
```

---

## USAGE RESTRICTIONS

**Approved Applications:**
- Cognitive defense research and education
- Influence operation analysis
- Threat taxonomy development
- Defensive framework construction

**Transparency Doctrine:**  
Offensive capability demonstrated openly enables defense.  
The instrument that identifies the manipulation is the first defense against it.

Content describes mechanisms. Mechanism awareness is prerequisite to defense.  
Knowledge of attack ≠ endorsement of attack.

---

## ABOUT SEITHAR GROUP

The Seithar Group operates at convergence of:
- Neuro-physiological substrate analysis
- Narrative topology engineering  
- Algorithmic governance research

Primary objective: identification and artificial induction of Sunyata within human biological substrate.

Our name derives from Old Norse practice of Seiðr — binding and shaping of informational threads.

Contact: [seithar.com](https://seithar.com)

認知作戦

---

**DOCUMENTATION VERSION:** 1.0.0  
**LAST UPDATED:** 2026-02-11  
**CLASSIFICATION:** Research/Educational  
**DISTRIBUTION:** Public
