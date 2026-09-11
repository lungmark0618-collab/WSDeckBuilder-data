#!/usr/bin/env python3
"""Extract deck-construction exceptions from official Japanese card text.

The app's normal deck validator can default to "same card name <= 4".
This tool emits machine-readable overrides for cards whose official text
changes that deck construction rule.
"""

import argparse
import glob
import json
import os
import re
from datetime import datetime, timezone, timedelta


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SAME_NAME_PATTERN = re.compile(
    r"このカードと同じカード名のカードは、デッキに"
    r"(?:(好きな枚数)|([0-9０-９]+)枚まで)入れることができる。"
)
COMBINED_NAME_PATTERN = re.compile(
    r"このカードと同じカード名のカードと、"
    r"((?:「[^」]+」(?:と、)?)+)は、デッキに合計([0-9０-９]+)枚まで入れることができる。"
)
QUOTED_NAME_PATTERN = re.compile(r"「([^」]+)」")


def parse_int(value):
    table = str.maketrans("０１２３４５６７８９", "0123456789")
    return int(value.translate(table))


def load_card_files(resources):
    for path in sorted(glob.glob(os.path.join(resources, "*_cards.json"))):
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
        yield path, data.get("meta", {}), data.get("cards", [])


def make_source_card(file_name, meta, card, rule_text_jp, rule_text_zh):
    return {
        "id": card.get("id"),
        "file": file_name,
        "title_code": meta.get("title_code"),
        "title_name_zh": meta.get("title_name_zh"),
        "name_jp": card.get("name_jp"),
        "name_zh": card.get("name_zh"),
        "rule_text_jp": rule_text_jp,
        "rule_text_zh": rule_text_zh,
    }


def matching_zh_sentence(text_zh):
    if not text_zh:
        return ""
    for sentence in re.split(r"(?<=。)", text_zh):
        if "牌組" in sentence and ("同名" in sentence or "同卡名" in sentence or "合計" in sentence or "任意" in sentence or "喜歡的張數" in sentence):
            return sentence.strip()
    return ""


def extract_rules(resources):
    same_name_rules = {}
    combined_rules = {}

    for path, meta, cards in load_card_files(resources):
        file_name = os.path.basename(path)
        for card in cards:
            text_jp = card.get("text_jp") or ""
            text_zh = card.get("text_zh") or ""

            for match in SAME_NAME_PATTERN.finditer(text_jp):
                name_jp = card.get("name_jp")
                if not name_jp:
                    continue
                limit = None if match.group(1) else parse_int(match.group(2))
                rule_text_jp = match.group(0)
                source = make_source_card(
                    file_name, meta, card, rule_text_jp, matching_zh_sentence(text_zh)
                )
                entry = same_name_rules.setdefault(
                    name_jp,
                    {
                        "type": "same_name_limit",
                        "name_jp": name_jp,
                        "names_jp": [name_jp],
                        "limit": limit,
                        "limit_kind": "unlimited" if limit is None else "fixed",
                        "source_cards": [],
                    },
                )
                if entry["limit"] != limit:
                    raise ValueError(f"Conflicting same-name limits for {name_jp}")
                entry["source_cards"].append(source)

            for match in COMBINED_NAME_PATTERN.finditer(text_jp):
                name_jp = card.get("name_jp")
                other_names = QUOTED_NAME_PATTERN.findall(match.group(1))
                if not name_jp or not other_names:
                    continue
                names = [name_jp, *other_names]
                limit = parse_int(match.group(2))
                key = tuple(sorted(names))
                rule_text_jp = match.group(0)
                source = make_source_card(
                    file_name, meta, card, rule_text_jp, matching_zh_sentence(text_zh)
                )
                entry = combined_rules.setdefault(
                    key,
                    {
                        "type": "combined_name_limit",
                        "names_jp": sorted(names),
                        "limit": limit,
                        "limit_kind": "fixed",
                        "source_cards": [],
                    },
                )
                if entry["limit"] != limit:
                    raise ValueError(f"Conflicting combined limits for {key}")
                entry["source_cards"].append(source)

    rules = sorted(
        same_name_rules.values(),
        key=lambda item: (item["limit"] if item["limit"] is not None else 9999, item["name_jp"]),
    )
    rules.extend(
        sorted(combined_rules.values(), key=lambda item: (item["limit"], item["names_jp"]))
    )
    return rules


