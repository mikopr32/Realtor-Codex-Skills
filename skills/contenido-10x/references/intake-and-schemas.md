# Intake, validación y contratos de datos

Usar este documento durante las fases **Intake** y **Verificación**. No investigar mercado, generar estrategia ni redactar contenido hasta completar los bloqueos aplicables.

## Índice

1. Principios operativos
2. Intake obligatorio
3. Intake recomendado
4. Intake condicional
5. Clasificación de datos
6. Reglas de bloqueo
7. Fair Housing y privacidad
8. Contrato `property-brief.json`
9. Contrato `verified-property.json`
10. Entrega entre fases

## 1. Principios operativos

1. Solicitar primero la información indispensable en una sola ronda consolidada.
2. Permitir `unknown` cuando el Realtor desconozca un dato; nunca rellenarlo por intuición.
3. Separar información pública, interna y restringida.
4. Registrar la procedencia de cada hecho: usuario, MLS, documento, URL o fuente oficial.
5. Mantener el texto original del usuario y el valor normalizado cuando sean diferentes.
6. No convertir opiniones, feedback de showings ni hipótesis en hechos.
7. Marcar contradicciones sin elegir silenciosamente una versión.
8. Pedir aprobación humana para datos sensibles, incentivos, financiamiento y claims condicionados.
9. Aplicar minimización de datos: recopilar solo lo necesario para producir las piezas autorizadas.
10. No usar datos del vendedor, ocupantes, prospectos o visitantes para segmentación o contenido.

## 2. Intake obligatorio

### Identificación y autorización

- Nombre interno del proyecto.
- Dirección completa privada para investigación y verificación.
- Dirección o ubicación pública autorizada: dirección completa, comunidad + ciudad, ciudad solamente o confidencial.
- Tipo de operación: venta o alquiler.
- Tipo de propiedad.
- Estatus del listing y fecha de vigencia.
- Confirmación de que el Realtor está autorizado para mercadear la propiedad.
- Confirmación de derechos de uso de fotografías, video, música, logotipo y testimonios.
- Fuente principal de los datos: MLS, builder, propietario, appraisal u otra.

### Datos públicos esenciales

- Precio y fecha de vigencia.
- Ciudad, estado y ZIP.
- Bedrooms, full bathrooms y half bathrooms.
- Living area y unidad.
- Año de construcción, o `unknown`.
- Tres fotografías como mínimo para el paquete completo.
- Fotografía principal autorizada.
- Tres a cinco características verificables que deben destacarse.
- URL pública o CTA alternativo.

### Objetivo y distribución

- Objetivo: nuevo listing, open house, reducción, relanzamiento, estilo de vida, inversión documentada, nueva construcción, 55+ u otro.
- Audiencia definida por necesidad o intención, no por clase protegida.
- Etapa del funnel: descubrimiento, consideración o acción.
- Idioma: español, inglés o bilingüe.
- Canales que se producirán.
- CTA principal y destino.
- Fecha objetivo de publicación.
- KPI principal.

### Profesional y cumplimiento

- Nombre del agente.
- Brokerage.
- Teléfono o email público.
- Disclosures provistos por el brokerage o el usuario.
- Reglas internas del brokerage que deban respetarse.
- Confirmación de si requiere aprobación antes de exportar o publicar.

## 3. Intake recomendado

Solicitarlo cuando mejore la precisión sin bloquear innecesariamente:

- MLS ID y URL del listing.
- Lot size, garage spaces, pool, waterfront, furnished y otras características.
- HOA, CDD, property taxes y qué incluye cada cargo.
- Floor plan, survey, seller disclosure o documentos del builder.
- Descripción actual del listing.
- Diferenciador principal según el Realtor.
- Feedback agregado y no identificable de showings.
- Preguntas y objeciones escuchadas.
- Propiedades, comunidades o builders que el Realtor considera competencia.
- Reducciones de precio y fechas.
- Inventario, vistas, saves, inquiries y showings disponibles.
- Presupuesto y radio geográfico de promoción.
- Branding: logotipo, foto profesional, colores, tipografías, website e Instagram.
- Tono deseado y palabras que no deben usarse.
- Pronunciación de nombres para voiceover.
- Materiales anteriores y métricas históricas.

