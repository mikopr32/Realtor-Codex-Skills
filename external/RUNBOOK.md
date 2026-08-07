# Runbook: poner a correr Nea + Vocero CRM

Guía de arranque para cuando decidas activar el stack vendorizado en esta
carpeta. Son **dos servicios que dependen uno del otro** — Nea (el agente de
WhatsApp) nunca habla directo con Meta ni existe solo: todo pasa por el "bot
gateway" de Vocero CRM.

```
Meta WhatsApp Cloud API
        │ webhook
        ▼
  external/nea-agent   (FastAPI, Postgres propio, OpenAI)
        │ relay + envío SIEMPRE vía CRM
        ▼
  external/vocero-crm  (Next.js, Postgres propio, bandeja/pipeline/agente)
```

No se puede correr Nea sin una instancia de Vocero CRM con el bot gateway
habilitado. Si solo quieres el CRM (sin el microservicio Nea aparte), Vocero
trae su propio agente in-process — en ese caso ignora `external/nea-agent` y
sigue solo la sección de Vocero.

## 0. Qué necesitas conseguir ANTES de tocar código

Ninguno de estos lo puedo generar yo dentro de este repo — son cuentas y
recursos reales que tienes que crear tú (o pedirle a quien administre la
infraestructura del negocio):

- [ ] **VPS con Docker** (o panel Coolify sobre ese VPS) — 2 GB RAM mínimo.
- [ ] **Dos dominios/subdominios** apuntando al VPS (registro A), uno para el
      CRM (ej. `crm.tunegocio.com`) y uno para Nea si lo separas del CRM (ej.
      `nea.tunegocio.com`). Si Nea corre en el mismo host que el CRM sin
      exponerse a internet, no necesita dominio propio, solo puerto interno.
- [ ] **App de Meta for Developers** con el producto WhatsApp Cloud API
      activado (developers.facebook.com), número de WhatsApp Business
      verificado.
- [ ] **API key de OpenAI** (platform.openai.com) — la usa Nea para conversar.
- [ ] **API key de OpenRouter** (openrouter.ai) — opcional, solo si además
      quieres el agente/Laboratorio in-process de Vocero.
- [ ] Dos bases de datos **Postgres separadas** (Nea y Vocero NO comparten
      base de datos). `docker compose` de cada repo ya trae su propio
      contenedor Postgres si no tienes uno gestionado.

## 1. Levanta Vocero CRM primero

Vocero es la base — Nea no tiene nada que hacer sin él.

```bash
cd external/vocero-crm
cp .env.example .env
```

Genera los secretos (documentado también en `INSTALL-IA.md` de esa carpeta):

```bash
openssl rand -base64 32   # → BETTER_AUTH_SECRET
openssl rand -base64 32   # → ENCRYPTION_KEY (debe quedar en exactamente 44 caracteres base64)
openssl rand -hex 32      # → META_WEBHOOK_VERIFY_TOKEN
openssl rand -hex 24      # → POSTGRES_PASSWORD
openssl rand -base64 32   # → BOT_API_KEY (solo si vas a correr Nea aparte; descomenta la línea en .env)
```

Rellena en `.env`: `APP_BASE_URL`, `DOMAIN`, los cuatro secretos de arriba,
`OPENROUTER_API_TOKEN`/`OPENROUTER_MODEL` (opcional), y **descomenta
`BOT_API_KEY`** con el valor generado — es la credencial que Nea usará para
autenticarse contra `/api/bot/*`.

Dos rutas de despliegue (detalladas en `external/vocero-crm/INSTALL-IA.md`):

- **Ruta A — Coolify**: crea el Postgres 16 como servicio, la app apuntando a
  `https://github.com/kevinrivm/vocero-crm` (build pack `dockerfile`, puerto
  `3000`), variables de la tabla como runtime env, sin pre-deploy command
  (las migraciones corren solas). Verifica `https://<dominio>/api/health`.
- **Ruta B — docker compose (VPS con solo Docker)**:
  ```bash
  docker compose up -d --build
  docker compose ps                 # espera los 3 servicios "healthy"
  curl https://<dominio>/api/health # {"ok":true}
  ```

Después: entra a `https://<dominio>`, **regístrate** (el primer registro crea
la organización y cierra el registro público), y ve a
**Configuración → WhatsApp** para conectar el número — ahí Vocero te da la URL
exacta del webhook para pegar en el panel de Meta. Esto es manual, no se
automatiza desde este repo.

## 2. Levanta Nea (solo si quieres el agente como microservicio aparte)

Sáltate este paso si te vas a quedar con el agente in-process de Vocero.

```bash
cd external/nea-agent
cp .env.example .env
```

Rellena `.env`:

- `VERIFY_TOKEN`: uno que inventes tú, igual al que pongas en el webhook de
  Meta apuntando a Nea (si Nea recibe el webhook directo en vez de Vocero).
- `CRM_BASE_URL` / `CRM_WEBHOOK_URL`: la URL pública de tu instancia de
  Vocero del paso 1.
- `CRM_BOT_API_KEY`: el mismo valor que pusiste en `BOT_API_KEY` del `.env`
  de Vocero — así se autentica contra `/api/bot/*`.
- `OPENAI_API_KEY`, `OPENAI_MODEL` (usa uno rápido, no "razonador").
- `DATABASE_URL`: Postgres **propio** de Nea (no el de Vocero).
- `ALLOWED_WA_IDS`: dejar poblado durante pruebas (solo responde a esos
  números); vaciar es una decisión explícita para salir a producción.

Local:

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --port 8000   # migraciones corren al arranque
curl localhost:8000/health
```

Docker / Coolify: usa el `Dockerfile` de esa carpeta (build pack `dockerfile`,
puerto `8000`, healthcheck ya incluido).

## 3. Verificación antes de tráfico real

- `cd external/nea-agent && pip install -r requirements-dev.txt && pytest -q`
  — 76 tests offline, deben pasar en verde.
- `cd external/vocero-crm && pnpm install && pnpm test` (revisa `package.json`
  de esa carpeta para el script exacto de test/build).
- Con `ALLOWED_WA_IDS` poblado en Nea, manda un WhatsApp real desde un número
  de prueba y confirma que: el webhook de Meta llega, Vocero lo registra en la
  bandeja, y la respuesta del agente sale por WhatsApp.
- Vacía `ALLOWED_WA_IDS` solo cuando decidas conscientemente salir a
  producción.

## Notas

- Cada carpeta (`nea-agent/`, `vocero-crm/`) trae su propio `README.md`,
  `CLAUDE.md` y `VENDORED.md`/`.env.example` con el detalle fino de cada
  variable — este runbook solo ordena el proceso conjunto.
- Ninguno de los dos `.env.example` trae secretos reales; todo lo marcado
  `REEMPLAZA_...` hay que generarlo o conseguirlo tú.
- Si actualizas el código fuente de cualquiera de los dos repos originales,
  vuelve a vendorizar (recopiar archivos sin `.git`) y anota el nuevo commit
  en su `VENDORED.md`.
