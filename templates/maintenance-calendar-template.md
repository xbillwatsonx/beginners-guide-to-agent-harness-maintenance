# Maintenance Calendar Template

Fill in your preferred days and times. Stagger jobs so none overlap.

```text
# Maintenance Calendar for <harness name>

## Daily

| Time | Task | Type | Status |
|------|------|------|--------|
| 7:00 AM | Harness health check | Report-only | [ ] Active |
| 8:00 AM | Backup freshness check | Report-only | [ ] Active |
| 8:00 AM | Session/job watchdog | Report-only | [ ] Active |
| 8:00 PM | Session/job watchdog | Report-only | [ ] Active |

## Weekly (Monday)

| Time | Task | Type | Status |
|------|------|------|--------|
| 9:00 AM | Update review | Report-only | [ ] Active |
| 10:00 AM | Memory/context review | Report-only | [ ] Active |
| 11:00 AM | Spend/provider check | Report-only | [ ] Active |
| 12:00 PM | Connector/auth check | Report-only | [ ] Active |
| 1:00 PM | Gateway/exposure check | Report-only | [ ] Active |

## Monthly (First Saturday)

| Time | Task | Type | Status |
|------|------|------|--------|
| 9:00 AM | Cleanup review | Report-only | [ ] Active |
| 10:00 AM | Restore drill | Report-only | [ ] Active |

## Monthly (First Sunday)

| Time | Task | Type | Status |
|------|------|------|--------|
| 8:00 AM | Full smoke test | Report-only | [ ] Active |

## Update Cadence

| Task | Frequency | Last Done | Next Due |
|------|-----------|-----------|----------|
| Check for updates | Weekly | | |
| Apply updates | Bi-weekly or as needed | | |
| Full backup | Before every update | | |
| Restore drill | Monthly | | |
| SOP review | Monthly | | |

## Notes

- All scheduled jobs are report-only unless marked otherwise.
- No two jobs run at the same minute.
- Backups, updates, and reboots are not scheduled here.
- Review this calendar during monthly cleanup.
```
