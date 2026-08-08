# Glossary

Plain-language definitions for terms used in this runbook.

### Agent
An AI assistant that can read files, run commands, and respond to prompts. Your agent is the "driver." The harness is everything that keeps it running.

### Agent Harness
The collection of software, configuration, memory, and scheduled jobs that keep your AI agent running. Includes the agent program itself, its config files, its workspace, its connected services, and the operating system underneath.

### Auth / Authentication
The process of proving you are who you say you are. API keys, OAuth tokens, and passwords are all forms of authentication. When auth breaks, connected services stop working.

### Backup
A copy of your important files saved somewhere safe. A backup is your undo button. Without one, a bad update means you start over.

### Baseline
A documented list of what "working" looks like. You check your baseline before and after every change to confirm nothing broke.

### Breaking Change
A change in a new version that removes or alters something your setup depends on. Breaking changes require extra planning and often config updates.

### Config / Configuration
Files that control how your agent behaves: which model it uses, what tools it has access to, how it connects to services, and what rules it follows.

### Cron Job
A scheduled task that runs automatically at a specific time. "Cron" is the scheduler. The job is the task. Cron is the alarm clock, not the brain.

### Dependency
Software that your agent needs to run. Node.js, Python, system libraries, and other packages are dependencies. An update might require a newer version of a dependency.

### Drift
Small, gradual changes that accumulate over time. Memory bloat, config drift, and stale workspace files are all forms of drift. Drift causes problems slowly, not all at once.

### Harness
See Agent Harness.

### Health Check
A quick test that confirms the most important things are still working. A health check answers: "Is the system basically functional?"

### Preflight Check
Checks you run *before* an update to confirm your system is healthy enough to survive the update process.

### Release Notes
A document published with each new version that explains what changed, what broke, and what you need to do about it.

### Report-Only
A scheduled job that checks things and shows you a report, but does not change anything. You decide what to do with the results. This is the safest kind of automation.

### Restore
The process of putting your backup files back in place. A restore undoes a bad update or recovers from a failure.

### Rollback
The full process of undoing an update: stop the agent, restore from backup, restart, and verify. Your escape hatch.

### Service
A program that runs in the background. On Linux, services are often managed by systemd. Your agent might run as a service.

### Smoke Test
A quick set of checks after an update that confirms the most important things still work. Named after the practice of blowing smoke through pipes to find leaks.

### Snapshot
A full copy of a virtual server's disk at a point in time. Cloud providers like DigitalOcean and Vultr offer snapshots. A snapshot is the fastest way to roll back a VPS.

### SOP (Standard Operating Procedure)
Your personal version of this runbook. An SOP has your specific commands, paths, and schedule filled in.

### systemd
A service manager on Linux. systemd starts, stops, and monitors background services. Many agent harnesses run as systemd services.

### Trailing Edge
The strategy of staying a few days to a week behind the newest release. Gives time for bugs to surface and fixes to land before you update.

### Workspace
The folder where your agent stores its memory, project files, task trackers, and other working data. The workspace is separate from the agent software itself.
