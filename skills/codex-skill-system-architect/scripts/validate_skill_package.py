#!/usr/bin/env python3
"""Validate a Codex skill package for required files and core sections."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "Identity",
    "When To Use",
    "Required Inputs",
    "Operational Workflow",
    "Validation",
    "Output",
]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text()


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    skill_md = path / "SKILL.md"

    if not skill_md.exists():
        return [f"Missing required file: {skill_md}"]

    text = read_text(skill_md)

    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter.")

    frontmatter_match = re.match(r"---\n(.*?)\n---", text, re.DOTALL)
    if not frontmatter_match:
        errors.append("SKILL.md frontmatter is missing closing delimiter.")
    else:
        frontmatter = frontmatter_match.group(1)
        if not re.search(r"^name:\s*[-a-z0-9]+$", frontmatter, re.MULTILINE):
            errors.append("Frontmatter must include a lowercase hyphen-case name.")
        if not re.search(r"^description:\s*.+", frontmatter, re.MULTILINE):
            errors.append("Frontmatter must include a description.")

    headings = re.findall(r"^#{1,3}\s+(.+)$", text, re.MULTILINE)
    heading_text = "\n".join(headings).lower()
    for section in REQUIRED_SECTIONS:
        if section.lower() not in heading_text:
            errors.append(f"SKILL.md should include a section matching: {section}")

    if len(text.split()) < 250:
        errors.append("SKILL.md appears too short for a production-grade skill.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_path", type=Path)
    args = parser.parse_args()

    errors = validate_skill(args.skill_path)
    if errors:
        print("Skill package validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Skill package validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
