# Multi-Agent Routing

## Single source of truth

El Orchestrator es owner de `PROPERTY_ID`, Property Profile, Fact Ledger, Message Map, gates y recomendación final. Ningún especialista sobrescribe archivos compartidos; devuelve resultados estructurados.

## Oleada 1 — Intake

El Orchestrator crea identidad, alcance, fuentes, Data Gap Report y claves. No delegar hasta resolver mezcla de propiedades o listings.

## Oleada 2 — Inteligencia paralela

- Property Intelligence Agent.
- CMA & Pricing Agent.
- Market & Buyer Demand Agent.
- Risk & Opportunity Agent.

Cada agente devuelve:

```text
SCOPE
OBSERVED_FACTS
SOURCES
CALCULATIONS
ASSUMPTIONS
CONFLICTS
GAPS
CONFIDENCE
RECOMMENDATIONS
```

## Gate de reconciliación

El Orchestrator resuelve identidad, comparables, periodos, geografía y cifras maestras. No promediar conclusiones incompatibles. Mantener escenario y confianza de cada una.

## Oleada 3 — Producción

- Positioning & Launch Agent usa solo Claim IDs aprobados.
- Performance & Optimization Agent usa métricas reconciliadas.
- Seller Report usa el mismo Message Map y rango de precio.

## Gate de validación

Validation Agent devuelve `PASS`, `PASS_WITH_LIMITATIONS` o `FAIL`, con `file`, `claim_id`, `issue`, `severity`, `owner` y `required_action`.

Máximo dos ciclos. Luego retirar, degradar o presentar la limitación.

## Escala

- Pregunta puntual: un agente.
- Appointment o análisis: Orchestrator + hasta tres especialistas.
- Full o relaunch: oleadas completas.
- Si la concurrencia es limitada, ejecutar oleadas parciales.

