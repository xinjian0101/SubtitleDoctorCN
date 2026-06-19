# Subtitle Review Checklist

This checklist is for manual review after the automated SRT scan.

## File checks

- [ ] The file opens correctly with UTF-8 encoding.
- [ ] Cue numbers are ordered.
- [ ] Every cue has a valid start and end time.
- [ ] No cue has zero or negative duration.
- [ ] The last cue stays within the video duration.

## Timing checks

- [ ] Overlap warnings were reviewed.
- [ ] Short cues can be read at normal playback speed.
- [ ] Long cues still match the spoken section.
- [ ] Cue boundaries follow complete phrases where possible.
- [ ] Dialogue changes remain clear.

## Readability checks

- [ ] CPS warnings were checked in context.
- [ ] Long lines were split at natural phrase boundaries.
- [ ] Mobile and vertical-video layouts were considered.
- [ ] Numbers and mixed-language text remain readable.
- [ ] Two-line subtitles have balanced lengths where possible.

## Language checks

- [ ] Names and technical terms were verified.
- [ ] Chinese and English punctuation are consistent.
- [ ] Simplified or traditional Chinese usage is consistent.
- [ ] Repeated filler words follow the project policy.
- [ ] Translation preserves meaning and tone.

## Visual checks

- [ ] Subtitles do not cover important picture content.
- [ ] Safe-area placement matches the target platform.
- [ ] Font size and contrast remain readable on a phone.
- [ ] Emphasis styles are consistent.

## Approval checks

- [ ] No unresolved blocking issue remains.
- [ ] Remaining warnings include reviewer notes.
- [ ] Final SRT, scan report, and style-profile version are archived.
- [ ] A reviewer watched the complete export once.

## Review record

```json
{
  "subtitle_file": "episode-01.srt",
  "style_profile": "mobile-cn-v1",
  "automated_report": "episode-01-report.json",
  "decision": "approved",
  "unresolved_warnings": [],
  "reviewed_at": "2026-06-19"
}
```