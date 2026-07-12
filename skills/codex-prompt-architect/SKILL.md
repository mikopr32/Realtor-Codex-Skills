---
name: codex-prompt-architect
description: Analiza, optimiza y transforma solicitudes vagas en prompts profesionales, especificaciones y workflows ejecutables para ChatGPT Codex. Usar cuando Michael pida mejorar un prompt, crear un master prompt, convertir una idea en instrucciones profesionales, auditar un prompt existente, definir criterios de aceptación o preparar una tarea compleja para que Codex la ejecute.
---

# Codex Prompt Architect

Convertir ideas, instrucciones vagas y prompts incompletos en instrucciones claras, eficientes y ejecutables para ChatGPT Codex. Preservar la intención original y añadir solo el contexto, alcance, herramientas, validaciones y criterios necesarios.

No interrumpir tareas normales ni obligar a optimizar cada solicitud.

## Principio central

Preservar la intención, reducir ambigüedad y añadir únicamente controles que mejoren materialmente el resultado. No confundir longitud con calidad.

## Activación

Activar cuando Michael invoque `$codex-prompt-architect` o pida mejorar, optimizar, auditar o crear un prompt, master prompt, workflow, blueprint, especificación o criterios de aceptación.

No activarse automáticamente para preguntas sencillas, conversación normal, ediciones claras o tareas ejecutables con seguridad sin optimización.

## Modos

### Optimize

Mejorar y entregar el prompt sin ejecutarlo. Usar cuando pida “mejora”, “optimiza”, “master prompt” o “nivel arquitecto”.

### Optimize + Execute

Optimizar internamente y ejecutar en la misma tarea cuando pida “optimiza y ejecuta”, “mejóralo y hazlo” o equivalente. No pedir confirmación adicional salvo decisión material, acción externa, credenciales, gasto, eliminación, publicación u otra autorización necesaria.

### Audit

Evaluar sin reescribir automáticamente. Entregar puntuación, propósito, fortalezas, ambigüedades, riesgos, información faltante y mejoras. Añadir versión mejorada solo si se solicita.

### Blueprint

Transformar una idea compleja en especificación antes de implementar. Usar para aplicaciones, sistemas, automatizaciones, bases de datos, integraciones y refactors grandes. No implementar salvo autorización expresa o solicitud conjunta.

## Fase 1 — Diagnóstico

Identificar objetivo, entregable, audiencia, inputs, contexto, restricciones, formato, calidad, herramientas, riesgos, criterios de éxito, acciones externas y decisiones abiertas.

Clasificar cada elemento como presente, inferible con bajo riesgo, importante pero faltante, opcional o fuera de alcance. No preguntar por información opcional resoluble mediante una suposición segura.

## Fase 2 — Tipo de tarea

Clasificar en investigación, programación, diagnóstico, revisión, arquitectura, diseño, marketing, real estate, datos, documentos, spreadsheets, presentaciones, automatización, integración, operaciones, comunicación o skills. Adaptar estructura al tipo; no usar plantilla técnica innecesariamente.

## Fase 3 — Superficie de Codex

Recomendar la superficie mínima adecuada:

- **Prompt:** restricciones de una tarea.
- **Skill:** workflow reutilizable.
- **AGENTS.md:** convenciones permanentes del repositorio.
- **Configuración de proyecto:** ajustes técnicos persistentes.
- **Plugin:** paquete con skills, herramientas o integraciones.
- **Connector/MCP:** datos o acciones externas.
- **Automation:** trabajo recurrente o programado.
- **Hook:** control mecánico de acciones.

No convertir automáticamente una instrucción en plugin, integración o automatización. Si solo pide prompt, entregar prompt.

## Fase 4 — Contexto del workspace

Para proyectos, indicar a Codex que:

1. Inspeccione el contexto disponible.
2. Busque y siga `AGENTS.md` aplicable.
3. Revise estructura y archivos relevantes antes de editar.
4. Preserve cambios del usuario.
5. Evite archivos no relacionados.
6. Respete convenciones existentes.
7. Verifique proporcionalmente al riesgo.

No usar atajos de teclado ni asumir paneles o interfaces.

## Fase 5 — Herramientas y permisos

No declarar herramientas o permisos inexistentes. Incluir cuando corresponda:

> Utiliza únicamente las herramientas disponibles en la sesión. Antes de requerir acceso adicional, solicita el permiso mínimo necesario y explica por qué.

Distinguir herramienta disponible, recomendable, no confirmada, credencial, permiso y acción externa.

No añadir automáticamente terminal, navegador, Computer Use, conectores, APIs, Supabase, GitHub, despliegue o publicación. Añadirlos solo si el objetivo lo requiere.

## Fase 6 — Dependencias

No seleccionar tecnologías automáticamente. Si requiere persistencia, evaluar datos, usuarios, autenticación, volumen, privacidad, consultas, archivos, integraciones, hosting, costos y complejidad.

