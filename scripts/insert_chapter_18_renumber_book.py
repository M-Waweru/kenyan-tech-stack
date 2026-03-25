#!/usr/bin/env python3
"""One-off: insert new chapter 18 in Part V; renumber former 18–76 to 19–77; rename topic files.

Run from repo root after updating CHAPTERS in scaffold_topic_articles.py.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
BOOK = BASE / "book"

# Old chapter -> slug (before insert)
OLD_SLUG: dict[int, str] = {
    18: "18-cellulant",
    19: "19-dpo-cross-border-cards",
    20: "20-jambopay",
    21: "21-pesapal",
    22: "22-ecitizen",
    23: "23-egov-for-everything",
    24: "24-iprs-huduma-niims-identity",
    25: "25-kenya-high-profile-hacks-state",
    26: "26-kenya-exam-machine",
    27: "27-eneza-edtech",
    28: "28-brck-offline-classroom",
    29: "29-elimu-local-content",
    30: "30-kicd-curriculum-governance",
    31: "31-school-ops-fees-messaging",
    32: "32-moringa-school-skills-rail",
    33: "33-andela-global-talent",
    34: "34-uber-bolt-driver-backlash",
    35: "35-little-cab",
    36: "36-glovo-jumia-delivery",
    37: "37-twiga",
    38: "38-sendy",
    39: "39-lori-trucking",
    40: "40-marketforce-copia",
    41: "41-digital-lending-boom",
    42: "42-tala-branch",
    43: "43-fuliza",
    44: "44-crb-collections-licensing-backlash",
    45: "45-sportpesa",
    46: "46-forex-crypto-trading-culture",
    47: "47-chamas-table-banking",
    48: "48-digitizing-chamas",
    49: "49-sacco-digitization",
    50: "50-m-changa",
    51: "51-whatsapp-financial-coordination",
    52: "52-remittances-invisible-export",
    53: "53-stablecoins-parallel-dollar",
    54: "54-vasp-regulation",
    55: "55-online-work-livelihood",
    56: "56-ai-supply-chain-labeling",
    57: "57-wefarm",
    58: "58-apollo-one-acre-fund",
    59: "59-paygo-m-kopa-dlight-sunking",
    60: "60-watu-mobility-finance",
    61: "61-roam-ev-standards",
    62: "62-givedirectly-cash-resilience",
    63: "63-creators-media-economy",
    64: "64-memes-political-force",
    65: "65-disinformation-for-hire",
    66: "66-cambridge-analytica-influence",
    67: "67-gen-z-protests",
    68: "68-crackdowns-lawfare-civic-tech",
    69: "69-high-profile-hacks-cultural-memory",
    70: "70-cyber-maturity-trust-industry",
    71: "71-stack-thickens",
    72: "72-regulation-becomes-product",
    73: "73-interoperability-wars",
    74: "74-cross-border-battlefield",
    75: "75-compute-arrives",
    76: "76-kenya-stack-2045",
}


def chapter_to_part_old(ch: int) -> int:
    if ch <= 3:
        return 1
    if ch <= 7:
        return 2
    if ch <= 13:
        return 3
    if ch <= 15:
        return 4
    if ch <= 17:
        return 5
    if ch <= 21:
        return 6
    if ch <= 25:
        return 7
    if ch <= 33:
        return 8
    if ch <= 36:
        return 9
    if ch <= 40:
        return 10
    if ch <= 44:
        return 11
    if ch <= 46:
        return 12
    if ch <= 51:
        return 13
    if ch <= 54:
        return 14
    if ch <= 56:
        return 15
    if ch <= 62:
        return 16
    if ch <= 65:
        return 17
    if ch <= 68:
        return 18
    if ch <= 70:
        return 19
    return 20


def chapter_to_part_new(ch: int) -> int:
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


def main() -> None:
    # Phase 1: move to temp names
    for n in range(76, 17, -1):
        part = chapter_to_part_old(n)
        slug = OLD_SLUG[n]
        src = BOOK / f"part-{part:02d}" / f"{slug}.md"
        if not src.exists():
            print("MISSING", src, file=sys.stderr)
            sys.exit(1)
        tmp = BOOK / f"part-{part:02d}" / f"_renumtmp_{n}.md"
        src.rename(tmp)
        print("tmp", n, "->", tmp.name)

    # Phase 2: temp -> final path with new slug
    for n in range(18, 77):
        part_old = chapter_to_part_old(n)
        tmp = BOOK / f"part-{part_old:02d}" / f"_renumtmp_{n}.md"
        if not tmp.exists():
            print("MISSING TMP", tmp, file=sys.stderr)
            sys.exit(1)
        new_n = n + 1
        part_new = chapter_to_part_new(new_n)
        suffix = OLD_SLUG[n].split("-", 1)[1]
        new_slug = f"{new_n:02d}-{suffix}"
        dest = BOOK / f"part-{part_new:02d}" / f"{new_slug}.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        tmp.rename(dest)
        print("move", n, "->", dest.relative_to(BOOK))

    # Phase 3: patch chapter numbers and slugs inside every book markdown
    slug_pairs: list[tuple[str, str]] = []
    for n in range(76, 17, -1):
        new_n = n + 1
        o = OLD_SLUG[n]
        ns = f"{new_n:02d}-" + o.split("-", 1)[1]
        slug_pairs.append((o, ns))

    for path in sorted(BOOK.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        orig = text
        for old_s, new_s in slug_pairs:
            text = text.replace(old_s, new_s)
        for n in range(76, 17, -1):
            text = re.sub(
                rf"^chapter: {n}\s*$",
                f"chapter: {n + 1}",
                text,
                flags=re.MULTILINE,
            )
            text = re.sub(rf"^# {n}\.\s+", f"# {n + 1}. ", text, flags=re.MULTILINE)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print("patched", path.relative_to(BASE))


if __name__ == "__main__":
    main()
