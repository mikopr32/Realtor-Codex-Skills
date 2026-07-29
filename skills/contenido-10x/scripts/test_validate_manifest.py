#!/usr/bin/env python3

import json
import tempfile
import unittest
from pathlib import Path

from validate_manifest import REQUIRED_JSON, validate


class ValidateManifestTests(unittest.TestCase):
    def test_complete_contract_passes_without_assets(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name, keys in REQUIRED_JSON.items():
                payload = {key: "passed" for key in keys}
                (root / name).write_text(json.dumps(payload), encoding="utf-8")

            report = validate(root, require_assets=False)

            self.assertEqual(report["status"], "passed")
            self.assertEqual(report["missing"], [])

    def test_missing_contract_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            report = validate(Path(folder), require_assets=False)

            self.assertEqual(report["status"], "blocking")
            self.assertIn("property-brief.json", report["missing"])

    def test_nested_blockers_are_counted(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name, keys in REQUIRED_JSON.items():
                payload = {key: "passed" for key in keys}
                if name == "qa-report.json":
                    payload["findings"] = {"blockers": ["private address exposed"]}
                (root / name).write_text(json.dumps(payload), encoding="utf-8")

            report = validate(root, require_assets=False)

            self.assertEqual(report["status"], "blocking")
            self.assertEqual(report["blocking_findings"], 1)


if __name__ == "__main__":
    unittest.main()
