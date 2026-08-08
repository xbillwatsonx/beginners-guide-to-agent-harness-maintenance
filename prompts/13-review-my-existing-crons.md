# Prompt: Review My Existing Crons

Copy this prompt into your agent chat.

---

Please review all existing scheduled jobs (cron jobs, timers, automated tasks) in my agent harness.

For each job, tell me:

1. **Name and ID:** What is this job called?
2. **Schedule:** When does it run?
3. **What it does:** What command or action does it perform?
4. **Is it report-only?** Does it only check and report, or does it change things?
5. **Last run status:** Did the last run succeed or fail?
6. **Is it still needed?** Based on what you know about my current setup, is this job still useful?
7. **Safety concern?** Does this job delete files, send messages, publish content, rotate credentials, or auto-upgrade software?

Flag any jobs that:
- Are failing repeatedly
- Are no longer needed
- Do things that should require approval (delete, publish, send, rotate, upgrade)
- Overlap with other jobs (run at the same time)
- Have no disable instruction

Do not change or disable any jobs. Just report what you find.
