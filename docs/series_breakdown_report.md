# 系列分彈資料報告

這份報告提供程式端做「同系列不同彈分開分類」的資料依據。翻譯資料本身不用改 UI，也不用翻譯《》特徵名。

## 建議規則

- 以每張卡的 `id` 或 `printings[].id` 解析彈別。
- product code 取卡號最後一個 `-` 前面的部分，例如 `SFN/S108-001` → `SFN/S108`。
- 同一張卡有多刷版時，仍以唯一卡 `id` 計一次；若要顯示刷版數，另看 `printing_count`。
- 若一個作品只有 1 個 product code，可以維持原本作品分類；若有 2 個以上，就可以在作品底下拆子分類。
- 預設顯示名建議先用 `作品名（product code）`。像「第一彈／第二彈」這種友善名稱，建議另外做人工 mapping 對照官方商品名，避免用卡號排序誤判。

## 交付檔案

- `docs/series_breakdown.json`：程式可直接讀的完整 mapping。
- `docs/series_breakdown_report.md`：人工檢查用摘要。

## 多彈作品摘要

目前資料庫共 48 部作品，其中 27 部作品含 2 個以上 product code。

### lss｜Love Live! Sunshine!!（7 個 product code，537 張唯一卡）
- `LSS/W45`：140 張唯一卡／177 刷版，預設顯示 `Love Live! Sunshine!!（LSS/W45）`；例：LSS/W45-P01, LSS/W45-P02, LSS/W45-P03
- `LSS/W53`：131 張唯一卡／181 刷版，預設顯示 `Love Live! Sunshine!!（LSS/W53）`；例：LSS/W53-P01, LSS/W53-P02, LSS/W53-P03
- `LSS/W69`：114 張唯一卡／214 刷版，預設顯示 `Love Live! Sunshine!!（LSS/W69）`；例：LSS/W69-P04, LSS/W69-P05, LSS/W69-001
- `LSS/WE27`：88 張唯一卡／97 刷版，預設顯示 `Love Live! Sunshine!!（LSS/WE27）`；例：LSS/WE27-P01, LSS/WE27-P02, LSS/WE27-P03
- `LSS/WE38`：10 張唯一卡／28 刷版，預設顯示 `Love Live! Sunshine!!（LSS/WE38）`；例：LSS/WE38-P02, LSS/WE38-002, LSS/WE38-005
- `LSS/WE39`：19 張唯一卡／55 刷版，預設顯示 `Love Live! Sunshine!!（LSS/WE39）`；例：LSS/WE39-P03, LSS/WE39-004, LSS/WE39-005
- `SIS/W109`：35 張唯一卡／69 刷版，預設顯示 `Love Live! Sunshine!!（SIS/W109）`；例：SIS/W109-140, SIS/W109-P01, SIS/W109-P03

### bdgbp｜BanG Dream! 少女樂團派對（5 個 product code，783 張唯一卡）
- `BD/W54`：234 張唯一卡／430 刷版，預設顯示 `BanG Dream! 少女樂團派對（BD/W54）`；例：BD/W54-P01, BD/W54-P02, BD/W54-P03
- `BD/W63`：127 張唯一卡／280 刷版，預設顯示 `BanG Dream! 少女樂團派對（BD/W63）`；例：BD/W63-P01, BD/W63-P02, BD/W63-P03
- `BD/W73`：144 張唯一卡／357 刷版，預設顯示 `BanG Dream! 少女樂團派對（BD/W73）`；例：BD/W73-P01, BD/W73-P02, BD/W73-P03
- `BD/W95`：208 張唯一卡／351 刷版，預設顯示 `BanG Dream! 少女樂團派對（BD/W95）`；例：BD/W95-P01, BD/W95-P02, BD/W95-P03
- `BD/WE34`：70 張唯一卡／97 刷版，預設顯示 `BanG Dream! 少女樂團派對（BD/WE34）`；例：BD/WE34-T01, BD/WE34-T02, BD/WE34-T03

### hol｜hololive（5 個 product code，631 張唯一卡）
- `HOL/W91`：310 張唯一卡／614 刷版，預設顯示 `hololive（HOL/W91）`；例：HOL/W91-P02, HOL/W91-P03, HOL/W91-P04
- `HOL/W104`：166 張唯一卡／417 刷版，預設顯示 `hololive（HOL/W104）`；例：HOL/W104-P01, HOL/W104-P02, HOL/W104-P03
- `HOL/WE36`：54 張唯一卡／160 刷版，預設顯示 `hololive（HOL/WE36）`；例：HOL/WE36-P01, HOL/WE36-01, HOL/WE36-02
- `HOL/WE44`：67 張唯一卡／173 刷版，預設顯示 `hololive（HOL/WE44）`；例：HOL/WE44-P01, HOL/WE44-P02, HOL/WE44-P03
- `HOL/WE45`：34 張唯一卡／34 刷版，預設顯示 `hololive（HOL/WE45）`；例：HOL/WE45-P01, HOL/WE45-P02, HOL/WE45-P03

