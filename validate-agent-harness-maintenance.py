#!/usr/bin/env python3
"""Validate the beginner agent harness maintenance package."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_FILES = [
    ".gitignore",
    "AGENTS.md",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "justfile",
    "make-release-zip.py",
    "runbook/agent-harness-maintenance-runbook.md",
    "runbook/quick-start-card.md",
    "runbook/glossary.md",
    "runbook/update-decision-tree.md",
    "runbook/maintenance-crons.md",
]

REQUIRED_PROMPTS = [
    "prompts/01-audit-my-agent-harness.md",
    "prompts/02-build-my-update-plan.md",
    "prompts/03-review-release-notes.md",
    "prompts/04-create-rollback-plan.md",
    "prompts/05-run-preflight-checks.md",
    "prompts/06-guide-me-through-update.md",
    "prompts/07-run-post-update-smoke-test.md",
    "prompts/08-diagnose-failed-update.md",
    "prompts/09-create-maintenance-calendar.md",
    "prompts/10-turn-this-into-my-own-sop.md",
    "prompts/11-design-my-maintenance-crons.md",
    "prompts/12-create-report-only-health-check.md",
    "prompts/13-review-my-existing-crons.md",
    "prompts/14-debug-a-failing-maintenance-cron.md",
    "prompts/15-turn-a-manual-checklist-into-a-safe-cron.md",
]

REQUIRED_TEMPLATES = [
    "templates/baseline-checklist-template.md",
    "templates/backup-checklist-template.md",
    "templates/rollback-plan-template.md",
    "templates/smoke-test-template.md",
    "templates/update-log-template.md",
    "templates/maintenance-calendar-template.md",
    "templates/maintenance-cron-template.md",
    "templates/maintenance-report-template.md",
]

REQUIRED_STARTER_KIT = [
    "starter-kit/example-maintenance-calendar.md",
    "starter-kit/example-crontab.txt",
    "starter-kit/example-health-check-checklist.md",
    "starter-kit/example-update-log.md",
]

REQUIRED_EXAMPLES = [
    "examples/safe-update-plan.md",
    "examples/failed-update-triage.md",
    "examples/report-only-cron-summary.md",
]

LIMITED_HYGIENE_MARKERS = [
    "TODO",
    "FIXME",
    "PRIVATE_WORKSPACE_MARKER",
    "/home/xbill/.openclaw",
    "AGENTMAIL_API_KEY",
]

# Prompts may use a fenced block or the package's plain-text copy section.
PROMPT_CODE_BLOCK_INDICATOR = "```"
PROMPT_COPY_SECTION_INDICATORS = ("Copy this prompt into your agent chat", "\n---\n")


def label(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return path.name


def validate(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    all_required = (
        REQUIRED_FILES
        + REQUIRED_PROMPTS
        + REQUIRED_TEMPLATES
        + REQUIRED_STARTER_KIT
        + REQUIRED_EXAMPLES
    )

    for rel in all_required:
        if not (root / rel).is_file():
            errors.append(f"missing required file: {rel}")

    # Hygiene check: scan all markdown, text, and Python files for private markers.
    # Skip the validator and release builder themselves (they contain the marker list).
    skip_hygiene = {
        "validate-agent-harness-maintenance.py",
        "make-release-zip.py",
    }
    for path in root.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".txt", ".py"}:
            if path.name in skip_hygiene:
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                warnings.append(f"{label(path, root)}: could not read file for hygiene check")
                continue
            for marker in LIMITED_HYGIENE_MARKERS:
                if marker in text:
                    errors.append(f"{label(path, root)} contains limited-hygiene marker: {marker}")

    # Prompt files must contain a fenced block or the standard copy section.
    for rel in REQUIRED_PROMPTS:
        prompt_path = root / rel
        if prompt_path.is_file():
            try:
                text = prompt_path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                warnings.append(f"{rel}: could not read for code block check")
                continue
            has_fenced_block = PROMPT_CODE_BLOCK_INDICATOR in text
            has_copy_section = all(indicator in text for indicator in PROMPT_COPY_SECTION_INDICATORS)
            if not has_fenced_block and not has_copy_section:
                warnings.append(f"{rel}: no recognizable copy-paste prompt section found")

    # Runbook files should be non-trivial (at least 500 bytes)
    for rel in REQUIRED_FILES:
        file_path = root / rel
        if file_path.is_file() and file_path.suffix == ".md":
            size = file_path.stat().st_size
            if size < 500:
                warnings.append(f"{rel}: file is small ({size} bytes), may be incomplete")

    # Check that the justfile has standard recipes
    justfile_path = root / "justfile"
    if justfile_path.is_file():
        try:
            jf_text = justfile_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            warnings.append("justfile: could not read for recipe check")
        else:
            for recipe in ["help", "validate", "package", "agent-preflight", "agent-verify", "agent-status"]:
                if recipe not in jf_text:
                    warnings.append(f"justfile: missing standard recipe '{recipe}'")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate agent harness maintenance runbook package.")
    parser.add_argument("path", nargs="?", default=".", help="Package root to validate.")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    errors, warnings = validate(root)
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    if warnings:
        print("Validation passed with warnings:")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
