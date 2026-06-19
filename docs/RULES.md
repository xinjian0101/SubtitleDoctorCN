# Rule Reference

SubtitleDoctorCN separates timing rules, readability rules, typography rules, and language-review hints.

## Timing rules

### `overlap`

Raised when a cue begins before the previous cue ends. Overlaps may be intentional for multiple speakers, so the finding requires review.

### `duration`

Raised when cue duration is zero or negative.

## Readability rules

### `reading_speed`

Characters per second are calculated after whitespace removal:

```text
characters_per_second = compact_character_count / duration_seconds
```

The default threshold is 15 characters per second. Content category, audience, and screen size may justify a different threshold.

### `line_length`

Raised when a subtitle line exceeds the configured character count. The default is 22 characters per line.

## Typography rules

### `mixed_punctuation`

Flags lines that appear to mix Chinese and Western punctuation styles. This is a review hint, not an automatic error.

## Safe correction policy

Automatic correction should be limited to deterministic transformations that preserve meaning and timestamps. Suggested safe operations:

- Normalize line endings.
- Remove trailing spaces.
- Collapse repeated blank lines.
- Normalize selected punctuation when the chosen style is explicit.

The tool should not automatically rewrite names, grammar, or dialogue meaning without review.

## Rule-pack design

Future rule packs should declare an identifier, version, language, enabled rules, thresholds, terminology dictionaries, and whether each correction is advisory or deterministic.
