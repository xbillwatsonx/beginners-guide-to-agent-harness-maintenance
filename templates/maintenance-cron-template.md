# Maintenance Cron Template

Use this template to design a single report-only maintenance cron job.

````text
# Job: <job name>

## Purpose
<One sentence describing what this job checks and why.>

## Schedule
Cron line: <cron expression>
Frequency: <daily / weekly / monthly>
Day and time: <e.g., Monday at 9:00 AM>
Launcher: <one tested script/command, or one tiny harness-native skill launcher>
Workflow home: <skill, task file, checklist, or helper script containing the real steps>

## Checks

1. <Check name>
   Command: <exact command>
   PASS: <what output means it passed>
   FAIL: <what output means it failed>

2. <Check name>
   Command: <exact command>
   PASS: <what output means it passed>
   FAIL: <what output means it failed>

## Expected Output

```text
<Job Name> Report - <date and time>
[PASS] <check 1 name>
[PASS] <check 2 name>
[FAIL] <check 3 name>: <reason>
...
Summary: X/Y checks passed. Z checks failed.
```

## Safety

- [ ] This job is report-only. It does not change any files, config, or state.
- [ ] This job does not delete, publish, send, rotate, or upgrade anything.
- [ ] This job has a disable instruction.

## Disable Instruction

To disable this job:
<command to disable or comment out the cron line>

## History

| Date | Status | Notes |
|------|--------|-------|
| | | |
````
