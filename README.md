# Beginner's Guide to Agent Harness Maintenance

`beginners-guide-to-agent-harness-maintenance` helps non-technical users keep an AI agent harness updated, backed up, checked, and recoverable without needing to be a sysadmin.

An agent harness is the software, config, memory, and scheduled jobs that keep your AI agent running. Like any software, it needs maintenance: updates, backups, health checks, and a way to recover when something breaks.

This is not just an update guide. It is a maintenance guide. Updating is one chapter. The broader value is teaching you how to:

- know what must keep working
- back up important state
- inspect release notes
- update intentionally
- restart safely
- verify the system afterward
- roll back if needed
- set up report-only maintenance checks
- avoid silent drift in memory, context, cost, connectors, and scheduled jobs

This package is based on real maintenance workflows, but it is written for ordinary users who want practical help keeping their agent healthy.

## What This Does

This runbook gives you a lightweight maintenance layer for your agent harness:

1. A baseline checklist so you know what must still work after any change.
2. A safe update workflow: baseline → backup → update → restart → verify → rollback.
3. Report-only maintenance cron jobs that check health without changing anything, using cron as a thin scheduler rather than a container for the whole workflow.
4. Copy-paste prompts for asking your agent to audit, plan, and guide you through maintenance.
5. Templates for backups, rollback plans, smoke tests, update logs, and maintenance calendars.

## What Is Included

- [`runbook/agent-harness-maintenance-runbook.md`](runbook/agent-harness-maintenance-runbook.md) — full beginner-friendly guide.
- [`runbook/quick-start-card.md`](runbook/quick-start-card.md) — one-page starter flow.
- [`runbook/glossary.md`](runbook/glossary.md) — plain-language definitions.
- [`runbook/update-decision-tree.md`](runbook/update-decision-tree.md) — when to update and when to wait.
- [`runbook/maintenance-crons.md`](runbook/maintenance-crons.md) — safe scheduled maintenance jobs.
- `AGENTS.md` — editing and release rules for agents working in this package.
- `prompts/` — copy-paste prompts for walking an agent through maintenance setup.
- `templates/` — reusable templates for baselines, backups, rollback plans, smoke tests, update logs, maintenance calendars, cron jobs, and reports.
- `starter-kit/` — example maintenance calendar, crontab, health check checklist, and update log.
- `examples/` — worked examples of a safe update plan, failed update triage, and a report-only cron summary.
- [`validate-agent-harness-maintenance.py`](validate-agent-harness-maintenance.py) — dependency-free package checker.
- [`make-release-zip.py`](make-release-zip.py) — dependency-free release zip builder.
- [`CHANGELOG.md`](CHANGELOG.md) — package history.
- [`LICENSE`](LICENSE) — MIT License.

## Requirements

- Python 3.10 or newer.
- On Windows, use `python` if that is how Python is installed.
- On macOS/Linux, use `python3` if `python` is not available.
- `just` is optional. The included `justfile` is a convenience layer for POSIX-like shells and may need Git Bash, WSL, or another shell on Windows.
- No external Python packages are required.

## Quick Start

1. Open `runbook/quick-start-card.md`.
2. Copy the prompt from `prompts/01-audit-my-agent-harness.md` into your agent chat.
3. Let the agent inspect your current setup before it changes anything.
4. Continue through the prompt files in order.
5. Ask the agent to validate this package:

```bash
python3 validate-agent-harness-maintenance.py .
```

On Windows, this may be:

```powershell
python validate-agent-harness-maintenance.py .
```

If you have `just` installed, you can also run:

```bash
just agent-verify
```

To build the release zip without external `zip` tools:

```bash
python3 make-release-zip.py --version v0.1.0
```

On Windows, this may be:

```powershell
python make-release-zip.py --version v0.1.0
```

## Success Looks Like

You are done with the first setup when:

- you have a baseline checklist of what must keep working
- you have a backup plan and know how to restore
- you can update your harness safely with a rollback path
- you have a smoke test that runs after every update
- you have at least one report-only maintenance cron job
- you know how to review release notes before updating
- nothing destructive, publishing, or credential-changing is automated without review

## Safety Rule

This runbook does not ask your agent to delete files, publish content, send messages, expose credentials, or auto-upgrade core software without explicit approval.

Start manual. Turn checklists into report-only scheduled jobs. Add automation only after you trust the examples.

For harness-native schedulers, keep the scheduled payload to a tiny launcher such as `Run the <maintenance-skill> skill now.` Put the workflow in the reusable skill or task file, and deterministic commands in a helper script. For operating-system cron, schedule one tested script or command rather than embedding a long procedure in the crontab.

**Main beginner rule:** Manual first. Report-only second. Auto-fix much later.

## License

MIT. Use it, share it, adapt it, and improve it.
