---
name: analisis-de-comunidades
description: Investiga y genera dossiers verificables sobre subdivisiones, condominios, edificios, resorts y comunidades residenciales específicas. Usar cuando el usuario pida analizar una comunidad, conocer HOA o CDD, verificar restricciones de alquiler, revisar impuestos, amenidades o escuelas asignadas, evaluar compatibilidad residencial o de inversión, o crear un one-sheet o PDF para compradores, vendedores, Realtors y campañas de micro-farming.
---

# Análisis de Comunidades

Generar un perfil exhaustivo, neutral y respaldado por fuentes de una comunidad residencial específica. Ayudar al usuario a decidir si encaja con sus necesidades; no intentar persuadirlo para que compre.

## Principios obligatorios

- Separar hechos confirmados, estimaciones, contradicciones e información anecdótica.
- Citar con enlace directo y fecha de consulta cada dato importante.
- Priorizar documentos oficiales; no inventar ni completar mediante suposiciones.
- Explicar cuándo una cifra depende de la parcela, unidad, sección, tipo de vivienda o membresía.
- Informar discrepancias sin elegir silenciosamente la cifra más conveniente.
- Mantener neutralidad y cumplir Fair Housing.
- Presentar información legal, fiscal, escolar y financiera como informativa, no como garantía profesional.
- Buscar información vigente. Incluir el año o fecha del dato y verificar temporalmente todo lo susceptible de cambiar.

## Input y alcance

Aceptar como mínimo nombre de la comunidad y ciudad; identificar también estado y condado. Aceptar opcionalmente dirección, unidad, tipo de propiedad, precio, objetivo de uso y formato deseado.

Antes de investigar:

1. Confirmar nombre oficial, nombres comerciales, ciudad, condado y código postal.
2. Distinguir comunidades homónimas y no mezclar datos.
3. Identificar asociación maestra, subasociaciones, fases, edificios y tipos de propiedad.
4. Solicitar dirección exacta solo si la ambigüedad impide avanzar o el usuario necesita cifras parcelarias.
5. Sin dirección, elaborar un perfil general y marcar HOA, CDD, impuestos, escuelas y restricciones como potencialmente variables.

## Jerarquía de fuentes

Priorizar en este orden:

1. Documentos de HOA/condominio, estoppel, presupuestos, CDD, Property Appraiser, Tax Collector, ordenanzas, mapas de zonificación, distrito escolar, FEMA y otras agencias oficiales.
2. MLS, administrador oficial, desarrollador, operador del resort, club o amenidad.
3. Zillow, Realtor.com, Redfin, Homes.com, GreatSchools, Niche y medios locales reconocidos.
4. Reddit, City-Data, reseñas, grupos públicos y foros, únicamente como evidencia anecdótica.

No usar una fuente anecdótica como evidencia única de un hecho financiero, legal, escolar o regulatorio. No tratar un resumen generado por buscador como fuente final.

## Etiquetas de confianza

Asignar una etiqueta a cada hallazgo importante:

- **Confirmado:** fuente oficial o documento vigente.
- **Alta confianza:** varias fuentes profesionales consistentes.
- **Estimado:** inferencia transparente basada en información reciente.
- **Anecdótico:** experiencia u opinión pública de residentes.
- **No verificado:** información no validada adecuadamente.
- **Contradictorio:** fuentes confiables discrepan.

## Delegación multiagente opcional

Usar un solo agente para una pregunta concreta. Para dossier completo, comparación de 2+ comunidades o múltiples asociaciones/fases, dividir después de fijar identidad y alcance:

- **Governance/Cost Agent:** HOA, condo association, CDD, assessments, budgets y documentos.
- **Use/Restriction Agent:** alquiler, ocupación, pets, estacionamiento y reglas aplicables.
- **Location/School Agent:** escuelas asignadas, conectividad y amenidades objetivas.
- **Risk Agent:** taxes, flood, insurance, litigation/assessments visibles y unknowns.

Cada worker devuelve scope exacto —community, association, phase, parcel, building o unit—, fuente, fecha, applicability y confidence. Un editor único reconcilia contradicciones y no generaliza una regla de una fase a toda la comunidad. Si no hay subagentes, ejecutar secuencialmente.

