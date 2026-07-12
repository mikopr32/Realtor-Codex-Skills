#!/usr/bin/env python3
"""Inventory installed Codex skills and flag description overlap candidates."""

import argparse
import json
import re
import sys
from itertools import combinations
from pathlib import Path


STOP = {"a", "an", "and", "the", "to", "for", "of", "or", "when", "use", "usar", "para", "de", "y", "o", "la", "el", "los", "las", "que", "un", "una"}


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    start = text.find("---\n")
    if start < 0:
        heading = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
        paragraph = re.search(r"\n\n([^#\n][^\n]+)", text)
        return {
            "name": path.parent.name,
            "description": paragraph.group(1).strip() if paragraph else (heading.group(1).strip() if heading else "Legacy skill without frontmatter"),
        }
    end = text.find("\n---", start + 4)
    if end < 0:
        raise ValueError("unclosed frontmatter: {}".format(path))
    block = text[start + 4:end]
    values = {}
    for line in block.splitlines():
        match = re.match(r"^(name|description):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip('"').strip("'")
    return values


def tokens(text):
    return {word for word in re.findall(r"[a-z0-9áéíóúñ]+", text.lower()) if len(word) > 2 and word not in STOP}


def similarity(left, right):
    union = left | right
    return 0.0 if not union else len(left & right) / len(union)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-root", required=True)
    parser.add_argument("--threshold", type=float, default=0.35)
    args = parser.parse_args()
    try:
        if not 0 <= args.threshold <= 1:
            raise ValueError("threshold must be between 0 and 1")
        records = []
        errors = []
        for path in sorted(Path(args.skills_root).glob("*/SKILL.md")):
            try:
                meta = frontmatter(path)
                records.append({
                    "folder": path.parent.name,
                    "name": meta.get("name", path.parent.name),
                    "description": meta.get("description", ""),
                    "path": str(path),
                })
            except (OSError, ValueError) as exc:
                errors.append(str(exc))
        overlaps = []
        for left, right in combinations(records, 2):
            score = similarity(tokens(left["description"]), tokens(right["description"]))
            if score >= args.threshold:
                overlaps.append({"left": left["name"], "right": right["name"], "jaccard": round(score, 3), "note": "Review manually; lexical overlap is not proof of duplication."})
        overlaps.sort(key=lambda item: item["jaccard"], reverse=True)
        result = {"skill_count": len(records), "skills": records, "overlap_candidates": overlaps, "parse_errors": errors}
        sys.stdout.write(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
        return 0 if not errors else 1
    except (OSError, ValueError, TypeError) as exc:
        sys.stderr.write("error: {}\n".format(exc))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
