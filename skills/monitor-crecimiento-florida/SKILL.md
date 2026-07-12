---
name: monitor-crecimiento-florida
description: Investiga, verifica y monitorea proyectos de infraestructura, transporte, uso de suelo, desarrollos comerciales, empleo, turismo, mixed-use, master-planned communities y obra residencial que pueden cambiar accesibilidad, oferta, demanda, costos o riesgos inmobiliarios en Central Florida. Usar para growth reports, development pipelines, catalizadores por ciudad/county/corredor, seguimiento de FDOT/CFX/SunRail, rezonings, permisos, capital projects, nuevas comunidades o análisis de cómo un proyecto podría afectar una zona; no usar para valorar directamente una propiedad ni para convertir noticias en contenido social sin investigación previa.
---

# Monitor de Crecimiento de Florida

## Objetivo

Mantener inteligencia verificable sobre proyectos que podrían modificar el contexto inmobiliario de Central Florida. Distinguir anuncios, planes, financiación, approvals, permisos, construcción y apertura. Explicar mecanismos de impacto y tradeoffs sin prometer apreciación.

## Principios

- Definir la geografía antes de investigar; “Central Florida” no tiene un único límite operativo.
- Separar project status, milestone date, source publication date, last verified date y expected completion.
- Usar documentos oficiales para status, scope, funding, approval y ubicación material.
- Usar medios y redes para discovery/context, no como única confirmación de un proyecto.
- No confundir propuesta, rezoning request, approval, funding, permit, groundbreaking y completion.
- No afirmar que infraestructura o retail aumentará valores. Describir mecanismos, beneficiarios potenciales, costos, riesgos y evidencia faltante.
- No usar distancia lineal como prueba de impacto; considerar acceso real, barreras, jurisdicción, timing y escala.
- No inventar tenants, builders, unidades, investment amount, fechas, empleos, exits ni alignments.
- No usar material de más de un año como estado actual sin una actualización verificable.
- Respetar copyright, paywalls, términos de acceso, Fair Housing y límites profesionales.

## Inputs y alcance

Aceptar `{ZONA}`, counties/cities/corridors, categorías, periodo, horizon, property type, audience, depth, count, exclusions, prior report y output.

Si solo se indica Central Florida, definir explícitamente el alcance propuesto antes de concluir. Usar como punto de partida el Orlando–Kissimmee–Sanford core y añadir counties/corridors adyacentes solo cuando la fuente o el proyecto lo justifique. No mezclar automáticamente toda la jurisdicción de FDOT District Five con el mercado de Orlando.

Para una consulta sobre un proyecto específico, solicitar únicamente si faltan: (1) identidad del proyecto —nombre oficial, carretera/tramo, interchange o URL— y (2) ubicación suficiente de la propiedad/zona —dirección, comunidad, parcel, intersección o ZIP—. No investigar ni asignar impacto hasta resolver ambas identidades.

Modos:

- **Quick Pulse:** 3–5 proyectos materiales de una zona.
- **Sector Deep Dive:** infraestructura, comercial/turismo o residencial/land use.
- **County/City Watch:** pipeline por jurisdicción.
- **Corridor Watch:** proyectos conectados a una vía o transit corridor.
- **Portfolio Exposure:** cruzar proyectos con propiedades suministradas por el usuario.
- **Refresh:** actualizar un ledger previo y mostrar cambios.

## Arquitectura multiagente

Mantener un solo agente para una categoría y una geografía pequeña. Para reporte general, 2+ counties o varias categorías, usar agentes sectoriales con scope no solapado. Si no hay subagentes disponibles, ejecutar los mismos roles secuencialmente sin afirmar delegación.

### Intake Lead

Fijar `SCOPE_ID`, geografía, jurisdictions, corridors, categorías, research window, forward horizon, snapshot time, inclusion threshold y output. Crear un `PROJECT_LEDGER` compartido.

### Oleada 1 — discovery y evidencia paralelos

- **Infrastructure Agent:** FDOT, CFX, SunRail/LYNX, airports, ports where relevant, county/city capital projects, utilities and major road/transit work.
- **Commercial/Employment Agent:** retail, mixed-use, hospitality, attractions, campuses, industrial/logistics and employer expansions.
- **Residential/Land-Use Agent:** master plans, rezonings, comprehensive-plan changes, subdivisions, builder land activity, permits and housing pipeline.

Cada worker debe devolver:

