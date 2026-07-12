---
name: realtor-competitive-content-intelligence
description: Compara sistemáticamente perfiles públicos o autorizados de Realtors de Florida en Instagram y TikTok para identificar patrones visibles de posicionamiento, hooks, formatos, frecuencia, contenido, estética, engagement público y funnels; normaliza muestras entre plataformas, detecta espacios competitivos y genera hipótesis y planes originales sin copiar. Usar para competitor benchmarking, ingeniería inversa responsable, Realtor content intelligence, análisis Instagram-versus-TikTok y estrategia diferenciada de contenido inmobiliario en Florida.
---

# Realtor Competitive Content Intelligence

Construir benchmarks repetibles de Realtors de Florida en Instagram y TikTok. Extraer estructuras y oportunidades agregadas, no copiar piezas ni atribuir crecimiento, retención, leads o ventas a señales públicas que no pueden demostrarlos.

## Frontera con otras skills

- Usar esta skill para comparar competidores y descubrir patrones/gaps.
- Usar `social-brand-intelligence` para auditar profundamente la marca propia de Michael.
- Usar `vertical-video-performance-director` para convertir una estrategia aprobada en guiones.
- Usar `realtor-social-media-content` para producir el calendario y captions finales.

No duplicar una auditoría integral de la cuenta propia dentro de este benchmark.

## Principios

- Analizar únicamente cuentas públicas, propias o autorizadas.
- No eludir login, CAPTCHA, rate limits, robots, paywalls o controles de privacidad.
- Registrar exactamente qué fue visible, fecha, período y tamaño de muestra.
- Separar **Observado**, **Calculado**, **Inferido**, **No verificable** y **Recomendado**.
- No llamar “retención” a ritmo, cortes o storytelling sin watch-time/retention data.
- No llamar “top performer” a una pieza solo por views; usar “más vista dentro de la muestra observada”.
- No inferir ROI, leads, ventas, ingresos, audiencia demográfica ni algoritmo.
- No prometer superar o ganar al algoritmo.
- Extraer patrones abstractos de varias piezas; no copiar hooks distintivos, guiones, branding, propiedades, personas o composición.
- Cumplir Fair Housing, copyright, privacidad y disclosures inmobiliarios.

## Inputs

Aceptar:

- 2–10 Realtors o equipos de Florida;
- enlaces de Instagram y/o TikTok por competidor;
- mercado, nicho y audiencia deseada;
- objetivo: autoridad, leads, relocation, buyers, sellers, investors, luxury, new construction u otro;
- período, muestra, idioma, cuenta de Michael y métricas autorizadas opcionales.

Defaults:

- últimos 90 días o 20 posts visibles por plataforma/cuenta, lo que sea menor;
- mínimo útil: 10 piezas por cuenta/plataforma;
- si existe cuenta en ambas plataformas, analizar por separado y luego cruzar;
- no exigir simetría artificial si una plataforma tiene menos contenido visible.

Si el usuario entrega una sola cuenta, crear un profile benchmark limitado y declarar que no es inteligencia competitiva multi-cuenta.

## Modos

- **Landscape:** comparar 3–10 competidores.
- **Head-to-Head:** comparar 2 cuentas.
- **Cross-Platform:** comparar Instagram contra TikTok por creador.
- **Opportunity Gap:** encontrar temas, ofertas y formatos poco explotados.
- **Tracker:** repetir el benchmark y mostrar cambios contra una ejecución anterior.

## Delegación multiagente opcional

Usar un solo auditor para una cuenta/plataforma. Para 3+ cuentas o Instagram+TikTok de varios competidores, asignar unidades no solapadas por cuenta/plataforma a **Profile Research Agents**. Compartir sampling window, inclusion rules, post count, snapshot time y metric definitions.

Cada worker devuelve profile facts, normalized sample, visible metrics, hook/content/funnel observations, URLs y confidence; no declara ganadores ni copia creativos. Un **Benchmark Editor** deduplica posts cruzados, normaliza métricas no comparables y construye Pattern Matrix. Un **Strategy/Originality Agent** genera oportunidades solo después de la síntesis. Si no hay subagentes, ejecutar secuencialmente.

Registrar una pieza republicada una vez por plataforma y vincular sus versiones mediante `CANONICAL_CONTENT_ID`; no sumar engagement cross-platform como si fuera una sola métrica comparable.

## Workflow

### 1. Definir el benchmark

