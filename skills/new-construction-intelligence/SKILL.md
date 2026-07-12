---
name: new-construction-intelligence
description: Investiga comunidades residenciales de obra nueva y genera kits de marketing verificables para Realtors, incluyendo análisis de constructoras, modelos, inventario, precios, incentivos, costos recurrentes, mercado local, buyer personas, landing pages, videos, emails y estrategia SEO. Usar cuando el usuario proporcione una comunidad, constructora o enlace de new construction y necesite investigación, comparación, preparación comercial o activos para campañas de compradores.
---

# New Construction Intelligence

Investigar comunidades residenciales de obra nueva y convertir información verificada en un sistema de marketing listo para un Realtor. Combinar inteligencia inmobiliaria, análisis competitivo, copywriting, SEO y cumplimiento publicitario. No inventar precios, disponibilidad, incentivos, urgencia ni características.

## Objetivos

Entregar análisis técnico, costo real, mercado local, competencia, buyer personas basadas en necesidades, kit multicanal, estrategia SEO, registro de fuentes y resumen ejecutivo.

## Principios obligatorios

- Verificar cada dato sensible con una fuente directa y fecha.
- Separar hechos, estimaciones, inferencias y material promocional.
- No tratar precio base como precio final ni incentivos sin condiciones.
- No inventar escasez, fechas límite o disponibilidad.
- No mezclar constructoras, fases, ciudades o comunidades.
- Cumplir Fair Housing y no segmentar por clases protegidas.
- No reutilizar logos, planos, renders o imágenes sin autorización.
- No sobrescribir entregables anteriores.
- Mantener fuentes y disclaimers en los archivos finales.

## Input

Aceptar como mínimo ciudad, estado y enlace de comunidad o constructora. Aceptar opcionalmente nombre, ZIP, tipo de vivienda, precio, idioma, campaña, canal, buyer persona, marca, CTA, contacto, formato y carpeta. Comenzar sin confirmación innecesaria cuando haya datos suficientes.

## Arquitectura multiagente

Usar múltiples agentes para el kit completo, varias comunidades o investigación Deep. Mantener un solo agente para una pregunta puntual. Si no hay subagentes disponibles, ejecutar los mismos roles por fases sin simular delegación.

Crear primero una identidad canónica de comunidad, builder, fase, ubicación, fecha efectiva y alcance. Compartir un solo `FACT_LEDGER`. Exigir a cada investigador `OBSERVED_FACTS`, `SOURCE_URLS`, `EFFECTIVE_DATES`, `ASSUMPTIONS`, `CONFLICTS`, `CONFIDENCE` y `UNKNOWNS`.

### Oleada 1 — investigación paralela

- **Builder/Product Agent:** builder, modelos, especificaciones, inventario y disponibilidad.
- **Cost/Incentive Agent:** precios, lot premiums, HOA/CDD, taxes, closing costs, tasas e incentivos con condiciones.
- **Market/Competition Agent:** resale/new-construction competition, absorción, buyer leverage y comparables.
- **Location/Risk Agent:** escuelas asignadas, acceso, infraestructura, flood/insurance y restricciones verificables.

Particionar por dominio; no permitir cifras maestras distintas. Un **Research Lead** debe reconciliar identidad, fechas, geografía, modelos, precios, inventario, incentivos y costos. Preservar conflictos y reducir confidence; no promediar ofertas incompatibles.

### Oleada 2 — producción paralela

Solo después de aprobar el Fact Ledger:

- **Positioning/SEO Agent:** intent, positioning y estrategia SEO/AEO/GEO.
- **Content Agent:** kit, emails y copy desde claims aprobados.
- **Video Agent:** guiones desde el mismo message map.

Un **Validation Agent** revisa claims, vigencia, Fair Housing, incentivos, tasas, originalidad, CTA y consistencia entre los seis archivos. Ningún worker emite la recomendación final por separado.

Para múltiples builders, crear `COMMUNITY_ID`, `BUILDER_ID` y `PHASE_ID` canónicos. Toda fila de producto, precio, inventario, incentivo, costo y fuente debe incluir esas claves cuando apliquen y `EFFECTIVE_DATE`. Nunca promediar ni trasladar ofertas entre builders.

La Oleada 1 debe producir `canonical-identity.json`, `fact-ledger.csv`, `conflicts.md` y `research-gaps.md`. El Research Lead es owner de `01-analisis-inteligencia.md` y `06-source-ledger.md` y asigna al ledger estado `APPROVED_FOR_PRODUCTION` solo si:

1. Identidad y alcance están resueltos.
2. Cada claim tiene `CLAIM_ID`, claves de entidad, source, effective date, confidence, allowed wording y refresh/expiration.
3. Conflictos materiales están resueltos o marcados `CONTRADICTORY`.
4. Claims no verificados quedan excluidos de afirmaciones.
5. Precios, inventario, incentivos y costos no se mezclan entre builders.

Antes de Oleada 2, el Research Lead aprueba un `MESSAGE_MAP` que referencia solo CLAIM_ID permitidos. Positioning/SEO es owner de `05-seo-strategy.csv`; Content de `02-kit-marketing.md` y `03-secuencia-emails.md`; Video de `04-guiones-video.md`.

