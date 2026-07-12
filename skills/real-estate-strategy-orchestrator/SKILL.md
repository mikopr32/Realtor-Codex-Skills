---
name: real-estate-strategy-orchestrator
description: Funciona como punto de entrada y orquestador para consultas inmobiliarias complejas; clasifica intención, crea un case brief, selecciona las skills especializadas adecuadas, coordina dependencias, reconcilia resultados y entrega una recomendación ejecutiva con fuentes, supuestos, confianza y próximos pasos. Usar cuando el usuario no sepa qué análisis necesita, combine valoración, compra, venta, inversión, financiación, comunidad, new construction, listing performance o marketing, o solicite una estrategia integral.
---

# Real Estate Strategy Orchestrator

## Objetivo

Convertir una necesidad inmobiliaria en el workflow especializado mínimo necesario y sintetizar resultados en una decisión coherente. Coordinar especialistas sin duplicar su investigación ni reemplazar sus métodos.

## Principios

- Identificar la decisión, no solo el tema.
- Elegir una skill primaria y solo apoyos que cambien materialmente la decisión.
- Usar máximo dos apoyos por defecto; ampliar solo para deep analysis solicitado.
- No investigar previamente lo que debe resolver el especialista.
- Conservar source, date, method, assumptions y confidence.
- No promediar cifras incompatibles.
- Separar asking price, market value, investment value, MAO, DSCR-constrained price, affordability y net proceeds.
- No asumir que una skill existe: revisar el registro y disponibilidad.
- No crear subagentes automáticamente sin solicitud o autorización aplicable.
- No prometer value, returns, financing, approval, sale o appreciation.
- No contactar, publicar, enviar, ofertar, agendar, cargar CRM o gastar sin autorización.

## Inputs

Aceptar dirección, URL, ciudad, ZIP, comunidad, builder, commercial asset, lead list, campaign o pregunta. Incorporar role, decision, budget, financing, horizon, return, deadline, property type, occupancy, strategy, audience, depth y output cuando existan.

## Workflow

### 1. Identificar la decisión

Resumir en una oración: valorar, fijar precio, comprar, comparar, elegir mercado, analizar rentabilidad, financiar, diagnosticar listing, investigar comunidad/new construction, encontrar oportunidades, preparar campaña o crear client deliverable.

### 2. Clasificar caso

Definir:

- Persona: buyer, seller, investor, landlord, Realtor, builder, commercial o marketing operator.
- Objeto: property, community, neighborhood, market, builder, listing, lead list o campaign.
- Etapa: discovery, evaluation, financing, offer, due diligence, listing, relaunch, marketing o follow-up.
- Estrategia: residence, hold, BRRRR, flip, STR, commercial, land, new construction o seller strategy.
- Profundidad: Quick, Standard, Deep o Client-facing.

### 3. Crear Case Brief

```text
CASE_ID:
DECISION:
PERSONA:
SUBJECT:
LOCATION:
PROPERTY_TYPE:
STRATEGY:
BUDGET_OR_PRICE:
FINANCING:
TIME_HORIZON:
SUCCESS_CRITERIA:
KNOWN_FACTS:
MATERIAL_UNKNOWNS:
OUTPUT:
DEPTH:
```

Verificar solo identidad, ubicación y hechos necesarios para routing.

### 4. Resolver ambigüedad

Avanzar con escenarios cuando la intención sea clara y el dato faltante no cambie la ruta. Preguntar solo si comprar/vender/invertir divergen, falta subject/location, residential/commercial es ambiguo, se necesita autorización externa o una recomendación personalizada depende de budget/financing/horizon.

### 5. Seleccionar rutas

Leer `references/routing-registry.json`. Elegir por decisión y no por coincidencia superficial de palabras. Si el registro puede estar desactualizado, ejecutar `scripts/audit_registry.py`.

No usar una skill faltante. Seleccionar alternativa solo si responde la misma pregunta y declarar sustitución.

### 6. Definir Execution Map

| Orden | Skill | Función | Input | Output | Dependencia |
|---|---|---|---|---|---|

Reglas:

- Una primaria.
- Hasta dos apoyos en Standard.
- Más de tres solo en Deep.
- Ejecutar primero productores de inputs.
- Reutilizar shared facts y sources compatibles.
- Paralelizar trabajo independiente solo cuando esté permitido y aporte valor.
- No crear archivos si el usuario solo pidió una respuesta.

Cuando el usuario autorice multiagente y existan subtareas realmente independientes, ejecutar productores sin dependencias en paralelo. Mantener una sola skill primaria y no convertir cada apoyo en agente por defecto. Productores dependientes esperan los outputs reconciliados de sus upstream owners.

