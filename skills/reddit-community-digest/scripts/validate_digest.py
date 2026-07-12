#!/usr/bin/env python3
"""Validate a Reddit community digest JSON before delivery."""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path


SORTS = {"top", "hot", "new", "rising", "controversial"}
PERIODS = {"hour", "day", "week", "month", "year", "all", None}
CONFIDENCE = {"High", "Moderate", "Limited"}


def iso(value, field):
    try:
        datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        raise ValueError("{} must be ISO-8601".format(field))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
        errors = []
        subreddit = data.get("subreddit", "")
        if not re.fullmatch(r"r/[A-Za-z0-9_]+", subreddit):
            errors.append("invalid subreddit")
        if data.get("sort") not in SORTS:
            errors.append("invalid sort")
        if data.get("time_window") not in PERIODS:
            errors.append("invalid time_window")
        if data.get("confidence") not in CONFIDENCE:
            errors.append("invalid confidence")
        try:
            iso(data.get("captured_at"), "captured_at")
        except ValueError as exc:
            errors.append(str(exc))
        requested = data.get("requested_count")
        if not isinstance(requested, int) or not 1 <= requested <= 25:
            errors.append("requested_count must be 1-25")
        posts = data.get("posts")
        if not isinstance(posts, list):
            errors.append("posts must be an array")
            posts = []
        if isinstance(requested, int) and len(posts) > requested:
            errors.append("post count exceeds requested_count")
        ranks, links = [], []
        for index, post in enumerate(posts, start=1):
            rank = post.get("rank")
            ranks.append(rank)
            link = post.get("permalink")
            links.append(link)
            if rank != index:
                errors.append("ranks must be sequential from 1")
            if not post.get("title") or not post.get("summary"):
                errors.append("post {} missing title or summary".format(index))
            if not isinstance(link, str) or "reddit.com/r/" not in link:
                errors.append("post {} lacks canonical Reddit link".format(index))
            if post.get("score_is_approximate") and post.get("approximate_score") is None:
                errors.append("post {} approximate score missing numeric estimate".format(index))
            if str(post.get("displayed_score", "")).lower() == "hidden" and post.get("approximate_score") is not None:
                errors.append("post {} hidden score cannot have numeric estimate".format(index))
            if post.get("published_at"):
                try:
                    iso(post.get("published_at"), "published_at")
                except ValueError as exc:
                    errors.append("post {} {}".format(index, exc))
        if len(set(links)) != len(links):
            errors.append("duplicate permalinks")
        result = {"valid": not errors, "post_count": len(posts), "errors": sorted(set(errors))}
        sys.stdout.write(json.dumps(result, indent=2) + "\n")
        return 0 if result["valid"] else 1
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        sys.stderr.write("error: {}\n".format(exc))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
