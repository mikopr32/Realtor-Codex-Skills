# Ejecución mediante navegador

## Dependencia

Leer y seguir íntegramente el skill `control-browser` antes de interactuar con ManyChat. Usar exclusivamente el navegador autorizado que ese skill disponga. No crear Playwright independiente, no usar scripts de shell para automatizar la interfaz y no intentar extraer credenciales.

## Inicio de sesión

- Reutilizar una sesión existente si está disponible.
- Si aparece login o MFA, ofrecer takeover manual en ChatGPT.
- No aceptar usuario, contraseña, token ni código MFA por chat.
- Después del login, confirmar visualmente cuenta, workspace, canal conectado y perfil.

## Estrategia de interacción

1. Abrir ManyChat y observar el estado actual.
2. Navegar por texto visible, roles accesibles y elementos inspeccionados.
3. Evitar coordenadas y selectores rígidos cuando exista una alternativa semántica.
4. Realizar una acción material por vez.
5. Verificar el resultado persistido antes de continuar.
6. Capturar evidencia visual o textual de hitos importantes.

No asumir que la interfaz coincide con documentación antigua. Si cambian etiquetas o estructura, inspeccionar y adaptar sin ampliar el alcance.

## Construcción

- Crear la automatización con nombre `DRAFT`.
- Configurar canal y trigger antes de construir ramas cuando ManyChat lo requiera.
- Crear o reutilizar campos y tags después de verificar tipo y propósito.
- Construir nodos en orden topológico.
- Conectar cada rama inmediatamente después de crearla.
- Guardar frecuentemente.
- Comparar nodos reales con la especificación.

## Edición

- Resolver el flujo exacto por nombre y contexto.
- Si está activo, duplicar primero cuando sea posible y editar la copia.
- No cambiar el original y la copia en la misma ejecución.
- Si existen nombres duplicados, detenerse y pedir identificación.

## Criterios de parada

Detenerse si:

- la cuenta o workspace no coincide;
- aparece una operación irreversible no prevista;
- el plan o canal no ofrece una función;
- la interfaz no permite verificar el guardado;
- hay más de un objetivo plausible;
- ManyChat muestra advertencias de cumplimiento;
- un test podría enviar mensajes a una audiencia real.

Informar el último estado confirmado y dejar lo creado en borrador.
