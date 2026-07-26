#!/usr/bin/env python3
"""Generate a concise QA checklist from a ManyChat flow specification."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: generate_test_cases.py <flow-spec.json>", file=sys.stderr)
        return 2

    try:
        spec = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    cases = [
        ("T01", "Contacto nuevo completa la ruta principal"),
        ("T02", "Contacto existente evita captura duplicada"),
        ("T03", "Ausencia de respuesta activa el fallback esperado"),
        ("T04", "Respuesta inválida activa reintento o ruta de error"),
        ("T05", "Reentrada sigue la política definida"),
        ("T06", "Solicitud humana activa handoff y notificación"),
        ("T07", "Enlaces externos abren el destino correcto"),
    ]

    branch_nodes = [
        node for node in spec.get("nodes", [])
        if node.get("type") in {"condition", "randomizer"}
    ]
    for node in branch_nodes:
        cases.append(
            (f"T{len(cases) + 1:02d}", f"Todas las ramas de {node.get('id')} - {node.get('name')} funcionan")
        )

    for integration in spec.get("integrations", []):
        label = f"{integration.get('id')} - {integration.get('provider', 'integración')}"
        cases.append((f"T{len(cases) + 1:02d}", f"{label} devuelve éxito y registra datos"))
        cases.append((f"T{len(cases) + 1:02d}", f"{label} falla y activa fallback/alerta"))

    print("| ID | Caso | Estado |")
    print("|---|---|---|")
    for case_id, description in cases:
        print(f"| {case_id} | {description} | NOT TESTED |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
