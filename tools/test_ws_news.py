import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import fetch_ws_news
import make_ws_news

class NewsSafetyTests(unittest.TestCase):
    def test_failed_fetch_keeps_existing_output(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / 'news.json'
            out.write_text('previous')
            with patch('sys.argv', ['fetch', '--out', str(out)]), patch.object(fetch_ws_news, 'fetch', side_effect=OSError('offline')):
                with self.assertRaises(RuntimeError): fetch_ws_news.main()
            self.assertEqual(out.read_text(), 'previous')

    def test_changed_markup_does_not_publish_empty_feed(self):
        with patch('sys.argv', ['fetch']), patch.object(fetch_ws_news, 'fetch', return_value='<html>changed</html>'):
            with self.assertRaises(RuntimeError): fetch_ws_news.main()

    def test_empty_merge_keeps_published_feed(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / 'news.json'
            out.write_text('previous')
            with patch.object(make_ws_news, 'load_items', return_value=[]), patch.object(make_ws_news, 'OUT_PATH', str(out)):
                with self.assertRaises(ValueError): make_ws_news.main()
            self.assertEqual(out.read_text(), 'previous')

    def test_manual_copy_overrides_official_and_keeps_other_categories(self):
        official = dict(date='2026-09-11', title_jp='商品', url='https://example.com/product', source='official')
        manual = dict(official, source='manual', title_zh='人工修正')
        rules = dict(date='2026-09-10', title_jp='規則', url='https://example.com/rules', categories=['ルール'])
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / 'news.json'
            with patch.object(make_ws_news, 'load_items', side_effect=[[official, rules], [manual]]), patch.object(make_ws_news, 'OUT_PATH', str(out)):
                make_ws_news.main()
            result = json.loads(out.read_text())['items']
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0]['title_zh'], '人工修正')
            self.assertEqual(result[1]['categories'], ['ルール'])
