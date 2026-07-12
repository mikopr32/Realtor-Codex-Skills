---
name: real-estate-lead-qualification
description: Limpia, normaliza, deduplica lógicamente y califica listas completas de propietarios o seller leads desde CSV, TSV, XLSX exportado o archivos autorizados de Drive; valida teléfono y email, detecta absentee indicators, estima rangos de valor, deuda y equity, calcula Lead Priority Score y exporta archivos auditables. Usar cuando el usuario pida analizar, limpiar, filtrar, enriquecer estructuralmente, puntuar o preparar listas inmobiliarias para revisión o importación a CRM.
---

# Real Estate Lead Qualification

## Objetivo

Procesar todas las filas de una lista de propietarios, mejorar su calidad estructural y priorizar señales de prospección sin afirmar intención de venta. Entregar resultados completos, auditables y privados.

## Reglas esenciales

- Procesar todas las filas; no truncar ni mostrar PII innecesaria en el chat.
- No llamar `Seller Score` a una estimación de propensión. Usar `Lead_Priority_Score`.
- Separar valores observados, estimaciones, supuestos y errores.
- Tratar equity como rango estimado salvo que valor y deuda estén verificados.
- No contactar, publicar, subir ni sincronizar leads sin autorización explícita.
- No comprar, enriquecer o combinar datos externos sin autorización y fuente lícita.
- No usar clases protegidas, proxies discriminatorios ni atributos sensibles para puntuar.
- Conservar filas no contactables en un archivo de revisión; no eliminarlas silenciosamente.
- Guardar entregables en una ubicación privada dentro del entorno autorizado.

## Inputs

Aceptar CSV o TSV. Para XLSX, usar la skill de spreadsheets para convertir o leer el workbook sin pérdida de datos. Para Google Drive, usar el conector disponible y autorizado; si no existe acceso, pedir que el usuario adjunte el archivo.

Aceptar opcionalmente:

- Fecha de valoración.
- Mapeo explícito de columnas.
- Valor actual o saldo hipotecario verificados.
- Supuestos de apreciación, LTV, tasa y plazo.
- Reglas de scoring aprobadas.
- Suppression list u opt-outs.
- Formato de importación del CRM.

## Workflow

### 1. Inspeccionar sin exponer

Determinar encoding, delimitador, headers, número de filas, duplicados aparentes, campos vacíos y tipos. Mostrar solo estadísticas y ejemplos redactados. No pegar teléfonos, emails o direcciones completas en el chat.

### 2. Mapear columnas

Mapear, cuando existan:

- `Owner`
- `PropertyAddress`
- `MailingAddress`
- `SaleDate`
- `SalePrice`
- `Phone`
- `Email`
- `CurrentValue`
- `MortgageBalance`

Reconocer alias comunes y registrar el header original. Si dos columnas compiten por el mismo campo, elegir solo con evidencia; de lo contrario, solicitar el mapeo mínimo necesario o marcar ambigüedad.

### 3. Normalizar y validar

- Conservar texto original y crear valores normalizados.
- Parsear formatos de fecha comunes y marcar fechas futuras o inválidas.
- Convertir precios con moneda, comas o paréntesis contables.
- Normalizar teléfonos para comparación y validar longitud razonable.
- Validar sintaxis de email sin afirmar que el buzón existe.
- Normalizar direcciones para comparar, preservando unidades.
- Detectar duplicados por dirección/owner/contacto y marcarlos; no perder filas.
- Neutralizar CSV formula injection en cada celda exportada.

### 4. Determinar contactabilidad

Clasificar:

- `Both`: teléfono y email sintácticamente válidos.
- `Phone`: solo teléfono válido.
- `Email`: solo email válido.
- `None`: ninguno válido.

Exportar `Both`, `Phone` y `Email` como contactables. Enviar `None` a revisión/enriquecimiento, salvo instrucción diferente. Aplicar opt-outs y suppression lists antes de cualquier uso comercial posterior.

### 5. Calcular tiempo de propiedad

Calcular `Years_Owned` desde `SaleDate` hasta la fecha de valoración usando días/365.2425. Si falta o es inválida, dejar vacío y añadir flag. No convertir una fecha de mortgage, recording o transfer en sale date sin verificar su significado.

### 6. Estimar valor, deuda y equity

Priorizar:

1. Valor actual y saldo verificados proporcionados por el usuario.
2. AVM o public record autorizado, con fuente y fecha.
3. Escenarios transparentes a partir de SalePrice/SaleDate.

