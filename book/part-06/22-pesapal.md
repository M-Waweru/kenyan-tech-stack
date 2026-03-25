---
title: "22. Pesapal: The SME Checkout Layer"
slug: pesapal
part: 6
part_title: Merchant Rails
chapter: 22
topic_type: company
period: 2000s–today
stack_layer: sme_checkout
tags:
  - topic
---

# 22. Pesapal: The SME Checkout Layer

## Lead

For a shop owner, payment failure is not a dashboard tile. It is stock stuck in the storeroom, rent due, and a customer who walks to the competitor with working **Lipa na M-PESA**. A stable checkout is the difference between “open” and “closed.”

**Agosta Liko** founded **Pesapal**; the company’s own **About** page claims regulation across five **African** markets and 300+ staff ([Pesapal — About Us][pesapal-about]). **Independent** Kenyan press adds a different lens: **Capital Business** reported **November 2025** that **KCB Group** agreed to take a **minority** stake—subject to **CBK** and competition approvals—framing **Pesapal** as processing card and mobile-money flows for hotels, airlines, retailers, and **SME**s across the same five-country footprint the bank wanted on its balance sheet ([Capital Business — KCB × Pesapal][capital-kcb-pesapal]). The **rail** is **small and medium enterprise (SME)**-friendly digital acceptance: cards and mobile money online and at point of sale, backed by APIs, reporting, and adjacent products (ticketing, reservations) that keep merchants inside one vendor gravity well. **Builders** are onboarding teams, risk analysts, and support desks tuned to businesses that do not have enterprise IT. **Users** are clinics, schools, restaurants, event organisers, and online sellers who need “paid” without hiring a payments engineer. **Referees** are **Central Bank of Kenya (CBK)** and peer regulators, **Data Protection Act, 2019** expectations when customer data transits dashboards, and consumer-protection pressure when receipts or refunds fail ([Data Protection Act][dpa], [ODPC][odpc]).

The tension is inclusion versus fraud: **SME** volumes are smaller per merchant but collectively huge; attackers target weak onboarding. The **shadow** is support load—every false decline becomes a **WhatsApp** escalation.

## Context

By the time **Pesapal** scaled, **Kenya** already treated **M-PESA** as default retail plumbing ([Part III](../part-03/index.md)). **SME**s still needed a neutral checkout brand that could speak **Visa** and **Safaricom** in the same sentence—adjacent to bank merchant programmes ([chapter 16](../part-05/16-jenga-api-banking-platformization.md)) and parallel to pan-African orchestration ([chapter 19](19-cellulant.md)), but legible on a **Pesapal**-branded pay button.

## History

### From a handful of transactions to daily habit

**Pesapal**’s own blog frames an origin story of near-zero early throughput growing into hundreds of thousands of daily transactions—narrative copy readers should treat as directional marketing unless triangulated with filings ([Pesapal — Untold Story][pesapal-story]). The durable fact on the corporate **About** page is regulatory footprint and multi-country operations—a **SME** gateway cannot scale on vibes alone when **CBK** and peers hold the pen ([Pesapal — About Us][pesapal-about]).

### Product bundle as moat

**Pesapal** extended from checkout into adjacent vertical tools (ticketing, hospitality, inventory-flavoured suites in company marketing). That pattern—payments as wedge, operations software as retention—is common among **African** **PSPs** fighting churn.

## Product and mechanics

### Composite scene: Saturday at the boutique

*Composite:* A customer pays at **Pesapal Sabi**-style point-of-sale hardware; the owner checks settlement in the evening before paying suppliers. A failed **STK** **Push** triggers a support call; the owner does not care whether the fault was **Safaricom** latency or **Pesapal** routing—they care that Saturday cash flow cleared.

Mechanically, **SME** gateways combine hosted checkout, **application programming interface (API)** integrations, **mobile money** and card rails, dispute tooling, and settlement reporting. Failure modes: **KYC** friction for micro-merchants, **chargeback** exposure on card legs, and **reconciliation** gaps when **PayBill** references are mis-typed.

## Business model and incentives

Revenue mixes per-transaction fees, device or subscription lines where sold, and value-added products. Incentives favour merchant count and active volume—same gravity that shaped **DPO** and **Cellulant**, at a different average ticket size.

## Regulation and referees

### Referee beat — five central banks, one brand

**Pesapal**’s public claim of multi-country **CBK**-style supervision means compliance work multiplies: licensing conditions, reporting, and consumer rules differ by jurisdiction ([Pesapal — About Us][pesapal-about]). **Kenya**-specific expectations sit inside **CBK** payments modernisation and consumer protection culture ([*Kenya’s Payments Journey*][cbk-payments]).

