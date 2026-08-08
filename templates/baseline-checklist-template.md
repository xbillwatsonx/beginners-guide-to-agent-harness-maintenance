# Baseline Checklist Template

Fill in the `<placeholders>` with your actual commands and paths. Run this checklist before every update.

```text
Pre-Update Baseline Checklist
Date: __________________
Harness: __________________
Current Version: __________________
Target Version: __________________

[ ] Agent process is running
    Command: <harness status command>
    Expected: "active" or "running"

[ ] Agent responds to a simple prompt
    Test: Ask "What version are you running?"

[ ] Workspace folder is readable
    Command: ls <workspace folder>

[ ] Config folder is readable
    Command: ls <config folder>

[ ] Disk space is above 20% free
    Command: df -h /

[ ] Backup exists and is recent
    Command: ls -lh <backup destination>
    Expected: File created within the last 24 hours

[ ] No stuck or looping jobs
    Command: <cron list command> + <cron history command>

[ ] Connected services are reachable
    Command: <channel probe command>

[ ] Scheduled jobs are listed and enabled
    Command: <cron list command>

[ ] Auth tokens are not expired
    Command: <auth check command>

[ ] Release notes reviewed for version <target version>
    Notes: _________________________________________________

[ ] Rollback plan is written and accessible
    Location: _________________________________________________

[ ] Access path confirmed (SSH, terminal, remote desktop)
    Method: _________________________________________________

[ ] No other maintenance in progress
    Verified: _________________________________________________

All checks passed: [ ] YES  [ ] NO (explain): __________________
Ready to update:    [ ] YES  [ ] NO (explain): __________________
```
