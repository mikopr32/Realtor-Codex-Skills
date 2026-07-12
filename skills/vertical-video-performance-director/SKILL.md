---
name: vertical-video-performance-director
description: Convierte conceptos, datos, propiedades y objetivos inmobiliarios en guiones de video vertical listos para grabar y editar para Instagram Reels, TikTok y YouTube Shorts; genera hooks, narrativa, teleprompter, shot list, B-roll, texto, subtítulos, pattern interrupts, CTA, cover, caption y variantes de prueba. Usar cuando el usuario pida crear, mejorar, adaptar, auditar o planificar videos cortos para educación, autoridad, leads, propiedades, comunidades, mercado o marca personal.
---

# Vertical Video Performance Director

## Objetivo

Diseñar videos verticales claros, creíbles y orientados a una acción medible. Optimizar atención, comprensión, retención y conversión sin garantizar viralidad ni usar clickbait engañoso.

## Principios

- Cumplir exactamente la promesa del hook.
- Elegir la duración mínima suficiente; no forzar 50 segundos ni una estructura fija.
- Verificar estadísticas, precios, tasas, incentivos, leyes y tendencias actuales.
- No prometer apreciación, aprobación, ahorro, rentabilidad, viralidad o resultados.
- Diseñar para consumo con y sin sonido, subtítulos legibles y safe zones.
- Usar visuales propios, autorizados, licenciados o legítimamente generados.
- No afirmar que un audio es trending sin verificar disponibilidad, fecha, región y uso comercial.
- Evitar Fair Housing risk, steering y claims profesionales no sustentados.
- No publicar ni subir contenido sin autorización explícita.

## Inputs

Aceptar como mínimo `{CONCEPTO}`. Aceptar opcionalmente plataforma, audiencia, mercado, objetivo, duración, formato, oferta, CTA, voz, idioma, producción, material, aparición en cámara, fuentes, propiedad, funnel y restricciones de brokerage.

Si solo hay concepto, asumir multiplataforma, audiencia inmobiliaria general, agente frente a cámara, objetivo de autoridad/conversación y CTA de baja fricción. Declarar brevemente los supuestos y avanzar.

## Workflow

### 1. Definir estrategia

Elegir una acción principal: reach, retención, autoridad, educación, saves, shares, comentarios, DMs, leads, appointments o property inquiry. No combinar múltiples CTAs competidores.

Definir audiencia por necesidad, conocimiento, objeción, resultado deseado y próxima acción; nunca por clases protegidas.

### 2. Verificar claims

Cuando el contenido use datos cambiantes, investigar fuentes vigentes. Crear un Fact Sheet con claim, valor, fuente, fecha, geografía, supuestos y redacción permitida. Si no puede verificarse, usar placeholder o eliminarlo.

### 3. Elegir duración

- 8–15 s: una idea o microtip.
- 20–30 s: error, mito o consejo.
- 30–45 s: explicación o comparación.
- 45–60 s: mini caso, proceso o estrategia.
- 60–90 s: educación profunda justificada.

Usar 130–165 palabras por minuto como rango inicial y ajustar a idioma, pausas y estilo. Ejecutar `scripts/check_timing.py` cuando exista teleprompter o timeline estructurado.

### 4. Crear y evaluar hooks

Generar 5–7 opciones entre resultado, error, contraste, curiosidad específica, objeción, demostración y opinión contraria sustentada. Evitar misterio vacío.

Puntuar 1–5 en claridad, especificidad, relevancia, credibilidad, curiosity gap, potencial visual y coherencia. Recomendar uno y conservar dos variantes para prueba.

### 5. Elegir estructura narrativa

Escoger según el concepto:

- Problema → mecanismo → solución → acción.
- Mito → evidencia → verdad → aplicación.
- Antes → cambio → después → lección.
- Opción A → opción B → tradeoff → recomendación.
- Pregunta → demostración → respuesta.
- Hook → open loop → valor → payoff → rehook.

No llamar loop a un cierre que no conecta naturalmente con el inicio.

### 6. Diseñar retención visual

