# Style Profiles

A style profile groups subtitle thresholds and typography choices for one delivery context.

## Profile fields

| Field | Type | Description |
|---|---|---|
| `profile_version` | integer | profile format version |
| `id` | string | stable profile identifier |
| `language` | string | primary language tag |
| `max_characters_per_line` | integer | line-length review threshold |
| `max_characters_per_second` | number | reading-speed threshold |
| `minimum_duration_ms` | integer | minimum cue duration |
| `maximum_lines` | integer | expected maximum visible lines |
| `punctuation_style` | string | selected typography style |
| `allow_intentional_overlap` | boolean | whether overlaps may be accepted after review |

## Suggested contexts

### Mobile short-form

- shorter lines;
- one or two lines;
- moderate reading speed;
- strong punctuation consistency;
- frequent review of rapid cuts.

### Long-form interview

- slightly longer lines;
- lower reading speed;
- terminology consistency;
- careful speaker-change handling.

### Bilingual captions

- separate language-specific limits;
- additional vertical-space checks;
- terminology dictionaries for names and brands;
- manual review of line pairing.

## Selection policy

Profiles should be selected by target platform, screen size, content type, and audience rather than by a single global default.

## Change control

A profile change should include before-and-after examples, a reason for each threshold change, reviewer approval, and a profile-version increment when behavior changes.
