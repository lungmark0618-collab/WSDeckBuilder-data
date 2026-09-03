#!/usr/bin/env python3
"""把 docs/series_breakdown.json 裡 Codex 補的官方商品名稱，轉成 App 可以直接
讀的 product_code -> 官方彈次標籤對照表（wave_names.json）。

只有「一個系列被拆成多彈」時才需要標籤：同一系列裡，每個 product 的
official_display_name_jp 通常是「系列日文名（可能包上「」或前面多一段商品
分類字樣）+ 版本字樣」（例如「葬送のフリーレン Vol.2」、「ブースターパック
「進撃の巨人」Vol.2」），把系列日文名那段拿掉、剩下的部分就是彈次標籤
（例如「Vol.2」）。第一彈通常官方名稱跟系列本名完全對得上，扣掉後剩空
字串，代表不需要額外標籤（App 端會直接顯示系列名，不加彈次）。

同一個系列裡只要有任何一彈算不出標籤、或算出來的標籤跟別彈撞在一起
（例如同名輕小說很多集，官方名稱都一樣，只是集數不同、這份資料看不出來），
整個系列就整批不寫進這個檔案——寧可讓 App 全部退回舊的「第一彈/第二彈」
數字猜測法當備援，也不要同一個系列裡一部分用官方名稱、一部分用猜的，
造成不一致。

用法：
    python3 tools/make_wave_names.py
"""
import json
import os
from typing import Optional

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
SRC_PATH = os.path.join(ROOT, "docs", "series_breakdown.json")
OUT_PATH = os.path.join(ROOT, "wave_names.json")

BRACKETS = "「」『』"


def derive_label(title_name_jp: str, official_name_jp: str) -> Optional[str]:
    if not official_name_jp or not title_name_jp:
        return None
    official_name_jp = official_name_jp.strip()
    title_name_jp = title_name_jp.strip()
    if official_name_jp == title_name_jp:
        return ""  # 這一彈的官方名稱就是系列本名，不需要額外標籤
    clean_official = "".join(ch for ch in official_name_jp if ch not in BRACKETS)
    clean_title = "".join(ch for ch in title_name_jp if ch not in BRACKETS)
    idx = clean_official.find(clean_title)
    if idx == -1:
        return None  # 官方名稱跟系列本名對不起來（可能是跨作聯名），不硬猜
    label = clean_official[idx + len(clean_title):].strip(" 　「」『』")
    if label and not any(ch.isalnum() for ch in label):
        return None  # 只剩標點符號的殘渣（例如官方名稱多打一個冒號），不當標籤用
    return label


def main():
    data = json.load(open(SRC_PATH, encoding="utf-8"))
    labels: dict = {}
    skipped_titles = []

    for s in data.get("sets", []):
        if s.get("product_count", 0) <= 1:
            continue
        title_name_jp = s.get("title_name_jp", "")
        per_title: dict = {}
        ok = True
        for p in s.get("products", []):
            code = p.get("product_code")
            official_name_jp = p.get("official_display_name_jp")
            if not code:
                continue
            label = derive_label(title_name_jp, official_name_jp)
            if label is None:
                ok = False
                break
            per_title[code] = label
        # 標籤必須每彈都拿得到、而且彼此不重複，才代表這份資料真的分得清楚
        if ok and len(set(per_title.values())) == len(per_title):
            labels.update(per_title)
        else:
            skipped_titles.append(s.get("title_code"))

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump({"waves": labels}, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")

    print(f"寫入 {len(labels)} 筆彈次標籤到 {OUT_PATH}")
    if skipped_titles:
        print(f"以下 {len(skipped_titles)} 個系列的官方名稱資料不夠乾淨，整批略過（App 端會退回數字猜測法）：")
        print(", ".join(skipped_titles))


if __name__ == "__main__":
    main()
