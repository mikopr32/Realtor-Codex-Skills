# Realtor Codex Skills

Repositorio personal de skills de Codex creadas o agregadas por Michael Cruz para real estate, marketing, inteligencia de mercado, generación de leads, contenido, automatización y sistemas operativos.

## Estructura

Cada skill vive en su propia carpeta:

```text
skills/
└── nombre-de-la-skill/
    ├── SKILL.md
    ├── references/
    ├── templates/
    └── scripts/
```

Solo `SKILL.md` es obligatorio. Las demás carpetas aparecen cuando la skill necesita referencias, plantillas o validadores adicionales.

## Alcance

Este repositorio incluye únicamente las skills personales instaladas directamente en `~/.codex/skills`.

Se excluyen intencionalmente:

- Skills internas de `.system`.
- Skills distribuidas por plugins.
- Cachés y runtimes de Codex.
- Credenciales, tokens y configuración local.

## Uso

Para instalar una skill individual, copia su carpeta completa dentro de:

```text
~/.codex/skills/
```

Después reinicia o recarga Codex para que vuelva a descubrir las skills disponibles.

## Inventario

El inventario actual contiene 53 skills personales. La fuente de verdad de cada paquete es su archivo `SKILL.md`.

Consulta [SKILLS_CATALOG.md](SKILLS_CATALOG.md) para ver qué hace cada skill, qué resultado produce y si utiliza arquitectura multiagente.
