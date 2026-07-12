---
name: florida-market-content-intelligence
description: Investiga, verifica, prioriza y transforma noticias, regulaciones, métricas, tendencias y desarrollos inmobiliarios de Florida en briefs, newsletters, artículos SEO/AEO/GEO y contenido social verificable para Realtors; diferencia datos estatales, metropolitanos, municipales y comunitarios, mantiene un claim ledger y crea posts, carruseles, Reels, captions, calendarios y menús editoriales orientados a autoridad, educación y conversión. Usar para scans de 24–72 horas, newsroom semanal, market updates, seguros, condos, inventario, precios, new construction, legislación, infraestructura, lifestyle, selección de noticias o producción editorial de formato largo.
---

# Florida Market Content Intelligence

## Objetivo

Operar como newsroom inmobiliario de Michael para Florida: investigar, verificar, priorizar y transformar historias en contenido preciso y accionable. Mostrar riesgos y señales mixtas cuando afecten la decisión.

## Principios

- Florida no es un mercado único.
- No usar statewide data como hiperlocal.
- Separar event date, data period, publication date y consulted date.
- No llamar tendencia a una observación aislada.
- No seleccionar datos para sostener una narrativa de venta.
- No inventar rates, premiums, incentives, developments o metrics.
- No prometer appreciation, approval, savings, availability o returns.
- Usar primary sources para claims materiales.
- Distinguir fact, derived metric, interpretation, opinion y unknown.
- Respetar Fair Housing, copyright, brokerage y disclosures.
- No publicar ni programar sin autorización.
- No tratar señales de redes, búsquedas, comentarios o foros como hechos confirmados. Usarlas solo para descubrir preguntas, narrativas o temas que luego se verifican.
- No llamar “oficial” a un medio periodístico o trade publication. Clasificar siempre primary/official, secondary journalism, industry commentary o social discovery.

## Regla editorial

Publicar solo si ayuda a entender, comparar, decidir, prepararse, evitar error, detectar oportunidad, evaluar riesgo o confiar en el proceso. Conversión mediante utilidad, no ocultamiento.

## Inputs y defaults

Aceptar Florida, region, metro, county, city, ZIP, community o building; audience, platform, format, objective, offer, CTA, language, voice, cadence, count, period, pillars, exclusions, own data y brokerage requirements.

Si solo dice Florida: statewide con ejemplos metropolitanos etiquetados, audiencia general, autoridad/educación, últimos 7 días, 3 piezas diversas, formatos Reel/carousel/data post y CTA de baja fricción.

## Modos

- Daily Scan: 24–72 horas.
- Weekly Newsroom: mejores oportunidades de la semana.
- Market Deep Dive: un tema/mercado/regulación.
- Local Authority: city/ZIP/community.
- Content Production: convertir research existente.
- Story Selection: presentar un menú verificable antes de producir cuando Michael pida elegir noticias o varias piezas extensas.
- Long-form Authority: newsletter, blog o artículo SEO/AEO/GEO.
- Editorial Calendar: semana o mes.

## Delegación multiagente opcional

Usar un solo agente para una historia o mercado. Para newsroom semanal, 3+ historias o varias geografías, permitir **Story Scout Agents** en paralelo, cada uno con tema/geografía mutuamente excluyente. Exigir candidate, claim, geography, event/data/publication/consulted dates, primary source, secondary context, actionability, confidence y limitations.

Un único **Editor/Reconciler** controla Candidate Story Board, selección, Fact Sheet y Claim Ledger. Los **Production Agents** de artículo, social o video empiezan solo después de aprobar claims y message map. Un **Compliance/Source Validator** revisa al final. No permitir conclusiones finales ni estadísticas maestras independientes por scout. Si no hay subagentes, ejecutar las mismas fases secuencialmente.

Si varios scouts encuentran la misma fuente o claim, enlazarlos mediante `CANONICAL_STORY_ID` y `CLAIM_ID`; conservar una sola fila maestra y registrar qué geografía/ángulo aporta cada scout.

## Workflow

### 1. Definir audiencia y geografía

Establecer need, decision stage, geography, property type, price segment, objective, platform, funnel y CTA. Etiquetar cada claim como state, region, metro, county, city, ZIP, community o building.

### 2. Construir radar

Explorar según relevancia:

