---
title: "19. Cellulant: The Pan-African Payments OG"
slug: cellulant
part: 6
part_title: Merchant Rails
chapter: 19
topic_type: company
period: 2003–today
stack_layer: merchant_payments
tags:
  - topic
---

# 19. Cellulant: The Pan-African Payments OG

## Lead

It is Friday evening and finance is still comparing three spreadsheets: **Ghana** mobile-money settlements, **Nigeria** bank transfers, and **Kenya** **M-PESA** receipts that refuse to match the enterprise resource planning column. Nobody wants “Africa strategy” as a synonym for reconciliation overtime.

**Ken Njoroge** and **Bolaji Akinboro** built **Cellulant** as an answer to that exhaustion—the bet that a merchant should orchestrate wallets, banks, and cards without hiring a small country of analysts per corridor. **TPG**’s **Series C** release names both as co-founders and frames pan-African scale ([TPG — Rise Fund × Cellulant Series C][tpg-cellulant]); **TechCrunch** contributor reporting the same month quoted **Njoroge** on throughput, bank clients, and positioning relative to **M-PESA**—independent tech press carrying the CEO’s own figures, not a substitute for audited statements ([TechCrunch — Africa Roundup, Cellulant][tc-cellulant]). The **rail** is multi-country **merchant** acceptance and settlement orchestration: one commercial relationship and integration posture stretched across fragmented national payment cultures. **Builders** are platform engineers, treasury ops, and partner teams wiring **application programming interface (API)**-style distribution to banks and **mobile network operators**. **Users** are retailers, **agritech** collectors, utilities, and any finance chief who needs “paid” to mean the same thing in **Nairobi** and **Lagos**. **Referees** are **Central Bank of Kenya (CBK)** and peer regulators, **tax** reporting regimes, and **Visa**/**Mastercard** scheme rules that do not care about your sprint board.

The tension is **coverage versus complexity**: every new rail deepens capability and explodes exception handling. The **shadow** is operational drag—fraud signatures differ by market, settlement windows differ by partner, and a single mis-mapped fee code becomes a month-end crisis.

## Context

Kenya’s stack already trained users on instant mobile receipts ([Part III](../part-03/index.md)); bank **API** culture followed through **Finserve**/**Jenga** and **open finance** pressure ([chapter 16](../part-05/16-jenga-api-banking-platformization.md)). **Cellulant** sits one layer out—closer to merchants who must accept whatever the customer’s hand already holds, not only what one bank or one telco prefers. **Daraja**-era **M-PESA** programmability lowered the floor for “integrate **Safaricom**”; pan-African aggregators addressed the harder sentence: “integrate **everyone**.”

## History

### From value-added services imagination to payments spine

**Cellulant**’s public funding narrative centres a **May 2018** **USD 47.5 million** **Series C** led by **The Rise Fund**, described in **TPG**’s release as among the largest fintech cheques of its era focused on African payments—capital earmarked for geographic expansion, consolidation, and scaling sector products including **agriculture** and digital banking adjacencies ([TPG — Rise Fund × Cellulant Series C][tpg-cellulant]). The chapter does not treat one round as destiny; it treats it as a signal that **institutional** capital began pricing “payments OS for many countries” as a category, not a boutique consultancy.

### Scale as both proof and burden

After **Series C**, the story is less about launch headlines than about living inside **multi-jurisdiction** **know your customer (KYC)** refresh cycles, partner certification, and the quiet work of keeping success rates high when **USSD** menus, bank redirects, and wallet prompts diverge by country.

### When independent press and the company disagree

**September 2020** brought a different kind of headline: **Nigerian** business paper **BusinessDay** published a long investigation into **Cellulant**’s **Nigeria** operations—**Akinboro**’s resignation, mass dismissals, lawsuits, and the winding-down of the **Agrikore** agriculture marketplace. The piece blends named court claims, anonymous staff, and on-the-record email from **Cellulant** acknowledging compliance failures on **Agrikore** and a **November 2020** decision to discontinue that marketplace business in **Nigeria** “for now” ([BusinessDay — Cellulant crises feature][bd-cellulant-crisis]). **Kenyan** newsrooms separately tracked **Njoroge**’s planned **CEO** exit timeline into **2021** ([Business Daily — Njoroge to depart][bd-njoroge-depart]). This chapter does not pick winners in those disputes; it treats them as proof that **pan-African** payment brands face **governance** and **narrative** stress tests as large as their **API** maps.

## Product and mechanics

### Composite scene: the treasury war room before month close

*Composite:* A payments operations lead in **Nairobi** chases a stuck settlement file while **Lagos** support escalates a wallet timeout pattern. **Engineering** patches a routing rule; **finance** needs a **SWIFT**-adjacent narrative for auditors; **sales** promises a unified dashboard the spreadsheet truth has not quite caught up with. The product is as much **discipline** as code.

Mechanically, aggregators like **Cellulant** sell consolidated acceptance—**mobile money**, cards, bank channels—plus reconciliation tooling and partner management. Failure modes are familiar: partner downtime, **foreign exchange (FX)** mismatch, **chargeback** disputes on card legs, and **webhook** delivery drama during peak commerce windows.

## Business model and incentives

Revenue typically mixes **transaction** fees, **setup** and **integration** charges, and higher-touch **enterprise** contracts. Incentives align with **volume** and **uptime**: merchants switch when decline rates or support latency hurt conversion. **CBK** and peer regulators indirectly set the ceiling—licensing, **payment service provider** expectations, and consumer-protection posture shape what can be launched without friction ([*Kenya’s Payments Journey*][cbk-payments]).

## Regulation and referees

### Referee beat — many flags, one product roadmap

