# Prompt: Review Release Notes

Copy this prompt into your agent chat. Replace `<version>` with the version you are considering.

---

Here are the release notes for version `<version>`:

<paste the release notes here>

Please review these release notes and tell me:

1. **Breaking changes:** Are there any changes that remove or alter something my setup depends on? List each one and explain what I need to do about it.
2. **Config changes:** Do I need to add, remove, or change any config settings?
3. **New dependencies:** Does this version require a newer version of Node.js, Python, or any system package?
4. **Security fixes:** Is this a security update? Am I exposed to the vulnerability it fixes?
5. **Auth changes:** Are there any changes to how authentication or API keys work?
6. **Preflight checks:** What should I verify before updating?
7. **Post-update tests:** What should I test after updating?
8. **Should I wait?** Is there anything in these notes that suggests I should wait for a patch release?

Base your answer on what you know about my current setup. If you are unsure about something, say so.
