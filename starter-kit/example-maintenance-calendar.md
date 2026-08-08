# Example Maintenance Calendar

This is a filled-in example of the maintenance calendar template. Replace the times and tasks with your own.

```text
# Maintenance Calendar for MyAgent

## Daily

| Time | Task | Type | Status |
|------|------|------|--------|
| 7:00 AM | Harness health check | Report-only | [x] Active |
| 8:00 AM | Backup freshness check | Report-only | [x] Active |
| 8:00 AM | Session/job watchdog | Report-only | [x] Active |
| 8:00 PM | Session/job watchdog | Report-only | [x] Active |

## Weekly (Monday)

| Time | Task | Type | Status |
|------|------|------|--------|
| 9:00 AM | Update review | Report-only | [x] Active |
| 10:00 AM | Memory/context review | Report-only | [x] Active |
| 11:00 AM | Spend/provider check | Report-only | [x] Active |
| 12:00 PM | Connector/auth check | Report-only | [x] Active |
| 1:00 PM | Gateway/exposure check | Report-only | [ ] Active |

## Monthly (First Saturday)

| Time | Task | Type | Status |
|------|------|------|--------|
| 9:00 AM | Cleanup review | Report-only | [x] Active |
| 10:00 AM | Restore drill | Report-only | [x] Active |

## Monthly (First Sunday)

| Time | Task | Type | Status |
|------|------|------|--------|
| 8:00 AM | Full smoke test | Report-only | [x] Active |

## Update Cadence

| Task | Frequency | Last Done | Next Due |
|------|-----------|-----------|----------|
| Check for updates | Weekly | 2026-07-13 | 2026-07-20 |
| Apply updates | Bi-weekly | 2026-07-06 | 2026-07-20 |
| Full backup | Before every update | 2026-07-06 | Before next update |
| Restore drill | Monthly | 2026-07-05 | 2026-08-02 |
| SOP review | Monthly | 2026-07-05 | 2026-08-02 |

## Notes

- All scheduled jobs are report-only.
- No two jobs run at the same minute.
- The gateway check is disabled because I do not expose a control UI.
- Review this calendar during monthly cleanup.
```