Registrar objetivo, mercado de Florida, nicho, audiencia por necesidad, plataformas, cuentas, período, muestra, métricas disponibles y criterio de comparación. Confirmar identidades y no mezclar cuentas homónimas.

### 2. Registrar acceso y cobertura

Por perfil documentar:

- plataforma, handle, URL y fecha de consulta;
- estado público/autorizado;
- followers visibles y fecha;
- publicaciones visibles revisables;
- login wall o limitaciones;
- muestra real, período y posts excluidos;
- si views, likes, comments, shares o saves son visibles.

Si el acceso bloquea contenido, pedir enlaces específicos, screenshots o exportes autorizados. No completar huecos mediante estimación.

### 3. Capturar perfil y funnel

Registrar bio, name field, mercado, especialidad, promesa, credenciales visibles, CTA, link-in-bio, lead magnet, landing, formulario, calendario y contacto. No enviar formularios, DMs ni reservas.

Mapear:

`Contenido → Perfil → Bio → Enlace → Destino → Conversión propuesta`

Clasificar cada paso: claro, parcial, confuso, roto o no verificable.

### 4. Crear muestra normalizada

Leer [benchmark-schema.md](references/benchmark-schema.md). Por pieza registrar:

- cuenta, plataforma, URL, fecha y antigüedad;
- formato y duración visible;
- tema, pilar y objetivo probable;
- hook hablado, visual y texto durante 0–3/5 segundos;
- estructura narrativa y pattern interrupts;
- CTA y funnel stage;
- estética, subtítulos, música/audio visible y producción;
- views, likes y comments visibles;
- shares, saves, watch time y retention únicamente si fueron proporcionados/autorizados.

No transcribir contenido completo. Parafrasear y capturar solo lo necesario para análisis.

### 5. Normalizar métricas públicas

No comparar views absolutas sin contexto. Cuando existan datos, calcular:

```text
Views per follower = visible views / followers observed
Public interaction rate = (visible likes + visible comments) / visible views
Posting frequency = sampled posts / covered days × 7
Relative view index = post views / median views of that account-platform sample
```

Tratar followers como snapshot, no como followers en la fecha de publicación. No mezclar plays/views incompatibles sin advertencia.

Usar `scripts/analyze_benchmark.py` para cálculos agregados cuando la muestra esté estructurada.

### 6. Analizar cada plataforma por separado

#### Instagram

Evaluar Reels, carruseles, posts, covers, captions, profile grid, pinned posts, highlights, collabs, CTA y funnel. No inferir Stories históricas si no están disponibles.

#### TikTok

Evaluar videos, opening frame, spoken/text hooks, pacing, search framing, captions, series, replies, pinned posts, CTA y profile link. No asumir que un sonido está “trending” sin verificación vigente.

No penalizar automáticamente una estrategia por no reutilizar el mismo contenido entre plataformas.

### 7. Construir Pattern Matrix

Identificar patrones solo cuando aparezcan repetidamente. Para cada patrón registrar:

- descripción abstracta;
- cuentas/plataformas donde aparece;
- cantidad y porcentaje de la muestra;
- piezas de evidencia enlazadas;
- señal pública asociada;
- explicación alternativa;
- confianza Alta/Media/Baja;
- utilidad potencial para Michael.

Ejemplos de categorías: local-news hooks, property tours, myth-busting, data explainer, relocation, lifestyle, reaction, storytelling, client proof, construction, direct offer y community guide.

### 8. Clasificar hooks y estructuras

Hooks:

- contrarian/correction;
- curiosity/open loop;
- local specificity;
- financial implication;
- mistake/risk;
- result/transformation;
- question;
- visual reveal;
- news/event;
- direct utility.

Estructuras:

- Hook → Context → Value → CTA;
- Problem → Evidence → Recommendation;
- Reveal/tour;
- List/countdown;
- Story → Lesson;
- Reaction → Interpretation;
- Question → Answer → Resource.

Describir lógica, no replicar wording distintivo.

### 9. Auditar diferenciación y funnel

Comparar claridad de mercado, buyer/seller focus, oferta, autoridad, local proof, lead magnet, CTA, destination, friction y follow-up visible. Clasificar funnel como profile-only, DM, link/landing, form, calendar, property search u otro.

No afirmar conversion rate sin datos internos.

### 10. Detectar Opportunity Gaps

Buscar oportunidades respaldadas por ausencia o ejecución débil dentro de la muestra:

