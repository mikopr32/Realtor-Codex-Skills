# Modelo operativo de ManyChat

## Verificación de capacidades

ManyChat cambia por canal, plan y políticas de plataformas. Antes de construir, verificar en la interfaz o documentación oficial actual:

- disponibilidad del trigger;
- ventana de mensajería;
- formatos permitidos;
- límites de botones, quick replies y mensajes;
- requisitos de templates;
- disponibilidad de API, External Request, AI o integraciones;
- posibilidad de preview y pruebas.

No extrapolar una función de Instagram a WhatsApp, Messenger, TikTok, SMS o email.

## Catálogo funcional

### Triggers

- keyword o mensaje entrante;
- comentario en post o Reel;
- respuesta o mención en Story;
- conversation starter;
- default reply;
- anuncio o enlace de entrada;
- evento externo, rule, tag, campo o fecha;
- template o trigger propio del canal.

### Bloques

- Message: contenido y CTA.
- Data Collection: capturar y validar respuestas.
- Action: campos, tags, notificaciones y operaciones.
- Condition: ramificar por datos o estado.
- Randomizer: pruebas A/B o distribución.
- Smart Delay: seguimiento dentro de límites aplicables.
- Start Automation: modularizar.
- External Request: enviar o recuperar datos.
- Dynamic/AI: contenido dinámico cuando esté disponible.
- Human Handoff: transferir y notificar.

## Patrones obligatorios

### Captura de datos

Incluir prompt, validación, reintento, fallback por ausencia, confirmación cuando sea necesario y guardado en el campo correcto. No volver a preguntar un dato existente salvo que deba confirmarse.

### Condiciones

Nombrar cada rama, definir criterio exacto y cerrar todas las rutas. Incluir una ruta por defecto.

### Enlaces externos

Usar HTTPS. Definir si el botón abre una web, inicia una acción o cuenta como opt-in. No asumir que abrir una web habilita seguimiento posterior.

### Handoff humano

Aplicar tag de estado, notificar al responsable, resumir respuestas capturadas y detener mensajes automatizados incompatibles.

### Reentrada

Definir si el contacto reinicia, retoma, salta preguntas ya completadas o se dirige a un menú.

## Diseño conversacional

Mantener un objetivo por flujo. Preguntar de una en una, usar lenguaje natural y explicar por qué se solicita información sensible. Priorizar Quick Replies para elecciones cerradas y Data Collection para datos abiertos.
