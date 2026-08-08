# Prompt: Run Preflight Checks

Copy this prompt into your agent chat. Replace `<version>` with the target version.

---

I am about to update my agent harness to version `<version>`. Please run the standard preflight checks for my setup.

Check:

1. **Current version:** What version am I running now?
2. **Agent responsiveness:** Can you respond to this prompt? (You just did, but confirm explicitly.)
3. **Disk space:** How much free space do I have? Is it above 20%?
4. **Backup freshness:** When was the last backup created? Is it recent enough to use?
5. **Stuck or looping jobs:** Are there any scheduled jobs that are stuck, looping, or repeatedly failing?
6. **Known issues:** Are there any known issues with version `<version>` that match my setup?
7. **No overlapping maintenance:** Is any other maintenance in progress (backups, reboots, other updates)?
8. **Access path:** If the agent goes down during the update, how will I access the system? (SSH, direct terminal, remote desktop?)

Report each item as PASS, WARN, or FAIL. If anything is WARN or FAIL, explain what I should do about it before proceeding.

Do not start the update. Just report the preflight results.
