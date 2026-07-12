#!/usr/bin/env python3
"""Emit a JSON inventory of installed Codex skills without loading their bodies."""

import argparse
import json
import re
from pathlib import Path


FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
FIELD = re.compile(r"^(name|description):\s*(.*?)\s*$", re.MULTILINE)


def parse_skill(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    match = FRONTMATTER.search(text)
    values = dict(FIELD.findall(match.group(1))) if match else {}
    return {
        "folder": path.parent.name,
        "name": values.get("name"),
        "description": values.get("description"),
        "path": str(path),
        "valid_metadata": bool(values.get("name") and values.get("description")),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-root", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()

    root = Path(args.skills_root).expanduser().resolve()
    skills = [parse_skill(path) for path in sorted(root.glob("*/SKILL.md"))]
    names = {}
    for skill in skills:
        if skill["name"]:
            names.setdefault(skill["name"], []).append(skill["folder"])
    duplicates = {name: folders for name, folders in names.items() if len(folders) > 1}
    payload = {
        "skills_root": str(root),
        "skill_count": len(skills),
        "valid_metadata_count": sum(item["valid_metadata"] for item in skills),
        "duplicate_names": duplicates,
        "skills": skills,
    }
    rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 1 if duplicates else 0


if __name__ == "__main__":
    raise SystemExit(main())
