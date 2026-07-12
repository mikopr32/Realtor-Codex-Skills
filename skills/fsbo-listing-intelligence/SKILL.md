---
name: fsbo-listing-intelligence
description: Descubre, verifica, normaliza y prioriza listings públicos For Sale by Owner (FSBO) por ciudad, ZIP code o área; diferencia FSBO real de listings con agente, flat-fee MLS, anuncios inactivos y duplicados; registra precio, historial visible, tiempo de publicación, contacto público o canal interno, fuentes y confianza; y prepara borradores de primer contacto sin enviarlos. Usar para investigación FSBO, buyer inventory, prospección autorizada, preparación de llamadas y creación de listas privadas para revisión o CRM.
---

# FSBO Listing Intelligence

## Objetivo

Descubrir propiedades públicamente anunciadas como FSBO, confirmar actividad y representación aparente, consolidar duplicados, priorizar mediante evidencia y preparar borradores respetuosos de contacto.

## Principios

- Tratar un FSBO público como inventario públicamente anunciado, no automáticamente off-market.
- Verificar cada resultado; “By Owner & Other” no prueba FSBO.
- Separar posted age, visible DOM y cumulative market time.
- No atribuir desesperación, urgencia o motivación personal.
- No inventar compradores, relaciones, cooperación ni disposición a pagar.
- No evadir autenticación, CAPTCHA, paywalls, robots o limitaciones técnicas.
- No revelar, enriquecer ni buscar contactos ocultos. Conservar en privado solo el contacto publicado para la transacción.
- No llamar, enviar mensajes, completar formularios, publicar ni cargar al CRM sin autorización explícita.
- Respetar Fair Housing, privacidad, advertising rules, brokerage policy, opt-outs y reglas aplicables al outreach.

## Inputs

Aceptar como mínimo `{UBICACIÓN}`. Aceptar opcionalmente radio, tipo, precio, beds/baths, buy box, propósito, cantidad, datos del agente, idioma, suppression list y formato CRM.

Modos:

- **Buyer Inventory:** buscar coincidencias para criterios reales. Solo mencionar un comprador si está confirmado.
- **Listing Prospecting:** preparar una oferta de valor sin pedir inmediatamente el listing.
- **Investor Search:** transferir candidatos a `$real-estate-opportunity-underwriter`.
- **Research Only:** investigar sin guiones ni recomendación de contacto.

## Delegación multiagente opcional

Usar un solo agente para una zona pequeña. Para múltiples fuentes, ZIP codes o muestras grandes, particionar discovery por fuente o geografía sin solapamiento. Cada **Discovery Agent** devuelve address raw/canonical candidate, source URL, observed date, asking price, claimed status y public contact channel; no puntúa ni prepara outreach.

Después, un único **Verification/Dedupe Agent** resuelve identidad, active/inactive, true FSBO, flat-fee/agent representation, duplicate cluster y observed age. Solo tras esa barrera un **Scoring Agent** prioriza y un **Compliance/Draft Agent** prepara borradores autorizados. Suprimir status incierto, representación activa y opt-outs. Si no hay subagentes, ejecutar secuencialmente.

## Workflow

### 1. Definir alcance

Establecer geografía, tipo, rango, propósito, fecha de corte, máximo de candidatos y criterios obligatorios. No mezclar áreas sin explicarlo.

### 2. Investigar fuentes accesibles

Buscar en portales con filtros FSBO, sitios especializados, clasificados, sitios personales y búsqueda web. Usar Marketplace o sesiones autenticadas únicamente cuando estén autorizadas y la navegación sea permitida.

Abrir la fuente original. No tratar snippets como evidencia. Registrar fuentes inaccesibles o bloqueadas y no afirmar cobertura exhaustiva.

### 3. Verificar candidatos

Confirmar URL, fuente, fecha de consulta, status, fecha publicada/actualizada, dirección o ubicación, precio, características, evidencia FSBO, anunciante, canal público y posible representación.

Clasificar:

- `Verified_FSBO`
- `Probable_FSBO`
- `Flat_Fee_MLS_FSBO`
- `Agent_Represented`
- `Representation_Unknown`

Excluir del reporte principal sold, removed, rental, auction-only, preforeclosure sin venta activa, Make Me Move, scam aparente y agent-represented. Tratar pending como monitoreo salvo solicitud distinta. Conservar todo descarte con razón.

### 4. Resolver tiempo de mercado

Registrar por separado:

