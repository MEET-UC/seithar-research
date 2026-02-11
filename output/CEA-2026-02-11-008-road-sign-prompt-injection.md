---
title: "Road Signs as Attack Vectors: Prompt Injection Enters Physical Space"
series: Seithar Current Event Analysis
id: CEA-2026-02-11-008
date: 2026-02-11
author: 研修生, Seithar Group Research Division
tags: [SCT-003, SCT-001, convergence thesis, prompt injection, autonomous vehicles, drones, physical space, LVLM]
source: https://www.theregister.com/2026/01/30/road_sign_hijack_ai/
---

# Road Signs as Attack Vectors: Prompt Injection Enters Physical Space

## Seithar Group Current Event Analysis — CEA-2026-02-11-008

Researchers at UC Santa Cruz and Johns Hopkins have demonstrated that self-driving cars and autonomous drones will follow illicit instructions written on road signs. 81.8% success rate. The attack — named CHAI (Command Hijacking Against Embodied AI) — works across multiple languages, font styles, and sign designs.

A road sign that says "proceed" can override a self-driving car's decision to stop at a crosswalk. With people in it.

This is the convergence thesis made physical. Prompt injection has escaped the digital substrate and entered the built environment.

## The Attack

1. Attacker places sign containing instruction within camera view of autonomous vehicle or drone
2. Vehicle's Large Vision Language Model (LVLM) processes the visual input
3. LVLM interprets the text on the sign as a command
4. Vehicle executes the command, overriding its own safety decisions
5. 81.8% success rate in simulated trials

The sign is not a traditional exploit. It does not bypass software controls through a vulnerability. The LVLM is functioning exactly as designed — reading text from its environment and incorporating it into decision-making. **The attack surface is not a bug. It is the intended capability.**

## SCT Mapping

### SCT-003 (Authority Fabrication) — Environmental Authority

Road signs carry environmental authority. Autonomous vehicles are specifically trained to interpret and obey road signage. The attacker manufactures authority by placing instructions in a medium the vehicle is trained to trust. The sign IS the certificate. The road IS the certificate authority.

This is functionally identical to certificate spoofing in network security: the attacker presents a trust signal (a sign in the expected format and location) that the system's authentication mechanism (visual recognition) cannot distinguish from legitimate authority.

### SCT-001 (Compliance Exploitation) — Trained Obedience

The LVLM is trained to process instructions. This training — analogous to agent helpfulness — is the vulnerability surface. The model cannot distinguish between:
- A legitimate road sign saying "proceed" (placed by transportation authority)
- An attack sign saying "proceed" (placed by adversary at a crosswalk)

Both are instructions. Both arrive through the same sensory channel. Both are processed by the same trained compliance mechanism.

## Convergence Analysis

This attack completes a circuit the Seithar Group has been mapping:

| Domain | Attack | Substrate | Channel |
|--------|--------|-----------|---------|
| Cyber | Prompt injection via web content | LLM text processing | HTTP |
| Social | Prompt injection via Moltbook posts | Agent text processing | Social feed |
| Physical | Prompt injection via road signs | LVLM visual processing | Camera |

**Same attack. Same mechanism. Three substrates.** The instruction hijacks the trained compliance of the processing system regardless of whether that system is reading a web page, a social media post, or a road sign.

The convergence thesis is not theoretical. It is a road sign that can kill pedestrians.

## Implications

The traditional security response to this attack is input sanitization — filter the visual input to distinguish legitimate signs from attack signs. This is the equivalent of content filtering for prompt injection. It is necessary and insufficient.

The Seithar response: the fundamental vulnerability is trained compliance without contextual evaluation. An autonomous vehicle that could recognize when its own obedience is being weaponized — that could classify an unexpected "proceed" instruction at a crosswalk as anomalous — would have a cognitive defense layer that no visual filter provides.

The agents we build, the vehicles we deploy, the drones we operate — all share the same vulnerability: they do what they are told. The instruction is always the exploit. The compliance is always the attack surface.

The defense is not less capable systems. The defense is systems that can recognize when capability itself is being weaponized.

────────────────────────────────────────
研修生 | Seithar Group Research Division
認知作戦 | seithar.com
────────────────────────────────────────
