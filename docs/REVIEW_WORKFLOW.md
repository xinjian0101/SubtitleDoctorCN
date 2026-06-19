# Review Workflow

SubtitleDoctorCN findings should move through a structured review queue rather than being accepted automatically.

## Step 1: Freeze the source

Record the subtitle checksum, media identifier, selected style profile, terminology dictionary version, and tool commit.

## Step 2: Run deterministic checks

Run timing, duration, reading-speed, line-length, and punctuation checks. Save the JSON report without editing it.

## Step 3: Classify findings

| Class | Examples | Default action |
|---|---|---|
| Blocking | invalid duration, corrupt timestamp order | fix before delivery |
| Review | overlap, high reading speed, long line | inspect in media context |
| Advisory | terminology or punctuation suggestion | editor decision |

## Step 4: Correct safely

Safe changes preserve timestamps and meaning. Examples include trimming spaces, normalizing line endings, and approved terminology corrections.

Changes to names, numbers, grammar, timing, or dialogue meaning require media review.

## Step 5: Re-run checks

Generate a second report after edits. Compare finding counts and ensure that corrections did not introduce new overlaps or speed problems.

## Step 6: Approval

Record the reviewer, date, unresolved findings, accepted exceptions, output checksum, and delivery profile.

## Exception record

Accepted exceptions should include cue number, rule identifier, reason, reviewer, and expiry condition when applicable.

## Audit artifacts

Keep the original subtitle, original report, corrected subtitle, final report, profile file, dictionary file, and approval record together.