- `Posted_Date`
- `Last_Updated`
- `Posted_Age_Days`
- `Visible_DOM`
- `Cumulative_Market_Time`
- `DOM_Confidence`

No llamar DOM a la edad del anuncio. Revisar relistados y contradicciones. Usar `Unknown` cuando no pueda verificarse.

### 5. Capturar datos responsablemente

Extraer dirección publicada, precio, características, descripción relevante, fechas, historial visible, contacto expresamente publicado, canal interno y URL.

Si no hay teléfono o email público, registrar `Internal_Messaging_Only`. No realizar reverse lookup ni descubrir información oculta.

### 6. Normalizar y deduplicar

Normalizar dirección, precio, teléfono para comparación, URL, fechas, status y representación. Consolidar por dirección/parcel/características y conservar URLs adicionales e información contradictoria.

Usar `scripts/compile_fsbo.py` para puntuar y exportar una colección JSON ya investigada. Leer `references/research-schema.md` antes de preparar el JSON.

### 7. Evaluar fit

Cuando exista buy box, comparar ubicación, precio, tipo, beds/baths, sqft, lote, condición, HOA, restricciones y características. No declarar match con información insuficiente.

En listing prospecting, detectar oportunidades de aportar pricing review, net proceeds comparison, safety checklist, marketing gap audit o buyer feedback; no utilizar presión.

### 8. Puntuar

Calcular `FSBO_Research_Priority_Score` de 0–100:

- Verificación y actividad: 25.
- Frescura de verificación: 15.
- Buyer fit o utilidad: 20.
- Señales de posicionamiento verificadas: 15.
- Calidad del registro: 15.
- Canal público: 10.

Clasificar 80–100 alta, 60–79 media, 40–59 monitoreo y <40 baja. El score organiza investigación; no predice respuesta, contratación o motivación.

### 9. Crear borradores

Solo preparar borradores para listings activos y verificables.

**Buyer real confirmado:**

> Hola, soy {NOMBRE}, Realtor con {BROKERAGE}. Vi la propiedad que publicaste en {FUENTE}. Estoy trabajando con un comprador cuyos criterios podrían coincidir con algunas de sus características. ¿Sigue disponible y estarías dispuesto a cooperar con un agente que represente exclusivamente al comprador? Antes de continuar, quisiera confirmar las condiciones de acceso, representación y compensación aplicables.

**Listing prospecting:**

> Hola, soy {NOMBRE}, Realtor con {BROKERAGE}. Vi que estás comercializando la propiedad en {ÁREA} directamente. Respeto que hayas decidido venderla por tu cuenta. Preparé una breve lista de factores que suelen afectar exposición, seguridad de showings y net proceeds. Si te resulta útil, puedo compartirla sin compromiso. ¿Prefieres que te la envíe por este canal?

No enviar. Para secuencias completas usar `$realtor-fsbo-expired-scripts`.

## Entregables

- `FSBO_Verified_Leads.csv`: candidatos activos con contacto privado.
- `FSBO_Excluded_Or_Unverified.csv`: descartes y verificación pendiente.
- `FSBO_Source_Ledger.csv`: fuentes, fechas, contradicciones y confianza.
- `FSBO_Outreach_Drafts.md`: borradores autorizados, nunca enviados.
- `FSBO_Research_Summary.json`: cobertura, conteos y limitaciones.

No mostrar teléfonos o emails en el chat. Presentar solo conteos, cobertura, ranking sin PII, limitaciones y enlaces privados.

## Integración

- `$real-estate-lead-qualification`: preparar lista para CRM.
- `$real-estate-opportunity-underwriter`: evaluar inversión.
- `$realestate-comps`: estudiar valor.
- `$realtor-fsbo-expired-scripts`: crear cadencia completa.
- `$realestate-screen`: buscar por buy box amplio no limitado a FSBO.

## Quality gate

- Cada candidato tiene URL y fecha de consulta.
- El status se verificó en la fuente original.
- FSBO real se separó de “By Owner & Other”.
- DOM no se confundió con posted age.
- Relistados y duplicados fueron revisados.
- Contactos proceden del anuncio o canal autorizado.
- No se buscó información oculta ni se mostró PII en chat.
- El score está explicado y no afirma motivación.
- Los guiones no inventan compradores o resultados.
- No se ejecutó contacto, CRM upload o publicación.
- Fuentes bloqueadas y limitaciones están registradas.
- Cualquier outreach futuro requiere suppression/opt-out checks y revisión aplicable.
