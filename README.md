# SubtitleDoctorCN

A local SRT quality checker for subtitle delivery workflows. The project finds common timeline, duration, reading-speed, line-length, and punctuation issues before subtitles are published, embedded, or handed off for review.

> The current release performs checks only. It does not rewrite subtitle text automatically and does not replace editorial review.

## Use cases

- Pre-delivery checks for short-form video, courses, interviews, and commentary
- Basic rule gates in batch subtitle workflows
- Punctuation consistency checks for mixed-language captions
- Parameterized review for different platform requirements
- Before-and-after comparison during subtitle revision

## Current capabilities

- Timeline overlap detection
- Invalid or unusual duration checks
- Characters-per-second review
- Maximum line-length review
- Mixed punctuation hints
- Structured JSON output
- Local processing with no subtitle upload

## Quick start

### Requirements

- Python 3.10 or newer
- A standard UTF-8 SRT file

### Run

```bash
python main.py example.srt --max-cps 15 --max-line 22 -o report.json
```

### Test

```bash
python -m unittest -v
```

## Options

| Option | Example | Description |
|---|---:|---|
| `--max-cps` | `15` | maximum characters per second before a review finding |
| `--max-line` | `22` | maximum characters per subtitle line |
| `-o` | `report.json` | output path for the JSON report |

Thresholds should reflect the audience, screen size, language density, and delivery platform. One threshold is not suitable for every project.

## Finding types

### Timeline overlap

A cue starts before the previous cue ends. This may cause simultaneous display or unexpected replacement behavior.

### Invalid duration

A cue with zero or negative duration cannot be displayed correctly. Very short or very long cues also require contextual review.

### High reading speed

Characters per second above the selected threshold may be difficult to read. Teams should use one consistent counting method when comparing revisions.

### Long line

A long line may wrap on mobile screens, cover important visual content, or reduce readability.

### Mixed punctuation

The checker flags lines that appear to combine punctuation styles. The finding is advisory because editorial style can differ by project.

## Recommended workflow

1. Export a UTF-8 SRT file from the editing or transcription tool.
2. Select the appropriate style profile and thresholds.
3. Run the checker and group findings by type.
4. Review each cue against the source media.
5. Revise the subtitle file.
6. Run the checker again.
7. Store the final SRT, report, profile version, and approval record together.

## Human review remains necessary

Rule-based checks cannot reliably determine:

- whether names, places, brands, and numbers are correct;
- whether meaning is faithful to the source;
- whether line breaks match tone and pacing;
- whether specialized terms need explanation;
- whether captions cover important visual information;
- whether speaker changes are clear.

## Known limitations

- The current baseline supports SRT quality checks only.
- It does not repair timelines or rewrite dialogue.
- It does not perform speech recognition or audio alignment.
- Rule and threshold checks can produce false positives.
- It does not determine delivery-platform policy.

## Documentation

- [Rule Reference](docs/RULES.md)
- [Style Profiles](docs/STYLE_PROFILES.md)
- [Review Workflow](docs/REVIEW_WORKFLOW.md)
- [Approval Record](docs/APPROVAL_RECORD.md)
- [Exception Policy](docs/EXCEPTION_POLICY.md)
- [Review Checklist](docs/REVIEW_CHECKLIST.md)
- [Maintenance Trace](MAINTENANCE_TRACE.md)

## License

MIT
