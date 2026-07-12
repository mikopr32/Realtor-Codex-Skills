#!/usr/bin/env python3
"""Aggregate public Realtor content benchmark rows from CSV."""

import argparse
import csv
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path


def number(value):
    if value in (None, ""):
        return None
    parsed = float(value)
    if parsed < 0:
        raise ValueError("metrics cannot be negative")
    return parsed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        with Path(args.input).open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        required = {"competitor_id", "platform", "post_url", "views_visible", "likes_visible", "comments_visible", "followers_observed", "hook_type", "pillar"}
        if not rows or not required.issubset(rows[0]):
            raise ValueError("CSV is empty or missing required columns")
        groups = defaultdict(list)
        for index, row in enumerate(rows, 2):
            if not row["competitor_id"] or not row["platform"] or not row["post_url"]:
                raise ValueError(f"row {index} requires competitor_id, platform and post_url")
            row["_views"] = number(row["views_visible"])
            row["_likes"] = number(row["likes_visible"])
            row["_comments"] = number(row["comments_visible"])
            row["_followers"] = number(row["followers_observed"])
            groups[(row["competitor_id"], row["platform"])].append(row)
        output = []
        for (competitor, platform), items in sorted(groups.items()):
            views = [x["_views"] for x in items if x["_views"] is not None]
            hooks = defaultdict(int)
            pillars = defaultdict(int)
            for item in items:
                hooks[item["hook_type"] or "unknown"] += 1
                pillars[item["pillar"] or "unknown"] += 1
            metrics = {
                "competitor_id": competitor,
                "platform": platform,
                "sample_size": len(items),
                "posts_with_visible_views": len(views),
                "median_visible_views": round(statistics.median(views), 4) if views else None,
                "hook_mix": dict(sorted(hooks.items())),
                "pillar_mix": dict(sorted(pillars.items())),
            }
            ratios = []
            interaction_rates = []
            for item in items:
                if item["_views"] is not None and item["_followers"] not in (None, 0):
                    ratios.append(item["_views"] / item["_followers"])
                if item["_views"] not in (None, 0) and item["_likes"] is not None and item["_comments"] is not None:
                    interaction_rates.append((item["_likes"] + item["_comments"]) / item["_views"])
            metrics["median_views_per_follower"] = round(statistics.median(ratios), 6) if ratios else None
            metrics["median_public_interaction_rate"] = round(statistics.median(interaction_rates), 6) if interaction_rates else None
            output.append(metrics)
        rendered = json.dumps({"row_count": len(rows), "group_count": len(output), "benchmarks": output}, indent=2, ensure_ascii=False) + "\n"
        if args.output:
            Path(args.output).write_text(rendered, encoding="utf-8")
        else:
            sys.stdout.write(rendered)
    except (OSError, ValueError, TypeError, csv.Error, statistics.StatisticsError) as exc:
        sys.stderr.write(f"error: {exc}\n")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
