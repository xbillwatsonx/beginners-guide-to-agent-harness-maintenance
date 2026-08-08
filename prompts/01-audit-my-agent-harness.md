# Prompt: Audit My Agent Harness

Copy this prompt into your agent chat. Replace `<harness name>` with the name of your agent software.

---

I want to set up a maintenance system for my agent harness. Before we change anything, please audit my current setup.

Tell me:

1. **What software am I running?** Name, version, how it was installed (package manager, git clone, desktop app, etc.).
2. **Where does it live?** Install directory, config folder, workspace folder.
3. **How does it run?** As a systemd service, a desktop app, a CLI process, a Docker container?
4. **What connected services does it have?** Email, chat, calendars, cloud storage, code repositories, APIs.
5. **What scheduled jobs exist?** List all cron jobs or timers. Include their schedule and what they do.
6. **What is the current state of memory?** Size, approximate age of oldest entries, any obvious bloat or contradictions.
7. **What is the disk usage?** Total disk space, free space, and the largest folders in the workspace.
8. **What backup system exists?** Is there a backup? When was the last one? Where is it stored?

Do not change any files. Do not create or modify cron jobs. Just report what you find.

After the audit, recommend the three most important maintenance actions I should take first.
