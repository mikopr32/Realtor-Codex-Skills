#!/usr/bin/env python3
"""Check teleprompter duration and optional segment timeline consistency."""

import argparse
import json
import re
import sys
from pathlib import Path


def word_count(text):
    return len(re.findall(r"\b[\wÀ-ÿ'-]+\b", text, flags=re.UNICODE))


def parse_clock(value):
    match = re.fullmatch(r"(?:(\d+):)?(\d+)(?:\.(\d+))?", str(value).strip())
    if not match:
        raise ValueError("invalid time '{}'".format(value))
    minutes = int(match.group(1) or 0)
    seconds = int(match.group(2))
    fraction = float("0." + (match.group(3) or "0"))
    return minutes * 60 + seconds + fraction


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--teleprompter", required=True, help="Plain-text teleprompter file")
    parser.add_argument("--wpm", type=float, default=150.0)
    parser.add_argument("--target-seconds", type=float)
    parser.add_argument("--timeline", help="Optional JSON array with start, end, audio")
    args = parser.parse_args()
    try:
        if args.wpm <= 0:
            raise ValueError("wpm must be positive")
        text = Path(args.teleprompter).read_text(encoding="utf-8")
        words = word_count(text)
        estimated = words / args.wpm * 60
        result = {
            "word_count": words,
            "wpm": args.wpm,
            "estimated_spoken_seconds": round(estimated, 2),
            "target_seconds": args.target_seconds,
            "target_delta_seconds": None if args.target_seconds is None else round(estimated - args.target_seconds, 2),
            "timeline": None,
            "warnings": [],
        }
        if args.target_seconds is not None and abs(estimated - args.target_seconds) > max(3, args.target_seconds * 0.12):
            result["warnings"].append("Teleprompter duration differs materially from target")
        if args.timeline:
            segments = json.loads(Path(args.timeline).read_text(encoding="utf-8"))
            if not isinstance(segments, list):
                raise ValueError("timeline must be a JSON array")
            previous_end = 0.0
            checks = []
            for index, segment in enumerate(segments, start=1):
                start = parse_clock(segment["start"])
                end = parse_clock(segment["end"])
                if end <= start:
                    raise ValueError("segment {} ends before it starts".format(index))
                gap = round(start - previous_end, 2)
                segment_words = word_count(segment.get("audio", ""))
                capacity = (end - start) * args.wpm / 60
                checks.append({
                    "segment": index, "start": start, "end": end,
                    "duration": round(end - start, 2), "gap_from_previous": gap,
                    "audio_words": segment_words, "word_capacity": round(capacity, 1),
                    "over_capacity": segment_words > capacity * 1.1,
                })
                if gap < 0:
                    result["warnings"].append("Timeline overlap before segment {}".format(index))
                if segment_words > capacity * 1.1:
                    result["warnings"].append("Audio is too dense in segment {}".format(index))
                previous_end = end
            result["timeline"] = {"total_seconds": previous_end, "segments": checks}
        sys.stdout.write(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        sys.stderr.write("error: {}\n".format(exc))
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
