# Solución del ejercicio 2

Fechas, en el cuadro de reemplazo (Ctrl+H) con `.*` activado:

- Buscar: `(\d{2})/(\d{2})/(\d{4})`
- Reemplazar: `$3-$2-$1`

Condición: seleccionar `Hipoxia`, Ctrl+Shift+L (por defecto no distingue mayúsculas, así
que toma también `hipoxia` y `HIPOXIA`), escribir `hipoxia`. El espacio final de una fila se
ve con «Render Whitespace» activado o buscando `_6h ,` con la coma.

Cuándo conviene: el editor gana para una tabla que se limpia una vez. El script gana
en cuanto la limpieza se va a repetir, porque la próxima tanda de muestras llega igual
de sucia y el script ya sabe qué hacer.
