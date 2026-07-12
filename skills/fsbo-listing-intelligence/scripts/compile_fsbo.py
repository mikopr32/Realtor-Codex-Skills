#!/usr/bin/env python3
"""Compile researched FSBO JSON into private, scored, reconciled CSV outputs."""

import argparse
import csv
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path


VERIFIED_REPRESENTATION = {"Verified_FSBO", "Probable_FSBO", "Flat_Fee_MLS_FSBO"}
FIELDS = [
    "Lead_ID", "Research_Priority_Score", "Priority_Band", "Verification_Status",
    "Address", "City", "State", "ZIP", "Price", "Property_Type", "Beds", "Baths",
    "Sqft", "Lot_Size", "Listing_Status", "Posted_Date", "Last_Updated",
    "Posted_Age_Days", "Visible_DOM", "Cumulative_Market_Time", "DOM_Confidence",
    "Representation_Type", "Public_Contact_Type", "Public_Contact_Value", "Primary_Source",
    "Primary_URL", "Additional_Source_URLs", "Buyer_Fit", "Opportunity_Signals",
    "Data_Quality_Flags", "Last_Verified", "Exclusion_Reason",
]


def safe(value):
    text = "" if value is None else str(value)
    return "'" + text if text.lstrip().startswith(("=", "+", "-", "@")) else text


def parse_day(value):
    if not value:
        return None
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").date()
    except ValueError:
        return None


def normalize_address(value):
    text = re.sub(r"[^a-z0-9 ]", " ", str(value or "").lower())
    words = {"street": "st", "avenue": "ave", "road": "rd", "drive": "dr", "court": "ct", "boulevard": "blvd"}
    return " ".join(words.get(token, token) for token in text.split())


def score(item, as_of):
    rep = item.get("representation_type")
    status = item.get("listing_status")
    points = 0
    reasons = []
    verification = 25 if rep == "Verified_FSBO" and status == "Active" else 15 if rep == "Probable_FSBO" and status == "Active" else 10 if rep == "Flat_Fee_MLS_FSBO" and status == "Active" else 5 if rep == "Representation_Unknown" and status == "Active" else 0
    points += verification
    reasons.append("verification:{}".format(verification))
    updated = parse_day(item.get("last_updated")) or parse_day(item.get("consulted_at"))
    age = None if updated is None else (as_of - updated).days
    freshness = 15 if age is not None and age <= 7 else 10 if age is not None and age <= 30 else 5 if age is not None and age <= 60 else 0
    points += freshness
    reasons.append("freshness:{}".format(freshness))
    fit = {"strong": 20, "partial": 10, "unknown": 5, "none": 0}.get(str(item.get("buyer_fit", "unknown")).lower(), 5)
    points += fit
    reasons.append("fit:{}".format(fit))
    signals = item.get("positioning_signals") or []
    positioning = min(15, len(signals) * 5)
    points += positioning
    reasons.append("positioning:{}".format(positioning))
    required = ["address", "price", "listing_status", "consulted_at", "source_url"]
    completeness = sum(bool(item.get(field)) for field in required)
    quality = 15 if completeness == len(required) else 8 if completeness >= 3 else 0
    points += quality
    reasons.append("quality:{}".format(quality))
    contact_type = item.get("public_contact_type")
    channel = 10 if contact_type in {"Phone", "Email", "Both", "Internal_Messaging_Only"} else 5 if contact_type else 0
    points += channel
    reasons.append("channel:{}".format(channel))
    points = min(100, max(0, points))
    band = "High" if points >= 80 else "Medium" if points >= 60 else "Monitor" if points >= 40 else "Low"
    return points, band, reasons, age


