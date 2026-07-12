#!/usr/bin/env python3
"""Score Florida editorial candidates and select a category-diverse shortlist."""

import argparse
import json
import sys
from pathlib import Path


MAXIMA = {
    "decision_relevance": 20,
    "consumer_impact": 20,
    "local_specificity": 15,
    "verifiability": 15,
    "freshness": 10,
    "actionability": 10,
    "visual_potential": 5,
    "originality_opportunity": 5,
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--count", type=int, default=3)
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        if not 1 <= args.count <= 10:
            raise ValueError("count must be 1-10")
        stories = json.loads(Path(args.input).read_text(encoding="utf-8"))
        if not isinstance(stories, list):
            raise ValueError("input must be a JSON array")
        scored = []
        for index, story in enumerate(stories, start=1):
            if not isinstance(story, dict):
                raise ValueError("story {} must be an object".format(index))
            if not story.get("title") or not story.get("category") or not story.get("geography"):
                raise ValueError("story {} requires title, category and geography".format(index))
            components = {}
            for field, maximum in MAXIMA.items():
                value = float(story.get(field, 0))
                if value < 0 or value > maximum:
                    raise ValueError("story {} {} must be 0-{}".format(index, field, maximum))
                components[field] = value
            item = dict(story)
            item["score_components"] = components
            item["editorial_score"] = round(sum(components.values()), 2)
            item["selection_status"] = "Candidate"
            scored.append(item)
        scored.sort(key=lambda item: item["editorial_score"], reverse=True)
        selected = []
        used_categories = set()
        for story in scored:
            if len(selected) >= args.count:
                break
            if story["category"] not in used_categories:
                selected.append(story)
                used_categories.add(story["category"])
        if len(selected) < args.count:
            for story in scored:
                if len(selected) >= args.count:
                    break
                if story not in selected:
                    selected.append(story)
        selected_ids = {id(item) for item in selected}
        for item in scored:
            item["selection_status"] = "Selected" if id(item) in selected_ids else "Candidate"
        result = {
            "candidate_count": len(scored),
            "requested_selection_count": args.count,
            "selected_count": len(selected),
            "selected_categories": [item["category"] for item in selected],
            "selected_stories": selected,
            "ranked_candidates": scored,
            "method_note": "Scores support editorial judgment. Selection prefers category diversity, then fills remaining slots by score.",
        }
        rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
        if args.output:
            Path(args.output).write_text(rendered, encoding="utf-8")
        else:
            sys.stdout.write(rendered)
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        sys.stderr.write("error: {}\n".format(exc))
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
