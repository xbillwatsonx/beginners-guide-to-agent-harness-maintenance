# Quick Start Card

Use this when you have an AI agent running and want to keep it healthy without becoming a sysadmin.

## The Simple Setup

Ask your agent to build three things:

1. A baseline checklist of what must keep working.
2. A safe update workflow with backup and rollback.
3. At least one report-only maintenance check.

## Prompt Order

### Do Today

1. `prompts/01-audit-my-agent-harness.md` — audit your current setup
2. `prompts/02-build-my-update-plan.md` — build a safe update plan
3. `prompts/05-run-preflight-checks.md` — run preflight before any update
4. `prompts/07-run-post-update-smoke-test.md` — verify after updating

### When You Need Them

5. `prompts/03-review-release-notes.md` — review what changed before updating
6. `prompts/04-create-rollback-plan.md` — write your undo plan before updating
7. `prompts/06-guide-me-through-update.md` — step-by-step update guidance
8. `prompts/08-diagnose-failed-update.md` — triage a failed update
9. `prompts/09-create-maintenance-calendar.md` — schedule your checks
10. `prompts/10-turn-this-into-my-own-sop.md` — make it yours
11. `prompts/11-design-my-maintenance-crons.md` — automate report-only checks
12. `prompts/12-create-report-only-health-check.md` — your first cron job
13. `prompts/13-review-my-existing-crons.md` — audit existing scheduled jobs
14. `prompts/14-debug-a-failing-maintenance-cron.md` — fix a broken job
15. `prompts/15-turn-a-manual-checklist-into-a-safe-cron.md` — automate a checklist safely

## What To Tell The Agent First

```text
Please use this runbook to help me set up a maintenance system for my agent harness. Start by inspecting my current setup: what software I am running, how it is installed, what config and workspace files exist, and whether I have any scheduled jobs. Do not change files yet. First explain what you found and what maintenance layer you recommend.
```

## What Good Looks Like

- you know what "working" looks like before any change
- you have a backup and know how to restore it
- you can update your harness safely with a rollback path
- you have a smoke test that runs after every update
- you have at least one report-only maintenance cron job
- you know how to review release notes before updating
- your maintenance calendar has realistic days and times

## Safety Boundary

Do not ask the agent to automate updates, delete files, or change config on day one. Start manual. Turn checklists into report-only scheduled jobs. Add automation only after you trust the examples.

**Main beginner rule:** Manual first. Report-only second. Auto-fix much later.