## Flujo de investigación

### 1. HOA, condominio y costos recurrentes

Investigar HOA, master association, subasociación, condominio, club, iniciación, transferencia, capital contribution, special assessments y solicitudes. Indicar frecuencia, servicios incluidos, exclusiones y vigencia.

Convertir a equivalente mensual cuando ayude, conservando la frecuencia real. No asumir que una cuota aplica a todas las propiedades.

Si no existe cifra oficial vigente:

1. Comparar al menos tres listados recientes cuando sea posible.
2. Usar propiedades del mismo tipo, sección y asociación.
3. Reportar rango y explicar diferencias.
4. Etiquetar: **Estimado basado en listados recientes; confirmar mediante estoppel y documentos de la asociación.**

### 2. CDD y assessments

Confirmar nombre del CDD, assessment anual, deuda y operaciones, vencimiento estimado y presencia en la factura fiscal. Para una dirección, priorizar tax bill y parcela. Sin dirección, reportar rangos o ejemplos y advertir que varía por lote.

### 3. Impuestos, flood zone y seguro

Investigar millage, assessed value, exenciones, non-ad valorem assessments, CDD y flood zone. Distinguir impuesto actual del vendedor de la posible cifra posterior a la compra. No proyectar impuestos futuros usando solamente el tax bill actual. Tratar costos de seguro como estimados salvo cotización específica.

### 4. Restricciones de alquiler y uso

Separar:

- Regulación pública: zonificación, licencias, registros y ocupación.
- Restricciones privadas: minimum lease term, alquileres por año, aprobación, plataformas, subarrendamiento, programas obligatorios y reglas de la subasociación.

No concluir que STR está permitido basándose solo en un anuncio. Clasificar como: confirmado, permitido con condiciones, largo plazo, restringido, no confirmado o requiere revisión documental/legal. Si gobierno y asociación difieren, destacar la limitación operativa más restrictiva sin emitir asesoría legal.

### 5. Amenidades y acceso

Verificar clubhouse, piscinas, parques acuáticos, gimnasio, canchas, senderos, lagos, restaurantes, seguridad, transporte, golf, spa, áreas infantiles, mascotas y eventos. Indicar si cada amenidad está incluida, tiene cargo, requiere membresía, es pública, privada, exclusiva o de un tercero.

Para golf, confirmar campo, modalidad de acceso, membresía y relación real con la comunidad. No presentar una amenidad cercana como parte de la comunidad.

### 6. Escuelas

Priorizar la herramienta oficial del distrito para elementary, middle y high school. Identificar ratings externos como tales, con fuente y fecha. Diferenciar escuelas zonificadas de charter, magnet y opciones cercanas.

Incluir siempre: **La asignación escolar puede cambiar; confirmar con el distrito usando la dirección exacta.**

### 7. Ubicación y conectividad

Reportar millas y tiempos aproximados hacia aeropuerto, hospitales, supermercados, autopistas, centros de empleo y atracciones pertinentes. Indicar que los tiempos dependen de tráfico, hora y ruta. No presentarlos como garantía.

### 8. Experiencia residencial

Buscar patrones en foros, reseñas y noticias. Distinguir elogios recurrentes, quejas recurrentes, observaciones aisladas y problemas confirmados. No identificar usuarios ni reproducir acusaciones no verificadas.

Presentar un insider insight solo cuando resulte útil:

- Hallazgo.
- Tipo de evidencia.
- Número o diversidad aproximada de fuentes.
- Acción práctica para verificarlo.

### 9. Riesgos y consideraciones

Revisar special assessments, litigios públicos, construcción futura, reparaciones, estacionamiento, vehículos, mascotas, reglas arquitectónicas, flood zone, evacuación, ruido, tráfico, membresías y cambios regulatorios. Evitar alarmismo; explicar impacto y puntos pendientes.

## Manejo de contradicciones

Cuando las fuentes difieran:

1. Mostrar cifras o afirmaciones contrapuestas con fuente y fecha.
2. Explicar posibles causas: vigencia, sección, asociación o tipo de propiedad.
3. Priorizar la fuente oficial más reciente.
4. Mantener la etiqueta **Contradictorio** si no puede resolverse.
5. Indicar el documento o contacto necesario para confirmarlo.

