#!/usr/bin/env python3
"""
Generate one markdown file per chapter (topic) under book/part-NN/.
Merges existing prose from authoring/manuscript/part-*.md into ## Lead; appends wiki-style section stubs.
"""
from __future__ import annotations

import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
BOOK = BASE / "book"
MANUSCRIPT = BASE / "authoring" / "manuscript"

# part_num -> manuscript filename
PART_MANUSCRIPT: dict[int, str] = {
    1: "part-01-before-the-hype.md",
    2: "part-02-connectivity.md",
    3: "part-03-money-as-a-network.md",
    4: "part-04-messaging-and-social.md",
    5: "part-05-banks-become-platforms.md",
    6: "part-06-merchant-rails.md",
    7: "part-07-the-state-stack.md",
    8: "part-08-education-stack.md",
    9: "part-09-global-apps-local-physics.md",
    10: "part-10-supply-chain-wars.md",
    11: "part-11-credit-habit.md",
    12: "part-12-money-as-entertainment.md",
    13: "part-13-community-finance.md",
    14: "part-14-diaspora-rails.md",
    15: "part-15-work-ai-factory.md",
    16: "part-16-survival-tech.md",
    17: "part-17-creators-memes-misinformation.md",
    18: "part-18-power-vs-networks.md",
    19: "part-19-cybersecurity-era.md",
    20: "part-20-future-stack.md",
}

