#!/usr/bin/env python3
"""Calculate transparent carrying-cost scenarios for a stale listing."""

import argparse
import json
import sys
from pathlib import Path


MONTHLY_FIELDS = (
    "mortgage_principal",
    "mortgage_interest",
    "property_tax",
    "insurance",
    "hoa_cdd",
    "utilities",
    "maintenance",
    "other_cash_costs",
)


def number(data, key, default=0.0):
    value = float(data.get(key, default))
    if value < 0:
        raise ValueError("{} cannot be negative".format(key))
    return value


def calculate(data):
    monthly = {key: number(data, key) for key in MONTHLY_FIELDS}
    equity = number(data, "net_equity")
    annual_rate = number(data, "annual_opportunity_rate")
    horizons = data.get("horizons_months", [1, 3, 6])
    if not horizons or any(int(months) <= 0 for months in horizons):
        raise ValueError("horizons_months must contain positive integers")

    principal = monthly["mortgage_principal"]
    cash_outflow = sum(monthly.values())
    operating_carry = cash_outflow - principal
    opportunity_cost = equity * annual_rate / 12.0
    economic_carry = operating_carry + opportunity_cost

    scenarios = []
    for raw_months in horizons:
        months = int(raw_months)
        scenarios.append(
            {
                "months": months,
                "cash_outflow": round(cash_outflow * months, 2),
                "principal_buildup": round(principal * months, 2),
                "operating_carry": round(operating_carry * months, 2),
                "opportunity_cost": round(opportunity_cost * months, 2),
                "economic_carry": round(economic_carry * months, 2),
            }
        )

    return {
        "monthly_inputs": {key: round(value, 2) for key, value in monthly.items()},
        "assumptions": {
            "net_equity": round(equity, 2),
            "annual_opportunity_rate": annual_rate,
            "note": "Opportunity cost is a scenario assumption, not a cash expense.",
        },
        "monthly_summary": {
            "cash_outflow": round(cash_outflow, 2),
            "principal_buildup": round(principal, 2),
            "operating_carry": round(operating_carry, 2),
            "opportunity_cost": round(opportunity_cost, 2),
            "economic_carry": round(economic_carry, 2),
        },
        "scenarios": scenarios,
        "exclusions": [
            "Market price changes, selling costs, repairs, and concessions are excluded.",
            "Mortgage principal is cash outflow but not economic carry because it builds equity.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--output", help="Optional output JSON path")
    args = parser.parse_args()

    try:
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
        result = calculate(data)
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
