# Ejercicio 1 · Limpiar los metadatos con pandas

El script `01_explorar_metadatos.py` reporta 5 muestras de normoxia. Deberían ser 4.

Escribe `scripts/ej01_limpiar_metadatos.py` que lea `data/metadatos_muestras.csv` y:

1. Normalice `condition` (minúsculas, sin espacios sobrantes)
2. Quite la fila duplicada
3. Convierta `fecha_extraccion` a un solo formato ISO (`AAAA-MM-DD`)
4. Convierta `rin` y `lecturas_millones` a numérico, con `NaN` donde no haya valor
5. Quite espacios sobrantes en `operador`
6. Guarde el resultado en `data/metadatos_limpios.csv`

Prueba: `01_explorar_metadatos.py` leyendo el archivo limpio debe dar 4-4-4.

**Pista de VS Code:** escribe el script con celdas `# %%` y ve verificando cada paso en la
ventana interactiva con Shift+Enter, en lugar de correr todo el archivo cada vez.

---

Solución: `soluciones/ej01_limpiar_metadatos.py`. Se publica en el repositorio después de la clase.