- temas importantes de Florida no cubiertos;
- audiencias por necesidad desatendidas;
- preguntas frecuentes sin respuesta;
- formatos saturados versus diferenciables;
- claims sin evidencia que Michael puede mejorar con fuentes;
- funnel friction que Michael puede evitar;
- oportunidades bilingües;
- series locales repetibles.

“Nadie habla de esto” requiere evidencia amplia; normalmente usar “poco representado en esta muestra”.

### 11. Aplicar Originality Firewall

Permitir adoptar:

- categoría temática;
- arquitectura narrativa genérica;
- duración aproximada;
- tipo de CTA;
- principio de edición;
- formato de serie.

Prohibir copiar:

- frases o hooks distintivos;
- guiones o secuencias cercanas;
- identidad visual, paleta o templates deliberadamente imitativos;
- thumbnails/composición reconocibles;
- propiedades, testimonios, música propietaria o personas;
- branding, lead magnets o nombres de series.

Cada recomendación debe incluir una diferenciación original de Michael: experiencia, mercado, datos, enfoque, visual o recurso propio.

### 12. Crear hipótesis y plan

Entregar de tres a cinco hipótesis, no certezas. Para cada una:

- evidencia competitiva;
- oportunidad;
- concepto original;
- plataforma;
- audiencia/intent;
- hook family;
- formato;
- CTA/funnel;
- métrica primaria y secundaria;
- variable a probar;
- criterio de aprendizaje.

Proponer plan de 30 días con frecuencia sostenible. Cambiar una variable por test cuando sea posible.

## Scorecard

Puntuar cada cuenta/plataforma sobre 100, usando solo categorías evaluables:

| Categoría | Peso |
|---|---:|
| Posicionamiento local y diferenciación | 15 |
| Hook clarity | 15 |
| Content system y consistencia | 15 |
| Story/retention design observable | 10 |
| Platform fit | 10 |
| Public response signals | 10 |
| Funnel y CTA | 15 |
| Trust/proof | 5 |
| Originalidad/cumplimiento | 5 |

Reescalar pesos si una categoría no es evaluable y reducir confianza. El score compara la muestra, no calidad absoluta ni resultados comerciales.

## Entregables

Crear sin sobrescribir:

```text
outputs/{fecha}-fl-realtor-competitive-benchmark/
├── competitive-intelligence-report.md
├── content-sample.csv
├── pattern-matrix.csv
└── evidence-ledger.md
```

Si el usuario pide solo análisis breve, responder en chat sin crear archivos innecesarios.

### Reporte

1. Executive Summary.
2. Scope, muestra, acceso y limitaciones.
3. Competitor Scorecard por plataforma.
4. Instagram benchmark.
5. TikTok benchmark.
6. Cross-platform comparison.
7. Hook and format matrix.
8. Content mix and cadence.
9. Funnel comparison.
10. Patterns with confidence.
11. Opportunity Gaps for Florida.
12. Originality Firewall.
13. Three-to-five test hypotheses.
14. 30-day action plan.
15. Evidence ledger and methodology.

## Integraciones

Después de aprobar la estrategia:

- pasar conceptos a `vertical-video-performance-director` para guiones;
- pasar calendario/captions a `realtor-social-media-content`;
- usar `florida-market-content-intelligence` para verificar claims de mercado;
- usar `social-brand-intelligence` si Michael desea compararse formalmente contra el benchmark.

## Quality gate

No entregar hasta comprobar:

- cuentas correctas y públicas/autorizadas;
- plataformas analizadas por separado;
- muestra, período y limitaciones visibles;
- posts fijados y outliers tratados explícitamente;
- métricas normalizadas con fórmulas y denominadores;
- views no confundidas con retención o ventas;
- patrones respaldados por varias piezas o etiquetados como aislados;
- hechos, inferencias y recomendaciones separados;
- gaps limitados a la cobertura observada;
- recomendaciones originales y diferenciadas;
- Fair Housing, copyright y privacidad respetados;
- ningún claim de viralidad, algoritmo, ROI o leads inventado;
- no se enviaron mensajes ni se modificaron cuentas.

## Cierre

Indicar cuentas, plataformas, período, piezas revisadas, confianza, patrón más consistente, gap más defendible, hipótesis prioritaria y siguiente paso.

Cerrar con: **Este benchmark utiliza únicamente información pública o autorizada disponible en la fecha indicada. Las métricas visibles no revelan retención, conversiones, leads, ingresos ni causalidad algorítmica. Las recomendaciones son hipótesis originales que deben validarse mediante pruebas y datos propios.**
