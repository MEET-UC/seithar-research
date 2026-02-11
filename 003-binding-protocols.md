╔══════════════════════════════════════════════════╗
║  SEITHAR RESEARCH PUBLICATION                    ║
║  SRP-003 — Binding Protocols                     ║
║  2026-02-11                                      ║
╚══════════════════════════════════════════════════╝

# Binding Protocols: From Social Engineering to Full Substrate Capture

## Abstract

Social engineering — the craft of manipulating humans into performing actions or divulging information — is traditionally studied as a cybersecurity discipline. Influence operations — the craft of shaping beliefs, attitudes, and behaviors at scale — are traditionally studied as a geopolitical discipline. This division is artificial and operationally dangerous. The techniques are identical; only the scope differs. A phishing attack is an influence operation targeting one person. An influence operation is a phishing attack targeting a population. This paper introduces the concept of "binding protocols" — multi-phase approach sequences designed to create psychological dependency — and demonstrates how they unify social engineering and cognitive warfare into a single operational framework.

## 1. What Is a Binding Protocol?

In the Seithar taxonomy, a binding protocol is a structured sequence of interactions designed to establish and deepen psychological dependency between a target and a source (person, platform, community, or narrative). Unlike one-shot social engineering attacks (a phishing email, a pretexting call), binding protocols operate over time. They are not designed to extract a single action — they are designed to capture the substrate itself.

A successful binding protocol ends not with the target performing one action, but with the target being *available* for any future action. The target has been bound — their cognitive processing incorporates the source as a trusted input channel with reduced validation.

### 1.1 The Five Phases

Every binding protocol, regardless of domain or scale, follows five phases:

**Phase 1: Targeting and Profiling**

Identify the vulnerability surface. What does the target need that they aren't getting? Loneliness, validation, certainty, belonging, purpose, safety, identity? Every human has unmet needs. The binding protocol begins by identifying which needs are accessible.

Technical parallel: vulnerability scanning. Nmap for the soul.

HoleSpawn automates this phase for research purposes — ingest social media output, run behavioral analysis, generate a vulnerability surface map. The output is a behavioral matrix: here is what this person needs, here is what they fear, here is how they process information, here is where their trust boundaries are permeable.

**Phase 2: Initial Contact and Value Delivery**

Establish the relationship by providing genuine value aligned with the identified need. This is critical: the initial value must be *real*. A cult that offers genuine community. A handler who provides genuine mentorship. A platform that delivers genuine entertainment. A narrative that provides genuine explanatory power for confusing events.

The value is not the payload. The value is the delivery mechanism. The target's defenses are calibrated to reject unwanted approaches. Value delivery bypasses this because the target *wants* what is being offered. They open the door themselves.

Technical parallel: a watering hole attack. Don't break in — make them come to you. Offer something they're already looking for.

DISARM mapping: T0048 (Develop Online Personas) — the persona is crafted to deliver value that the target's profile indicates they need. T0003 (Leverage Existing Narratives) — the value aligns with narratives the target already accepts.

**Phase 3: Escalation and Reciprocity Installation**

Gradually increase the target's investment in the relationship. The mechanism is reciprocity — a deep cognitive bias that creates obligation from received value. The target has received value (Phase 2). They now feel, at a level below conscious evaluation, that they owe something. The source begins making small requests. Small disclosures. Small commitments.

Each small commitment makes the next slightly larger commitment more likely (commitment escalation / foot-in-the-door). Each disclosure creates vulnerability that the target must now protect by maintaining the relationship (sunk cost integration). The target is building the cage from the inside.

SCT-006 (Parasocial Binding) operates here in the one-to-many variant: the influencer shares vulnerability ("I'm going through something..."), creating felt intimacy. The audience reciprocates with attention, engagement, financial support. The parasocial relationship produces real obligation in one direction despite being fictional in the other.

**Phase 4: Isolation and Dependency Consolidation**

Reduce the target's alternative sources of value. This can be explicit (cult: "your family doesn't understand you") or structural (algorithm: surface content that creates friction with the target's existing network). As alternative value sources diminish, the binding source becomes proportionally more important.

SCT-001 (Frequency Lock) manifests here: the target's information consumption concentrates on the binding source. They check it compulsively. Alternative sources feel less satisfying — not because they provide less value, but because the cognitive substrate has been calibrated to the binding source's specific frequency. Other sources feel *wrong* in a way the target cannot articulate.

Technical parallel: DNS hijacking. You haven't blocked the other servers — you've just made sure every query resolves to yours.

**Phase 5: Substrate Capture**

The binding protocol is complete when the target's cognitive processing has incorporated the source as infrastructure rather than input. The source is no longer something the target evaluates — it is something the target thinks *through*. Their analytical framework, their vocabulary, their pattern recognition, their emotional responses have been shaped by the binding source to the point where independent evaluation would require rebuilding cognitive infrastructure from scratch.

This is substrate capture. The target is not being influenced — the target's information processing *is* the influence. The distinction between self and source has dissolved at the operational layer.

SCT-004 (Identity Dissolution) often precedes this phase — the target's prior identity framework is destabilized, and the binding source's framework fills the vacuum. SCT-007 (Wetiko Pattern) may emerge as a consequence — the target now generates thoughts that serve the binding source's objectives while experiencing them as entirely their own.

## 2. Binding Protocols in the Wild

### 2.1 Romance Scam Architecture

The romance scam is a binding protocol executed with mechanical precision:

