#!/usr/bin/env python3
"""Validate a Michael Cruz Coach content brief stored as JSON."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REQUIRED = (
    "mode",
    "objective",
    "audience_segment",
    "funnel_stage",
    "problem",
    "desired_shift",
    "promise",
    "platform",
    "format",
    "pillar",
    "offer",
    "cta",
    "primary_kpi",
    "editorial_lenses",
    "claims",
    "approval_status",
)

ALLOWED_MODES = {"piece", "campaign", "calendar", "repurpose", "audit", "optimize"}
ALLOWED_STATUS = {
    "verified",
    "provided_by_michael",
    "attributed_experience",
    "example",
    "hypothesis",
    "pending_verification",
}
NUMBERISH = re.compile(r"(?:[$%]\s*\d|\d[\d,.]*\s*(?:%|k|m|million|mil|mill[oó]n|casos?|leads?|citas?))", re.I)


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["The JSON root must be an object."]

    for key in REQUIRED:
        if key not in data:
            errors.append(f"Missing required field: {key}")

    mode = data.get("mode")
    if mode not in ALLOWED_MODES:
        errors.append(f"Invalid mode: {mode!r}. Allowed: {sorted(ALLOWED_MODES)}")

    for key in ("objective", "audience_segment", "funnel_stage", "problem", "desired_shift", "promise", "platform", "format", "pillar", "offer", "primary_kpi"):
        if key in data and not nonempty(data[key]):
            errors.append(f"Field must be a non-empty string: {key}")

    cta = data.get("cta")
    if not isinstance(cta, dict):
        errors.append("cta must be an object.")
    else:
        for key in ("type", "value", "destination"):
            if not nonempty(cta.get(key)):
                errors.append(f"cta.{key} must be a non-empty string.")

    lenses = data.get("editorial_lenses")
    if not isinstance(lenses, list) or "michael-ami" not in lenses:
        errors.append("editorial_lenses must be a list containing michael-ami.")
    elif len(lenses) > 4:
        errors.append("Use Michael/AMI plus at most three reference lenses.")

    claims = data.get("claims")
    if not isinstance(claims, list):
        errors.append("claims must be a list.")
    else:
        for index, claim in enumerate(claims):
            label = f"claims[{index}]"
            if not isinstance(claim, dict):
                errors.append(f"{label} must be an object.")
                continue
            text = claim.get("text")
            status = claim.get("status")
            source = claim.get("source")
            if not nonempty(text):
                errors.append(f"{label}.text must be a non-empty string.")
            if status not in ALLOWED_STATUS:
                errors.append(f"{label}.status is invalid: {status!r}")
            if status == "verified" and not nonempty(source):
                errors.append(f"{label}.source is required when status is verified.")
            if nonempty(text) and NUMBERISH.search(text) and status in {"example", "hypothesis", "pending_verification"}:
                # Numeric scenarios are allowed, but must remain visibly qualified downstream.
                pass

    if data.get("approval_status") != "draft":
        errors.append("approval_status must remain 'draft'; publication requires separate approval.")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_content_brief.py <brief.json>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERROR: File not found: {path}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"ERROR: Invalid JSON: {exc}", file=sys.stderr)
        return 2

    errors = validate(data)
    if errors:
        print("INVALID CONTENT BRIEF")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VALID CONTENT BRIEF")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
