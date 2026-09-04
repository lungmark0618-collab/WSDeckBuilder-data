# Translation Quality Audit

## Scope

- Checked all 78 card data files currently in `cards/`.
- Checked 19,762 cards total.
- Used `Weiß Schwarz 裁判級綜合規則與賽事判例手冊.pdf` as the rules-reading reference.
- Kept the current project policy that trait names in `《》` and card names in `「」` remain Japanese for physical-card lookup.

## Terminology Baseline

The card database currently enforces these terms:

| Japanese / Concept | Current Project Term |
|---|---|
| 山札 / Deck zone | 牌組 |
| 控え室 / Waiting Room | 休息室 |
| クロック / Clock | 傷害區 |
| ストック / Stock | 能量區 |
| 思い出 / Memory | 回憶區 |
| レベル置場 / Level zone | 等級區 |
| レスト / Rest | 橫置 |
| スタンド / Stand | 正置 |
| リバース / Reverse | 倒置 |
| ダメージキャンセル | 傷害取消 |

The judge manual often writes the deck zone as `牌庫 Deck`, while this repo currently validates `牌組` and forbids `牌庫`. I did not change this globally because it is a project-level glossary decision, not a one-card typo. If we want to align more closely with the manual later, the validator and glossary should be changed first, then all card data regenerated together.

## Result

There are translation-quality problems that can mislead readers.

The good news: I found no remaining kana outside protected trait/card-name fields in `text_zh`; the problem is not untranslated Japanese text.

The bad news: 30 files contain high-risk machine-translation artifacts in effect text. These are not just style issues; several change the direction, timing, or target of an effect.

## Repair Progress

### 2026-09-04 Conservative Repair Pass

- Added `tools/repair_high_risk_translation_phrases.py` for repeatable conservative cleanup.
- Repaired 2,671 affected cards across the 30 high-risk files.
- Reduced high-risk pattern hits from 8,118 to 169.
- Remaining high-risk cards after this pass: 160.
- Remaining kana outside protected `《》` / `「」` fields: 0.
- This pass intentionally did not try to fully rewrite complex effects. The remaining 160 cards should be fixed by retranslation from `text_jp`, not by broader global replacement.

Remaining high-risk files after the first repair pass:

| File | Series | Remaining High-Risk Cards |
|---|---|---:|
| `imc_cards.json` | 偶像大師 灰姑娘女孩 | 21 |
| `dc_cards.json` | D.C.＆Dal Segno | 15 |
| `smp_cards.json` | Summer Pockets | 10 |
| `gbf_cards.json` | 碧藍幻想 | 9 |
| `mar_cards.json` | MARVEL | 9 |
| `thp_cards.json` | 東方Project | 9 |
| `ga_cards.json` | GA文庫 | 7 |
| `kms_cards.json` | 黃金拼圖 | 7 |
| `tal_cards.json` | Tales of 系列 | 7 |
| `im_cards.json` | 偶像大師 | 6 |
| `rz_cards.json` | Re:從零開始的異世界生活 | 6 |
| `prd_cards.json` | 動畫 公主連結！Re:Dive | 5 |
| `dal_cards.json` | 約會大作戰 | 4 |
| `knk_cards.json` | 出租女友 | 4 |
| `mki_cards.json` | 敗北女角太多了！ | 4 |
| `nta_cards.json` | 魔法少女奈葉 | 4 |
| `pxr_cards.json` | PIXAR | 4 |
| `sby_cards.json` | 青春豬頭少年系列 | 4 |
| `ddd_cards.json` | 膽大黨 | 3 |
| `ias_cards.json` | 偶像大師 百萬人演唱會！ | 3 |
| `isc_cards.json` | 偶像大師 閃耀色彩 | 3 |
| `kj8_cards.json` | 怪獸8號 | 3 |
| `all_cards.json` | 突擊莉莉 | 2 |
| `anm_cards.json` | anemoi | 2 |
| `bav_cards.json` | 蔚藍檔案 | 2 |
| `key_cards.json` | Key | 2 |
| `vrg_cards.json` | VIRTUAL GIRL @ WORLD'S END | 2 |
| `bd10th_cards.json` | BanG Dream! 10th Anniversary | 1 |
| `bdy_cards.json` | BanG Dream! [夢限大Mewtype] | 1 |
| `pi_cards.json` | Fate/kaleid liner 魔法少女☆伊莉雅 | 1 |

## High-Risk Findings

