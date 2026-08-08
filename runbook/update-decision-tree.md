# Update Decision Tree

Should you update your agent harness right now? Use this guide to decide.

## The Quick Test

Ask yourself three questions:

1. **Is there a security fix I am exposed to?** → Update soon (within days).
2. **Is there a bug fix for a problem I am actually experiencing?** → Update when convenient.
3. **Is there a new feature I need?** → Update when convenient.

If you answered "no" to all three, you can wait.

## The Full Decision Tree

```text
New version available
│
├─ Is it a security fix?
│  ├─ YES → Am I exposed to this vulnerability?
│  │  ├─ YES → Update within days
│  │  └─ NO  → Treat as normal update
│  └─ NO  → Continue
│
├─ Is it a major version bump? (e.g., 1.x → 2.0)
│  ├─ YES → Wait. Read the migration guide.
│  │  ├─ Do I have time to handle breaking changes?
│  │  │  ├─ YES → Plan a dedicated update window
│  │  │  └─ NO  → Wait until you do
│  │  └─ Are there known issues reported?
│  │     ├─ YES → Wait for a patch release
│  │     └─ NO  → Proceed with extra caution
│  └─ NO  → Continue
│
├─ Is the release less than 3 days old?
│  ├─ YES → Wait. Let early adopters find the bugs.
│  └─ NO  → Continue
│
├─ Am I more than 4 versions behind?
│  ├─ YES → Update in small steps. Do not leap.
│  │  └─ Read the release notes for each intermediate version.
│  └─ NO  → Continue
│
├─ Does this release have breaking changes?
│  ├─ YES → Read the migration guide. Plan extra time.
│  └─ NO  → Continue
│
├─ Do I have a current backup?
│  ├─ YES → Continue
│  └─ NO  → Create a backup first. Never update without one.
│
└─ Proceed with the safe update workflow:
    Baseline → Backup → Stop → Update → Start → Verify → (Rollback if needed)
```

## When to Wait

- The release is brand new (less than a few days old).
- It is a major version bump and you have not read the migration guide.
- You do not have a current backup.
- You do not have time to troubleshoot if something goes wrong.
- You are in the middle of important work that cannot be interrupted.
- The release notes mention breaking changes that affect your setup and you have not prepared for them.

## When to Update Soon

- Security fix for a vulnerability you are exposed to.
- Bug fix for a problem that is actively causing you trouble.
- You are on a version that is no longer supported.

## When to Update When Convenient

- New features you want.
- Performance improvements.
- General bug fixes that do not affect you directly.
- You are a few versions behind and want to catch up gradually.

## The Trailing-Edge Sweet Spot

Stay **3-7 days** behind the newest release for normal updates. This gives time for:

- Early bug reports to surface
- Quick patch releases (x.y.1, x.y.2) to land
- Community discussion to highlight known issues

For security fixes you are exposed to, update faster. For major version bumps, wait longer and plan carefully.
