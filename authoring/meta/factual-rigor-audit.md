---
title: Factual Rigor Audit
description: Structure vs content coverage, citation gaps, new sources. Part-by-part audit for inline citations and factual claims.
tags:
  - meta
  - audit
---
# Factual Rigor Audit

**Purpose:** Align the manuscript with verifiable facts, add inline citations to actual stories and sources, and track coverage gaps between the [Structure](structure.md) and the written book parts.

**Principles:**
- Every factual claim should be traceable to a public source (news, reports, laws, official data, academic research).
- Named characters and companies should be introduced with citeable references (interviews, profiles, company histories).
- Structure chapters not yet written should be flagged as "To Draft."
- Scenes and vignettes can be composite but should be grounded in documented contexts.

**Workspace note:** **Published site content** lives under `book/` only: `book/part-NN/*.md`, `book/appendices/`, and `book/prologue.md`. **Authoring-only** material lives under `authoring/meta/` (this file, outline, workflows) and `authoring/manuscript/` (merged part drafts for `scripts/scaffold_topic_articles.py`). Deploy **`book/`** to the web. Avoid duplicating editorial work in `kenyan-tech-stack-garden/` to prevent drift.

---

## Part I — Before the Hype (1968–2007)

### Structure vs Content

| Structure Chapter | Book Section | Status | Notes |
|-------------------|--------------|--------|-------|
| 1) Banking in the Dark: Bespoke Software for Banks & Traders | [01-banking-in-the-dark.md](../../book/part-01/01-banking-in-the-dark.md) | **Expanded** | KBA timeline + Craft Silicon / Budhabhatti (`SRC-28`–`30`, `SRC-34`); tighten CBK primary refs on next pass |
| 2) The Cybercafé Republic | [02-cybercafe-republic.md](../../book/part-01/02-cybercafe-republic.md) | **Expanded** | Chronology + mechanics; anchor thesis (`SRC-36`); add more peer-reviewed cites |
| 3) Telcoms Before the Boom: The Mobile Explosion | [03-telcoms-before-the-boom.md](../../book/part-01/03-telcoms-before-the-boom.md) | **Expanded** | Full narrative spine + ETACS→GSM→Oct 2000 launch (`SRC-37`); Joseph/Maitai (`SRC-35`, `SRC-37`, `SRC-42`); Kencell→Celtel **1 Nov 2004** (`SRC-41`, `SRC-43`); SIM ladder as caveated press (`SRC-31`); verify penetration vs **CA** tables (`SRC-18`–`SRC-21`) |

### Missing from Structure (Coverage Gaps)

| Structure Element | In Book? | Action |
|-------------------|----------|--------|
| **Kamal Budhabhatti (Craft Silicon)** — anchor character | Yes (Ch.1) | Keep in sync with `SRC-28`–`30`; optional Cast appendix entry |
| "The Bank IT Head" / "The Integrator Engineer" archetypes | Implicit only | Optional: name exemplars if citeable |
| Cybercafé: specific dates, proliferation stats, studies | No | Research and add timeline + metrics |
| Telcoms: first SIM era, Safaricom/Telkom split, coverage milestones | Partial (Ch.3 topic file) | Layer CA QoS reports + annual-report coverage metrics on next pass |

### Citation Gaps (Part I)

| Claim / Topic | Current Source | Gap | Suggested Source Type |
|---------------|----------------|-----|------------------------|
| "1988 — Enterprise software adoption in banking" | SRC-24 (NBER mobile money) | SRC-24 is about mobile money, not 1988 banking | Banking sector reports, Craft Silicon founding, Kenya Bankers Association history |
| Midnight reconciliation scene | None | Scene is composite; acceptable if framed | Optional: bank ops reports, audit standards |
| Cybercafé as "first user interface" | None | Needs chronology: when did cybercafés peak? | CA/ITU stats, academic papers on Kenyan internet adoption |
| "Phone becomes identity" — mobile era | None | Needs first-SIM / subscriber growth data | CA historical statistics, GSMA reports |
| Craft Silicon / core banking in Kenya | None | Company not mentioned | Craft Silicon corporate history, press, client list |

### Sources to Add (Part I)

| ID | Description | URL/Reference | Notes |
|----|-------------|---------------|-------|
| SRC-28 | Craft Silicon / Kamal Budhabhatti — company history, founding story | https://www.howwemadeitinafrica.com/how-kamal-budhabhatti-built-one-of-kenyas-foremost-it-companies/17410/ | Founding Oct 2000; bank software origin; Africa Awards 2010 |
| SRC-29 | Kamal Budhabhatti — Meet the Boss interview | https://www.howwemadeitinafrica.com/meet-the-boss-kamal-budhabhatti-ceo-craft-silicon-kenya/16861/ | Anchor character profile |
| SRC-30 | Craft Silicon — official company / team | https://www.craftsilicon.com/about/management-team/ | Management, scope |
| SRC-31 | Kenya mobile sector evolution — SIM prices, Safaricom 2001, subscriber growth | https://techtrendske.co.ke/2025/08/19/kenya-mobile-subscribers-2025 | SIM KSh 200k → KSh 2.5k (2001) → &lt;KSh 100 (2002) |
| SRC-32 | Kenya mobile subscription trends (academic) | https://thesai.org/Publications/ViewPaper?Code=ijarai&Issue=1&SerialNo=1&Volume=4 | Safaricom/Celtel 1999; operators timeline |
| SRC-33 | Statista — Kenya mobile subscriptions 2000–2024 | https://www.statista.com/statistics/498385/number-of-mobile-cellular-subscriptions-in-kenya/ | Time-series data |
| *TBD* | Kenya cybercafé history / proliferation | To research | No strong single source yet; try ITU, ISP association, news archives |
| *TBD* | Kenya banking IT / enterprise software era (1980s–90s) | To research | KBA, Central Bank, or bank histories |

### Inline Citation Checklist (Part I)

- [x] §1: Anchor enterprise banking IT era to KBA technology timeline (`SRC-34`); removed unsupported "1988" peg
- [x] §1: Craft Silicon / Kamal Budhabhatti with citations (`SRC-28`–`30`)
- [x] §2: Timeline skeleton (1995 institutional / late 1990s café boom / late 2000s mobile pressure); deepen with venue counts when you find a study
- [ ] §2: Add one named cybercafé news vignette (optional colour)
- [ ] §3: Add official CA table citation for 1–2 subscriber milestones (year, numbers)
- [x] §3: Named figures/events: Michael Joseph, Vodafone stake, Oct 2000 GSM, Kencell/Celtel rename (`SRC-32`, `SRC-35`, `SRC-37`)

---

## Part II — Connectivity (2005–2012)

*To be audited next. Placeholder.*

---

## Audit Progress

| Part | Audited | Citation gaps addressed | New sources added |
|------|---------|-------------------------|-------------------|
| I | ✓ | Pending | Pending |
| II | — | — | — |
| III–XX | — | — | — |

---

### Navigate the manuscript

← **Previous:** [Full outline — Structure](structure.md) · [**Home**](../../book/index.md) · **Next:** [Prologue](../../book/prologue.md) →
