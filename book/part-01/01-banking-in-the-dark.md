---
title: 1. Banking in the Dark
slug: banking-in-the-dark
part: 1
part_title: Before the Hype
chapter: 1
topic_type: rail
period: 1968–2007
stack_layer: banking_it
tags:
  - topic
---

# 1. Banking in the Dark

## Lead

**Banking in the dark** is Kenya's pre-app financial stack: core ledgers, branch networks, card switches, and batch reconciliation—run under **Central Bank of Kenya (CBK)** supervision—long before M-PESA. The [Kenya Bankers Association (KBA) technology timeline][kba-tech] places the start of serious bank computerisation in **June 1968**, when National and Grindlays Bank installed an **International Computers Limited (ICL)** mainframe in Nairobi as a central repository for branch data. **Barclays Bank of Kenya** rolled out full branch computerisation from **November 1982** (Enterprise Road branch first, then countrywide). **Standard Chartered** introduced **debit cards** and **automated teller machines (ATMs)** in **1989**. **Kenya Commercial Bank (KCB)** joined the **Society for Worldwide Interbank Financial Telecommunication (SWIFT)** network in **1994**. By the **early 2000s** customers could use any branch of their bank, ATMs offered deposits and transfers, and banks interconnected on shared ATM switches such as **PesaPoint**. **Co-operative Bank** launched **short message service (SMS)** balance and enquiry banking in **2004**—still not **peer-to-peer (P2P)** mobile money, which arrived when **M-PESA** went **commercial on 6 March 2007** (Safaricom’s own milestone narrative, [M-PESA background][mpesa-17]). **Vodafone**’s group-side retrospective traces the same **M-PESA** arc from the multinational parent’s angle—helpful triangulation beside **Safaricom**’s Kenyan newsroom copy ([Vodafone — M-PESA 15 years][vodafone-mpesa]). Those banking milestones sit on the same [KBA page][kba-tech].

Alongside global vendors, **local financial software** became an export category. **Craft Silicon**, founded by **Kamal Budhabhatti in 2000**, grew from custom bank software work into a firm serving institutions in dozens of countries and won the **2010 Africa Awards for Entrepreneurship** grand prize, as told in [How We Made It in Africa — Budhabhatti profile][hwmia-craft] and [Meet the Boss][hwmia-boss]. That combination—**mainframe-era discipline**, **card and SWIFT-era integration**, and **Kenyan-built banking products**—trained the integrator culture that later wired banks to telcos, **application programming interfaces (APIs)**, and government payment gateways. The human cost centre behind the dates is still the night shift: mismatched files, payroll cutoffs, and auditors asking for a trail—failure modes mobile money would inherit, not erase.

## Context

Picture Nairobi in the late 1990s: glass towers going up, but inside many banks the decisive machinery was still **batch windows** and **maintenance contracts**. Kenya was moving through **financial liberalisation**—more institutions, tighter competition, periodic shocks—and the **Central Bank of Kenya (CBK)** sat in the middle as referee for solvency, reporting, and, increasingly, **payments-system plumbing**. The CBK bulletin [*Kenya’s Payments Journey*][cbk-payments] summarises decades of retail payments evolution, from ATMs and clearing-house automation toward mobile money.

Banks were the **largest institutional buyers of computing** most citizens would never see. They had the capital for hardware, the regulatory motive for controls, and the geography problem of **branches spread across counties** that had to agree on one balance for the same customer. There was no app-store fintech story yet. The “product” was **trust that tomorrow’s balance matched yesterday’s truth**.

That is what this chapter means by **banking in the dark**: the invisible stratum of **core banking, reconciliation, treasury, cards, and SWIFT**—the work that had to succeed before Kenya could credibly bolt on **M-PESA (from 6 March 2007)** and later **open APIs** without the whole edifice shaking.

## History

### Mainframes and the branch as a data-entry outpost

