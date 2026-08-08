# Prompt: Run Post-Update Smoke Test

Copy this prompt into your agent chat. Replace `<version>` with the version you just installed.

---

I just updated my agent harness to version `<version>`. Please run the standard post-update smoke test.

Check:

1. **Version number:** Confirm the running version matches `<version>`.
2. **Workspace access:** Can you read files in the workspace? Can you write a test file and delete it?
3. **Connected services:** Are chat, email, and other connected services reachable?
4. **Scheduled jobs:** Are all scheduled jobs still listed? Did the most recent runs succeed?
5. **Config integrity:** Compare current config to the pre-update baseline. Any unexpected changes?
6. **Recent logs:** Check the last 50 lines of logs. Any new errors or warnings?
7. **Basic commands:** Can you run your status, health, and probe commands successfully?
8. **Memory access:** Can you read and search the memory file?

Report each item as PASS or FAIL. If anything fails, stop and help me triage before I do anything else.

If everything passes, confirm: "Smoke test passed. Version `<version>` is running and healthy."
