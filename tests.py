import unittest
import main


class SubtitleDoctorTest(unittest.TestCase):
    def test_overlap_detection(self):
        content = """1
00:00:00,000 --> 00:00:02,000
第一句

2
00:00:01,500 --> 00:00:03,000
第二句
"""
        issues = main.lint(main.parse_srt(content))
        self.assertTrue(any(item["type"] == "overlap" for item in issues))


if __name__ == "__main__":
    unittest.main()
