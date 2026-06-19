# Approval Record

A delivery review should preserve enough information to reproduce the quality check.

## Required information

- Source subtitle filename.
- Source file checksum.
- Related media identifier.
- Selected profile identifier and version.
- Terminology dictionary identifier and version.
- Tool commit SHA.
- Reviewer name.
- Review date.
- Number of unresolved findings.
- Final output checksum.

## Decision values

Use one of these values:

- `approved`
- `approved-with-notes`
- `changes-required`
- `rejected`

## Finding record

For every accepted finding, record the cue number, rule identifier, reviewer decision, reason, and whether the decision applies only to the current file.

## Storage

Keep the approval record beside the original report, corrected subtitle, final report, selected profile, and dictionary snapshot.

## Integrity

An approval record should be treated as invalid when the final subtitle checksum does not match the recorded output checksum.