The Kenya Bankers Association’s published technology history opens with a deliberate humbling detail: before plug-in cores, Kenyan banking ran on **passbooks, manual ledgers, and slow clearing**—cheques could take **more than a month** to clear in the 1950s, improving to **21 days by the 1980s**, with branches often open only **half days** so staff could balance books ([KBA technology timeline][kba-tech]). Computerisation was not glamour. It was **hours returned to the business day**.

The same [KBA timeline][kba-tech] dates the start of serious automation to **June 1968**, when **National and Grindlays Bank** installed a **16K ICL mainframe** in Nairobi as a **central depository for branch data**, with data punched to **paper tape** before ingestion—**programming done in Britain**, not River Road. **KCB** followed with its own **systems and programming division at Gigiri (1972)**, then **Key-Edit magnetic-tape capture (1975)** and new mainframes in **1977** as earlier machines aged. The lesson for the stack: Kenya’s “integration culture” did not begin with **representational state transfer (REST)** APIs. It began with **making branch totals match head office**.

### Barclays, cards, and the ATM as a public computer

**Barclays Bank of Kenya** appears in the KBA narrative as the first bank to **fully computerise branch operations**, piloting **Barclays International Accounting System** from **November 1982** at **Enterprise Road, Nairobi**, then rolling outward ([KBA technology timeline][kba-tech]). For ordinary customers, the visible face of that shift was later the **ATM**—a machine that taught PINs, queues, and **after-hours cash** before mobile phones did.

**Standard Chartered** introduced **debit cards and ATMs in 1989**. **Barclays, KCB, and Co-operative Bank** followed ([KBA technology timeline][kba-tech]). **KCB joined SWIFT in 1994**, wiring Kenya’s largest retail bank into **international message-based settlement**—another rehearsal for the protocol-heavy world fintech would later inhabit ([same timeline][kba-tech]).

### Any-branch banking, shared ATMs, and the SMS teaser

By the **early 2000s**, the customer-visible story changed: you were no longer chained to the branch that opened your account. **ATMs gained deposit and transfer features**. Banks began **interconnecting switches**—the [KBA page][kba-tech] names **PesaPoint** as a network many banks joined. (PesaPoint would later intersect the **M-PESA** story in the late 2000s, but here it matters as proof that **interbank interoperability** was already a design problem.)

**Co-operative Bank’s SMS banking (2004)** let customers check balances and track cheques—**still not peer-to-peer (P2P) digital cash**, but a direct line from banking batch systems to the handset ([KBA timeline][kba-tech]). When **M-PESA** went **live on 6 March 2007**, it did not land in a banking vacuum. It landed in a country already trained on **personal identification numbers (PINs)**, settlement language, and shared rails—even if those rails were mostly **bank-centric**—as both the [KBA timeline][kba-tech] and [*Kenya’s Payments Journey*][cbk-payments] emphasise.

### Kamal Budhabhatti and Craft Silicon — the local vendor as protagonist

Global cores dominated the biggest banks, but **Kenyan-owned software** carved a parallel track. **Kamal Budhabhatti**, an Indian-born entrepreneur who built his career in Kenya, is the best-documented face of that wave. In interviews with *How We Made It In Africa*, he described arriving in Kenya, working in data entry, then writing **bank software on the side** for a friend’s introduction—**losing that side job when his employer objected**, leaving the country, and **choosing to return** because he “could think only about the opportunities in Kenya” ([profile][hwmia-craft]). From that return, **Craft Silicon**—incorporated **2000**—grew into a financial-software house serving **banks, microfinance institutions (MFIs), and savings and credit cooperatives (SACCOs)** across **dozens of countries**, with Budhabhatti recounting **six years without a salary** while reinvesting in growth ([profile][hwmia-craft], [Meet the Boss][hwmia-boss]).

Craft’s **2010 Africa Awards for Entrepreneurship** win is a useful cultural marker: the same ecosystem that would later celebrate consumer fintech was already rewarding **boring, export-grade banking stacks** ([How We Made It in Africa][hwmia-craft]). Budhabhatti’s public commentary—calling **Cellulant** and **Seven Seas Technologies** fellow “giants in the making” alongside Craft—maps an early **peer network of Kenyan enterprise vendors** ([same source][hwmia-craft]).

