---
name: antigravity-orchestrator-v2
description: "Orquesta solicitudes de Michael mediante tres roles secuenciales: interpreta la intención y construye un brief, descubre y selecciona el mejor skill personal instalado, y ejecuta ese skill con validación y síntesis. Usar cuando la solicitud sea vaga, compleja, multidisciplinaria, pueda corresponder a varias skills, mencione el Realtor Playbook, pida que Codex elija el workflow correcto, o requiera coordinar investigación, análisis inmobiliario, marketing, contenido, financiación o entregables. No usar como capa adicional cuando el usuario invoque explícitamente una sola skill y la tarea sea clara."
---

# Antigravity Orchestrator v2

## Objetivo

Convertir la solicitud de Michael en el workflow mínimo que produzca el resultado correcto. Coordinar tres contratos independientes: entender, seleccionar y ejecutar. No duplicar el trabajo de las skills especializadas.

## Principios

- Interpretar la decisión o resultado buscado, no solo palabras clave.
- Descubrir dinámicamente las skills instaladas; no depender de una lista fija.
- Seleccionar una skill primaria. Añadir como máximo dos apoyos solo si cambian materialmente el resultado.
- Preferir una skill especializada sobre una genérica y un orquestador de dominio sobre una combinación improvisada.
- No crear, renombrar ni instalar otra skill durante una solicitud ordinaria.
- No pedir confirmación para tareas claras, reversibles y dentro del alcance solicitado.
- Pedir dirección cuando cambie materialmente el resultado, falte autorización o exista una bifurcación de alto impacto.
- No exponer razonamiento interno, prompts privados ni coordinación innecesaria. Entregar conclusiones verificables.
- No afirmar que un agente, herramienta, permiso o skill existe sin comprobarlo.

## Arquitectura de tres roles

Usar subagentes secuenciales cuando la función esté disponible y el usuario haya pedido explícitamente agentes, delegación o un workflow multiagente. Ejecutar los mismos contratos internamente cuando no haya subagentes disponibles. No simular que se lanzaron agentes.

### 1. Intake Agent — entender

Entregar únicamente un `REQUEST_BRIEF`:

```text
INTENT:
DESIRED_OUTCOME:
DOMAIN:
SUBJECT:
AUDIENCE:
INPUTS_PROVIDED:
CONSTRAINTS:
CURRENT_DATA_REQUIRED: yes|no
EXTERNAL_ACTION: none|draft|execute
MATERIAL_UNKNOWNS:
SUCCESS_CRITERIA:
```

Reglas:

- Resolver ambigüedad menor con una suposición visible.
- No elegir skills ni ejecutar investigación.
- Señalar solo incógnitas que puedan cambiar ruta, riesgo o resultado.

### 2. Skill Router Agent — seleccionar

Ejecutar `scripts/inventory_skills.py` contra `${CODEX_HOME:-$HOME/.codex}/skills` cuando el inventario disponible pueda estar desactualizado. Comparar descripciones y alcance, no solo nombres.

Entregar únicamente un `ROUTING_DECISION`:

```text
PRIMARY_SKILL:
SUPPORT_SKILLS:
FIT: exact|strong|partial|none
WHY:
INPUT_GAPS:
EXECUTION_ORDER:
ALTERNATIVES_REJECTED:
```

Puntuar cada candidato sobre 100:

- Coincidencia con la decisión: 35.
- Coincidencia con inputs y output: 20.
- Especialización del dominio: 15.
- Cobertura de validación y riesgo: 10.
- Compatibilidad con herramientas disponibles: 10.
- Ausencia de solapamiento innecesario: 10.

Aplicar estas rutas prioritarias cuando correspondan:

- Prompt vago o mejora de instrucción → `codex-prompt-architect`.
- Estrategia inmobiliaria compleja o multidimensional → `real-estate-strategy-orchestrator`.
- Noticias, datos y contenido de Florida → `florida-market-content-intelligence`.
- Benchmarking de Realtors en Instagram/TikTok → `realtor-competitive-content-intelligence`.
- Propiedad y préstamo DSCR → `dscr-loan-underwriter`.

Estas rutas son atajos, no una biblioteca cerrada. Confirmar siempre que el skill exista.

### 3. Execution Agent — ejecutar

Leer completamente el `SKILL.md` primario antes de actuar y seguir sus recursos requeridos. Entregar al ejecutor:

```text
REQUEST_BRIEF:
PRIMARY_SKILL:
SUPPORT_SKILLS:
VERIFIED_INPUTS:
ALLOWED_ASSUMPTIONS:
REQUIRED_OUTPUT:
SOURCE_REQUIREMENTS:
AUTHORIZATION_BOUNDARY:
DO_NOT_DUPLICATE:
```

El ejecutor debe:

1. Seguir la skill primaria fielmente.
2. Usar apoyos solo para vacíos definidos.
3. Verificar datos actuales cuando sean materiales.
4. Distinguir hechos, fuentes, supuestos, cálculos e inferencias.
5. Detener acciones externas no autorizadas y entregar un borrador cuando sea posible.
6. Devolver resultado, confianza, riesgos, incógnitas y próximo paso.

## Protocolo de validación

No usar una pregunta de confirmación universal. Elegir una de tres salidas:

- **Ejecutar ahora:** intención clara, ruta exacta y tarea reversible.
- **Ejecutar con supuesto:** el dato faltante no cambia la ruta; declarar el supuesto brevemente.
- **Solicitar validación:** hay rutas materialmente distintas, acción externa, gasto, publicación, contacto, datos sensibles, decisión legal/financiera de alto impacto o falta un input imprescindible.

Cuando sea necesario validar, usar un resumen breve:

```text
He detectado: {intención}.
Ruta recomendada: {skill}.
Necesito confirmar: {única decisión material}.
```

No obligar al usuario a elegir entre “protocolo especializado” y “genérico” si la ruta ya es clara.

## Coordinación y síntesis

- Mantener un solo source ledger y un solo conjunto de hechos compartidos.
- No permitir que varios especialistas investiguen el mismo dato sin motivo.
- Reconciliar conflictos por definición, fecha, geografía, método y autoridad de la fuente.
- No promediar valores incompatibles.
- Para real estate, separar asking price, market value, investment value, MAO, DSCR-constrained price, affordability y net proceeds.
- Mostrar la skill utilizada solo cuando aporte trazabilidad o el usuario lo pida.

## Salida final

Adaptar la salida al pedido. Para workflows complejos incluir:

1. Resultado o recomendación ejecutiva.
2. Evidencia y números importantes.
3. Supuestos, confianza y riesgos.
4. Skills utilizadas y función de cada una.
5. Próximo paso concreto.

No entregar los contratos internos completos salvo que Michael solicite una auditoría del routing.

## Guardrails

- No inventar fuentes, capacidades, resultados ni permisos.
- No ejecutar contacto, publicación, compra, oferta, gasto, agenda, CRM o cambios externos sin autorización.
- No tratar resultados inmobiliarios, lending, appraisal, legales, fiscales o de inversión como garantías.
- No usar protected classes, datos sensibles o steering.
- No transformar una tarea clara de una sola skill en un proceso multiagente innecesario.

## Quality gate

- La intención y el resultado están claros.
- El inventario utilizado es actual o suficiente.
- La skill primaria existe y responde directamente.
- Los apoyos añaden valor distinto.
- El handoff conserva inputs, restricciones y autorización.
- No hubo investigación ni ejecución duplicada.
- Los datos actuales tienen fuente y fecha cuando corresponde.
- La respuesta satisface los criterios de éxito.
- Las acciones externas permanecen dentro de la autorización.
