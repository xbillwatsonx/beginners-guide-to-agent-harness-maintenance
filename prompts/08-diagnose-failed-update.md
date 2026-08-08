# Prompt: Diagnose Failed Update

Copy this prompt into your agent chat. Describe what went wrong.

---

My agent harness update failed. Here is what happened:

<describe what you did, what error you saw, and what is not working>

Please help me diagnose the problem:

1. **What is the exact error?** Parse the error message in plain language.
2. **What caused it?** Is this a known issue? A config problem? A dependency conflict? A permissions issue?
3. **Can it be fixed without rolling back?** If yes, what is the fix?
4. **Should I roll back?** If the fix is complex or uncertain, should I restore from backup instead?
5. **What is the rollback command?** Show me the exact command to restore from my most recent backup.
6. **How do I prevent this next time?** What preflight check would have caught this?

If you recommend rolling back, guide me through it step by step. If you recommend fixing forward, explain the fix clearly and wait for my approval before making changes.