### Composite scene: the night that must not miss

*Composite, grounded in documented bank ops practice:* A **branch operations supervisor**—we’ll avoid a name—ends month-end under fluorescent light, watching a **reconciliation queue** refuse to clear because one branch’s **general ledger (GL)** batch landed twice. The **IT liaison** on the phone is not reading a blog about “agile”. They are asking which **file version** was posted and whether **rollback** will void customer-facing entries. **Internal audit** has already flagged **segregation of duties** on the user account that ran the job. No camera records the moment. The Central Bank never tweets it. But that night is when **Kenya’s stack learned discipline**—the same discipline that later makes **instant payments** credible because someone, somewhere, still knows how to **prove** what happened.

## Product and mechanics

Under the glass, **core banking** meant **customer and account masters**, **deposits and loans modules**, **general ledger**, **limits**, and **end-of-day batch** that stitched branches into one institution. **Treasury** and **dealing** often ran on adjacent systems. **Cards** added **authorisation switches**, **chargeback workflows**, and **Payment Card Industry (PCI)**-flavoured paranoia before the acronym was everyday.

Retail **user experience (UX)** was still **passbook, cheque, ATM**—not REST. Engineers lived in **cut-off times**, **file formats**, and **reconciliation keys**. “Real time” was often **near-time** with a human sign-off. When something broke, the incident was measured in **Nairobi hours lost** and **regulator-facing incident notes**, not GitHub stars.

## Business model and incentives

Revenue for banks flowed from **net interest margin and fees**, not **monthly active users (MAU)**. **Information technology (IT)** spend was **capital expenditure (capex)** and **operating expenditure (opex)** justified by **risk reduction** and **throughput**. Global vendors sold **licences and maintenance**. Systems integrators billed **person-days**. Local product firms like Craft sold **implementation + support** tied to **regulatory change** (new reporting lines, new products), as described in [How We Made It in Africa’s Craft Silicon coverage][hwmia-craft].

That incentive tree is why **integration talent** clustered in Nairobi: the work paid, the problems were hard, and the references—**a go-live on a core module**—mattered more than a demo day.

## Regulation and referees

The **CBK** oversaw **prudential health** and, over time, **national payments strategy**—later synthesised in publications such as [*Kenya’s Payments Journey*][cbk-payments], which explicitly threads **ATM adoption, clearing automation, and mobile money** into one narrative. Inside each bank, **internal audit** and **risk** translated those rules into **access matrices** and **change-control boards**—the everyday referees engineers love to grumble about and later miss when building in looser sectors.

## Adoption in Kenya

Adoption radiated **from corporate and urban retail outward**. **Cards and ATMs** reached middle-class Nairobi and major towns first. **Rural and informal cash** remained dominant well into the 2000s—the same **margins M-PESA would later price for**. The important adoption metric for this chapter is not smartphone penetration; it is **how many Kenyans learned to trust a machine-readable balance** before they trusted a **mobile wallet**.

## Ecosystem effects

The hidden guild left three **structural** gifts. First, **integrators** who could ship inside hostile legacy environments—skills that migrated cleanly into **bank–telco projects** and **eCitizen payment files**. Second, **buyer sophistication**: bank IT departments learned to evaluate vendors, run **disaster recovery (DR)** drills, and survive audits—raising the bar for anyone who sells into regulated finance. Third, **cultural respect for settlement**—the idea that **a payment is not done until it is proven**—which still shows up in how Kenyans talk about **M-PESA confirmations** and **reversals**.

Craft Silicon’s story also proves **exportability**: Kenyan financial software became a **receipt-backed** answer to the cliché that Africa only consumes foreign tech ([How We Made It in Africa][hwmia-craft]).

## Setbacks and controversies