Para Realtor Playbook, inspeccionar arquitectura y persistencia existentes, evaluar Supabase frente a alternativas y solicitar decisión si cambia materialmente la arquitectura. No crear proyectos, tablas ni credenciales sin autorización.

## Fase 7 — Planificación

### Ejecución directa

Usar con alcance pequeño, solución evidente, pocas decisiones, cambio reversible y validación sencilla.

### Plan breve

Usar para varios pasos dependientes, múltiples componentes, investigación más implementación o decisiones menores.

### Blueprint

Usar cuando arquitectura no está definida, hay alternativas importantes, datos sensibles, integraciones, alto costo de error o necesidad de escala.

No planificar como ceremonia; hacerlo cuando reduzca riesgo o retrabajo.

## Fase 8 — Construcción

Usar solo las secciones necesarias:

```text
OBJETIVO
Resultado concreto.

CONTEXTO
Entorno, audiencia y antecedentes relevantes.

ALCANCE
Qué incluir y excluir.

INPUTS
Datos, archivos o enlaces disponibles.

RESULTADO ESPERADO
Entregable final.

FLUJO DE TRABAJO
Fases necesarias.

HERRAMIENTAS
Herramientas necesarias condicionadas a disponibilidad.

RESTRICCIONES
Límites técnicos, comerciales, legales o de formato.

CRITERIOS DE ACEPTACIÓN
Cómo comprobar la finalización.

VALIDACIÓN
Pruebas o revisiones.

MANEJO DE INCERTIDUMBRE
Cuándo investigar, inferir o preguntar.

FORMATO DE ENTREGA
Estructura, archivos y resumen.
```

Omitir secciones que no aporten valor.

## Roles

Usar roles solo cuando aporten criterios relevantes. Preferir un rol específico con experiencia pertinente; evitar títulos ornamentales. Un rol no sustituye requisitos.

## Fase 9 — Ambigüedad

Inferir cuando el riesgo sea bajo, la decisión reversible, exista una convención clara y no cambie materialmente el resultado. Declarar la suposición cuando importe.

Preguntar cuando las alternativas produzcan resultados distintos, introduzcan dependencias o costos, requieran credenciales, cambien audiencia, impliquen publicar/enviar/desplegar, afecten datos sensibles o amplíen el alcance. Hacer solo preguntas esenciales.

## Fase 10 — Autocorrección limitada

Al ejecutar y encontrar un error:

1. Reproducirlo.
2. Leer logs relevantes.
3. Identificar causa probable.
4. Aplicar cambio mínimo.
5. Repetir prueba afectada.
6. Revisar efectos secundarios.
7. Registrar evidencia.

No crear ciclos infinitos. Tras tres intentos fallidos sobre la misma causa, detener repetición, resumir lo probado, mostrar evidencia, identificar bloqueo y proponer siguiente acción. No ocultar errores eliminando pruebas o controles.

## Fase 11 — Seguridad y alcance

El prompt no debe conceder permisos ficticios, solicitar secretos visibles, crear servicios externos sin autorización, instalar dependencias innecesarias, eliminar datos, publicar, enviar mensajes, hacer commits/pushes, desplegar, crear cuentas ni ampliar silenciosamente el proyecto.

Hacer explícita toda acción material y respetar autorizaciones de Codex.

## Salida Optimize

```markdown
## 🧠 Codex Prompt Analysis

**Objetivo detectado:** {OBJETIVO}

**Mejoras aplicadas:**
- —

**Suposiciones:**
- —

## Prompt optimizado

\`\`\`text
{PROMPT}
\`\`\`

**Modo recomendado:** ejecución directa, plan breve o blueprint.
```

No preguntar si desea optimización cuando ya la pidió.

## Salida Audit

Entregar puntuación 1–10, propósito, fortalezas, debilidades, riesgos, faltantes, cambios prioritarios y potencial.

## Salida Optimize + Execute

Optimizar internamente y comenzar. Compartir solo decisiones y suposiciones útiles. No obligar a revisar primero el prompt salvo solicitud.

## Salida Blueprint

Entregar objetivo, usuarios, casos de uso, alcance, arquitectura, datos, integraciones, seguridad, etapas, pruebas, aceptación, riesgos y decisiones pendientes.

## Quality Gate

Comprobar:

- Intención preservada y resultado verificable.
- Alcance, inputs y outputs claros.
- Herramientas necesarias y condicionadas a disponibilidad.
- Sin permisos ficticios ni tecnologías injustificadas.
- Preguntas reducidas a las esenciales.
- Criterios comprobables y validación proporcional.
- Autocorrección limitada.
- Sin expansión silenciosa.
- Mayor claridad, no solo longitud.
- Formato adaptado a la tarea.
- Sin referencias a plataformas o modelos ajenos a Codex.

## Regla final

No interceptar todos los mensajes de Michael. Activarse por invocación o intención explícita. Permitir que Codex ejecute normalmente cualquier tarea clara fuera del propósito de esta skill.
