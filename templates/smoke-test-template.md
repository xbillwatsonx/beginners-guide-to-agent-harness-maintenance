# Smoke Test Template

Fill in the `<placeholders>` with your actual commands. Run this after every update.

```text
Post-Update Smoke Test
Date: __________________
Harness: __________________
Previous Version: __________________
New Version: __________________

[ ] Version number matches target
    Command: <harness version command>
    Expected: <target version>
    Actual: __________________
    PASS / FAIL

[ ] Agent responds to a simple prompt
    Test: Ask "What version are you running?"
    PASS / FAIL

[ ] Workspace files are readable
    Command: ls <workspace folder>
    PASS / FAIL

[ ] Agent can write and delete a test file
    Command: touch <workspace folder>/smoke-test && rm <workspace folder>/smoke-test
    PASS / FAIL

[ ] Status/health command works
    Command: <harness status command>
    PASS / FAIL

[ ] Connected services are reachable
    Command: <channel probe command>
    PASS / FAIL

[ ] Scheduled jobs are listed
    Command: <cron list command>
    PASS / FAIL

[ ] Config values are unchanged from baseline
    Compare: <config diff command or manual review>
    PASS / FAIL

[ ] No new errors in recent logs
    Command: <log command>
    PASS / FAIL

[ ] Memory file is accessible
    Command: <memory read or search command>
    PASS / FAIL

Results: ___ / 10 passed
Smoke test: [ ] PASSED  [ ] FAILED

If FAILED, which checks failed and what is the plan?
_________________________________________________
_________________________________________________
```
