#!/usr/bin/env python3
"""Deterministic rental and flip underwriting from labeled JSON inputs."""

import argparse
import json
import sys
from pathlib import Path


def num(data, key, default=0.0):
    value = float(data.get(key, default))
    if value < 0:
        raise ValueError("{} cannot be negative".format(key))
    return value


def ratio(numerator, denominator):
    return None if denominator == 0 else round(numerator / denominator, 4)


def rental(data):
    price = num(data, "purchase_price")
    closing = num(data, "buy_closing_costs")
    rehab = num(data, "rehab")
    other_cash = num(data, "other_cash_invested")
    rent = num(data, "monthly_rent")
    other_income = num(data, "monthly_other_income")
    vacancy = num(data, "vacancy_rate")
    if vacancy > 1:
        raise ValueError("vacancy_rate must be between 0 and 1")
    monthly_expenses = num(data, "monthly_operating_expenses")
    debt = num(data, "monthly_debt_service")
    cash_invested = num(data, "cash_invested", price + closing + rehab + other_cash)
    gross = (rent + other_income) * 12
    effective_income = gross * (1 - vacancy)
    annual_expenses = monthly_expenses * 12
    noi = effective_income - annual_expenses
    annual_debt = debt * 12
    cash_flow = noi - annual_debt
    return {
        "strategy": "rental",
        "annual_gross_income": round(gross, 2),
        "annual_effective_income": round(effective_income, 2),
        "annual_operating_expenses": round(annual_expenses, 2),
        "noi": round(noi, 2),
        "annual_debt_service": round(annual_debt, 2),
        "annual_pre_tax_cash_flow": round(cash_flow, 2),
        "cap_rate": ratio(noi, price),
        "dscr": ratio(noi, annual_debt),
        "cash_on_cash": ratio(cash_flow, cash_invested),
        "cash_invested": round(cash_invested, 2),
    }


def flip(data):
    arv = num(data, "arv")
    rehab = num(data, "rehab")
    contingency_rate = num(data, "rehab_contingency_rate")
    if contingency_rate > 1:
        raise ValueError("rehab_contingency_rate must be between 0 and 1")
    buy_costs = num(data, "buy_closing_costs")
    financing = num(data, "financing_costs")
    holding = num(data, "holding_costs")
    fixed_sale = num(data, "fixed_selling_costs")
    selling_rate = num(data, "selling_cost_rate")
    if selling_rate > 1:
        raise ValueError("selling_cost_rate must be between 0 and 1")
    target_profit = num(data, "target_profit")
    purchase = num(data, "purchase_price")
    rehab_total = rehab * (1 + contingency_rate)
    sale_costs = fixed_sale + arv * selling_rate
    non_purchase_costs = rehab_total + buy_costs + financing + holding + sale_costs
    mao = arv - non_purchase_costs - target_profit
    total_cost = purchase + non_purchase_costs
    profit = arv - total_cost
    return {
        "strategy": "flip",
        "arv": round(arv, 2),
        "rehab_with_contingency": round(rehab_total, 2),
        "selling_costs": round(sale_costs, 2),
        "non_purchase_costs": round(non_purchase_costs, 2),
        "maximum_allowable_offer": round(mao, 2),
        "total_project_cost_at_input_price": round(total_cost, 2),
        "profit_at_input_price": round(profit, 2),
        "roi_on_total_cost": ratio(profit, total_cost),
        "margin_on_arv": ratio(profit, arv),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
        strategy = data.get("strategy")
        if strategy == "rental":
            result = rental(data)
        elif strategy == "flip":
            result = flip(data)
        else:
            raise ValueError("strategy must be 'rental' or 'flip'")
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
