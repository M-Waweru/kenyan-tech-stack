---
title: 16. Jenga API and the Platformization of Banking
slug: jenga-api-banking-platformization
part: 5
part_title: Banks Become Platforms
chapter: 16
topic_type: rail
period: 2014–today
stack_layer: open_banking_baas
tags:
  - topic
---

# 16. Jenga API and the Platformization of Banking

## Lead

A founder who once spent months begging for **portable document format (PDF)** bank statements now calls an **application programming interface (API)** and gets structured data in seconds. That shift is not cosmetic. It changes which companies can exist, how fast they ship, and what “integration” means on a CV.

The **rail** is banking-as-a-service in the practical Kenyan sense: **know your customer (KYC)**, **anti-money laundering (AML)** and customer due diligence hooks, account queries, send-money and receive-payment flows, airtime and bill primitives—surfaced for developers building their own journeys ([Jenga API product site][jenga-io], [Finserve products][finserve-products]). **Finserve Africa**, described on its marketing surfaces as a subsidiary of **Equity Group Holdings PLC**, positioned **Jenga**—Swahili for “build”—as a developer-first stack with a claimed **Payment Card Industry Data Security Standard (PCI DSS)** Level 1 certification posture ([Jenga API product site][jenga-io]). Builders are Finserve engineers, bank digital and integration teams, and the integrator founder wiring callbacks next to **M-PESA** ([Part III](../part-03/index.md)). Users are SMEs, schools, **software as a service (SaaS)** firms, and enterprises that need bank-grade movement without owning a core. Referees are **Central Bank of Kenya (CBK)** oversight, prudential rules, Data Protection Act, 2019 obligations, and the compliance officer who can still say “no” when a flow touches suspicious transaction reporting culture.

The tension is speed versus control: APIs accelerate distribution, but outages, schema changes, and policy shifts propagate straight into dependent products. Once bank capability became a service layer, the next competitive arena became experience—the subject of [chapter 17](17-neobank-wave-banking-ux.md).

## Context

Kenya’s stack by the late 2010s already assumed programmable money: **Safaricom**’s **Daraja** portal (2021) and dense mobile money habit meant many teams could collect; bank APIs answered a different question—ledger truth, settlements, cross-border East Africa corridors, and regulated identity checks for onboarding ([Daraja portal release][daraja-2021], [*Kenya’s Payments Journey*][cbk-payments]). **Equity** had long treated technology as a distribution weapon—**Equitel** and mobile banking rails preceded the **Finserve** carve-out narrative that public materials tell today ([Finserve products][finserve-products]).

## History

### From in-house engine to Finserve and Jenga

Finserve’s own product page traces a lineage through **Equitel** and then **Jenga API**, **Jenga** payment gateway (PGW), and **mKey**—language that frames the unit as Equity’s fintech delivery arm, not a side project ([Finserve products][finserve-products]). The **Jenga** consumer-facing site doubles down on **Equity Group Holdings** ownership and markets a broad menu: send money, receive payments, buy goods and bills, airtime, credit, RegTech (KYC/AML), and account services ([Jenga API product site][jenga-io]).

### Developer formalisation

Documentation and sandbox ergonomics live on **developer.jengahq.io**, the public integration surface partners are steered toward ([Jenga developer portal][jenga-dev]). The chapter does not pretend every Kenyan fintech runs on Jenga—but it does claim this wave normalised a job description: read bank docs, handle OAuth-ish secrets, replay webhooks, and speak compliance well enough to pass enterprise security reviews.

## Product and mechanics

### Composite scene: the compliance thread on release week

*Composite, grounded in typical bank-API integration practice:* A product team prepares go-live on a disbursement flow. Engineering has green tests; risk asks for data-retention mapping under the Data Protection Act, 2019; compliance wants evidence of customer consent for account lookups; operations needs support playbooks when a timeout hits on Friday evening. The API is not “a line of code.” It is a contract that drags referees into the room ([Data Protection Act][dpa]).

Mechanically, builders integrate server-to-server: credentials, signed requests, callback verification, idempotency, and reconciliation files or dashboards. Failures are rarely exotic—clock skew, wrong environment keys, payload drift after a silent version bump—yet they surface as customer trust incidents.

## Business model and incentives

Finserve’s incentives align with **Equity**’s ecosystem strategy: more embedded finance, more transaction throughput, more developer gravity across markets Jenga claims to serve. Partners gain speed; they accept platform dependency—pricing changes, maintenance windows, and terms updates that can rewrite unit economics overnight (Finserve publishes terms and privacy PDFs from the [Jenga API][jenga-io] site footer for readers who need the fine print).

