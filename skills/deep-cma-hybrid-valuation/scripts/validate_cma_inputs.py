#!/usr/bin/env python3
"""Validate required intake fields for Deep CMA Hybrid Valuation Engine."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_FIELDS = [
    "address",
    "city",
    "state",
    "zip",
    "bedrooms",
    "bathrooms",
    "sqft",
    "year_built",
    "lot_size",
    "pool",
    "garage",
    "condition",
    "recent_improvements",
    "sold_comp_date_range",
    "zillow_link",
    "report_objective",
]

VALID_OBJECTIVES = {
    "listing price",
    "validar valor",
    "value validation",
    "estrategia de reduccion",
    "reduction strategy",
    "inversion",
    "investment",
    "seller presentation",
    "relaunch",
    "precio para listar",
}


def load_json(path: str) -> dict:
    with Path(path).open("r", encoding="utf-8") as f:
        return json.load(f)


def validate(payload: dict) -> dict:
    missing = []
    warnings = []

    for field in REQUIRED_FIELDS:
        value = payload.get(field)
        if value is None or value == "":
            missing.append(field)

    for numeric in ("bedrooms", "bathrooms", "sqft", "year_built"):
        value = payload.get(numeric)
        if value not in (None, ""):
            try:
                if float(value) <= 0:
                    warnings.append(f"{numeric} should be greater than zero")
            except (TypeError, ValueError):
                warnings.append(f"{numeric} should be numeric")

    objective = str(payload.get("report_objective", "")).strip().lower()
    if objective and objective not in VALID_OBJECTIVES:
        warnings.append("report_objective is not a standard objective; confirm wording")

    zillow_link = str(payload.get("zillow_link", "")).lower()
    if zillow_link and "zillow" not in zillow_link:
        warnings.append("zillow_link does not appear to be a Zillow URL")

    return {
        "valid": not missing,
        "missing_required_fields": missing,
        "warnings": warnings,
        "critical_question_count": min(len(missing), 5),
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_cma_inputs.py intake.json", file=sys.stderr)
        return 2

    result = validate(load_json(sys.argv[1]))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

