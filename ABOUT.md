# About SubtitleDoctorCN

## Mission

SubtitleDoctorCN provides deterministic subtitle quality checks before captions are delivered, embedded, or published.

## Intended users

- Subtitle editors
- Video-production teams
- Course and interview publishers
- Developers building local caption-review pipelines
- Teams that need reproducible profile-based checks

## Core capabilities

- SRT parsing
- Timeline overlap checks
- Duration checks
- Reading-speed checks
- Line-length checks
- Mixed-punctuation hints
- Profile-driven thresholds
- Strict parsing mode
- Safe whitespace cleanup and SRT rendering

## Boundaries

The tool does not perform speech recognition, translate dialogue, rewrite meaning, verify proper names, or replace editorial review against source media.

## Architecture

```text
SRT input -> parser -> optional deterministic cleanup
          -> profile thresholds -> rule engine -> JSON report
          -> optional normalized SRT output
```

## Design priorities

1. Preserve timestamps and dialogue meaning
2. Keep automatic changes deterministic and narrow
3. Separate blocking errors from review findings
4. Version style profiles
5. Retain cue indices for auditability
6. Run locally

## Maturity

The project is an executable MVP with profile schemas, review workflows, exception policies, approval records, tests, and normalized SRT output.

## Governance

Parser and timing changes require fixtures. New automatic corrections must remain opt-in and must not alter dialogue meaning without explicit editorial control.
