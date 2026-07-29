# Investigación de mercado y búsqueda

Leer este recurso cuando la solicitud requiera investigación actual, posicionamiento de una propiedad, SEO, AEO, GEO, comparables públicos, preguntas del comprador o claims externos. Omitirlo cuando el usuario solo pida adaptar texto con hechos ya aprobados.

## Resultado

Determinar, con evidencia:

1. cómo compite la propiedad en su micromercado;
2. qué busca y pregunta el comprador probable;
3. qué ángulo conecta la propiedad con esa intención;
4. qué afirmaciones pueden publicarse y cuáles deben bloquearse.

No sustituir un CMA, appraisal, opinión legal ni asesoría de Fair Housing.

## Entradas mínimas

Antes de investigar, exigir:

- dirección o, si debe permanecer privada, comunidad + ciudad + ZIP;
- estatus, precio vigente y fecha de verificación;
- tipo de propiedad, beds/baths, área, año y características verificadas;
- objetivo, audiencia por necesidad, idiomas, canales y CTA;
- URL pública/MLS u otra fuente del listing, si existe;
- HOA, CDD, impuestos, incentivos y documentos disponibles;
- restricciones de privacidad y claims que requieren aprobación.

Permitir `unknown`; nunca completar vacíos por intuición. Separar `confirmed`, `needs_verification`, `private` y `prohibited`.

## Protocolo

### 1. Delimitar el micromercado

Investigar de lo específico a lo amplio:

1. comunidad/subdivisión;
2. ZIP o radio competitivo razonable;
3. ciudad/condado;
4. área metropolitana solo como contexto.

Definir el set competitivo por tipo, rango de precio, tamaño, antigüedad, condición, amenidades y alternativa de nueva construcción. Explicar inclusiones y exclusiones. No presentar portales públicos como MLS.

### 2. Investigar el mercado

Buscar, según disponibilidad autorizada:

- inventario activo y alternativas relevantes;
- precio, precio por área y tiempo en mercado;
- reducciones, concesiones e incentivos vigentes;
- ventas recientes y listings pendientes;
- HOA/CDD, impuestos y costos recurrentes;
- oferta de builders;
- infraestructura y proyectos oficiales;
- amenidades y accesos verificables;
- feedback, fricciones y preguntas observables;
- diferenciadores y desventajas materiales.

Responder: **¿por qué esta propiedad debería entrar en la consideración del comprador frente a sus alternativas actuales?**

No crear una radiografía genérica de la ciudad ni afirmar causalidad a partir de correlaciones.

### 3. Mapear intención

Clasificar consultas por:

- `intent`: informational, local, commercial, comparison, transactional;
- `funnel_stage`: discovery, consideration, decision;
- `language`: es, en;
- `geography`: community, ZIP, city, county, metro;
- `audience_need`: first-home, move-up, downsizing, relocation, investment u otra necesidad permitida;
- `content_role`: discover, educate, answer, compare, convert.

Investigar:

- keyword primaria y temas de apoyo;
- long tails locales;
- preguntas completas y comparaciones;
- entidades: propiedad, comunidad, ciudad, condado, amenidades y fuentes oficiales;
- vocabulario que usa el público;
- resultados dominantes y vacíos de respuesta;
- estacionalidad o tendencia relativa cuando exista evidencia.

No inventar volumen, dificultad, CPC, ranking ni “trending”. Si no hay herramienta fiable, usar `metric_status: unavailable` y priorizar por relevancia estratégica.

### 4. Traducir a SEO, AEO y GEO

**SEO**

- Asignar una intención principal por pieza o página.
- Usar una keyword primaria y pocas secundarias naturales.
- Proponer title, meta description, H1/H2, slug, alt text y enlaces internos solo para superficies web.
- Evitar keyword stuffing, páginas duplicadas y datos estructurados que no coincidan con contenido visible.

**AEO**

- Formular preguntas como las haría un comprador.
- Responder primero de forma directa; ampliar después con contexto y trade-offs.
- Crear FAQ solo con preguntas útiles y respuestas verificadas.
- Señalar costos, condiciones, fechas y límites.

**GEO**

- Usar nombres consistentes y relaciones explícitas entre propiedad, comunidad, ciudad y condado.
- Redactar claims autocontenidos, fechados y atribuibles.
- Favorecer datos concretos, citas enlazables y comparaciones transparentes.
- Distinguir hechos, inferencias y recomendaciones.
- No afirmar que el contenido será citado o recomendado por un motor generativo.

### 5. Sintetizar

Priorizar:

1. relevancia para la propiedad;
2. intención cercana a conversión;
3. diferenciación comprobable;
4. autoridad y frescura de la evidencia;
5. capacidad de responder una objeción real.

Entregar un ángulo principal, hasta tres ángulos secundarios, objeciones, mensajes autorizados y contenidos recomendados. No convertir toda keyword en copy.

## Jerarquía de fuentes

Preferir fuentes primarias y actuales:

1. gobierno, county, ciudad, agencias y registros oficiales;
2. MLS/asociación Realtor con acceso autorizado;
3. property appraiser, tax collector, permisos y planificación;
4. HOA, developer, builder, utility o escuela oficial;
5. portales inmobiliarios con metodología y fecha visibles;
6. investigaciones institucionales y reportes de mercado;
7. periodismo local reputado;
8. datos propios documentados del agente;
9. foros, reseñas y redes solo para descubrir lenguaje, preguntas o hipótesis.

Una fuente de menor rango puede detectar una señal, pero no verificar un claim sensible. Confirmar con una fuente superior o marcarlo como no verificado. Guardar URL directa, no la página de resultados.

## Freshness

