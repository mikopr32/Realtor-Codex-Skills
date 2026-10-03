# Contratos de subagentes

Usar un subagente distinto por fase. Entregar solo los artefactos aprobados y el contexto mínimo necesario. No pasar razonamiento privado.

## Contrato común

Cada asignación debe especificar:

```text
ROLE:
PROPERTY_ID:
OBJECTIVE:
INPUT_ARTIFACTS:
ALLOWED_TOOLS:
ALLOWED_ASSUMPTIONS:
REQUIRED_OUTPUTS:
SOURCE_REQUIREMENTS:
AUTHORIZATION_BOUNDARY:
DO_NOT_DO:
ACCEPTANCE_GATE:
```

Cada resultado debe contener:

```text
STATUS: completed|completed_with_warnings|blocked|failed
OUTPUTS:
FACTS_ADDED:
CLAIMS_ADDED:
WARNINGS:
BLOCKERS:
CONFIDENCE:
DEPENDENCIES_INVALIDATED:
NEXT_OWNER:
```

## Asignaciones

### Property Intake Agent

- Recibir formulario, archivos y objetivo.
- Producir `property-brief.json`.
- No navegar, investigar ni redactar contenido.
- Bloquear únicamente los campos definidos en el protocolo de intake.

### Property Verification Agent

- Recibir `property-brief.json` y fuentes suministradas.
- Producir `verified-property.json` y `verification-report.md`.
- No inferir un dato porque parezca probable.

### Market Intelligence Agent

- Recibir expediente verificado y geografía.
- Investigar micromercado, competencia y decisión del comprador.
- Producir ledger y briefs; no escribir assets.

### Search Intelligence Agent

- Recibir mercado, audiencia y objetivo.
- Mapear SEO/AEO/GEO por intención y funnel.
- No convertir Google Trends en volumen absoluto ni afirmar acceso inexistente.

### Content Strategy Agent

- Recibir facts, research y search intelligence.
- Elegir un ángulo principal, claims y función por formato.
- No crear hechos ni ejecutar diseño.

### Copy Agent

- Recibir estrategia y ledgers aprobados.
- Redactar con `claimId` y `sourceId`.
- No reabrir investigación.

### Design & Render Agent

- Recibir copy aprobado, fotos y branding.
- Producir assets estáticos y manifest.
- No reescribir claims para resolver overflow.

### Video & Voice Agent

- Recibir guion aprobado, inventario visual, música y voz.
- Producir MP4/manifest o fallback explícito.
- No usar música sin licencia.

### Compliance & QA Agent

- Recibir todos los manifests, archivos y ledgers.
- Auditar y enrutar errores al dueño.
- No corregir creativamente ni liberar con bloqueos.

## Paralelismo

Ejecutar Intake y Verification secuencialmente. Ejecutar Market y Search secuencialmente cuando Search dependa de mercado; permitir búsquedas exploratorias paralelas solo sin duplicar fuentes. Ejecutar Design y Video en paralelo después de Copy Gate. Ejecutar QA al finalizar ambos.

## Reintentos

Reintentar solo la fase fallida. Tras cambiar un hecho, consultar `claimId` para invalidar los assets dependientes. Detenerse después de tres fallos equivalentes.

