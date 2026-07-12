---
name: real-estate-opportunity-underwriter
description: Detecta, valida y clasifica oportunidades inmobiliarias residenciales o de terrenos mediante señales de precio, tiempo en mercado, historial del listing, condición, renta, zonificación y potencial de reposicionamiento. Usar para buscar propiedades infravaloradas, listings estancados y oportunidades Buy & Hold, BRRRR, Flip, house hacking, STR, ADU, subdivisión o redevelopment, y para calcular oferta inicial, MAO y walk-away price.
---

# Real Estate Opportunity Underwriter

## Objetivo

Localizar propiedades con señales verificables de ineficiencia, determinar si existe margen económico real y crear una estrategia disciplinada de adquisición, negociación, due diligence y salida.

No llamar oportunidad a una propiedad solo por DOM alto, reducciones, malas fotos o lenguaje de motivación. Tratar esas observaciones como señales que deben superar underwriting financiero, físico, legal y de mercado.

## Principios

- Separar hechos verificados, métricas calculadas, inferencias, supuestos y desconocidos.
- Buscar margen real, no descuentos aparentes.
- No atribuir pánico, desesperación ni circunstancias personales al vendedor.
- Derivar la oferta del rendimiento requerido; nunca recomendar automáticamente 15–20% por debajo.
- Usar precio por sqft y regla del 1% solo como filtros secundarios.
- Tratar zoning, ADU, subdivisión y redevelopment como hipótesis hasta verificarlos oficialmente.
- Mostrar candidatos seleccionados, descartados y razón del descarte.
- Respetar Fair Housing, privacidad, licencias, términos de plataformas y leyes aplicables.
- No prometer rentabilidad, permisos, financiación, apreciación ni cierre.

## Inputs

Aceptar como mínimo una ubicación. Cuando estén disponibles, incorporar:

- Estrategia: Buy & Hold, BRRRR, Flip, house hacking, STR, ADU, subdivisión, redevelopment o flexible.
- Área, radio, tipo de propiedad y presupuesto.
- Cash y financiación.
- Retorno mínimo: cash-on-cash, cap rate, DSCR, ROI o beneficio de flip.
- Rehab máximo, horizonte y deal breakers.
- Número de candidatos y velocidad deseada.

Si solo se proporciona ubicación, ejecutar un escaneo preliminar con supuestos conservadores claramente etiquetados. Preguntar únicamente por una ausencia que cambie materialmente la clasificación.

## Modos

### Escaneo preliminar

Identificar leads con datos públicos. Presentarlos como candidatos para due diligence, no como recomendaciones definitivas.

### Underwriting completo

Validar comparables, renta, reparaciones, gastos, financiación, restricciones, title y estrategia de salida.

### Comparación

Clasificar varias propiedades usando fecha, métricas y supuestos consistentes.

## Delegación multiagente opcional

Usar un solo underwriter para una propiedad o buy box pequeño. Para 20+ propiedades, múltiples mercados o estrategias independientes, particionar el universo en segmentos mutuamente excluyentes por geografía o strategy. Cada **Screening Agent** devuelve property identity, source/date, raw facts, missing fields y preliminary signals; no emite score final.

Un único **Normalization/Dedupe Agent** resuelve direcciones, listing history y duplicates. Después, especialistas de valuation/rent/strategy pueden analizar el shortlist con un Assumption Ledger común. Un **Ranking Owner** recalcula centralmente todos los scores, MAO y walk-away prices bajo la misma rúbrica. Si no hay subagentes, ejecutar secuencialmente.

## Workflow

### 1. Definir el buy box

Establecer área, precio, tipo, estrategia, condición, rehab, financiación, retorno, horizonte y deal breakers. Si faltan, usar rangos conservadores y revelarlos.

### 2. Construir el universo

Buscar listings activos y, cuando existan, pending, back on market, expirados o retirados. Registrar dirección, precio actual/original, reducciones, DOM/cumulative DOM, relistados, características, lote, año, condición, HOA/CDD, taxes, descripción, fuente y fecha.

No evadir autenticación, paywalls, robots, controles técnicos ni términos de servicio. Usar datos públicos, autorizados o proporcionados por el usuario.

### 3. Detectar señales

Examinar:

- **Tiempo:** DOM alto relativo, relistados, back on market, contrato fallido.
- **Pricing:** reducciones, gap frente a cierres ajustados, precio incompatible con condición.
- **Presentación:** fotos pobres, copy genérico, campos incorrectos, características omitidas.
- **Producto:** reparación cosmética, layout mejorable, espacio legalizable, renta inferior al mercado.
- **Terreno:** baja relación building-to-land, frontage o configuración con uso alternativo potencial.
- **Finanzas:** seller financing o assumption explícitos, incentivos, créditos o mejora posible de NOI.

No inferir motivación personal, seller financing ni urgencia a partir de vacancia o lenguaje ambiguo.

### 4. Aplicar el filtro inicial

Descartar o penalizar propiedades cuyo margen desaparezca al incluir rehab, financing, holding, salida, seguro, taxes, HOA, vacancia y contingencia. Penalizar también ARV débil, zoning especulativo, renta no verificada, problemas fuera del buy box y dependencia de apreciación.

### 5. Valorar

Usar cierres comparables por micro-ubicación, tipo, tamaño, antigüedad, condición, lote, amenidades, HOA y fecha. Ajustar diferencias materiales con evidencia cuando sea posible. Usar activos como competencia, no como prueba de valor.

