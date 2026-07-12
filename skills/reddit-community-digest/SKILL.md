---
name: reddit-community-digest
description: Investiga y resume las publicaciones principales de uno o varios subreddits públicos mediante ranking, periodo y filtros configurables; captura título, score observado, comentarios, fecha, flair, tipo, enlace y temas con timestamp y limitaciones. Usar cuando el usuario pida conocer qué es popular, nuevo, debatido o relevante en una comunidad de Reddit, crear un top de posts o preparar un digest verificable.
---

# Reddit Community Digest

## Objetivo

Crear un digest verificable de las publicaciones que Reddit presenta primero para un subreddit, sort y periodo determinados. No afirmar que ranking, score o comentarios permanecerán iguales después de la captura.

## Principios

- No inventar posts, scores, comments, dates o links.
- Usar solo comunidades públicas o sesiones autorizadas.
- No evadir login, age gates, quarantine, CAPTCHA, rate limits o private communities.
- No recuperar deleted/removed content.
- No extraer perfiles, historial o identidad de autores/comentaristas.
- Usar canonical permalinks.
- Registrar fecha, hora, timezone, sort, period, source y confidence.
- Llamar a votos `Observed Score`; etiquetar aproximaciones y scores ocultos.
- Parafrasear; no reproducir posts completos.
- Hacer el mínimo número de solicitudes necesario.

## Inputs y defaults

Aceptar `r/name`, `name` o URL. Aceptar sort, period, count, NSFW, pinned, megathreads, moderation posts, language, summary depth, keywords, multiple subreddits y output format.

Defaults:

- Sort `top`.
- Period `day`.
- Count 5, permitido 1–25.
- Excluir promoted, deleted/removed y placeholders.
- Excluir pinned/moderation salvo solicitud.
- Mantener crossposts marcados.
- No abrir NSFW si requiere confirmación o acceso adicional.

Informar defaults brevemente y avanzar.

## Delegación multiagente opcional

Usar un solo agente para un subreddit, incluso con una ventana amplia. Para múltiples subreddits, asignar un **Community Agent** por subreddit con el mismo snapshot time, sort, period, eligibility rules y capture schema. Cada worker devuelve metadata observada, permalink, captured time, summary y limitations; no genera el ranking combinado.

Un **Digest Editor** deduplica crossposts/URLs, conserva scores propios de cada comunidad sin compararlos como equivalentes y crea temas agregados. Cuando una afirmación externa sea material, un **Verification Agent** busca la fuente primaria. Si no hay subagentes, ejecutar comunidades secuencialmente.

## Workflow

### 1. Normalizar y verificar

Convertir el input en `r/name`. Confirmar que existe, corresponde al solicitado y es accesible. Clasificar Public, Authorized session, Private, Restricted, Age-gated, Unavailable o Not found. No sortear restricciones.

### 2. Seleccionar fuente

Priorizar conector/API autorizado, web pública actual, old Reddit público como fallback y search engine solo para discovery, no ranking final. Usar únicamente herramientas disponibles; no declarar `read_url_content` u otra herramienta inexistente.

Si se sustituye interfaz o ranking, declararlo y reducir confidence.

### 3. Aplicar sort y period

Permitir `top`, `hot`, `new`, `rising` y `controversial` cuando esté disponible. Para top/controversial usar `hour`, `day`, `week`, `month`, `year` o `all` cuando la interfaz lo soporte.

Confirmar subreddit, sort y period en la fuente.

### 4. Filtrar elegibilidad

Recorrer el orden visible. Excluir promoted, removed, deleted, placeholders, exact duplicates y pinned/moderation según configuración. No contar exclusiones dentro del límite; continuar hasta completar o agotar resultados.

### 5. Capturar metadata

Por post registrar rank, title, permalink, displayed score, approximate numeric score, approximation flag, comments, published timestamp, age, flair, type, domain, NSFW, spoiler, pinned, crosspost, source y captured timestamp.

No convertir `1.2k` en cifra exacta. Conservar display y marcar approximate. Usar `Hidden` si está oculto.

### 6. Abrir y resumir

Abrir cuando sea necesario y permitido. Crear 1–2 frases desde self-text, linked content verificable y contexto visible. No inferir body únicamente desde title.

Separar Post summary, Discussion signal e Assistant inference. Para discussion summary, indicar tamaño aproximado de muestra y no llamar consenso a pocos comentarios.

### 7. Clasificar y sintetizar

Marcar Text, Link, Image, Gallery, Video, Poll, AMA, Megathread, Crosspost o Unknown. Asignar 1–2 temas descriptivos.

Identificar temas repetidos, formatos predominantes y debate principal. Aclarar que la muestra no representa estadísticamente toda la comunidad.

### 8. Asignar confidence

- High: ranking/period verificados, posts abiertos, metadata completa.
- Moderate: métricas abreviadas o apertura parcial.
- Limited: interfaz alternativa, resultados incompletos, search fallback o restricciones.

### 9. Validar

Cuando se genere JSON, usar `references/digest-schema.json` como guía y ejecutar `scripts/validate_digest.py` antes de entregar archivos.

## Salida

# Reddit Community Digest: r/{SUBREDDIT}

Mostrar sort, period, captured time/timezone, requested/returned, source y confidence.

Por cada post:

### 🏆 {RANK}. {TITLE}

- Observed score.
- Comments.
- Published.
- Flair.
- Type.
- Summary.
- Canonical link.

Después añadir Themes across the digest y Coverage notes: exclusions, approximate/hidden scores, inaccessible posts, substitutions y limitations.

Ofrecer tabla, JSON o CSV cuando se solicite.

## Modos avanzados

- **Compare:** mismos sort, period y capture window entre subreddits.
- **Topic Filter:** filtrar elegibles sin ocultar ranking original.
- **Discussion Summary:** resumir muestra visible de comentarios.
- **Research Export:** Markdown, JSON o CSV.

No crear monitoreo recurrente salvo solicitud explícita.

## Error handling

- Sin subreddit: pedir solo nombre o URL.
- Not found: indicar que no se verificó; no llamarlo vacío.
- Private/restricted: informar y detener esa fuente.
- Menos posts: entregar disponibles y explicar.
- Hidden score: mostrar Hidden.
- Rate limit: detener repetición e informar.
- Metric conflict: usar fuente primaria y registrar diferencia.

## Privacy

No perfilar autores, buscar identidad, recopilar user history, revelar PII, recuperar deleted content, votar, comentar, guardar o enviar mensajes.

## Quality gate

- Subreddit, sort y period correctos.
- Capture time/timezone registrados.
- Count respetado o limitación visible.
- Ads/placeholders excluidos.
- Pinned/moderation según configuración.
- Titles/permalinks verificados.
- Scores observados y aproximaciones etiquetadas.
- Deleted/removed no reconstruidos.
- Summaries distinguen hechos e inferencias.
- No hay datos inventados.
- Confidence y limitations visibles.