# chapter -> (slug, topic_type, period_hint, stack_layer)
CHAPTERS: dict[int, tuple[str, str, str, str]] = {
    1: ("01-banking-in-the-dark", "rail", "1988–2007", "banking_it"),
    2: ("02-cybercafe-republic", "rail", "1990s–2000s", "assisted_digital"),
    3: ("03-telcoms-before-the-boom", "rail", "1990s–2007", "telecoms"),
    4: ("04-bitange-ndemo-bet", "institution", "2005–2012", "policy_connectivity"),
    5: ("05-subsea-cable-shock", "rail", "2009–2012", "international_bandwidth"),
    6: ("06-safaricom-platform-incumbent", "company", "2000s–today", "telco_platform"),
    7: ("07-home-internet-wifi-culture", "rail", "2005–today", "fixed_broadband"),
    8: ("08-mpesa-payment-os", "rail", "2007–today", "mobile_money"),
    9: ("09-mpesa-for-business", "rail", "2007–today", "merchant_acceptance"),
    10: ("10-daraja-api-turn", "rail", "2010s–today", "payments_api"),
    11: ("11-mpesa-ecosystem-effects", "concept", "2007–today", "ecosystem"),
    12: ("12-mpesa-africa-expansion-limits", "concept", "2007–today", "comparative"),
    13: ("13-trust-dark-twin-fraud-sim-swaps", "concept", "2007–today", "trust_security"),
    14: ("14-africas-talking", "company", "2010s–today", "comms_api"),
    15: ("15-whatsapp-kenya-rail", "infrastructure", "2010s–today", "messaging"),
    16: ("16-jenga-api-banking-platformization", "rail", "2014–today", "open_banking_baas"),
    17: ("17-neobank-wave-banking-ux", "concept", "2014–today", "consumer_banking"),
    18: ("18-retail-banking-app-table-stakes", "concept", "2014–today", "consumer_banking"),
    19: ("19-cellulant", "company", "2003–today", "merchant_payments"),
    20: ("20-dpo-cross-border-cards", "company", "2000s–today", "card_gateway"),
    21: ("21-jambopay", "company", "2000s–today", "collections"),
    22: ("22-pesapal", "company", "2000s–today", "sme_checkout"),
    23: ("23-ecitizen", "institution", "2014–today", "egov"),
    24: ("24-egov-for-everything", "institution", "2014–today", "egov"),
    25: ("25-iprs-huduma-niims-identity", "institution", "2000s–today", "identity"),
    26: ("26-kenya-high-profile-hacks-state", "concept", "2010s–today", "cybersecurity"),
    27: ("27-kenya-exam-machine", "concept", "—", "education_demand"),
    28: ("28-eneza-edtech", "company", "2010s–today", "edtech"),
    29: ("29-brck-offline-classroom", "company", "2010s–today", "edtech_hardware"),
    30: ("30-elimu-local-content", "company", "2010s–today", "edtech_content"),
    31: ("31-kicd-curriculum-governance", "institution", "—", "curriculum"),
    32: ("32-school-ops-fees-messaging", "concept", "—", "school_ops"),
    33: ("33-moringa-school-skills-rail", "company", "2010s–today", "skills"),
    34: ("34-andela-global-talent", "company", "2010s–today", "talent_export"),
    35: ("35-uber-bolt-driver-backlash", "infrastructure", "2015–today", "mobility"),
    36: ("36-little-cab", "company", "2016–today", "mobility"),
    37: ("37-glovo-jumia-delivery", "concept", "2015–today", "delivery_commerce"),
    38: ("38-twiga", "company", "2014–2024", "ag_supply_chain"),
    39: ("39-sendy", "company", "2010s–today", "logistics"),
    40: ("40-lori-trucking", "company", "2010s–today", "logistics"),
    41: ("41-marketforce-copia", "concept", "2010s–today", "informal_retail"),
    42: ("42-digital-lending-boom", "concept", "2012–2025", "digital_credit"),
    43: ("43-tala-branch", "concept", "2012–today", "digital_credit"),
    44: ("44-fuliza", "rail", "2019–today", "overdraft"),
    45: ("45-crb-collections-licensing-backlash", "concept", "2012–today", "credit_governance"),
    46: ("46-sportpesa", "company", "2010s–today", "betting"),
    47: ("47-forex-crypto-trading-culture", "concept", "2010s–today", "retail_trading"),
    48: ("48-chamas-table-banking", "concept", "—", "community_finance"),
    49: ("49-digitizing-chamas", "concept", "2010s–today", "community_finance"),
    50: ("50-sacco-digitization", "concept", "2000s–today", "cooperatives"),
    51: ("51-m-changa", "company", "2010s–today", "fundraising"),
    52: ("52-whatsapp-financial-coordination", "infrastructure", "2010s–today", "messaging_finance"),
    53: ("53-remittances-invisible-export", "rail", "2010s–today", "remittances"),
    54: ("54-stablecoins-parallel-dollar", "concept", "2020s–today", "crypto"),
    55: ("55-vasp-regulation", "institution", "2020s–today", "crypto_regulation"),
    56: ("56-online-work-livelihood", "concept", "2010s–today", "digital_labor"),
    57: ("57-ai-supply-chain-labeling", "concept", "2010s–today", "ai_labor"),
    58: ("58-wefarm", "company", "2010s–today", "agritech"),
    59: ("59-apollo-one-acre-fund", "concept", "2000s–today", "agritech"),
    60: ("60-paygo-m-kopa-dlight-sunking", "concept", "2010s–today", "paygo_energy"),
    61: ("61-watu-mobility-finance", "company", "2010s–today", "asset_finance"),
    62: ("62-roam-ev-standards", "company", "2020s–today", "emobility"),
    63: ("63-givedirectly-cash-resilience", "institution", "2010s–today", "cash_transfers"),
    64: ("64-creators-media-economy", "concept", "2016–today", "creator_economy"),
    65: ("65-memes-political-force", "concept", "2016–today", "political_media"),
    66: ("66-disinformation-for-hire", "concept", "2016–today", "influence"),
    67: ("67-cambridge-analytica-influence", "concept", "2013–today", "influence_ops"),
    68: ("68-gen-z-protests", "concept", "2010s–today", "activism"),
    69: ("69-crackdowns-lawfare-civic-tech", "concept", "2010s–today", "civic_tech"),
    70: ("70-high-profile-hacks-cultural-memory", "concept", "2010s–today", "cybersecurity"),
    71: ("71-cyber-maturity-trust-industry", "concept", "2020s–today", "cybersecurity"),
    72: ("72-stack-thickens", "concept", "2026–2045", "forecast"),
    73: ("73-regulation-becomes-product", "concept", "2026–2045", "forecast"),
    74: ("74-interoperability-wars", "concept", "2026–2045", "forecast"),
    75: ("75-cross-border-battlefield", "concept", "2026–2045", "forecast"),
    76: ("76-compute-arrives", "concept", "2026–2045", "forecast"),
    77: ("77-kenya-stack-2045", "concept", "2045", "forecast"),
}

PART_TITLE: dict[int, tuple[str, str]] = {
    1: ("Before the Hype", "1968–2007"),
    2: ("Connectivity", "2005–2012"),
    3: ("Money as a Network", "2007–today"),
    4: ("Messaging and Social Rails", "2010–today"),
    5: ("Banks Become Platforms", "2014–today"),
    6: ("Merchant Rails", "2003–today"),
    7: ("The State Stack", "2014–today"),
    8: ("The Education Stack", "—"),
    9: ("Global Apps vs Local Physics", "2015–today"),
    10: ("Supply Chain Wars", "2014–2024"),
    11: ("Credit Becomes a Habit", "2012–2025"),
    12: ("Money as Entertainment", "2016–today"),
    13: ("Community Finance", "forever → now"),
    14: ("Diaspora Rails and Parallel Dollar", "2010–today"),
    15: ("Work-from-Home Republic and AI Factory", "2010–today"),
    16: ("Survival Tech", "—"),
    17: ("Creators, Memes, Misinformation", "2016–today"),
    18: ("Power vs Networks", "2013–today"),
    19: ("Cybersecurity Era", "—"),
    20: ("The Future Stack (2026–2045)", "2026–2045"),
}

