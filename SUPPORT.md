# Support

## Start here

Review these documents before opening an issue:

- [README](README.md) for supported commands and formats
- [About](ABOUT.md) for mission, boundaries, and maturity
- [Rule Reference](docs/RULES.md) for finding definitions
- [Style Profiles](docs/STYLE_PROFILES.md) for threshold behavior
- [Review Workflow](docs/REVIEW_WORKFLOW.md) for editorial handling
- [Exception Policy](docs/EXCEPTION_POLICY.md) for accepted deviations

## Bug reports

Use the structured **Bug report** form for SRT or WebVTT parsing, timing checks, profile loading, cleanup, rendering, conversion, or report defects.

Include:

- exact commit or release;
- operating system and Python version;
- subtitle format and encoding;
- minimal synthetic subtitle fixture;
- profile file or threshold arguments;
- complete reproduction command;
- expected and actual output.

## Feature requests

Use the **Feature request** form. Describe the production workflow, format impact, editorial controls, compatibility requirements, and measurable acceptance criteria.

## Subtitle-data rules

Do not upload confidential transcripts, unreleased dialogue, private media, client names, or personal information. Replace all content with synthetic subtitle text while preserving the timing structure needed to reproduce the behavior.

## Project boundaries

SubtitleDoctorCN does not provide:

- speech recognition;
- translation quality guarantees;
- proper-name verification;
- automatic semantic rewriting;
- final editorial approval;
- player-specific rendering guarantees across every device.

## Cleanup behavior

Automatic cleanup is intentionally narrow and opt-in. It normalizes whitespace and subtitle formatting; it must not silently change dialogue meaning.

## Response expectations

Support is community-maintained and best effort. Small reproducible subtitle files and clearly identified format expectations are the fastest to review.
