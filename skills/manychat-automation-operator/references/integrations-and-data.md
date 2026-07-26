# Integraciones y datos

## Modelo de datos recomendado

Campos reutilizables:

```text
lead_type
lead_source
lead_campaign
preferred_language
city_interest
state_interest
property_type
price_range
timeline
financing_status
preapproval_status
current_rent
homeownership_status
appointment_status
lead_score
crm_sync_status
crm_contact_id
consent_status
last_automation
last_conversion
```

Tags recomendados:

```text
SOURCE_Instagram
SOURCE_Facebook
SOURCE_WhatsApp
INTENT_Buyer
INTENT_Seller
INTENT_Realtor
STATUS_New
STATUS_Qualified
STATUS_Appointment
STATUS_Nurture
STATUS_Human-Handoff
```

Verificar campos y tags existentes antes de crear. No reutilizar un campo con significado distinto.

## Contrato de integración

Definir para cada CRM, hoja, formulario o API:

- sistema destino;
- método de conexión;
- evento que dispara;
- URL como placeholder;
- autenticación como placeholder;
- mapeo origen-destino;
- campo de deduplicación;
- respuesta exitosa;
- respuesta fallida;
- retry o fallback;
- responsable de la alerta.

## External Request

Definir método, headers, payload y mapping. Usar placeholders como `{{WEBHOOK_URL}}` y `{{API_SECRET}}`. No mostrar ni guardar secretos.

Ejemplo conceptual:

```json
{
  "method": "POST",
  "url": "{{WEBHOOK_URL}}",
  "headers": {"Content-Type": "application/json"},
  "body": {
    "first_name": "{{first_name}}",
    "email": "{{email}}",
    "phone": "{{phone}}",
    "city": "{{city_interest}}",
    "source": "ManyChat"
  }
}
```

## Formularios y landing pages

Preferir parámetros documentados, webhooks o APIs sobre simular que un humano llena formularios externos. Si se usa un formulario:

- verificar nombres reales de campos;
- confirmar si acepta prefill;
- probar envío;
- evitar duplicados;
- conservar una ruta de error.

## CRM

No declarar sincronización exitosa hasta verificar el registro en el destino. Si el conector externo requiere una herramienta distinta, realizar primero una lectura inocua de conexión antes de configurar una ejecución futura.