La ausencia de estos datos reduce el nivel de confianza; no autoriza inferencias.

## 4. Intake condicional

| Situación | Datos exigidos antes de usar el claim o producir la pieza |
|---|---|
| Open house | Fecha, horario, zona horaria, instrucciones de acceso, registro y aprobación del seller/brokerage |
| Reducción de precio | Precio anterior, nuevo precio, fecha efectiva y autorización para comunicar ambos |
| Nueva construcción | Builder, comunidad, modelo, disponibilidad, incentivos, condiciones, fecha de expiración y fuente oficial |
| Comunidad 55+ | Confirmación oficial, nombre legal de la comunidad y restricciones comunicables |
| Oportunidad de inversión | Rentas, gastos, restricciones, ocupación y proyecciones documentadas; distinguir real de estimado |
| Financiamiento | Lender, tasa/APR, puntos, down payment, condiciones, fecha de vigencia y disclaimer |
| HOA o CDD | Monto, frecuencia, periodo, fuente y qué incluye; no asumir que una cuota incluye servicios |
| Escuelas | Fuente oficial, fecha y zonificación; no usar ratings como garantía ni lenguaje de preferencia familiar |
| Seguridad o crimen | No usar en contenido promocional. Si el usuario insiste, escalar a revisión de compliance |
| Alquiler | Depósito, plazo, disponibilidad, utilities, mascotas y criterios legales aprobados |
| Música o voz | Archivo/licencia, idioma, pronunciación y permiso de uso |
| Seller u ocupante presente | Restricciones de privacidad, fotografía, horarios e información que no puede divulgarse |
| Coming Soon | Fecha autorizada y reglas vigentes de MLS y brokerage |
| Publicidad pagada | Objetivo, presupuesto, geografía permitida, privacy policy y requisitos de Special Ad Category/Housing |
| Testimonio | Texto aprobado, identidad autorizada y permiso expreso de publicación |

## 5. Clasificación de datos

Asignar una sola clasificación principal a cada campo y conservar historial de cambios.

### `confirmed`

Dato respaldado por una fuente aceptable y vigente, o confirmado directamente por la parte autorizada cuando esa sea la fuente apropiada.

Ejemplos: precio vigente en MLS; HOA documentado; horario aprobado de open house.

### `needs_verification`

Dato plausible pero sin evidencia suficiente, desactualizado, contradictorio o pendiente de confirmar.

Regla: puede permanecer en el expediente interno, pero no publicarse como hecho.

### `agent_assumption`

Hipótesis estratégica u opinión no verificable.

Ejemplos: “probable comprador relocator”, “la cocina es el mayor diferenciador”. Mantener claramente separada de los hechos; nunca convertirla en claim factual.

### `private`

Dato necesario para operar o investigar, pero no autorizado para piezas públicas.

Ejemplos: dirección privada, instrucciones de acceso, identidad del seller, teléfono personal, códigos, documentos internos.

### `prohibited`

Dato o uso que no debe procesarse para segmentación o contenido por razones legales, éticas, contractuales o de seguridad.

Ejemplos: clase protegida real o inferida, código de acceso publicado, claim discriminatorio, datos médicos o migratorios, promesa financiera no sustentada.

## 6. Reglas de bloqueo

### Bloqueo total

Detener el workflow y solicitar corrección cuando ocurra cualquiera de estos casos:

- Falta autorización para mercadear o usar los activos.
- No existe un contacto profesional público.
- La propiedad no puede identificarse con precisión para verificación interna.
- El usuario solicita segmentar, excluir o describir personas por una clase protegida.
- Existe riesgo de publicar datos privados, códigos o información de seguridad.
- Se solicita inventar, ocultar deliberadamente o alterar un hecho material.

### Bloqueo de investigación

No iniciar investigación profunda cuando falten:

