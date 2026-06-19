import tempfile
import unittest
from pathlib import Path

import main


class WebVTTSupportTest(unittest.TestCase):
    def test_parse_basic_webvtt(self):
        content = """WEBVTT

intro
00:00:00.000 --> 00:00:02.000
First caption

00:02.500 --> 00:04.000 align:start
Second caption
"""
        cues = main.parse_vtt(content, strict=True)
        self.assertEqual(len(cues), 2)
        self.assertEqual(cues[0].identifier, "intro")
        self.assertEqual(cues[1].start_ms, 2500)

    def test_vtt_round_trip(self):
        cues = [main.Cue(1, 0, 2000, "Caption", "cue-a")]
        output = main.render_vtt(cues)
        reparsed = main.parse_vtt(output, strict=True)
        self.assertEqual(reparsed[0].start_ms, 0)
        self.assertEqual(reparsed[0].end_ms, 2000)
        self.assertEqual(reparsed[0].identifier, "cue-a")

    def test_srt_to_vtt_rendering(self):
        cues = main.parse_srt("1\n00:00:00,000 --> 00:00:01,500\nHello\n", strict=True)
        output = main.render_subtitle(cues, "vtt")
        self.assertTrue(output.startswith("WEBVTT"))
        self.assertIn("00:00:00.000 --> 00:00:01.500", output)

    def test_parse_subtitle_detects_extension(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.vtt"
            path.write_text("WEBVTT\n\n00:00:00.000 --> 00:00:01.000\nText\n", encoding="utf-8")
            subtitle_format, cues = main.parse_subtitle(str(path), strict=True)
        self.assertEqual(subtitle_format, "vtt")
        self.assertEqual(len(cues), 1)

    def test_unsupported_extension_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_text("text", encoding="utf-8")
            with self.assertRaises(ValueError):
                main.parse_subtitle(str(path))


if __name__ == "__main__":
    unittest.main()
