#!/usr/bin/env python3
"""Validate and rank verified growth-project records."""

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from urllib.parse import urlparse


MAXIMA = {
    "local_relevance": 20,
    "status_evidence": 20,
    "scale_materiality": 15,
    "real_estate_mechanism": 15,
    "timeline_clarity": 10,
    "source_quality": 10,
    "actionability": 10,
}

LIFECYCLE_STAGES = {
    "concept", "study", "application-filed", "recommended", "approved",
    "funded", "permitted", "under-construction", "partially-open",
    "completed", "unknown",
}

STATUS_CONDITIONS = {"active", "delayed", "paused", "canceled", "unknown"}
HORIZON_RELEVANCE = {
    "within-horizon", "impact-within-horizon", "beyond-horizon-watch", "unknown"
}
CONFLICT_STATES = {"none", "resolved", "non-material-documented", "material-unresolved"}
FRESHNESS_STATES = {"current", "stale-disclosed", "stale-rejected"}
REQUIRED_COVERAGE = {
    "jurisdiction", "lifecycle_stage", "status_condition", "status_as_of", "expected_completion"
}


def valid_date(value: str) -> bool:
    if value == "unknown":
        return True
    try:
        dt.date.fromisoformat(value)
        return True
    except (TypeError, ValueError):
        return False


def parse_real_date(value: str, field: str, claim_id: str) -> dt.date:
    try:
        return dt.date.fromisoformat(value)
    except (TypeError, ValueError):
        raise ValueError(f"source claim {claim_id} requires ISO date for {field}")


