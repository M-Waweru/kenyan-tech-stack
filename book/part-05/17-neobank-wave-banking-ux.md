---
title: "17. Neobank Wave: Banking as UX"
slug: neobank-wave-banking-ux
part: 5
part_title: Banks Become Platforms
chapter: 17
topic_type: concept
period: 2014–today
stack_layer: consumer_banking
tags:
  - topic
---

# 17. Neobank Wave: Banking as UX

## Lead

A customer opens an account from a couch: national identification photo, selfie, a few taps, a waiting screen, then push notifications before anyone visits a branch. The product is not only “banking.” It is the **user experience (UX)** of trust—how errors read, how fast support answers, how fees show up in plain language.

The **rail** is app-first retail banking: competing downloads and notifications—not marble lobbies—built on three recurring Kenya patterns: incumbent digital sub-brands (**NCBA LOOP**), fintech–sponsor bank partnerships (**Fingo** × **Ecobank**), and fintech-led licence ownership after microfinance bank acquisition (**Branch**’s **Century Microfinance Bank** chapter). Under all of them sits **banking-as-a-service (BaaS)** and **open application programming interface (API)** culture—the subject of [chapter 16](16-jenga-api-banking-platformization.md)—even when marketing never mentions the letters API.

**Eric Muriuki**, chief executive officer of **LOOP DFS** and **NCBA Group** director for digital business, is the clearest institutional face of the incumbent path in Kenya’s public materials: a twenty-year Kenyan banking-technology résumé, credited with pioneering **M-SHWARI**-style mobile savings and loans before **NCBA LOOP** was positioned as a “fully digital banking experience” aimed at younger, mobile-first users ([LOOP leadership][loop-leadership]). **Fingo Africa**—co-founded by Kiiru Muhoya, James da Costa, Ian Njuguna, and Gitari Tirima—markets itself as a youth-built digital bank in partnership with **Ecobank**, with public claims of **Central Bank of Kenya (CBK)** supervision via the partner bank and a May 2023 Kenya launch story carried in trade press ([Fingo about][fingo-about], [TechCrunch — Fingo × Ecobank][tc-fingo]). **Branch**’s route—buying into a deposit-taking charter after years as a digital lender—adds a third politics: who owns the regulatory primary when the app and the bank licence share a cap table ([Techweez — Branch × Century MFB][techweez-branch]).

Referees include CBK prudential rules, Digital Credit Providers Regulations, 2022 where lending edges blur, Data Protection Act, 2019 for onboarding data, and the **Office of the Data Protection Commissioner (ODPC)** as privacy enforcement matures ([DCP Regulations][dcp-regs], [Data Protection Act][dpa], [ODPC][odpc]). The shadow is predictable: onboarding fraud, account takeover, dark patterns in credit UX, and regulatory tightening whenever consumer harm trends on social feeds and in **WhatsApp** groups.

Merchant acceptance and checkout—the next stack layer—became the natural arena once everyday banking started in an app ([Part VI](../part-06/index.md)).

## Context

Kenya’s **subscriber identity module (SIM)**-first money culture ([Part III](../part-03/index.md)) and **WhatsApp**-thick coordination ([Part IV](../part-04/15-whatsapp-kenya-rail.md)) trained users to expect instant confirmation loops. **Jenga**-class API stacks ([chapter 16](16-jenga-api-banking-platformization.md)) trained builders to expect programmable bank primitives. Neobank-shaped products sit at the intersection: regulated money, consumer-grade UX, and distribution that may ride a group balance sheet, a sponsor bank, or a fintech-controlled microfinance bank charter.

