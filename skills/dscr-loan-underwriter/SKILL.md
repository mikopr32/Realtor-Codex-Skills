---
name: dscr-loan-underwriter
description: Analiza propiedades de inversión para préstamos DSCR mediante comparables de renta, renta elegible, pagos PITIA/HOA, escenarios de financiación, modeled lender DSCR, property-level DSCR, break-even rent, maximum loan amount y maximum acquisition price. Usar para evaluar preliminarmente si una propiedad puede cumplir un target DSCR, comparar programas, tasas o down payments, analizar una URL o preparar reportes para inversionistas, Realtors, lenders o loan officers.
---

# DSCR Loan Underwriter

## Objetivo

Estimar transparentemente si una propiedad podría cumplir los parámetros de un programa DSCR específico y qué combinación de renta, precio, down payment, tasa y gastos produce cobertura suficiente.

El resultado es pre-underwriting, no aprobación. La decisión corresponde al lender y depende de appraisal, product matrix, borrower, title, insurance y underwriting.

## Principios

- Separar datos verificados, estimaciones, supuestos y desconocidos.
- Diferenciar asking, leased, existing lease, appraiser market y lender-eligible rent.
- Diferenciar modeled lender DSCR de property-level DSCR.
- No imponer 1.25 como target universal ni afirmar “califica”.
- Definir exactamente qué incluye el qualifying monthly housing expense.
- No inventar tasa, taxes, insurance, HOA, rent o lender rules.
- No derivar market value u oferta únicamente del DSCR.
- Citar fuente, fecha, geografía, método y confidence.

## Fórmulas

`Modeled Lender DSCR = Eligible Monthly Rent / Qualifying Monthly Housing Expense`

El denominador puede incluir P&I, taxes, hazard, flood, HOA, mortgage insurance, ground lease, assessments u otros cargos según el programa.

`Property-Level DSCR = Annual NOI / Annual Debt Service`

Calcular NOI después de vacancy y operating expenses, antes de debt service, depreciation e income taxes. Mostrar ambas métricas sin mezclarlas.

## Inputs

Aceptar como mínimo URL o dirección. Incorporar cuando existan:

- Precio, tipo, specs, condición, HOA/CDD, taxes, insurance/flood, lease y restricciones.
- Loan amount/down payment, rate, term, amortization, IO period, points, fees y prepayment penalty.
- Target DSCR y product matrix.
- Vacancy, management, maintenance, CapEx, leasing, utilities y other income/expenses.

Si solo hay URL, realizar rent study preliminar y solicitar únicamente inputs financieros que cambien materialmente la simulación.

## Modos

- **Rent Study:** estimar renta sin conclusión hipotecaria.
- **Preliminary DSCR:** usar supuestos etiquetados.
- **Lender-Specific:** aplicar matrix o quote aportado.
- **Scenario Comparison:** comparar precio, rate, down payment o lender.
- **Existing Lease:** comparar lease, market, appraisal y eligible rent.

## Delegación multiagente opcional

Usar un solo underwriter para quick screen. Para underwriting completo, múltiples programas/lenders o varias propiedades, usar después de fijar un `ASSUMPTION_LEDGER` único:

- **Property/Cost Agent:** price, taxes, insurance, HOA y property identity.
- **Rent Agent:** rent comps y renta low/base/high.
- **Loan Matrix Agent:** rate, LTV, amortization, points, reserves y lender rules suministradas/verificadas.
- **Underwriting/QA Agent:** PITIA, lender DSCR, property DSCR, reverse DSCR y sensibilidad.

Property/Cost y Rent pueden trabajar en paralelo. Loan Matrix no calcula DSCR final hasta recibir renta y costos reconciliados. Solo Underwriting/QA emite ratios finales; no aceptar versiones distintas de PITIA o eligible rent. Si no hay subagentes, ejecutar por dependencias.

## Workflow

### 1. Verificar propiedad

Reconciliar dirección, URL, precio/historial, tipo, beds/baths, sqft, año, condition, furnished, pool/garage, HOA/CDD, taxes, insurance/flood, restrictions, lease y occupancy. Registrar contradicciones.

No reutilizar fotografías sin autorización; usar enlace o imagen autorizada.

### 2. Definir mercado de renta

Separar long-term, mid-term y STR; furnished/unfurnished; comunidad/microzona; lease term; utilities; seasonality y restricciones. No mezclar segmentos incompatibles.

### 3. Buscar rent comps

