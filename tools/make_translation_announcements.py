#!/usr/bin/env python3
"""從已發布系列基準產生新系列公告；既有修字與重新產 manifest 不公告。"""
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta

ROOT = Path(__file__).resolve().parent.parent

def generate(manifest, known, announcements, date):
    seen = set(known)
    items = list(announcements)
    ids = {item['id'] for item in items}
    for entry in manifest['sets']:
        code = entry['title_code']
        if code not in seen:
            item_id = f"data-update-{code}-{entry['data_version']}"
            if item_id not in ids:
                name = entry.get('title_name_zh') or code
                items.append(dict(id=item_id, date=date, title=f'「{name}」新系列卡表已上線',
                    body='新收錄的系列卡表已發布。尚未安裝時，請到設定檢查並下載卡表；安裝後即可在圖鑑查看。'))
                ids.add(item_id)
            seen.add(code)
    return sorted(seen), sorted(items, key=lambda item: (item['date'], item['id']), reverse=True)

def main():
    manifest = json.loads((ROOT / 'manifest.json').read_text())
    baseline = ROOT / 'announcement_series.json'
    if not baseline.exists():
        raise RuntimeError('缺少系列基準，拒絕將所有舊系列當成新通知')
    known = json.loads(baseline.read_text())['title_codes']
    feed_path = ROOT / 'announcements.json'
    feed = json.loads(feed_path.read_text())
    date = datetime.now(timezone(timedelta(hours=8))).date().isoformat()
    known, feed['items'] = generate(manifest, known, feed['items'], date)
    for path, data in [(baseline, {'title_codes': known}), (feed_path, feed)]:
        temp = path.with_suffix('.tmp')
        temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
        temp.replace(path)

if __name__ == '__main__':
    main()
