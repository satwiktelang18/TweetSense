import unittest

from tweet_columns import detect_text_column


class TweetColumnTests(unittest.TestCase):
    def test_detects_common_export_columns(self):
        self.assertEqual(detect_text_column(["id", "full_text"]), "full_text")
        self.assertEqual(detect_text_column(["Author", "Message"]), "Message")

    def test_prefers_tweet_column_first(self):
        self.assertEqual(detect_text_column(["text", "tweet"]), "tweet")

    def test_returns_none_without_text_column(self):
        self.assertIsNone(detect_text_column(["created_at", "likes"]))


if __name__ == "__main__":
    unittest.main()
