# Scheduled Maintenance Jobs: Let Your Harness Check Itself

## The Core Rule

> **Cron is the alarm clock, not the brain.**

Cron owns *when* to run. The maintenance task owns *what* to do. The report owns *what happened*.

Keep the schedule line short. Put the actual steps in a reusable skill, task file, script, or checklist. Do not put long multi-step instructions directly inside a cron payload.

There are two common scheduler styles:

- **Operating-system cron:** schedule one tested script or command.
- **Harness-native scheduler:** use a tiny launcher such as `Run the <maintenance-skill> skill now.` The skill owns the workflow, and helper scripts own deterministic command logic.

## Safety Rules for Beginners

1. **Start with manual checklists.** Run them yourself first. Know what "good" looks like.
2. **Turn checklists into report-only scheduled jobs.** The job checks things and reports. It does not change anything.
3. **Keep the schedule line short.** One line. One script, command, or tiny skill launcher.
4. **Put the steps in a separate file.** A reusable skill, task file, script, or checklist. Not inside the cron payload.
5. **Never let beginner cron jobs:** delete files, send emails, publish content, rotate credentials, or auto-upgrade core software without explicit approval.
6. **Stagger your jobs.** Do not schedule backups, updates, and reboots at the same time.
7. **Always include a disable instruction.** Know how to turn the job off if it causes problems.

## Recommended Beginner-Safe Maintenance Jobs

### 1. Daily Harness Health Check

**What it checks:**
- Agent service or app is running
- Workspace folder is readable
- Basic status command works
- Disk space is not dangerously low (above 15% free)

**Frequency:** Daily, early morning (e.g., 7:00 AM)

**Cron line:**
```text
0 7 * * * <path to health check script>
```

**What the report looks like:**
```text
Health Check Report - 2026-07-14 07:00
[PASS] Agent service is running
[PASS] Workspace folder readable
[PASS] Status command returned OK
[PASS] Disk space: 45% free (92 GB available)
[PASS] Memory file size: 18 KB (healthy)
Summary: All checks passed.
```

### 2. Backup Freshness Check

**What it checks:**
- Latest backup file exists
- Backup is recent (created within your backup window)
- Backup has plausible size (not zero bytes, not suspiciously small)
- Backup file permissions are restricted

**Frequency:** Daily, after your backup window (e.g., 8:00 AM)

**Cron line:**
```text
0 8 * * * <path to backup check script>
```

### 3. Weekly Update Review

**What it checks:**
- Current version
- Latest available version
- Release notes summary
- Whether there are security fixes pending

**Frequency:** Weekly (e.g., Monday at 9:00 AM)

**Cron line:**
```text
0 9 * * 1 <path to update review script>
```

**Important:** This job is **report-only**. It tells you about available updates. It does not install them.

### 4. Weekly Memory/Context Review

**What it checks:**
- Memory file size (is it growing too large?)
- Stale entries (references to completed or abandoned projects)
- Conflicting instructions
- Outdated project references

**Frequency:** Weekly (e.g., Monday at 10:00 AM)

**Cron line:**
```text
0 10 * * 1 <path to memory review script>
```

**Important:** This job is **report-only**. It flags potential issues. It does not edit or delete memory.

### 5. Monthly Smoke Test

**What it checks:**
- Agent can read workspace rules
- Agent can find important folders
- Agent can run safe verification commands
- Agent can explain what changed recently

**Frequency:** Monthly (e.g., first Sunday at 8:00 AM)

**Cron line:**
```text
0 8 1-7 * 0 <path to smoke test script>
```

### 6. Spend/Provider Check

**What it checks:**
- Current default model and provider
- Fallback model paths
- Any surprise cost spikes
- Any model or provider changes since last check

**Frequency:** Weekly (e.g., Monday at 11:00 AM)

**Cron line:**
```text
0 11 * * 1 <path to spend check script>
```

### 7. Connector/Auth Check

**What it checks:**
- Connected services (email, chat, calendars, storage, code repos)
- Auth token status (expired? about to expire?)
- Any services that were connected but are now unreachable

**Frequency:** Weekly (e.g., Monday at 12:00 PM)

**Cron line:**
```text
0 12 * * 1 <path to connector check script>
```

### 8. Gateway/Public Exposure Check

**What it checks:**
- Control UI is not exposed to the public internet
- Authentication is enabled
- Only expected ports are open
- Local tunnel or VPN assumptions are documented

