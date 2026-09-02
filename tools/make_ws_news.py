#!/usr/bin/env python3
"""合併官網自動抓的公告（cards/ws_news_auto.json）跟手動加的公告
（cards/ws_news_manual.json），產生 App 實際讀取的 ws_news.json。

分開兩個來源檔案是為了讓 fetch_ws_news.py 重跑的時候不會把手動加的項目
洗掉——手動的永遠保留，自動的每次整批覆蓋重抓。

用法：
    python3 tools/make_ws_news.py
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
AUTO_PATH = os.path.join(ROOT, "cards", "ws_news_auto.json")
MANUAL_PATH = os.path.join(ROOT, "cards", "ws_news_manual.json")
OUT_PATH = os.path.join(ROOT, "ws_news.json")

# 首頁列表用不到上百則，只留最近的份量就好，檔案小、App 載入也快
MAX_ITEMS = 80


def load_items(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    return json.load(open(path, encoding="utf-8")).get("items", [])


def main():
    items = load_items(AUTO_PATH) + load_items(MANUAL_PATH)
    # 同一天同標題同連結視為同一則，手動版本（可能帶中文說明）優先保留
    dedup: dict[tuple, dict] = {}
    for item in items:
        key = (item.get("date"), item.get("title_jp"), item.get("url"))
        if key not in dedup or item.get("source") == "manual":
            dedup[key] = item
    merged = sorted(dedup.values(), key=lambda x: x.get("date", ""), reverse=True)[:MAX_ITEMS]

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump({"items": merged}, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"合併完成，共 {len(merged)} 則 → {OUT_PATH}")


if __name__ == "__main__":
    main()
