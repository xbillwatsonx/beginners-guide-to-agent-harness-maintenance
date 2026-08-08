# Example Health Check Checklist

This is a filled-in example of a health check. Replace the `<placeholders>` with your actual commands.

```text
Daily Health Check - <harness name>
Run: Every day at 7:00 AM
Type: Report-only

[ ] Agent process is running
    Command: <harness status command>
    Expected: "active" or "running"

[ ] Agent responds to a simple prompt
    Test: Ask "What is today's date?"

[ ] Workspace folder is readable
    Command: ls <workspace folder>

[ ] Config folder is readable
    Command: ls <config folder>

[ ] Disk space is above 15% free
    Command: df -h /
    Threshold: 15% free minimum

[ ] Memory file is healthy
    Command: ls -lh <workspace folder>/MEMORY.md
    Threshold: Under 100 KB

[ ] Recent logs are clean
    Command: <log command>
    Check: No critical errors in the last hour

[ ] Backup exists and is recent
    Command: ls -lh <backup destination>
    Expected: File created within the last 24 hours

[ ] Scheduled jobs are listed
    Command: <cron list command>

[ ] Last scheduled job run succeeded
    Command: <cron history command>

Expected output format:
```text
Health Check Report - 2026-07-14 07:00
[PASS] Agent is running
[PASS] Workspace accessible
[PASS] Config accessible
[PASS] Disk space: 45% free (92 GB available)
[PASS] Memory file: 18 KB (healthy)
[PASS] Logs clean: no errors in last hour
[PASS] Backup exists: created 2026-07-13 22:00 (1.2 MB)
[PASS] Scheduled jobs: 8 listed, 8 enabled
[PASS] Last job run: health-check succeeded at 2026-07-14 07:00
Summary: 9/9 checks passed.
```
```