**Frequency:** Weekly (e.g., Monday at 1:00 PM)

**Cron line:**
```text
0 13 * * 1 <path to gateway check script>
```

### 9. Session/Job Watchdog

**What it checks:**
- Stuck sessions (active but not progressing)
- Looping jobs (repeated failures)
- Abandoned long-running tasks
- Repeated failure patterns

**Frequency:** Daily (e.g., 8:00 AM and 8:00 PM)

**Cron line:**
```text
0 8,20 * * * <path to watchdog script>
```

### 10. Monthly Cleanup Review

**What it checks:**
- Stale logs
- Old downloads
- Oversized caches
- Abandoned experiments
- Disk usage trends

**Frequency:** Monthly (e.g., first Saturday at 9:00 AM)

**Cron line:**
```text
0 9 1-7 * 6 <path to cleanup review script>
```

**Important:** This job is **report-only**. It lists what could be cleaned up. It does not delete anything.

### 11. Monthly Restore Drill

**What it checks:**
- Backups are usable, not just present
- Restore to a temporary location succeeds
- Restored files are intact and readable

**Frequency:** Monthly (e.g., first Saturday at 10:00 AM)

**Cron line:**
```text
0 10 1-7 * 6 <path to restore drill script>
```

**Important:** Restore to a **temporary location**, not over your live files. This is a drill, not a real restore.

## How to Build Your First Report-Only Cron Job

1. **Write the checklist manually.** Run it yourself a few times. Know what "pass" and "fail" look like.
2. **Choose the task container.** Use a simple shell/Python script for deterministic checks, or a reusable harness skill/task file when agent judgment is needed.
3. **Test the task manually.** Run the script or invoke the skill yourself. Confirm the output is clear and useful.
4. **Schedule a thin launcher.** Point operating-system cron at the tested script, or have the harness scheduler invoke the named skill with one short line.
5. **Check the first few runs.** Confirm the job runs on schedule and the output makes sense.
6. **Add more jobs one at a time.** Do not schedule 11 jobs on day one.

## Cron Syntax Quick Reference

```text
# ┌────────── minute (0-59)
# │ ┌──────── hour (0-23)
# │ │ ┌────── day of month (1-31)
# │ │ │ ┌──── month (1-12)
# │ │ │ │ ┌── day of week (0-7, 0=Sunday)
# │ │ │ │ │
# * * * * * command to run
```

Common schedules:

```text
0 7 * * *       Every day at 7:00 AM
0 7 * * 1       Every Monday at 7:00 AM
0 7 1 * *       First day of every month at 7:00 AM
0 7 1-7 * 0     First Sunday of every month at 7:00 AM
0 7 1-7 * 6     First Saturday of every month at 7:00 AM
0 8,20 * * *    Every day at 8:00 AM and 8:00 PM
*/15 * * * *    Every 15 minutes
0 */6 * * *     Every 6 hours
```

## How to Disable a Cron Job

**If you used `crontab -e`:**

Comment out the line with `#`:
```text
# 0 7 * * * /path/to/script.sh  # Disabled 2026-07-14 - investigating false alarms
```

**If you used a harness-specific scheduler:**

Use the harness command to disable the job:
```text
<harness cron disable command> <job name or ID>
```

Always include a note about why you disabled it and when.

## Staggering Example

Here is a safe weekly schedule with staggered jobs:

```text
# Monday - Review and planning (report-only)
0 9 * * 1  /path/to/update-review.sh       # Check for updates
0 10 * * 1 /path/to/memory-review.sh       # Review memory health
0 11 * * 1 /path/to/spend-check.sh         # Check costs
0 12 * * 1 /path/to/connector-check.sh     # Check connected services
0 13 * * 1 /path/to/gateway-check.sh       # Check public exposure

# Daily - Health and safety (report-only)
0 7 * * *   /path/to/health-check.sh       # Daily health check
0 8 * * *   /path/to/backup-check.sh       # Backup freshness
0 8,20 * * * /path/to/watchdog.sh          # Session/job watchdog

# Monthly - Deep checks (report-only)
0 9 1-7 * 6 /path/to/cleanup-review.sh     # First Saturday
0 10 1-7 * 6 /path/to/restore-drill.sh     # First Saturday
0 8 1-7 * 0 /path/to/smoke-test.sh         # First Sunday
```

Notice: no two jobs run at the same minute. Backups, updates, and reboots are not scheduled here at all. Every job is report-only.