- Dirección privada o micromercado identificable.
- Tipo de propiedad.
- Precio o rango autorizado.
- Estatus y fecha de vigencia.

Permitir investigación limitada si el usuario autoriza explícitamente trabajar solo a nivel ciudad o comunidad; etiquetar el alcance reducido.

### Bloqueo de claim o pieza

Bloquear únicamente el claim o activo afectado cuando:

- Precio, incentivo, tasa, open house o disponibilidad no estén vigentes.
- HOA, CDD, impuestos, escuelas, permisos o restricciones carezcan de fuente.
- Haya contradicción entre MLS, usuario y documentos.
- Falten disclosures exigidos.
- Haya menos de tres fotos para el paquete completo.
- No exista licencia de música o voz.

Continuar con las demás piezas cuando sea seguro y mostrar `completed_with_warnings`.

### Umbral para avanzar

Avanzar a Market Intelligence solo si:

- Todos los obligatorios tienen valor o `unknown` aceptado.
- Ningún bloqueo total está abierto.
- La ubicación investigable está confirmada y permanece privada cuando corresponda.

Avanzar a Content Strategy solo si:

- Los hechos publicables están en `confirmed`.
- Los `needs_verification` están excluidos o aprobados como no publicables.
- Las contradicciones materiales están resueltas.

## 7. Fair Housing y privacidad

### Fair Housing

- Definir audiencias por intención, necesidad, etapa, precio, tipo de propiedad y geografía permitida.
- No dirigir, excluir ni describir al público por raza, color, religión, sexo, orientación sexual, identidad de género, discapacidad, situación familiar u origen nacional; añadir cualquier clase protegida estatal o local aplicable.
- No inferir clases protegidas a partir de nombre, idioma, fotografía, ZIP, escuela, conducta o datos digitales.
- Evitar frases como “ideal para familias”, “perfecta para jóvenes”, “comunidad cristiana”, “vecindario seguro” o equivalentes.
- Permitir hechos neutrales verificables sobre características físicas y amenidades.
- Tratar “55+” únicamente como condición oficial verificada de la comunidad, sin ampliar inferencias sobre residentes.
- Marcar contenido de Housing para revisión de requisitos publicitarios aplicables.

### Privacidad

- Aplicar `public_visibility` por campo: `public`, `internal` o `restricted`.
- Mantener dirección privada, instrucciones de acceso, códigos, datos del seller y documentos sensibles fuera de exports.
- No incluir metadatos EXIF ni nombres originales de archivos si revelan información privada.
- No guardar información de prospectos en el expediente de la propiedad.
- No publicar testimonios, imágenes de personas o información de ocupación sin autorización.
- Escapar datos en HTML y sanitizar nombres y rutas antes de renderizar.

## 8. Contrato `property-brief.json`

Contrato normalizado producido por Intake. Los campos desconocidos usan `null`; no usar cadenas vacías. Cada hecho relevante incluye valor, clasificación, visibilidad y procedencia.

```json
{
  "schema_version": "1.0",
  "project_id": "string",
  "created_at": "ISO-8601",
  "property": {
    "internal_name": "string",
    "private_address": {
      "value": "string",
      "classification": "private",
      "public_visibility": "restricted",
      "source": "user"
    },
    "public_location": {
      "value": "string|null",
      "classification": "confirmed|needs_verification",
      "public_visibility": "public|internal",
      "source": "user|mls|document"
    },
    "operation": "sale|rent",
    "property_type": "string",
    "status": "string",
    "price": {
      "amount": 0,
      "currency": "USD",
      "effective_date": "YYYY-MM-DD",
      "classification": "confirmed|needs_verification",
      "source": "string"
    },
    "facts": [
      {
        "key": "bedrooms",
        "value": 0,
        "unit": null,
        "classification": "confirmed|needs_verification|agent_assumption|private|prohibited",
        "public_visibility": "public|internal|restricted",
        "source": "string|null",
        "as_of": "YYYY-MM-DD|null",
        "notes": "string|null"
      }
    ],
    "features_to_highlight": ["string"],
    "assets": [
      {
        "asset_id": "string",
        "type": "photo|video|floor_plan|logo|music|voice",
        "path_or_url": "string",
        "usage_authorized": true,
        "primary": false,
        "public_visibility": "public|internal|restricted"
      }
    ]
  },
  "campaign": {
    "objective": "string",
    "audience_need": "string",
    "funnel_stage": "discovery|consideration|action",
    "languages": ["es", "en"],
    "channels": ["pdf", "instagram_post", "carousel", "story", "email", "video"],
    "cta": {"label": "string", "destination": "string"},
    "target_publish_at": "ISO-8601|null",
    "primary_kpi": "string"
  },
  "professional": {
    "agent_name": "string",
    "brokerage": "string",
    "phone": "string|null",
    "email": "string|null",
    "disclosures": ["string"]
  },
  "authorizations": {
    "marketing": true,
    "asset_rights": true,
    "approval_required": true,
    "confirmed_at": "ISO-8601"
  },
  "open_questions": ["string"],
  "blocking_issues": ["string"],
  "intake_status": "incomplete|ready|blocked"
}
```

