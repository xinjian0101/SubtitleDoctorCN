from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


TIME_RE = re.compile(r"(\d{2}):(\d{2}):(\d{2}),(\d{3})")
MIXED_PUNCT = re.compile(r"[，。！？；：].*[,.!?;:]|[,.!?;:].*[，。！？；：]")


@dataclass(frozen=True)
class Cue:
    index: int
    start_ms: int
    end_ms: int
    text: str


def to_ms(value: str) -> int:
    match = TIME_RE.fullmatch(value.strip())
    if not match:
        raise ValueError(f"Invalid SRT timestamp: {value}")
    hour, minute, second, millisecond = map(int, match.groups())
    return ((hour * 60 + minute) * 60 + second) * 1000 + millisecond


def parse_srt(content: str) -> list[Cue]:
    cues: list[Cue] = []
    for block in re.split(r"\r?\n\r?\n+", content.strip()):
        lines = [line.rstrip() for line in block.splitlines()]
        if len(lines) < 3 or "-->" not in lines[1]:
            continue
        start, end = [part.strip() for part in lines[1].split("-->", 1)]
        cues.append(Cue(int(lines[0]), to_ms(start), to_ms(end), "\n".join(lines[2:])))
    return cues


def lint(cues: list[Cue], max_chars_per_line: int = 22, max_cps: float = 15.0) -> list[dict]:
    issues: list[dict] = []
    previous_end = -1
    for cue in cues:
        duration = (cue.end_ms - cue.start_ms) / 1000
        if cue.start_ms < previous_end:
            issues.append({"cue": cue.index, "type": "overlap", "message": "Timeline overlaps the previous cue"})
        previous_end = max(previous_end, cue.end_ms)
        if duration <= 0:
            issues.append({"cue": cue.index, "type": "duration", "message": "Duration must be positive"})
            continue
        compact = re.sub(r"\s+", "", cue.text)
        cps = len(compact) / duration
        if cps > max_cps:
            issues.append({"cue": cue.index, "type": "reading_speed", "value": round(cps, 2)})
        for line in cue.text.splitlines():
            if len(line) > max_chars_per_line:
                issues.append({"cue": cue.index, "type": "line_length", "value": len(line)})
        if MIXED_PUNCT.search(cue.text):
            issues.append({"cue": cue.index, "type": "mixed_punctuation"})
    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Lint Chinese SRT subtitles.")
    parser.add_argument("srt")
    parser.add_argument("-o", "--output", default="subtitle-report.json")
    parser.add_argument("--max-line", type=int, default=22)
    parser.add_argument("--max-cps", type=float, default=15.0)
    args = parser.parse_args()
    cues = parse_srt(Path(args.srt).read_text(encoding="utf-8-sig"))
    issues = lint(cues, args.max_line, args.max_cps)
    report = {"cues": len(cues), "issue_count": len(issues), "issues": issues}
    Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Checked {len(cues)} cues; found {len(issues)} issues")


if __name__ == "__main__":
    main()
