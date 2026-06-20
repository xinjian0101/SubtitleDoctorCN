<div align="center">

# SubtitleDoctorCN

**Deterministic SRT and WebVTT quality checks for production subtitle workflows.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Formats](https://img.shields.io/badge/Formats-SRT%20%7C%20WebVTT-0969da)](ABOUT.md)
[![License](https://img.shields.io/badge/License-MIT-2ea44f)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active%20MVP-f59e0b)](MAINTENANCE_TRACE.md)

[Quick start](#quick-start) · [Checks](#quality-checks) · [Profiles](docs/STYLE_PROFILES.md) · [About](ABOUT.md) · [Review workflow](docs/REVIEW_WORKFLOW.md)

</div>

---

SubtitleDoctorCN checks subtitle timing, reading speed, line length, duration, overlap, and punctuation consistency before delivery. It supports SRT and WebVTT, versioned style profiles, strict parsing, JSON reports, and deterministic cleanup without rewriting dialogue meaning.

> [!IMPORTANT]
> Rule-based findings require editorial review against the source media. Automatic cleanup is intentionally limited to safe whitespace and format normalization.

## At a glance

| Area | Current support |
|---|---|
| Input | SRT and WebVTT |
| Timing | Overlap, positive duration, min/max duration |
| Readability | Characters per second, line length |
| Style | Mixed-punctuation advisory |
| Profiles | Versioned JSON thresholds |
| Cleanup | Safe whitespace normalization |
| Conversion | SRT ↔ WebVTT |
| Reports | Structured JSON with issue levels |

## Quick start

Check an SRT file:

```bash
python main.py example.srt \
  --profile profiles/mobile-short.json \
  -o subtitle-report.json
```

Clean and convert WebVTT to SRT:

```bash
python main.py captions.vtt \
  --strict \
  --clean \
  --clean-format srt \
  --clean-output captions-cleaned.srt
```

Run tests:

```bash
python -m unittest -v
```

## Capability matrix

| Capability | Status | Notes |
|---|---:|---|
| SRT parsing and rendering | ✅ | UTF-8 input |
| WebVTT parsing and rendering | ✅ | Identifiers and cue settings supported |
| Profile-driven thresholds | ✅ | JSON profile files |
| Strict malformed-block rejection | ✅ | Includes block number |
| Deterministic cleanup | ✅ | Whitespace only |
| Audio alignment | ⏳ | Not implemented |
| Dialogue rewriting | ❌ | Intentionally outside scope |

## Quality checks

| Finding | Level | Meaning |
|---|---|---|
| `duration` | error | End time is not greater than start time |
| `overlap` | warning | Cue overlaps the previous cue |
| `short_duration` | warning | Cue is shorter than the profile minimum |
| `long_duration` | warning | Cue is longer than the profile maximum |
| `reading_speed` | warning | Characters per second exceed the threshold |
| `line_length` | warning | A line exceeds the configured limit |
| `mixed_punctuation` | info | Punctuation styles may be inconsistent |

## CLI examples

```bash
python main.py subtitles.srt --max-cps 15 --max-line 22
python main.py subtitles.vtt --strict
python main.py subtitles.srt --clean --clean-output normalized.srt
python main.py subtitles.srt --clean --clean-format vtt --clean-output normalized.vtt
```

## Recommended workflow

```text
subtitle export
      ↓
strict parser
      ↓
style profile
      ↓
rule checks
      ↓
editor review against source media
      ↓
optional deterministic cleanup
      ↓
final report + approval record
```

## Repository map

| Path | Purpose |
|---|---|
| `main.py` | Parsers, renderers, cleanup, checks, and CLI |
| `profiles/` | Versioned delivery profiles |
| `schema/` | Profile contract |
| `dictionaries/` | Terminology examples |
| `docs/` | Rules, review, approval, and exception policies |
| `example.srt` | Synthetic sample subtitle |
| `test_*.py` | Parser, profile, cleanup, and WebVTT tests |
| `ABOUT.md` | Mission, maturity, boundaries, and governance |

## Human review remains necessary

The checker cannot reliably determine whether names, brands, numbers, translation choices, tone, speaker identity, or visual placement are correct. Review every final file against the source media.

## Documentation

- [About the project](ABOUT.md)
- [Rule reference](docs/RULES.md)
- [Style profiles](docs/STYLE_PROFILES.md)
- [Review workflow](docs/REVIEW_WORKFLOW.md)
- [Approval record](docs/APPROVAL_RECORD.md)
- [Exception policy](docs/EXCEPTION_POLICY.md)
- [Review checklist](docs/REVIEW_CHECKLIST.md)
- [Maintenance trace](MAINTENANCE_TRACE.md)

## License

MIT