The map is crowded with near-neobanks that never split the brand: tier-one retail apps (**Equity**, **KCB**, **Co-operative Bank of Kenya**, **Absa**) poured engineering into mobile-first journeys, **M-PESA** till and pay bill ergonomics, and in-app credit lines—competing for the same attention without calling themselves neobanks. That incumbent app arms race is the subject of [chapter 18](18-retail-banking-app-table-stakes.md). Digital credit providers under **Digital Credit Providers (DCP)** rules—peers such as **Tala** on the licensed-lender track—stayed credit-first rather than buying deposit infrastructure ([DCP Regulations][dcp-regs]). The sections below separate history by governance model; the product section names how BaaS fits underneath.

## History

### LOOP and the incumbent-led digital sub-brand

**NCBA LOOP**’s leadership narrative ties the brand to Muriuki’s track record on **M-SHWARI**/**M-PAWA**/**MOKASH**-style rollouts before pitching LOOP as Africa’s first “fully digital” experience in the company’s own copy—marketing language readers should treat as positioning, not an adjudicated global first ([LOOP leadership][loop-leadership]). 2023 press and podcast cycles captured public friction around a major app reset—useful evidence that UX refactors are political events for retail banks, not silent deploys ([TechTrends KE — LOOP podcast][techtrends-loop]).

### Branch, Century Microfinance Bank, and the charter-acquisition path

A different bet was to buy the licence instead of renting balance sheet from a sponsor. **Branch**’s acquisition of a controlling stake in **Century Microfinance Bank**—84.89% ownership reported in Kenyan tech press—was framed as the first time a Kenya-era digital lender of that cohort ended up atop an actual microfinance bank, with physical branches still on file in Nairobi and a deposit institution account count reported in the low tens of thousands at the time of the story ([Techweez — Branch × Century MFB][techweez-branch]). **Rose Muturi**, Branch East Africa managing director, described the pre-deal constraint as microlending-only regulation and pitched the bank shell as the route to savings, bill payment, and “basics of banking” beyond a single credit SKU ([Techweez — Branch × Century MFB][techweez-branch]). Gazette notices and cabinet exemption paperwork featured in the same coverage—useful reminders that cross-border ownership of Kenyan deposit institutions shows up in Treasury politics, not only app store ratings ([Techweez — Branch × Century MFB][techweez-branch]).

### Fingo, Ecobank, and the partnership neobank

Fingo’s public story is **Y Combinator** lineage, **Ecobank** as pan-African rails, and a Kenya launch moment in May 2023 with $4 million seed financing reported in **TechCrunch**—check amounts and timing against filings where precision matters for your own diligence ([Fingo about][fingo-about], [TechCrunch — Fingo × Ecobank][tc-fingo]). The About page lists 100K open accounts in 2023 as a milestone—operator-provided metrics, not independent audit ([Fingo about][fingo-about]).

### Umba, Daraja Microfinance Bank, and the profitability gauntlet

**Umba**—often filed in press as a Nigeria-born digital bank expanding in Kenya—took the same MFB-acquisition path as **Branch**, buying a majority stake in **Daraja Microfinance Bank** so it could offer deposit-insured current accounts, savings, fixed deposits, lending, and payments under Kenyan supervision ([The Paypers — Umba Kenya launch][paypers-umba-ke]). Trade coverage of the Kenya go-live pitched low-fee positioning against legacy players—classic neobank marketing ([The Paypers — Umba Kenya launch][paypers-umba-ke]).

The outside money story is less triumphant: **TechCrunch** reporting on FairMoney–Umba acquisition talks (February 2024) cited sources and a pitch deck snippet—roughly USD 335,000 revenue versus USD 1.54 million expenses in the first half of 2023—and noted a USD 20 million all-stock deal frame that would approximate total outside funding raised ([TechCrunch — FairMoney / Umba talks][tc-fairmoney-umba]). The same news cycle linked Umba’s Kenya thesis to Daraja’s microfinance licence—scarce compared with Nigeria’s crowded MFB field—as strategic value beyond headline install counts ([TechCrunch — FairMoney / Umba talks][tc-fairmoney-umba]). Broader Africa neobank coverage in **TechCrunch** stressed how few players were truly in the black even when growth headlines looked loud ([TechCrunch — African neobanks in the red][tc-neobanks-red]). Later **Innovation Village** reporting on a USD 5 million debt facility (October 2024) quoted Umba leadership describing Kenya operations as “approaching profitability” with strong 2024 revenue growth—operator narrative readers should reconcile with filings, not headlines alone ([Innovation Village — Umba debt Kenya][innovation-umba-debt]).