There is no single “Africa licence.” A pan-African **payment service provider** stack answers to **CBK** in **Kenya**, central banks and communications authorities elsewhere, **Data Protection Act, 2019**-style laws where **personal data** crosses dashboards, and **scheme** compliance for card acceptance ([Data Protection Act][dpa], [ODPC][odpc]). **Cellulant**’s category lives in the paperwork between those chairs.

## Adoption in Kenya

**Kenya** functions as headquarters energy and talent magnet; adoption shows up in large merchants and institutions that already run **M-PESA** **PayBill**/**Till** culture but need multi-country symmetry. Exact market share is proprietary; the directional claim is behavioural—**finance** teams stopped accepting “we will fix **Africa** in phase three” as a serious answer.

## Ecosystem effects

**Cellulant**-class platforms **lowered the integration tax** for regional expansion and trained a generation of **Kenyan** integrators in multi-rail thinking. They also sit upstream of dedicated **card** gateways such as **DPO** ([chapter 20](20-dpo-cross-border-cards.md))—cards stayed essential for travel, **e-commerce**, and **business-to-business** tickets **mobile money** rarely covers alone.

## Setbacks and controversies

**Shadow** costs: partner concentration, **fraud** migration (attackers follow volume), and **customer** perception that “the gateway failed” even when the underlying telco or bank hiccupped. **Fundraising** headlines age quickly; operations age slowly. **Investigative** and **court-sourced** reporting on the **2020** **Nigeria** crisis showed how fast a **flagship** vertical (**Agrikore**) could become a compliance lightning rod—whatever the final allocation of blame ([BusinessDay — Cellulant crises feature][bd-cellulant-crisis]).

## Competition and alternatives

**In-house** builds, bank-led merchant suites, **telco** aggregators, and newer **fintech** switches compete corridor by corridor. **M-PESA**-first **Daraja** flows ([chapter 10](../part-03/10-daraja-api-turn.md)) suit many **Kenyan** SMEs; pan-African orchestration suits anyone whose invoice line items span borders.

## Legacy and open questions

Legacy: **Kenya** exported not only **M-PESA** imagination but **payment orchestration** craft—how to sound credible in **Johannesburg**, **Accra**, and **Nairobi** in the same week. Open questions: **interoperability** mandates, **real-time** settlement norms, and whether **concentration** among a few super-aggregators creates a new systemic map.

## Builder read

*Interpretation.*

Treat each country as its own **referee** stack: **KYC**, **sanctions**, **data residency**, and **scheme** rules drift faster than your **API** versioning policy. **Observability** per partner rail is not optional—your **merchant** sees one brand: yours.

## See also

- [16. Jenga API and the Platformization of Banking](../part-05/16-jenga-api-banking-platformization.md)
- [10. Daraja and the API Turn](../part-03/10-daraja-api-turn.md)
- [20. DPO: Cross-Border Card Rails](20-dpo-cross-border-cards.md)
- [Part index](index.md)

## Sources

- `SRC-13` — [Data Protection Act, 2019](https://new.kenyalaw.org/akn/ke/act/2019/24/eng%402019-11-15)
- `SRC-17` — [Office of the Data Protection Commissioner](https://www.odpc.go.ke/who-we-are/)
- `SRC-38` — [CBK — *Kenya's Payments Journey* (PDF)](https://www.centralbank.go.ke/wp-content/uploads/2023/02/Kenyas-Payments-Journey.pdf)
- `SRC-83` — [TPG — The Rise Fund leads $47.5M Series C for Cellulant (May 2018)](https://www.tpg.com/news-and-insights/first-major-commitment-africa-rise-fund-leads-475-million-series)
- `SRC-92` — [TechCrunch — Africa Roundup; Cellulant / Njoroge interview (Jun 2018)](https://techcrunch.com/2018/06/10/africa-roundup-african-startup-investments-turn-to-fintech-this-winter-season/)
- `SRC-95` — [BusinessDay (Nigeria) — Cellulant crises / Agrikore (investigative)](https://businessday.ng/companies/article/cellulant-the-untold-story-of-the-crises-that-rocked-one-of-africas-leading-fintechs/)
- `SRC-97` — [Business Daily — Cellulant co-founder Ken Njoroge to depart June (Jan 2021)](https://www.businessdailyafrica.com/bd/corporate/companies/cellulant-co-founder-ken-njoroge-to-depart-in-june-3260736)
- [Full Source Catalog](../appendices/sources.md)

---

### Navigate

← **Previous:** [← 18. Retail Banking App as Table Stakes](../part-05/18-retail-banking-app-table-stakes.md) · [**Part 6 index**](index.md) · **Next:** [20. DPO: Cross-Border Card Rails](20-dpo-cross-border-cards.md) →

[tpg-cellulant]: https://www.tpg.com/news-and-insights/first-major-commitment-africa-rise-fund-leads-475-million-series
[tc-cellulant]: https://techcrunch.com/2018/06/10/africa-roundup-african-startup-investments-turn-to-fintech-this-winter-season/
[bd-cellulant-crisis]: https://businessday.ng/companies/article/cellulant-the-untold-story-of-the-crises-that-rocked-one-of-africas-leading-fintechs/
[bd-njoroge-depart]: https://www.businessdailyafrica.com/bd/corporate/companies/cellulant-co-founder-ken-njoroge-to-depart-in-june-3260736
[cbk-payments]: https://www.centralbank.go.ke/wp-content/uploads/2023/02/Kenyas-Payments-Journey.pdf
[dpa]: https://new.kenyalaw.org/akn/ke/act/2019/24/eng%402019-11-15
[odpc]: https://www.odpc.go.ke/who-we-are/