## Regulation and referees

### Referee beat — CBK, credit rules, and data law

CBK remains the macro referee for banking conduct and systemic risk; public payments history from the regulator explicitly threads mobile money and banking modernisation, which is the backdrop against which bank APIs stop looking “experimental” ([*Kenya’s Payments Journey*][cbk-payments]). Where products touch digital credit or lending workflows, Digital Credit Providers Regulations, 2022 and licensing reality matter for what can be shipped without stepping outside perimeter ([DCP Regulations][dcp-regs]). Personal data handling invokes **Office of the Data Protection Commissioner (ODPC)** expectations and the Data Protection Act, 2019 ([ODPC][odpc], [Data Protection Act][dpa]).

## Adoption in Kenya

Adoption clusters where **Equity** banking relationships and integrator culture overlap: payroll and human resources platforms, agritech payouts, education fees, trade finance adjacency, and B2B marketplaces that need multi-country send/receive within East Africa. Exact market share is proprietary; the directional claim is behavioural—“call the bank API” became a plausible sprint, not a twelve-month partnership ritual.

## Ecosystem effects

Jenga-era thinking lowered the floor for “bank-backed” products: startups could prototype on regulated rails, incumbents could court ecosystem distribution, and telco-first Kenya gained a parallel bank integration dialect alongside [Daraja](../part-03/10-daraja-api-turn.md). Friction moved up-stack—to merchant acceptance and checkout wars handled in [Part VI](../part-06/index.md).

## Setbacks and controversies

Dependency risk is the quiet controversy: when a platform pauses or changes rules, downstream users discover they were feature tenants, not owners. Customer ownership fights—who holds the KYC relationship, who owns notifications—show up in partnership disputes long before regulators write a letter.

## Competition and alternatives

Other Kenyan and regional banks built API and open banking-style programmes; global banking-as-a-service vendors compete for enterprise budgets. **M-PESA**-first flows still win many consumer journeys. Competition is less “one winner” than multi-rail fluency: cards, mobile money, and bank APIs chosen by ticket size, settlement, and reconciliation fit.

## Legacy and open questions

Legacy: bank capability as a developer surface became thinkable at national scale. Open questions: interoperability standards, fee transparency for embedded products, incident disclosure norms, and whether concentration of API power creates a new single-point-of-failure map.

## Builder read

*Interpretation.*

Treat bank APIs like critical infrastructure: circuit-breakers, multi-rail fallbacks, and observability that your CFO can read. Assume compliance will move faster than your roadmap. If you cannot explain data flows to a Data Protection Act auditor, you are not ready for scale—only for a demo.

## See also

- [10. Daraja and the API Turn](../part-03/10-daraja-api-turn.md)
- [17. Neobank Wave: Banking as UX](17-neobank-wave-banking-ux.md)
- [18. Retail Banking App as Table Stakes](18-retail-banking-app-table-stakes.md)
- [19. Cellulant: The Pan-African Payments OG](../part-06/19-cellulant.md)
- [Part index](index.md)

## Sources

- `SRC-13` — [Data Protection Act, 2019](https://new.kenyalaw.org/akn/ke/act/2019/24/eng%402019-11-15)
- `SRC-16` — [Digital Credit Providers Regulations, 2022](https://new.kenyalaw.org/akn/ke/act/ln/2022/46/eng%402022-04-22)
- `SRC-17` — [Office of the Data Protection Commissioner](https://www.odpc.go.ke/who-we-are/)
- `SRC-38` — [CBK — *Kenya's Payments Journey* (PDF)](https://www.centralbank.go.ke/wp-content/uploads/2023/02/Kenyas-Payments-Journey.pdf)
- `SRC-65` — [Safaricom — Daraja M-PESA APIs portal (9 Nov 2021)](https://www.safaricom.co.ke/media-center-landing/press-releases/safaricom-simplifies-access-to-m-pesa-apis-to-businesses)
- `SRC-66` — [Finserve Africa — Our Products](https://www.finserve.africa/our-products.php)
- `SRC-67` — [Jenga API — product site](https://www.jengaapi.io/)
- `SRC-68` — [Jenga developer portal](https://developer.jengahq.io/)
- [Full Source Catalog](../appendices/sources.md)

---

### Navigate

← Previous: [← 15. WhatsApp: Kenya's Real Communication Infrastructure](../part-04/15-whatsapp-kenya-rail.md) · [Part 5 index](index.md) · Next: [17. Neobank Wave: Banking as UX](17-neobank-wave-banking-ux.md) →
