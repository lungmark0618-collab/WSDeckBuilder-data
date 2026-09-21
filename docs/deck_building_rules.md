# Deck Building Rules

Generated from official Japanese `text_jp` deck-construction clauses.

The app should keep the default same-card-name limit at 4, then apply these machine-readable overrides.

## Validator Usage

- Count deck cards by canonical Japanese card name, not by card ID or translated name.
- For `same_name_limit`, use `names_jp[0]` as the card-name group. If `limit_kind` is `unlimited`, do not report a same-name count violation for that name; otherwise compare the count with `limit`.
- For `combined_name_limit`, sum all cards whose Japanese names are in `names_jp`, then compare that total with `limit`.
- `source_cards` is provenance for review and debugging. It should not be used as the rule target because alternate printings can have different card IDs.

## Same Name Limits

| Name JP | Limit | Source Cards |
|---|---:|---|
| 黒い仔山羊 | 5 張 | OVL/S99-047 |
| 6人1組 S・P | 6 張 | JJ/S66-014 |
| 六魔将軍 | 6 張 | FT/SE10-29 |
| “調停者”メラクェラ | 7 張 | RZ/SE35-45 |
| 宇宙のバランス サノス | 8 張 | MAR/S89-070 |
| 無限の食欲 | 8 張 | KMD/W96-097 |
| 羽型のあざ | 10 張 | VR/W22-074 |
| ゴブリン近衛隊 | 13 張 | OVL/S99-086 |
| マックス・レボ・バンド | 13 張 | SW/S49-045, SW/S49-045a_, SW/S49-045b_, SW/S49-045c_ |
| ポンゴとパディータの子どもたち | 15 張 | Dds/S104-016 |
| “トリック・オア・トラブル”杉並 | 任意張數 | DC/W81-006 |
| “侵攻”巨人 | 任意張數 | AOT/S35-095 |
| “多勢の兵”ストームトルーパー | 任意張數 | SW/S49-071, SW/S49-071_ |
| “害虫の王”テラフォーマー | 任意張數 | TF/S32-T02 |
| “忌むべき存在”テラフォーマー | 任意張數 | TF/S32-084 |
| “捕食”巨人 | 任意張數 | AOT/S35-094, AOT/S50-095 |
| “新たなる先兵”ストームトルーパー | 任意張數 | SW/S49-075 |
| “脱皮” トール | 任意張數 | KMD/W96-046 |
| “街を歩けば”アクシズ教徒 | 任意張數 | KS/W55-089, KS/W75-086 |
| きゅうと鳴くキュゥべえ | 任意張數 | MM/W35-091 |
| アルカ・ノイズ | 任意張數 | SG/W39-041 |
| エクスカベータ | 任意張數 | ND/W67-088 |
| ガモーリアン | 任意張數 | SW/S49-042, SW/S49-042_ |
| キャベツ | 任意張數 | KS/W49-057 |
| ゴブリン軍楽隊 | 任意張數 | OVL/S99-090 |
| ゴブリン重装甲歩兵団 | 任意張數 | OVL/S99-093 |
| スカウト・トルーパー | 任意張數 | SW/S49-076, SW/S49-076_, SW/S49-076S_ |
| セルポ星人 | 任意張數 | DDD/S118-086 |
| ノイズ | 任意張數 | SG/W27-043, SG/W52-041, SG/W72-041 |
| ノイズ（第4話） | 任意張數 | SG/W19-038 |
| バジュラ（大） | 任意張數 | MF/S13-034 |
| バジュラ（小） | 任意張數 | MF/S13-040 |
| ファースト・オーダー ストームトルーパー | 任意張數 | SW/S49-072, SW/S49-072_ |
| ボレアス家の獣人メイド | 任意張數 | MTI/S83-067 |
| マシンガンたのしーなー！ ZEMAL | 任意張數 | GGO/S59-088 |
| メロディア | 任意張數 | MK/S33-013 |
| 三式潜航輸送艇 まるゆ | 任意張數 | KC/S25-166 |
| 三式潜航輸送艇 まるゆ改 | 任意張數 | KC/S31-020 |
| 亜人の軍勢 | 任意張數 | OVL/SE51-11 |
| 伊吹萃香 | 任意張數 | THP/S130-T16 |
| 分身体 狂三 | 任意張數 | DAL/W79-018 |
| 影分身 サリー | 任意張數 | BFR/S78-046 |
| 指先 | 任意張數 | RZ/S55-015 |
| 泥の英霊 | 任意張數 | PI/SE31-15 |
| 湖上の氷精 チルノ | 任意張數 | THP/S130-091 |
| 無限の〈ニベルコル〉 | 任意張數 | DAL/W131-088, Fdl/W120-140 |
| 空からの襲撃 アルカ・ノイズ | 任意張數 | SG/W89-049 |
| 見えざる手 | 任意張數 | RZ/S55-008 |
| 豚頭将軍 | 任意張數 | TSK/S70-022 |
| 豚頭族 | 任意張數 | TSK/S70-019 |
| 赤銅の群 暗黒騎士 | 任意張數 | SAO/S80-066 |
| 連携するトリオン兵 アイドラ | 任意張數 | WTR/S85-039 |
| 量産型イリス | 任意張數 | ND/W67-083 |
| 駆逐イ級 | 任意張數 | KC/SE28-17 |
| 黒の兵士 | 任意張數 | CC/S48-039 |
| 黒水 | 任意張數 | RZ/SE35-46 |
| 黒羽根 | 任意張數 | MR/W80-068 |

