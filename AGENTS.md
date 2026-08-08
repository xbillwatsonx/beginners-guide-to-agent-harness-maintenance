# AGENTS.md - Agent Harness Maintenance Package

This package is a beginner-facing public runbook.

## Before Editing

Run:

```bash
just --list
just agent-preflight
```

Use the existing `justfile` recipes before raw shell commands when they fit. On systems without a POSIX-like shell, use the direct Python commands from `README.md`.

## Editing Rules

- Keep the language beginner-friendly.
- Keep examples generic and reusable. Use `<placeholder>` slots instead of specific harness commands.
- Do not add private workspace paths, secrets, account IDs, chat logs, or internal-only names.
- Do not make destructive, publishing, messaging, cron, or background automation steps part of the default flow.
- If you add a new required file, add it to `REQUIRED_FILES` in `validate-agent-harness-maintenance.py`.
- If you add a new prompt file, add it to `REQUIRED_PROMPTS` in the validator.
- If you add a new template, add it to `REQUIRED_TEMPLATES` in the validator.

## Verification

After edits, run:

```bash
just agent-verify
```

Before any public release, also do a human public-readiness review for:

- plain-language clarity
- no private details
- no unsupported automation claims
- no instructions that mark unreviewed work complete
- `python3 validate-agent-harness-maintenance.py .` or `python validate-agent-harness-maintenance.py .` passes
- `python3 make-release-zip.py --version <tag>` or `python make-release-zip.py --version <tag>` builds the archive
- the release tree is clean; the zip builder refuses dirty/untracked files by default
- the `.sha256` checksum file is uploaded with the zip asset

Do not publish, push, tag, or package a release unless the user explicitly asks.
