# Prompt: Create Report-Only Health Check

Copy this prompt into your agent chat.

---

Help me create a report-only health check for my agent harness. This will be my first scheduled maintenance job.

The health check should verify:

1. **Agent is running:** The service or app is active.
2. **Workspace is accessible:** You can read and list files in the workspace.
3. **Basic commands work:** Status, health, and probe commands return success.
4. **Disk space is adequate:** At least 15% free.
5. **Memory is healthy:** Memory file exists, is readable, and is not bloated (under 100 KB or a reasonable threshold for my setup).
6. **Recent logs are clean:** No critical errors in the last hour of logs.

For each check, include:
- The exact command to run
- What output means PASS
- What output means FAIL

Format the output as a clear report:

```text
Health Check Report - <date and time>
[PASS] Agent is running
[PASS] Workspace accessible
[FAIL] Disk space: 8% free (WARNING: below 15% threshold)
...
Summary: 5/6 checks passed. 1 check failed.
```

This job must be report-only. It checks things and prints a report. It does not change anything.

Save the health check as a script or reusable instruction I can schedule as a cron job.
