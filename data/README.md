# Los datos de la clase

Datos reales de **hepatocarcinoma** (carcinoma hepatocelular), reducidos para que se
puedan leer y analizar en un par de segundos.

**Fuente:** proyecto TCGA Liver Hepatocellular Carcinoma (TCGA-LIHC), versión *Firehose Legacy*,
tomado del repositorio público de cBioPortal (estudio `lihc_tcga`). Son datos de acceso abierto.
Si los usas en un trabajo, cita al TCGA Research Network:
*Comprehensive and Integrative Genomic Characterization of Hepatocellular Carcinoma*,
Cell, 2017, 169(7):1327-1341.

## `hcc_tabla.csv`: la tabla de la clase

Es la tabla que usamos en la clase. **Una fila por paciente**, ya con las dos fuentes unidas y la
expresión en escala log2(valor + 1), para poder empezar a analizar sin preparar nada.

| Columna | Qué es |
| --- | --- |
| `id_paciente` | Identificador del paciente, por ejemplo `TCGA-2V-A95S` |
| `grado` | Grado histológico del tumor: G1 (bien diferenciado) a G4 (poco diferenciado). Faltan 5 |
| `edad` | Edad al diagnóstico, en años. Falta 1 |
| `sexo` | `Male` o `Female` |
| `AFP`, `CA9`, `TOP2A`, `ALB`, `GAPDH` | Expresión de cada gen, en log2(valor + 1) |

371 pacientes × 9 columnas. Los valores faltantes están vacíos. Los dos archivos de abajo
(`hcc_expresion.csv` y `hcc_clinicos.csv`) son los datos originales, de los que sale esta tabla;
los usa la versión avanzada del análisis en `respaldo/analisis_hcc_completo`.

## Qué le quitamos al original

| Original | Aquí |
| --- | --- |
| 20 531 genes | **12 genes** |
| 373 muestras de tumor | **371 tumores primarios** (muestras que terminan en `-01`) |
| 74 variables clínicas | **7 variables** |

Los 12 genes se eligieron porque cuentan una historia:

| Grupo | Genes | Qué esperamos |
| --- | --- | --- |
| Tumor agresivo | `AFP`, `GPC3` | Más expresión en tumores de grado alto |
| Proliferación | `MKI67`, `TOP2A` | Más expresión en tumores de grado alto |
| Hipoxia | `CA9`, `VEGFA`, `SLC2A1` | Varían, sobre todo `CA9` |
| Función hepática | `ALB`, `APOA1`, `TTR` | Menos expresión en tumores de grado alto |
| Genes de referencia | `GAPDH`, `ACTB` | Casi no cambian |

## `hcc_expresion.csv`

Genes en **filas** y muestras en **columnas**, como llegan los datos de TCGA. El valor es la
expresión normalizada por RSEM (cuentas estimadas, sin transformar).

- Primera columna: `gen`
- Las demás columnas: una muestra cada una, por ejemplo `TCGA-2V-A95S-01`

El identificador de la muestra termina en `-01` (tumor primario). Para unir esta tabla con la
clínica hay que quitar ese final y quedarse con el paciente: `TCGA-2V-A95S`.

## `hcc_clinicos.csv`

Una fila por paciente.

| Columna | Qué es |
| --- | --- |
| `id_paciente` | Identificador del paciente, por ejemplo `TCGA-2V-A95S` |
| `edad` | Edad al diagnóstico, en años |
| `sexo` | `Male` o `Female` |
| `grado` | Grado histológico del tumor: G1 (bien diferenciado) a G4 (poco diferenciado) |
| `estadio` | Estadio AJCC (Stage I a IV) |
| `factor_riesgo` | Factores de riesgo conocidos; puede haber varios separados por `\|` |
| `estado_vital` | `0:LIVING` o `1:DECEASED` |
| `meses_supervivencia` | Meses de seguimiento |

**Los valores faltantes vienen como texto**, igual que en el original: `[Not Available]`,
`[Not Applicable]`, `[Unknown]` o `[Discrepancy]`. Pandas no sabe que eso significa «vacío»;
hay que decírselo al leer el archivo (`na_values=`). Pasa todo el tiempo con datos reales.

Los valores `Male`, `Female` y los estadios se dejaron en inglés, como están en el original.

---

# Los datos de la práctica en casa: un experimento inventado

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