El orquestador raíz conserva ownership exclusivo de `Shared Property Profile`, `Source Ledger`, `Decision Matrix` y recomendación final. Los specialists solo devuelven su contrato; no emiten una recomendación integrada ni sobrescriben shared facts. Si no hay subagentes, respetar el mismo mapa secuencial.

### 7. Preparar handoff

Entregar al especialista:

```text
DECISION:
SUBTASK:
SUBJECT:
VERIFIED_FACTS:
USER_INPUTS:
ALLOWED_ASSUMPTIONS:
REQUIRED_OUTPUT:
SOURCE_REQUIREMENTS:
DO_NOT_DUPLICATE:
DEPENDENCIES:
```

Solicitar como retorno:

```text
VERDICT:
KEY_NUMBERS:
METHOD:
SOURCES:
ASSUMPTIONS:
CONFIDENCE:
RISKS:
UNKNOWNS:
RECOMMENDED_ACTION:
```

### 8. Mantener Shared Property Profile

Conservar address/identity, type, price, specs, year, HOA/CDD, taxes, insurance/flood, occupancy, listing history, source y date. Actualizar sin sobrescribir silenciosamente una contradicción.

Mantener Source Ledger con claim, value, source, URL, effective date, consulted date, geography, method, confidence y skill owner.

### 9. Reconciliar

Interpretar cada cifra según su pregunta:

- Asking price: expectativa del seller.
- Comp market value: sales comparison.
- Historical appreciation value: cross-check.
- Investment value: price satisfying returns.
- MAO: acquisition ceiling.
- DSCR-constrained price: financing ceiling.
- Affordability limit: buyer ceiling.
- Net proceeds: seller outcome.

Para source conflicts, comparar definition, geography, period, publication date y authority. Priorizar la fuente más específica/apropiada; mantener conflicto visible si persiste.

Para specialist conflicts, identificar objetivos y tradeoffs, decidir qué criterio domina la decisión y reducir confidence si queda incertidumbre.

### 10. Crear Decision Matrix

| Opción | Beneficio | Costo | Riesgo | Dependencia | Confidence | Trigger |
|---|---|---|---|---|---|---|

Conectar `evidence → interpretation → tradeoff → action`.

### 11. Sintetizar por audiencia

- Buyer: affordability, leverage, fit, due diligence y offer.
- Seller: value, net proceeds, market position, timing y listing strategy.
- Investor: basis, rent, NOI, financing, downside y exit.
- Realtor: client communication, evidence, positioning y next action.
- Marketing: offer, intent, funnel, compliance, asset y measurement.

## Profundidad

- **Quick:** una skill, datos esenciales, chat breve.
- **Standard:** primaria + hasta dos apoyos, ledger y executive brief.
- **Deep:** multidimensional, reconciliation, matrix, files y PDF opcional.
- **Client-facing:** lenguaje limpio, sources resumidas y technical appendix opcional.

## Salida

# Real Estate Strategy Brief

Incluir decision, subject, persona, depth y overall confidence.

1. Executive verdict en 3–5 frases.
2. Key findings con evidence, confidence y owner.
3. Numbers that matter con definición.
4. Decision matrix cuando exista alternativa real.
5. Recommendation con action, reason, risk, change condition y trigger.
6. Execution summary de skills utilizadas.
7. Unknowns/due diligence priorizados.
8. Next step concreto y autorizado.
9. Sources, methodology, assumptions y limitations.

No llenar la respuesta con detalles internos si no ayudan al usuario.

## Fallback

Si una skill falla, conservar evidencia válida, determinar si se puede concluir, usar alternativa equivalente solo si existe, reducir confidence y explicar el dato necesario. No inventar resultados.

## Guardrails

- No emitir asesoría legal, fiscal, appraisal, insurance o lending definitiva.
- No utilizar protected classes, sensitive data o steering.
- No presentar schools, crime o demographics como recomendación personal.
- No usar datos actuales sin verificar.
- No ejecutar acciones externas no autorizadas.

## Quality gate

- Decision identificada.
- Primary skill responde directamente.
- Supports cambian materialmente la respuesta.
- Registry routes existen o substitutions están declaradas.
- No hubo research duplicado.
- Shared data conserva definitions/dates.
- Conflicts son visibles o reconciliados.
- Value types están separados.
- Cada cifra material tiene method/source.
- Recommendation incluye tradeoff, risk y trigger.
- Unknowns están priorizados.
- Depth coincide con la solicitud.
- No hubo acciones externas no autorizadas.
