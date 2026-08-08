# Backup Checklist Template

Fill in the `<placeholders>` with your actual paths. Use this to verify your backup before and after creation.

```text
Backup Checklist
Date: __________________
Backup File: __________________

Before Creating Backup:
[ ] Enough disk space for backup
    Command: df -h <backup destination>
[ ] Backup destination is writable
    Command: touch <backup destination>/test && rm <backup destination>/test

Creating Backup:
[ ] Backup command:
    <your backup command here>
[ ] Backup file created: [ ] YES  [ ] NO
[ ] Backup file size: __________________
[ ] Backup file permissions: __________________
    Expected: 600 (owner read/write only)

After Creating Backup:
[ ] Backup file exists
    Command: ls -lh <backup file path>
[ ] Backup file has plausible size (not zero, not suspiciously small)
    Size: __________________
[ ] Backup file permissions are restricted
    Command: ls -l <backup file path>
[ ] Backup file is recent (created within your backup window)
    Date: __________________
[ ] You can list the contents of the backup
    Command: tar -tzf <backup file path> | head -20

Restore Drill (Monthly):
[ ] Restore to temporary location succeeded
    Command: tar -xzf <backup file path> -C /tmp/restore-test
[ ] Restored files are intact and readable
    Command: ls -la /tmp/restore-test/
[ ] Cleanup test restore
    Command: rm -rf /tmp/restore-test

Backup verified: [ ] YES  [ ] NO (explain): __________________
```
