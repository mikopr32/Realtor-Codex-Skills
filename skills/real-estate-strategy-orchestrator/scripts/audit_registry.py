#!/usr/bin/env python3
"""Audit a routing registry against installed Codex skill folders."""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", required=True)
    parser.add_argument("--skills-root", required=True)
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.registry).read_text(encoding="utf-8"))
        routes = data.get("routes")
        if not isinstance(routes, list):
            raise ValueError("registry must contain a routes array")
        installed = {path.parent.name for path in Path(args.skills_root).glob("*/SKILL.md")}
        intents = []
        referenced = []
        invalid = []
        for index, route in enumerate(routes, start=1):
            intent = route.get("intent")
            primary = route.get("primary")
            supports = route.get("supports", [])
            if not intent or not primary or not isinstance(supports, list):
                invalid.append(index)
                continue
            intents.append(intent)
            referenced.append(primary)
            referenced.extend(supports)
        duplicate_intents = sorted(name for name, count in Counter(intents).items() if count > 1)
        missing = sorted(set(referenced) - installed)
        unused_installed = sorted(installed - set(referenced))
        result = {
            "route_count": len(routes),
            "valid_route_count": len(routes) - len(invalid),
            "invalid_route_indexes": invalid,
            "duplicate_intents": duplicate_intents,
            "missing_referenced_skills": missing,
            "referenced_skill_count": len(set(referenced)),
            "installed_skill_count": len(installed),
            "installed_but_unreferenced": unused_installed,
            "valid": not invalid and not duplicate_intents and not missing,
        }
        sys.stdout.write(json.dumps(result, indent=2) + "\n")
        return 0 if result["valid"] else 1
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        sys.stderr.write("error: {}\n".format(exc))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
