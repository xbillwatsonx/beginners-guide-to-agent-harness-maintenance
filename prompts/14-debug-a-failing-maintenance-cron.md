# Prompt: Debug a Failing Maintenance Cron

Copy this prompt into your agent chat. Replace `<job name>` with the failing job.

---

My maintenance cron job `<job name>` is failing. Here is what I know:

<describe what you see: error messages, when it started failing, what changed recently>

Please help me debug this:

1. **What is the exact error?** Parse any error messages in plain language.
2. **When did it start failing?** Check the run history. Was it working before?
3. **What changed?** Was there an update, config change, or environmental change around the time it started failing?
4. **Is it a real problem or a false alarm?** Is the check itself broken, or is it correctly reporting a real issue?
5. **How do I fix it?** If it is a real problem, what is the fix? If it is a false alarm, how do I adjust the check?
6. **Should I disable it temporarily?** If the fix will take time, should I disable the job to stop the noise?

Do not disable or change the job without my approval. Present your diagnosis and recommended fix, then wait for me to decide.