def valid_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--sources", required=True)
    parser.add_argument("--output")
    parser.add_argument("--count", type=int, default=10)
    args = parser.parse_args()

    try:
        if not 1 <= args.count <= 100:
            raise ValueError("count must be between 1 and 100")
        records = json.loads(Path(args.input).read_text(encoding="utf-8"))
        if not isinstance(records, list):
            raise ValueError("input must be a JSON array")

        sources = json.loads(Path(args.sources).read_text(encoding="utf-8"))
        if not isinstance(sources, list):
            raise ValueError("sources must be a JSON array")
        source_claims = {}
        for index, claim in enumerate(sources, start=1):
            if not isinstance(claim, dict):
                raise ValueError(f"source claim {index} must be an object")
            for field in (
                "claim_id", "canonical_project_id", "phase_id", "normalized_claim", "url",
                "source_class", "authority_issuer", "publication_date", "consulted_date",
                "effective_date", "freshness_status", "confidence", "conflict_status",
            ):
                if claim.get(field) in (None, ""):
                    raise ValueError(f"source claim {index} requires {field}")
            if claim["claim_id"] in source_claims:
                raise ValueError(f"duplicate claim_id: {claim['claim_id']}")
            if not valid_url(claim["url"]):
                raise ValueError(f"source claim {claim['claim_id']} has invalid URL")
            publication_date = parse_real_date(
                claim["publication_date"], "publication_date", claim["claim_id"]
            )
            consulted_date = parse_real_date(
                claim["consulted_date"], "consulted_date", claim["claim_id"]
            )
            effective_date = parse_real_date(
                claim["effective_date"], "effective_date", claim["claim_id"]
            )
            if publication_date > consulted_date or effective_date > consulted_date:
                raise ValueError(f"source claim {claim['claim_id']} has a future source date")
            if consulted_date > dt.date.today():
                raise ValueError(f"source claim {claim['claim_id']} has a future consulted_date")
            supported_fields = claim.get("supported_fields")
            if not isinstance(supported_fields, list) or not supported_fields:
                raise ValueError(f"source claim {claim['claim_id']} requires supported_fields")
            if claim["conflict_status"] not in CONFLICT_STATES:
                raise ValueError(f"source claim {claim['claim_id']} has invalid conflict_status")
            if claim["conflict_status"] == "material-unresolved":
                raise ValueError(f"source claim {claim['claim_id']} has unresolved material conflict")
            if claim["freshness_status"] not in FRESHNESS_STATES:
                raise ValueError(f"source claim {claim['claim_id']} has invalid freshness_status")
            if claim["freshness_status"] == "stale-rejected":
                raise ValueError(f"source claim {claim['claim_id']} is stale and rejected")
            evidence_date = max(publication_date, effective_date)
            age_days = (consulted_date - evidence_date).days
            expected_freshness = "stale-disclosed" if age_days > 365 else "current"
            if claim["freshness_status"] != expected_freshness:
                raise ValueError(
                    f"source claim {claim['claim_id']} freshness_status must be {expected_freshness}"
                )
            source_claims[claim["claim_id"]] = claim

        seen = set()
        ranked = []
        for index, record in enumerate(records, start=1):
            if not isinstance(record, dict):
                raise ValueError(f"record {index} must be an object")
            for field in (
                "canonical_project_id", "source_project_id", "phase_id", "project_name",
                "category", "primary_category_owner",
                "geography", "jurisdiction", "lifecycle_stage", "status_condition",
                "status_as_of", "expected_completion", "last_verified", "horizon_relevance",
                "ledger_status", "conflict_status",
            ):
                if not record.get(field):
                    raise ValueError(f"record {index} requires {field}")
            canonical_id = record["canonical_project_id"]
            phase_id = record["phase_id"]
            composite_id = (canonical_id, phase_id)
            if composite_id in seen:
                raise ValueError(f"duplicate project phase: {canonical_id}/{phase_id}")
            seen.add(composite_id)
            if record["lifecycle_stage"] not in LIFECYCLE_STAGES:
                raise ValueError(f"record {index} has invalid lifecycle_stage")
            if record["status_condition"] not in STATUS_CONDITIONS:
                raise ValueError(f"record {index} has invalid status_condition")
            if record["horizon_relevance"] not in HORIZON_RELEVANCE:
                raise ValueError(f"record {index} has invalid horizon_relevance")
            for date_field in ("status_as_of", "expected_completion", "last_verified"):
                if not valid_date(record[date_field]):
                    raise ValueError(f"record {index} has invalid {date_field}")
            if record["ledger_status"] != "APPROVED_FOR_IMPACT":
                raise ValueError(f"record {index} is not APPROVED_FOR_IMPACT")
            if record["conflict_status"] not in CONFLICT_STATES:
                raise ValueError(f"record {index} has invalid conflict_status")
            if record["conflict_status"] == "material-unresolved":
                raise ValueError(f"record {index} has unresolved material conflict")
            if not isinstance(record.get("dependencies"), list):
                raise ValueError(f"record {index} dependencies must be an array")
            claim_ids = record.get("supporting_claim_ids")
            if not isinstance(claim_ids, list) or not claim_ids:
                raise ValueError(f"record {index} requires supporting_claim_ids")
            for claim_id in claim_ids:
                claim = source_claims.get(claim_id)
                if not claim:
                    raise ValueError(f"record {index} references missing claim_id {claim_id}")
                if claim["canonical_project_id"] != canonical_id or claim["phase_id"] != phase_id:
                    raise ValueError(f"claim {claim_id} does not match project phase")
            covered = {
                field
                for claim_id in claim_ids
                for field in source_claims[claim_id]["supported_fields"]
            }
            missing_coverage = sorted(REQUIRED_COVERAGE - covered)
            if missing_coverage:
                raise ValueError(
                    f"record {index} lacks source coverage for: {', '.join(missing_coverage)}"
                )

            components = {}
            for field, maximum in MAXIMA.items():
                value = float(record.get(field, 0))
                if not 0 <= value <= maximum:
                    raise ValueError(f"record {index} {field} must be 0-{maximum}")
                components[field] = value

            item = dict(record)
            item["score_components"] = components
            item["growth_relevance_score"] = round(sum(components.values()), 2)
            ranked.append(item)

        ranked.sort(key=lambda item: (-item["growth_relevance_score"], item["canonical_project_id"]))
        payload = {
            "project_count": len(ranked),
            "returned_count": min(args.count, len(ranked)),
            "projects": ranked[: args.count],
            "method_note": "Score ranks monitoring relevance; it is not a property appreciation forecast.",
        }
        rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            Path(args.output).write_text(rendered, encoding="utf-8")
        else:
            sys.stdout.write(rendered)
        return 0
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        sys.stderr.write(f"error: {exc}\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
