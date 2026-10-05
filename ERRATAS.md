# Erratas sembradas (para quien da la clase)

Cuatro fallas, una por script, en el orden en que se corrigen. Cada una tarda menos
de un minuto y produce un commit con sentido.

| # | Archivo | Línea aproximada | Qué está mal | Cómo se corrige | Error que produce |
| --- | --- | --- | --- | --- | --- |
| 1 | `scripts/01_explorar_metadatos.py` | 18 y 19 | La columna se llama `condicion` en el script y `condition` en el CSV | Cambiar `"condicion"` por `"condition"` (aparece dos veces en esa celda; Ctrl+D las toma juntas) | `KeyError: 'condicion'` |
| 2 | `scripts/02_cargar_conteos.py` | 7 | `sep=","` para un archivo tabulado | `sep="\t"` | Imprime `50 genes x 0 muestras` y luego `No cuadran: faltan {...}` |
| 3 | `scripts/03_normalizar.py` | 8 | Ruta absoluta `/home/miguel/proyectos/...` | `ruta_datos("conteos.tsv")` e importar `ruta_datos` desde `utils` | `FileNotFoundError` |
| 4 | `scripts/04_grafico_expresion.py` | 3 | Falta `import matplotlib.pyplot as plt` | Agregar el import. La bombilla de VS Code (Ctrl+.) lo ofrece sola | `NameError: name 'plt' is not defined` |

Mensajes de commit sugeridos, en orden:

1. `Corrige nombre de columna y normaliza valores de condition`
2. `Corrige separador de TSV y ruta absoluta` (fallas 2 y 3 juntas, desde el servidor)
3. `Agrega import faltante`

## Cosas que no son fallas pero se ven en clase

- El script 01 reporta **5** muestras de normoxia en lugar de 4: es el duplicado del CSV. No lo corrijas en clase; es el ejercicio 1.
- Después de normalizar `condition` con multicursor en el CSV, `git status` mostrará el CSV modificado además del script. Va en el mismo primer commit.
- `results/` está en `.gitignore`. Cuando corras 03 y 04, la carpeta aparece en el explorador pero no en el panel de Git. Es intencional y vale la pena señalarlo.

## Si alguien ya corrigió el repo

Para volver al estado con fallas: `git checkout -- scripts/` deshace cambios sin commit.
Si ya hubo commits, `git log` para ver el inicial y `git reset --hard <hash>`.
