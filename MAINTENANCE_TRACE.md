# Maintenance Trace

Batch: `content-enrichment-2026-06-19`

## Iteration 07

- Expanded the README with use cases, parameter guidance, issue explanations, review workflow, human-review boundaries, and limitations.
- Kept the existing SRT-only and check-only scope explicit.

## Iteration 08

- Added this visible maintenance trace.
- Defined test and compatibility expectations for future subtitle-rule changes.

## Iteration 09

- Planned document: `docs/REVIEW_CHECKLIST.md`.
- Converts automated findings into an ordered human approval workflow.

## Validation record

| Check | Result |
|---|---|
| Existing CLI retained | pass |
| Existing CPS and line-length parameters retained | pass |
| No automatic-fix claim introduced | pass |
| Local-processing statement retained | pass |
| Documentation links reviewed | pass after iteration 09 |

## Maintenance policy

1. Every rule must include a clear error code and human-readable message.
2. Threshold changes require fixtures for Chinese, English, numbers, and mixed punctuation.
3. Parser changes must preserve valid SRT timing and text.
4. Automatic repair must remain opt-in if introduced later.
5. Reports must retain source cue indices so reviewers can locate problems.
6. Style profiles must be versioned and reproducible.

## Open items

- No ASS/SSA/VTT parser in the current baseline.
- No acoustic alignment or speaker identification.
- No semantic proofreading or proper-noun verification.
- No automatic player preview.