## Adoption in Kenya

Adoption clusters in urban **SME** retail, hospitality, education fees, and events—anywhere **cash** and **card** mixed with **M-PESA** in the same week. **Pesapal** competes for merchants who want a single invoice for “online + shop floor.”

## Ecosystem effects

**Pesapal**-class players trained SME owners to expect professional receipts, SMS notifications, and dashboard settlement views—the same UX bar retail bank apps later had to match ([chapter 18](../part-05/18-retail-banking-app-table-stakes.md)). They also fed government digitisation: citizens accustomed to phone receipts for shop payments tolerate similar flows for fees ([chapter 21](21-jambopay.md), [Part VII](../part-07/index.md)).

## Setbacks and controversies

Support queues during peak commerce, **fraud** rings targeting **weak** **password** hygiene on **merchant** portals, and **social** **media** **storms** over delayed settlements show up in any high-volume **PSP**. **Multi-product** **bundles** **increase** **attack** **surface**—more dashboards, more credentials.

## Competition and alternatives

**M-PESA** Till and PayBill direct setups, bank merchant acquirers, global gateways, and **Cellulant**- or **DPO**-class competitors fragment the market. SMEs often run two rails—**M-PESA** for local foot traffic, **Pesapal** (or peers) when cards or invoices matter.

## Legacy and open questions

Legacy: Kenya gained a repeatable SME checkout vernacular—API keys and settlement exports became normal small-business literacy. Bank minority stakes (where consummated) will test whether **Pesapal** stays a neutral checkout brand or becomes more visibly a **lender**-adjacent channel—watch filings and regulator notices, not only blog posts ([Capital Business — KCB × Pesapal][capital-kcb-pesapal]). Open questions: margin pressure as interchange and scheme rules shift, open finance impacts on routing, and whether super-app wallets disintermediate standalone gateways.

## Builder read

*Interpretation.*

Optimise for Friday-evening support load: SME merchants pay with their weekend. Instrument decline reasons per rail; offer manual fallbacks without shaming customers who still carry cash.

## See also

- [21. JamboPay: Collections as Anti-Leakage Infrastructure](21-jambopay.md)
- [19. Cellulant: The Pan-African Payments OG](19-cellulant.md)
- [18. Retail Banking App as Table Stakes](../part-05/18-retail-banking-app-table-stakes.md)
- [23. eCitizen: The State Becomes a Product](../part-07/23-ecitizen.md)
- [Part index](index.md)

## Sources

- `SRC-13` — [Data Protection Act, 2019](https://new.kenyalaw.org/akn/ke/act/2019/24/eng%402019-11-15)
- `SRC-17` — [Office of the Data Protection Commissioner](https://www.odpc.go.ke/who-we-are/)
- `SRC-38` — [CBK — *Kenya's Payments Journey* (PDF)](https://www.centralbank.go.ke/wp-content/uploads/2023/02/Kenyas-Payments-Journey.pdf)
- `SRC-89` — [Pesapal — About Us (Kenya; regulated markets)](https://www.pesapal.com/about-us)
- `SRC-90` — [Pesapal blog — The Untold Story of Pesapal (growth narrative)](https://www.pesapal.com/blog/the-untold-story-of-pesapal-from-three-transactions-a-year-to-hundreds-of-thousands-a-day)
- `SRC-96` — [Capital Business — KCB to acquire minority stake in Pesapal (Nov 2025)](https://www.capitalfm.co.ke/business/2025/11/kcb-to-acquire-minority-stake-in-pesapal/)
- [Full Source Catalog](../appendices/sources.md)

---

### Navigate

← **Previous:** [← 21. JamboPay: Collections as Anti-Leakage Infrastructure](21-jambopay.md) · [**Part 6 index**](index.md) · **Next:** [23. eCitizen: The State Becomes a Product](../part-07/23-ecitizen.md) →

[pesapal-about]: https://www.pesapal.com/about-us
[capital-kcb-pesapal]: https://www.capitalfm.co.ke/business/2025/11/kcb-to-acquire-minority-stake-in-pesapal/
[pesapal-story]: https://www.pesapal.com/blog/the-untold-story-of-pesapal-from-three-transactions-a-year-to-hundreds-of-thousands-a-day
[cbk-payments]: https://www.centralbank.go.ke/wp-content/uploads/2023/02/Kenyas-Payments-Journey.pdf
[dpa]: https://new.kenyalaw.org/akn/ke/act/2019/24/eng%402019-11-15
[odpc]: https://www.odpc.go.ke/who-we-are/
