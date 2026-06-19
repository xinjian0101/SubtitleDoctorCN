import unittest
import main


class SubtitleDoctorTest(unittest.TestCase):
    def test_overlap_detection(self):
        cues = [
            main.Cue(1, 0, 2000, "First line"),
            main.Cue(2, 1500, 3000, "Second line"),
        ]
        issues = main.lint(cues)
        self.assertTrue(any(item["type"] == "overlap" for item in issues))


if __name__ == "__main__":
    unittest.main()
