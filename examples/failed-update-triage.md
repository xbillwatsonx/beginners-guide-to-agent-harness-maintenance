# Example: Failed Update Triage

This is a worked example of diagnosing and recovering from a failed update.

```text
# Failed Update Triage - MyAgent v2.4.0

## What Happened

1. Updated MyAgent from v2.3.1 to v2.4.0 using `npm update -g myagent`
2. Restarted the service: `systemctl --user restart myagent`
3. Service failed to start. Status showed "failed".
4. Checked logs: `journalctl --user -u myagent -n 50`

## Error Message

```
Error: Cannot find module 'new-dependency'
Require stack:
- /usr/lib/node_modules/myagent/dist/server.js
```

## Diagnosis

The v2.4.0 release notes mentioned a new dependency (`new-dependency`), but the npm update did not install it automatically. This is a known issue with global npm packages when new dependencies are added.

## Decision: Roll Back

The fix requires manual dependency installation and possibly config changes. Since I need the agent working now, I will roll back and investigate the v2.4.0 migration later.

## Rollback Steps

1. Stop the service:
   systemctl --user stop myagent

2. Restore from backup:
   tar -xzf ~/backups/myagent-state-20260714-090000.tgz -C "$HOME"

3. Start the service:
   systemctl --user start myagent

4. Verify:
   myagent --version
   # Output: v2.3.1  ← Confirmed rolled back

5. Smoke test passed: 10/10

## Root Cause

- Did not fully read the release notes before updating.
- The release notes mentioned "new dependency: new-dependency" in the migration section.
- npm global installs do not always resolve new dependencies automatically.

## Prevention

- Add "Check for new dependencies in release notes" to the preflight checklist.
- For npm global installs, add `npm ls -g myagent --depth=0` to preflight to check current dependency tree.
- Consider using `npm install -g myagent` instead of `npm update -g myagent` for major version bumps.

## Next Steps

- [ ] Read the v2.4.0 migration guide fully.
- [ ] Test the update in a separate environment or at a low-stakes time.
- [ ] Update the preflight checklist with the new dependency check.
- [ ] Schedule the v2.4.0 update for a weekend when I have time to troubleshoot.
