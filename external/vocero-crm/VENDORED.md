# Vocero CRM (vendorizado)

Copia de referencia del código fuente de [`kevinrivm/vocero-crm`](https://github.com/kevinrivm/vocero-crm),
un CRM de WhatsApp self-hosted (Next.js + Postgres) con bandeja en tiempo
real, pipeline, plantillas y un agente de IA in-process con "Laboratorio" de
evaluación. Es el companion obligatorio de `../nea-agent`: expone el "bot
gateway" (`/api/bot/*`) hacia el que Nea reenvía y envía todos los mensajes.

- **Origen:** https://github.com/kevinrivm/vocero-crm
- **Commit:** `fcf0a15ec4a9d8b6147f7a1f536781e576b0648a` (2026-08-05)
- **Historial de git:** no incluido (copia de archivos, sin `.git`).

Este no es una skill de Codex/Claude (no tiene `SKILL.md`); se incluye aquí
únicamente como referencia de código. Para desplegarlo, sigue
`INSTALL-IA.md` de esta misma carpeta o el runbook conjunto en
[`../RUNBOOK.md`](../RUNBOOK.md) (requiere VPS/Docker, dominio propio, app de
Meta WhatsApp Cloud API y, opcionalmente, una API key de OpenRouter).