## Product and mechanics

### Composite scene: two downloads, one rainy Saturday

*Composite, grounded in typical digital-bank onboarding practice:* A **Jomo Kenyatta University of Agriculture and Technology (JKUAT)** student tries **Fingo** because a friend sent a referral link; onboarding is entirely in-app, **know your customer (KYC)** is document plus liveness, marketing promises peer-to-peer pricing that undercuts informal mobile money tax for small transfers ([Fingo about][fingo-about]). The same afternoon, a small business owner installs **LOOP** for separate business and personal money rituals—tariff PDFs and complaints policies linked in footer copy the way regulated retail banks still do things ([LOOP leadership context][loop-leadership]). A third household member already has **Branch** on the phone from the lending era; the icon stayed put while the behind-the-scenes story shifted toward microfinance bank products after the Century deal ([Techweez — Branch × Century MFB][techweez-branch]).

Mechanically, all three tracks lean on smartphone identity capture, risk scoring, push notifications, and card or virtual payment instruments where product roadmaps allow—then diverge on who holds the charter, who owns customer support escalations, and cross-border ambition (**Ecobank** footprint narrative versus **NCBA** group distribution versus **Branch**’s integration story).

### Delivery patterns — sub-brand, partnership front-end, owned charter

Incumbent sub-brands reuse group compliance, brand risk, and existing core banking contracts—the **LOOP** pattern. Partnership neobanks split product velocity and regulatory primary: the sponsor bank answers CBK for deposit rules while the fintech ships UX—the **Fingo** × **Ecobank** pattern. Owned-charter plays fold app distribution and licence control into one corporate story after MFB acquisition—**Branch**’s path ([Techweez — Branch × Century MFB][techweez-branch]). None of these labels guarantee unit economics; they describe governance and referee interfaces.

### BaaS, open finance, and embedded rails

BaaS—in the Kenyan builder sense profiled in [chapter 16](16-jenga-api-banking-platformization.md)—is accounts, KYC and **anti-money laundering (AML)** hooks, payments, and statements exposed for integration; the neobank app is positioning, notifications, and lifecycle marketing. Many high-throughput finance experiences never mint a neobank brand at all: payroll **software as a service (SaaS)**, agritech disbursements, and B2B marketplaces often consume bank primitives through **Jenga**-class APIs or peer bank programmes while staying invisible to retail switchers.

