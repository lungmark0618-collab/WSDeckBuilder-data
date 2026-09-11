import unittest
from make_translation_announcements import generate

class TranslationAnnouncementTests(unittest.TestCase):
    def test_existing_series_version_bump_does_not_announce(self):
        known, items = generate({'sets': [{'title_code': 'A', 'data_version': 9}]}, ['A'], [], '2026-09-11')
        self.assertEqual(items, [])

    def test_new_series_once_and_manual_announcements_preserved(self):
        manifest = {'sets': [{'title_code': 'B', 'title_name_zh': '新作品', 'data_version': 2}]}
        manual = {'id': 'manual', 'date': '2026-09-10', 'title': '通知', 'body': '內容'}
        known, items = generate(manifest, ['A'], [manual], '2026-09-11')
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]['id'], 'data-update-B-2')
        self.assertEqual(items[1], manual)
        _, repeated = generate(manifest, known, items, '2026-09-12')
        self.assertEqual(items, repeated)

    def test_existing_release_id_is_not_duplicated(self):
        old = {'id': 'data-update-A-1', 'date': '2026-09-10', 'title': '公告', 'body': '內容'}
        _, items = generate({'sets': [{'title_code': 'A', 'data_version': 1}]}, [], [old], '2026-09-11')
        self.assertEqual(items, [old])