## 9. Contrato `verified-property.json`

Producido por Verificación. Debe conservar referencias a los hechos originales y separar claims autorizados de datos rechazados.

```json
{
  "schema_version": "1.0",
  "project_id": "string",
  "verified_at": "ISO-8601",
  "verification_mode": "connected_sources|supplied_data_only",
  "public_property": {
    "location": "string|null",
    "operation": "sale|rent",
    "property_type": "string",
    "status": "string",
    "price": {"amount": 0, "currency": "USD", "as_of": "YYYY-MM-DD"},
    "facts": [
      {
        "fact_id": "string",
        "key": "string",
        "value": "string|number|boolean|null",
        "unit": "string|null",
        "classification": "confirmed",
        "source_ids": ["string"],
        "as_of": "YYYY-MM-DD|null",
        "review_after": "YYYY-MM-DD|null"
      }
    ],
    "approved_features": ["string"],
    "approved_assets": ["asset_id"]
  },
  "private_context": {
    "address_retained_for_research": true,
    "restricted_fact_ids": ["string"]
  },
  "claims": {
    "approved": [
      {
        "claim_id": "string",
        "claim": "string",
        "source_ids": ["string"],
        "allowed_public_wording": "string",
        "confidence": "high|medium|low",
        "expires_at": "ISO-8601|null"
      }
    ],
    "conditional": [
      {
        "claim_id": "string",
        "claim": "string",
        "required_evidence": "string",
        "status": "needs_verification"
      }
    ],
    "prohibited": [
      {
        "claim": "string",
        "reason": "fair_housing|privacy|unsupported|security|contractual"
      }
    ]
  },
  "sources": [
    {
      "source_id": "string",
      "type": "user|mls|official|builder|document|portal",
      "title": "string",
      "url_or_reference": "string|null",
      "accessed_at": "ISO-8601",
      "reliability": "high|medium|low"
    }
  ],
  "contradictions": [
    {
      "field": "string",
      "values": ["string"],
      "source_ids": ["string"],
      "resolution": "string|null",
      "status": "open|resolved"
    }
  ],
  "compliance": {
    "fair_housing": "passed|warning|blocked",
    "privacy": "passed|warning|blocked",
    "disclosures": "passed|warning|blocked",
    "notes": ["string"]
  },
  "blocking_issues": ["string"],
  "verification_status": "verified|verified_with_warnings|blocked"
}
```

## 10. Entrega entre fases

Antes de entregar a Market Intelligence:

1. Validar ambos JSON contra sus contratos.
2. Confirmar que `intake_status` sea `ready`.
3. Confirmar que `verification_status` sea `verified` o `verified_with_warnings`.
4. Excluir del contexto público todo campo `private`, `restricted` o `prohibited`.
5. Transferir solo facts `confirmed` y claims `approved`.
6. Transferir `conditional` como preguntas pendientes, nunca como hechos.
7. Mantener un registro de quién aprobó, qué aprobó y cuándo.