Planificar pattern interrupts útiles cada 2–5 segundos: cambio de plano, punch-in, B-roll, texto, objeto, gráfico, ubicación, pregunta, pausa o sonido. Cada cambio debe recuperar atención o mejorar comprensión.

### 7. Escribir el guion técnico

Entregar:

| Tiempo | Objetivo | Audio/teleprompter | Visual/acción | B-roll | Texto en pantalla | Edición/audio |
|---|---|---|---|---|---|---|

Indicar plano, movimiento, pausa, énfasis, transición y fuente visual. Mantener el texto en pantalla breve.

Después entregar el teleprompter limpio sin instrucciones técnicas.

### 8. Diseñar CTA

Relacionar una acción con el funnel:

- Save: conservar guía/comparación.
- Share: enviar a alguien que enfrenta la decisión.
- Comment/DM keyword: solo si existe proceso real de respuesta.
- Lead: enviar una propiedad o pedir análisis.
- Authority: seguir para información específica.
- Appointment: agendar cuando la oferta lo justifique.

No usar “link en bio” por defecto ni prometer automatización inexistente.

### 9. Dirigir producción

Especificar formato 9:16, plano, eye line, iluminación, micrófono, fondo, props, energía, ritmo y tomas. Crear una versión one-take y otra con cortes cuando sea útil.

Para cada B-roll indicar clip, duración, fuente autorizada y función narrativa. No sugerir copiar noticias, listings, logos, música o videos sin permiso.

Para subtítulos indicar contraste, bloques breves, safe zones y revisión manual de nombres/cifras.

Si no se investiga música actual, recomendar solo estilo, BPM y energía, no “trending audio”. Mantener voz dominante.

### 10. Preparar publicación y prueba

Entregar cover de 3–7 palabras, caption, CTA, pinned comment, keywords, disclaimer, variante corta y adaptación por plataforma.

Crear A/B test cambiando una sola variable: hook, primer frame, cover, duración, CTA, estructura o formato. No cambiar todo simultáneamente.

## Métricas

Elegir según objetivo:

- Retención: 1-second hold, 3-second hold, average watch time, percentage viewed, completion y rewatches.
- Valor: saves, shares y comentarios significativos.
- Conversión: profile visits, DMs, clicks, leads, appointments y inquiries.

Comparar primero con la mediana reciente de la cuenta y videos similares; no imponer benchmarks universales.

## Formato de salida

# Vertical Video Brief: {CONCEPTO}

## 1. Estrategia

Plataforma, audiencia, objetivo, funnel, duración, estructura, CTA y métrica principal.

## 2. Fact Sheet

Claims, evidencia, fuente/fecha y redacción permitida.

## 3. Hooks

Tabla de hook, tipo, score, promesa y visual inicial.

## 4. Guion técnico

Timeline completo en tabla.

## 5. Teleprompter

Texto hablado limpio.

## 6. Producción

Shot list, props, B-roll, audio, iluminación, edición, subtítulos y safe zones.

## 7. Publicación

Cover, caption, CTA, pinned comment, keywords y disclaimer.

## 8. Variantes

Hook A/B, versión corta y adaptación por plataforma.

## 9. Medición

Hipótesis, métrica primaria, secundarias y próximo test.

Leer `references/production-quality.md` para revisar accesibilidad, derechos, claims y producción.

## Integración

Usar `$realtor-social-media-content` para calendarios, carousels y estrategia social amplia. Usar esta skill para dirección de video vertical lista para producir.

## Quality gate

- Hook y payoff coinciden.
- Primera frase funciona sin contexto.
- Primer frame contiene información o movimiento útil.
- Duración y densidad son coherentes.
- Teleprompter suena natural.
- Cifras tienen fuente, fecha, geografía y supuestos.
- Visuales y audio tienen uso permitido.
- Subtítulos, contraste y safe zones son adecuados.
- Existe una sola acción principal.
- CTA corresponde al funnel.
- No hay clickbait, garantías, steering o datos inventados.
- El paquete está listo para grabar y medir.
