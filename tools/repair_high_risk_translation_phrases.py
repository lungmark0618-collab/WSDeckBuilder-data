#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conservative repair pass for known high-risk WS translation artifacts."""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CARDS = ROOT / "cards"
PROTECTED = re.compile(r"(《[^》]*》|「[^」]*」)")
KANA = re.compile(r"[\u3040-\u309f\u30a0-\u30fa\u30fc-\u30ff]")

HIGH_RISK = [
    "休息室到放置",
    "手牌從舞台",
    "舞台從休息室",
    "對手到",
    "手牌到返回",
    "手牌到加入",
    "傷害賦予",
    "傷害与",
    "与傷害",
    "的卡手牌",
    "的卡攻擊",
    "的卡舞台",
    "你費用可以支付",
    "次的能力得到",
    "放置可以",
    "到見",
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


def high_risk_count(text: str) -> int:
    clean = strip_protected(text)
    return sum(clean.count(pattern) for pattern in HIGH_RISK)


def repair_segment(s: str) -> str:
    # Exact broken phrases from the previous rough post-processing pass.
    replacements = {
        "你費用可以支付": "你可以支付費用",
        "費用可以支付": "可以支付費用",
        "如此做的話": "這麼做了的話",
        "手牌到返回": "回到手牌",
        "手牌到可以返回": "可以回到手牌",
        "手牌到加入": "加入手牌",
        "休息室到放置": "放到休息室",
        "傷害區到放置": "放到傷害區",
        "能量區到放置": "放到能量區",
        "的卡手牌從舞台到被放置時": "此卡從手牌被放置到舞台時",
        "的卡手牌從舞台到置或回合中": "在此卡從手牌被放置到舞台的回合中",
        "的卡舞台從休息室到被放置時": "此卡從舞台被放置到休息室時",
        "的卡舞台從休息室到置或時": "此卡從舞台被放置到休息室時",
        "手牌從舞台到被放置時": "從手牌被放置到舞台時",
        "手牌從舞台到置或回合中": "從手牌被放置到舞台的回合中",
        "舞台從休息室到被放置時": "從舞台被放置到休息室時",
        "舞台從休息室到置或時": "從舞台被放置到休息室時",
        "的卡攻擊時": "此卡攻擊時",
        "。的卡": "。此卡",
        "，的卡": "，此卡",
        "〔的卡": "〔此卡",
        "的卡的攻擊的終到": "此卡的攻擊結束時",
        "的卡的對手": "此卡的戰鬥對手",
        "的卡的正面的角色": "此卡正面的角色",
        "的卡的力量": "此卡攻擊力",
        "的卡的魂傷": "此卡魂傷",
        "的卡次的能力得到": "此卡獲得以下能力",
        "此卡手牌到返回": "此卡回到手牌",
        "此卡回憶到": "將此卡送入回憶區",
        "次的能力得到": "獲得以下能力",
        "次的能力賦予": "賦予以下能力",
        "放置可以": "可以放置",
        "CX區到": "CX區有",
        "的牌組洗牌": "將那個牌組洗牌",
        "牌組的上到放置": "放到牌組最上方",
        "牌組的下到放置": "放到牌組最下方",
        "牌組的上或休息室到放置": "放到牌組最上方或休息室",
        "牌組的上或下到放置": "放到牌組最上方或最下方",
        "回合的終到": "回合結束時",
        "CX的等級0與，視為": "CX的等級視為0",
        "等級0與，視為": "等級視為0",
        "傷害取消發生": "傷害取消照常發生",
        "，、": "，",
        "、": "，",
    }
    for old, new in replacements.items():
        s = s.replace(old, new)

    regexes = [
        (r"對手到([xXＸ\d]+)傷害(\d+)回賦予", r"給予對手\1點傷害\2次"),
        (r"對手到([xXＸ\d]+)傷害(\d+)回与", r"給予對手\1點傷害\2次"),
        (r"對手到([xXＸ\d]+)傷害賦予", r"給予對手\1點傷害"),
        (r"對手到([xXＸ\d]+)傷害与", r"給予對手\1點傷害"),
        (r"對手到([xXＸ\d]+)傷害", r"給予對手\1點傷害"),
        (r"([^\n。！？，]*)選擇對手到見", r"\1選擇給對手看"),
        (r"(\d+)張為止", r"至多\1張"),
        (r"([xXＸ])張為止", r"至多\1張"),
        (r"自己的牌組的從上方(\d+)張", r"自己的牌組最上方\1張卡"),
        (r"你自己的牌組的從上方(\d+)張", r"自己的牌組最上方\1張卡"),
        (r"你自己的牌組從上方(\d+)張", r"自己的牌組最上方\1張卡"),
        (r"牌組的從上方(\d+)張", r"牌組最上方\1張卡"),
        (r"牌組從上方(\d+)張", r"牌組最上方\1張卡"),
        (r"^的卡", r"此卡"),
        (r"^的回合中", r"在那個回合中"),
    ]
    for pattern, repl in regexes:
        s = re.sub(pattern, repl, s)

    s = s.replace("Ｘ", "x")
    s = re.sub(r"，{2,}", "，", s)
    s = s.replace("，。", "。")
    return s


def repair_text(text: str) -> str:
    if high_risk_count(text) == 0:
        return text
    return "".join(seg if protected else repair_segment(seg) for protected, seg in split_protected(text))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    before = after = cards_changed = files_changed = kana_bad = 0
    samples = []
    for path in sorted(CARDS.glob("*_cards.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for card in data.get("cards", []):
            old = card.get("text_zh") or ""
            before += high_risk_count(old)
            new = repair_text(old)
            after += high_risk_count(new)
            if KANA.search(strip_protected(new)):
                kana_bad += 1
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

    print(f"high_risk_before={before}")
    print(f"high_risk_after={after}")
    print(f"cards_changed={cards_changed}")
    print(f"files_changed={files_changed}")
    print(f"kana_outside_protected={kana_bad}")
    for file, cid, old, new in samples:
        print(f"\n--- {file} {cid}")
        print("OLD", old.replace("\n", " / ")[:260])
        print("NEW", new.replace("\n", " / ")[:260])


if __name__ == "__main__":
    main()