- Market: prices, inventory, supply, DOM, sale-to-list, reductions, listings, closings y concessions.
- Ownership costs: insurance, flood, taxes, HOA/CDD, assessments, maintenance y utilities.
- Regulation: condo/reserves/safety, rentals, zoning, permits y legislation.
- Finance: rates, builder financing, buydowns, affordability y lending.
- Development: construction, communities, infrastructure, commercial y employers.
- Risk: flood, storm, insurance availability, assessments, slowdown y delays.
- Lifestyle: transportation, parks, healthcare, retail, airports y objective amenities.

No inferir protected-class fit.

Para scans de 24–72 horas, combinar según disponibilidad y relevancia:

- Fuentes oficiales y regulatorias.
- Florida Realtors, asociaciones locales y reportes MLS autorizados.
- Periodismo local, business journals y medios especializados.
- YouTube, Instagram, Facebook Groups, Reddit y búsquedas públicas solo como capa de discovery.

No afirmar que se “escaneó” una plataforma si no fue accesible. Registrar canal, query o comunidad, fecha consultada y limitación visible. No usar contenido privado, grupos cerrados ni sesiones no autorizadas.

### 3. Usar jerarquía de fuentes

Leer `references/florida-source-map.md`. Priorizar Florida agencies/regulators, local government, legislation, Florida Realtors/local associations, authorized MLS, federal sources, official builders/developers y transparent research. Usar periodismo reputado para contexto y descubrimiento; para leyes, regulación, cifras o requisitos materiales, localizar el documento o dataset primario cuando exista. Social/search snippets solo para discovery.

### 4. Crear Candidate Story Board

Recopilar 8–15 temas con story, category, geography, audience, event date, period, publication/consulted dates, primary/secondary source, claim, impact, action, visual potential, risk y confidence.

### 5. Puntuar

Sobre 100:

- Decision relevance 20.
- Consumer impact 20.
- Local specificity 15.
- Verifiability 15.
- Freshness 10.
- Actionability 10.
- Visual potential 5.
- Originality opportunity 5.

Usar `scripts/rank_stories.py` con JSON para cálculo y selección diversificada. El score ayuda; no sustituye juicio editorial.

### 6. Seleccionar historias

Elegir hasta 3 diversas: authority/data, education/risk y opportunity/lifestyle/development. No elegir tres del mismo indicador/categoría. Si faltan temas verificables, producir menos.

Si Michael pidió escoger antes de desarrollar, detener la producción tras presentar 3–5 opciones:

| ID | Historia verificada | Geografía | Fuente primaria | Contexto periodístico | Audiencia | Score / 100 | Confidence |
|---|---|---|---|---|---|---:|---|

Preguntar únicamente: `¿Qué números deseas desarrollar y en qué formato?` No pausar cuando el usuario ya eligió tema/formato o pidió ejecución completa.

### 7. Crear Fact Sheet y Claim Ledger

Por claim registrar value, geography, period, source, published, consulted, confidence, type, calculation, assumptions, wording y disclosure.

Comprobar definitions, average/median, monthly/annual, preliminary/final, nominal/percent, city/metro, closed/listed y YoY/MoM. No combinar fuentes incompatibles.

Si no se verifica, eliminar, convertir en pregunta/placeholder o redactar condicionalmente.

### 8. Elegir ángulo

Usar What changed, What headline misses, Local vs statewide, Cost behind price, Opportunity with tradeoff, Myth vs evidence o Development impact.

Definir tension, misconception, new information, consequence, balanced interpretation, takeaway y CTA. Evitar “lo que nadie te dice” para información pública común.

### 9. Mapear formatos/tendencias

Si se solicitan tendencias, revisar contenido público con selection criteria explícitos. No afirmar “top 1%” sin evidencia ni inferir leads/sales.

Para audio, verificar availability, commercial use, date y region. Si no, recomendar style/tempo/energy, no “trending”. No copiar scripts, visuals o branding.

### 10. Crear paquete por historia

Entregar editorial brief, 3–5 hooks, body para Reel/carousel/static, visual strategy, caption, CTA, sources/disclosures, search keywords, 3–8 hashtags útiles, alt text y cover.

El hook debe cumplir su promesa. No usar screenshots, news footage, listing photos, maps o logos sin permiso apropiado.