def exclude_reason(item):
    status = item.get("listing_status")
    rep = item.get("representation_type")
    if status != "Active":
        return "Status is {}".format(status or "Unknown")
    if rep not in VERIFIED_REPRESENTATION:
        return "Representation is {}".format(rep or "Unknown")
    return ""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="JSON array of researched listings")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--as-of", default=date.today().isoformat())
    args = parser.parse_args()
    try:
        as_of = datetime.strptime(args.as_of, "%Y-%m-%d").date()
        items = json.loads(Path(args.input).read_text(encoding="utf-8"))
        if not isinstance(items, list):
            raise ValueError("input JSON must be an array")
        out = Path(args.output_dir)
        out.mkdir(parents=True, exist_ok=True)
        masters = {}
        duplicate_count = 0
        for index, item in enumerate(items, start=1):
            if not isinstance(item, dict):
                raise ValueError("every JSON item must be an object")
            dedupe_key = normalize_address(item.get("address")) or "url:" + str(item.get("source_url", index))
            if dedupe_key in masters:
                duplicate_count += 1
                master = masters[dedupe_key]
                master.setdefault("additional_source_urls", []).append(item.get("source_url"))
                master.setdefault("positioning_signals", []).extend(item.get("positioning_signals") or [])
                master.setdefault("data_quality_flags", []).append("Duplicate source consolidated")
                master.setdefault("evidence", []).extend(item.get("evidence") or [])
            else:
                masters[dedupe_key] = dict(item)
        verified, excluded, ledger = [], [], []
        for index, item in enumerate(masters.values(), start=1):
            points, band, reasons, posted_age = score(item, as_of)
            reason = exclude_reason(item)
            row = {
                "Lead_ID": "FSBO-{:04d}".format(index),
                "Research_Priority_Score": points,
                "Priority_Band": band,
                "Verification_Status": item.get("representation_type", "Representation_Unknown"),
                "Address": item.get("address", ""), "City": item.get("city", ""),
                "State": item.get("state", ""), "ZIP": item.get("zip", ""),
                "Price": item.get("price", ""), "Property_Type": item.get("property_type", ""),
                "Beds": item.get("beds", ""), "Baths": item.get("baths", ""),
                "Sqft": item.get("sqft", ""), "Lot_Size": item.get("lot_size", ""),
                "Listing_Status": item.get("listing_status", "Unknown"),
                "Posted_Date": item.get("posted_date", ""), "Last_Updated": item.get("last_updated", ""),
                "Posted_Age_Days": posted_age if posted_age is not None else "",
                "Visible_DOM": item.get("visible_dom", ""),
                "Cumulative_Market_Time": item.get("cumulative_market_time", ""),
                "DOM_Confidence": item.get("dom_confidence", "Unknown"),
                "Representation_Type": item.get("representation_type", "Representation_Unknown"),
                "Public_Contact_Type": item.get("public_contact_type", ""),
                "Public_Contact_Value": item.get("public_contact_value", ""),
                "Primary_Source": item.get("source", ""), "Primary_URL": item.get("source_url", ""),
                "Additional_Source_URLs": " | ".join(filter(None, item.get("additional_source_urls") or [])),
                "Buyer_Fit": item.get("buyer_fit", "unknown"),
                "Opportunity_Signals": "; ".join(dict.fromkeys(item.get("positioning_signals") or [])),
                "Data_Quality_Flags": "; ".join(dict.fromkeys(item.get("data_quality_flags") or [])),
                "Last_Verified": item.get("consulted_at", ""),
                "Exclusion_Reason": reason,
            }
            (excluded if reason else verified).append(row)
            for evidence in item.get("evidence") or []:
                ledger.append({
                    "Lead_ID": row["Lead_ID"], "Address": row["Address"],
                    "Field": evidence.get("field", ""), "Value": evidence.get("value", ""),
                    "Source_URL": evidence.get("source_url", item.get("source_url", "")),
                    "Effective_Date": evidence.get("effective_date", ""),
                    "Consulted_At": item.get("consulted_at", ""),
                    "Confidence": evidence.get("confidence", ""),
                })
        verified.sort(key=lambda row: int(row["Research_Priority_Score"]), reverse=True)
        def write_csv(name, rows, fields):
            with (out / name).open("w", encoding="utf-8-sig", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                for row in rows:
                    writer.writerow({field: safe(row.get(field, "")) for field in fields})
        write_csv("FSBO_Verified_Leads.csv", verified, FIELDS)
        write_csv("FSBO_Excluded_Or_Unverified.csv", excluded, FIELDS)
        ledger_fields = ["Lead_ID", "Address", "Field", "Value", "Source_URL", "Effective_Date", "Consulted_At", "Confidence"]
        write_csv("FSBO_Source_Ledger.csv", ledger, ledger_fields)
        summary = {
            "as_of": as_of.isoformat(), "observations": len(items),
            "unique_properties": len(masters), "duplicates_consolidated": duplicate_count,
            "verified_active_fsbo": len(verified), "excluded_or_unverified": len(excluded),
            "priority_distribution": {band: sum(row["Priority_Band"] == band for row in verified) for band in ["High", "Medium", "Monitor", "Low"]},
            "privacy_note": "Public contact values are stored only in the private CSV and should not be exposed in chat.",
        }
        (out / "FSBO_Research_Summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
        sys.stdout.write(json.dumps(summary, indent=2) + "\n")
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        sys.stderr.write("error: {}\n".format(exc))
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
