# Changelog

## Unreleased

### Added

- SRT parsing and timestamp conversion.
- Timeline overlap and invalid-duration checks.
- Configurable reading-speed and line-length thresholds.
- Mixed-punctuation review hint.
- Rule reference under `docs/RULES.md`.
- Versioned terminology dictionary format example.
- Runnable subtitle fixture and automated test workflow.

### Changed

- Documentation now distinguishes deterministic corrections from editorial suggestions.

### Known limitations

- The MVP does not preserve advanced SRT formatting tags.
- Multi-speaker intentional overlaps are reported without semantic interpretation.
- Grammar and terminology findings remain advisory.
- ASS and WebVTT inputs are not yet supported.

## 0.1.0 — 2026-06-19

Initial executable subtitle quality-checking MVP.

## Maintenance policy

- Timestamp behavior must remain backward compatible.
- New rules require a stable identifier and documented severity.
- Automatic corrections must preserve timestamps and dialogue meaning.
- Dictionary changes must remain project-configurable rather than universal defaults.
