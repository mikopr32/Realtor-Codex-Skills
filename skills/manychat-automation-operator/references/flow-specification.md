# Especificación intermedia del flujo

## Propósito

Representar el flujo esperado antes de operar ManyChat. Usar JSON UTF-8. Mantener identificadores estables aunque cambie el copy.

## Estructura mínima

```json
{
  "spec_version": "1.0",
  "automation": {
    "name": "DRAFT - Instagram - Keyword CASA - v1",
    "mode": "BUILD",
    "channel": "instagram",
    "objective": "Calificar compradores",
    "primary_conversion": "appointment",
    "language": "es",
    "status": "draft"
  },
  "trigger": {
    "type": "post_comment",
    "keywords": ["CASA"],
    "scope": "specific_posts",
    "configuration": {}
  },
  "fields": [
    {"name": "city_interest", "type": "text", "required": true}
  ],
  "tags": [
    {"name": "INTENT_Buyer", "purpose": "Clasificación"}
  ],
  "nodes": [
    {
      "id": "N01",
      "type": "message",
      "name": "Bienvenida",
      "content": {"text": "¡Gracias por escribir CASA!"},
      "save_to": null,
      "next": ["N02"]
    }
  ],
  "integrations": [],
  "tests": [],
  "kpis": ["completion_rate", "appointment_rate"]
}
```

## Tipos de nodo normalizados

- `message`
- `data_collection`
- `action`
- `condition`
- `randomizer`
- `smart_delay`
- `start_automation`
- `external_request`
- `dynamic_content`
- `ai_step`
- `human_handoff`
- `end`

Cada nodo debe tener `id`, `type`, `name` y `next`. Usar `next: []` solo para finales deliberados. Las condiciones deben declarar ramas con nombre y destino. Los randomizers deben sumar 100.

## Campos

Usar campos del sistema para información estándar cuando el canal lo permita. Usar Custom User Fields para datos comerciales. Definir siempre tipo y propósito. Usar campos para valores mutables y tags para clasificación o eventos.

Tipos recomendados: `text`, `number`, `boolean`, `date`, `datetime`.

## Integraciones

Para cada integración declarar:

```json
{
  "id": "I01",
  "provider": "lofty",
  "method": "webhook",
  "trigger_node": "N10",
  "field_mapping": {
    "first_name": "system.first_name",
    "email": "system.email",
    "city": "custom.city_interest"
  },
  "success_path": "N11",
  "failure_path": "N12",
  "dedupe_key": "email",
  "secrets": ["WEBHOOK_URL"]
}
```

No incluir valores secretos.

## Convenciones

- Automatización: `DRAFT - <Canal> - <Campaña> - v<n>`.
- Campos: `snake_case` semántico.
- Tags: `<CATEGORIA>_<Valor>`, por ejemplo `INTENT_Buyer`.
- Nodos: `N01`, `N02`, en orden de lectura.
- Integraciones: `I01`, `I02`.
- Tests: `T01`, `T02`.

## Criterios de aprobación

Confirmar objetivo, trigger, conversión, datos requeridos, destino del lead y comportamiento ante fallos. Señalar cualquier supuesto que afecte canal, cumplimiento o integración.
