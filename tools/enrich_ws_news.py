#!/usr/bin/env python3
"""幫「商品情報」類的公告多抓幾筆規格重點（發售日、售價、卡片種類數），
給 App 的公告詳情頁用——使用者點進一則公告後，不用馬上跳出去官網，
先看這幾行重點，有興趣才點連結去看完整頁面。

只在意結構化的規格資料（dt/dd 規格表、售價、卡片種類數這幾行固定
格式的文字），不去解析或翻譯官網的宣傳文案段落——那些是官方寫的
行銷文字，不是這裡該碰的東西，而且自由格式的段落沒辦法可靠地
用正規表達式抓出正確重點。抓不到規格表的公告（規則更新、賽事、
卡表連結等等）highlights_zh 就留空，App 端那則詳情頁只會顯示標題
跟「前往官網查看完整內容」的連結，不會生出不存在的內容。

用法：
    python3 tools/enrich_ws_news.py --in cards/ws_news_auto.json
"""
import argparse
import html
import json
import re
import sys
import time
import urllib.request
from typing import Optional

UA = "Mozilla/5.0 (compatible; WSDeckBuilderBot/1.0)"

_UNIT_ZH = {"パック": "包", "ボックス": "盒", "カートン": "箱"}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def _clean(text: str) -> str:
    text = re.sub(r"<br\s*/?>", " ", text)
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(text).strip()


def extract_detail_image(page_html: str) -> Optional[str]:
    """商品頁自己的商品視覺圖（包裝盒圖），比公告列表頁的縮圖更大張、
    更適合放公告詳情頁——使用者說「官網有放大圖的話我們也要有」，
    這裡就是那張大圖的來源。"""
    m = re.search(r'products__imgin"><img src="([^"]+)"', page_html)
    return html.unescape(m.group(1)) if m else None


def extract_highlights(page_html: str) -> list[str]:
    highlights: list[str] = []

    date_m = re.search(
        r'products__specItem--title">発売日</dt>\s*'
        r'<dd class="products__specItem--detail">([^<]+)</dd>',
        page_html,
    )
    if date_m:
        highlights.append(f"發售日：{_clean(date_m.group(1))}")

    # 「1パック8枚入り／希望小売価格440円(税込)」這種單位＋售價成對出現的段落，
    # 一份商品規格通常有 2～3 段（單包／整盒／整箱），整箱常常沒有標價格
    for block in re.findall(r"<p>(1(?:パック|ボックス|カートン)[\s\S]*?)</p>", page_html):
        text = _clean(block)
        unit_m = re.match(r"1(パック|ボックス|カートン)", text)
        if not unit_m:
            continue
        unit_zh = _UNIT_ZH[unit_m.group(1)]
        price_m = re.search(r"([\d,]+)円\(税込\)", text)
        qty_m = re.search(r"(\d+)(?:パック|枚|ボックス)入り", text)
        parts = [f"整{unit_zh}" if unit_zh != "包" else "單包"]
        if qty_m:
            parts.append(f"{qty_m.group(1)}{'包' if unit_m.group(1) == 'ボックス' else '張' if unit_m.group(1) == 'パック' else '盒'}入")
        if price_m:
            parts.append(f"售價 {price_m.group(1)} 日圓（含稅）")
        if len(parts) > 1:
            highlights.append("、".join(parts))

    count_m = re.search(r"カード種類数[：:]\s*([^<\n]+)", page_html)
    if count_m:
        text = _clean(count_m.group(1))
        text = text.replace("ノーマル", "一般").replace("パラレル", "平行卡")
        text = text.replace("以上", "以上").replace("（予定）", "（暫定）").replace("(予定)", "（暫定）")
        highlights.append(f"卡片種類：{text}")

    return highlights


def main():
    parser = argparse.ArgumentParser(description="幫商品類公告補規格重點")
    parser.add_argument("--in", dest="in_path", default="cards/ws_news_auto.json")
    args = parser.parse_args()

    data = json.load(open(args.in_path, encoding="utf-8"))
    items = data["items"]

    enriched = 0
    for item in items:
        if "/products/" not in item["url"]:
            item["highlights_zh"] = []
            item["detail_image_url"] = None
            continue
        try:
            page = fetch(item["url"])
        except Exception as exc:
            print(f"抓詳情失敗 {item['url']}：{exc}", file=sys.stderr)
            item["highlights_zh"] = []
            item["detail_image_url"] = None
            continue
        highlights = extract_highlights(page)
        item["highlights_zh"] = highlights
        item["detail_image_url"] = extract_detail_image(page)
        if highlights:
            enriched += 1
        time.sleep(0.4)  # 對官網客氣一點

    with open(args.in_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f"補到規格重點：{enriched}/{len(items)} 則 → {args.in_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