| Dato | Revisar |
|---|---|
| Precio, estatus, open house, incentivos | El mismo día |
| Tasas, pagos o términos financieros | El mismo día y con condiciones |
| Inventario, competencia y DOM | Preferiblemente ≤30 días |
| Métricas de mercado | ≤90 días, indicando periodo |
| HOA, CDD, impuestos | Último periodo oficial disponible |
| Proyectos, permisos e infraestructura | Estado oficial actual |
| Intención/tendencias de búsqueda | Registrar ventana y fecha de consulta |
| Demografía/empleo | Última publicación; mostrar año |

Asignar `accessed_at`, `review_after` y `expires_after`. Si la evidencia está vencida, no reutilizar el claim sin revisión.

## Source ledger

Guardar una entrada por fuente:

```json
{
  "source_id": "SRC-001",
  "url": "https://...",
  "publisher": "Entidad",
  "title": "Documento o página",
  "source_type": "government|mls|official|portal|report|news|first_party|forum",
  "published_at": "2026-07-01",
  "accessed_at": "2026-07-29",
  "geography": ["Kissimmee", "Osceola County"],
  "reliability": "high|medium|discovery_only",
  "facts_supported": ["..."],
  "evidence_excerpt": "Paráfrasis breve, no cita extensa",
  "review_after": "2026-08-28",
  "expires_after": "2026-10-27",
  "usage_restrictions": []
}
```

## Claim ledger

Todo dato externo que llegue al contenido debe tener:

```json
{
  "claim_id": "CLM-001",
  "claim": "Afirmación exacta",
  "source_ids": ["SRC-001"],
  "claim_type": "fact|inference|recommendation",
  "confidence": "high|medium|low",
  "verified_at": "2026-07-29",
  "public_wording": "Redacción permitida",
  "review_after": "2026-08-28",
  "expires_after": "2026-10-27",
  "allowed_surfaces": ["pdf", "web", "email"],
  "status": "approved|conditional|blocked"
}
```

No publicar claims `conditional` sin resolver su condición ni claims `blocked`. Si dos fuentes difieren, conservar ambas, describir el conflicto y usar la versión más autorizada solo si la discrepancia puede explicarse.

## Outputs JSON

Producir cuatro objetos, embebidos o como archivos cuando la tarea lo requiera:

### `market-intelligence.json`

```json
{
  "research_mode": "live|supplied-data-only",
  "as_of": "2026-07-29",
  "micro_market": {},
  "competitive_set_method": {},
  "market_signals": [],
  "buyer_needs": [],
  "objections": [],
  "verified_differentiators": [],
  "risks_and_tradeoffs": [],
  "positioning_implications": [],
  "limitations": []
}
```

### `search-intelligence.json`

```json
{
  "as_of": "2026-07-29",
  "primary_intent": {},
  "queries": [
    {
      "query": "...",
      "language": "es",
      "intent": "comparison",
      "funnel_stage": "consideration",
      "geography": "city",
      "audience_need": "relocation",
      "priority": "high",
      "evidence": ["SRC-001"],
      "confidence": "medium",
      "metric_status": "unavailable",
      "recommended_surface": "carousel"
    }
  ],
  "content_gaps": [],
  "limitations": []
}
```

### `aeo-question-map.json`

Incluir `question`, `direct_answer`, `supporting_claim_ids`, `intent`, `funnel_stage`, `language`, `caveat` y `recommended_surface`.

### `geo-entity-map.json`

Incluir entidades con `entity`, `type`, `canonical_name`, `relationships`, `source_ids`, `approved_facts`, `ambiguous_terms` y `schema_recommendation`. No generar Schema.org con datos desconocidos.

Entregar también `source-ledger.json` y `claim-ledger.json` cuando cualquier pieza use investigación externa.

## Operación sin web o sin fuente

Usar `research_mode: supplied-data-only`. Entonces:

- no simular búsqueda ni actualidad;
- etiquetar consultas como `hypothesis` o `unvalidated`;
- omitir métricas no disponibles;
- bloquear precio, estatus, inventario, tasas, incentivos y otros claims temporales no verificados;
- producir solo estrategia evergreen basada en datos aportados;
- listar investigación pendiente, impacto y fuente ideal;
- pedir aprobación humana antes de exportar contenido que contenga inferencias.

## Fair Housing, privacidad y límites

- Segmentar por necesidad, producto, presupuesto, ubicación solicitada y etapa; no por clases protegidas ni proxies.
- No inferir raza, color, religión, sexo, discapacidad, situación familiar, origen nacional u otras protecciones estatales/locales.
- Evitar expresiones como “ideal para familias”, “perfecto para jóvenes”, “barrio seguro”, “zona exclusiva” o referencias a la composición de residentes.
- Describir características objetivas: dormitorios, accesibilidad documentada, amenidades, distancias y reglas oficiales.
- Sobre escuelas y crimen, enlazar fuentes oficiales/neutrales y permitir que el consumidor evalúe; no calificar ni recomendar.
- No usar nombres, teléfonos, emails, dirección privada, feedback identificable o datos del seller sin autorización.
- No prometer apreciación, ROI, elegibilidad, pago o rentabilidad. Mostrar supuestos y disclosures cuando el usuario aporte cálculos autorizados.
- Marcar posibles problemas como `blocking`, `warning` o `suggestion`; no afirmar garantía legal.

## Gate de salida

No transferir la investigación al agente de estrategia hasta confirmar:

- alcance y fecha claramente declarados;
- set competitivo y método documentados;
- cada claim publicable enlazado al ledger;
- métricas no verificadas eliminadas o etiquetadas;
- conflicto de fuentes resuelto o expuesto;
- intención priorizada por pieza;
- revisión de privacidad y Fair Housing;
- limitaciones visibles.