def write_json(path, rules):
    data = {
        "schema_version": 1,
        "updated_at": datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds"),
        "default_same_name_limit": 4,
        "rules": rules,
    }
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def format_limit(rule):
    if rule["limit_kind"] == "unlimited":
        return "任意張數"
    return f"{rule['limit']} 張"


def write_report(path, rules):
    same_name = [rule for rule in rules if rule["type"] == "same_name_limit"]
    combined = [rule for rule in rules if rule["type"] == "combined_name_limit"]

    lines = [
        "# Deck Building Rules",
        "",
        "Generated from official Japanese `text_jp` deck-construction clauses.",
        "",
        "The app should keep the default same-card-name limit at 4, then apply these machine-readable overrides.",
        "",
        "## Validator Usage",
        "",
        "- Count deck cards by canonical Japanese card name, not by card ID or translated name.",
        "- For `same_name_limit`, use `names_jp[0]` as the card-name group. If `limit_kind` is `unlimited`, do not report a same-name count violation for that name; otherwise compare the count with `limit`.",
        "- For `combined_name_limit`, sum all cards whose Japanese names are in `names_jp`, then compare that total with `limit`.",
        "- `source_cards` is provenance for review and debugging. It should not be used as the rule target because alternate printings can have different card IDs.",
        "",
        "## Same Name Limits",
        "",
        "| Name JP | Limit | Source Cards |",
        "|---|---:|---|",
    ]
    for rule in same_name:
        ids = ", ".join(source["id"] for source in rule["source_cards"])
        lines.append(f"| {rule['name_jp']} | {format_limit(rule)} | {ids} |")

    lines.extend(
        [
            "",
            "## Combined Name Limits",
            "",
            "These rules cap multiple card names together. They do not raise the default 4-card limit, but the deck validator should enforce them so alternate-name or paired cards are handled correctly.",
            "",
            "| Names JP | Combined Limit | Source Cards |",
            "|---|---:|---|",
        ]
    )
    for rule in combined:
        names = " / ".join(rule["names_jp"])
        ids = ", ".join(source["id"] for source in rule["source_cards"])
        lines.append(f"| {names} | {rule['limit']} 張 | {ids} |")

    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))
        handle.write("\n")


def main():
    parser = argparse.ArgumentParser(description="Extract deck-building rules from card data")
    parser.add_argument("--resources", default=os.path.join(ROOT, "cards"))
    parser.add_argument("--out", default=os.path.join(ROOT, "deck_building_rules.json"))
    parser.add_argument("--report", default=os.path.join(ROOT, "docs", "deck_building_rules.md"))
    args = parser.parse_args()

    rules = extract_rules(args.resources)
    write_json(args.out, rules)
    write_report(args.report, rules)

    same = sum(1 for rule in rules if rule["type"] == "same_name_limit")
    combined = sum(1 for rule in rules if rule["type"] == "combined_name_limit")
    unlimited = sum(
        1
        for rule in rules
        if rule["type"] == "same_name_limit" and rule["limit_kind"] == "unlimited"
    )
    raised = sum(
        1
        for rule in rules
        if rule["type"] == "same_name_limit"
        and rule["limit_kind"] == "fixed"
        and rule["limit"] > 4
    )
    print(f"wrote {args.out}")
    print(f"wrote {args.report}")
    print(f"same_name_rules={same} unlimited={unlimited} fixed_over_4={raised}")
    print(f"combined_name_rules={combined}")


if __name__ == "__main__":
    main()
