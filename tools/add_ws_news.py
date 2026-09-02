#!/usr/bin/env python3
"""在 ws_news_manual.json 加一則手動公告——官網自動抓不到、或想額外補中文
說明的項目用這個，跟 fetch_ws_news.py 抓下來的官方清單分開存，不會被
下次自動抓取覆蓋掉。

用法：
    python3 tools/add_ws_news.py "標題（日文或中文皆可）" \\
        --url https://ws-tcg.com/... --category 商品情報 --zh "中文說明"

加完直接檢查一下 cards/ws_news_manual.json 再 push——這支腳本不會自動
commit，也不會自動跑 make_ws_news.py 合併，記得兩步都要做。
"""
import argparse
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, "..", "cards", "ws_news_manual.json")


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("title", help="標題（title_jp 欄位）")
    parser.add_argument("--zh", default=None, help="中文說明（title_zh 欄位），不填就留空")
    parser.add_argument("--url", default="", help="連結，沒有就留空")
    parser.add_argument("--category", default="公告", help="分類標籤，預設「公告」")
    parser.add_argument("--date", help="不填就用今天（YYYY-MM-DD）")
    args = parser.parse_args()

    date = args.date or datetime.date.today().isoformat()

    feed = {"items": []}
    if os.path.exists(PATH):
        feed = json.load(open(PATH, encoding="utf-8"))

    feed["items"].append({
        "date": date,
        "categories": [args.category],
        "title_jp": args.title,
        "title_zh": args.zh,
        "url": args.url,
        "source": "manual",
    })

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(feed, f, ensure_ascii=False, indent=1)
        f.write("\n")

    print(f"加好了，現在共 {len(feed['items'])} 則手動公告")
    print("記得跑 python3 tools/make_ws_news.py 合併，再 git add / commit / push")


if __name__ == "__main__":
    sys.exit(main())