SECTION_STUBS = """
## Context

Expand: conditions—market, regulation, distribution, prior rails—that made this topic matter in Kenya.

## History

Expand: dated chronology (founding, launches, scale moments, crises, pivots). Cite [Source Catalog](../appendices/sources.md).

## Product and mechanics

Expand: how it works for users, businesses, and developers (flows, APIs, fees, trust, UX).

## Business model and incentives

Expand: who pays whom, unit economics, strategic constraints.

## Regulation and referees

Expand: CBK, CA, sector regulators, courts, consumer protection—who sets the rules.

## Adoption in Kenya

Expand: segments, channels, geography, typical use cases.

## Ecosystem effects

Expand: what this unlocked downstream (categories, partners, copycats, stack dependencies).

## Setbacks and controversies

Expand: documented failures, backlash, outages, hacks, labor conflict, policy fights.

## Competition and alternatives

Expand: local and global alternatives readers should compare.

## Legacy and open questions

What remains unsettled or in flux.

## Builder read

*Interpretation.* If you are building on or next to this rail today: constraints, failure modes, whitespace.

## See also

- [Part index](index.md)

## Sources

- [Source Catalog](../appendices/sources.md)
"""


def chapter_to_part(ch: int) -> int:
    if ch <= 3:
        return 1
    if ch <= 7:
        return 2
    if ch <= 13:
        return 3
    if ch <= 15:
        return 4
    if ch <= 18:
        return 5
    if ch <= 22:
        return 6
    if ch <= 26:
        return 7
    if ch <= 34:
        return 8
    if ch <= 37:
        return 9
    if ch <= 41:
        return 10
    if ch <= 45:
        return 11
    if ch <= 47:
        return 12
    if ch <= 52:
        return 13
    if ch <= 55:
        return 14
    if ch <= 57:
        return 15
    if ch <= 63:
        return 16
    if ch <= 66:
        return 17
    if ch <= 69:
        return 18
    if ch <= 71:
        return 19
    return 20


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4 :].lstrip("\n")
    return text


def parse_chapters(text: str) -> dict[int, tuple[str, str]]:
    """Return chapter_num -> (title_line_without ##, body until next chapter or EVIDENCE_BLOCK)."""
    text = strip_frontmatter(text)
    # Split on ## N. Title
    pattern = re.compile(r"^## (\d+)\.\s+(.+)$", re.MULTILINE)
    matches = list(pattern.finditer(text))
    out: dict[int, tuple[str, str]] = {}
    for i, m in enumerate(matches):
        num = int(m.group(1))
        title = m.group(2).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]
        stop = body.find("<!-- EVIDENCE_BLOCK -->")
        if stop != -1:
            body = body[:stop]
        body = body.strip()
        out[num] = (title, body)
    return out


def load_all_chapter_titles() -> dict[int, str]:
    titles: dict[int, str] = {}
    for fname in PART_MANUSCRIPT.values():
        p = MANUSCRIPT / fname
        if not p.exists():
            continue
        for num, (title, _) in parse_chapters(p.read_text(encoding="utf-8")).items():
            titles[num] = title
    return titles


def chapter_href(from_ch: int, to_ch: int) -> str:
    fp, tp = chapter_to_part(from_ch), chapter_to_part(to_ch)
    slug = CHAPTERS[to_ch][0] + ".md"
    if fp == tp:
        return slug
    return f"../part-{tp:02d}/{slug}"


def topic_navigation_footer(ch: int, titles: dict[int, str]) -> str:
    part = chapter_to_part(ch)
    mid = f"[**Part {part} index**](index.md)"
    if ch <= 1:
        prev_link = "[Prologue](../prologue.md)"
    else:
        pt = titles.get(ch - 1, f"Chapter {ch - 1}")
        prev_link = f"[← {ch - 1}. {pt}]({chapter_href(ch, ch - 1)})"
    if ch >= 77:
        next_link = "[Appendix — Cast](../appendices/appendix-cast.md)"
    else:
        nt = titles.get(ch + 1, f"Chapter {ch + 1}")
        next_link = f"[{ch + 1}. {nt}]({chapter_href(ch, ch + 1)})"
    return (
        f"\n\n---\n\n### Navigate\n\n"
        f"← **Previous:** {prev_link} · {mid} · **Next:** {next_link} →\n"
    )