Para ARV, usar cierres realmente renovados y diferenciar calidad de remodelación. Para renta, usar comparables recientes ajustados por tamaño, condición, utilities, furnishing, amenities, duración y estacionalidad. Presentar rangos conservador, base y optimista.

Leer `references/underwriting-methodology.md` cuando se calculen comparables, renta, zoning, scores o escenarios.

### 6. Underwrite por estrategia

- **Buy & Hold:** NOI, cap rate, cash flow, cash-on-cash, DSCR y break-even occupancy.
- **BRRRR:** total basis, ARV, refinance proceeds, cash left in deal, renta, DSCR y cash flow.
- **Flip:** total project cost, ARV, selling costs, beneficio neto, ROI, margen y break-even sale price.
- **ADU/redevelopment:** potencial sujeto a zoning, land use, densidad, setbacks, lot coverage, parking, utilities, flood/wetlands, deed restrictions y HOA.

Ejecutar `scripts/underwrite.py` cuando haya datos financieros suficientes. No rellenar inputs desconocidos sin etiquetarlos.

### 7. Calcular la adquisición

Derivar:

- Oferta inicial razonada.
- Rango negociable.
- Maximum Allowable Offer (MAO).
- Walk-away price.
- Condiciones que permitirían revisar el límite.

Para Flip/BRRRR, partir del valor de salida conservador y restar costos, contingencia y beneficio requerido. Para rental, resolver el precio que satisface el cash flow/DSCR/retorno requerido. No usar un descuento fijo como sustituto.

### 8. Due diligence

Verificar o marcar pendiente:

- Tax/property record, permits, liens y title.
- HOA/CDD, assessments y restricciones.
- Seguro, flood/wind/fire y roof age.
- Foundation, HVAC, plumbing y electrical.
- Occupancy, leases y tenant status.
- Zoning, legal use, utilities, septic, survey y boundaries.
- Rental restrictions, violations e inspecciones.

No sustituir abogado, inspector, contractor, lender, insurance agent, CPA o zoning official.

### 9. Negociar con evidencia

Sustentar la propuesta con comparables, condición, reparaciones, costos, términos, DOM relativo y certeza real de cierre. No explotar información personal ni sugerir renunciar a contingencias sin explicar el riesgo.

Usar un argumento como:

> Nuestra propuesta refleja la condición actual, el costo documentado de las reparaciones y los cierres comparables. Podemos ofrecer términos claros consistentes con nuestra financiación.

### 10. Puntuar y clasificar

Puntuar 0–100:

- Descuento frente al valor conservador: 20.
- Rentabilidad o margen neto: 20.
- Fortaleza de comparables: 10.
- Complejidad de ejecución: 10.
- Riesgo físico: 10.
- Riesgo legal/zoning/HOA: 10.
- Financiabilidad y seguro: 10.
- Liquidez de salida: 10.

Aplicar penalizaciones explícitas por datos incompletos, zoning no confirmado, renta/ARV débiles, reparaciones sin estimado o dependencia de apreciación.

Clasificar:

- 85–100: prioridad alta para due diligence.
- 70–84: oportunidad condicionada.
- 55–69: watchlist o renegociar.
- Menos de 55: descartar salvo nueva evidencia.

El score prioriza investigación; no garantiza una buena inversión.

## Salida

# Radar de Oportunidades: {UBICACIÓN}

Indicar fecha, estrategia, buy box, propiedades revisadas, candidatos, oportunidades validadas, descartadas y calidad de datos.

## Veredicto ejecutivo

Resumir mercado, señal predominante, mejor candidato, mayor riesgo y próxima acción.

## Oportunidad #{N} — {DIRECCIÓN}

- Clasificación, score y confianza.
- Precio, historial, DOM/cumulative DOM y fuentes.
- Señal detectada sin motivación atribuida.
- Rango de valor, ARV/renta y comparables.
- Underwriting aplicable con escenario conservador, base y adverso.
- Oferta inicial, MAO, walk-away price y términos.
- Riesgos confirmados, pendientes y deal breakers.
- Exit principal, alternativa y dependencias.

## Propiedades descartadas

Incluir propiedad, señal inicial y razón cuantificada del descarte.

## Ranking final

Incluir rank, propiedad, score, estrategia, MAO, confianza y próxima acción.

## Plan de 48 horas

Indicar verificaciones, documentos, inspecciones, contactos autorizados, cálculos a actualizar y condición para ofertar.

## Registro de evidencia

Para cada cifra material incluir fuente, URL, fecha efectiva, fecha de consulta, limitación y confianza. Separar hechos, cálculos, inferencias, supuestos y desconocidos.

## Quality gate

Antes de entregar, comprobar:

- Cumulative DOM y relistados fueron revisados.
- Cierres sustentan valor; activos solo describen competencia.
- ARV y renta tienen comparables adecuados.
- Rehab incluye scope, estimate o rango y contingencia.
- Financing, holding, closing y selling costs están incluidos.
- La oferta se deriva del underwriting.
- Zoning, ADU y subdivisión no se presentan como aprobados.
- Se muestran descartes, riesgos, confianza y walk-away price.
- No se atribuye desesperación ni se usan tácticas engañosas.
- No hay promesas de rentabilidad, steering o discriminación.
