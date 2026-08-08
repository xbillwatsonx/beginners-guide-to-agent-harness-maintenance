# Prompt: Turn a Manual Checklist Into a Safe Cron

Copy this prompt into your agent chat.

---

I have a manual maintenance checklist I run regularly. Help me turn it into a safe, report-only cron job.

Here is my checklist:

<paste your manual checklist here>

For each item in my checklist:

1. **Can it be automated safely?** If the check requires judgment (e.g., "review memory for contradictions"), it may need to stay manual or be simplified.
2. **What is the automated version?** The exact command or check that replaces the manual step.
3. **What does PASS look like?** The output that means this check passed.
4. **What does FAIL look like?** The output that means this check failed.

Rules:
- The cron job must be report-only. It checks and reports. It does not change anything.
- If a checklist item involves deleting, editing, publishing, or changing config, keep it manual.
- Format the output as a clear PASS/FAIL report.
- Include a summary line at the end.
- Provide the exact cron schedule line. If my harness has its own scheduler, keep its payload to a tiny launcher that invokes one named reusable skill or task.
- Put the real workflow in the skill, task file, or helper script, not in the scheduler payload.

After you design the automated version, show me both the original checklist and the automated version side by side so I can see what changed. Wait for my approval before we schedule anything.
