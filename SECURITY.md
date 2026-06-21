# Security Policy

## Supported versions

Security fixes are applied to the current `main` branch. Older snapshots and unsupported forks may not receive updates.

## Reporting a vulnerability

Do not publish confidential subtitles, unreleased dialogue, private media references, personal information, credentials, or working exploit details in a public issue.

Use GitHub private vulnerability reporting when available. If it is unavailable, open a minimal issue that identifies the affected commit and component without including sensitive content.

Include:

- affected commit;
- subtitle format and parser path;
- minimal synthetic fixture;
- operating system and Python version;
- impact summary;
- expected and actual behavior.

## Security boundaries

SubtitleDoctorCN reads local subtitle files and writes local reports or cleaned subtitle files. Users remain responsible for file permissions, output paths, source-media access, and editorial review.

Automatic cleanup is intentionally narrow and must not be treated as semantic sanitization.

## Out of scope

- confidential content posted publicly by users;
- security of unrelated media players;
- translation or transcription accuracy;
- unsupported local modifications;
- player-specific rendering defects without a project code path.

## Disclosure

Allow maintainers reasonable time to reproduce, correct, test, and document a confirmed issue before public disclosure.
