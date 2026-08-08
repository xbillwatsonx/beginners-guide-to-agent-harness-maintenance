# Prompt: Guide Me Through Update

Copy this prompt into your agent chat. Replace `<version>` with the target version.

---

I am ready to update my agent harness to version `<version>`. Guide me through the safe update workflow step by step.

Use the safe update flow:

1. **Baseline:** Confirm preflight checks passed.
2. **Backup:** Show me the exact backup command to run. Wait for me to confirm it completed.
3. **Stop:** Show me the exact stop command. Wait for me to confirm the agent is stopped.
4. **Update:** Show me the exact update command. Wait for me to confirm it completed.
5. **Start:** Show me the exact start command. Wait for me to confirm the agent is running.
6. **Verify:** Run the post-update smoke test.

At each step:
- Show me the exact command to run.
- Wait for me to confirm the result before moving to the next step.
- If anything fails, stop and help me triage.

Do not skip steps. Do not assume a step succeeded unless I confirm it.
