# Exception Policy

Some findings are intentional editorial choices. Exceptions must be explicit and reviewable.

## Acceptable exception examples

- Intentional timing overlap for simultaneous speakers.
- A long line that cannot be split without changing meaning.
- A project-approved brand spelling that differs from a general dictionary.
- A rapid caption synchronized to a visible on-screen event.

## Required exception fields

- Cue number.
- Rule identifier.
- Decision.
- Reason.
- Reviewer.
- Review date.
- Scope: current cue, current file, or named project.

## Prohibited exceptions

Do not approve corrupt timestamps, unreadable output, accidental text loss, or unsupported claims that a file passed all checks.

## Expiration

Project-wide exceptions should be reviewed when the profile version, dictionary version, or delivery platform changes.

## Reporting

Final reports should show accepted exceptions separately from unresolved findings. Accepted exceptions must not be counted as automatically corrected issues.

## Auditability

Store exception decisions with the exact source and output checksums so they cannot be reused silently for a different file.