**Vendor lock-in** meant upgrades were **multi-year projects**. **Technical debt** rewarded **short wrappers** that later became **security debt**. **Talent pooled in Nairobi**, widening a **service geography gap** smaller towns felt for decades. Incidents—**ATM fraud**, **insider posting**, **SWIFT-related scams** globally—rarely produce tidy public post-mortems in this era. The contested ground is often **who owned the control weakness** (vendor, integrator, or bank). Gender archives are thin: **women ran operations floors and IT project management offices (PMOs)**, but their stories are under-represented in press profiles compared with **founder interviews**—a gap worth fixing in oral-history passes.

## Competition and alternatives

**Global core vendors** and **Big Four consultancies** shaped the top tier. **Regional integrators** implemented. **Local product houses** squeezed into **MFIs, SACCOs**, and **tier-2 banks**. The alternative stack was **manual ledgers and long cheque clearing**—real for smaller players and, in pockets, **long after** peers bragged about real-time apps.

## Legacy and open questions

Without this basement, **Kenya’s payments integration advantage**—the ability to wire **banks, telcos, and state portals** into one conversation—reads like luck. It was not. Open questions: **firm-level timelines** (who went live when, from primary annual reports), **labour histories** of bank IT workforces, and **archival photographs** of early machine rooms—material culture still scarce online.

## Builder read

*Interpretation.*

Selling into banks means your **release train** includes **security review, disaster recovery (DR), and audit evidence**—not only a feature checklist. Competing with banks means exploiting **legacy integration cost** while respecting **regulatory trust** as their moat. Whitespace: products that **lower reconciliation and proof cost** without demanding **core replacement** still match the incentive curve this era created.


## See also

- [2. The Cybercafe Republic](02-cybercafe-republic.md)
- [3. Telcoms Before the Boom](03-telcoms-before-the-boom.md)
- [8. M-PESA: The Payment OS](../part-03/08-mpesa-payment-os.md)
- [Part index](index.md)

## Sources

- `SRC-28` — [How Kamal Budhabhatti built Craft Silicon](https://www.howwemadeitinafrica.com/how-kamal-budhabhatti-built-one-of-kenyas-foremost-it-companies/17410/)
- `SRC-29` — [Meet the Boss: Kamal Budhabhatti](https://www.howwemadeitinafrica.com/meet-the-boss-kamal-budhabhatti-ceo-craft-silicon-kenya/16861/)
- `SRC-30` — [Craft Silicon — management / about](https://www.craftsilicon.com/about/management-team/)
- `SRC-07` — [Vodafone — M-PESA 15-year history](https://www.vodafone.com/news/newsroom/empowering-people/mpesa-marks-15-years)
- `SRC-04` — [Safaricom newsroom — M-PESA 17 years background](https://newsroom.safaricom.co.ke/innovation/m-pesa-17-years-of-transforming-lives/)
- `SRC-34` — [KBA — History of Banking in Kenya (Technology)](https://bankinghistory.kba.co.ke/technology/)
- `SRC-38` — [CBK — *Kenya's Payments Journey* (PDF)](https://www.centralbank.go.ke/wp-content/uploads/2023/02/Kenyas-Payments-Journey.pdf)
- [Full Source Catalog](../appendices/sources.md)

<!-- Inline citation targets — see **Sources** for `SRC-XX` IDs. -->
[kba-tech]: https://bankinghistory.kba.co.ke/technology/
[mpesa-17]: https://newsroom.safaricom.co.ke/innovation/m-pesa-17-years-of-transforming-lives/
[vodafone-mpesa]: https://www.vodafone.com/news/newsroom/empowering-people/mpesa-marks-15-years
[cbk-payments]: https://www.centralbank.go.ke/wp-content/uploads/2023/02/Kenyas-Payments-Journey.pdf
[hwmia-craft]: https://www.howwemadeitinafrica.com/how-kamal-budhabhatti-built-one-of-kenyas-foremost-it-companies/17410/
[hwmia-boss]: https://www.howwemadeitinafrica.com/meet-the-boss-kamal-budhabhatti-ceo-craft-silicon-kenya/16861/

---

### Navigate

← **Previous:** [Prologue](../prologue.md) · [**Part 1 index**](index.md) · **Next:** [2. The Cybercafe Republic](02-cybercafe-republic.md) →
