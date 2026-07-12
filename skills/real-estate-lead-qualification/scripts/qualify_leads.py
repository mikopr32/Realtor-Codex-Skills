#!/usr/bin/env python3
"""Normalize, score, and reconcile a complete real-estate lead CSV/TSV."""

import argparse
import csv
import json
import math
import re
import sys
from datetime import date, datetime
from pathlib import Path


ALIASES = {
    "Owner": ["owner", "owner name", "property owner", "ownername"],
    "PropertyAddress": ["address", "property address", "site address", "situs address", "propertyaddress"],
    "MailingAddress": ["mailing address", "mail address", "owner address", "mailingaddress"],
    "SaleDate": ["sale date", "purchase date", "last sale date", "recording date", "saledate"],
    "SalePrice": ["sale price", "purchase price", "last sale price", "amount", "saleprice"],
    "Phone": ["phone", "phone number", "mobile", "telephone", "cell"],
    "Email": ["email", "email address", "e-mail"],
    "CurrentValue": ["current value", "market value", "estimated value", "avm"],
    "MortgageBalance": ["mortgage balance", "loan balance", "estimated debt", "current loan amount"],
}

CANONICAL = [
    "Source_Row_ID", "Lead_Priority_Score", "Priority_Band", "Score_Reasons",
    "Contact_Type", "Owner", "PropertyAddress", "MailingAddress", "Phone", "Email",
    "SaleDate", "SalePrice", "Years_Owned", "Absentee_Indicator",
    "Estimated_Value_Low", "Estimated_Value_Base", "Estimated_Value_High",
    "Estimated_Debt_Low", "Estimated_Debt_Base", "Estimated_Debt_High",
    "Estimated_Equity_Dollars_Low", "Estimated_Equity_Dollars_Base", "Estimated_Equity_Dollars_High",
    "Estimated_Equity_Percent_Low", "Estimated_Equity_Percent_Base", "Estimated_Equity_Percent_High",
    "Equity_Method", "Equity_Confidence", "Duplicate_Flag", "Data_Quality_Flags",
]


def key(value):
    return re.sub(r"[^a-z0-9]", "", (value or "").strip().lower())


def safe_cell(value):
    text = "" if value is None else str(value)
    if text.lstrip().startswith(("=", "+", "-", "@")):
        return "'" + text
    return text


def parse_money(value):
    text = (value or "").strip()
    if not text:
        return None
    negative = text.startswith("(") and text.endswith(")")
    cleaned = re.sub(r"[^0-9.]", "", text)
    if not cleaned:
        return None
    number = float(cleaned)
    return -number if negative else number


def parse_date(value):
    text = (value or "").strip()
    if not text:
        return None
    formats = ("%Y-%m-%d", "%m/%d/%Y", "%m/%d/%y", "%Y/%m/%d", "%m-%d-%Y", "%Y%m%d")
    for fmt in formats:
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            pass
    return None


def normalize_phone(value):
    digits = re.sub(r"\D", "", value or "")
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    return digits if 10 <= len(digits) <= 15 else ""


def normalize_email(value):
    text = (value or "").strip().lower()
    return text if re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", text) else ""


def normalize_address(value):
    text = re.sub(r"[^a-z0-9# ]", " ", (value or "").lower())
    replacements = {
        "street": "st", "avenue": "ave", "road": "rd", "boulevard": "blvd",
        "drive": "dr", "lane": "ln", "court": "ct", "highway": "hwy",
        "apartment": "apt", "suite": "ste",
    }
    words = [replacements.get(word, word) for word in text.split()]
    return " ".join(words)


def amortized_balance(principal, annual_rate, term_years, years_elapsed):
    if principal <= 0 or years_elapsed >= term_years:
        return 0.0
    n = int(round(term_years * 12))
    k = max(0, min(n, int(math.floor(years_elapsed * 12))))
    r = annual_rate / 12.0
    if r == 0:
        return principal * (n - k) / n
    growth_n = (1 + r) ** n
    growth_k = (1 + r) ** k
    return principal * (growth_n - growth_k) / (growth_n - 1)