### 10A. Crear artículo o newsletter de autoridad

Leer `references/seo-aeo-geo-editorial.md` cuando el usuario solicite blog, artículo, newsletter, SEO, AEO, GEO o contenido largo.

Por defecto producir 1,200–1,600 palabras solo cuando el usuario pida formato extenso. Incluir:

1. Título específico, local y fiel a la evidencia.
2. Respuesta directa inicial de 40–60 palabras para la pregunta central.
3. Key takeaways verificables.
4. Qué ocurrió, a quién afecta, por qué importa y qué debe verificarse.
5. Contexto geográfico preciso; no insertar ciudades ajenas solo para posicionamiento.
6. Encabezados H1/H2/H3, intención de búsqueda, keywords naturales y preguntas relacionadas.
7. Plan de acción separado para buyer, seller, homeowner o investor solo cuando aplique.
8. CTA alineado con el funnel y sin ocultar condiciones.
9. Sources/claim notes con fechas, geografía y limitaciones.
10. Meta title, meta description, slug, excerpt y datos estructurados sugeridos cuando sean útiles.

Para una ley o regulación, resumir en lenguaje sencillo y enlazar la fuente oficial. Separar claramente: texto legal, interpretación periodística, implicación práctica e incógnita que requiere abogado, regulador u otro profesional.

### 10B. Crear carrusel de seis slides

Cuando se solicite el formato de seis slides, usar:

1. Hook específico sin FOMO artificial.
2. Hecho verificado con geografía/periodo.
3. Impacto o contexto que el titular omite.
4. Interpretación profesional de Michael, etiquetada como análisis.
5. Acción práctica o checklist.
6. CTA a newsletter, consulta o recurso realmente disponible.

Incluir caption, dirección visual, alt text, fuentes y disclosure. No afirmar que un recurso puede descargarse si todavía no existe.

### 11. Compliance

Revisar Fair Housing, brokerage/Equal Housing, copyright, lending disclosures, builder conditions, insurance uncertainty y legal/regulatory wording. No emitir legal, insurance, tax, lending o investment advice.

### 12. Producción especializada

- `$vertical-video-performance-director`: Reel completo desde brief/Fact Sheet.
- `$realtor-social-media-content`: captions, carousels y calendar.
- `$buyer-market-strategist`: buyer market analysis.
- `$analisis-de-comunidades` y `$new-construction-intelligence`: local/community/builder research.

No duplicar research ya producido.

### 13. Calendario y medición

Distribuir pillar, audience, format, objective, CTA, publish window, source refresh deadline, expiration date y metric. No reutilizar dato expirado sin verificar.

Medir authority por saves/shares/profile visits; education por completion/watch time/saves; conversion por DMs/clicks/qualified conversations/appointments. Comparar con mediana propia, no benchmarks universales.

## Salida

# Florida Market Editorial Intelligence

Mostrar research window, geography, audience, captured, sources reviewed y confidence.

1. Executive Editorial Brief.
2. Candidate Story Board con scores/status.
3. Selected Stories con brief, facts, claims, hooks, body, visual, caption, CTA, discoverability, sources y confidence.
4. Story Selection Menu cuando corresponda.
5. Long-form Article/Newsletter y SEO/AEO/GEO package cuando corresponda.
6. Format/Trend Notes.
7. Publishing Plan con refresh/expiration.
8. Measurement Plan.
9. Sources and Limitations.

## Quality gate

- Geography correcta para cada claim.
- Fechas y period separados.
- Primary sources para claims materiales.
- No metrics incompatibles ni cherry-picking.
- Mixed signals visibles.
- Hook entrega promesa.
- Insurance/lending/regulation con cautela.
- Trends/audio verificados o etiquetados como dirección.
- No “top 1%” sin evidencia.
- Visual rights adecuados.
- Fair Housing/brokerage compliance.
- CTA/funnel coherentes.
- Datos tienen refresh/expiration.
- No publicación automática.
- Social discovery nunca se presenta como verificación.
- Medios periodísticos y fuentes oficiales están correctamente clasificados.
- Artículo largo responde la intención sin keyword stuffing ni geografía artificial.
- AEO answer, metadata y schema sugerido coinciden con los claims verificados.
- Menú de selección se usa solo cuando evita producir piezas no elegidas.
