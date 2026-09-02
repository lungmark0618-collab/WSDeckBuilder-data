#!/usr/bin/env python3
"""抓 ws-tcg.com 官方公告清單（新商品、卡表更新、大會、規則異動）。

官網「お知らせ」頁是純伺服器渲染的靜態頁面，每則公告都是一個
`<li class="news__item">`，裡面有日期、分類、標題、連結，格式很穩定，
用正規表達式抓就夠了，不需要另外裝 BeautifulSoup 這類套件（跟這個
repo 其他工具腳本一樣，刻意不引入額外依賴）。

用法：
    python3 tools/fetch_ws_news.py --out cards/ws_news_auto.json --pages 2
"""

import argparse
import html
import json
import re
import sys
import time
import urllib.request

BASE_URL = "https://ws-tcg.com/information/"
UA = "Mozilla/5.0 (compatible; WSDeckBuilderBot/1.0)"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8")


def parse_items(html_text: str) -> list[dict]:
    items = []
    # 用 <li class="news__item"> 當分隔點，避免內層 <ul><li>（分類清單）造成巢狀誤判
    chunks = html_text.split('<li class="news__item">')[1:]
    for chunk in chunks:
        href_m = re.search(r'<a href="([^"]+)"', chunk)
        date_m = re.search(r'<time class="news__itemDate" datetime="([^"]+)"', chunk)
        title_m = re.search(r'<p class="news__itemTitle">([^<]+)</p>', chunk)
        if not (href_m and date_m and title_m):
            continue
        categories = re.findall(r'<li class="news__itemCatItem">([^<]+)</li>', chunk)
        items.append({
            "date": date_m.group(1),
            "categories": [html.unescape(c.strip()) for c in categories],
            "title_jp": html.unescape(title_m.group(1).strip()),
            "title_zh": None,
            "url": html.unescape(href_m.group(1)),
            "source": "official",
        })
    return items


def main():
    parser = argparse.ArgumentParser(description="抓官網公告清單")
    parser.add_argument("--pages", type=int, default=2, help="抓幾頁（每頁約 30 則）")
    parser.add_argument("--out", default="cards/ws_news_auto.json")
    args = parser.parse_args()

    all_items: list[dict] = []
    seen_urls_dates = set()
    for page in range(1, args.pages + 1):
        url = BASE_URL if page == 1 else f"{BASE_URL}page/{page}/"
        try:
            body = fetch(url)
        except Exception as exc:
            print(f"抓第 {page} 頁失敗：{exc}", file=sys.stderr)
            break
        page_items = parse_items(body)
        if not page_items:
            break
        for item in page_items:
            key = (item["url"], item["date"], item["title_jp"])
            if key in seen_urls_dates:
                continue
            seen_urls_dates.add(key)
            all_items.append(item)
        print(f"第 {page} 頁：{len(page_items)} 則", file=sys.stderr)
        time.sleep(0.5)  # 對官網客氣一點，不要連續狂打

    all_items.sort(key=lambda x: x["date"], reverse=True)
    out = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S+08:00"),
        "items": all_items,
    }
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"共 {len(all_items)} 則 → {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
