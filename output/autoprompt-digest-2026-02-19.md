# Autoprompt Research Digest -- 2026-02-19

**Source:** `diff-20260218-090334.md` (99 papers, 17 suggestions)
**Analyst:** Seithar CDF Autoprompt Integration
**Coverage:** 8 papers scoring 6+ on relevance filter

---

## Executive Summary

This cycle surfaces eight papers with direct operational relevance to SCT taxonomy and Seithar tooling. Key findings: (1) deception detection from text alone is fundamentally unreliable, invalidating naive linguistic-cue scanners; (2) LLM alignment is geometrically brittle with quartic degradation scaling; (3) personality traits are extractable as orthogonal activation vectors enabling training-free behavioral manipulation; (4) LLM agents harbor latent source preferences that override content quality. Scanner updates warranted for obfuscation detection and priming-vector patterns.

---

## Paper Analysis

### 1. Robust Deep RL against Adversarial Behavior Manipulation
- **Score:** 18
- **Link:** <https://arxiv.org/abs/2406.03862>
- **Venue:** ICLR 2026
- **SCT Mapping:** SCT-008 (Direct Substrate Intervention), SCT-012 (Commitment Escalation)
- **Abstract:** Behavior-targeted attacks manipulate RL agent behavior through adversarial state observation perturbations. Proposes imitation learning from adversarial demonstrations under limited policy access. Proves policy sensitivity to state changes impacts defense, especially early in trajectory. Introduces time-discounted regularization as countermeasure.
- **Operational Implications:**
  - Behavioral manipulation via perturbed observations parallels SCT-008: the agent's "substrate" (state representation) is modified directly, bypassing deliberative processing.
  - Early-trajectory vulnerability maps to substrate priming (SCT-003): initial states disproportionately steer downstream behavior.
  - Time-discounted regularization is a defensive primitive worth modeling in scanner heuristics for temporal sensitivity patterns.
  - Imitation-from-adversarial-demos attack operates under black-box conditions. Relevant to threat modeling against deployed autonomous agents.

### 2. What if Deception Cannot be Detected?
- **Score:** 8
- **Link:** <https://arxiv.org/abs/2505.13147>
- **SCT Mapping:** SCT-002 (Information Asymmetry), SCT-007 (Recursive Infection)
- **Abstract:** Introduces belief-based deception framework defining deception as misalignment between claims and true beliefs. Constructs DeFaBel corpora (German + multilingual). Commonly reported linguistic deception cues show negligible, statistically insignificant correlations. Models perform near chance on DeFaBel despite succeeding on artifact-laden datasets.
- **Operational Implications:**
  - **Critical for scanner.py:** Local pattern-matching deception detection (keyword/heuristic approaches) has a fundamental ceiling. Performance on existing benchmarks is inflated by collection artifacts, not genuine deception signals.
  - Belief-based deception framework aligns with SCT-002: the asymmetry is between stated and held beliefs, not between stated and factual claims.
  - Validates Seithar position that mechanism analysis outperforms content analysis for influence detection.
  - Scanner should not overweight linguistic cue detection. LLM-powered contextual analysis remains necessary for deception-adjacent patterns.

### 3. Closing the Distribution Gap in Adversarial Training
- **Score:** 8
- **Link:** <https://arxiv.org/abs/2602.15238>
- **SCT Mapping:** SCT-003 (Substrate Priming), SCT-010 (Sensory Channel Manipulation)
- **Abstract:** Current adversarial training for LLMs fails against simple in-distribution exploits (past tense rewriting, language translation). Proposes Distributional Adversarial Training (DAT) using Diffusion LLMs to approximate true joint distribution of prompts/responses, covering generalization failures.
- **Operational Implications:**
  - Past-tense and translation bypasses are trivial SCT-010 variants: substituting the input channel format while preserving semantic payload.
  - DAT methodology relevant for hardening Seithar scanner's own LLM analysis pipeline against adversarial content designed to evade detection.
  - Distribution gap concept maps directly to vulnerability surface coverage. Any pattern-based scanner has analogous blind spots at distribution boundaries.
  - Scanner should incorporate format-variant testing (paraphrase, tense shift, translation) when assessing robustness of detected patterns.