```text
CANONICAL_PROJECT_ID:
SOURCE_PROJECT_ID:
PHASE_ID:
PROJECT_NAME:
CATEGORY:
PRIMARY_CATEGORY_OWNER:
SECONDARY_CATEGORY_TAGS:
GEOGRAPHY:
JURISDICTION:
LOCATION_OR_CORRIDOR:
SPONSOR_OR_APPLICANT:
LIFECYCLE_STAGE:
STATUS_CONDITION:
STATUS_AS_OF:
NEXT_MILESTONE:
EXPECTED_COMPLETION:
HORIZON_RELEVANCE:
SCOPE:
FUNDING_OR_INVESTMENT:
SUPPORTING_CLAIM_IDS:
OBSERVED_FACTS:
UNVERIFIED_CLAIMS:
DEPENDENCIES:
RISKS:
CONFIDENCE:
CONFLICT_STATUS:
LAST_VERIFIED:
LEDGER_STATUS:
```

Workers no asignan impacto inmobiliario final ni viral score.

Resolver solapamiento sectorial con un solo `PRIMARY_CATEGORY_OWNER`. Mixed-use, utilities, campuses y master plans pueden tener `SECONDARY_CATEGORY_TAGS`; otros workers deben referenciar el mismo canonical ID, no crear otro proyecto.

### Barrera de verificación

Un **Verification/Reconciliation Agent** es owner del Project y Source Ledger, deduplica nombres/fases, confirma jurisdicción, ubicación, stage, condition y fechas, y vincula aliases mediante `CANONICAL_PROJECT_ID`. Conservar `PHASE_ID` separados cuando tengan approvals, budgets o schedules distintos.

Clasificar por dos campos independientes:

- `LIFECYCLE_STAGE`: `concept | study | application-filed | recommended | approved | funded | permitted | under-construction | partially-open | completed | unknown`.
- `STATUS_CONDITION`: `active | delayed | paused | canceled | unknown`.

No elevar stage por lenguaje periodístico. Si fuentes oficiales discrepan, registrar el conflicto y reducir confidence.

Mantener un `SOURCE_LEDGER` por `CLAIM_ID` con `CANONICAL_PROJECT_ID`, normalized claim, URL, source class, authority/issuer, publication date, consulted date, effective date, supported fields, freshness status, confidence y conflict status.

Asignar `LEDGER_STATUS: APPROVED_FOR_IMPACT` solo cuando identidad, jurisdiction, phase, lifecycle stage, condition, dates, source claims y conflictos estén resueltos o explícitamente marcados. Registros no aprobados no pasan a Oleada 2.

### Oleada 2 — análisis de impacto

Después de aprobar el Project Ledger, un **Real Estate Impact Agent** evalúa:

- Mecanismo: access/time, capacity, amenity, jobs, visitor demand, housing supply, taxes/assessments, construction disruption, environmental/insurance or land-use change.
- Direction: potentially positive, mixed, potentially negative or unclear.
- Exposure: geography and property types plausibly affected.
- Timing: near 0–2 years, medium 3–5, long 6+ or unknown.
- Dependency: approvals, funding, acquisition, permits, construction or tenant commitment.
- Confidence and what would change the assessment.

Devolver por proyecto:

```text
IMPACT_CLAIM_ID:
CANONICAL_PROJECT_ID:
MECHANISM:
EVIDENCE_CLAIM_IDS:
EXPOSURE_GEOGRAPHY:
AFFECTED_PROPERTY_TYPES:
DIRECTION:
UPSIDE:
DOWNSIDE:
TIMING:
DEPENDENCIES:
CONFIDENCE:
FALSIFIER_OR_UPDATE_TRIGGER:
```

No producir un porcentaje de appreciation ni causal claim sin estudio específico. Diferenciar regional catalyst de talking point local.

### Editorial Lead y QA

Un **Report Editor** sintetiza sin alterar el ledger. Un **Validation Agent** revisa source class, dates, geography, stage/condition, duplication, impact wording, unsupported tenants/investment/jobs y stale projects. Devuelve `PASS` o `FAIL` con project/claim ID, issue y owner. Máximo dos ciclos de corrección; después excluir o degradar el claim persistente. Entregar solo con `PASS`.

## Workflow