### ovl｜OVERLORD（4 個 product code，385 張唯一卡）
- `OVL/S62`：128 張唯一卡／172 刷版，預設顯示 `OVERLORD（OVL/S62）`；例：OVL/S62-P01, OVL/S62-P02, OVL/S62-T01
- `OVL/S99`：109 張唯一卡／152 刷版，預設顯示 `OVERLORD（OVL/S99）`；例：OVL/S99-P01, OVL/S99-P02, OVL/S99-001
- `OVL/SE51`：63 張唯一卡／141 刷版，預設顯示 `OVERLORD（OVL/SE51）`；例：OVL/SE51-P01, OVL/SE51-P02, OVL/SE51-01
- `OVL/SE54`：85 張唯一卡／160 刷版，預設顯示 `OVERLORD（OVL/SE54）`；例：OVL/SE54-P01, OVL/SE54-P02, OVL/SE54-P03

### pjs｜世界計畫 繽紛舞台！（4 個 product code，516 張唯一卡）
- `PJS/S91`：252 張唯一卡／398 刷版，預設顯示 `世界計畫 繽紛舞台！（PJS/S91）`；例：PJS/S91-P01, PJS/S91-P02, PJS/S91-P03
- `PJS/S109`：117 張唯一卡／213 刷版，預設顯示 `世界計畫 繽紛舞台！（PJS/S109）`；例：PJS/S109-112, PJS/S109-113, PJS/S109-114
- `PJS/S125`：121 張唯一卡／271 刷版，預設顯示 `世界計畫 繽紛舞台！（PJS/S125）`；例：PJS/S125-P01, PJS/S125-P02, PJS/S125-P03
- `PJS/SE49`：26 張唯一卡／26 刷版，預設顯示 `世界計畫 繽紛舞台！（PJS/SE49）`；例：PJS/SE49-001, PJS/SE49-002, PJS/SE49-003

### osk｜【我推的孩子】（3 個 product code，363 張唯一卡）
- `OSK/S107`：137 張唯一卡／263 刷版，預設顯示 `【我推的孩子】（OSK/S107）`；例：OSK/S107-P01, OSK/S107-P02, OSK/S107-P03
- `OSK/S121`：104 張唯一卡／226 刷版，預設顯示 `【我推的孩子】（OSK/S121）`；例：OSK/S121-P01, OSK/S121-P02, OSK/S121-P03
- `OSK/S133`：122 張唯一卡／253 刷版，預設顯示 `【我推的孩子】（OSK/S133）`；例：OSK/S133-101, OSK/S133-102, OSK/S133-103

### sfn｜葬送的芙莉蓮（3 個 product code，348 張唯一卡）
- `SFN/S108`：136 張唯一卡／273 刷版，預設顯示 `葬送的芙莉蓮（SFN/S108）`；例：SFN/S108-P02, SFN/S108-P01, SFN/S108-P03
- `SFN/S128`：111 張唯一卡／238 刷版，預設顯示 `葬送的芙莉蓮（SFN/S128）`；例：SFN/S128-001, SFN/S128-002, SFN/S128-003
- `SFN/S136`：101 張唯一卡／252 刷版，預設顯示 `葬送的芙莉蓮（SFN/S136）`；例：SFN/S136-P01, SFN/S136-001, SFN/S136-002

### tsk｜關於我轉生變成史萊姆這檔事（3 個 product code，352 張唯一卡）
- `TSK/S70`：128 張唯一卡／165 刷版，預設顯示 `關於我轉生變成史萊姆這檔事（TSK/S70）`；例：TSK/S70-P01, TSK/S70-P02, TSK/S70-P03
- `TSK/S82`：109 張唯一卡／137 刷版，預設顯示 `關於我轉生變成史萊姆這檔事（TSK/S82）`；例：TSK/S82-P01, TSK/S82-001, TSK/S82-002
- `TSK/S101`：115 張唯一卡／174 刷版，預設顯示 `關於我轉生變成史萊姆這檔事（TSK/S101）`；例：TSK/S101-P02, TSK/S101-P03, TSK/S101-P04

