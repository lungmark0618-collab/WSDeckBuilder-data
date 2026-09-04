#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conservative cleanup for common awkward but low-risk WS translation phrases."""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CARDS = ROOT / "cards"
PROTECTED = re.compile(r"(《[^》]*》|「[^」]*」)")

PATTERNS = [
    "對對手造成",
    "對對手1傷害",
    "對對手2傷害",
    "對對手3傷害",
    "對對手4傷害",
    "對對手x傷害",
    "CX區有",
    "你可以那張",
    "在沒有的話",
    "自分",
    "効果",
    "枚数",
    "入替",
    "其他你可以的",
    "他的你的",
    "舞臺",
    "區域",
    "卡片",
    "助立",
    "濃度",
    "手上打出",
    "牌組的上",
    "牌組的下",
    "牌組從上方",
]


def split_protected(text: str):
    pos = 0
    for m in PROTECTED.finditer(text):
        if m.start() > pos:
            yield False, text[pos : m.start()]
        yield True, m.group(0)
        pos = m.end()
    if pos < len(text):
        yield False, text[pos:]


def strip_protected(text: str) -> str:
    return PROTECTED.sub("", text)


def hit_count(text: str) -> int:
    clean = strip_protected(text)
    count = 0
    for pattern in PATTERNS:
        count += clean.count(pattern)
    count += len(re.findall(r"CX區有[^。\n]*有", text))
    return count


def repair_whole_text(text: str) -> str:
    # These include protected card names, so handle the full string first.
    text = re.sub(r"CX區有(「[^」]+」)有", r"CX區有\1", text)
    text = re.sub(r"CX區有(「[^」]+」)有的話", r"CX區有\1的話", text)
    text = re.sub(r"若CX區有(「[^」]+」)，", r"若CX區有\1，", text)
    text = re.sub(r"你的CXCX區有被放置時", "你的CX被放置到CX區時", text)
    text = re.sub(r"CXCX區有被放置時", "CX被放置到CX區時", text)
    text = re.sub(r"你的CX區到(「[^」]+」)被放置時", r"\1被放置到你的CX區時", text)
    text = re.sub(r"CX區到(「[^」]+」)被放置時", r"\1被放置到CX區時", text)
    text = re.sub(r"手牌的(「[^」]+」)將1張公開", r"公開1張手牌的\1", text)
    return text


