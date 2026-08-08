# Example: Safe Update Plan

This is a worked example of a safe update plan for a fictional agent harness called "MyAgent" running as a systemd user service on Linux, installed via npm.

```text
# Safe Update Plan - MyAgent

## Harness Info
- Name: MyAgent
- Type: Local CLI agent, npm global install
- Service: myagent.service (systemd user)
- Config folder: ~/.myagent
- Workspace folder: ~/.myagent/workspace

## Current Version
Check with: myagent --version

## Update Command
npm update -g myagent

## Safe Update Flow

### 1. Baseline (Preflight)
myagent status
myagent --version
ls ~/.myagent/workspace
df -h /
ls -lh ~/backups/

### 2. Backup
ts=$(date -u +%Y%m%d-%H%M%S)
tar -czf "$HOME/backups/myagent-state-$ts.tgz" -C "$HOME" .myagent
chmod 600 "$HOME/backups/myagent-state-$ts.tgz"
ls -lh "$HOME/backups/myagent-state-$ts.tgz"

### 3. Stop
systemctl --user stop myagent
systemctl --user status myagent  # Confirm stopped

### 4. Update
npm update -g myagent

### 5. Start
systemctl --user start myagent
systemctl --user status myagent  # Confirm running

### 6. Verify (Smoke Test)
myagent --version                 # Confirm new version
myagent status                    # Confirm running
ls ~/.myagent/workspace           # Workspace readable
myagent channels status --probe   # Services reachable
myagent cron list                 # Jobs listed
journalctl --user -u myagent -n 20  # Check logs

### 7. Rollback (If Needed)
systemctl --user stop myagent
tar -xzf ~/backups/myagent-state-<timestamp>.tgz -C "$HOME"
systemctl --user start myagent
myagent --version  # Confirm rolled back to previous version
```

## Key Safety Points
- Restart from the terminal, not from inside the agent.
- Never skip the backup step.
- If the smoke test fails, roll back immediately. Debug later.
- Keep this plan in ~/.myagent/workspace/update-plan.md so the agent can reference it.