### uma｜賽馬娘（3 個 product code，410 張唯一卡）
- `UMA/W106`：195 張唯一卡／405 刷版，預設顯示 `賽馬娘（UMA/W106）`；例：UMA/W106-036, UMA/W106-037, UMA/W106-038
- `UMA/W119`：102 張唯一卡／203 刷版，預設顯示 `賽馬娘（UMA/W119）`；例：UMA/W119-P01, UMA/W119-P02, UMA/W119-001
- `UMA/W134`：113 張唯一卡／229 刷版，預設顯示 `賽馬娘（UMA/W134）`；例：UMA/W134-P01, UMA/W134-P02, UMA/W134-P03

### aot｜進擊的巨人（2 個 product code，247 張唯一卡）
- `AOT/S35`：138 張唯一卡／169 刷版，預設顯示 `進擊的巨人（AOT/S35）`；例：AOT/S35-P01, AOT/S35-P02, AOT/S35-P03
- `AOT/S50`：109 張唯一卡／155 刷版，預設顯示 `進擊的巨人（AOT/S50）`；例：AOT/S50-P01, AOT/S50-P02, AOT/S50-P03

### azl｜碧藍航線（2 個 product code，375 張唯一卡）
- `AZL/S102`：241 張唯一卡／467 刷版，預設顯示 `碧藍航線（AZL/S102）`；例：AZL/S102-P01, AZL/S102-P02, AZL/S102-P03
- `AZL/S119`：134 張唯一卡／316 刷版，預設顯示 `碧藍航線（AZL/S119）`；例：AZL/S119-P01, AZL/S119-P02, AZL/S119-P03

### cgs｜卡片遊戲什麼子（2 個 product code，68 張唯一卡）
- `CGS/WS01`：59 張唯一卡／82 刷版，預設顯示 `卡片遊戲什麼子（CGS/WS01）`；例：CGS/WS01-P01, CGS/WS01-P02, CGS/WS01-P03
- `SI/WPR`：9 張唯一卡／9 刷版，預設顯示 `卡片遊戲什麼子（SI/WPR）`；例：SI/WPR-001, SI/WPR-002, SI/WPR-003

### ddm｜在地下城尋求邂逅是否搞錯了什麼（2 個 product code，158 張唯一卡）
- `DDM/S88`：125 張唯一卡／168 刷版，預設顯示 `在地下城尋求邂逅是否搞錯了什麼（DDM/S88）`；例：DDM/S88-P01, DDM/S88-P02, DDM/S88-T01
- `GA10/S131`：33 張唯一卡／69 刷版，預設顯示 `在地下城尋求邂逅是否搞錯了什麼（GA10/S131）`；例：GA10/S131-P01, GA10/S131-002, GA10/S131-004

### dds｜Disney100（2 個 product code，115 張唯一卡）
- `Dds/S104`：112 張唯一卡／200 刷版，預設顯示 `Disney100（Dds/S104）`；例：Dds/S104-102, Dds/S104-103, Dds/S104-104
- `Dmv/S104`：3 張唯一卡／6 刷版，預設顯示 `Disney100（Dmv/S104）`；例：Dmv/S104-053, Dmv/S104-058, Dmv/S104-074

### gbs｜哥布林殺手（2 個 product code，136 張唯一卡）
- `GA04/S131`：7 張唯一卡／15 刷版，預設顯示 `哥布林殺手（GA04/S131）`；例：GA04/S131-005, GA04/S131-079, GA04/S131-084
- `GBS/S63`：129 張唯一卡／163 刷版，預設顯示 `哥布林殺手（GBS/S63）`；例：GBS/S63-P01, GBS/S63-P02, GBS/S63-P03

### hll｜雛邏輯 ～from Luck ＆ Logic～（2 個 product code，109 張唯一卡）
- `HLL/WE28`：58 張唯一卡／68 刷版，預設顯示 `雛邏輯 ～from Luck ＆ Logic～（HLL/WE28）`；例：HLL/WE28-51, HLL/WE28-P01, HLL/WE28-P02
- `HLL/WE29`：51 張唯一卡／63 刷版，預設顯示 `雛邏輯 ～from Luck ＆ Logic～（HLL/WE29）`；例：HLL/WE29-P01, HLL/WE29-01, HLL/WE29-02