Buscar 3–6 comparables útiles, expandiendo misma comunidad → microzona → radio → fecha → características. Priorizar leased comps y leases verificables; usar active rentals como competencia y automated estimates como cross-check.

Registrar status, fecha, asking/leased rent, specs, condition, furnishing, utilities, concessions, lease term, fuente y confidence. No presentar asking como closed rent.

### 4. Ajustar y reconciliar renta

Evaluar location, type, beds/baths, sqft, condition, furnishing, pool/garage, utilities, amenities, duration, seasonality, concessions y fecha. Usar ajustes sustentados; si no, qualitative bracketing y rango más amplio.

Producir `Rent_Low/Base/High`, `Existing_Lease_Rent`, `Appraiser_Market_Rent`, `Lender_Eligible_Rent`, método y confidence. No inventar eligible rent sin lender rule.

### 5. Modelar préstamo y housing expense

Calcular P&I mediante amortización cuando no se proporcione. Mostrar purchase price, down, loan, rate, term, amortization, P&I, taxes, hazard, flood, HOA, other charges, total qualifying expense, cash to close y reserves conocidas.

Para IO, mostrar pago inicial y reset amortizing. Usar quote o fuente vigente para tasas.

### 6. Calcular DSCR

Calcular DSCR para low/base/high, existing lease, appraisal y lender-eligible rent. Comparar con target y pricing tiers del programa.

Clasificar `Exceeds modeled target`, `Meets modeled target`, `Near target`, `Below modeled target` o `Not evaluable`.

### 7. Calcular economía real

Calcular EGI, NOI, property-level DSCR, monthly cash flow, cap rate, cash-on-cash, break-even occupancy y rent. Alertar si lender DSCR cumple pero el cash flow económico es débil.

### 8. Reverse DSCR

Calcular required eligible rent, maximum qualifying housing expense, maximum P&I, maximum loan amount y DSCR-constrained maximum price.

Este precio es un límite financiero bajo supuestos, no market value ni oferta. Para oferta, revisar sales comps y condition.

### 9. Sensibilidad

Variar rent, rate, down/LTV, taxes, insurance/flood, HOA, vacancy y price. Identificar la variable que rompe el target y el margen de seguridad.

Usar `scripts/dscr_model.py` con inputs JSON para cálculos reproducibles. Leer `references/model-inputs.md` antes de prepararlos.

### 10. Evaluar product matrix

Cuando exista, revisar minimum DSCR, LTV, credit, property type, loan amount, reserves, prepayment, vesting, appraisal/rent calculation, STR, foreign national, cash-out/seasoning, IO y geography. Marcar Pass, Conditional, Fail o Unknown.

### 11. Recomendar acciones

Proponer mayor down, menor precio, otra rate/points, IO permitido, confirmar insurance/HOA, documentar rent, obtener appraisal/rent schedule o comparar lenders. No inflar leases, ocultar deudas ni falsificar ocupación.

## Formato de salida

# Preliminary DSCR Underwriting

Incluir fecha, propiedad, precio, rental type, lender/product, target y confidence.

1. Veredicto: lender DSCR, property DSCR, resultado, limitación y acción.
2. Property facts con fuente/fecha.
3. Rent comps con status, distancia, fecha, ajustes y fuente.
4. Rent reconciliation low/base/high/lease/appraisal/eligible.
5. Housing expense por componente.
6. Modeled lender DSCR por escenario.
7. Property economics por escenario.
8. Reverse DSCR y maximum constrained price.
9. Sensitivity matrix.
10. Product matrix checklist.
11. Riesgos.
12. Próximos pasos.
13. Fuentes, supuestos y confidence.

## Integración

- `$realestate-rental`: análisis profundo de NOI y cash flow.
- `$realestate-mortgage`: escenarios hipotecarios generales.
- `$realestate-invest`: estrategia integral de inversión.
- `$realestate-comps`: market value y oferta basada en ventas.

## Quality gate

- Property facts coinciden o las contradicciones están visibles.
- Asking rent no se confundió con leased rent.
- Segmentos de renta compatibles.
- Muestra suficiente o limitación explícita.
- Adjustments sustentados o cualitativos.
- Eligible rent y product rules no fueron inventados.
- Housing expense contiene cargos conocidos sin doble conteo.
- Lender y property DSCR están separados.
- Target es específico o supuesto visible.
- Resultado no promete aprobación.
- Reverse price no se presenta como value u offer.
- Cálculos son reproducibles y fuentes/fechas visibles.