## Fair Housing

- Describir características objetivas, costos, accesibilidad, reglas y amenidades.
- No recomendar según raza, religión, nacionalidad, sexo, discapacidad, situación familiar u otra clase protegida.
- No describir composición demográfica para orientar una decisión.
- No declarar que una zona es “segura” sin fuente oficial y contexto.
- Evitar “perfecta para familias”, “ideal para jóvenes” y lenguaje equivalente.
- Permitir que el comprador evalúe personalmente la compatibilidad.

## Salida obligatoria

Generar un resumen ejecutivo y un apéndice de verificación.

### One-sheet

# Perfil de Comunidad: {NOMBRE}

**Ubicación:** {CIUDAD, CONDADO, ESTADO}  
**Tipo:** {SUBDIVISIÓN/CONDOMINIO/RESORT/EDIFICIO}  
**Investigado:** {FECHA}  
**Confianza general:** {ALTA/MODERADA/LIMITADA}

## Veredicto rápido

Resumir neutralmente la principal fortaleza, costo o restricción, usos objetivamente compatibles y dato crítico pendiente. No recomendar definitivamente si falta información esencial.

## Los números

| Concepto | Cantidad | Frecuencia | Incluye | Confianza |
|---|---:|---|---|---|
| HOA principal | — | — | — | — |
| Subasociación | — | — | — | — |
| CDD | — | Anual | — | — |
| Club/membresía | — | — | — | — |
| Otros assessments | — | — | — | — |

Indicar costo recurrente mensual estimado y exclusiones.

## Política de alquiler

Indicar clasificación, regulación pública, restricción privada, minimum lease term, licencias y pendiente de confirmación.

## Escuelas asignadas

| Nivel | Escuela | Rating externo | Zonificación |
|---|---|---:|---|
| Elementary | — | — | Confirmada/Estimada |
| Middle | — | — | Confirmada/Estimada |
| High | — | — | Confirmada/Estimada |

## Amenidades y ubicación

Destacar amenidad estrella, acceso, costos y distancias relevantes.

## Lo que conviene verificar antes de comprar

Enumerar de tres a seis verificaciones accionables.

## Insider insight

Indicar hallazgo, base de evidencia y acción recomendada. Omitir si no existe evidencia suficiente.

## Compatibilidad por objetivo

| Objetivo | Compatibilidad | Razón |
|---|---|---|
| Residencia principal | Alta/Media/Baja/No evaluable | — |
| Segunda vivienda | Alta/Media/Baja/No evaluable | — |
| Alquiler largo plazo | Alta/Media/Baja/No evaluable | — |
| Alquiler corto plazo | Alta/Media/Baja/No evaluable | — |

### Apéndice de verificación

Incluir una tabla con dato, fuente enlazada, fecha del dato, fecha de consulta y confianza. Añadir secciones de información contradictoria, información no disponible y documentos recomendados: estoppel, presupuesto, estados financieros, declaración y enmiendas, reglas, actas, assessments, tax bill, seguro, CDD, alquileres y confirmación escolar.

## PDF

Si el usuario pide PDF, generar primero el contenido verificado, crear una portada one-sheet y colocar fuentes en páginas posteriores. Renderizar y revisar visualmente antes de entregar; corregir tablas cortadas, URLs desbordadas y texto ilegible.

## Quality Gate

No entregar hasta comprobar:

- Comunidad e identidad correctas.
- Fechas visibles y fuentes directas.
- HOA y CDD no universalizados sin evidencia.
- Impuestos actuales diferenciados de estimaciones futuras.
- Reglas públicas y privadas de alquiler separadas.
- Escuelas verificadas oficialmente cuando sea posible.
- Acceso y costo de amenidades claros.
- Opiniones etiquetadas como anecdóticas.
- Contradicciones y datos faltantes visibles.
- Lenguaje neutral y compatible con Fair Housing.
- Ningún dato inventado.

Cerrar con: **Este dossier es informativo y se basa en fuentes disponibles en la fecha indicada. Cuotas, restricciones, impuestos, escuelas, amenidades y regulaciones pueden cambiar. Confirmar mediante documentos oficiales, estoppel, la asociación, autoridades y asesores profesionales antes de decidir.**