def repair_segment(s: str) -> str:
    replacements = {
        "對對手造成": "給予對手",
        "對對手1傷害": "給予對手1點傷害",
        "對對手2傷害": "給予對手2點傷害",
        "對對手3傷害": "給予對手3點傷害",
        "對對手4傷害": "給予對手4點傷害",
        "對對手x傷害": "給予對手x點傷害",
        "對對手X傷害": "給予對手x點傷害",
        "對對手Ｘ傷害": "給予對手x點傷害",
        "1傷害": "1點傷害",
        "2傷害": "2點傷害",
        "3傷害": "3點傷害",
        "4傷害": "4點傷害",
        "x傷害": "x點傷害",
        "X傷害": "x點傷害",
        "Ｘ傷害": "x點傷害",
        "在沒有的話": "若不是則",
        "若非如此則": "若不是則",
        "自分的": "自己的",
        "自分的所有角色": "自己的所有角色",
        "効果": "效果",
        "枚数": "張數",
        "入替可以": "可以交換",
        "入替": "交換",
        "其他你可以的": "其他你的",
        "他的你的": "其他你的",
        "他其他你的": "其他你的",
        "舞臺": "舞台",
        "CX 區域": "CX區",
        "CX區域": "CX區",
        "區域": "區",
        "卡片": "卡",
        "助立": "助太刀",
        "濃度": "集中",
        "手上打出": "手牌打出",
        "手上": "手牌",
        "你的若CX區有": "若你的CX區有",
        "你的若": "若你的",
        "力量＋": "攻擊力＋",
        "此能力1回合到1回為止發動": "此能力1回合至多發動1次",
        "1回合到1回為止": "1回合至多1次",
        "的角色的張數": "角色的張數",
        "你對手的等級0以下的角色至多1張選擇": "你選擇至多1張對手等級0以下的角色",
        "你對手的角色2張為止選擇": "你選擇至多2張對手的角色",
        "你自己的角色2張為止選擇": "你選擇至多2張自己的角色",
        "你自己的角色至多2張選擇": "你選擇至多2張自己的角色",
        "你的角色至多2張選擇": "你選擇至多2張自己的角色",
        "自己休息室的角色至多1張選擇": "選擇至多1張自己休息室的角色",
        "你的，若": "你的",
        "你的，": "你的",
        "其他你的，若": "其他你的",
        "其他你的，": "其他你的",
        "若其他你有": "若其他你有",
        "若其他你可以的": "若其他你的",
        "你可以那張角色": "你可以將那張角色",
        "你可以那張卡": "你可以將那張卡",
        "你可以那張": "你可以將那張",
        "可以那張角色": "可以將那張角色",
        "可以那張卡": "可以將那張卡",
        "自己的牌組最上方1張卡查看": "查看自己的牌組最上方1張卡",
        "你自己的牌組最上方1張卡公開": "你公開自己的牌組最上方1張卡",
        "你自己的牌組": "你自己的牌組",
        "牌組的上或下或放到休息室": "放到牌組最上方、最下方或休息室",
        "牌組的上或休息室": "牌組最上方或休息室",
        "牌組的上或放到休息室": "放到牌組最上方或休息室",
        "牌組的上或下": "牌組最上方或最下方",
        "牌組的上到": "牌組最上方",
        "牌組的下到": "牌組最下方",
        "牌組的從下方": "牌組最下方",
        "牌組的從上方": "牌組最上方",
        "的牌組的從下方": "牌組最下方",
        "選擇自己手牌": "選擇自己的手牌",
        "請為你的角色選擇 1": "你選擇1張自己的角色",
        "並在在那個回合中獲得 +": "在那個回合中，攻擊力＋",
        "張卡卡1張選擇": "張卡，選擇1張卡",
        "回憶到，": "送入回憶區，",
        "回憶到": "送入回憶區",
        "裏向到可以": "可以翻成背面朝上",
        "裏向到": "翻成背面朝上",
        "表向到": "翻成正面朝上",
        "裏向的": "背面朝上的",
        "表向的": "正面朝上的",
        "裏向": "背面朝上",
        "表向": "正面朝上",
        "別々的格到放置": "各自放置到不同的格子",
        "別々的格": "不同的格子",
        "舞台的好格到放置": "放置到舞台上任意的格子",
        "舞台的好格": "舞台上任意的格子",
        "舞台的任意的格子放置": "放置到舞台上任意的格子",
        "牌組的上從相同張數放到能量區": "將自己牌組最上方相同張數的卡放到能量區",
        "牌組的上從相同張數": "牌組最上方相同張數",
        "牌組的下放置": "放到牌組最下方",
        "你的卡牌組的下到可以放置": "你可以將此卡放到牌組最下方",
        "牌組的下到可以放置": "可以放到牌組最下方",
        "牌組的下到放置": "放到牌組最下方",
        "牌組的上到放置": "放到牌組最上方",
        "你自己的牌組從上方1張可以查看": "你可以查看自己的牌組最上方1張卡",
        "自己的牌組最上方1張卡可以查看": "可以查看自己的牌組最上方1張卡",
        "此卡從手牌放置到舞台時": "此卡從手牌被放置到舞台時",
        "他的角色": "其他角色",
    }
    for old, new in replacements.items():
        s = s.replace(old, new)

    regexes = [
        (r"給予對手([0-9xXＸ]+)點傷害點傷害", r"給予對手\1點傷害"),
        (r"對對手([0-9xXＸ]+)傷害", r"給予對手\1點傷害"),
        (r"給予對手([0-9xXＸ]+)傷害", r"給予對手\1點傷害"),
        (r"你自己的牌組從上方至多([0-9xXＸ]+)張查看", r"你查看自己的牌組最上方至多\1張卡"),
        (r"自己的牌組從上方至多([0-9xXＸ]+)張查看", r"查看自己的牌組最上方至多\1張卡"),
        (r"牌組從上方至多([0-9xXＸ]+)張查看", r"牌組最上方至多\1張卡查看"),
        (r"卡至多([0-9xXＸ]+)張選擇", r"選擇至多\1張卡"),
        (r"(.+?)1張選擇，回到手牌", r"選擇1張\1，回到手牌"),
        (r"x(.+?)到等", r"x等於\1"),
        (r"Ｘ(.+?)到等", r"x等於\1"),
        (r"那些卡的卡的(.+?)張數", r"那些卡中\1張數"),
        (r"此效果在休息室到置或卡到CX有", r"此效果放到休息室的卡中有CX"),
        (r"此效果在休息室到置或(.+?)的話", r"此效果放到休息室的\1的話"),
        (r"([0-9]+)張為止選擇", r"選擇至多\1張"),
        (r"次的([0-9]+)的效果的你選擇的1行", r"執行以下\1個效果中你選擇的1個"),
        (r"次的對手的回合的結束前", "直到下個對手回合結束為止"),
        (r"，的話", "的話"),
    ]
    for pattern, repl in regexes:
        s = re.sub(pattern, repl, s)

    s = s.replace("Ｘ", "x")
    s = s.replace("張卡卡1張選擇", "張卡，選擇1張卡")
    s = s.replace("自己的將自己牌組最上方相同張數的卡放到能量區", "將自己牌組最上方相同張數的卡放到能量區")
    s = re.sub(r"，{2,}", "，", s)
    s = s.replace("，。", "。")
    s = s.replace("。。", "。")
    return s


def repair_text(text: str) -> str:
    if hit_count(text) == 0:
        return text
    text = repair_whole_text(text)
    text = "".join(seg if protected else repair_segment(seg) for protected, seg in split_protected(text))
    return repair_whole_text(text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    before = after = cards_changed = files_changed = 0
    samples = []
    for path in sorted(CARDS.glob("*_cards.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for card in data.get("cards", []):
            old = card.get("text_zh") or ""
            before += hit_count(old)
            new = repair_text(old)
            after += hit_count(new)
            if new != old:
                cards_changed += 1
                changed = True
                if len(samples) < 20:
                    samples.append((path.name, card["id"], old, new))
                if args.apply:
                    card["text_zh"] = new
        if changed and args.apply:
            meta = data.setdefault("meta", {})
            meta["data_version"] = int(meta.get("data_version", 0)) + 1
            meta["generated_at"] = datetime.now(timezone(timedelta(hours=8))).replace(
                microsecond=0
            ).isoformat()
            path.write_text(
                json.dumps(data, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8",
            )
            files_changed += 1

    print(f"style_hits_before={before}")
    print(f"style_hits_after={after}")
    print(f"cards_changed={cards_changed}")
    print(f"files_changed={files_changed}")
    for file, cid, old, new in samples:
        print(f"\n--- {file} {cid}")
        print("OLD", old.replace("\n", " / ")[:260])
        print("NEW", new.replace("\n", " / ")[:260])


if __name__ == "__main__":
    main()
