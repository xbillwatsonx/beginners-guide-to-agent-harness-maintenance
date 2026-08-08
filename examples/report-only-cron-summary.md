# Example: Report-Only Cron Summary

This is a worked example of what a week of report-only maintenance cron output looks like.

```text
========================================
Weekly Maintenance Summary
Week of: 2026-07-06 to 2026-07-12
Harness: MyAgent v2.3.1
========================================

## Daily Health Checks (7 runs)

All 7 runs passed (9/9 checks each).
- Disk space stable at ~45% free.
- Memory file grew from 18 KB to 19 KB (normal).
- No service interruptions detected.

## Backup Freshness Checks (7 runs)

All 7 runs passed.
- Backups created daily at 10:00 PM.
- All backups have plausible size (1.1-1.3 MB).
- Permissions correct (600) on all backups.

## Session/Job Watchdog (14 runs)

13 runs passed. 1 warning.

### Warning: 2026-07-09 20:00
- Job "nightly-cleanup" has failed 3 consecutive times.
- Error: "Permission denied: /var/log/myagent/"
- Action: Check permissions on /var/log/myagent/. May need sudo or user-level log path.

## Update Review (1 run - Monday)

[PASS] Current version: v2.3.1
[INFO] Latest version: v2.4.0 (released 2026-07-10)
[INFO] Release type: Feature release with new dependency
[INFO] Breaking changes: None listed
[INFO] Security fixes: None
[RECOMMENDATION] Wait 3-5 days for early bug reports, then update.

## Memory/Context Review (1 run - Monday)

[PASS] Memory file size: 19 KB (healthy, under 100 KB threshold)
[WARN] 3 entries reference completed project "old-side-project"
[WARN] 1 entry has a date from 2025 (may be stale)
[INFO] No conflicting instructions found.
[RECOMMENDATION] Review the 3 old-project entries during monthly cleanup.

## Spend/Provider Check (1 run - Monday)

[PASS] Default model: gpt-4 (unchanged)
[PASS] Fallback: claude-3 (unchanged)
[PASS] Weekly spend: $2.40 (within normal range)
[INFO] No surprise cost spikes detected.

## Connector/Auth Check (1 run - Monday)

[PASS] Gmail: connected, token valid (expires 2026-08-15)
[PASS] Discord: connected
[PASS] GitHub: connected
[WARN] Calendar: token expires in 7 days (2026-07-19)
[RECOMMENDATION] Refresh calendar OAuth token this week.

## Action Items for Next Week

- [ ] Investigate nightly-cleanup permission error.
- [ ] Refresh calendar OAuth token before July 19.
- [ ] Review v2.4.0 release notes and plan update for weekend.
- [ ] Review stale memory entries during monthly cleanup.

========================================
End of Weekly Summary
========================================
```
