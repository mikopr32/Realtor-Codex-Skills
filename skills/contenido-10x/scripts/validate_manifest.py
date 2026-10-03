#!/usr/bin/env python3
"""Validate the minimum Contenido 10X artifact contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REQUIRED_JSON = {
    "property-brief.json": (),
    "verified-property.json": (),
    "market-intelligence.json": (),
    "search-intelligence.json": (),
    "content-strategy.json": (),
    "copy-deck.json": (),
    "source-ledger.json": (),
    "claim-ledger.json": (),
    "qa-report.json": ("status",),
}

PACKAGE_ASSETS = (
    "ficha-tecnica.pdf",
    "post-instagram.png",
    "carrusel-01.png",
    "carrusel-02.png",
    "carrusel-03.png",
    "carrusel-04.png",
    "carrusel-05.png",
    "story-instagram.png",
    "email.html",
    "email.txt",
    "subject.txt",
    "copy-instagram.txt",
    "guion-video.txt",
)


def load_json(path: Path) -> tuple[Any | None, str | None]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return None, str(exc)


def find_blockers(value: Any) -> int:
    if isinstance(value, dict):
        count = 0
        for key, child in value.items():
            if key.lower() in {"blocking", "blockers"}:
                if child is True:
                    count += 1
                elif isinstance(child, list):
                    count += len(child)
                elif isinstance(child, int):
                    count += child
            count += find_blockers(child)
        return count
    if isinstance(value, list):
        return sum(find_blockers(item) for item in value)
    return 0


def validate(root: Path, require_assets: bool) -> dict[str, Any]:
    missing: list[str] = []
    invalid: list[dict[str, str]] = []
    warnings: list[str] = []
    blockers = 0

    for name, keys in REQUIRED_JSON.items():
        path = root / name
        if not path.is_file():
            missing.append(name)
            continue
        value, error = load_json(path)
        if error:
            invalid.append({"file": name, "error": error})
            continue
        if not isinstance(value, (dict, list)):
            invalid.append({"file": name, "error": "top-level JSON must be object or array"})
            continue
        if isinstance(value, dict):
            for key in keys:
                if key not in value:
                    invalid.append({"file": name, "error": f"missing key: {key}"})
            blockers += find_blockers(value)

    if require_assets:
        for name in PACKAGE_ASSETS:
            if not (root / name).is_file():
                missing.append(name)
        if not (root / "video-vertical.mp4").is_file():
            warnings.append("video-vertical.mp4 missing; document the fallback or render failure")

    status = "passed"
    if missing or invalid or blockers:
        status = "blocking"
    elif warnings:
        status = "warning"

    return {
        "status": status,
        "root": str(root.resolve()),
        "missing": missing,
        "invalid": invalid,
        "blocking_findings": blockers,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--require-assets", action="store_true")
    args = parser.parse_args()

    if not args.root.is_dir():
        print(json.dumps({"status": "blocking", "error": "root is not a directory"}))
        return 2

    report = validate(args.root, args.require_assets)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] in {"passed", "warning"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
