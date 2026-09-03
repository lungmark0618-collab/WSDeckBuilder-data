#!/usr/bin/env python3
"""把官網公告標題（日文）翻成中文，給首頁公告列表用。

官網公告標題幾乎都是幾種固定樣板組出來的（「XX公開」「XX掲載」
「XXルール更新」……），商品名稱本身（像「アズールレーン」「Vol.3」）
維持原文不翻——這些是官方沒有中文譯名的專有名詞，硬翻反而看不懂。

這裡刻意只認得認得出來的樣板，不是每一則都翻得出來：翻不出來的
標題回傳 None，App 端本來就會自動退回顯示日文原文（WSNewsItem.
displayTitle），不會壞掉，只是那一則沒有中文可看。比起硬翻出語意
可能有錯的句子，寧可讓翻不出來的維持原文。

用法（單獨測試）：
    python3 tools/translate_ws_news.py
"""
import re
from typing import Optional

# 商品名稱允許前後有全形或半形括號／空白，捕捉括號裡的原文（保留不翻）
_BRACKET = r"[\[［]\s*(.+?)\s*[\]］]"


def _build_patterns() -> list[tuple[re.Pattern, str]]:
    patterns: list[tuple[re.Pattern, str]] = []
    product_terms = ["ブースターパック", "トライアルデッキ", "プレミアムブースター"]
    combo = "トライアルデッキ＆ブースターパック"
    zh_of = {
        "ブースターパック": "補充包",
        "トライアルデッキ": "試打組",
        "プレミアムブースター": "特別補充包",
        combo: "試打組＆補充包",
    }
    for term in product_terms + [combo]:
        zh = zh_of[term]
        for action_jp, action_zh in (("公開", "公開"), ("掲載", "卡表刊載"), ("更新", "更新")):
            patterns.append((
                re.compile(rf"^{re.escape(term)}\s*{_BRACKET}\s*{action_jp}！?$"),
                f"{zh}［\\1］{action_zh}",
            ))
    # 燙金簽名卡：「ブースターパック [XXX] 箔押しサインカード公開！」跟
    # 「ブースターパック XXX 箔押しサインカード情報公開」（有無括號、有無「情報」
    # 都各自出現過），四種組合各自寫一條樣板，不共用同一個正規表達式，
    # 避免可有可無的括號群組跟後面的群組編號對不上而套錯欄位
    for has_bracket, name_pat in ((True, _BRACKET), (False, r"(.+?)")):
        for has_info, info_jp, info_zh in ((True, "情報", "資訊"), (False, "", "")):
            patterns.append((
                re.compile(rf"^ブースターパック\s*{name_pat}\s*箔押しサインカード{info_jp}公開！?$"),
                f"補充包［\\1］燙金簽名卡{info_zh}公開",
            ))
    return patterns


_PATTERNS = _build_patterns()

# 固定不變的整句公告，日文有好幾種寫法但意思一樣，統一對到同一句中文
_EXACT = {
    "デッキ構築ルールを更新": "牌組構築規則更新",
    "デッキ構築ルール更新": "牌組構築規則更新",
    "総合ルールを更新": "綜合規則更新",
    "総合ルール更新": "綜合規則更新",
    "エラッタ更新": "勘誤表更新",
}

# 句尾固定詞綴的樣板：抓「主體＋固定詞綴」，主體維持原文
_SUFFIX_PATTERNS: list[tuple[re.Pattern, str]] = [
    (re.compile(r"^(.+?)\s*出展情報\s*更新$"), "\\1 參展資訊更新"),
    (re.compile(r"^(.+?)\s*入賞者のデッキレシピを?掲載$"), "\\1 得獎者牌組配方刊載"),
    (re.compile(r"^(.+?)\s*おすすめデッキレシピを?掲載$"), "\\1 推薦牌組配方刊載"),
    (re.compile(r"^(.+?)\s*開催決定$"), "\\1 確定舉辦"),
    (re.compile(r"^【開催中】\s*(.+)$"), "【舉辦中】\\1"),
    (re.compile(r"^(.+?)特設ページ公開！?$"), "\\1特設頁面公開"),
]


def translate(title_jp: str) -> Optional[str]:
    title = title_jp.strip()
    if title in _EXACT:
        return _EXACT[title]
    for pattern, template in _PATTERNS:
        m = pattern.match(title)
        if m:
            zh = template
            for i, group in enumerate(m.groups(), start=1):
                zh = zh.replace(f"\\{i}", group or "")
            return zh
    for pattern, template in _SUFFIX_PATTERNS:
        m = pattern.match(title)
        if m:
            return template.replace("\\1", m.group(1))
    return None


if __name__ == "__main__":
    import json
    import os

    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "..", "ws_news.json")
    if os.path.exists(path):
        items = json.load(open(path, encoding="utf-8"))["items"]
        hit = 0
        for item in items:
            zh = translate(item["title_jp"])
            mark = "✓" if zh else "·"
            if zh:
                hit += 1
            print(f"{mark} {item['title_jp']}")
            if zh:
                print(f"    → {zh}")
        print(f"\n{hit}/{len(items)} 則翻得出來")