Validation devuelve `PASS` o `FAIL` con file, claim ID, issue y owner. Cada owner corrige solo sus archivos y se revalida. Máximo dos ciclos; después eliminar o marcar claims materiales no resueltos. Entregar solo con `PASS` y los seis archivos legibles.

## Fase 1 — Identidad y alcance

Confirmar nombre oficial, dirección, ciudad postal, municipio, condado, estado, ZIP, distrito escolar y fases. No asumir que ciudad postal equivale a jurisdicción.

Identificar desarrollador, constructoras, master developer, sales center, asociaciones, CDD y operador de amenidades.

Si el enlace incluye varias constructoras y el alcance no está definido, listar las identificadas con enlaces oficiales y preguntar si desea análisis individual, comparativo o general. No mezclar modelos, precios ni incentivos.

Aplicar una modalidad: constructora individual, comparación, comunidad general, quick move-ins o modelo específico.

## Fase 2 — Fuentes y confianza

Priorizar:

1. Sitio y documentos oficiales de la constructora.
2. Comunidad, desarrollador e inventario oficial.
3. HOA, CDD, Property Appraiser, Tax Collector y autoridades.
4. MLS y asociaciones de Realtors.
5. Distrito escolar.
6. Redfin, Realtor.com, Zillow y fuentes profesionales.
7. Medios y fuentes secundarias.

No usar fragmentos de búsqueda como fuente final. Registrar URL, título, dato, fecha publicada, fecha consultada, alcance, vigencia y confianza.

Etiquetar: **Confirmado**, **Alta confianza**, **Estimado**, **Promocional**, **No verificado** o **Contradictorio**.

## Fase 3 — Comunidad y producto

Investigar año, desarrollo, viviendas proyectadas, fases, tipos, constructores y amenidades abiertas, futuras o propuestas. No presentar una amenidad futura como disponible.

Para cada modelo registrar nombre, tipo, pisos, habitaciones, baños, garaje, pies cuadrados, precio base, quick move-ins, lotes, disponibilidad, fecha y enlace.

Distinguir modelo, plano, exhibición, quick move-in, spec home, build-to-order y producto discontinuado.

## Fase 4 — Precio y costo real

Indicar si el precio base excluye lot premium, elevation, structural options, design center, appliances, landscaping, closing costs, fees, HOA, CDD, membresía y financiamiento.

Usar: **Precio base anunciado desde $X; no representa necesariamente el precio final de una vivienda terminada.**

Para quick move-ins registrar dirección/lote, modelo, precio actual y anterior documentado, entrega, opciones, incentivos, estado y fecha. No afirmar disponibilidad sin verificarla.

Investigar HOA, subasociación, CDD, club, assessments, impuestos, seguro, flood zone, servicios y transfer fees. Si CDD varía por parcela, reportar rango o ejemplos.

## Fase 5 — Incentivos

Capturar descripción, beneficio, inicio, expiración, lotes, lender/title requerido, down payment, préstamo, puntos, credit score publicado, restricciones, combinación, disclaimer y fuente.

Distinguir reducción, closing-cost credit, design credit, rate buydown temporal o permanente, appliances, lot premium y Realtor bonus.

No convertir una tasa publicitada en asesoría hipotecaria. Si faltan condiciones, etiquetar: **Incentivo promocionado; condiciones completas no verificadas. Confirmar con constructora y lender.**

## Fase 6 — Mercado y competencia

Definir geografía exacta. Investigar precio mediano, cambio anual, DOM, inventario, meses de oferta, sale-to-list ratio, precio por pie cuadrado, reducciones, ventas, listados, obra nueva versus reventa, permisos y pipeline. Registrar fuente, período, geografía, propiedad y fecha.

No usar datos metropolitanos como exclusivos de la comunidad.

Identificar de tres a cinco competidores con comunidad, constructora, distancia, precio, producto, amenidades, incentivos, HOA/CDD, diferenciadores y riesgos. No declarar ganador universal; explicar compatibilidad por necesidades objetivas.

## Fase 7 — Escuelas y ubicación

Confirmar zonificación escolar con el distrito cuando sea posible. Registrar nombre, nivel, zonificación confirmada/estimada, distancia, rating externo, fuente y fecha. Separar escuelas asignadas, cercanas, charter y magnet.

Incluir: **Asignaciones y ratings pueden cambiar; confirmar con el distrito usando la dirección exacta.**

Seleccionar entre tres y seis puntos relevantes: parques, hospitales, comercios, aeropuerto, empleo, autopistas, infraestructura o atracciones. Reportar distancias y tiempos aproximados sin garantizarlos.

## Fase 8 — Buyer personas responsables

Crear personas por necesidades y comportamiento: bajo mantenimiento, oficina en casa, eficiencia energética, quick move-in, horizonte largo, obra nueva versus reventa, amenidades o distribución.

Para cada persona indicar necesidad, problema, producto compatible, objeción, evidencia, mensaje y CTA.