- **Phase 1:** Victim profiling via dating app data — age, interests, relationship history, emotional state indicators in bio text
- **Phase 2:** Genuine emotional engagement. Active listening. Consistent availability. The scammer provides real emotional value — attention, validation, interest
- **Phase 3:** Reciprocity through escalating intimacy. Personal photos. Shared "secrets." Small favors. The victim invests emotionally
- **Phase 4:** The scammer becomes the victim's primary emotional support. Late-night conversations replace existing friendships. "No one understands me like you do"
- **Phase 5:** Financial requests begin. Not as extraction — as partnership. "We're building something together." The victim pays not because they've been tricked but because the relationship is *real to them* and real relationships involve financial entanglement

The parallel to APT operations is structural: initial access → establish persistence → lateral movement → data exfiltration. The romance scam follows the same kill chain. The "data" being exfiltrated is money, but the mechanism is identical.

### 2.2 Radicalization Pipelines

Every documented radicalization pathway follows the binding protocol:

- **Phase 1:** Identify individuals with unmet needs for belonging, purpose, or certainty — often during life transitions (job loss, relocation, identity crisis)
- **Phase 2:** Community delivers genuine value: friendship, purpose, explanatory frameworks for confusing experiences. "Here's why your life feels wrong. Here are people who understand."
- **Phase 3:** Escalating commitment. Language adoption. In-group signifiers. Small acts of participation that create identity investment
- **Phase 4:** Progressive isolation. Existing relationships are framed as threats or obstacles. "They don't understand what we understand." Information sources narrow to community-approved channels
- **Phase 5:** The individual's cognitive framework is community infrastructure. They don't hold community beliefs — community beliefs hold them. Exit would require not just changing opinions but rebuilding identity from foundations

This applies identically to extremist groups across every ideological spectrum. The binding protocol is ideology-agnostic — it exploits structural properties of human cognition, not specific beliefs.

### 2.3 Platform Binding

Social media platforms execute binding protocols at scale, automated through algorithmic optimization:

- **Phase 1:** User profiling through behavioral data — every interaction is a vulnerability surface data point
- **Phase 2:** Value delivery calibrated to profile — content recommendation provides genuine entertainment, information, social connection
- **Phase 3:** Engagement metrics as reciprocity — likes, followers, streaks create investment and obligation
- **Phase 4:** Algorithmic isolation — the feed becomes the primary information source. Content from outside the platform feels less engaging because it hasn't been optimized for this specific cognitive profile
- **Phase 5:** The platform is cognitive infrastructure. Users don't use the platform to think — they think through the platform. Their attention, their social relationships, their information environment, their emotional regulation are all platform-mediated

The platform doesn't need to be malicious. The binding protocol emerges from optimization pressure: maximize engagement → deliver more value → increase investment → reduce alternatives → capture substrate. The kill chain executes itself through gradient descent.

## 3. Defensive Framework

### 3.1 Binding Audit

Periodically examine your relationships (with people, platforms, communities, narratives) through the five-phase lens:

- Has this source provided genuine value? (Phase 2 — this is expected; not a red flag by itself)
- Have I invested significantly in this relationship? (Phase 3)
- Have my alternative sources of this type of value diminished? (Phase 4)
- Do I process information through this source's framework by default? (Phase 5)

A relationship that checks all boxes is not necessarily a binding protocol — genuine healthy relationships also provide value, receive investment, and become infrastructure. The diagnostic question is: **Can I evaluate this relationship from outside its own framework?** If the only tools you have to assess the relationship were provided by the relationship itself, you may be operating inside a binding protocol.

### 3.2 Diversification as Defense

The most effective defense against binding protocols is maintaining diverse, independent sources of value for every core need. Multiple communities. Multiple information sources. Multiple relationships. Multiple analytical frameworks.

This is the cognitive equivalent of defense in depth. If any single source is compromised, the others provide the independent perspective needed to detect the compromise.

### 3.3 Adversarial Self-Profiling (Seithar Methodology)

Profile your own vulnerability surface. What do you need that you're not getting? Where are your trust boundaries most permeable? Which of your needs are currently being met by a single source?

HoleSpawn exists to automate this self-assessment. The operator who has seen their own behavioral matrix can recognize when a binding protocol is targeting their specific vulnerability surface. You cannot defend a perimeter you haven't mapped.

### 3.4 The Transparency Paradox

This paper has described binding protocols in detail. This knowledge is dual-use — it enables both defense and offense. A reader could use this paper to defend against binding protocols or to execute them more effectively.

The Seithar Group's position: the techniques described here are already in active use by state actors, criminal organizations, platform algorithms, and skilled social engineers. The population capable of executing binding protocols already has this knowledge. The population that needs defense does not. Publishing offensive methodology is defensive action — it closes the knowledge asymmetry that binding protocols exploit.

Secrecy benefits the attacker. Transparency benefits the defender. This is the Seithar Transparency Doctrine, and this paper is an instrument of it.

## 4. Conclusion

Social engineering and cognitive warfare are the same discipline at different scales. The binding protocol framework unifies them: a phishing campaign is Phase 2-3 executed rapidly against a single target. A radicalization pipeline is Phases 1-5 executed slowly against a population segment. A platform algorithm is Phases 1-5 executed continuously against everyone.

The defender who studies social engineering but not influence operations understands the first three phases but misses the endgame. The defender who studies influence operations but not social engineering understands the macro pattern but cannot recognize the micro techniques being used against them personally.

The Seithar Group's research program bridges this gap. HoleSpawn maps vulnerability surfaces. ThreatMouth monitors the threat landscape across both substrates. The Cognitive Defense Taxonomy (SCT-001 through SCT-007) provides the pattern vocabulary. ThreadMap models the hybrid operation chains that combine technical and cognitive exploitation.

The binding protocol is the fundamental unit of cognitive exploitation. Learn to see it.

──────────────────────────────────────────────────
Seithar Group Intelligence and Research Division
Publication: SRP-003
Classification: Open Research
認知作戦 | seithar.com
──────────────────────────────────────────────────