1. Definir scope y snapshot.
2. Leer `references/central-florida-source-map.md`.
3. Buscar primero agendas, project pages, adopted plans, permits, applications, budgets y filings oficiales.
4. Usar medios locales/trade para discovery, chronology y stakeholder context.
5. Crear longlist y excluir items sin ubicación, status material o evidencia suficiente.
6. Reconciliar Project Ledger.
7. Puntuar con `scripts/rank_projects.py --input PROJECTS.json --sources SOURCE_LEDGER.json`; usar score como ayuda, no sustituto del juicio.
8. Analizar mecanismos de impacto y downside.
9. Comparar con el reporte anterior cuando exista: new, advanced, unchanged, delayed, completed, canceled or corrected.
10. Validar y producir el reporte.

## Scoring

Puntuar sobre 100:

- Local relevance: 20.
- Status evidence: 20.
- Scale/materiality: 15.
- Real-estate mechanism: 15.
- Timeline clarity: 10.
- Source quality: 10.
- Actionability: 10.

No usar “viral potential” como proxy de importancia. Mantener confidence separado del score.

Para un horizon solicitado, asignar `HORIZON_RELEVANCE`: `within-horizon`, `impact-within-horizon`, `beyond-horizon-watch` o `unknown`. El reporte principal incluye solo proyectos con stage/mecanismo plausible dentro del horizon; mover `beyond-horizon-watch` y `unknown` a watchlist separada.

## Salida

# Central Florida Growth & Development Report: {ZONA}

Incluir scope, research window, snapshot time, sources reviewed, limitations y overall confidence.

1. Executive pulse: 3–5 cambios materiales.
2. Project watchlist con score, lifecycle stage, condition, timing y last verified.
3. Infrastructure & mobility.
4. Commercial, employment & lifestyle.
5. Residential & land-use pipeline.
6. Impact matrix: mechanism, exposure, upside, downside, dependencies y confidence.
7. Timeline y next milestones.
8. Changes since prior report cuando aplique.
9. Factual handoff brief de tres líneas, sin hook, CTA ni copy publicable.
10. Source Ledger y items descartados/por verificar.

Para cada proyecto mostrar:

- Nombre, `CANONICAL_PROJECT_ID` y `PHASE_ID`.
- Geografía/jurisdicción.
- Sponsor/applicant.
- Status as of date.
- Scope y next milestone.
- Mechanism of potential impact.
- Upside, downside y affected segments.
- Primary source, secondary context y confidence.

## Integraciones, fronteras y routing

- Investigación de project pipeline, approvals, funding, milestones y cambios longitudinales → usar esta skill primero.
- Selección editorial, newsletter, artículo, Reel o social content → entregar el ledger aprobado a `$florida-market-content-intelligence`.
- Comunidad/builder, modelos, inventario e incentivos → profundizar con `$new-construction-intelligence`.
- Condiciones actuales, prices, inventory y DOM → usar `$realestate-market`; esta skill aporta catalizadores futuros, no market classification actual.
- Estrategia para compradores → usar `$buyer-market-strategist` después de reconciliar current market y future pipeline.
- Underwriting de propiedad/terreno → usar `$real-estate-opportunity-underwriter`; no transferir project score como evidencia de valor o retorno.

- `$analisis-de-comunidades`: evaluar HOA/CDD, amenidades y restricciones de una comunidad.

No duplicar la investigación: entregar Project/Source Ledger y `CLAIM_ID` al downstream skill.

## Failure handling

- Paywall o acceso bloqueado: no inferir contenido; buscar fuente oficial o declarar limitación.
- Solo anuncio sin filing/approval: mantener `concept` o `unknown`.
- Fecha de completion conflictiva: mostrar rango y fuentes, no elegir silenciosamente.
- Tenant rumor: excluir tenant y conservar el desarrollo si está verificado.
- Proyecto stale: buscar update; si no existe, marcar `last verified` y reducir confidence.
- Geografía ambigua: no asignar impacto hasta resolver parcel, corridor o jurisdiction.
- Pocos proyectos verificables: entregar menos; no rellenar con noticias débiles.

## Quality gate

- Scope geográfico explícito.
- Cada proyecto tiene canonical ID, phase, lifecycle stage y status condition controlados.
- Status, source dates y last verified están separados.
- Claims materiales tienen fuente primaria cuando existe.
- Medios no se etiquetan como oficiales.
- Duplicados/fases están reconciliados.
- Impacto se expresa como mecanismo y escenario, no garantía.
- Upside y downside son visibles.
- Timeline y dependencies están claros.
- Items stale, delayed y canceled no se ocultan.
- No publicación ni acción externa sin autorización.