The CBK’s 2020–2025 national payments vision—reported when it landed—committed the regulator to API standards, data portability, and risk/consumer-protection clarity for third-party account access and payment initiation, inside a broader digital finance policy conversation ([The Paypers — CBK open banking plan][paypers-open-bank]). The *Kenya’s Payments Journey* bulletin line readers may know from CBK publications tracks the same modernisation arc—mobile money interoperability and banking digitisation as sequential homework ([CBK — Kenya's Payments Journey][cbk-payments]). In practice, “open banking” here is directional policy and bilateral bank API deals, not a single retail switching standard like some European regimes publish—plan for integration entropy, not a tidy spec sheet.

## Business model and incentives

Revenue still lives in net interest margin, fees, and interchange where cards exist—neobank UX is acquisition and retention technology for those old engines. Youth cohorts are strategically valuable because lifetime value math rewards early primary account status, even when short-run balances are thin.

BaaS and API programmes earn banks integration fees, float, and deposits gathered through partners—**Equity**’s **Finserve** logic—while partners trade speed for platform dependency ([chapter 16](16-jenga-api-banking-platformization.md)). Partnership neobanks split economics through white-label or revenue-share contracts that rarely surface in App Store screenshots; owned-charter plays keep spread and fee income inside the fintech-bank group but inherit capital adequacy and integration cost curves banks know well.

## Regulation and referees

### Referee beat — CBK footer as user-visible law

LOOP’s site states plainly that **LOOP** is regulated by the Central Bank of Kenya—a sentence users rarely read until something breaks ([LOOP leadership page footer][loop-leadership]). Fingo’s About copy positions the product as CBK-regulated through **Ecobank**—partnership banking in legal clothing ([Fingo about][fingo-about]). Branch-style MFB ownership puts deposit rules, microfinance reporting, and consumer protection letters on the same cap table as the app team—different escalation geometry from a pure DCP lender. Where apps surface digital credit outside bank perimeters, DCP licensing and disclosure rules join the stack ([DCP Regulations][dcp-regs]). Biometric KYC and behavioural data raise Data Protection Act questions that product managers now own with legal ([Data Protection Act][dpa], [ODPC][odpc]).

## Adoption in Kenya

Adoption skews urban, smartphone, and digitally literate—with agent and **unstructured supplementary service data (USSD)** rails still carrying everyone else ([Part III](../part-03/index.md)). The neobank wave’s inclusion claim is partly real (cheaper onboarding) and partly aspirational (excludes anyone without a compliant ID trail).

### Reported LOOP scale (third-party press)

Kenyan business media profiling **NCBA Group** innovation reproduced a concrete **LOOP** scorecard: from inception to end of 2024, LOOP had disbursed more than USD 48 million in loans, processed more than USD 876 million in transactions in 2024, and handled more than 400,000 consumers and 160,000 merchants registered in Kenya ([Swala Nyeti — NCBA innovation profile][swala-ncba]). Treat those figures as press-sourced, not audited gospel—the same article bundles group-level claims (for example 68 million customers across **NCBA**’s footprint) that are not LOOP-only ([Swala Nyeti — NCBA innovation profile][swala-ncba]). For investment-grade truth, default to **NCBA Group** annual reports and CBK returns.

### Reported Fingo scale (launch window and operator milestones)

**TechCrunch**’s May 2023 launch piece—still the clean international byline on the story—quoted **Fingo** as acquiring 10,000 active users with a 100,000-person waitlist within 24 hours of going live, and rehearsed the $4 million seed round and CBK approval timing ([TechCrunch — Fingo × Ecobank][tc-fingo]). **Fingo**’s own About timeline claims 100K open accounts in 2023 and 5K by 2022 ([Fingo about][fingo-about]). The reporter also surfaced **Ecobank Group** adviser Diallo Djiba’s line that the tie-up was meant to scale youth-focused products across **Ecobank**’s footprint ([TechCrunch — Fingo × Ecobank][tc-fingo]).

### Branch scale and commentary (sparse public scorecard)

Unlike **LOOP**, **Branch** does not sit inside a tier-one group innovation profile circuit that publishes USD transaction totals in business media on the same rhythm. The durable public record for the charter strategy is still the acquisition cycle itself—stake size, regulatory paper, and operator quotes about moving past single-product lending ([Techweez — Branch × Century MFB][techweez-branch])—plus whatever users say in reviews and SME forums. Treat Branch-as-neobank comparisons as category debate: the product is banking, the go-to-market remains app-first credit heritage.

### What outside voices emphasise (praise, pressure, scepticism)

Trade and SME press frame **LOOP** as a “crown jewel” of Kenyan neobanking—celebrating in-app account opening, embedded credit at checkout, and PayBill-style flows without re-keying bill numbers—while leaning on macro colour such as CBK-cited mobile money volumes (**Kenyan shilling (KSh)** 6.59 trillion in 2024 in one feature’s telling) to argue the country is tilting cashless ([Bizna Kenya — LOOP feature][bizna-loop]). That is optimistic narrative copy, useful for how LOOP wants to be *read*, not a substitute for CBK primary tables.

**TechCrunch**’s analysis layer on **Fingo** was cooler: Kenya’s bank–fintech partnerships are “few and far between” compared with **Nigeria**’s faster collaboration habit; CBK took time to interrogate data, transactions, and customer-handling boundaries before approval; and **M-PESA**’s dominance of mobile money—the piece cited **Safaricom** controlling more than 90% of that medium—plus entrenched **KCB** and **Equity** digital channels would make “onboard millions” a slog, not a given ([TechCrunch — Fingo × Ecobank][tc-fingo]). That tension—inclusion narrative versus distribution physics—is the honest outer commentary track.

User-side discourse (app-store reviews, social threads, podcasts such as the **TechTrends KE** LOOP reset episode) tends to cluster around UX whiplash after major redesigns and support latency—not captured in tidy KPI tables but decisive for trust ([TechTrends KE — LOOP podcast][techtrends-loop]).

## Ecosystem effects

App-first banking UX forced incumbents to ship faster, publish tariffs in clickable form, and staff product and design benches that banks once rented from vendors. It also exported Kenyan talent templates—**M-SHWARI**-shaped operators are reference cases across the region ([LOOP leadership][loop-leadership]). BaaS adoption ([chapter 16](16-jenga-api-banking-platformization.md)) meant neobank experiments could prototype on shared rails; MFB M&A showed credit-first apps a second path to deposit products when sponsor deals felt too slow ([Techweez — Branch × Century MFB][techweez-branch]).

## Setbacks and controversies

Fraud migrates to the onboarding funnel; social engineering targets new users who confuse chat support with bank support. Major app changes trigger backlash visible in public social threads—trust is UX-sensitive. Partnership neobanks face questions about who carries losses and who answers regulators when products misfire. Charter acquisitions inherit legacy core debt, staff culture clash, and integration timetables that press releases understate ([Techweez — Branch × Century MFB][techweez-branch]). BaaS outages and contract changes hit every downstream brand that bet the farm on one integration ([chapter 16](16-jenga-api-banking-platformization.md)).

## Competition and alternatives

**M-PESA** and Sacco culture still anchor millions of users. Traditional retail apps (**Equity**, **KCB**, **Co-operative Bank of Kenya**, **Absa**, **Standard Chartered**), DCP lenders with wallet-like UX, regional super-apps, and global fintech wallets compete for the same attention minutes. Neobank labels are a small slice of that field—many users never care whether the backend is BaaS, MFB, or tier-one core banking so long as float clears and fees feel fair. The competitive vector is often lifestyle bundling and trust repair after a bad chatbot day—not only interest rates.

## Legacy and open questions

Legacy: banking became something you evaluate like software—onboarding minutes, notification quality, reversal speed. Open questions: fairness of digital exclusion, sustainable unit economics for youth segments, how CBK supervision evolves when front-end brands multiply behind partner licences, whether open finance standards converge or stay balkanised by bank ([The Paypers — CBK open banking plan][paypers-open-bank], [CBK — Kenya's Payments Journey][cbk-payments]), and which governance model—sub-brand, partnership, or owned charter—survives the next credit cycle.

## Builder read

*Interpretation.*

Ship recovery UX as deliberately as onboarding UX: when a user is scared, your chat bot is the regulator’s front line. Treat KYC images and metadata as sensitive personal data with retention limits you can defend to ODPC without sweating ([Data Protection Act][dpa]). If you are buying BaaS from [chapter 16](16-jenga-api-banking-platformization.md)’s world, model multi-rail fallbacks and contract sunsets; if you are shipping a neobank skin, map referee interfaces explicitly—users will blame the icon on the phone, not the PDF schedule in legal’s folder.

## See also

- [16. Jenga API and the Platformization of Banking](16-jenga-api-banking-platformization.md)
- [18. Retail Banking App as Table Stakes](18-retail-banking-app-table-stakes.md)
- [8. M-PESA: The Payment OS](../part-03/08-mpesa-payment-os.md)
- [19. Cellulant: The Pan-African Payments OG](../part-06/19-cellulant.md)
- [Part index](index.md)

## Sources

- `SRC-13` — [Data Protection Act, 2019](https://new.kenyalaw.org/akn/ke/act/2019/24/eng%402019-11-15)
- `SRC-16` — [Digital Credit Providers Regulations, 2022](https://new.kenyalaw.org/akn/ke/act/ln/2022/46/eng%402022-04-22)
- `SRC-17` — [Office of the Data Protection Commissioner](https://www.odpc.go.ke/who-we-are/)
- `SRC-69` — [LOOP — Our Leadership](https://loop.co.ke/about-us/our-leadership/)
- `SRC-70` — [Fingo Africa — About us](https://www.fingo.africa/about-us)
- `SRC-71` — [TechCrunch — Fingo × Ecobank, $4M seed / Kenya launch](https://techcrunch.com/2023/05/04/kenyas-fingo-partners-with-ecobank-launches-neobank-on-the-back-of-4m-investment/)
- `SRC-72` — [TechTrends KE — 24Bit podcast, LOOP app reset (Mar 2023)](https://techtrendske.co.ke/2023/03/20/24bit-podcast-a-sitdown-with-loop-discussing-their-new-app-and-new-approach/)
- `SRC-73` — [Swala Nyeti — NCBA / LOOP innovation profile (LOOP metrics to end 2024)](https://swalanyeti.co.ke/business/article/9972/how-ncba-group-is-leading-africas-financial-revolution-through-innovation)
- `SRC-74` — [Bizna Kenya — NCBA LOOP “crown jewel” feature (Feb 2025)](https://biznakenya.com/ncba-loop-the-crown-jewel-of-kenyas-neobanking/)
- `SRC-75` — [Techweez — Branch acquires Century Microfinance Bank (Mar 2022)](https://techweez.com/2022/03/02/branch-acquires-century-microfinance/)
- `SRC-76` — [The Paypers — CBK open banking / payments vision summary (Jan 2021)](https://thepaypers.com/fintech/news/central-bank-of-kenya-releases-plan-to-implement-open-banking)
- `SRC-38` — [CBK — *Kenya's Payments Journey* (PDF)](https://www.centralbank.go.ke/wp-content/uploads/2023/02/Kenyas-Payments-Journey.pdf)
- `SRC-82` — [The Paypers — Nigerian digital bank Umba starts operations in Kenya (Feb 2023)](https://thepaypers.com/fintech/news/nigerian-digital-bank-umba-starts-operations-in-kenya)
- `SRC-78` — [TechCrunch — FairMoney in talks to buy Umba, $20M all-stock frame (Feb 2024)](https://techcrunch.com/2024/02/20/nigerian-digital-bank-fairmoney-in-talks-to-buy-umba-in-20m-all-stock-deal-sources-say/)
- `SRC-79` — [TechCrunch — Most African neobanks remain in the red (Jan 2024)](https://techcrunch.com/2024/01/31/despite-glimmers-of-profit-most-african-neobanks-remain-in-the-red/)
- `SRC-80` — [Innovation Village — Umba $5M debt facility, Kenya secured lending (Oct 2024)](https://innovation-village.com/umba-secures-5m-to-scale-secured-lending-in-kenya-eyes-profitability-in-2024/)
- [Full Source Catalog](../appendices/sources.md)

---

### Navigate

← Previous: [← 16. Jenga API and the Platformization of Banking](16-jenga-api-banking-platformization.md) · [Part 5 index](index.md) · Next: [18. Retail Banking App as Table Stakes](18-retail-banking-app-table-stakes.md) →
