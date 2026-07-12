#!/usr/bin/env python3
"""Deterministic hybrid valuation calculations for structured CMA data."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import median


def money(value: float) -> float:
    return round(float(value), 2)


def compound_appreciation(last_sale_price: float, annual_rate: float, years: float) -> float:
    return money(last_sale_price * ((1 + annual_rate) ** years))


def simple_cumulative_appreciation(last_sale_price: float, cumulative_rate: float) -> float:
    return money(last_sale_price * (1 + cumulative_rate))


def weighted_average(items: list[dict], value_key: str, weight_key: str) -> float:
    total_weight = sum(float(item.get(weight_key, 0)) for item in items)
    if total_weight <= 0:
        raise ValueError("Total weight must be greater than zero")
    total = sum(float(item[value_key]) * float(item.get(weight_key, 0)) for item in items)
    return money(total / total_weight)


def cma_value(comps: list[dict]) -> dict:
    if not comps:
        raise ValueError("At least one comparable is required")

    adjusted_values = [float(comp["adjusted_value"]) for comp in comps]
    weighted = weighted_average(comps, "adjusted_value", "weight")
    return {
        "weighted_cma_value": weighted,
        "median_adjusted_value": money(median(adjusted_values)),
        "low_adjusted_value": money(min(adjusted_values)),
        "high_adjusted_value": money(max(adjusted_values)),
    }


def reconciled_value(cma: float, historical: float, cma_weight: float) -> dict:
    if cma_weight < 0 or cma_weight > 1:
        raise ValueError("cma_weight must be between 0 and 1")
    historical_weight = round(1 - cma_weight, 4)
    value = (float(cma) * cma_weight) + (float(historical) * historical_weight)
    return {
        "cma_weight": round(cma_weight, 4),
        "historical_weight": historical_weight,
        "reconciled_value": money(value),
    }


def run(payload: dict) -> dict:
    cma = cma_value(payload["comps"])

    hist_cfg = payload["historical_appreciation"]
    method = hist_cfg.get("method", "compound")
    if method == "compound":
        historical_value = compound_appreciation(
            hist_cfg["last_sale_price"],
            hist_cfg["annual_rate"],
            hist_cfg["years_elapsed"],
        )
    elif method == "simple_cumulative":
        historical_value = simple_cumulative_appreciation(
            hist_cfg["last_sale_price"],
            hist_cfg["cumulative_rate"],
        )
    else:
        raise ValueError("Unsupported historical appreciation method")

    rec = reconciled_value(
        cma["weighted_cma_value"],
        historical_value,
        float(payload.get("cma_weight", 0.70)),
    )

    return {
        "cma": cma,
        "historical_appreciation_value": historical_value,
        "reconciliation": rec,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json", help="Structured valuation input JSON")
    args = parser.parse_args()

    payload = json.loads(Path(args.input_json).read_text(encoding="utf-8"))
    print(json.dumps(run(payload), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