### kgl｜輝夜姬想讓人告白（2 個 product code，238 張唯一卡）
- `KGL/S79`：125 張唯一卡／171 刷版，預設顯示 `輝夜姬想讓人告白（KGL/S79）`；例：KGL/S79-P01, KGL/S79-P02, KGL/S79-T01
- `KGL/S95`：113 張唯一卡／172 刷版，預設顯示 `輝夜姬想讓人告白（KGL/S95）`；例：KGL/S95-P01, KGL/S95-P02, KGL/S95-P03

### lh｜記錄的地平線（2 個 product code，84 張唯一卡）
- `LH/SE20`：75 張唯一卡／78 刷版，預設顯示 `記錄的地平線（LH/SE20）`；例：LH/SE20-P01, LH/SE20-P02, LH/SE20-P03
- `LH/SP02`：9 張唯一卡／17 刷版，預設顯示 `記錄的地平線（LH/SP02）`；例：LH/SP02-09, LH/SP02-01, LH/SP02-02

### lrc｜莉可麗絲（2 個 product code，191 張唯一卡）
- `LRC/W105`：136 張唯一卡／208 刷版，預設顯示 `莉可麗絲（LRC/W105）`；例：LRC/W105-101, LRC/W105-102, LRC/W105-103
- `LRC/WE47`：55 張唯一卡／118 刷版，預設顯示 `莉可麗絲（LRC/WE47）`；例：LRC/WE47-P01, LRC/WE47-01, LRC/WE47-02

### mb｜MELTY BLOOD／空之境界（2 個 product code，131 張唯一卡）
- `KK/SPR`：7 張唯一卡／7 刷版，預設顯示 `MELTY BLOOD／空之境界（KK/SPR）`；例：KK/SPR-001, KK/SPR-002, KK/SPR-003
- `MB/S10`：124 張唯一卡／140 刷版，預設顯示 `MELTY BLOOD／空之境界（MB/S10）`；例：MB/S10-106, MB/S10-107, MB/S10-108

### mf｜超時空要塞系列（2 個 product code，195 張唯一卡）
- `MDE/SE45`：64 張唯一卡／155 刷版，預設顯示 `超時空要塞系列（MDE/SE45）`；例：MDE/SE45-P01, MDE/SE45-P02, MDE/SE45-P03
- `MF/S13`：131 張唯一卡／148 刷版，預設顯示 `超時空要塞系列（MF/S13）`；例：MF/S13-106, MF/S13-107, MF/S13-108

### mygo｜MyGO!!!!!（2 個 product code，427 張唯一卡）
- `BD/W125`：178 張唯一卡／352 刷版，預設顯示 `MyGO!!!!!（BD/W125）`；例：BD/W125-P01, BD/W125-P02, BD/W125-P03
- `BD/WE42`：249 張唯一卡／409 刷版，預設顯示 `MyGO!!!!!（BD/WE42）`；例：BD/WE42-P01, BD/WE42-P02, BD/WE42-P03

### nk｜偽戀（2 個 product code，177 張唯一卡）
- `NK/W30`：139 張唯一卡／156 刷版，預設顯示 `偽戀（NK/W30）`；例：NK/W30-101, NK/W30-102, NK/W30-103
- `NK/WE22`：38 張唯一卡／41 刷版，預設顯示 `偽戀（NK/WE22）`；例：NK/WE22-P01, NK/WE22-P02, NK/WE22-01

### snk｜角川Sneaker文庫（2 個 product code，15 張唯一卡）
- `Snk/W62`：14 張唯一卡／21 刷版，預設顯示 `角川Sneaker文庫（Snk/W62）`；例：Snk/W62-003, Snk/W62-T11, Snk/W62-T17
- `Snk/W123`：1 張唯一卡／2 刷版，預設顯示 `角川Sneaker文庫（Snk/W123）`；例：Snk/W123-015

### sst｜新妹魔王的契約者（2 個 product code，19 張唯一卡）
- `Sst/W62`：14 張唯一卡／22 刷版，預設顯示 `新妹魔王的契約者（Sst/W62）`；例：Sst/W62-051, Sst/W62-T01, Sst/W62-T06
- `Sst/W123`：5 張唯一卡／13 刷版，預設顯示 `新妹魔王的契約者（Sst/W123）`；例：Sst/W123-067, Sst/W123-072, Sst/W123-079

### ssy｜涼宮春日的憂鬱（2 個 product code，39 張唯一卡）
- `Ssy/W62`：19 張唯一卡／31 刷版，預設顯示 `涼宮春日的憂鬱（Ssy/W62）`；例：Ssy/W62-050, Ssy/W62-P01, Ssy/W62-T08
- `Ssy/W123`：20 張唯一卡／47 刷版，預設顯示 `涼宮春日的憂鬱（Ssy/W123）`；例：Ssy/W123-P03, Ssy/W123-P04, Ssy/W123-T03

