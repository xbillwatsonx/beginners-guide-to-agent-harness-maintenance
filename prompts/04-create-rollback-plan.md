# Prompt: Create Rollback Plan

Copy this prompt into your agent chat.

---

Help me create a rollback plan for my agent harness. This is my undo button if an update goes wrong.

Include:

1. **Stop command:** How to stop the agent before restoring.
2. **Restore command:** The exact command to restore my config and workspace from the most recent backup.
3. **Start command:** How to restart the agent after restoring.
4. **Verification:** How to confirm the restore worked (smoke test commands).
5. **Fallback plan:** What to do if the restore itself fails (e.g., use an older backup, restore from cloud snapshot, reinstall from scratch).
6. **Backup location:** The exact path where my backups are stored.
7. **Last known good state:** The date and version of my last known working setup.

Use my actual paths, service names, and commands. Do not use placeholders.

Save this as a rollback plan I can reference during any update. I should be able to follow it step by step without thinking.
