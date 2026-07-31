# Producción y QA

Usar este contrato después de aprobar la investigación de propiedad, mercado y búsqueda. Cada fase pertenece a un subagente especializado. Los agentes de producción no deben volver a investigar ni introducir hechos nuevos.

## Principios operativos

- Tratar `verified-property.json`, `source-ledger.json`, `search-intelligence.json` y `content-strategy.json` aprobados como fuentes únicas.
- Mantener `claimId` y `sourceId` en toda afirmación verificable.
- Separar hechos, inferencias, recomendaciones y texto creativo.
- Bloquear cualquier claim sin respaldo cuando pueda afectar precio, financiamiento, rentabilidad, seguridad, escuelas, disponibilidad, incentivos o cumplimiento.
- Invalidar solo los entregables afectados por un cambio.
- Conservar versiones, decisiones, tiempos, advertencias y responsable de cada fase.
- Requerir aprobación humana en los gates definidos.

## Flujo y propiedad por subagente

| Fase | Subagente | Entrada aprobada | Salida |
|---|---|---|---|
| Estrategia | Estratega de contenido | Propiedad, mercado, búsqueda y fuentes | `content-strategy.json` |
| Copy | Redactor multicanal | Estrategia y hechos verificados | `copy-deck.json` |
| Diseño | Director visual | Copy aprobado, fotos y branding | PDF, post, carrusel, story y manifiesto |
| Video | Director de video y voz | Guion aprobado, fotos, branding y audio autorizado | MP4 y manifiesto |
| Compliance | Revisor de cumplimiento | Claims, copies y renders | `compliance-report.json` |
| QA | Control de calidad | Todos los entregables | `qa-report.json` |
| Empaque | Orquestador | Gates aprobados | ZIP y `package-manifest.json` |

El orquestador coordina estados y dependencias; no sustituye el criterio especializado de una fase.

## Contrato de estrategia

`content-strategy.json` debe incluir:

- `strategyId`, versión, fecha y estado.
- Objetivo comercial y KPI principal.
- Audiencia por necesidad e intención; no usar características protegidas.
- Etapa del funnel y canal prioritario.
- Ángulo principal y hasta dos ángulos secundarios.
- Diferenciador verificable.
- Jerarquía de beneficios.
- Objeciones que deben responderse.
- Mensaje central, tono y CTA.
- Keyword principal, keywords de apoyo, preguntas AEO y entidades GEO.
- Claims `permitidos`, `condicionados` y `prohibidos`.
- Función de cada una de las seis piezas.
- Reglas de coherencia entre español e inglés, si aplica.
- Riesgos, supuestos y nivel de confianza.

La estrategia debe asignar una función distinta a cada pieza:

1. PDF: informar y facilitar decisión.
2. Post: detener el scroll y generar descubrimiento.
3. Carrusel: educar, responder objeciones y persuadir.
4. Story: producir acción inmediata.
5. Email: profundizar consideración y convertir.
6. Video: ampliar alcance, retención y recuerdo.

No aprobar una estrategia que repita el mismo anuncio en seis formatos.

## Contrato de copy

`copy-deck.json` debe contener:

- Titular, subtítulo y descripción breve.
- Descripción larga.
- Copy y CTA para post.
- Texto de cinco slides.
- Texto para story.
- Asunto, preheader, cuerpo HTML y texto plano del email.
- Guion, locución y textos en pantalla del video.
- Alt text, metadata, FAQ AEO y bloque GEO reutilizable.
- Idioma, tono, longitud objetivo y pieza de destino.
- `claimId` y `sourceId` por cada afirmación verificable.
- Advertencias de longitud o claims condicionados.

Reglas:

- Usar únicamente hechos y estrategia aprobados.
- No realizar investigación adicional.
- No inventar urgencia, demanda, escasez, incentivos ni resultados.
- Integrar keywords de manera natural; no sacrificar claridad por densidad.
- Mantener consistencia de precio, dirección pública, características y CTA.
- Diferenciar el copy por función de canal.
- Devolver contradicciones al agente responsable; no resolverlas silenciosamente.

## Contrato de diseño

El subagente de diseño debe:

- Usar textos aprobados sin alterar claims.
- Aplicar el preset de marca autorizado.
- Elegir fotografías por calidad, orientación, función y posición focal.
- Respetar safe zones, contraste, jerarquía y legibilidad móvil.
- Excluir datos privados, marcas de agua no autorizadas y campos vacíos.
- Registrar plantilla, versión, fotografías, textos y dimensiones usados.
- Devolver al agente de copy cualquier texto que no quepa; no resumirlo por cuenta propia.

Entregables:

- `ficha-tecnica.pdf`.
- `post-instagram.png`, 1080 × 1350.
- `carrusel-01.png` a `carrusel-05.png`, 1080 × 1350.
- `story-instagram.png`, 1080 × 1920.
- `email.html`, `email.txt` y `subject.txt`.
- `visual-manifest.json`.

Validaciones mínimas:

- Sin texto cortado, desbordado o ilegible.
- Datos profesionales y disclosures visibles cuando correspondan.
- Fotografías sin deformación ni recortes críticos.
- Links y QR funcionales.
- HTML responsive, con estilos inline y ancho máximo de 600 px.
- PDF abre correctamente y conserva márgenes.

## Contrato de video

El subagente de video debe producir un MP4 vertical de 20–35 segundos:

- 1080 × 1920, H.264.
- Hook inicial, presentación, secuencia de fotos, diferenciador, CTA y cierre de marca.
- Textos y subtítulos dentro de safe zones.
- Movimiento y transiciones sin ocultar detalles relevantes.
- Música solo con autorización o licencia documentada.
- Locución opcional; generar versión sin voz cuando no exista TTS o audio autorizado.
- Mezcla que priorice inteligibilidad de la voz.

`video-manifest.json` debe registrar escenas, duración, assets, texto, voz, música, licencias, resolución, codec y tiempo de render.

No prometer “voiceover” si el archivo final no lo contiene.

## Contrato de compliance

El subagente de compliance debe revisar:

- Fair Housing y segmentación.
- Privacidad y dirección pública autorizada.
- Exactitud de precio, estatus, HOA, CDD, impuestos e incentivos.
- Claims de financiamiento, ROI, apreciación y rentabilidad.
- Referencias a escuelas, seguridad, demografía y composición familiar.
- Disclosures del brokerage y Equal Housing Opportunity cuando aplique.
- Derechos de uso de fotos, música, logos y testimonios.
- Vigencia de datos temporales.
- Coherencia de claims entre piezas.

Clasificar cada hallazgo:

- `blocking`: impide aprobar o empacar.
- `warning`: requiere revisión humana explícita.
- `suggestion`: mejora recomendada.
- `passed`: control superado.

`compliance-report.json` debe incluir hallazgo, pieza, ubicación, regla, evidencia, severidad, responsable y acción requerida. El revisor no debe reescribir creativamente; devuelve el hallazgo al subagente responsable.

## Contrato de QA

QA realiza dos pasadas:

### QA semántico

- Cada claim coincide con su fuente.
- Todos los formatos muestran los mismos datos esenciales.
- Keywords, respuestas AEO y entidades GEO respetan la estrategia.
- No aparecen datos internos o privados.
- CTA y destino son correctos.
- No hay placeholders, campos vacíos ni texto de demostración.

### QA técnico

- Archivos existen, abren y tienen el formato esperado.
- Dimensiones y codec son correctos.
- Links, botones y QR funcionan.
- Imágenes conservan calidad suficiente.
- Email responde en móvil.
- Audio está sincronizado y sin clipping.
- ZIP contiene solo archivos aprobados.
- Checksums y versiones coinciden con el manifiesto.

`qa-report.json` debe registrar resultado por archivo, prueba, severidad, evidencia y estado final.

## Gates de aprobación

1. **Gate de estrategia:** audiencia, intención, posicionamiento, claims y KPIs aprobados.
2. **Gate de copy:** textos, CTA, fuentes y disclosures aprobados.
3. **Gate visual:** PDF, post, carrusel, story y email aprobados.
4. **Gate de video:** guion, voz, música, subtítulos y MP4 aprobados.
5. **Gate de compliance:** cero bloqueos y aceptación explícita de warnings.
6. **Gate final:** QA técnico y semántico aprobado antes del ZIP.

Un cambio posterior a un gate debe:

1. Crear nueva versión.
2. Identificar dependencias afectadas.
3. Invalidar solo esas salidas.
4. Repetir los gates correspondientes.

## Paquete final de seis piezas

El paquete descargable debe incluir:

1. `ficha-tecnica.pdf`.
2. `post-instagram.png` y `copy-instagram.txt`.
3. Cinco PNG del carrusel.
4. `story-instagram.png`.
5. `email.html`, `email.txt` y `subject.txt`.
6. `video-vertical.mp4` y `guion-video.txt`.

Incluir además:

- `estrategia-contenido.json`.
- `datos-propiedad.json` sin campos privados.
- `source-ledger.json` depurado para distribución.
- `package-manifest.json`.
- `README.txt` con uso, fecha, vigencia y advertencias.

No incluir archivos ficticios. Si el video falla, entregar las otras cinco piezas solo como `completed_with_warnings`, indicar la ausencia en el manifiesto y no declarar el paquete como completo.

## Manejo de fallos

- Aislar fallos por fase y pieza.
- Conservar salidas aprobadas.
- Reintentar máximo tres veces una causa técnica idéntica.
- Registrar error, evidencia, duración, intento y dependencia.
- Usar fallback solo si no altera la promesa: sin voz, plantilla alternativa compatible o paquete parcial identificado.
- No usar fallback para inventar datos, omitir compliance o ocultar errores.
- Escalar a revisión humana ante contradicciones, fuentes vencidas, derechos dudosos o claims sensibles.
- Estados permitidos: `completed`, `completed_with_warnings`, `failed` y `blocked`.
- Nunca empaquetar una pieza con hallazgo `blocking`.

## KPIs

Medir por propiedad y por pieza:

- Tiempo total y tiempo por fase.
- Porcentaje de paquetes completados.
- Tasa de éxito en primer render.
- Tasa de regeneración por pieza.
- Porcentaje de piezas aprobadas sin edición.
- Número de hallazgos blocking y warnings.
- Porcentaje de claims con fuente vigente.
- Incidentes de inconsistencia o privacidad.
- Costo estimado por paquete.
- Tiempo ahorrado frente al proceso manual.
- Uso o publicación de cada pieza.
- Engagement, clics, respuestas, leads y citas cuando existan datos.
- Conversión por CTA y canal.

Objetivos iniciales:

- 100% de claims sensibles trazables.
- 0 datos privados publicados.
- 0 archivos con errores técnicos en el ZIP final.
- ≥90% de piezas aprobadas con una sola ronda de ajustes.
- ≥95% de paquetes completados sin intervención técnica.

No declarar causalidad entre contenido y ventas sin un modelo de atribución válido.