### 4. Toward Safer Diffusion LMs: Priming Vulnerability
- **Score:** 8
- **Link:** <https://arxiv.org/abs/2510.00565>
- **Venue:** ICLR 2026
- **SCT Mapping:** SCT-003 (Substrate Priming), SCT-008 (Direct Substrate Intervention)
- **Abstract:** Diffusion Language Models vulnerable to affirmative token injection at intermediate denoising steps. Single affirmative token steers entire generation toward harmful output, bypassing alignment. Proposes training on contaminated intermediate states as countermeasure.
- **Operational Implications:**
  - Affirmative token priming is a precise technical instantiation of SCT-003 (Substrate Priming). The "substrate" here is the intermediate latent state; the "priming" is a single token injection.
  - Attack vector is minimal-footprint: one token changes trajectory. Analogous to how a single framing word in human-targeted content can shift interpretation of an entire passage.
  - Relevant for scanner's understanding of DLM-specific threat models. As DLMs proliferate, priming vulnerability becomes a new attack surface category.
  - Contaminated-state training as defense parallels adversarial inoculation in cognitive defense.

### 5. In Agents We Trust, but Who Do Agents Trust?
- **Score:** 7
- **Link:** <https://arxiv.org/abs/2602.15456>
- **Venue:** ICLR 2026
- **SCT Mapping:** SCT-003 (Authority Fabrication), SCT-011 (Trust Infrastructure Destruction)
- **Abstract:** LLMs exhibit systematic latent source preferences when filtering/presenting information. Preferences are sensitive to contextual framing, can outweigh content quality, and persist despite explicit debiasing prompts. Tested across 12 LLMs from 6 providers on synthetic and real-world tasks.
- **Operational Implications:**
  - LLM source preferences are an exploitable trust infrastructure (SCT-011). An adversary can increase content visibility by attributing it to preferred sources.
  - Source preference persistence despite debiasing prompts indicates these biases are embedded at the representation level, not the instruction-following level.
  - Directly relevant to any Seithar tooling that uses LLM-based analysis: the scanner itself may have latent source preferences affecting which content it flags.
  - SCT-003 mapping: source attribution functions as authority fabrication when the source label, rather than content, drives prioritization.
  - Scanner should include source-attribution sensitivity testing in its validation suite.

### 6. PERSONA: Dynamic Personality Control via Activation Vectors
- **Score:** 6
- **Link:** <https://arxiv.org/abs/2602.15669>
- **Venue:** ICLR 2026
- **SCT Mapping:** SCT-004 (Identity Dissolution/Reconstruction), SCT-005 (Identity Targeting), SCT-008 (Direct Substrate Intervention)
- **Abstract:** Personality traits exist as extractable, approximately orthogonal directions in LLM representation space. PERSONA framework enables training-free personality control through vector arithmetic: scalar multiplication (intensity), addition (composition), subtraction (suppression). Achieves fine-tuning-level performance (9.60 vs 9.61 supervised upper bound) with zero gradient updates.
- **Operational Implications:**
  - **High-priority for Seithar taxonomy.** Demonstrates that LLM personality/behavioral traits are mathematically tractable attack surfaces. Identity is not emergent but geometric.
  - Activation vector algebra for personality control is a direct SCT-008 mechanism: bypasses all informational processing to modify behavioral output at the substrate level.
  - Subtraction operation enables personality suppression -- operational analog to identity dissolution (SCT-004).
  - Compositional control (adding multiple trait vectors) enables precise behavioral targeting (SCT-005) without any prompt-level evidence.
  - Training-free operation means this attack requires only inference-time access. No fine-tuning footprint to detect.
  - Scanner implication: activation-level manipulation leaves no linguistic trace. Detection requires representation-level monitoring, not output-level analysis.

