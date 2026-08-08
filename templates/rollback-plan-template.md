# Rollback Plan Template

Fill in the `<placeholders>` with your actual commands and paths. Keep this accessible before every update.

```text
Rollback Plan
Harness: __________________
Current Version: __________________
Target Version: __________________
Date Prepared: __________________

Backup Location: <path to backup file>
Backup Date: __________________
Cloud Snapshot (if applicable): __________________

Step 1: Stop the Agent
    Command: <harness stop command>
    Expected: Service stopped, no errors
    Done: [ ]

Step 2: Restore Config and Workspace from Backup
    Command: tar -xzf <backup file path> -C <restore target directory>
    Expected: Files extracted without errors
    Done: [ ]

Step 3: Restart the Agent
    Command: <harness start command>
    Expected: Service started, status shows "active"
    Done: [ ]

Step 4: Verify the Restore
    [ ] Agent responds to a simple prompt
    [ ] Version number matches pre-update version
    [ ] Workspace files are intact
    [ ] Connected services are reachable
    [ ] Scheduled jobs are listed
    Done: [ ]

Step 5: If Restore Fails
    Fallback 1: Use older backup
        Location: __________________
    Fallback 2: Restore from cloud snapshot
        Provider: __________________
        Snapshot date: __________________
    Fallback 3: Reinstall from scratch
        Install guide: __________________

Rollback completed: [ ] YES  [ ] NO
Verification passed: [ ] YES  [ ] NO
Notes: _________________________________________________
```
