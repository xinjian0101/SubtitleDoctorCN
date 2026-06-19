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
    if minute >= 60 or second >= 60:
        raise ValueError(f"Invalid SRT timestamp: {value}")
    return ((hour * 60 + minute) * 60 + second) * 1000 + millisecond


def from_ms(value: int) -> str:
    if value < 0:
        raise ValueError("Timestamp must be non-negative")
    hour, remainder = divmod(value, 3_600_000)
    minute, remainder = divmod(remainder, 60_000)
    second, millisecond = divmod(remainder, 1000)
    return f"{hour:02d}:{minute:02d}:{second:02d},{millisecond:03d}"


def parse_srt(content: str, strict: bool = False) -> list[Cue]:
    cues: list[Cue] = []
    for block_number, block in enumerate(re.split(r"\r?\n\r?\n+", content.strip()), 1):
        lines = [line.rstrip() for line in block.splitlines()]
        if len(lines) < 3 or "-->" not in lines[1]:
            if strict and any(line.strip() for line in lines):
                raise ValueError(f"Invalid SRT block {block_number}")
            continue
        try:
            start, end = [part.strip() for part in lines[1].split("-->", 1)]
            cues.append(Cue(int(lines[0]), to_ms(start), to_ms(end), "\n".join(lines[2:])))
        except ValueError as exc:
            if strict:
                raise ValueError(f"Invalid SRT block {block_number}: {exc}") from exc
    return cues


def load_profile(path: str | None) -> dict:
    if not path:
        return {}
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("Profile must be a JSON object")
    return value


def clean_text(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(line.rstrip() for line in normalized.split("\n")).strip()


def clean_cues(cues: list[Cue]) -> list[Cue]:
    return [Cue(cue.index, cue.start_ms, cue.end_ms, clean_text(cue.text)) for cue in cues]


def render_srt(cues: list[Cue]) -> str:
    blocks = [
        f"{cue.index}\n{from_ms(cue.start_ms)} --> {from_ms(cue.end_ms)}\n{cue.text}"
        for cue in cues
    ]
    return "\n\n".join(blocks) + ("\n" if blocks else "")


def lint(
    cues: list[Cue],
    max_chars_per_line: int = 22,
    max_cps: float = 15.0,
    min_duration_ms: int = 0,
    max_duration_ms: int | None = None,
) -> list[dict]:
    if max_chars_per_line <= 0 or max_cps <= 0:
        raise ValueError("Thresholds must be positive")
    issues: list[dict] = []
    previous_end = -1
    for cue in cues:
        duration_ms = cue.end_ms - cue.start_ms
        duration = duration_ms / 1000
        if cue.start_ms < previous_end:
            issues.append({"cue": cue.index, "type": "overlap", "level": "warning", "message": "Timeline overlaps the previous cue"})
        previous_end = max(previous_end, cue.end_ms)
        if duration_ms <= 0:
            issues.append({"cue": cue.index, "type": "duration", "level": "error", "message": "Duration must be positive"})
            continue
        if min_duration_ms and duration_ms < min_duration_ms:
            issues.append({"cue": cue.index, "type": "short_duration", "level": "warning", "value": duration_ms})
        if max_duration_ms is not None and duration_ms > max_duration_ms:
            issues.append({"cue": cue.index, "type": "long_duration", "level": "warning", "value": duration_ms})
        compact = re.sub(r"\s+", "", cue.text)
        cps = len(compact) / duration
        if cps > max_cps:
            issues.append({"cue": cue.index, "type": "reading_speed", "level": "warning", "value": round(cps, 2)})
        for line in cue.text.splitlines():
            if len(line) > max_chars_per_line:
                issues.append({"cue": cue.index, "type": "line_length", "level": "warning", "value": len(line)})
        if MIXED_PUNCT.search(cue.text):
            issues.append({"cue": cue.index, "type": "mixed_punctuation", "level": "info"})
    return issues


def summarize(issues: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for issue in issues:
        level = issue.get("level", "warning")
        counts[level] = counts.get(level, 0) + 1
    return counts


def main() -> None:
    parser = argparse.ArgumentParser(description="Check SRT subtitle quality.")
    parser.add_argument("srt")
    parser.add_argument("-o", "--output", default="subtitle-report.json")
    parser.add_argument("--profile")
    parser.add_argument("--max-line", type=int)
    parser.add_argument("--max-cps", type=float)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--clean", action="store_true")
    parser.add_argument("--clean-output", default="subtitle-cleaned.srt")
    args = parser.parse_args()

    profile = load_profile(args.profile)
    max_line = args.max_line if args.max_line is not None else int(profile.get("max_characters_per_line", 22))
    max_cps = args.max_cps if args.max_cps is not None else float(profile.get("max_characters_per_second", 15.0))
    min_duration = int(profile.get("minimum_duration_ms", 0))
    maximum = profile.get("maximum_duration_ms")
    max_duration = int(maximum) if maximum is not None else None

    cues = parse_srt(Path(args.srt).read_text(encoding="utf-8-sig"), strict=args.strict)
    if args.clean:
        cues = clean_cues(cues)
        Path(args.clean_output).write_text(render_srt(cues), encoding="utf-8")
    issues = lint(cues, max_line, max_cps, min_duration, max_duration)
    report = {
        "profile": profile.get("id") if profile else None,
        "cues": len(cues),
        "issue_count": len(issues),
        "level_summary": summarize(issues),
        "issues": issues,
    }
    Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Checked {len(cues)} cues; found {len(issues)} issues")


if __name__ == "__main__":
    main()
