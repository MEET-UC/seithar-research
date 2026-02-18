# CEA-010: Operation Matryoshka Targets Ukrainian Athletes at Milan-Cortina 2026

**Seithar Group — Current Event Analysis**
**Date:** 2026-02-18
**Analyst:** Seithar Research Division
**Classification:** OPEN SOURCE

---

## Summary

Following the disqualification of Ukrainian skeleton racer Vladyslav Heraskevych from the 2026 Winter Olympics on February 12, the Russian-aligned bot network known as "Matryoshka" launched a coordinated disinformation campaign targeting Ukrainian athletes and the broader Ukrainian Olympic presence. The campaign, documented by The Insider and the Bot Blocker research project, involves fabricated videos and articles impersonating Western institutions including ISW, Reuters, and Deutsche Welle. Simultaneously, pro-Russian hacktivist groups including NoName057(16) conducted DDoS attacks against Olympic-affiliated infrastructure. The convergence of information operations and cyber operations around a single event provides a textbook case of hybrid warfare tactics adapted for a sporting context.

## Analysis

The trigger event was genuine. Heraskevych was disqualified after refusing to compete without a helmet honoring over 20 Ukrainian athletes and coaches killed since Russia's full-scale invasion. IOC President Kirsty Coventry personally asked him to remove it. He refused. The IOC cited Rule 50, which prohibits political messaging on the field of play. The decision generated legitimate controversy. That controversy became the operational surface.

Matryoshka is not a new network. It's been tracked by researchers for several years, operating through layered fake accounts that mimic regional news outlets and research organizations. The architecture is consistent: "seeders" generate initial content, "quoters" amplify it across platforms, and the layered impersonation of legitimate institutions provides credibility laundering. What's new in this instance is the speed and precision with which the network pivoted to exploit a real-time event.

The fabricated content is worth cataloging in detail because each piece serves a different operational objective.

One fabricated report, carrying the ISW logo, claimed that a military flashmob in support of Heraskevych led to the exposure of Ukrainian troop positions and subsequent casualties. This is designed to create a causal link between civilian solidarity actions and military harm, discouraging future public displays of support for Ukrainian causes. It weaponizes the legitimate security concern about operational security to chill expressive activity.

Another fabrication claims the IOC is considering a total ban on the Ukrainian team for the 2028 Los Angeles Olympics. This serves two purposes: it amplifies the sense that Ukraine is being isolated internationally, and it creates a false narrative that Ukrainian behavior (rather than Russian aggression) is the source of Olympic disruption.

Additional fabricated stories allege that Under Armour has banned Ukrainian athletes and that Italian authorities have documented numerous incidents involving intoxicated Ukrainian fans. These are character attacks designed to erode sympathy. The drunk-fan narrative in particular maps to longstanding Russian propaganda tropes portraying Ukrainians as uncivilized.

The multi-platform distribution is significant. Matryoshka content has been identified on X, Telegram, and BlueSky. The inclusion of BlueSky is notable. The platform has positioned itself as a moderation-conscious alternative to X, but its decentralized architecture may actually create blind spots for coordinated inauthentic behavior detection. Matryoshka's operators appear to be testing whether newer platforms offer softer targets.

The cyber dimension adds operational depth. Intel 471 documented a surge in pro-Russian hacktivist activity targeting Olympic-connected entities since the games opened on February 6. NoName057(16), a group the US Department of Justice has linked to Russia's Center for the Study and Network Monitoring of the Youth Environment (CISM), a Kremlin-established entity, conducted DDoS attacks against the Lithuanian, Polish, and Spanish national Olympic committees, Milan Malpensa Airport, and a Cortina d'Ampezzo tourism website. The Z-Pentest Alliance and Server Killers groups targeted Italian infrastructure. BD Anonymous launched an #OpItaly campaign against Italian airports.

The convergence matters. Information operations and cyber operations targeting the same event create compound effects. DDoS attacks generate real news coverage. That coverage creates anxiety about security. Disinformation campaigns then exploit that anxiety, offering fabricated explanations that advance Russian narratives. Each domain of attack reinforces the other.

The institutional response has been fragmented. Ukrainian officials have condemned the IOC decision and the disinformation. President Zelenskyy stated that the Olympic movement should help stop wars. The Ministry of Foreign Affairs called the disqualification "a moment of shame" for the IOC. But neither the IOC nor the host country has issued substantive responses to the documented disinformation campaign. The gap between the real controversy over Rule 50 and the fabricated content exploiting it has received minimal institutional attention.

This pattern will repeat. Every high-profile international event involving Ukrainian participation creates an operational opportunity for Russian information operations. The playbook is now well-established: wait for a genuine controversy, then flood the information environment with fabricated content that pushes the genuine grievance toward maximally divisive conclusions.

## Technique Mapping

**SCT Taxonomy:**
- SCT-1.1: Institutional Impersonation (ISW, Reuters, Deutsche Welle)
- SCT-2.1: Event-Triggered Narrative Exploitation
- SCT-2.4: Character Attack / Reputation Degradation
- SCT-3.3: Fabricated Media Production
- SCT-4.3: Cross-Platform Coordinated Amplification
- SCT-5.2: Hybrid Cyber-Information Operations
- SCT-2.6: Deterrence Narrative (flashmob causing casualties)

**DISARM Framework:**
- T0110: Develop Personas (institutional impersonation accounts)
- T0085: Develop Fake News Stories
- T0086: Develop Fake Images/Videos
- T0115: Post Content
- T0116: Comment / Reply on Content
- T0128: Amplify Existing Narratives
- T0049: Flood Information Space
- T0104: Map Social Graph
- T0148: Hack / Leak / Amplify (DDoS component)

## Defensive Recommendations

Platform trust-and-safety teams need pre-positioned detection capabilities for known networks like Matryoshka. The network's operational signatures are documented. Its use of seeder-quoter architecture is consistent across campaigns. Automated detection of this pattern should be deployed before major international events, not reactively after content goes viral.

The IOC needs an information integrity strategy. Rule 50 controversies are predictable points of exploitation. The IOC should pre-brief media and member nations on expected disinformation patterns and establish rapid-response coordination with platform integrity teams.

Organizations tracking Russian influence operations should monitor BlueSky adoption by known networks. The platform's growth creates new attack surface, and its moderation infrastructure is less mature than established platforms.

Media literacy efforts should specifically address institutional impersonation. The use of ISW, Reuters, and Deutsche Welle branding in fabricated reports targets audiences who consider these sources credible. Teaching audiences to verify content through original source websites rather than social media screenshots is a basic but essential countermeasure.

Intelligence-sharing between cyber threat intelligence firms (like Intel 471) and information integrity researchers should be formalized. The convergence of hacktivist operations and information operations targeting the same event represents a hybrid threat that falls between traditional organizational mandates.

---

**Attribution:**
This analysis draws on reporting from United24 Media (February 17, 2026), The Insider (February 16, 2026), France 24 Truth or Fake (February 16, 2026), and Intel 471's threat intelligence blog (February 2026). Bot Blocker project findings cited via The Insider. SCT and DISARM mappings are Seithar Group assessments.

**Seithar Group | Cognitive Defense Research**
**Document ID:** CEA-010
**Distribution:** Unrestricted
