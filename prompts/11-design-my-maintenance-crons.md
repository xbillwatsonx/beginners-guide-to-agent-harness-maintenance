# Prompt: Design My Maintenance Crons

Copy this prompt into your agent chat.

---

Help me design a set of report-only maintenance cron jobs for my agent harness.

Based on what you know about my setup, recommend:

1. **Which jobs I need:** From the 11 recommended job types, which ones apply to my setup?
2. **Schedule for each job:** What day and time? Make sure no two jobs overlap.
3. **What each job checks:** The exact checks, in order.
4. **What "pass" and "fail" look like:** For each check, what output means it passed and what means it failed.
5. **The cron line:** The exact cron schedule line for each job.
6. **How to disable each job:** The exact command to turn it off if needed.

Rules:
- Every job must be report-only. No file deletion, no config changes, no auto-updates.
- Keep the cron line short. For operating-system cron, use one tested command or script path. For a harness-native scheduler, use a tiny launcher that invokes one named reusable skill or task.
- Put the real workflow in the skill, task file, or helper script, not in the scheduler payload.
- Stagger the times. No two jobs at the same minute.
- Start with 2-3 jobs. We can add more later.

Save the cron lines and job descriptions where I can review them before scheduling anything.