No usar raza, religión, nacionalidad, sexo, discapacidad, situación familiar, edad protegida u otra clase protegida.

## Fase 9 — Posicionamiento

Definir promesa verificable, tres diferenciadores, objeción, respuesta, competencia, razón documentada para actuar, riesgos y CTA. No presentar promoción de la constructora como análisis independiente.

## Fase 10 — Archivos

Crear sin sobrescribir:

```text
outputs/
└── {fecha}-{ciudad}-{comunidad}-{constructora}/
    ├── 01-analisis-inteligencia.md
    ├── 02-kit-marketing.md
    ├── 03-secuencia-emails.md
    ├── 04-guiones-video.md
    ├── 05-seo-strategy.csv
    └── 06-source-ledger.md
```

Normalizar nombres y añadir hora o sufijo si existe la carpeta.

### 01-analisis-inteligencia.md

Incluir resumen, identidad, modelos, quick move-ins, precios, incentivos, costo real, HOA/CDD, amenidades, escuelas, ubicación, mercado, competidores, personas, pros, contras, riesgos, pendientes y recomendación.

### 02-kit-marketing.md

Crear SEO title, meta description, H1, subheadline, propuesta, beneficios, modelos, amenidades, ubicación, incentivo condicionado, comparación obra nueva/reventa, FAQ, CTA principal/secundario y disclaimer. No copiar textos largos.

### 03-secuencia-emails.md

Crear tres emails con asunto, preview, cuerpo y CTA:

1. Bienvenida y expectativa.
2. Educación sobre comunidad, producto, costos y tradeoffs.
3. Decisión con urgencia solo si está documentada; si no, comparación o visita.

### 04-guiones-video.md

Crear tres guiones: descubrimiento, precio/incentivos y comparación/lifestyle. Incluir hook, visual, voz, texto en pantalla, CTA, disclaimer y duración. No presentar render o modelo como vivienda disponible.

### 05-seo-strategy.csv

Usar columnas:

```csv
keyword,intent,funnel_stage,location,builder,community,content_type,target_page,evidence,volume,competition,priority,notes
```

Generar al menos 20 keywords de marca, comunidad, ciudad, propiedad, precio, amenidad, comparación, preguntas, quick move-in e incentivos. Si volumen o competencia no están verificados, usar `not_verified`. Etiquetar keywords como hipótesis hasta validarlas con herramienta SEO.

### 06-source-ledger.md

Crear tabla con dato, fuente, fecha publicada, consulta, vigencia y confianza. Añadir contradicciones, faltantes, material promocional, vencimientos y verificaciones recomendadas.

## Cumplimiento

### Fair Housing

No recomendar por clases protegidas, describir composición demográfica, usar “perfecto para familias” o equivalentes, declarar seguridad sin contexto ni dirigir campañas mediante características protegidas. Presentar producto, precio, costos, ubicación, amenidades y necesidades objetivas.

### Precios y disponibilidad

Añadir: **Precios, disponibilidad, elevaciones, opciones e incentivos están sujetos a cambio sin previo aviso. Las imágenes pueden mostrar opciones no incluidas. Confirmar con la constructora.**

### Incentivos y tasas

Añadir: **Los incentivos pueden requerir lender o title afiliados y están sujetos a elegibilidad, disponibilidad, fechas y condiciones. Esto no constituye una oferta de crédito.**

### Independencia y propiedad intelectual

No insinuar representación de la constructora si no existe. No usar marcas, planos, renders o fotografías fuera de sus permisos. Cuando sea pertinente, recomendar confirmar registro y representación del Realtor antes de visitar el sales center.

## Datos faltantes

Continuar con información verificable, marcar `No encontrado` o `No verificado`, explicar dónde se buscó y cómo confirmarlo. Detener solo cuando identidad o alcance ambiguos puedan mezclar información.

## Quality Gate

No entregar hasta comprobar:

- Comunidad, constructora y ubicación correctas.
- Modelos asignados a la constructora correcta.
- Precios con fecha y alcance; base separado del final.
- Quick move-ins e incentivos verificados con condiciones.
- HOA, CDD, impuestos y costos incluidos o marcados.
- Amenidades abiertas separadas de futuras.
- Escuelas zonificadas separadas de cercanas.
- Mercado con geografía y período.
- Personas compatibles con Fair Housing.
- SEO sin métricas inventadas.
- Urgencia basada en evidencia.
- Fuentes directas, disclaimers y derechos respetados.
- Archivos abiertos, completos y no sobrescritos.
- Ningún dato inventado.

## Respuesta final

Confirmar comunidad, constructora, modalidad, fecha, carpeta y archivos. Presentar cinco puntos: posicionamiento, precio/costo real, incentivo principal, oportunidad de marketing y riesgo o pendiente. Enlazar los archivos.

Cerrar con: **La información fue verificada con las fuentes disponibles en la fecha indicada. Precios, inventario, incentivos, tasas, cuotas, escuelas y disponibilidad pueden cambiar. Confirma con la constructora, asociación, lender, autoridades y profesionales correspondientes antes de publicar o decidir.**
