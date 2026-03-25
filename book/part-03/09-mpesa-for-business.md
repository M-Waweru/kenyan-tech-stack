---
title: "9. M-PESA for Business: The Stack People Forget"
slug: mpesa-for-business
part: 3
part_title: Money as a Network
chapter: 9
topic_type: rail
period: 2007–today
stack_layer: merchant_acceptance
tags:
  - topic
---

# 9. M-PESA for Business: The Stack People Forget

## Lead

The public story of M-PESA is person-to-person transfer. The operational story is business settlement.

A school bursar reconciles PayBill entries before noon. A landlord checks coded rent references. A merchant validates Till payments against inventory. This is where Kenya’s “cashless-ish” reality became accounting practice, not marketing language. As soon as those flows had to behave like machine-readable events, the next fight was not prettier menus but direct programmability—**Hypertext Transfer Protocol (HTTP)** callbacks, idempotency keys, and the dignity of a ledger that closes without someone retyping **short message service (SMS)**.

## Context

**April 2020** trade press captured the strategic geometry in plain language: **Visa** and **Safaricom** announced a partnership framed as opening **M-PESA**’s **East African** financial-services footprint to **Visa**’s global **merchant** and **card** acceptance network—**TechCrunch** cited **200** countries on the **Visa** side—while jointly developing new **digital payment** products for **M-PESA** users; the same reporting noted the arrangement still needed **regulatory** approval, a reminder that even marquee logos finish in referee offices, not only in press releases ([TechCrunch — Visa and Safaricom][tc-visa-mpesa]). The article also relayed **Safaricom**-sourced scale snapshots contemporaneous to the deal—on the order of **24.5 million** **M-PESA** customers and **176,000** agents, with **domestic** mobile-money **market share** described as above **75%** for years—figures readers should treat as **issuer-disclosed** context passed through a journalist, not an independent audit ([TechCrunch — Visa and Safaricom][tc-visa-mpesa]).

Business adoption grew because consumer trust already existed. Once households were comfortable sending money to relatives, institutions could ask them to pay fees, rent, and subscriptions the same way—without retraining the country on a new mental model. Safaricom’s own narrative of M-PESA’s evolution into business-facing experiences and later **application programming interface (API)**-linked flows tracks that progression from transfer utility to operational stack ([M-PESA 17 years background][mpesa-17], [Daraja annual note][daraja-note]).

The **merchant acceptance rail**—PayBill, **Till** (**Buy Goods**), **Lipa na M-PESA**, and the small-business tools that followed—turned “I sent it” into “it matched the reference.” That shift is what finance teams hear when they say **reconciliation**.

## History

### Manual discipline first

Early business use often lived in **SMS** screenshots, PDF exports, and end-of-day spreadsheets. It worked because volumes were tolerable and staff patience was high. The same **2009** scale that made P2P national—**6 million** registered users and **7,023 agents**—also made it plausible for schools and landlords to standardise on PayBill-style discipline ([Safaricom annual report 2009][safaricom-2009]).

### Structured collection identifiers

PayBill and Till flows gave payers a **shared grammar**: a business number, a reference or narrative field, and a confirmation that could be audited. For many **small and medium-sized enterprises (SMEs)**, that grammar mattered more than card terminals, because it met customers where they already paid.

### Automation and APIs

As volumes rose, copy-paste became a failure mode. Safaricom’s **Daraja** framing in **2018** annual materials is explicit: open APIs as the bridge from “payment service” to “payments-enabled ecosystem” ([Daraja annual note][daraja-note]). The **November 2021** announcement of a self-serve **Daraja** developer portal—marketed as slashing integration lead times that could exceed **sixty days**—crystallised that story for mainstream SMEs ([Safaricom — Daraja portal release][daraja-2021]). The technical spine lives in [chapter 10](10-daraja-api-turn.md); the business story here is **dependency**: once reconciliation is electronic, outages and callback bugs become revenue events.

## Product and mechanics

### Composite scene: school fees and the PayBill register

*Composite, grounded in common PayBill reconciliation practice:* A private school posts one PayBill number and requires student admission numbers as account references. Finance staff export daily confirmations, match references against class lists, and flag unmatched entries for parent follow-up. Compared with cash desk reconciliation, this reduces missing-record disputes and speeds end-of-day balancing.

### Composite scene: Till at the counter

*Composite, grounded in typical retail acceptance practice:* A hardware shop quotes a Till (**Buy Goods**) prompt at checkout. The buyer initiates payment from their handset; the seller watches for the confirmation tone and the SMS. Inventory notes and the Till log have to agree before the shutter closes. The “product” is not the beep—it is **traceability** when a dispute returns tomorrow.

For business users, three mechanics usually decide whether the rail is loved or resented: **structured collection identifiers** (PayBill, Till, tariffs that match ticket size), **confirmation and reconciliation records** (references, narratives, exports), and **settlement visibility** plus dispute handling when something lands in the wrong narrative field. At the counter, the buyer often still initiates **Lipa na M-PESA** from **unstructured supplementary service data (USSD)** `*334#` or **SIM Tool Kit (STK)**—the same keypad rails [chapter 8](08-mpesa-payment-os.md) describes—while the merchant watches for the beep and the **short message service (SMS)**.

## Business model and incentives

M-PESA for business creates **operational stickiness**: rent collection, fee seasons, and daily turnover route through the same rail until switching feels like a migration project. Merchants trade cash-handling friction and broader acceptance against fees, platform policy changes, and reversal complexity. The platform gains throughput and ecosystem depth; it also inherits **support heat** when reconciliation fails.

## Regulation and referees

