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
| “調停者”メラクェラ | 7 張 | RZ/SE35-45 |
| 宇宙のバランス サノス | 8 張 | MAR/S89-070 |
| 羽型のあざ | 10 張 | VR/W22-074 |
| ゴブリン近衛隊 | 13 張 | OVL/S99-086 |
| ポンゴとパディータの子どもたち | 15 張 | Dds/S104-016 |
| “トリック・オア・トラブル”杉並 | 任意張數 | DC/W81-006 |
| “侵攻”巨人 | 任意張數 | AOT/S35-095 |
| “害虫の王”テラフォーマー | 任意張數 | TF/S32-T02 |
| “忌むべき存在”テラフォーマー | 任意張數 | TF/S32-084 |
| “捕食”巨人 | 任意張數 | AOT/S35-094, AOT/S50-095 |
| エクスカベータ | 任意張數 | ND/W67-088 |
| ゴブリン軍楽隊 | 任意張數 | OVL/S99-090 |
| ゴブリン重装甲歩兵団 | 任意張數 | OVL/S99-093 |
| セルポ星人 | 任意張數 | DDD/S118-086 |
| バジュラ（大） | 任意張數 | MF/S13-034 |
| バジュラ（小） | 任意張數 | MF/S13-040 |
| 亜人の軍勢 | 任意張數 | OVL/SE51-11 |
| 伊吹萃香 | 任意張數 | THP/S130-T16 |
| 分身体 狂三 | 任意張數 | DAL/W79-018 |
| 指先 | 任意張數 | RZ/S55-015 |
| 泥の英霊 | 任意張數 | PI/SE31-15 |
| 湖上の氷精 チルノ | 任意張數 | THP/S130-091 |
| 無限の〈ニベルコル〉 | 任意張數 | DAL/W131-088 |
| 見えざる手 | 任意張數 | RZ/S55-008 |
| 豚頭将軍 | 任意張數 | TSK/S70-022 |
| 豚頭族 | 任意張數 | TSK/S70-019 |
| 量産型イリス | 任意張數 | ND/W67-083 |
| 黒の兵士 | 任意張數 | CC/S48-039 |
| 黒水 | 任意張數 | RZ/SE35-46 |

## Combined Name Limits

These rules cap multiple card names together. They do not raise the default 4-card limit, but the deck validator should enforce them so alternate-name or paired cards are handled correctly.

| Names JP | Combined Limit | Source Cards |
|---|---:|---|
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
| “Astral Harmony”倉田ましろ / 平凡な私でも 倉田ましろ | 4 張 | BD/WE42-100 |
| “Astral Harmony”広町七深 / 普通じゃなくても 広町七深 | 4 張 | BD/WE42-016 |
| “Rausch und/and Craziness Ⅱ”湊友希那 / 青薔薇の歌姫 湊友希那 | 4 張 | BD/WE42-075 |
| “ふふん、任せて！”二葉つくし / 自信満々な努力家 二葉つくし | 4 張 | BD/WE42-079 |
| “キズナの音楽”花園たえ / ウサギ好き 花園たえ | 4 張 | BD/WE42-087 |
| “ナイトメア・オア・クイーン”狂三 / あの時のコースで 狂三 | 4 張 | DAL/W131-P01 |
| “パジャマパーティー”叶星 / 庭園の護り人 叶星 | 4 張 | ALL/S127-P06 |
| “ラグナロクブレイカー”はやて / 満身創痍 はやて | 4 張 | ND/W67-107 |
| “世界を彩る役者”瀬田薫 / 運命を共に 瀬田薫 | 4 張 | BD/WE42-008 |
| “受け止めたい思い”青葉モカ / 継続してきた演奏 青葉モカ | 4 張 | BD/WE42-052 |
| “真祖”シャルティア / ヴァンパイア・ブライド | 4 張 | OVL/SE54-48 |
| “短冊の行方”氷川日菜 / 不思議だから大好き 氷川日菜 | 4 張 | BD/WE42-038 |
| かつて見た星空 星乃一歌 / フロムトーキョー/流星のパルス | 4 張 | PJS/S109-116 |
| ちびひまり / 楽園へようこそ ひまり | 4 張 | DS/W81-P04 |
| わたしが一番！ 花海咲季 / 夏を満喫するわよ！ 花海咲季 | 4 張 | GIM/W124-P05 |
| アイノマテリアル/アイスドロップ / 仲間達からの祝福 花里みのり | 4 張 | PJS/S109-113 |
| イラつくあいつ / 水辺の休憩所 | 4 張 | BD/WE42-104 |
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
| 北の守護神 ビカラ / 祭夜の子神 ビカラ | 4 張 | GBF/S134-P02 |
| 心に秘めた葛藤 音夢 / 花より団子 音夢 | 4 張 | DC/W128-059 |
| 木琴占い / 選挙ポスター撮影 | 4 張 | DC/W128-096 |
| 覚醒アイテム～Princess～ / 超々∞MUGENDAI　春日未来 | 4 張 | IMS/SE55-76 |
