---
title: "AI Governance, From First Principles"
date: 2026-06-17
draft: false
tags: ["AI Governance", "opinion"]
categories: ["opinion"]
description: "Field Notes on AI Governance: Stop Memorizing AI Regulations. Start Asking Two Questions."
---
## Table of Contents
- [1. Where I started](#1-where-i-started)
- [2. Why, what, and how](#2-why-what-and-how)
- [3. From two questions to a map](#3-from-two-questions-to-a-map)
- [4. Reading the frameworks](#4-reading-the-frameworks)
  - [4a. The EU AI Act](#4a-the-eu-ai-act)
  - [4b. NIST's AI Risk Management Framework](#4b-nists-ai-risk-management-framework)
  - [4c. The OECD AI Principles](#4c-the-oecd-ai-principles)
  - [4d. The UK's pro-innovation approach](#4d-the-uks-pro-innovation-approach)
  - [4e. Frontier (scaling-law) governance](#4e-frontier-scaling-law-governance)
- [5. What the map shows](#5-what-the-map-shows)
- [6. Where it's going](#6-where-its-going)
- [References, by framework](#references-by-framework)


## 1. Where I started

When I first tried to read about AI governance, I found myself in an alphabet soup. There's a pile of names to learn: the EU AI Act, NIST, Bletchley, the OECD Principles, Korea's Basic Act, "the omnibus," Singapore's framework, the UK's different one, a treaty and the abbreviations stack up faster than the understanding does. If you've tried, you've probably hit the same wall.

Then there was this other problem. Almost everything I came across on popular media discourses about governance, the commentary, the threads, the posts, the summaries are all framed as fundamentally about *risk*: what could go wrong, and how to hold it back. But when I went and read the actual acts, that wasn't quite what they said. Several of them diverged from that risk-first story. Some were built to *enable* AI, not restrain it. The discourse and the documents didn't line up, and at first I couldn't tell why.

What helped was small. Instead of reading each framework as a block of obligations to memorize, I started asking each one the same two things: *what* is it actually for, and *how* does it go about it. The rest of this piece is those two questions, applied.

## 2. Why, what, and how

Forget AI for a second (Can you imagine I made AI write that! Now Claude has existentialism positionally encoded). 
Let's take an analogy: think about a speed limit. 

At first it's just a sign but underneath the sign are three layers. 

- First, the **why**: Establishes the need for the rule. Cars are fast and heavy, and people die when they crash. That danger is the *need* — the reason a rule exists at all.

- Given that need, the **what**: the rule picks a goal. Keep people from dying. 

- And the **how**: it picks a method: a posted number, police, fines.

Every rule works this way, because every rule is a response to some need: a building code, a food-safety inspection, even a recipe. AI governance isn't an exception; it only seems muddled because it arrives wrapped in acronyms.
![A sketch diagram summarizing the 'what' and 'how' questions in AI governance frameworks](/images/ai_governance/ai_governance_sketch.png)


Here's the part that matters for reading frameworks. For AI, almost everyone agrees on the *why*: the technology is consequential enough that *something* is warranted. The differences you actually want to see live one floor down, in the **what** and the **how**.

So those are the two questions we carry through the rest of the piece. 

💡 *WHAT* is a framework for, and *HOW* does it act.

A rule can aim to protect people and still act with a feather touch; it can aim to *encourage* a technology and still act through hard law. That independence is why the question people reach for first: "is this pro or anti-innovation?" — is a tricky place to start since it bundles a what and a how into one word.

I gave myself a challenge that I'll try to categorise some of the existing framework just from these 2 intuitive questions.

## 3. From two questions to a map

We need to add some dimensions to these 2 questions now.

Start with **WHAT is it for?** Read enough of these documents OR let AI summarize it for you (which is was what I did) and the goals, broadly speaking, collapse into three.

Some frameworks are built mainly to **prevent harm**: Easy!

Some are built mainly to **protect rights** : dignity, fairness, not being discriminated against, a say in decisions that affect you. This overlaps with harm, but it points at something different: *what people are owed, not only what might hurt them.*

And some are built mainly to **enable** the technology : treating governance as a way to *unlock* AI rather than hold it back and aid it's adoption (safely).

Most frameworks touch more than one. But almost all of them *lead* with one, and that leading choice is the answer to WHAT. It already does work: a framework that leads with "enable" is a different animal from one that leads with "prevent harm," before you've read a single line of obligations.

That's one of the two questions placed. Next, the harder and more revealing one: HOW.

**HOW does it act?** The "act" hides three separate choices.

- *How hard does it push?* It's not binary. There's a range in which it operates.A speed limit pushes hard: break it and you pay. A "Drive Safely" billboard pushes softly: it asks, and that's all. Frameworks run the same range, from a voluntary set of principles nobody can fine you over to a binding law with real penalties. Call this the **weight**.

- *Who does the pushing?* One national authority or from a group of countries signing a shared treaty. Call this the **authority**.

- *What sets the obligation off?* This is the subtle one. A speed limit can be triggered by *where you are* — a school zone, a motorway — which is the road's use. It can be triggered by *what you're driving* — trucks face limits cars don't, because of what the vehicle *is*. Or you might simply opt in to a voluntary standard, like a recommended speed on German Autobahns. Frameworks have the same three triggers: 
    
    - the **use** an AI is put to 
    
    - the **choice** to adopt a voluntary code
    
    - the model's sheer **scale**, governed for what it could do simply by being big. 

    Call this the **trigger**.

![Diagram: the 'WHAT' and 'HOW' dimensions in AI governance frameworks](/images/ai_governance/what_how.png)


Every framework  does NOT *reduce* to these. The real ones are richer but because reading each through WHAT and HOW is what finally gave me a mental model I could hold, I decided to share that approach.

## 4. Reading the frameworks

With WHAT and HOW in hand, each framework stops being a wall of obligations and becomes a quick reading. I'm no expert in the field of policy drafting and governance so I won't be explaining the frameworks in details + there are already really good references for that, linked at the end. 

The point is to *place* them, and to notice that once you do, they mostly explain themselves.

### 4a. **The EU AI Act** 
The European Union's law for artificial intelligence, passed in 2024 and the first comprehensive AI law anywhere. The strict one, and the one everyone's heard of.

**WHAT**
- *Leads with:* preventing harm, with a strong lean toward protecting rights. It sorts AI by how much damage a given **use** could do, and bans or tightly controls the uses it judges dangerous.

**HOW**
- *Weight:* Heavy. A binding law with real fines.
- *Authority:* a single central regime: one set of rules for the whole EU.
- *Trigger:* mostly the **use** : a hiring filter or a credit-scoring model is caught for what it decides.

*PS:* the EU also bolts a **scale** trigger onto the very largest general-purpose models. The newest idea, tucked inside the oldest-style law. Keep it at the back of your head for now; it comes back.

### 4b. **NIST's AI Risk Management Framework**
NIST is the US government's standards agency; in 2023 it released this as a voluntary set of practices for any organization building AI. Not a law but rather a playbook a company runs on itself.

**WHAT**
- *Leads with:* preventing harm. BUT aimed at how an organization builds and runs its AI rather than at the product itself. The goal it names is "trustworthy AI."

**HOW**
- *Weight:* light. Voluntary, no fines, no certificate to earn. Its force comes from being adopted, not enforced.
- *Authority:* The organization runs it on itself, with no regulator or sector body in the loop.
- *Trigger:* you opt in. It applies when a company chooses to pick it up, and not otherwise.

*The catch*: NIST never says how much risk is too much. It tells you to find, measure, and manage your risks but you set the bar yourself. That makes it fit any industry, and also easy to satisfy at a low bar.

### 4c. **The OECD AI Principles** 
The OECD is an international economic organization of ~38 mostly-wealthy democracies; in 2019 (updated 2024) it published these shared AI principles, since signed by around 47 countries. It's to be seen as a common reference point, not a rulebook.

**WHAT**
- *Leads with:* protecting rights and values. Human-centered fairness, transparency, accountability along with a pro-innovation streak that fits an economic body.

**HOW**
- *Weight:* light. Voluntary, no enforcement.
- *Authority:* a club of states agreeing on common ground.
- *Trigger:* you opt in. A country or company chooses to align with it.

*Why is this one important?:*  What makes it matter is not enforcement but **vocabulary**. Later laws, including the EU Act, borrowed its definitions and language. So it shapes the hard rules downstream without binding anyone itself.

At this point, I'd also like to refer to another framework that kind of falls under similar block for me with some noteworthy differences.

**UNESCO's Recommendation on the Ethics of AI (2021):** This is the same kind of instrument as the OECD's: voluntary, values-led, agreed by many states BUT far broader, adopted by all 193 member states, including much of the Global South the OECD club leaves out. Its one distinct move: it ships practical tools to help countries actually implement it, where OECD mostly stops at principles.

### 4d. **The UK's pro-innovation approach** 
Rather than pass an AI law, the UK chose (from 2023) to steer AI through its *existing* regulators and an openly pro-growth stance. 

**WHAT**
- *Leads with:* enabling the technology: getting AI adopted and keeping the country competitive is the stated goal; safety principles ride along, but the framing is growth.

**HOW**
- *Weight:* light. Non-binding principles, no single law. (Binding rules are floated only for the very largest models, and keep getting delayed.)
- *Authority:* No central AI regulator. The existing sector regulators: finance, health, data protection — each applying the principles in their own patch. 
- *Trigger:* Whatever already governs your sector. There's no AI-specific trigger; you're caught by the rules that already apply to your domain.

🚀 **The bold move:** In 2025, the "AI Growth Lab" launches — sandboxes where specific rules can be temporarily switched *off* so a company can pilot something. **This is a rare instance where governance is used to clear a path, not block one!** (Pretty wild, right? 😲)

*The sting in the tail:* a successful pilot can make that relaxation permanent, with less scrutiny than a normal law.

The UK approach pairs well with what Singapore is doing.

**Singapore's Model AI Governance Framework:** Singapore's tech regulator (the IMDA) issues this as voluntary guidance. Same pole as the UK (pro-innovation, light, opt-in), but with a different distinctive move. **Instead of relaxing rules in sandboxes, Singapore builds *tools*: an open-source testing kit (AI Verify) that turns principles into things you can measure**, and it was the first to publish guidance specifically for autonomous AI "agents." (Anchor the Politician selection in Meritocracy and it does seem to have some benefits, no?)

### 4e. **Frontier (scaling-law) governance** 
Scaling laws isn't a new term for tech-people but it's used here in a different context. The rule is aimed not at how AI is *used* but at the most powerful models themselves: the "frontier" systems from the biggest labs. It began as voluntary commitments (the 2024 Seoul summit, where major labs pledged safety practices) and has since hardened into law in places (California's 2025 frontier-AI law; South Korea's 2026 AI Act).

**WHAT**
- *Leads with:* preventing harm, specifically the large, catastrophic kind a highly capable model might enable.

**HOW**
- *Weight:* all over the map — from voluntary lab pledges with no defined repercussion upon violation to California's binding law with real penalties.
- *Authority:* Mixed. an industry-and-summit handshake in one place, a US state legislature in another, a national government in Korea.
- *Trigger:* Not the use, but the **scale**. A model is governed for what it could do simply by being big enough. (Analogous example to our initial Speed Limit scenario would be trucks: rules for what the vehicle *is*, not where it's driven. This is the EU's "scale" grown into a whole approach.)

The twist worth noticing: this scale-based idea spread just as the political wind shifted. The 2024 summits were about "safety"; by 2025–26 they were about "impact" and "adoption," and the US federal government swung the other way, rolling back its own safety rules and moving to override stricter state laws. The newest way to govern AI arrived right as the appetite to govern it cooled.

Now, Last one, I promise.

**The Council of Europe's AI treaty (2024):** a binding international agreement built around human rights, signed by the UK, US, EU, Canada and others. It's the rare *rights-led and binding* combination but it binds *countries* to uphold principles rather than binding products to meet specs, and so far no country has ratified it, so its teeth remain on paper.

## 5. What the map shows

Place everything and the map starts talking back. Three things stand out.

![Summary map of AI governance frameworks, showing axes for "what" (goal: rights vs. harms vs. adoption) and "how" (method: law vs. voluntary), plotted with key frameworks.](/images/ai_governance/framework_summary.png)


- **Rights get principles; harms get laws.** 

    - Nearly every framework that leads with *preventing harm*: the EU Act, California's frontier law, Korea's is binding, with real penalties. 

    - Nearly every one that leads with *protecting rights* : OECD, UNESCO is voluntary. The lone rights-led *and* binding instrument, the Council of Europe's treaty, isn't ratified by anyone. 

We pass hard rules to stop damage, soft ones to protect rights  maybe because damage is concrete and rights are an argument.

- **"Pro- or anti-innovation?" is the wrong question.** 
    - Call the UK "pro-innovation" and you've bundled two facts: it centers on *enabling* (a WHAT) and pushes *lightly* (a HOW). The EU is the opposite pair. One word, two questions mashed together. Pull them apart and the debate resolves into coordinates.

Everyone agrees AI needs *something*, and that's what the commentary fixates on. But the frameworks differ in the *what* and the *how*, and several lead with *enabling*, not risk. 

The discourse was on the shared floor(the WHY?)but the documents were one floor down, where they differ((the WHAT and HOW)); still in the same building though.

## 6. Where it's going

Two last notes.

Governing AI by its *scale* is a new paradigm. Every older rule we had, for cars, drugs, hiring attaches to **what something is used for**. 
Governing a model for **what it might do simply by being large** has almost no precedent. 
It's still rare, still aimed mostly at frontier systems, the thresholds crude. But it's the one move here that isn't borrowed from how we govern everything else — worth watching.

The other note is direction. Stack the recent changes: the EU delaying its strict rules, the UK switching rules off for pilots, the US rolling back its own safety work, the summits trading "safety" for "impact" and they lean the same way: toward *enabling*. 

Risk built the first wave of AI governance; the current wave is loosening it.

None of this tells you whether a framework is Good or better than othes. The two questions don't settle that. They just helped me see it from the reference point of what I already knew. 

---

## References, by framework

Everything that fed this piece — primary sources plus the explainers, reports, and analyses we leaned on — grouped so you can go deep on any one framework.

**EU AI Act**
- Primary text — [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- Article-mapped summary — [artificialintelligenceact.eu](https://artificialintelligenceact.eu/high-level-summary/)
- Why the "four-tier pyramid" misleads — [Modulos](https://www.modulos.ai/blog/eu-ai-act-risk-categories-explained-why-the-four-tier-pyramid-is-wrong/)
- What problem it's actually solving — [Europe of Knowledge](https://era.ideasoneurope.eu/2026/01/02/revisiting-what-problems-the-eu-ai-act-is-actually-solving/)
- "Rights-driven" framing and its paradoxes — [The Regulatory Review](https://www.theregreview.org/2026/03/10/rangone-the-paradoxes-of-the-european-unions-ai-regulation/)
- Proportionality / Draghi–Letta critique — [Intereconomics](https://www.intereconomics.eu/contents/year/2025/number/3/article/better-regulation-and-the-eu-s-artificial-intelligence-act.html)
- Innovation-burden critique — [Bloomberg Law](https://news.bloomberglaw.com/us-law-week/eu-ai-acts-burdensome-regulations-could-impair-ai-innovation)
- Defense: adaptive, sandbox-based regulation — [arXiv 2511.00027](https://arxiv.org/abs/2511.00027)
- Phased timeline & risk-tier percentages — [Opsio](https://opsiocloud.com/blogs/what-is-eu-ai-act-risk-classification/)

**NIST AI Risk Management Framework**
- Framework text — [AI RMF 1.0](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)
- Resource center — [NIST AIRC](https://airc.nist.gov/airmf-resources/airmf/)
- It sets no risk tolerance — [arXiv 2406.15371](https://arxiv.org/pdf/2406.15371)
- Voluntary, non-certifiable, weak on agents — [Witness AI](https://witness.ai/blog/nist-ai-risk-management-framework/)
- Uneven adoption & cost — [Lumenova](https://www.lumenova.ai/blog/pros-and-cons-of-implementing-the-nist-ai-risk-management-framework/)
- General principles → inconsistent application — [Securiti](https://securiti.ai/nist-ai-risk-management-framework/)

**OECD AI Principles**
- Official text — [OECD](https://www.oecd.org/en/topics/ai-principles.html) · [OECD.AI](https://oecd.ai/en/ai-principles)
- Definitional influence & safe-harbour role — [Adeptiv](https://adeptiv.ai/oecd-ai-principles-overview/)
- Non-binding; the Policy Observatory — [White & Case](https://www.whitecase.com/insight-our-thinking/ai-watch-global-regulatory-tracker-oecd)
- "Industry-leads" philosophy critique — [arXiv 2110.02707](https://arxiv.org/pdf/2110.02707)
- The 2024 walk-back on rights — [arXiv 2408.01440](https://arxiv.org/pdf/2408.01440)
- Vague principles, inconsistent reading — [arXiv 2407.13934](https://arxiv.org/pdf/2407.13934)

**UNESCO Recommendation on the Ethics of AI**
- Official page — [UNESCO](https://www.unesco.org/ethics-ai/en)
- Key facts — [UNESCO (PDF)](https://unesdoc.unesco.org/ark:/48223/pf0000385082)

**UK pro-innovation approach**
- Parliament overview — [UK POST](https://post.parliament.uk/artificial-intelligence-ethics-governance-and-regulation/)
- Current state of play — [Glacis guide](https://www.glacis.io/guide-uk-ai-regulation)
- The AI Growth Lab (rules switched off) — [Bird & Bird](https://www.twobirds.com/en/insights/2025/uk/the-uk-government-has-announced-plans-to-introduce-regulatory-sandboxes-to-encourage-ai-adoption--bi)
- King's Speech 2026 / "Regulating for Growth" Bill — [Bird & Bird](https://www.twobirds.com/en/insights/2026/ai-in-the-kings-speech-2026-regulating-for-growth-bill-announced)
- "Regulatory stagnation" warning — [AI CERTs](https://www.aicerts.ai/news/regulatory-stagnation-warning-as-uk-delays-ai-law/)
- Sandbox mechanics; adoption barriers — [Compliance Week](https://www.complianceweek.com/regulatory-policy/uk-outlines-ai-sandbox-plan-as-regulators-weigh-compliance-risks/36341.article)
- Fragmentation across regulators — [SureCloud](https://www.surecloud.com/blog-hub/eu-vs-uk-ai-regulation-what-it-means-for-governance-risk)

**Singapore Model AI Governance Framework**
- AI Verify testing toolkit — [FPF explainer](https://fpf.org/blog/ai-verify-singapores-ai-governance-testing-initiative-explained/)
- First agentic-AI governance framework — [Bird & Bird](https://www.twobirds.com/en/insights/2026/singapore/singapore-introduces-new-model-ai-governance-framework-for-agentic-ai)

**Frontier / scaling-law governance**
- From Seoul to the India summit — [The Future Society](https://thefuturesociety.org/indiaaisummit/)
- India AI Impact Summit takeaways — [Brookings](https://www.brookings.edu/articles/takeaways-from-the-india-ai-impact-summit/)
- California SB-53, explained — [Brookings](https://www.brookings.edu/articles/what-is-californias-ai-safety-law/)
- SB-53 mechanics & thresholds — [WilmerHale](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20251001-transparency-in-frontier-artificial-intelligence-act-sb-53-california-requires-new-standardized-ai-safety-disclosures)
- US deregulation & state-law preemption — [King & Spalding](https://www.kslaw.com/news-and-insights/new-state-ai-laws-are-effective-on-january-1-2026-but-a-new-executive-order-signals-disruption)
- US state-vs-federal patchwork — [Baker Botts](https://www.bakerbotts.com/thought-leadership/publications/2026/january/us-ai-law-update)

**South Korea AI Basic Act**
- Overview & key takeaways — [Cooley](https://www.cooley.com/news/insight/2026/2026-01-27-south-koreas-ai-basic-act-overview-and-key-takeaways)
- Decree backlash (too light vs too heavy) — [Business & Human Rights RC](https://www.business-humanrights.org/en/latest-news/s-korea-draft-decree-for-ai-basic-act-spark-backlash-over-limited-scope-and-delayed-penalties/)

**Council of Europe AI treaty**
- Framework Convention (official) — [Council of Europe](https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence)
- Context, approach & scope of obligations — [Cambridge (EJRR)](https://www.cambridge.org/core/journals/european-journal-of-risk-regulation/article/council-of-europe-framework-convention-on-artificial-intelligence-context-regulatory-approach-and-scope-of-obligations/0ED34EFE5AA7C9628F7053720F88F48C)