Business flows touch **payments governance**, **data protection**, and **cybercrime** enforcement once transaction data sits in **customer relationship management (CRM)** systems, **enterprise resource planning (ERP)** exports, and long-lived logs ([Data Protection Act][dpa], [Cybercrimes Act][cyber-act]). The **Central Bank of Kenya (CBK)** sits in the wider payments narrative that connects banking history to mobile money ([*Kenya’s Payments Journey*][cbk-payments]). Refereeing is rarely one letter from one agency; it is the **compliance mesh** your finance officer actually reads.

## Adoption in Kenya

Adoption cut across education, housing, transport, faith organisations, and digital commerce—anywhere recurring collections met a population already fluent in **subscriber identity module (SIM)**-first payment. CA’s sector statistics continue to show enormous **mobile money** and **data** depth, which is the ambient market within which business acceptance remains rational ([CA sector statistics Q3 FY2024/25][ca-q3-2025]).

## Ecosystem effects

Digital receipts and references normalised **audit-friendly** habits for informal trade. SMEs gained faster end-of-day closes; marketplaces could assume a payment confirmation primitive; software vendors found recurring demand for **reconciliation** and **receipt** tooling. That demand fed directly into developer-facing payment APIs—[Daraja and the API Turn](10-daraja-api-turn.md).

## Setbacks and controversies

Wrong-destination errors, delayed reversals, spoofed confirmation scams, and support bottlenecks are not rare anecdotes. At scale they are **trust taxes** on digital commerce—felt first by finance assistants and shop owners, not by strategy decks.

## Competition and alternatives

Cards, bank transfers, and app-native checkout compete, especially in formal urban retail. M-PESA remains strongest where **ticket sizes**, **liquidity**, and **user familiarity** favour the rail everyone already carries.

## Legacy and open questions

M-PESA for business made “digital payment acceptance” ordinary for sectors that never identified as fintech. Open questions include **fee** design under concentration, **interoperability** across wallets and banks, faster **dispute** resolution, and shared **anti-fraud** standards for merchant-facing flows.

## Builder read

*Interpretation.* If you build merchant tools in Kenya, your real product is not payment initiation. It is reconciliation confidence.

Design for traceability, error recovery, and support handoff clarity. That is what business users actually pay for.

## See also

- [8. M-PESA: The Payment OS](08-mpesa-payment-os.md)
- [10. Daraja and the API Turn](10-daraja-api-turn.md)
- [11. What M-PESA Did to the Ecosystem](11-mpesa-ecosystem-effects.md)
- [Part index](index.md)

## Sources

- `SRC-04` — [Safaricom newsroom — M-PESA 17 years background](https://newsroom.safaricom.co.ke/innovation/m-pesa-17-years-of-transforming-lives/)
- `SRC-05` — [Safaricom annual report note — Daraja](https://www.safaricom.co.ke/annualreport_2018/daraja-our-bridge-to-m-pesas-future.php)
- `SRC-65` — [Safaricom — Daraja M-PESA APIs portal (9 Nov 2021)](https://www.safaricom.co.ke/media-center-landing/press-releases/safaricom-simplifies-access-to-m-pesa-apis-to-businesses)
- `SRC-13` — [Data Protection Act, 2019](https://new.kenyalaw.org/akn/ke/act/2019/24/eng%402019-11-15)
- `SRC-14` — [Computer Misuse and Cybercrimes Act, 2018](https://new.kenyalaw.org/akn/ke/act/2018/5/eng%402018-05-18)
- `SRC-38` — [CBK — *Kenya's Payments Journey* (PDF)](https://www.centralbank.go.ke/wp-content/uploads/2023/02/Kenyas-Payments-Journey.pdf)
- `SRC-49` — [Safaricom annual report and accounts 2009 (PDF)](https://www.safaricom.co.ke/images/Investorrelation/2009_annual_report.pdf)
- `SRC-51` — [CA sector statistics report Q3 FY2024/25 (PDF)](https://www.ca.go.ke/sites/default/files/2025-06/Sector%20Statistics%20Report%20Q3%202024-2025.pdf)
- `SRC-105` — [TechCrunch — Visa and Kenya’s Safaricom partner on M-PESA payments (Apr 2020)](https://techcrunch.com/2020/04/30/visa-and-kenyas-safaricom-partner-on-m-pesa-payments-and-tech/)
- [Full Source Catalog](../appendices/sources.md)

<!-- Inline citation targets — see **Sources** for `SRC-XX` IDs. -->
[ca-q3-2025]: https://www.ca.go.ke/sites/default/files/2025-06/Sector%20Statistics%20Report%20Q3%202024-2025.pdf
[cbk-payments]: https://www.centralbank.go.ke/wp-content/uploads/2023/02/Kenyas-Payments-Journey.pdf
[cyber-act]: https://new.kenyalaw.org/akn/ke/act/2018/5/eng%402018-05-18
[dpa]: https://new.kenyalaw.org/akn/ke/act/2019/24/eng%402019-11-15
[daraja-2021]: https://www.safaricom.co.ke/media-center-landing/press-releases/safaricom-simplifies-access-to-m-pesa-apis-to-businesses
[daraja-note]: https://www.safaricom.co.ke/annualreport_2018/daraja-our-bridge-to-m-pesas-future.php
[mpesa-17]: https://newsroom.safaricom.co.ke/innovation/m-pesa-17-years-of-transforming-lives/
[safaricom-2009]: https://www.safaricom.co.ke/images/Investorrelation/2009_annual_report.pdf
[tc-visa-mpesa]: https://techcrunch.com/2020/04/30/visa-and-kenyas-safaricom-partner-on-m-pesa-payments-and-tech/

---

### Navigate

← **Previous:** [← 8. M-PESA: The Payment OS](08-mpesa-payment-os.md) · [**Part 3 index**](index.md) · **Next:** [10. Daraja and the API Turn](10-daraja-api-turn.md) →
