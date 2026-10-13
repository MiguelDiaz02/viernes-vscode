# Ejercicio 4 · Usar el depurador en lugar de print

Queremos saber qué gen cambia más entre hipoxia 24 h y normoxia.

1. Escribe `scripts/ej04_depurador.py` que calcule, a partir de `log_cpm`, el promedio por
   condición y la diferencia `hipoxia_24h - normoxia` para cada gen.
2. Antes de correrlo completo, pon un punto de interrupción (clic en el margen izquierdo)
   justo después de calcular los promedios y presiona F5.
3. En el panel de variables, inspecciona la tabla de promedios. ¿Tiene las tres columnas
   que esperabas? ¿Los nombres coinciden con `orden`?
4. Avanza línea por línea con F10 hasta el final.
5. Ordena los genes por diferencia e imprime los cinco de arriba y los cinco de abajo.

Arriba deberían quedar genes de respuesta a hipoxia (ALDOA, ANKRD37, P4HA1, CA9, VEGFA…) y abajo los hepáticos (TTR, APOA1, ALB). Si no, el depurador te dice en qué paso se torció.

---

Solución: `soluciones/ej04_depurador.py`. Se publica en el repositorio después de la clase.