def map_columns(headers, overrides):
    normalized = {key(header): header for header in headers}
    result = {}
    ambiguities = []
    for canonical, aliases in ALIASES.items():
        if canonical in overrides:
            candidate = overrides[canonical]
            if candidate not in headers:
                raise ValueError("Mapped column '{}' does not exist".format(candidate))
            result[canonical] = candidate
            continue
        matches = []
        for alias in [canonical] + aliases:
            found = normalized.get(key(alias))
            if found and found not in matches:
                matches.append(found)
        if matches:
            result[canonical] = matches[0]
        if len(matches) > 1:
            ambiguities.append({"field": canonical, "matches": matches, "selected": matches[0]})
    return result, ambiguities


def score_lead(equity_pct, years, absentee, contact_type):
    score = 0
    reasons = []
    if equity_pct is not None:
        if equity_pct >= 0.60:
            points = 40
        elif equity_pct >= 0.40:
            points = 30
        elif equity_pct >= 0.20:
            points = 15
        else:
            points = 0
        score += points
        reasons.append("Equity:{}".format(points))
    else:
        reasons.append("Equity:NE")
    if years is None or years < 2:
        points = 0
    elif years < 7:
        points = 5
    elif years <= 10:
        points = 15
    elif years <= 15:
        points = 20
    else:
        points = 25
    score += points
    reasons.append("Tenure:{}".format(points))
    absentee_points = 20 if absentee == "Yes" else 10 if absentee == "Uncertain" else 0
    score += absentee_points
    reasons.append("Absentee:{}".format(absentee_points))
    contact_points = {"Both": 15, "Phone": 10, "Email": 8, "None": 0}[contact_type]
    score += contact_points
    reasons.append("Contact:{}".format(contact_points))
    score = min(100, max(0, score))
    band = "High" if score >= 75 else "Medium" if score >= 50 else "Low" if score >= 25 else "Nurture/Review"
    return score, band, "; ".join(reasons)


def round_or_blank(value, digits=2):
    return "" if value is None else round(value, digits)


