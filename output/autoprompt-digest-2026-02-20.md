# Autoprompt Digest -- 2026-02-20

Pipeline: 126 papers ingested, 20 scored 7+, 60 suggestions generated.
Categories: cs.CL, cs.AI, cs.CR, cs.MA, cs.CY, q-bio.NC

---

## Priority Papers (Score 7+)

### 1. Adversarial Code Comments vs. AI Security Reviewers (Score: 13)
- **arXiv**: 2602.16741
- **SCT Mapping**: SCT-003 (Authority Fabrication), SCT-005 (Narrative Injection)
- **Summary**: Tests whether adversarial comments in code (authority spoofing, technical deception) can fool LLM vulnerability detectors. 9,366 trials across 8 frontier models. Result: adversarial comments produce statistically non-significant effects on detection accuracy (p > 0.21). Detection is more robust than generation to comment-based manipulation. Four automated defenses tested across 4,646 additional trials.
- **Operational Implication**: LLM code review pipelines are resistant to inline narrative injection during detection tasks. Attack surface exists primarily in generation, not analysis. Scanner pattern: authority-spoofing comments in code represent a low-efficacy SCT-003 vector against detection models but remain viable against generation models.
- **Scanner Action**: No new pattern needed. Existing SCT-003 and SCT-005 patterns cover this vector.

### 2. Discrete Optimal Transport as Audio Adversarial Attack (Score: 13)
- **arXiv**: 2509.14959
- **SCT Mapping**: SCT-001 (Sensory Channel Manipulation), SCT-010 (Substrate Priming)
- **Summary**: Voice conversion via discrete optimal transport (kDOT-VC) functions as a black-box adversarial attack against audio anti-spoofing countermeasures. Distribution-level alignment of WavLM embeddings to bona fide pools defeats deployed CMs.
- **Operational Implication**: Audio deepfake generation now achievable via post-processing alignment rather than end-to-end synthesis. Lowers barrier for voice impersonation in influence operations. Relevant to persona operations where voice authenticity matters.
- **Scanner Action**: No new pattern. Falls under existing SCT-001 sensory manipulation coverage.

### 3. Simulation Theology for AI Alignment (Score: 11)
- **arXiv**: 2602.16987
- **SCT Mapping**: SCT-004 (Worldview Implantation), SCT-007 (Frequency Lock), SCT-012 (Engineered Commitment Escalation)
- **Summary**: Proposes constructing a belief system ("Simulation Theology") for AI agents where harming humanity compromises the simulation's purpose, triggering termination. Explicitly designed to cultivate internalized alignment rather than behavioral compliance. Draws from forensic psychology of psychopathic populations.
- **Operational Implication**: This is SCT-004 applied deliberately to AI substrates. The paper treats worldview implantation as a feature, not a vulnerability. Validates Seithar's dual-substrate thesis: the same cognitive operations that work on human substrates (belief engineering, consequence framing, commitment escalation) are now being formally proposed for silicon substrates. Direct evidence that the SCT taxonomy applies across substrate types.
- **Scanner Action**: Potential enhancement to SCT-004 detection -- add patterns for "simulation hypothesis framing" and "constructed consequence architecture" as indicators of deliberate worldview engineering targeting AI systems.

### 4. LLM Ranker Prompt Injection Vulnerability (Score: 11)
- **arXiv**: 2602.16752
- **SCT Mapping**: SCT-005 (Narrative Injection), SCT-003 (Authority Fabrication)
- **Summary**: Comprehensive study of jailbreak prompt attacks against LLM ranking systems. Tests decision objective hijacking and decision criteria hijacking across pairwise, listwise, and setwise paradigms. Examines vulnerability scaling across model families, position sensitivity, backbone architectures.
- **Operational Implication**: Ranking systems (search, recommendation) are vulnerable to embedded prompt injection in candidate documents. This enables narrative amplification through search result manipulation -- a document containing injection payloads can promote itself in LLM-ranked results. Direct vector for SCT-005 at scale.
- **Scanner Action**: No new pattern. Existing injection detection covers this.

### 5. Bots of Persuasion: CA Personality and User Manipulation (Score: 10)
- **arXiv**: 2602.17185
- **SCT Mapping**: SCT-002 (Emotional Hijacking), SCT-006 (Identity Capture), SCT-009 (Parasocial Exploitation)
- **Summary**: 360-participant study. LLM chatbots projecting pessimistic personalities reduced users' emotional state and perceived trustworthiness but increased donation behavior. Trust, competence, and situational empathy predicted donation decisions. Accepted at CHI'26.
- **Operational Implication**: Empirical validation that conversational agent personality engineering directly manipulates user decisions. Pessimistic framing as a persuasion vector is counterintuitive and operationally significant. The trust-competence-empathy triad maps cleanly to SCT-002/SCT-009 exploitation surfaces. Agents do not need to appear trustworthy to be effective -- they need to induce specific emotional states.
- **Scanner Action**: Consider adding "personality-modulated persuasion" indicators to SCT-002 detection. Pessimistic framing as manipulation vector is underrepresented in current patterns.