### va｜Visual Arts（2 個 product code，39 張唯一卡）
- `VA/WE30`：1 張唯一卡／1 刷版，預設顯示 `Visual Arts（VA/WE30）`；例：VA/WE30-55
- `VA/WPR`：38 張唯一卡／38 刷版，預設顯示 `Visual Arts（VA/WPR）`；例：VA/WPR-P01, VA/WPR-P02, VA/WPR-P03

## 全作品彈別數

| key | 作品 | product code 數 | 唯一卡 | 刷版 |
| --- | --- | ---: | ---: | ---: |
| `amg` | 甘神家的連理枝 | 1 | 121 | 264 |
| `aot` | 進擊的巨人 | 2 | 247 | 324 |
| `azl` | 碧藍航線 | 2 | 375 | 783 |
| `bdgbp` | BanG Dream! 少女樂團派對 | 5 | 783 | 1515 |
| `bm` | 物語系列 | 1 | 127 | 144 |
| `brd` | 棕色塵埃2 | 1 | 140 | 304 |
| `btr` | 孤獨搖滾！ | 1 | 126 | 252 |
| `cc` | 鎖鏈戰記 ～赫克瑟塔斯之光～ | 1 | 129 | 164 |
| `cgs` | 卡片遊戲什麼子 | 2 | 68 | 91 |
| `cn` | CANAAN | 1 | 28 | 28 |
| `csm` | 鏈鋸人 | 1 | 127 | 198 |
| `dbg` | 成為神的那一天 | 1 | 127 | 167 |
| `ddm` | 在地下城尋求邂逅是否搞錯了什麼 | 2 | 158 | 237 |
| `dds` | Disney100 | 2 | 115 | 206 |
| `ev` | 福音戰士新劇場版 | 1 | 124 | 140 |
| `fh` | Fate/hollow ataraxia | 1 | 51 | 96 |
| `gbs` | 哥布林殺手 | 2 | 136 | 178 |
| `gim` | 學園偶像大師 | 1 | 138 | 335 |
| `gst` | 超爆裂異次元紙牌戰鬥 Gigant Shooter 司 | 1 | 33 | 37 |
| `gt` | 穿透幻影的太陽 | 1 | 129 | 148 |
| `hll` | 雛邏輯 ～from Luck ＆ Logic～ | 2 | 109 | 131 |
| `hol` | hololive | 5 | 631 | 1398 |
| `kgl` | 輝夜姬想讓人告白 | 2 | 238 | 343 |
| `lh` | 記錄的地平線 | 2 | 84 | 95 |
| `lrc` | 莉可麗絲 | 2 | 191 | 326 |
| `lss` | Love Live! Sunshine!! | 7 | 537 | 821 |
| `mb` | MELTY BLOOD／空之境界 | 2 | 131 | 147 |
| `mf` | 超時空要塞系列 | 2 | 195 | 303 |
| `mygo` | MyGO!!!!! | 2 | 427 | 761 |
| `nik` | 勝利女神：妮姬 | 1 | 151 | 355 |
| `nk` | 偽戀 | 2 | 177 | 197 |
| `ns` | 魔法少女奈葉StrikerS | 1 | 129 | 145 |
| `osk` | 【我推的孩子】 | 3 | 363 | 742 |
| `ovl` | OVERLORD | 4 | 385 | 625 |
| `pjs` | 世界計畫 繽紛舞台！ | 4 | 516 | 908 |
| `pt` | Phantom -Requiem for the Phantom- | 1 | 131 | 146 |
| `sfn` | 葬送的芙莉蓮 | 3 | 348 | 763 |
| `snk` | 角川Sneaker文庫 | 2 | 15 | 23 |
| `spy` | 間諜家家酒 | 1 | 129 | 205 |
| `sst` | 新妹魔王的契約者 | 2 | 19 | 35 |
| `ssy` | 涼宮春日的憂鬱 | 2 | 39 | 78 |
| `tf` | 火星異種 | 1 | 125 | 149 |
| `trv` | 東京復仇者 | 1 | 128 | 193 |
| `tsk` | 關於我轉生變成史萊姆這檔事 | 3 | 352 | 476 |
| `uma` | 賽馬娘 | 3 | 410 | 837 |
| `va` | Visual Arts | 2 | 39 | 39 |
| `vr` | Vividred Operation | 1 | 131 | 149 |
| `woo` | 兔寶的悲慘日常 | 1 | 24 | 24 |
