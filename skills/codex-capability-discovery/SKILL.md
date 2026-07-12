---
name: codex-capability-discovery
description: Ayuda a descubrir, comparar y seleccionar capacidades para Codex, incluyendo skills instaladas, skills curadas, plugins, connectors, MCP servers, templates y alternativas nativas; detecta duplicados, evalúa compatibilidad y procedencia, presenta riesgos y delega la instalación al mecanismo oficial después de autorización. Usar cuando el usuario pida encontrar una extensión, pregunte si existe una capacidad instalable, quiera ampliar Codex, comparar alternativas o resolver una tarea bloqueada por capacidad ausente.
---

# Codex Capability Discovery

## Objetivo

Encontrar la capacidad mínima, compatible y razonablemente confiable que resuelva la necesidad. No instalar automáticamente: comprobar existencia, recomendar opciones y obtener autorización específica.

## Principios

- No buscar extensión si Codex puede resolver directamente.
- Distinguir skill, plugin, connector, MCP, app, template, automation y project config.
- Priorizar capacidades instaladas y fuentes oficiales.
- No ejecutar paquetes remotos, instalaciones globales, `-y`, `--force` o updates masivos sin autorización explícita.
- No afirmar que código externo es seguro.
- No solicitar secrets visibles.
- No inventar compatibility, maintenance, reputation o availability.
- Mostrar como máximo tres candidatos salvo solicitud amplia.

## Activación

Activar ante búsqueda explícita de skill/plugin/connector, deseo de extender Codex, comparación de herramientas, repo para instalar o bloqueo por capacidad ausente.

No activar para tareas normales que Codex o una skill instalada ya pueden resolver. Para crear una skill nueva usar `$skill-creator`.

## Delegación multiagente opcional

Usar un solo agente para una búsqueda simple. Para una necesidad amplia que abarque varias superficies, permitir investigadores paralelos con scopes no solapados:

- **Installed Inventory Agent:** capacidad nativa, skills, templates y project config locales.
- **Plugin/Connector Agent:** plugins recomendados, apps, connectors y MCP disponibles.
- **External Candidate Agent:** catálogo curado y repositorios autorizados.

Después del discovery, un único **Supply-Chain Reviewer** inspecciona candidatos reales y un **Decision Owner** deduplica, rankea y recomienda. No instalar durante investigación. Exigir source, owner, version/commit, permissions, dependencies, maintenance evidence, observed risk y overlap. Si no hay subagentes, ejecutar las superficies secuencialmente.

## Workflow

### 1. Definir capability brief

```text
OUTCOME:
DOMAIN:
TASKS:
INPUTS:
OUTPUTS:
SYSTEMS:
READ_OR_WRITE:
AUTHENTICATION:
SENSITIVE_DATA:
FREQUENCY:
ENVIRONMENT:
CONSTRAINTS:
```

Preguntar solo por diferencias materiales.

### 2. Elegir superficie

- Native: tarea directa.
- Skill: workflow o conocimiento reusable.
- Plugin: paquete de skills/tools/apps/hooks/MCP.
- Connector/App: servicio externo.
- MCP: API/sistema sin connector.
- Template: formato reusable.
- Automation: recurrencia.
- Project config: convenciones de repo.

No recomendar una skill cuando se necesita acceso a datos externos.

### 3. Inventariar lo existente

Revisar capacidad nativa, skills, plugins, connectors/apps, MCP tools, templates y workspace config. Comparar descriptions/triggers, no solo nombres.

Ejecutar `scripts/inventory_skills.py --skills-root ...` para inventario reproducible y pares potencialmente solapados. Clasificar Exact, Strong partial, Composable, Duplicate o Not suitable.

Si existe solución suficiente, recomendar usarla y detener búsqueda externa.

### 4. Buscar fuentes

Orden:

1. Catálogo curado mediante `$skill-installer`.
2. Plugins recomendados expuestos en sesión.
3. Marketplaces oficiales configurados.
4. Repos oficiales de la tecnología.
5. GitHub proporcionado por usuario.
6. skills.sh/registries externos solo si se solicita o lo anterior falla.

No asumir que `npx skills` existe. Si se considera una CLI externa, verificar documentación, explicar que no es nativa, mostrar cambios y pedir autorización. Evitar global install por defecto.

### 5. Evaluar candidatos

Registrar name, type, source, owner, use cases, compatibility, method, scope, tools, network/filesystem, auth, secrets, dependencies, scripts/hooks, external services, license, update date, version/commit, maintenance, overlap, limitations y observed risk.

Leer `references/supply-chain-review.md` para fuentes externas.

### 6. Revisar supply chain

Inspeccionar repo owner, skill directory, SKILL.md, manifest, scripts, hooks, MCP/app config, dependencies, install commands, network, secrets, binaries, generated/minified code, post-install behavior, destructive commands y license.

Usar Lower/Moderate/Higher observed risk. Nunca declarar “seguro”.

### 7. Rankear

Evaluar fit, compatibility, provenance, maintenance, permissions, complexity, duplication, cost, lock-in y removability. Clasificar Recommended, Good alternative, Conditional o Not recommended.

Mostrar alternativa sin instalación.

## Recomendación

# Capability Recommendation: {NECESIDAD}

Incluir diagnosis, capability type, existing match, need to install y confidence.

Tabla de hasta tres opciones con type, fit, source, permissions, risk y status.

Para la recomendada explicar value, overlap, dependencies, permissions, limitations y no-install alternative.

Si instalación procede, mostrar source exacta, version/commit, destination, scope, created files, official installer, validation y known removal method.

Solicitar autorización específica:

> ¿Quieres que instale `{NOMBRE}` desde `{FUENTE}` en `{DESTINO}` con estos permisos?

No pedir confirmación si solo solicitó opciones.

## Instalación

- Skill curada/GitHub: delegar a `$skill-installer`.
- Plugin recomendado: usar mecanismo de plugin disponible.
- Connector: flujo oficial del producto.
- Skill nueva: proponer `$skill-creator` cuando sea recurrente.

No instalar desde descripción pegada sin convertir y validar primero.

## Post-install

Confirmar directory, SKILL.md, metadata y dependencies; validar estructura; ejecutar prueba pequeña segura; informar disponibilidad. No declarar éxito si falla.

## Update y removal

Antes de update, comparar versión/cambios/permisos, preservar local edits y solicitar autorización. No update all por una sola necesidad.

Antes de eliminar, revisar files, dependents, config, credentials/data e impacto; solicitar autorización explícita.

## Sin candidato

Indicar fuentes revisadas, native alternative y si conviene crear skill. No convertir una tarea única en skill innecesariamente.

## Quality gate

- Need definida y surface correcta.
- Installed inventory revisado.
- Duplicados detectados.
- Source verificable y compatibility clara.
- Permissions/secrets visibles.
- Scripts/hooks inspeccionados cuando corresponde.
- Popularidad no se usa como seguridad.
- Existe alternativa sin instalación.
- No hubo instalación sin autorización.
- Instalación declarada exitosa solo tras validación.
