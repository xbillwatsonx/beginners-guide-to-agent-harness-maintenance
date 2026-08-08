# Agent Harness Maintenance Runbook

## Table of Contents

1. [What an Agent Harness Is](#1-what-an-agent-harness-is)
2. [What Can Break Over Time](#2-what-can-break-over-time)
3. [The Maintenance Mindset](#3-the-maintenance-mindset)
4. [Your Baseline: What Must Still Work](#4-your-baseline-what-must-still-work)
5. [Backups and Snapshots](#5-backups-and-snapshots)
6. [Update Planning](#6-update-planning)
7. [Release-Note Review](#7-release-note-review)
8. [Preflight Checks](#8-preflight-checks)
9. [Updating Safely](#9-updating-safely)
10. [Restarting Services or Apps](#10-restarting-services-or-apps)
11. [Post-Update Smoke Tests](#11-post-update-smoke-tests)
12. [Rollback and Recovery](#12-rollback-and-recovery)
13. [Maintenance Cron Jobs](#13-maintenance-cron-jobs)
14. [Monthly Cleanup and Drift Review](#14-monthly-cleanup-and-drift-review)
15. [Turning This Into Your Own SOP](#15-turning-this-into-your-own-sop)

---

## 1. What an Agent Harness Is

An agent harness is the collection of software, configuration, memory, and scheduled jobs that keep your AI agent running. It is not just the agent itself. It includes:

- The agent software (the program that runs your AI assistant)
- Configuration files (how the agent behaves, which models it uses, what tools it has)
- Memory and workspace files (what the agent knows about you and your projects)
- Scheduled jobs (cron jobs, timers, or automated tasks the agent runs)
- Connected services (email, chat, calendars, cloud storage, code repositories)
- The operating system and dependencies underneath

Think of it like a car. The agent is the driver. The harness is the engine, brakes, tires, fuel system, and dashboard. You do not need to be a mechanic, but you do need to know when to check the oil.

### Common Harness Types

| Type | Example | Where It Runs |
|------|---------|---------------|
| Local CLI agent | Installed via package manager or git clone | Your laptop or desktop |
| Desktop agent | Installed as a native app | Windows, macOS, or Linux desktop |
| WSL/Linux harness | Agent running inside Windows Subsystem for Linux | Windows with WSL |
| VPS/server harness | Agent running on a cloud virtual server | DigitalOcean, Vultr, Linode, etc. |
| Repo-based install | Agent cloned from GitHub and run from source | Any machine with git and the runtime |

Your harness type affects how you update, back up, and restart. The principles are the same. The commands differ.

---

## 2. What Can Break Over Time

Agent harnesses do not break all at once. They drift. Small problems accumulate until something stops working. Here is what to watch for:

### Silent Drift

- **Memory bloat:** Your agent's memory file grows too large. Old decisions, outdated project references, and duplicate notes pile up. The agent gets confused or slow.
- **Context pollution:** Workspace files accumulate stale instructions. The agent follows rules that no longer apply.
- **Config drift:** You change a setting to test something and forget to change it back. The agent behaves differently and you do not know why.

### Update Risks

- **Breaking changes:** A new version changes how something works. Your config, scripts, or automations stop working.
- **Dependency conflicts:** An update requires a newer version of something else. The install fails or the agent crashes.
- **Auth breakage:** An update resets or invalidates authentication tokens. Connected services stop working.

### Infrastructure Decay

- **Disk space:** Logs, caches, and old downloads fill up your disk. The agent cannot write files.
- **Service failures:** The agent's background process stops. Scheduled jobs stop running. You do not notice until you need it.
- **Credential expiry:** API keys, OAuth tokens, or service accounts expire. Integrations silently fail.

### Cost Surprises

- **Model changes:** A default model changes to a more expensive one. Your usage costs spike.
- **Fallback paths:** A free model becomes unavailable and the agent silently switches to a paid one.
- **Runaway jobs:** A scheduled task gets stuck in a loop. It burns through credits or API quota.

None of these are emergencies if you catch them early. That is what maintenance is for.

---

## 3. The Maintenance Mindset

Maintenance is not about fixing things when they break. It is about checking things before they break.

### The Three Levels

1. **Manual:** You run the checks yourself. You decide what to do with the results.
2. **Report-only:** A scheduled job runs the checks and shows you a report. You decide what to do.
3. **Auto-fix:** A scheduled job runs the checks and fixes problems automatically.

**Start at level 1. Stay at level 2 for a long time. Only move to level 3 for things you fully trust.**

### The Core Loop

```text
Baseline → Backup → Change → Verify → (Rollback if needed)
```

Every maintenance action follows this loop. Whether you are updating software, changing config, or cleaning up files, you:

1. Know what "working" looks like before you start.
2. Save a copy of the current state.
3. Make one change at a time.
4. Check that everything still works.
5. Have a way to undo the change if it does not.

### How Often?

| Task | Frequency |
|------|-----------|
| Harness health check | Daily (automated, report-only) |
| Backup freshness check | Daily (automated, report-only) |
| Update review | Weekly |
| Memory/context review | Weekly |
| Full smoke test | Monthly |
| Spend/provider check | Weekly |
| Connector/auth check | Weekly |
| Cleanup review | Monthly |
| Restore drill | Monthly |

You do not need to do all of these on day one. Start with a health check and a backup. Add more as you get comfortable.

---

## 4. Your Baseline: What Must Still Work

Before you change anything, you need to know what "working" looks like. This is your baseline.

### Building Your Baseline Checklist

Ask your agent:

```text
Help me build a baseline checklist for my agent harness. List everything that must still work after an update or config change. Include:
- the agent software itself (is it running? can it respond?)
- connected services (email, chat, calendars, storage, code repos)
- scheduled jobs (are they still scheduled? did the last run succeed?)
- workspace access (can the agent read and write its files?)
- basic commands (can the agent run its status, health, and probe commands?)
- disk space and memory usage
- any custom integrations I depend on

For each item, include the exact command or check I should run. Use <placeholder> slots for harness-specific commands so I can fill them in.
```

### Example Baseline Checklist

```text
[ ] Agent process is running: <harness status command>
[ ] Agent can respond to a simple prompt
[ ] Workspace folder is readable: ls <workspace folder>
[ ] Config folder is readable: ls <config folder>
[ ] Disk space is above 20% free: df -h /
[ ] Backup exists and is recent: ls -lh <backup destination>
[ ] Connected chat services are reachable: <channel probe command>
[ ] Scheduled jobs are listed and enabled: <cron list command>
[ ] Last scheduled job run succeeded: <cron history command>
[ ] Auth tokens are not expired: <auth check command>
```

Fill in the `<placeholders>` with your actual commands. Save this checklist. Run it before every update.

---

## 5. Backups and Snapshots

A backup is your undo button. Without one, a bad update means you start over.

### What to Back Up

At minimum:

- Your agent's config folder (all settings, credentials, and customizations)
- Your agent's workspace folder (memory, project files, task trackers)
- Your agent's data directory (sessions, logs, database if applicable)

If your agent runs on a cloud VPS, also take a provider snapshot before major updates.

### How to Back Up

**For local or WSL harnesses:**

```bash
# Create a timestamped backup
ts=$(date -u +%Y%m%d-%H%M%S)
tar -czf "$HOME/harness-backup-$ts.tgz" -C "$HOME" <config folder> <workspace folder>
chmod 600 "$HOME/harness-backup-$ts.tgz"
ls -lh "$HOME/harness-backup-$ts.tgz"
```

**For VPS/server harnesses:**

1. Take a cloud provider snapshot (DigitalOcean, Vultr, Linode all support this).
2. Also create a file-level backup of your config and workspace as above.

### Backup Checklist

```text
[ ] Backup file exists
[ ] Backup file has a plausible size (not zero bytes, not suspiciously small)
[ ] Backup file is recent (created today or within your backup window)
[ ] Backup file permissions are restricted (600 or similar)
[ ] You have tested restoring from a backup at least once
```

### How Often?

- Before every update: always.
- Weekly automated: if your provider supports it.
- After major config changes: always.

---

## 6. Update Planning

Do not update just because a new version exists. Update because you have a reason and a plan.

### The Update Decision Tree

See `runbook/update-decision-tree.md` for a visual guide. The short version:

1. **Check your current version:** `<harness version command>`
2. **Check the latest available version:** Look at the project's releases page or changelog.
3. **Read the release notes:** See [Section 7](#7-release-note-review).
4. **Decide:**

| Situation | Action |
|-----------|--------|
| Security fix for a vulnerability you are exposed to | Update soon (within days) |
| Bug fix for a problem you are experiencing | Update when convenient |
| New feature you need | Update when convenient |
| New feature you do not need | Wait |
| Major version bump with breaking changes | Wait, read migration guide, plan extra time |
| Release is less than a few days old | Wait for early bug reports to surface |
| You are many versions behind | Update in small steps, not one giant leap |

### The Trailing-Edge Strategy

Stay a few days to a week behind the newest release. This gives time for:

- Early adopters to find bugs
- Quick patch releases to land
- Community discussion to surface known issues

Small, frequent updates are boring. Waiting months makes updates scary. Aim for weekly or bi-weekly.

---

## 7. Release-Note Review

Release notes tell you what changed, what broke, and what you need to do about it. Read them before you update.

### What to Look For

1. **Breaking changes:** Words like "breaking," "removed," "deprecated," "migration required." These mean something you depend on might stop working.
2. **Security fixes:** Words like "security," "vulnerability," "CVE." These are the most important updates.
3. **Config changes:** New required settings, changed defaults, removed options.
4. **Dependency changes:** New requirements for Node.js, Python, or system packages.
5. **Auth changes:** Changes to how authentication or API keys work.

### How to Review with Your Agent

Copy this prompt into your agent chat:

```text
Here are the release notes for <harness name> version <version number>:

<paste release notes here>

Please review these release notes and tell me:
1. Are there any breaking changes that affect my setup?
2. Do I need to change any config files?
3. Are there new required dependencies?
4. Is this a security update I should prioritize?
5. What preflight checks should I run before updating?
6. What should I test after updating?
7. Is there anything in these notes that suggests I should wait?

Base your answer on what you know about my current setup. If you are unsure about something, say so.
```

---

## 8. Preflight Checks

Preflight checks are the things you verify before you start an update. They confirm your system is healthy enough to survive the update process.

### Standard Preflight Checklist

```text
[ ] Current version is known: <harness version command>
[ ] Agent is running and responsive
[ ] No stuck or looping jobs: <job list command>
[ ] Disk space is adequate (at least 20% free)
[ ] Backup is fresh (created in the last hour or day)
[ ] Release notes have been reviewed
[ ] Rollback plan is written (see Section 12)
[ ] You have a way to access the system if the agent goes down (SSH, direct terminal, remote desktop)
[ ] No other maintenance is in progress (backups, reboots, other updates)
[ ] You have 30-60 minutes of uninterrupted time
```

### Preflight Prompt

```text
I am about to update <harness name> from version <current> to version <target>. Please run through the standard preflight checklist for my setup. Check:
- current version
- agent responsiveness
- disk space
- backup freshness
- any stuck or looping jobs
- any known issues with version <target> that match my setup

Report any warnings or blockers. Do not start the update.
```

---

## 9. Updating Safely

The safe update flow is always the same:

```text
1. Baseline  →  Run your pre-update checks
2. Backup    →  Create a fresh backup
3. Stop      →  Stop the agent service or app
4. Update    →  Run the update command
5. Start     →  Restart the agent service or app
6. Verify    →  Run your smoke tests
7. Rollback  →  If verification fails, restore from backup
```

### Generic Update Commands

The exact commands depend on your harness type. Here are the patterns:

**Package manager install (npm, pip, brew, apt):**

```bash
<package manager> update <harness package>
# Example: npm update -g <harness package>
```

**Git clone install:**

```bash
cd <harness install directory>
git pull
<install command>
# Example: ./install.sh or npm install
```

**Desktop app:**

- Check for updates in the app menu
- Or download the latest installer from the project website
- Close the app, run the installer, reopen

**VPS/server (systemd service):**

```bash
<harness stop command>
# Example: systemctl --user stop <harness service>
<update command>
<harness start command>
# Example: systemctl --user start <harness service>
```

### The Golden Rule

**Restart from outside the agent.** If your agent manages its own service, do not ask it to restart itself during an update. Use a terminal, SSH, or the service manager directly.

---

## 10. Restarting Services or Apps

After an update, you need to restart the agent. How you restart depends on how it runs.

### Common Restart Methods

| Harness Type | Restart Command |
|-------------|-----------------|
| systemd user service | `systemctl --user restart <service name>` |
| systemd system service | `sudo systemctl restart <service name>` |
| Desktop app | Close and reopen the application |
| CLI (foreground) | Stop with Ctrl+C, then run the start command again |
| Docker container | `docker restart <container name>` |
| pm2 process | `pm2 restart <process name>` |

### After Restart

Wait 10-30 seconds. Then check:

```text
[ ] Service status shows "active" or "running": <service status command>
[ ] Agent responds to a simple prompt
[ ] No error messages in recent logs: <log check command>
[ ] Connected services are reachable: <channel probe command>
```

If the service does not start, check the logs before trying anything else:

```bash
<log command>
# Example: journalctl --user -u <service name> -n 50
```

---

## 11. Post-Update Smoke Tests

A smoke test is a quick check that the most important things still work. It is not exhaustive. It answers one question: "Is the system basically functional?"

### Standard Smoke Test

```text
[ ] Agent responds to a simple prompt
[ ] Agent can read its workspace files
[ ] Agent can write a test file (and deletes it after)
[ ] Agent can run its status/health command
[ ] Connected chat services are reachable
[ ] Scheduled jobs are still listed
[ ] Config values are unchanged (compare to baseline)
[ ] Version number matches the expected target
[ ] No new error messages in logs
```

### Smoke Test Prompt

```text
I just updated <harness name> to version <version>. Please run the standard post-update smoke test:
1. Confirm the version number.
2. Confirm you can read and write workspace files.
3. Confirm connected services are reachable.
4. Confirm scheduled jobs are still listed.
5. Check recent logs for errors.
6. Compare current config to the pre-update baseline.

Report pass/fail for each item. If anything fails, stop and help me triage before I do anything else.
```

---

## 12. Rollback and Recovery

If an update breaks something, you need to undo it. This is why you made a backup.

### Rollback Plan Template

Before every update, write down:

```text
Rollback Plan for <harness name> update to version <version>

1. Stop the agent: <stop command>
2. Restore from backup: <restore command>
3. Restart the agent: <start command>
4. Verify: <smoke test command>
5. If restore fails: <fallback plan>

Backup location: <path to backup file>
Backup date: <date and time>
```

### How to Restore

**From a tar backup:**

```bash
<harness stop command>
# Restore config and workspace
tar -xzf "$HOME/harness-backup-<timestamp>.tgz" -C "$HOME"
<harness start command>
```

**From a cloud provider snapshot:**

1. Power down the VPS.
2. Restore from the snapshot (via your provider's control panel).
3. Power on the VPS.
4. Verify the agent is running and responsive.

### If Rollback Fails

1. Do not panic. You have the backup file. The data is safe.
2. Check the error message. Is it a permissions problem? A disk space problem?
3. Try restoring to a different location first to confirm the backup is valid.
4. If the backup itself is corrupted, use the previous backup or the cloud snapshot.
5. Ask your agent for help: "My restore failed with this error: <error>. Help me diagnose it."

---

## 13. Maintenance Cron Jobs

Scheduled maintenance jobs let your harness check itself. The key rule:

> **Cron is the alarm clock, not the brain.**

Cron owns *when* to run. The maintenance task owns *what* to do. The report owns *what happened*. For a harness-native scheduler, use a tiny launcher that names the reusable maintenance skill or task. For operating-system cron, schedule one tested script or command.

### Safety Rules for Beginners

1. Start with manual checklists.
2. Turn checklists into report-only scheduled jobs.
3. Keep the schedule line short.
4. Put the actual steps in a reusable skill, task file, script, or checklist.
5. Do not put long multi-step instructions directly inside a cron payload.
6. Do not let beginner cron jobs delete files, send emails, publish content, rotate credentials, or auto-upgrade core software without explicit approval.
7. Stagger scheduled jobs so backups, updates, and reboots do not overlap.
8. Always include a disable/stop instruction.

### Recommended Beginner-Safe Maintenance Jobs

See `runbook/maintenance-crons.md` for detailed templates. Here is the summary:

| # | Job | Frequency | What It Does |
|---|-----|-----------|---------------|
| 1 | Daily harness health check | Daily | Confirms agent is running, workspace readable, disk not full |
| 2 | Backup freshness check | Daily | Confirms latest backup exists, is recent, has plausible size |
| 3 | Weekly update review | Weekly | Checks current vs available version, reviews release notes, reports only |
| 4 | Weekly memory/context review | Weekly | Checks for stale memory, bloat, conflicting instructions |
| 5 | Monthly smoke test | Monthly | Runs basic verification commands, confirms agent can read/write/respond |
| 6 | Spend/provider check | Weekly | Checks default model, fallback paths, surprise-spend risk |
| 7 | Connector/auth check | Weekly | Probes connected services, reports stale or broken auth |
| 8 | Gateway/public exposure check | Weekly | Confirms control UI not exposed, auth enabled, expected ports only |
| 9 | Session/job watchdog | Daily | Checks for stuck sessions, looping jobs, abandoned tasks |
| 10 | Monthly cleanup review | Monthly | Reports stale logs, old downloads, oversized caches (no deletion) |
| 11 | Monthly restore drill | Monthly | Confirms backups are usable, restores to temp location, records proof |

### Cron Syntax Quick Reference

```text
# ┌────────── minute (0-59)
# │ ┌──────── hour (0-23)
# │ │ ┌────── day of month (1-31)
# │ │ │ ┌──── month (1-12)
# │ │ │ │ ┌── day of week (0-7, 0=Sunday)
# │ │ │ │ │
# * * * * * command to run
```

Examples:

```text
0 7 * * *   # Every day at 7:00 AM
0 7 * * 1   # Every Monday at 7:00 AM
0 7 1 * *   # First day of every month at 7:00 AM
*/15 * * * * # Every 15 minutes
```

---

## 14. Monthly Cleanup and Drift Review

Once a month, take 30 minutes to review what has changed and clean up what has accumulated.

### Monthly Review Checklist

```text
[ ] Review the last month of update logs
[ ] Check current version against latest available
[ ] Review memory file for bloat, stale entries, contradictions
[ ] Review workspace for abandoned projects, old downloads, stale notes
[ ] Check disk usage: du -sh <workspace folder> <config folder>
[ ] Review scheduled jobs: are they all still needed? are they all succeeding?
[ ] Check connected services: any auth warnings? any unused connections?
[ ] Review spend: any cost surprises? any model changes?
[ ] Run a restore drill: confirm backups are usable
[ ] Update your baseline checklist if anything changed
```

### Cleanup Safety

- **Report first, delete later.** List what could be cleaned up. Do not delete anything until you review the list.
- **Check dependencies.** Before removing a folder or file, make sure nothing depends on it.
- **Keep the last few backups.** Do not delete your only backup.
- **Test after cleanup.** Run your smoke test to confirm nothing broke.

---

## 15. Turning This Into Your Own SOP

An SOP (Standard Operating Procedure) is your personal version of this runbook. It has your specific commands, your specific paths, and your specific schedule.

### How to Build Your SOP

Copy this prompt into your agent chat:

```text
Help me turn the Agent Harness Maintenance Runbook into my personal SOP. Use what you know about my setup to fill in the <placeholder> slots with my actual commands, paths, and service names.

Include:
1. My baseline checklist with real commands
2. My backup command with real paths
3. My update command for my specific harness type
4. My restart command
5. My smoke test with real checks
6. My rollback plan with real paths
7. My maintenance calendar with real days and times
8. My first report-only cron job

Save this as <my-sop-filename>. Keep it in my workspace where you can reference it before every update.
```

### Keeping It Current

Update your SOP when:

- You change your harness type (local to VPS, CLI to desktop)
- You add or remove connected services
- Your backup destination changes
- Your schedule changes
- You learn a better way to do something

Review your SOP during your monthly cleanup. If it is out of date, update it before you need it.

---

## Appendix: Placeholder Reference

Throughout this runbook, `<placeholder>` slots are used instead of specific commands. Fill these in for your harness:

| Placeholder | What It Means | Example |
|-------------|---------------|---------|
| `<harness status command>` | Command to check if the agent is running | `systemctl --user status my-agent` |
| `<harness version command>` | Command to check the current version | `my-agent --version` |
| `<harness stop command>` | Command to stop the agent | `systemctl --user stop my-agent` |
| `<harness start command>` | Command to start the agent | `systemctl --user start my-agent` |
| `<workspace folder>` | Path to the agent's workspace | `~/.my-agent/workspace` |
| `<config folder>` | Path to the agent's config | `~/.my-agent` |
| `<backup destination>` | Where backups are stored | `~/backups/` or a cloud folder |
| `<channel probe command>` | Command to check connected services | `my-agent channels status --probe` |
| `<cron list command>` | Command to list scheduled jobs | `my-agent cron list` |
| `<log command>` | Command to view recent logs | `journalctl --user -u my-agent -n 50` |
| `<service name>` | Name of the agent's systemd service | `my-agent.service` |
| `<harness package>` | Package name for package manager installs | `my-agent` |
| `<harness install directory>` | Where the agent is installed from source | `~/my-agent-install` |