def part_intro(text: str) -> str:
    text = strip_frontmatter(text)
    first = re.search(r"^# .+$", text, re.MULTILINE)
    if not first:
        return ""
    after = text[first.end() :].strip()
    m = re.search(r"^## \d+\.", after, re.MULTILINE)
    if m:
        after = after[: m.start()].strip()
    return after.strip()


def yaml_escape(s: str) -> str:
    if any(c in s for c in '":\n'):
        return '"' + s.replace('"', '\\"') + '"'
    return s


def write_topic(ch: int, title: str, lead_body: str, titles: dict[int, str]) -> None:
    part = chapter_to_part(ch)
    slug, topic_type, period, stack_layer = CHAPTERS[ch]
    part_dir = BOOK / f"part-{part:02d}"
    part_dir.mkdir(parents=True, exist_ok=True)
    fn = slug + ".md"
    path = part_dir / fn
    title_full = f"{ch}. {title}"
    fm = f"""---
title: {yaml_escape(title_full)}
slug: {slug.split("-", 1)[1] if "-" in slug else slug}
part: {part}
part_title: {yaml_escape(PART_TITLE[part][0])}
chapter: {ch}
topic_type: {topic_type}
period: {yaml_escape(period)}
stack_layer: {stack_layer}
tags:
  - topic
---

# {title_full}

## Lead

{lead_body}
{SECTION_STUBS}{topic_navigation_footer(ch, titles)}"""
    path.write_text(fm, encoding="utf-8")
    print("Wrote", path.relative_to(BASE))


def write_part_index(part: int) -> None:
    part_dir = BOOK / f"part-{part:02d}"
    part_dir.mkdir(parents=True, exist_ok=True)
    ptitle, pperiod = PART_TITLE[part]
    ms_path = MANUSCRIPT / PART_MANUSCRIPT[part]
    intro = ""
    parsed: dict[int, tuple[str, str]] = {}
    evidence_tail = ""
    if ms_path.exists():
        full = ms_path.read_text(encoding="utf-8")
        intro = part_intro(full)
        parsed = parse_chapters(full)
        if "<!-- EVIDENCE_BLOCK -->" in full:
            idx = full.find("<!-- EVIDENCE_BLOCK -->")
            evidence_tail = "\n\n" + full[idx:]
            evidence_tail = evidence_tail.replace("](../sources.md", "](../appendices/sources.md")

    chaps = sorted(c for c in CHAPTERS if chapter_to_part(c) == part)
    toc_lines = []
    for c in chaps:
        slug, _, _, _ = CHAPTERS[c]
        title = parsed.get(c, (f"Chapter {c}", ""))[0]
        toc_lines.append(f"- [{c}. {title}]({slug}.md)")
    toc = "\n".join(toc_lines)

    index_body = f"""# Part {part}: {ptitle} ({pperiod})

{intro}

## Topics in this part

{toc}
{evidence_tail}
"""
    nav_prev = (
        f"[Part {part - 1} index](../part-{part - 1:02d}/index.md)"
        if part > 1
        else "[Prologue](../prologue.md)"
    )
    nav_next = (
        f"[Part {part + 1} index](../part-{part + 1:02d}/index.md)"
        if part < 20
        else "[Appendix — Cast](../appendices/appendix-cast.md)"
    )
    index_body = re.sub(
        r"\n---\n\n### Navigate the manuscript\n\n.*",
        f"\n\n---\n\n### Navigate\n\n← **Previous:** {nav_prev} · [**Book home**](../index.md) · **Next:** {nav_next} →",
        index_body,
        flags=re.DOTALL,
    )

    front = f"""---
title: "Part {part}: {ptitle}"
part: {part}
part_title: {yaml_escape(ptitle)}
period: {yaml_escape(pperiod)}
chapter_type: part-intro
tags:
  - topic-index
---

"""
    (part_dir / "index.md").write_text(front + index_body, encoding="utf-8")
    print("Wrote", (part_dir / "index.md").relative_to(BASE))


def main() -> None:
    titles = load_all_chapter_titles()
    # Load all manuscript chapter bodies
    by_chapter: dict[int, tuple[str, str]] = {}
    for part, fname in PART_MANUSCRIPT.items():
        p = MANUSCRIPT / fname
        if not p.exists():
            continue
        parsed = parse_chapters(p.read_text(encoding="utf-8"))
        by_chapter.update(parsed)

    for ch in range(1, 78):
        if ch not in CHAPTERS:
            raise SystemExit(f"Missing CHAPTERS entry for {ch}")
        title, body = by_chapter.get(ch, (f"Chapter {ch}", "_No manuscript section found; add content from research._"))
        if not body.strip():
            body = "_Draft: migrate detail from [Source Catalog](../appendices/sources.md) and public records._"
        write_topic(ch, title, body, titles)

    for part in range(1, 21):
        write_part_index(part)


if __name__ == "__main__":
    main()
