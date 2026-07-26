# Seguridad, aprobación y QA

## Matriz de autorización

### Permitido después de aprobar la construcción

- crear un flujo nuevo como borrador;
- crear nodos, campos y tags documentados;
- configurar enlaces e integraciones autorizadas;
- ejecutar preview;
- probar con contactos de prueba;
- guardar sin activar.

### Requiere autorización específica

- activar o publicar;
- cambiar un trigger activo;
- editar una automatización que recibe tráfico;
- iniciar broadcasts o secuencias;
- enviar a contactos reales;
- modificar integraciones globales;
- reemplazar, archivar o eliminar recursos;
- ejecutar acciones que generen costo.

## Checklist de estructura

- Trigger conectado.
- Todos los nodos accesibles desde una entrada.
- Todas las rutas terminan o continúan deliberadamente.
- Condiciones con ruta por defecto.
- Randomizers suman 100.
- Campos con tipo correcto.
- Tags sin duplicados.
- Fallback de datos inválidos.
- Ruta por ausencia de respuesta.
- Reentrada definida.
- Handoff humano funcional.

## Checklist de integración

- URL HTTPS.
- Mapeo completo.
- Secretos fuera del flujo documentado.
- Dedupe definido.
- Respuesta de éxito comprobada.
- Respuesta de error comprobada.
- Fallback y alerta.
- Registro visible en el destino.

## Casos mínimos

1. Contacto nuevo y happy path.
2. Contacto existente.
3. Cada rama.
4. Respuesta inválida.
5. Ausencia de respuesta.
6. Reentrada.
7. Handoff.
8. Link externo.
9. Integración exitosa.
10. Integración fallida.

## Severidad

- `critical`: riesgo de envío real, pérdida de datos, trigger incorrecto, integración rota o ruta principal bloqueada. No publicar.
- `major`: una rama secundaria, validación o fallback falla. Corregir antes de publicar salvo aceptación explícita.
- `minor`: copy, espaciado o detalle visual sin impacto funcional. Informar y decidir.

## Cierre

Comparar especificación y estado real. Reportar `PASS`, `FAIL` o `NOT TESTED` por caso. Nunca transformar un `NOT TESTED` en éxito inferido.
