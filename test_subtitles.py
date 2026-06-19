import unittest

import main


class SubtitleProfileTest(unittest.TestCase):
    def test_profile_duration_limits(self):
        cues = [main.Cue(1, 0, 500, "Short")]
        issues = main.lint(cues, min_duration_ms=700)
        self.assertTrue(any(item["type"] == "short_duration" for item in issues))

    def test_strict_parser_rejects_invalid_block(self):
        with self.assertRaises(ValueError):
            main.parse_srt("1\ninvalid\ntext", strict=True)

    def test_clean_and_render_preserve_timestamps(self):
        cues = [main.Cue(1, 0, 2000, "Line with space   ")]
        cleaned = main.clean_cues(cues)
        output = main.render_srt(cleaned)
        self.assertIn("00:00:00,000 --> 00:00:02,000", output)
        self.assertIn("Line with space\n", output)
        self.assertNotIn("space   ", output)

    def test_timestamp_round_trip(self):
        value = "01:02:03,456"
        self.assertEqual(main.from_ms(main.to_ms(value)), value)


if __name__ == "__main__":
    unittest.main()