def equity_scenarios(sale_price, years, current_value, balance):
    if current_value is not None and balance is not None:
        values = [current_value] * 3
        debts = [max(0.0, balance)] * 3
        method, confidence = "Verified/provided value and debt", "High"
    elif sale_price is not None and years is not None:
        appreciation = [0.02, 0.04, 0.06]
        ltvs = [0.90, 0.80, 0.70]
        rates = [0.07, 0.065, 0.06]
        values = [sale_price * ((1 + rate) ** years) for rate in appreciation]
        debts = [amortized_balance(sale_price * ltv, rate, 30, years) for ltv, rate in zip(ltvs, rates)]
        method, confidence = "Scenario model from sale price/date", "Low"
    else:
        return [None] * 3, [None] * 3, [None] * 3, [None] * 3, "Not evaluable", "Not evaluable"
    equity_dollars = [value - debt for value, debt in zip(values, debts)]
    equity_pct = [None if value <= 0 else equity / value for value, equity in zip(values, equity_dollars)]
    return values, debts, equity_dollars, equity_pct, method, confidence


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--as-of", default=date.today().isoformat())
    parser.add_argument("--column-map", help="JSON file mapping canonical names to source headers")
    args = parser.parse_args()
    try:
        as_of = datetime.strptime(args.as_of, "%Y-%m-%d").date()
        source = Path(args.input)
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        overrides = json.loads(Path(args.column_map).read_text(encoding="utf-8")) if args.column_map else {}
        sample = source.read_text(encoding="utf-8-sig")[:65536]
        dialect = csv.Sniffer().sniff(sample, delimiters=",\t;|")
        with source.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle, dialect=dialect)
            headers = reader.fieldnames or []
            mapping, ambiguities = map_columns(headers, overrides)
            raw_rows = list(reader)
        source_columns = ["Source_" + header if header in CANONICAL else header for header in headers]
        fieldnames = CANONICAL + [column for column in source_columns if column not in CANONICAL]
        processed = []
        seen = {}
        for index, raw in enumerate(raw_rows, start=2):
            get = lambda name: raw.get(mapping.get(name, ""), "")
            flags = []
            sale_date = parse_date(get("SaleDate"))
            if get("SaleDate") and sale_date is None:
                flags.append("InvalidSaleDate")
            if sale_date and sale_date > as_of:
                flags.append("FutureSaleDate")
                sale_date = None
            years = None if sale_date is None else (as_of - sale_date).days / 365.2425
            sale_price = parse_money(get("SalePrice"))
            current_value = parse_money(get("CurrentValue"))
            balance = parse_money(get("MortgageBalance"))
            if get("SalePrice") and sale_price is None:
                flags.append("InvalidSalePrice")
            phone = normalize_phone(get("Phone"))
            email = normalize_email(get("Email"))
            if get("Phone") and not phone:
                flags.append("InvalidPhone")
            if get("Email") and not email:
                flags.append("InvalidEmail")
            contact_type = "Both" if phone and email else "Phone" if phone else "Email" if email else "None"
            property_address = get("PropertyAddress").strip()
            mailing_address = get("MailingAddress").strip()
            norm_property = normalize_address(property_address)
            norm_mailing = normalize_address(mailing_address)
            absentee = "Uncertain" if not norm_property or not norm_mailing else "No" if norm_property == norm_mailing else "Yes"
            values, debts, eq_dollars, eq_pct, method, confidence = equity_scenarios(
                sale_price, years, current_value, balance
            )
            score, band, reasons = score_lead(eq_pct[1], years, absentee, contact_type)
            owner = get("Owner").strip()
            duplicate_key = "|".join([norm_property, key(owner), phone, email])
            duplicate = "No"
            if duplicate_key.strip("|") and duplicate_key in seen:
                duplicate = "Yes; matches row {}".format(seen[duplicate_key])
            elif duplicate_key.strip("|"):
                seen[duplicate_key] = index
            if not property_address:
                flags.append("MissingPropertyAddress")
            if contact_type == "None":
                flags.append("NoValidContact")
            row = {
                "Source_Row_ID": index,
                "Lead_Priority_Score": score,
                "Priority_Band": band,
                "Score_Reasons": reasons,
                "Contact_Type": contact_type,
                "Owner": owner,
                "PropertyAddress": property_address,
                "MailingAddress": mailing_address,
                "Phone": phone,
                "Email": email,
                "SaleDate": sale_date.isoformat() if sale_date else "",
                "SalePrice": round_or_blank(sale_price),
                "Years_Owned": round_or_blank(years, 3),
                "Absentee_Indicator": absentee,
                "Equity_Method": method,
                "Equity_Confidence": confidence,
                "Duplicate_Flag": duplicate,
                "Data_Quality_Flags": "; ".join(flags),
            }
            labels = ["Low", "Base", "High"]
            for i, label in enumerate(labels):
                row["Estimated_Value_{}".format(label)] = round_or_blank(values[i])
                row["Estimated_Debt_{}".format(label)] = round_or_blank(debts[i])
                row["Estimated_Equity_Dollars_{}".format(label)] = round_or_blank(eq_dollars[i])
                row["Estimated_Equity_Percent_{}".format(label)] = round_or_blank(eq_pct[i], 4)
            for header, out_header in zip(headers, source_columns):
                row[out_header] = raw.get(header, "")
            processed.append(row)
        contactable = [row for row in processed if row["Contact_Type"] != "None"]
        review = [row for row in processed if row["Contact_Type"] == "None"]
        def write_csv(path, rows):
            with path.open("w", encoding="utf-8-sig", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
                writer.writeheader()
                for row in rows:
                    writer.writerow({name: safe_cell(row.get(name, "")) for name in fieldnames})
        write_csv(output_dir / "Qualified_Contactable_Leads.csv", contactable)
        write_csv(output_dir / "Review_Or_Enrichment_Required.csv", review)
        summary = {
            "as_of": as_of.isoformat(),
            "input": source.name,
            "original_rows": len(processed),
            "contactable_rows": len(contactable),
            "review_rows": len(review),
            "reconciled": len(processed) == len(contactable) + len(review),
            "duplicate_rows_flagged": sum(row["Duplicate_Flag"] != "No" for row in processed),
            "equity_evaluable_rows": sum(row["Equity_Confidence"] != "Not evaluable" for row in processed),
            "priority_distribution": {band: sum(row["Priority_Band"] == band for row in processed) for band in ["High", "Medium", "Low", "Nurture/Review"]},
            "column_mapping": mapping,
            "mapping_ambiguities": ambiguities,
            "scenario_assumptions": {
                "appreciation_rates": [0.02, 0.04, 0.06],
                "original_ltvs": [0.90, 0.80, 0.70],
                "mortgage_rates": [0.07, 0.065, 0.06],
                "term_years": 30,
            },
        }
        (output_dir / "Processing_Summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
        sys.stdout.write(json.dumps(summary, indent=2) + "\n")
    except (OSError, ValueError, TypeError, json.JSONDecodeError, csv.Error) as exc:
        sys.stderr.write("error: {}\n".format(exc))
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
