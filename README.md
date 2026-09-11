# WSDeckBuilder 卡表資料

[WSDeckBuilder](https://github.com/lungmark0618-collab/WSDeckBuilder-ios) 這個 iOS App
的線上更新資料源。**這個 repo 只是我自己手機的資料來源，不是給人使用的專案。**

```
cards/             各作品卡表（App 逐部比對 data_version，只下載有變動的）
manifest.json      卡表版本目錄，由 CI 自動產生，不要手改
announcements.json 開發者通知（App 右上角鈴鐺），手動編輯，不用重新上架
tools/             產生與檢查 manifest 的腳本、加通知的小工具
```

## 著作權

- 卡片的**日文卡名與能力文字**著作權屬 **Bushiroad** 及各原作品權利方，
  資料取自[官方卡表](https://ws-tcg.com/cardlist/)
- 繁體中文譯文為個人翻譯，屬原文的衍生著作
- **卡圖不在此 repo 內**，JSON 只記錄官方圖片網址
- 非官方、非商業，與 Bushiroad 無任何關聯

此處內容僅供本人的個人工具使用，不授權任何再散布或商業利用。
若權利方認為不妥，請開 issue 或來信，我會立即移除。

## 首頁公告自動更新

`.github/workflows/news.yml` 每 6 小時抓取官方兩頁公告（UTC 00:17、06:17、12:17、18:17；台灣時間 08:17、14:17、20:17、02:17）。GitHub 排程可能延遲，亦可在 Actions 的「更新首頁公告」手動執行。

流程：抓公告 → 補商品規格／圖片 → 合併 `cards/ws_news_manual.json` → 驗證 → 有變更才發布 `ws_news.json`。手動資料優先，不會被自動抓取覆蓋。抓取失敗、官網標記改變或結果為空時，工作失敗並保留線上上一份資料；詳情暫時抓不到時沿用既有商品規格。

日常維護：在 Actions 查看紅色失敗紀錄；官網改版時調整 `tools/fetch_ws_news.py`／`tools/enrich_ws_news.py`，文字修正放在手動公告檔。修改手動公告會自動觸發發布。GitHub 失敗通知依帳號自己的通知設定；公開專案長期沒有活動時 GitHub 可能停用排程，需在 Actions 重新啟用。

App 開啟及返回前景會檢查公告，成功更新後 15 分鐘內不重複下載，失敗後自動請求至少相隔 1 分鐘；手動重新整理可立即重試。未連線會保留快取，商品與公告更新不需要重新發布 App。
