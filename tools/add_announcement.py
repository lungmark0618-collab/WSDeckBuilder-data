#!/usr/bin/env python3
"""在 announcements.json 加一則通知。

用法：
    python3 tools/add_announcement.py "標題" "內容，可以寫長一點"

加完直接檢查一下 announcements.json 再 push——這支腳本不會自動 commit。

這個目錄底下的 .py 改動也會觸發 manifest CI 重新產生，commit 標題請務必寫中文，
不然會變成使用者在 App 設定裡看到的更新說明（notes 直接取 commit 標題）。
"""
import argparse
import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, "..", "announcements.json")


def slugify(title: str) -> str:
    # 抓開頭幾個中英數字元當 id 的可讀部分，避免整串標題塞進 id
    keep = re.sub(r"[^0-9A-Za-z一-鿿]+", "-", title).strip("-")
    return keep[:20] if keep else "note"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", help="通知標題")
    parser.add_argument("body", help="通知內容")
    parser.add_argument("--date", help="不填就用今天（YYYY-MM-DD）")
    args = parser.parse_args()

    date = args.date or datetime.date.today().isoformat()

    feed = {"schema_version": 1, "items": []}
    if os.path.exists(PATH):
        feed = json.load(open(PATH, encoding="utf-8"))

    item_id = f"{date}-{slugify(args.title)}"
    if any(item["id"] == item_id for item in feed["items"]):
        item_id = f"{item_id}-{len(feed['items'])}"

    feed["items"].append({
        "id": item_id,
        "date": date,
        "title": args.title,
        "body": args.body,
    })

    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(feed, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"加好了：{item_id}")
    print(f"共 {len(feed['items'])} 則通知，記得 git add / commit / push")


if __name__ == "__main__":
    sys.exit(main())