## Combined Name Limits

These rules cap multiple card names together. They do not raise the default 4-card limit, but the deck validator should enforce them so alternate-name or paired cards are handled correctly.

| Names JP | Combined Limit | Source Cards |
|---|---:|---|
| -The LIVE エーデル- 鳳 ミチル / 煌めく水槽、輝く瞳 | 4 張 | RSL/SE38-26 |
| -The LIVE エーデル- 鶴姫 やちよ / “大地の神”鶴姫 やちよ | 4 張 | RSL/SE38-12 |
| Beat Eater/Awake Now / えむ流？ダンスの極意！ 小豆沢こはね | 4 張 | PJS/S109-114 |
| Change the world！ / 世界を変える音 | 4 張 | BD/WE42-105 |
| Keep→it up♡ 市川雛菜 / クリアマリンカーム 市川雛菜 | 4 張 | ISC/SE53-52 |
| M@STERS OF IDOL WORLD!!2015 / ザ☆ワイルドストロベリー　萩原雪歩 | 4 張 | IM/SE52-70 |
| ONE FOR ALL あずさ / ステージへの決意 あずさ | 4 張 | IM/SE27-005 |
| ONE FOR ALL やよい / みんなのアイドルやよい | 4 張 | IM/SE27-008 |
| ONE FOR ALL 亜美 / 輝きの向こう側へ！ 亜美 | 4 張 | IM/SE27-004 |
| ONE FOR ALL 伊織 / “今を大切に”伊織 | 4 張 | IM/SE27-006 |
| ONE FOR ALL 千早 / クールでストイック千早 | 4 張 | IM/SE27-012 |
| ONE FOR ALL 小鳥 / 朝礼 小鳥 | 4 張 | IM/SE27-001 |
| ONE FOR ALL 律子 / 頭脳明晰 律子 | 4 張 | IM/SE27-011 |
| ONE FOR ALL 春香 / 天海 春香 | 4 張 | IM/SE27-007 |
| ONE FOR ALL 真 / スーパーレディ 真 | 4 張 | IM/SE27-014 |
| ONE FOR ALL 真美 / 輝きの向こう側へ！ 真美 | 4 張 | IM/SE27-003 |
| ONE FOR ALL 美希 / “今を大切に”美希 | 4 張 | IM/SE27-010 |
| ONE FOR ALL 貴音 / “今を大切に”貴音 | 4 張 | IM/SE27-013 |
| ONE FOR ALL 雪歩 / 先輩として雪歩 | 4 張 | IM/SE27-002 |
| ONE FOR ALL 響 / “今を大切に”響 | 4 張 | IM/SE27-009 |
| SD アリス / 光彩陸離 アリス | 4 張 | SAO/S100-P02 |
| “Angelic Angel”東條 希 / “花の女神”東條 希 | 4 張 | LL/WE39-017 |
| “Astral Harmony”倉田ましろ / 平凡な私でも 倉田ましろ | 4 張 | BD/WE42-100 |
| “Astral Harmony”広町七深 / 普通じゃなくても 広町七深 | 4 張 | BD/WE42-016 |
| “Rausch und/and Craziness Ⅱ”湊友希那 / 青薔薇の歌姫 湊友希那 | 4 張 | BD/WE42-075 |
| “あなたのことだけ”高坂 穂乃果 / “いまが最高！”高坂 穂乃果 | 4 張 | LL/W68-041 |
| “いまが最高！”南 ことり / “獣使い☆ことり”南 ことり | 4 張 | LL/W68-040 |
| “いまが最高！”園田 海未 / “衣装のおかげです”園田 海未 | 4 張 | LL/W68-039 |
| “ふふん、任せて！”二葉つくし / 自信満々な努力家 二葉つくし | 4 張 | BD/WE42-079 |
| “キズナの音楽”花園たえ / ウサギ好き 花園たえ | 4 張 | BD/WE42-087 |
| “ナイトメア・オア・クイーン”狂三 / あの時のコースで 狂三 | 4 張 | DAL/W131-P01 |
| “パジャマパーティー”叶星 / 庭園の護り人 叶星 | 4 張 | ALL/S127-P06 |
| “ブレイクタイム” リゼ＆ココア / 私らしさ リゼ | 4 張 | GU/W88-P15 |
| “ラグナロクブレイカー”はやて / 満身創痍 はやて | 4 張 | ND/W67-107 |
| “世界を彩る役者”瀬田薫 / 運命を共に 瀬田薫 | 4 張 | BD/WE42-008 |
| “受け止めたい思い”青葉モカ / 継続してきた演奏 青葉モカ | 4 張 | BD/WE42-052 |
| “夏祭りデート”西木野 真姫 / 紅の魅力 西木野 真姫 | 4 張 | LL/WE39-048 |
| “真祖”シャルティア / ヴァンパイア・ブライド | 4 張 | OVL/SE54-48 |
| “短冊の行方”氷川日菜 / 不思議だから大好き 氷川日菜 | 4 張 | BD/WE42-038 |
| 【秘伝・未来焼き】響＆未来 / お昼寝の準備 響＆未来 | 4 張 | SG/W72-103 |
| かつて見た星空 星乃一歌 / フロムトーキョー/流星のパルス | 4 張 | PJS/S109-116 |
| ちびひまり / 楽園へようこそ ひまり | 4 張 | DS/W81-P04 |
| わたしが一番！ 花海咲季 / 夏を満喫するわよ！ 花海咲季 | 4 張 | GIM/W124-P05 |
| アイノマテリアル/アイスドロップ / 仲間達からの祝福 花里みのり | 4 張 | PJS/S109-113 |
| イラつくあいつ / 水辺の休憩所 | 4 張 | BD/WE42-104 |
| オーバードライブ！三森すずこ / 浴衣ドレス シャロ | 4 張 | MK/S33-103 |
| オーバードライブ！佐々木未来 / 浴衣ドレス エリー | 4 張 | MK/S33-102 |
| オーバードライブ！徳井青空 / 浴衣ドレス ネロ | 4 張 | MK/S33-101 |
| オーバードライブ！橘田いずみ / 浴衣ドレス コーデリア | 4 張 | MK/S33-104 |
| オーバー・マイセルフ 渋谷 凛 / 渋谷 凛 | 4 張 | IMC/W115-P02, IMC/W115-T30 |
| カナデトモスソラ/再生 / 音楽が見せてくれる世界 宵崎奏 | 4 張 | PJS/S109-115 |
| ザ☆ワイルドストロベリー　三浦あずさ / 輝きの向こう側へ！ あずさ | 4 張 | IM/SE52-73 |
| ザ☆ワイルドストロベリー　星井美希 / 輝きの向こう側へ！ 美希 | 4 張 | IM/SE52-64 |
| ステージ裏での激励 天馬司 / トンデモワンダーズ/Glory Steady Go! | 4 張 | PJS/S109-112 |
| スパークドリンク / 超々∞MUGENDAI　エミリー | 4 張 | IMS/SE55-75 |
| トロピカルガール たきな / ファーストリコリス フキ | 4 張 | LRC/WE47-37 |
| ハッピーハロウィン♪ 有咲 / 素直な笑顔 市ヶ谷有咲 | 4 張 | BD/WE42-082 |
| フラスタ / 超々∞MUGENDAI　伊吹 翼 | 4 張 | IMS/SE55-71 |
| ホラー大好き 小梅 / ホワイトスノードール 白坂小梅 | 4 張 | IMC/W115-T31 |
| メイクミー・キスユー 赤城みりあ / 赤城 みりあ | 4 張 | IMC/W115-T51 |
| リバーシブル・トースト 田中摩美々 / 紺碧のボーダーライン 白瀬咲耶 | 4 張 | ISC/SE53-61 |
| 一切衆生慈恵嘱目装 ガレヲン / 六竜の『金』 ガレヲン | 4 張 | GBF/S134-P03 |
| 冬のひととき 暁 / 暁型駆逐艦1番艦 暁改 | 4 張 | KC/S42-106, KC/S67-T03 |
| 北の守護神 ビカラ / 祭夜の子神 ビカラ | 4 張 | GBF/S134-P02 |
| 大人な彼女 英梨々 / 懐かしい記憶 英梨々 | 4 張 | SHS/W98-P02 |
| 宝瓶宮のアクエリアス / 永遠に褪せない笑顔 ルーシィ | 4 張 | FT/S120-031 |
| 封印された拳 アクション仮面 / 正義の仮面 アクション仮面 | 4 張 | CS/S114-030 |
| 心に秘めた葛藤 音夢 / 花より団子 音夢 | 4 張 | DC/W128-059 |
| 木琴占い / 選挙ポスター撮影 | 4 張 | DC/W128-096 |
| 覚醒アイテム～Princess～ / 超々∞MUGENDAI　春日未来 | 4 張 | IMS/SE55-76 |
