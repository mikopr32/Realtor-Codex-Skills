---
name: manychat-automation-operator
description: Diseñar, construir, modificar, auditar, probar, optimizar y publicar automatizaciones en una cuenta autorizada de ManyChat. Usar para respuestas automáticas, palabras clave, comentarios a DM, Story replies, conversaciones guiadas, captura y calificación de leads, campos, tags, condiciones, secuencias, follow-up, handoff humano, landing pages, CRM, Google Sheets, formularios, webhooks, APIs y flujos de Instagram, Messenger, WhatsApp, TikTok, SMS o email. También usar cuando el usuario pida entrar a ManyChat y crear o editar directamente una automatización mediante navegador.
---

# ManyChat Automation Operator

## Objetivo

Convertir una intención comercial en una automatización verificable de ManyChat. Diseñar primero una especificación estructurada, obtener aprobación, construirla en una sesión autorizada, probarla y pedir autorización independiente antes de activarla o afectar tráfico real.

## Seleccionar modo

- `DESIGN`: producir arquitectura, copy, campos, tags, integraciones y pruebas sin entrar a ManyChat.
- `BUILD`: diseñar, obtener aprobación y construir como borrador mediante navegador.
- `AUDIT`: inspeccionar una automatización existente sin modificarla.
- `OPTIMIZE`: auditar, proponer cambios y modificar solo después de aprobar el alcance.

Interpretar “entra”, “construye”, “créala en mi cuenta” o “hazlo en ManyChat” como intención explícita de usar el sitio. Para interacción directa, leer y seguir íntegramente el skill `control-browser` antes de abrir ManyChat. No implementar control del navegador con scripts propios.

## Flujo obligatorio

### 1. Interpretar la solicitud

Extraer:

- objetivo y conversión principal;
- canal y audiencia;
- trigger;
- oferta y CTA;
- datos por capturar;
- lógica de calificación;
- destino del lead;
- seguimiento;
- idioma;
- KPI principal.

Preguntar solo por decisiones críticas que cambien materialmente el flujo. Para detalles no críticos, proponer supuestos explícitos. No prometer una función sin verificar que existe para el canal, plan y estado actual de ManyChat. Consultar documentación oficial actual cuando la capacidad sea incierta o pueda haber cambiado.

### 2. Crear la especificación

Leer [flow-specification.md](references/flow-specification.md). Crear una especificación antes de tocar una cuenta real. Validarla con:

```bash
python3 scripts/validate_flow_spec.py <flow-spec.json>
```

Entregar un resumen con número de nodos, campos, tags, integraciones, rutas y pruebas. Guardar el nombre como `DRAFT - <canal> - <campaña> - v<n>`.

### 3. Obtener aprobación de construcción

Antes de escribir en ManyChat, mostrar:

- qué se creará o modificará;
- automatización exacta;
- integraciones implicadas;
- supuestos;
- elementos que permanecerán en borrador.

Obtener aprobación. Una petición explícita que ya incluya el flujo completo autoriza preparar el diseño, pero no omitir el resumen previo a la mutación de la cuenta.

### 4. Preparar la ejecución

Leer:

- [manychat-model.md](references/manychat-model.md) para triggers, bloques y restricciones;
- [browser-execution.md](references/browser-execution.md) para operar la interfaz;
- [integrations-and-data.md](references/integrations-and-data.md) si hay CRM, formularios, APIs o webhooks;
- [safety-and-qa.md](references/safety-and-qa.md) antes de modificar, probar o publicar;
- [real-estate-patterns.md](references/real-estate-patterns.md) para compradores, vendedores, Realtors, eventos, propiedades u open houses.

Confirmar que la sesión corresponde a la cuenta y workspace correctos. Si aparece un login, permitir takeover manual; nunca pedir contraseñas, códigos MFA, API keys ni secretos en el chat.

### 5. Construir de forma verificable

Construir primero como borrador. Después de cada operación material:

1. inspeccionar el estado visible;
2. verificar nombre, tipo y valor;
3. compararlo con la especificación;
4. registrar el resultado;
5. continuar únicamente si coincide.

Reutilizar campos y tags existentes cuando su nombre, tipo y significado coincidan exactamente. No crear duplicados aproximados. No depender de posiciones visuales o selectores memorizados; inspeccionar la interfaz actual.

Para editar un flujo activo, resolver el objetivo exacto y duplicarlo como respaldo cuando la interfaz lo permita. No cambiar simultáneamente el original y la copia.

### 6. Probar

Generar casos con:

```bash
python3 scripts/generate_test_cases.py <flow-spec.json>
```

Probar al menos:

- ruta principal;
- cada ramificación;
- respuesta válida e inválida;
- ausencia de respuesta;
- contacto nuevo y existente;
- reentrada;
- handoff humano;
- enlace externo;
- integración exitosa y fallida.

No considerar suficiente el preview si no ejecuta acciones, validaciones o integraciones reales. Usar un contacto de prueba autorizado y evitar mensajes a audiencias reales.

### 7. Publicar con autorización independiente

Mantener el flujo en borrador salvo que el usuario autorice expresamente activarlo, publicarlo, cambiar el trigger activo o enviar mensajes reales. Presentar:

- pruebas aprobadas y fallidas;
- diferencias contra la especificación;
- impacto esperado;
- riesgos o limitaciones pendientes.

No publicar con pruebas críticas fallidas.

### 8. Reportar

Informar:

- nombre y canal;
- trigger;
- nodos, campos y tags creados o reutilizados;
- integraciones;
- estado final;
- pruebas;
- pendientes;
- KPI principal;
- siguiente optimización recomendada.

## Guardrails

- No eliminar automatizaciones, campos, tags, contactos o datos sin petición explícita y confirmación del objetivo exacto.
- No activar broadcasts, secuencias masivas o mensajes a contactos reales por inferencia.
- No sobrescribir un flujo activo si puede duplicarse y versionarse.
- No almacenar secretos en archivos del skill, especificaciones o respuestas.
- No eludir restricciones de canal, consentimiento, ventanas de mensajería o revisión de templates.
- Detenerse ante cuenta equivocada, ambigüedad del objetivo, función no disponible, error de integración, interfaz inesperada o imposibilidad de verificar el resultado.
- No declarar éxito por haber hecho clic; verificar el estado persistido.

## Métricas de calidad

Exigir:

- 100% de nodos conectados;
- 100% de campos mapeados;
- cero publicación sin autorización;
- cero eliminación no autorizada;
- 100% de rutas críticas probadas;
- coincidencia documentada entre especificación y flujo real.

Para rendimiento comercial, seleccionar métricas como activation rate, reply rate, completion rate, captura de email/teléfono, lead qualification rate, citas, handoffs, CTR, CRM sync success y abandono por nodo.