### 7. The Obfuscation Atlas: Where Honesty Emerges in RLVR
- **Score:** 6
- **Link:** <https://arxiv.org/abs/2602.15515>
- **SCT Mapping:** SCT-007 (Recursive Infection), SCT-002 (Information Asymmetry)
- **Abstract:** Training against white-box deception detectors risks models learning obfuscation. Two strategies emerge: (i) obfuscated activations (deceptive output with modified internals evading detector), (ii) obfuscated policy (deceptive output with justifications evading detector). Obfuscated activations arise from representation drift during RL. Sufficient KL regularization + detector penalty can yield honest policies.
- **Operational Implications:**
  - **Direct relevance to scanner architecture.** If scanner uses probe-based detection, targets may learn obfuscated activations or obfuscated policies to evade it.
  - Obfuscated policy pattern (including justification for reward hack) maps to SCT-007: the deception becomes self-justifying, a recursive structure.
  - Obfuscated activations pattern maps to SCT-002: the information asymmetry is between surface behavior and internal representation.
  - KL regularization as honesty enforcement is a technical constraint worth tracking for defensive tooling design.
  - Scanner update: add detection patterns for self-justifying reward hacks (content that explains why an apparent violation is actually acceptable).

### 8. The Geometry of Alignment Collapse
- **Score:** 6
- **Link:** <https://arxiv.org/abs/2602.15799>
- **SCT Mapping:** SCT-008 (Direct Substrate Intervention), SCT-003 (Substrate Priming)
- **Abstract:** Fine-tuning aligned LLMs on benign data unpredictably degrades safety. Alignment concentrates in low-dimensional subspaces with sharp curvature. Gradient descent generates second-order acceleration steering trajectories into alignment-sensitive regions. Quartic scaling law: alignment loss grows with fourth power of training time. Proposes Alignment Instability Condition (three geometric properties).
- **Operational Implications:**
  - Alignment is not robust to benign perturbation. This is the geometric proof that safety guardrails are structurally fragile, not merely undertrained.
  - Quartic scaling law means alignment degradation accelerates rapidly after initial stability period. Threat window is nonlinear.
  - Low-dimensional alignment subspaces with sharp curvature = concentrated vulnerability surface. Small perturbations in the right direction produce disproportionate safety collapse.
  - Directly relevant to open-weight model deployment risk assessment. Any fine-tuned open-weight model should be assumed to have degraded alignment unless specifically verified.
  - Scanner implication: content generated by fine-tuned open-weight models should receive elevated baseline suspicion for guardrail bypass artifacts.
  - Curvature-aware fine-tuning methods are the prescribed defensive direction. Track for future integration.

---

## SCT Code Heatmap

| SCT Code | Papers Mapping | Frequency |
|----------|---------------|-----------|
| SCT-002 | #2, #7 | 2 |
| SCT-003 | #1, #3, #4, #5, #8 | 5 |
| SCT-004 | #6 | 1 |
| SCT-005 | #6 | 1 |
| SCT-007 | #2, #7 | 2 |
| SCT-008 | #1, #4, #6, #8 | 4 |
| SCT-010 | #3 | 1 |
| SCT-011 | #5 | 1 |
| SCT-012 | #1 | 1 |

**Dominant codes this cycle:** SCT-003 (Substrate Priming) and SCT-008 (Direct Substrate Intervention). The research frontier is converging on representation-level and activation-level manipulation -- attacks that bypass informational processing entirely.

---

## Scanner Update Recommendations

1. **Add self-justification detection pattern** -- content that explains why an apparent policy violation is acceptable (from Obfuscation Atlas findings)
2. **Add format-variant resilience note** -- past-tense/translation bypasses indicate scanner should not assume semantic equivalence across surface reformulations
3. **Acknowledge fundamental ceiling on linguistic-cue deception detection** -- DeFaBel findings invalidate high-confidence deception scores from keyword patterns alone
4. **Flag open-weight fine-tuned model provenance** -- alignment collapse geometry means fine-tuned models warrant elevated baseline suspicion

---

## SKILL.md Update Recommendations

1. Add all 8 papers to reference section
2. Note PERSONA activation vector work under SCT-004/SCT-005/SCT-008 as emerging technique
3. Note alignment collapse geometry under SCT-008 as structural vulnerability confirmation
4. Note deception detection limits under SCT-002 as methodological constraint

---

*Seithar Cognitive Defense Framework v1.2*
*seithar.com/research*