| Problem Pattern | Count | Why It Matters |
|---|---:|---|
| `休息室到放置` | 1,904 | Zone movement direction is awkward or unclear; should be `放到休息室`. |
| `你費用可以支付` | 1,176 | Cost timing is understandable but nonstandard; should be `你可以支付費用`. |
| `的卡手牌` / `手牌從舞台` | 1,701 combined | Can invert movement direction; `手札から舞台に置かれた時` must read as `從手牌被放置到舞台時`. |
| `對手到...傷害` / `傷害賦予` / `傷害与` | 889 combined | Damage effects must be explicit, e.g. `給予對手1點傷害`; current wording may be unreadable. |
| `手牌到加入` / `手牌到返回` | 883 combined | Search/salvage effects become unclear; should be `加入手牌` / `回到手牌`. |
| `到見` | 309 | Search effects should say `給對手看`; current wording is not readable. |
| `次的能力得到` | 235 | Ability-granting text should say `獲得以下能力`. |

## Most Affected Files

| File | Series | High-Risk Cards |
|---|---|---:|
| `dc_cards.json` | D.C.＆Dal Segno | 236 |
| `imc_cards.json` | 偶像大師 灰姑娘女孩 | 195 |
| `rz_cards.json` | Re:從零開始的異世界生活 | 189 |
| `nta_cards.json` | 魔法少女奈葉 | 155 |
| `smp_cards.json` | Summer Pockets | 141 |
| `mar_cards.json` | MARVEL | 139 |
| `all_cards.json` | 突擊莉莉 | 127 |
| `sby_cards.json` | 青春豬頭少年系列 | 122 |
| `im_cards.json` | 偶像大師 | 121 |
| `isc_cards.json` | 偶像大師 閃耀色彩 | 113 |
| `dal_cards.json` | 約會大作戰 | 110 |
| `ddd_cards.json` | 膽大黨 | 93 |
| `key_cards.json` | Key | 93 |
| `ias_cards.json` | 偶像大師 百萬人演唱會！ | 85 |
| `prd_cards.json` | 動畫 公主連結！Re:Dive | 76 |
| `thp_cards.json` | 東方Project | 73 |
| `bav_cards.json` | 蔚藍檔案 | 72 |
| `pi_cards.json` | Fate/kaleid liner 魔法少女☆伊莉雅 | 65 |
| `knk_cards.json` | 出租女友 | 63 |
| `pxr_cards.json` | PIXAR | 62 |

## Representative Examples

### Movement Direction

- File: `all_cards.json`
- Card: `ALL/S76-P12`
- Japanese: `他のあなたの《リリィ》のキャラかこのカードが手札から舞台に置かれた時`
- Current Chinese: `其他你的《リリィ》的角色或的卡手牌從舞台到被放置時`
- Safer wording: `其他你的《リリィ》角色或此卡從手牌被放置到舞台時`

### Optional Cost

- File: `all_cards.json`
- Card: `ALL/S76-P24`
- Japanese: `あなたはコストを払ってよい。そうしたら`
- Current Chinese: `你費用可以支付。如此做的話`
- Safer wording: `你可以支付費用。這麼做了的話`

### Damage

- File: `all_cards.json`
- Card: `ALL/S76-010`
- Japanese: `相手に2ダメージを与える`
- Current Chinese: `對手到2傷害賦予`
- Safer wording: `給予對手2點傷害`

### Search / Reveal

- File: `all_cards.json`
- Card: `ALL/S76-045`
- Japanese: `《リリィ》のキャラを1枚まで選んで相手に見せ、手札に加え`
- Current Chinese: `《リリィ》的角色1張為止選擇對手到見、手牌到加入`
- Safer wording: `選擇至多1張《リリィ》角色給對手看，加入手牌`

## Style Findings

These are lower priority because they usually do not change the rule meaning, but they should still be cleaned up during future review:

| Pattern | Count | Recommended Style |
|---|---:|---|
| `你自己的牌組` | 1,560 | `自己的牌組` or `你的牌組`, chosen consistently. |
| `從上方` | 1,349 | `最上方` is clearer for card zones. |
| `1張為止` and similar | 1,394 combined | `至多1張`, `至多2張`, etc. |
| `自分的` | 199 | `自己的`. |
| `他的你的` | 127 | `你的`. |

## Recommendation

Do not do a blind global replace on the current card files. I tested that approach locally and it can fix many phrases, but it also risks damaging normal phrases such as `剩下的卡` if the rule is too broad.

The safer path is:

1. Pause new-series translation briefly.
2. Fix the 30 high-risk files in priority order, starting with the top 10 above.
3. For each file, retranslate affected cards from `text_jp`, not from the broken Chinese.
4. Validate after each file: structure check, kana scan outside `《》` / `「」`, and card-count check.
5. After the high-risk set is clean, resume new-series translation using this audit as a quality gate.
