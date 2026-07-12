# Multi-Agent Routing

## Principio

El Orquestador es dueño de la geografía, claves canónicas, Source Ledger, conflictos y entrega final. Los especialistas investigan dominios; ninguno crea una conclusión final independiente.

## Oleada 1 — Descubrimiento

- `Builder Discovery Agent`: builders nacionales, regionales y locales; comunidades; identidad; estado operativo.
- `Official Source Agent`: páginas oficiales, master developers y documentos públicos.

Ejecutar en paralelo cuando haya al menos seis comunidades esperadas. Ambos devuelven `ENTITIES`, `SOURCES`, `GAPS`, `CONFLICTS` y `CONFIDENCE`.

## Gate 1 — Registro canónico

El Orquestador deduplica y asigna `BUILDER_ID`, `COMMUNITY_ID` y `PHASE_ID`. No iniciar extracción profunda hasta resolver duplicados materiales.

## Oleada 2 — Investigación por dominio

- `Cost and Amenities Agent`: CDD, HOA, cuotas, amenidades, gated, 55+, mantenimiento y restricciones públicas.
- `Product and Inventory Agent`: colecciones, modelos, precios base y quick move-ins.
- `Incentive Agent`: promociones, tasas, créditos, vigencia y requisitos.

Ejecutar en paralelo usando el mismo registro canónico. Toda observación debe incluir claves, URL, fecha consultada, fecha efectiva, estado y confianza.

## Gate 2 — Reconciliación

El `Verification Agent` deduplica inventario, vincula claims con entidades, detecta promociones expiradas, separa amenidades abiertas/futuras y devuelve `PASS`, `PASS_WITH_GAPS` o `FAIL`.

Un `FAIL` material regresa al owner una sola vez. Máximo dos ciclos de corrección; luego degradar el claim o eliminarlo del resumen y mantenerlo en Verification Queue.

## Oleada 3 — Síntesis

El `Study and Strategy Agent` usa exclusivamente claims aprobados para crear comparaciones, buyer-fit basado en necesidades, visitas prioritarias, preguntas y flashcards. El Orquestador calcula KPIs y entrega.

## Reglas de partición

- Particionar por dominio para una ciudad mediana.
- Particionar por zona o builder si hay más de 30 comunidades, manteniendo un ledger común.
- No asignar el mismo builder/comunidad a dos especialistas del mismo dominio salvo verificación intencional.
- No permitir que especialistas sobrescriban archivos compartidos; deben devolver resultados estructurados al Orquestador.
- No exceder la concurrencia disponible. Si hay menos slots, ejecutar oleadas parciales.

## Contrato de retorno

Cada especialista devuelve:

```text
SCOPE
ENTITIES_OR_CLAIMS
SOURCES
EFFECTIVE_DATES
ASSUMPTIONS
CONFLICTS
GAPS
CONFIDENCE
RECOMMENDED_VERIFICATION
```

