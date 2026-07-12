#!/usr/bin/env python3
"""Calculate observed ad longevity and aggregate abstract competitive patterns."""

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


FIELDS = ["Advertiser", "Ad_ID", "Status", "Start_Date", "Last_Verified", "Observed_Longevity_Days", "Longevity_Class", "Format", "Offer", "Hook_Type", "CTA", "Funnel", "Variants", "Ad_Library_URL", "Limitations"]


def day(value, required=False):
    if value in (None, ""):
        if required:
            raise ValueError("required date is missing")
        return None
    return datetime.strptime(str(value), "%Y-%m-%d").date()


def longevity_class(days):
    if days is None:
        return "Unknown"
    if days <= 7:
        return "New"
    if days <= 30:
        return "Short-running"
    if days <= 90:
        return "Established"
    return "Long-running"


def safe(value):
    text = "" if value is None else str(value)
    return "'" + text if text.lstrip().startswith(("=", "+", "-", "@")) else text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    try:
        ads = json.loads(Path(args.input).read_text(encoding="utf-8"))
        if not isinstance(ads, list):
            raise ValueError("input must be a JSON array")
        out = Path(args.output_dir)
        out.mkdir(parents=True, exist_ok=True)
        rows = []
        pattern_counts = defaultdict(Counter)
        advertiser_patterns = defaultdict(lambda: defaultdict(set))
        for ad in ads:
            start = day(ad.get("visible_start_date"))
            verified = day(ad.get("last_verified_date"), required=True)
            if start and start > verified:
                raise ValueError("visible_start_date cannot be after last_verified_date")
            days = None if start is None else (verified - start).days
            advertiser = str(ad.get("advertiser", "")).strip()
            if not advertiser or not ad.get("ad_library_url"):
                raise ValueError("advertiser and ad_library_url are required")
            row = {
                "Advertiser": advertiser, "Ad_ID": ad.get("ad_id", ""),
                "Status": ad.get("status", "Unknown"),
                "Start_Date": "" if start is None else start.isoformat(),
                "Last_Verified": verified.isoformat(),
                "Observed_Longevity_Days": "" if days is None else days,
                "Longevity_Class": longevity_class(days),
                "Format": ad.get("format", "Unknown"), "Offer": ad.get("offer", "Unknown"),
                "Hook_Type": ad.get("hook_type", "Unknown"), "CTA": ad.get("cta", "Unknown"),
                "Funnel": ad.get("funnel", "Unknown"), "Variants": int(ad.get("variants_observed", 0)),
                "Ad_Library_URL": ad.get("ad_library_url"),
                "Limitations": "; ".join(ad.get("limitations") or []),
            }
            rows.append(row)
            categories = {
                "offer": [ad.get("offer")], "format": [ad.get("format")],
                "hook_type": [ad.get("hook_type")], "cta": [ad.get("cta")],
                "funnel": [ad.get("funnel")],
                "visual": ad.get("visual_patterns") or [],
                "message": ad.get("message_patterns") or [],
            }
            for category, values in categories.items():
                for value in filter(None, values):
                    value = str(value)
                    pattern_counts[category][value] += 1
                    advertiser_patterns[category][value].add(advertiser)
        with (out / "Competitive_Ad_Table.csv").open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS)
            writer.writeheader()
            for row in rows:
                writer.writerow({field: safe(row.get(field, "")) for field in FIELDS})
        patterns = []
        for category, counter in pattern_counts.items():
            for pattern, count in counter.most_common():
                advertisers = len(advertiser_patterns[category][pattern])
                patterns.append({
                    "category": category, "pattern": pattern, "ad_frequency": count,
                    "advertiser_frequency": advertisers,
                    "classification": "Cross-advertiser pattern" if advertisers >= 2 else "Single-advertiser/isolated observation",
                })
        summary = {
            "ads_reviewed": len(rows),
            "advertisers_reviewed": len(set(row["Advertiser"] for row in rows)),
            "active_ads": sum(str(row["Status"]).lower() == "active" for row in rows),
            "long_running_ads": sum(row["Longevity_Class"] == "Long-running" for row in rows),
            "patterns": patterns,
            "confidence": "Limited" if len(rows) < 5 or len(set(row["Advertiser"] for row in rows)) < 2 else "Moderate",
            "interpretation_warning": "Observed longevity and pattern frequency do not prove spend, ROI, conversions, CPL, or lead quality.",
        }
        (out / "Competitive_Patterns.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        sys.stdout.write(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        sys.stderr.write("error: {}\n".format(exc))
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