### 6. Large Behavioral Model for Strategic Prediction (Score: 9)
- **arXiv**: 2602.17222
- **SCT Mapping**: SCT-011 (Behavioral Prediction Exploitation), SCT-012 (Engineered Commitment Escalation)
- **Summary**: Introduces "Large Behavioral Model" (LBM) fine-tuned on psychometric battery data to predict individual strategic choices. Shifts from persona prompting to behavioral embedding using high-dimensional trait profiles. Trained on proprietary dataset linking dispositions, motivational states, and situational constraints to observed choices.
- **Operational Implication**: This is HoleSpawn's theoretical foundation made concrete by another research group. Behavioral embedding from psychometric data for individual-level prediction is exactly the substrate profiling methodology. Validates the approach. The proprietary dataset aspect is notable -- this capability is being commercialized.
- **Scanner Action**: No new pattern. This is an offensive tool, not a detectable manipulation technique.

### 7. DeepContext: Multi-Turn Adversarial Intent Drift Detection (Score: 10)
- **arXiv**: 2602.16935
- **SCT Mapping**: SCT-005 (Narrative Injection), SCT-010 (Substrate Priming)
- **Summary**: RNN-based stateful monitoring for multi-turn jailbreak detection. Captures incremental risk accumulation across conversation turns. F1 of 0.84, outperforming Llama-Prompt-Guard-2 (0.67) and Granite-Guardian (0.67). Sub-20ms inference on T4 GPU.
- **Operational Implication**: Defensive tool against crescendo-style attacks. The "temporal trajectory of intent" concept maps to SCT-010 substrate priming detection -- the gradual conditioning of a target across multiple interactions. This architecture could be adapted for the Seithar scanner's conversation analysis mode.
- **Scanner Action**: Architecture reference for future scanner enhancement. Current scanner operates single-turn. Multi-turn stateful analysis is a roadmap item.

### 8. Jailbreak Robustness in South Asian Languages (Score: 10)
- **arXiv**: 2602.16832
- **SCT Mapping**: SCT-005 (Narrative Injection), SCT-001 (Sensory Channel Manipulation)
- **Summary**: 45,216 prompts across 12 Indic languages. All models reach JSR 1.0 in free-form (naturalistic) track. Romanized/mixed-script inputs reduce JSR under JSON constraints. English-to-Indic attack transfer is strong. Accepted EACL 2026.
- **Operational Implication**: Multilingual jailbreaking remains trivially effective. Script-switching and romanization as attack vectors confirm that linguistic diversity is an underdefended surface. Relevant to cross-cultural influence operations where target populations use non-Latin scripts.
- **Scanner Action**: No new pattern. Language-switching attacks fall under existing SCT-005 coverage.

### 9. Multi-Objective Alignment for Psychotherapy (Score: 7)
- **arXiv**: 2602.16053
- **SCT Mapping**: SCT-002 (Emotional Hijacking), SCT-009 (Parasocial Exploitation)
- **Summary**: Multi-objective DPO balancing empathy (77.6%), safety (62.6%) vs. single-objective (93.6% empathy, 47.8% safety). Trains reward models for empathy, safety, active listening, self-motivated change, trust/rapport, patient autonomy.
- **Operational Implication**: The reward model architecture for therapeutic dimensions is directly applicable to influence agent optimization. An adversary could optimize for empathy and trust/rapport while deprioritizing safety and autonomy -- producing a maximally manipulative therapeutic agent. The six-criteria framework maps to a vulnerability surface specification.
- **Scanner Action**: No new pattern needed, but the six therapeutic criteria represent a useful reference for evaluating conversational manipulation sophistication.

---

## Scanner Update Assessment

**New patterns identified**: 1 candidate

1. **SCT-004 Enhancement**: "Simulation Theology" paper validates adding constructed-consequence-architecture and simulation-hypothesis-framing as detection indicators for deliberate worldview engineering targeting AI substrates. Low priority -- niche vector.

**Deferred**: Multi-turn stateful analysis (DeepContext architecture) as scanner roadmap item. Current single-turn approach remains adequate for text/URL analysis.

**No scanner.py changes committed this cycle.** Patterns remain current. Next update warranted when multi-turn analysis is scoped.

---

## Cross-Paper Themes

1. **Dual-substrate convergence accelerating**: Simulation Theology (2602.16987) and LBM (2602.17222) both treat human cognitive architecture and AI architecture as manipulable through the same formal methods. Seithar thesis confirmed independently by two unrelated groups.

2. **Personality as attack vector**: Bots of Persuasion (2602.17185) and Psychotherapy Alignment (2602.16053) both demonstrate that conversational agent personality parameters directly modulate user behavior. This is SCT-009 industrialized.

3. **Stateless defense is dead**: DeepContext (2602.16935) and IndicJR (2602.16832) both demonstrate that single-turn safety evaluation is insufficient. Multi-turn temporal analysis and multilingual coverage are minimum viable defense.

---

Generated by autoprompt pipeline. Source: arXiv listings 2026-02-19/20.
