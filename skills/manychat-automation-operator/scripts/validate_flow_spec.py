#!/usr/bin/env python3
"""Validate a ManyChat intermediate flow specification."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ALLOWED_NODE_TYPES = {
    "message",
    "data_collection",
    "action",
    "condition",
    "randomizer",
    "smart_delay",
    "start_automation",
    "external_request",
    "dynamic_content",
    "ai_step",
    "human_handoff",
    "end",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def validate(spec: dict) -> list[str]:
    errors: list[str] = []
    required = ["spec_version", "automation", "trigger", "fields", "tags", "nodes", "integrations", "tests", "kpis"]
    for key in required:
        if key not in spec:
            errors.append(f"missing top-level key: {key}")

    automation = spec.get("automation", {})
    for key in ["name", "mode", "channel", "objective", "primary_conversion", "status"]:
        if not automation.get(key):
            errors.append(f"automation.{key} is required")
    if automation.get("mode") not in {"DESIGN", "BUILD", "AUDIT", "OPTIMIZE"}:
        errors.append("automation.mode must be DESIGN, BUILD, AUDIT, or OPTIMIZE")
    if automation.get("status") not in {"draft", "active", "paused"}:
        errors.append("automation.status must be draft, active, or paused")

    trigger = spec.get("trigger", {})
    if not trigger.get("type"):
        errors.append("trigger.type is required")

    fields = spec.get("fields", [])
    field_names = [item.get("name") for item in fields if isinstance(item, dict)]
    if len(field_names) != len(set(field_names)):
        errors.append("field names must be unique")
    for index, field in enumerate(fields):
        if not field.get("name") or not field.get("type"):
            errors.append(f"fields[{index}] requires name and type")

    tags = spec.get("tags", [])
    tag_names = [item.get("name") for item in tags if isinstance(item, dict)]
    if len(tag_names) != len(set(tag_names)):
        errors.append("tag names must be unique")

    nodes = spec.get("nodes", [])
    node_ids = [node.get("id") for node in nodes if isinstance(node, dict)]
    if not nodes:
        errors.append("nodes must not be empty")
    if len(node_ids) != len(set(node_ids)):
        errors.append("node ids must be unique")
    known_ids = set(node_ids)

    for index, node in enumerate(nodes):
        node_id = node.get("id", f"index {index}")
        for key in ["id", "type", "name", "next"]:
            if key not in node:
                errors.append(f"node {node_id} missing {key}")
        if node.get("type") not in ALLOWED_NODE_TYPES:
            errors.append(f"node {node_id} has unsupported type {node.get('type')}")
        if not isinstance(node.get("next", []), list):
            errors.append(f"node {node_id}.next must be a list")
            continue
        for target in node.get("next", []):
            if target not in known_ids:
                errors.append(f"node {node_id} points to unknown node {target}")
        if node.get("type") == "randomizer":
            weights = node.get("weights", [])
            if sum(weights) != 100:
                errors.append(f"randomizer {node_id} weights must sum to 100")

    integration_ids = [
        item.get("id") for item in spec.get("integrations", []) if isinstance(item, dict)
    ]
    if len(integration_ids) != len(set(integration_ids)):
        errors.append("integration ids must be unique")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        fail("usage: validate_flow_spec.py <flow-spec.json>")
        return 2
    path = Path(sys.argv[1])
    try:
        spec = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(str(exc))
        return 2
    errors = validate(spec)
    if errors:
        for error in errors:
            fail(error)
        return 1
    print("PASS: flow specification is structurally valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
