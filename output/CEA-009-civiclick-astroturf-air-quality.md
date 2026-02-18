# CEA-009: CiviClick and the Industrialization of AI-Powered Regulatory Capture

**Seithar Group — Current Event Analysis**
**Date:** 2026-02-18
**Analyst:** Seithar Research Division
**Classification:** OPEN SOURCE

---

## Summary

An investigation by the Los Angeles Times, published February 17, 2026, revealed that over 20,000 public comments opposing air quality regulations at the South Coast Air Quality Management District (SCAQMD) were generated through CiviClick, a Washington, D.C.-based platform self-described as "the first and best AI-powered grassroots advocacy platform." The campaign, orchestrated by public affairs consultant Matt Klink, may have materially influenced the board's June 2025 decision to scrap proposed rules phasing out gas-powered appliances in Southern California. When the agency's cybersecurity team contacted a small sample of purported commenters, three of five respondents denied any knowledge of messages sent in their names.

## Analysis

This case is a clean example of how AI-powered influence operations have moved from the domain of nation-state actors into the commercial lobbying toolkit. It deserves close attention not because the technique is new in principle, but because the execution demonstrates how effectively AI lowers the barrier to manufacturing apparent public consensus at regulatory scale.

The proposed rules, 1111 and 1121, would have imposed fees on gas-powered furnaces and water heaters across a four-county region affecting roughly 10 million appliance units. The air district estimated the rules would prevent 6 tons of daily NOx emissions, avert nearly 2,500 premature deaths, and prevent over 10,000 new asthma cases. These are not trivial numbers. The opposition had real financial stakes: Klink's firm, California Strategies, counts Sempra (parent company of SoCal Gas) among its clients.

What happened next follows a pattern that information operations researchers will recognize immediately. CiviClick's platform conducted "aggressive omni-channel outreach" to half a million people in its database. The platform's website advertises "AI message assistance" for creating "custom advocacy letters," which means the system likely generated unique, individualized text for each submission rather than identifiable form letters. The SCAQMD typically receives public comments numberable on one hand per agenda item. It received over 20,000.

The board noticed. It would be difficult not to. But the volume itself became the weapon. Board members could point to overwhelming public opposition to justify their vote. Whether each comment was genuine was, functionally, beside the point. The political cover had been manufactured.

Three critical details warrant separate examination.

First, the identity problem. At least three people contacted by the SCAQMD's cybersecurity team said they hadn't written to the agency and didn't know messages had been sent in their names. This pushes the operation beyond astroturfing into potential identity misuse. CiviClick's CEO told Campaigns & Elections that the campaign involved outreach to people in the company's "database of advocates." The gap between someone being in a database and someone authorizing messages sent in their name is the gap between advocacy and fraud.

Second, the attribution laundering. Klink took credit for the campaign in a sponsored article on Campaigns & Elections, describing it as a "David vs. Goliath" victory. This framing is instructive. The actual David in this scenario would be individual citizens affected by air pollution. The actual Goliath is a lobbying apparatus backed by a major energy utility, deploying AI to simulate grassroots opposition. The narrative inversion is itself an information operation technique.

Third, the regulatory response gap. The SCAQMD's spokeswoman confirmed the volume was unusual and the agency had concerns about authenticity, but said they couldn't draw definitive conclusions from the small number of responses to their inquiry. This captures the structural problem perfectly. Regulatory bodies are designed to receive and respond to public input. They are not designed to authenticate it. When AI can generate thousands of unique, plausible comments attributed to real people in a database, the entire public comment infrastructure becomes exploitable.

Samuel Woolley at the University of Pittsburgh called this "absolutely the next step in digital astroturfing." He's right, but the framing understates the problem. Astroturfing implies fake grassroots support. What CiviClick enables is something more precise: the industrialization of apparent democratic participation. The comments look real. They sound real. They're attributed to real addresses in the affected region. The regulatory system has no mechanism to distinguish them from genuine public engagement.

This has implications well beyond air quality regulation in Southern California. Every federal and state regulatory agency that accepts public comment is now a potential target. The EPA, FCC, SEC, and dozens of others rely on public input as a democratic legitimacy mechanism. If that input can be manufactured at scale for the cost of a CiviClick subscription, the entire notice-and-comment process becomes a vector for regulatory capture.

## Technique Mapping

**SCT Taxonomy:**
- SCT-4.1: Astroturfing / Manufactured Grassroots
- SCT-4.2: Social Proof Manufacturing
- SCT-2.5: Narrative Inversion (David vs. Goliath framing)
- SCT-3.2: AI-Assisted Content Generation at Scale
- SCT-6.1: Regulatory Process Exploitation
- SCT-1.3: Identity Appropriation

**DISARM Framework:**
- T0111: Develop AI-Generated Content
- T0115: Post Content (to regulatory comment systems)
- T0029: Create Fake Grassroots Support
- T0128: Amplify Existing Narratives
- T0099: Leverage Existing Databases for Targeting
- T0143: Automate Bot Accounts (adapted: automated comment generation)

## Defensive Recommendations

Regulatory agencies need authentication mechanisms for public comments. At minimum, this means email verification with unique confirmation links for each submission. Agencies should also implement duplicate detection not just at the text level but at the behavioral level, flagging submissions that arrive through common infrastructure or in temporal clusters.

Legislative action should address the gap between database inclusion and active consent. If a platform submits comments on behalf of individuals, those individuals must have explicitly authorized each specific submission. Blanket database membership should not constitute authorization.

Transparency requirements for AI-assisted advocacy are overdue. Any platform submitting comments to regulatory bodies using AI-generated or AI-assisted content should be required to disclose the use of AI in each submission. This won't prevent the practice, but it gives regulatory bodies the information needed to weight comments appropriately.

Investigative journalists and watchdog organizations should begin systematic monitoring of public comment volumes across regulatory agencies. Sudden spikes in comment volume, particularly when accompanied by unusual linguistic diversity (the opposite of form-letter campaigns), should trigger scrutiny.

The CiviClick model will be replicated. It's too effective and too cheap not to be. The defensive infrastructure needs to be built before the next regulatory fight, not after.

---

**Attribution:**
This analysis is based on publicly available reporting from the Los Angeles Times (Tony Barboza, February 17, 2026) and the Campaigns & Elections sponsored article referenced therein. Client relationship data drawn from 2025 California Secretary of State lobbying disclosures. SCT and DISARM mappings are Seithar Group assessments.

**Seithar Group | Cognitive Defense Research**
**Document ID:** CEA-009
**Distribution:** Unrestricted
