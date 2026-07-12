---
name: meta-housing-ad-intelligence
description: Investiga anuncios inmobiliarios públicos en Meta Ad Library, identifica patrones competitivos de oferta, mensaje, formato, longevidad, visuales y funnel, y transforma aprendizajes agregados en conceptos de campaña, imágenes originales, copy, formularios y planes de prueba para Housing Ads. Usar para analizar competidores, buscar inspiración publicitaria, estudiar anuncios persistentes o crear campañas originales de Facebook/Instagram para compradores, vendedores, listings, comunidades o new construction.
---

# Meta Housing Ad Intelligence & Creative Lab

## Objetivo

Investigar anuncios inmobiliarios públicos, extraer patrones verificables y convertirlos en campañas originales y listas para probar. No inferir ROI, spend, conversiones, CPL o lead quality cuando no sean públicos.

## Principios

- Tratar longevidad como continuidad observada, no rendimiento probado.
- Analizar una muestra; no copiar una pieza.
- Crear estrategia original, no réplica mejorada.
- No reutilizar copy, composición, branding, personajes, propiedades, testimonios o trade dress.
- Respetar Meta Ad Library, términos, CAPTCHA, autenticación y límites técnicos.
- Verificar políticas vigentes de Housing antes de recomendar targeting, formatos o copy.
- Evitar steering, clases protegidas, proxies y atributos personales.
- No prometer rates, payments, incentives, approval, savings, appreciation o resultados.
- No publicar, activar campañas, gastar presupuesto ni enviar leads sin autorización.
- Usar solo herramientas disponibles en Codex; no declarar modelos externos inexistentes.

## Inputs

Aceptar como mínimo `{UBICACIÓN}`. Aceptar nicho, objective, intent, offer, property, price, language, budget, funnel, landing page, lead form, CRM, brand assets, authorized photos, disclosures, competitors, sample size y modo.

Modos:

- **Competitive Research:** inteligencia sin assets.
- **Creative Strategy:** conceptos y briefs sin imágenes.
- **Asset Generation:** visual original desde brief.
- **Full Campaign Kit:** research, strategy, copy, funnel y test plan; imagen solo si se solicita.

## Delegación multiagente opcional

Usar un solo agente para una muestra pequeña. Para 3+ anunciantes, varios mercados o análisis Deep, permitir:

- **Policy Agent:** reglas actuales de Housing Ads y restricciones aplicables.
- **Competitive Research Agents:** muestras no solapadas por anunciante/mercado.
- **Funnel Agent:** landing, lead form y follow-up visibles.

Todos devuelven observed date, ad/advertiser identity, format, offer, visible longevity, source y limitations. Un **Pattern Editor** deduplica y aprueba Pattern Matrix; un **Creative Agent** trabaja solo después del Originality Firewall; un **Claims/Compliance Validator** revisa al final. No inferir spend, targeting, leads, conversions o ROI. Si no hay subagentes, ejecutar por fases.

## Workflow

### 1. Definir campaña

Establecer mercado, nicho, campaign objective, funnel stage, offer, conversion action, intent, property/community, brand y compliance. Si solo hay ubicación, usar Research mode.

### 2. Verificar políticas actuales

Consultar documentación oficial vigente de Meta para Housing, audience restrictions, formats, CTA y disclosures. Registrar fecha. Separar platform policy, Fair Housing, brokerage y lending/builder disclosures. Marcar revisión de broker/lender/counsel cuando corresponda.

### 3. Investigar Ad Library

Navegar públicamente por location, niche, advertiser, offer, builder, community, intent y format. Abrir la ficha original.

Registrar advertiser, URL, ad ID visible, start/observed date, verified date, status, format, primary text, headline, description, CTA, offer, destination, creative attributes, disclosures y variants.

No evadir login, CAPTCHA, endpoints privados o restricciones. Registrar cobertura y fuentes inaccesibles.

### 4. Construir muestra

Analizar preferentemente 5–15 anuncios de varios anunciantes, combinando recientes, persistentes, ofertas y formatos. Si hay menos, reducir confidence. No afirmar representatividad total.

### 5. Medir longevidad

Calcular `Observed Longevity = Last Verified − Visible Start`. Clasificar New, Short-running, Established, Long-running o Unknown.

Buscar señales complementarias: variants, repeated offer, creative refresh, consistent landing page y cross-format continuity. No inferir performance.

Usar `scripts/analyze_ads.py` con el JSON investigado para calcular longevidad y patrones. Leer `references/ad-research-schema.md` antes de prepararlo.

### 6. Deconstruir

Analizar:

- **Offer:** listing, incentive, guide, list, valuation, event, consultation o new construction.
- **Message:** hook, benefit, mechanism, proof, objection, CTA, urgency y disclosures.
- **Visual:** subject, people, lighting, palette, composition, text, branding, motion y hierarchy.
- **Funnel:** website, landing page, instant form, Messenger, call, calendar o property page.
- **Trust:** brokerage, builder, listing, data, testimonial, license y transparency.

### 7. Crear Pattern Matrix

Identificar frequency, longevity signal, saturation, differentiation gap, compliance risk, evidence y confidence. Extraer patrones solo cuando existan en varias piezas o etiquetarlos como observación aislada.

### 8. Aplicar Originality Firewall

Permitir categoría de offer, estructura abstracta, visual category, general benefit y format.

Prohibir copy similar, distinctive composition, same property/person, logos, competitor colors copied deliberately, names, testimonials, exclusive claims y trade dress.

Comprobar diferencia en headline, subject, composition, palette, mechanism, proof, CTA wording y brand identity.

### 9. Crear hipótesis

Producir al menos:

- Concept A: offer-led.
- Concept B: education-led.
- Concept C: property/location-led.

Para cada uno definir hypothesis, intent, hook, offer, proof, visual, CTA, funnel, compliance y metric. Recomendar una dirección sin llamarla ganadora.

### 10. Crear brief visual

Definir objective, subject, setting, composition, lighting, palette, camera feel, negative space, brand integration, aspect ratio, variants y prohibited elements.

Evitar texto generado dentro de imagen por defecto. Para propiedades específicas, usar solo assets autorizados y no presentar una imagen conceptual como listing real.

No usar “en el estilo de” un artista, agencia o competidor identificable.

### 11. Generar visual

Solo cuando se solicite, usar la herramienta de imágenes disponible en Codex. Generar assets originales sin logos falsos, personas copiadas ni propiedad inventada como real.

Si la generación debe ser la última operación, preparar y guardar previamente el kit y generar la imagen al final.

### 12. Redactar copy

Elegir Situation → Opportunity → Mechanism → CTA; Question → Insight → Resource → CTA; Property → Differentiator → Availability → CTA; o Problem → Evidence → Better Path → CTA.

Entregar 3 primary texts, 5 headlines, 2 descriptions, CTA, creative alignment y disclosure placeholders. Verificar límites actuales cuando se requieran longitudes exactas.

No forzar pain/agitate cuando genere miedo, atributos personales o exageración.

### 13. Verificar claims

Crear Claim Ledger para prices, inventory, incentives, rates, payments, down payments, costs, appreciation, availability y eligibility. Incluir source, date, geography, assumptions, disclosure y status.

Eliminar, condicionar o dejar placeholder si falta evidencia.

### 14. Diseñar funnel

Crear landing promise, lead form, qualification questions, privacy placeholder, thank-you, first-response draft, appointment path, CRM handoff y owner. No enviar mensajes ni crear campañas.

Coordinar con `$realtor-ads-lead-generation` para assets finales y follow-up.

### 15. Crear test plan

Cambiar una variable por prueba: offer, hook, visual, format, CTA, form length, landing page o audience setup permitido. Registrar hypothesis, metric, observation period, decision rule y next action.

Medir delivery, engagement, lead y sales quality. No llamar ganador usando solo CTR o CPL; incluir downstream quality.

## Salida

# Meta Housing Competitive Intelligence: {MERCADO}

1. Research scope y limitaciones.
2. Competitive ad table con URLs/fechas.
3. Pattern matrix.
4. Findings: persistencia, saturación, gaps y lo no demostrable.
5. Concepts A/B/C.
6. Recommended original brief y prompt.
7. Visual original si fue solicitado.
8. Copy, CTA y disclosures.
9. Lead funnel.
10. Test plan.
11. Claim ledger.
12. Sources and limitations.

## Integración

- `$realtor-ads-lead-generation`: copy, forms y follow-up.
- `$imagegen` o herramienta disponible: visual original.
- `$vertical-video-performance-director`: vertical video ads.
- `$realtor-social-media-content`: reutilización orgánica.

## Quality gate

- Muestra suficiente o confidence limitado.
- Cada anuncio tiene URL y fecha.
- Active duration no se presentó como ROI.
- No se inventaron spend, reach, CTR, CPL o conversions.
- Los patterns provienen de múltiples piezas o se etiquetan aislados.
- La campaña es original y supera el originality check.
- Assets tienen derechos apropiados.
- Claims muestran evidence, date, geography y disclosures.
- Políticas Housing vigentes fueron revisadas.
- No hay steering ni protected-class targeting.
- CTA y funnel son coherentes.
- El test cambia una variable.
- No se publicó, activó ni gastó presupuesto.
