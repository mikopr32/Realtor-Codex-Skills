#!/usr/bin/env python3
"""Reproducible modeled lender and property-level DSCR calculations."""

import argparse
import json
import math
import sys
from pathlib import Path


def num(data, key, default=0.0, required=False):
    if required and key not in data:
        raise ValueError("missing required input: {}".format(key))
    value = float(data.get(key, default))
    if value < 0:
        raise ValueError("{} cannot be negative".format(key))
    return value


def payment_factor(annual_rate, years):
    n = int(round(years * 12))
    if n <= 0:
        raise ValueError("term_years must be positive")
    r = annual_rate / 12.0
    return 1.0 / n if r == 0 else r * (1 + r) ** n / ((1 + r) ** n - 1)


def classify(value, target):
    if value is None:
        return "Not evaluable"
    if value >= target + 0.10:
        return "Exceeds modeled target"
    if value >= target:
        return "Meets modeled target"
    if value >= target - 0.05:
        return "Near target"
    return "Below modeled target"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
        price = num(data, "purchase_price", required=True)
        rate = num(data, "annual_interest_rate", required=True)
        years = num(data, "term_years", required=True)
        target = num(data, "target_dscr", required=True)
        if target == 0:
            raise ValueError("target_dscr must be positive")
        if "loan_amount" in data:
            loan = num(data, "loan_amount")
        elif "down_payment_amount" in data:
            loan = max(0.0, price - num(data, "down_payment_amount"))
        elif "ltv" in data:
            ltv_input = num(data, "ltv")
            if ltv_input > 1:
                raise ValueError("ltv must be decimal between 0 and 1")
            loan = price * ltv_input
        else:
            raise ValueError("provide loan_amount, down_payment_amount, or ltv")
        if loan > price:
            raise ValueError("loan_amount cannot exceed purchase_price in this model")
        factor = payment_factor(rate, years)
        pi = loan * factor
        housing_keys = ["property_tax", "hazard_insurance", "flood_insurance", "hoa", "mortgage_insurance", "other_housing_costs"]
        housing_costs = {key: num(data, key) for key in housing_keys}
        non_pi_housing = sum(housing_costs.values())
        qualifying_expense = pi + non_pi_housing
        vacancy = num(data, "vacancy_rate")
        if vacancy > 1:
            raise ValueError("vacancy_rate must be between 0 and 1")
        other_income = num(data, "monthly_other_income")
        operating_keys = ["monthly_management", "monthly_maintenance", "monthly_capex", "monthly_leasing", "monthly_owner_utilities", "monthly_other_operating_expenses"]
        other_opex = sum(num(data, key) for key in operating_keys)
        fixed_property_opex = housing_costs["property_tax"] + housing_costs["hazard_insurance"] + housing_costs["flood_insurance"] + housing_costs["hoa"] + housing_costs["other_housing_costs"]
        scenarios = []
        rents = {label: data.get("rent_" + label) for label in ("low", "base", "high")}
        if not any(value is not None for value in rents.values()):
            raise ValueError("provide at least one rent_low, rent_base, or rent_high")
        for label, raw_rent in rents.items():
            if raw_rent is None:
                continue
            rent = float(raw_rent)
            if rent < 0:
                raise ValueError("rent_{} cannot be negative".format(label))
            lender_dscr = None if qualifying_expense == 0 else rent / qualifying_expense
            egi = rent * (1 - vacancy) + other_income
            monthly_noi = egi - fixed_property_opex - other_opex
            property_dscr = None if pi == 0 else monthly_noi / pi
            cash_flow = monthly_noi - pi
            scenarios.append({
                "scenario": label,
                "eligible_rent": round(rent, 2),
                "modeled_lender_dscr": None if lender_dscr is None else round(lender_dscr, 3),
                "target_result": classify(lender_dscr, target),
                "monthly_noi": round(monthly_noi, 2),
                "property_level_dscr": None if property_dscr is None else round(property_dscr, 3),
                "monthly_cash_flow": round(cash_flow, 2),
            })
        base_rent = float(data.get("rent_base", next(value for value in rents.values() if value is not None)))
        required_rent = target * qualifying_expense
        max_housing = base_rent / target
        max_pi = max(0.0, max_housing - non_pi_housing)
        max_loan = max_pi / factor if factor else 0.0
        current_ltv = 0.0 if price == 0 else loan / price
        max_price = None if current_ltv == 0 else max_loan / current_ltv
        result = {
            "inputs": {"purchase_price": price, "loan_amount": round(loan, 2), "ltv": round(current_ltv, 4), "annual_interest_rate": rate, "term_years": years, "target_dscr": target},
            "monthly_housing_expense": {"principal_and_interest": round(pi, 2), **{key: round(value, 2) for key, value in housing_costs.items()}, "total": round(qualifying_expense, 2)},
            "scenarios": scenarios,
            "reverse_dscr_using_base_rent": {
                "required_rent_at_current_payment": round(required_rent, 2),
                "maximum_qualifying_housing_expense": round(max_housing, 2),
                "maximum_principal_and_interest": round(max_pi, 2),
                "maximum_loan_amount": round(max_loan, 2),
                "dscr_constrained_maximum_price_at_current_ltv": None if max_price is None else round(max_price, 2),
            },
            "warnings": [
                "This is a modeled scenario, not lender approval.",
                "Confirm eligible rent, housing-expense components, product matrix, appraisal, insurance, and borrower requirements.",
                "The DSCR-constrained price is not market value or an offer recommendation.",
            ],
        }
        rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
        if args.output:
            Path(args.output).write_text(rendered, encoding="utf-8")
        else:
            sys.stdout.write(rendered)
    except (OSError, ValueError, TypeError, json.JSONDecodeError, StopIteration) as exc:
        sys.stderr.write("error: {}\n".format(exc))
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