Si solo existen precio y fecha de compra, producir rangos `Low/Base/High`. Usar apreciación compuesta y amortización hipotecaria estándar con LTV, tasa y plazo declarados. No usar reducción lineal de deuda.

Calcular:

- `Estimated_Value_Low/Base/High`
- `Estimated_Debt_Low/Base/High`
- `Estimated_Equity_Dollars_Low/Base/High`
- `Estimated_Equity_Percent_Low/Base/High`
- `Equity_Method`
- `Equity_Confidence`

Equity bruto no equivale a net proceeds. No descontar closing costs, liens, repairs o concessions salvo solicitud expresa.

Leer `references/data-scoring-methodology.md` para interpretar escenarios, confidence y scoring.

### 7. Calcular Lead Priority Score

Usar bandas mutuamente excluyentes:

**Equity base — máximo 40**

- ≥60%: 40.
- 40–59.99%: 30.
- 20–39.99%: 15.
- <20% o no evaluable: 0.

**Antigüedad — máximo 25**

- <2 años: 0.
- 2–6.99: 5.
- 7–10: 15.
- 10.01–15: 20.
- >15: 25.

**Absentee indicator — máximo 20**

- Direcciones normalizadas claramente diferentes: 20.
- Diferencia incierta o falta una dirección: 10.
- Coinciden: 0.

**Contactabilidad — máximo 15**

- Both: 15.
- Phone: 10.
- Email: 8.
- None: 0.

Limitar el resultado a 0–100. Incluir `Score_Reasons`; no interpretar el score como probabilidad de vender.

### 8. Ejecutar el procesador

Usar `scripts/qualify_leads.py` para CSV/TSV. Pasar `--column-map` cuando el mapeo automático sea ambiguo. Mantener los supuestos predeterminados solo si el usuario no proporciona otros y revelarlos en el resumen.

Ejemplo:

```bash
python3 scripts/qualify_leads.py \
  --input leads.csv \
  --output-dir outputs/leads-qualified \
  --as-of 2026-07-11
```

### 9. Verificar resultados

Comprobar:

- `original_rows = contactable_rows + review_rows`.
- Todos los `Source_Row_ID` están presentes una sola vez.
- No se perdieron leading zeros.
- Scores están entre 0 y 100.
- Equity low ≤ base ≤ high cuando los escenarios permiten ese orden.
- No hay fórmulas activas en el CSV.
- Los outputs abren correctamente y mantienen encoding UTF-8 con BOM.

## Entregables

Crear una carpeta única con:

- `Qualified_Contactable_Leads.csv`: filas con al menos un contacto válido.
- `Review_Or_Enrichment_Required.csv`: filas no contactables o con errores críticos.
- `Processing_Summary.json`: conteos, mapeo, supuestos, flags y reconciliación.

El CSV debe incluir como mínimo:

`Source_Row_ID, Lead_Priority_Score, Score_Reasons, Contact_Type, Owner, PropertyAddress, MailingAddress, Phone, Email, SaleDate, SalePrice, Years_Owned, Absentee_Indicator, Estimated_Value_Low, Estimated_Value_Base, Estimated_Value_High, Estimated_Debt_Low, Estimated_Debt_Base, Estimated_Debt_High, Estimated_Equity_Dollars_Low, Estimated_Equity_Dollars_Base, Estimated_Equity_Dollars_High, Estimated_Equity_Percent_Low, Estimated_Equity_Percent_Base, Estimated_Equity_Percent_High, Equity_Method, Equity_Confidence, Duplicate_Flag, Data_Quality_Flags`.

Preservar las columnas originales después de las columnas calculadas, con prefijo `Source_` cuando sea necesario para evitar colisiones.

## Respuesta final

Mostrar únicamente:

- Total original.
- Contactables.
- Revisión/enriquecimiento.
- Duplicados señalados.
- Filas con equity evaluable.
- Distribución por prioridad.
- Supuestos principales.
- Enlaces a los tres entregables.

No mostrar contactos individuales salvo solicitud explícita.

## Quality gate

- Todas las filas están reconciliadas.
- El mapeo y las ambigüedades están documentados.
- Teléfono/email se consideran sintácticamente válidos, no verificados externamente.
- Deuda usa amortización o saldo verificado, no reducción lineal.
- Equity es rango y muestra método/confianza.
- Score no solapa bandas ni afirma intención.
- Duplicados y exclusiones permanecen auditables.
- PII permanece privada y no se ejecutó contacto.
- CSV formula injection fue neutralizada.
- Las acciones comerciales posteriores quedan sujetas a consentimiento, opt-outs, suppression lists y revisión de reglas aplicables.
