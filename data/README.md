# El experimento (inventado)

Células HepG2 (hepatocarcinoma humano) cultivadas en normoxia o expuestas a hipoxia
(1 % O₂) durante 6 o 24 horas. Cuatro réplicas por condición, en dos lotes de cultivo.
RNA-seq de extremos pareados. Los números son simulados; los genes y la biología, no.

## `metadatos_muestras.csv`

Una fila por muestra. Llegó así del laboratorio, con los problemas de siempre:

- `condition` tiene mayúsculas mezcladas y un espacio al final en una fila
- `fecha_extraccion` viene en dos formatos distintos
- `rin` tiene un `n/a` en lugar de un valor vacío
- `lecturas_millones` tiene una celda vacía
- `operador` tiene un espacio al inicio en una fila
- hay una muestra duplicada

Nada de esto es un error de los datos. Es lo que hay que limpiar antes de analizar.

| Columna | Qué es |
| --- | --- |
| `sample_id` | Identificador de la muestra |
| `condition` | normoxia, hipoxia_6h o hipoxia_24h |
| `tiempo_h` | Horas de exposición a hipoxia |
| `replica` | Número de réplica biológica |
| `lote` | Lote de cultivo (L1 o L2) |
| `fecha_extraccion` | Fecha de extracción de RNA |
| `rin` | RNA Integrity Number |
| `lecturas_millones` | Lecturas secuenciadas, en millones |
| `operador` | Quien hizo la extracción |

## `conteos.tsv`

Matriz de 50 genes × 12 muestras, conteos crudos, separada por tabuladores.
Incluye genes de respuesta a hipoxia (VEGFA, CA9, SLC2A1, BNIP3, LDHA…), genes de
referencia estables (ACTB, GAPDH, RPLP0…) y genes hepáticos que bajan a las 24 h
(ALB, APOA1, TTR). Hay un efecto de lote pequeño en L2.
