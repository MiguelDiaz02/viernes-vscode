"""Expresión génica en hepatocarcinoma (TCGA-LIHC): ¿cambia con el grado del tumor?

Script terminado de la clase, por si te perdiste en algún bloque.
Se escribe desde cero en scripts/analisis_hcc.py dentro de una carpeta vacía:
el propio script crea las carpetas y descarga los datos. Bloques numerados del 1 al 6.
"""

# ------------------------------------------------------------------
# 1a. Bibliotecas
# ------------------------------------------------------------------
from pathlib import Path
from urllib.request import urlretrieve

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ------------------------------------------------------------------
# 1b. Rutas del proyecto y carpetas
# ------------------------------------------------------------------
RAIZ = Path(__file__).resolve().parent.parent
CARPETA_DATOS = RAIZ / "data"
CARPETA_TABLAS = RAIZ / "results" / "tablas"
CARPETA_FIGURAS = RAIZ / "results" / "figuras"

for carpeta in (CARPETA_DATOS, CARPETA_TABLAS, CARPETA_FIGURAS):
    carpeta.mkdir(parents=True, exist_ok=True)  # si ya existe, no pasa nada

print("Proyecto en:", RAIZ)


# ------------------------------------------------------------------
# 1c. Descargar los datos
# ------------------------------------------------------------------
URL_BASE = "https://raw.githubusercontent.com/MiguelDiaz02/viernes-vscode/main/data"
ARCHIVOS = ["hcc_expresion.csv", "hcc_clinicos.csv"]


def descargar(nombre):
    """Descarga un archivo de datos a data/ (si ya está, no lo vuelve a bajar)."""
    destino = CARPETA_DATOS / nombre
    if destino.exists():
        print("Ya existe:", destino.name)
        return destino
    urlretrieve(f"{URL_BASE}/{nombre}", destino)
    print("Descargado:", destino.name)
    return destino


for archivo in ARCHIVOS:
    descargar(archivo)


# ------------------------------------------------------------------
# 2. Cargar los datos
# ------------------------------------------------------------------
expresion = pd.read_csv(CARPETA_DATOS / "hcc_expresion.csv", index_col="gen")
clinicos = pd.read_csv(
    CARPETA_DATOS / "hcc_clinicos.csv",
    index_col="id_paciente",
    na_values=["[Not Available]", "[Not Applicable]", "[Unknown]", "[Discrepancy]"],
)

print("Expresión (genes x muestras):", expresion.shape)
print("Clínicos (pacientes x variables):", clinicos.shape)
print(clinicos.head())


# ------------------------------------------------------------------
# 3. Funciones
# ------------------------------------------------------------------
def log2_expresion(tabla):
    """Pasa la expresión a log2(valor + 1) para comprimir la escala."""
    return np.log2(tabla + 1)


def agrupar_grado(grado):
    """Junta los grados del tumor en dos grupos: G1-G2 (bajo) y G3-G4 (alto)."""
    if grado in ("G1", "G2"):
        return "G1-G2"
    return "G3-G4"


def resumir_por_grupo(datos, genes):
    """Promedio de cada gen por grupo de grado y cambio entre grupos (en log2)."""
    promedios = datos.groupby("grupo_grado")[genes].mean().T
    promedios["cambio_log2"] = promedios["G3-G4"] - promedios["G1-G2"]
    return promedios.sort_values("cambio_log2", ascending=False)


# ------------------------------------------------------------------
# 4. Preparar la tabla de trabajo
# ------------------------------------------------------------------
genes = list(expresion.index)

datos = log2_expresion(expresion).T  # ahora: muestras en filas, genes en columnas
datos.index = datos.index.str[:12]  # TCGA-2V-A95S-01 -> TCGA-2V-A95S
datos.index.name = "id_paciente"
datos = datos.join(clinicos)  # une las dos tablas por id_paciente
datos = datos.dropna(subset=["grado"])  # fuera los pacientes sin grado
datos["grupo_grado"] = datos["grado"].map(agrupar_grado)

print("Tabla de trabajo:", datos.shape)
print(datos["grupo_grado"].value_counts())


# ------------------------------------------------------------------
# 5. Resumen por grupo
# ------------------------------------------------------------------
resumen = resumir_por_grupo(datos, genes)
print(resumen.round(2))

resumen.round(3).to_csv(CARPETA_TABLAS / "resumen_por_grado.csv")


# ------------------------------------------------------------------
# 6. Figura
# ------------------------------------------------------------------
genes_figura = ["AFP", "CA9", "TOP2A", "ALB"]

fig, ejes = plt.subplots(1, len(genes_figura), figsize=(12, 3.5))
for eje, gen in zip(ejes, genes_figura):
    grado_bajo = datos.loc[datos["grupo_grado"] == "G1-G2", gen]
    grado_alto = datos.loc[datos["grupo_grado"] == "G3-G4", gen]
    eje.boxplot([grado_bajo, grado_alto], tick_labels=["G1-G2", "G3-G4"])
    eje.set_title(gen)

ejes[0].set_ylabel("log2(expresión + 1)")
fig.suptitle("Expresión por grado tumoral (TCGA-LIHC)")
fig.tight_layout()
fig.savefig(CARPETA_FIGURAS / "expresion_por_grado.png", dpi=150)
plt.close(fig)

print("Figura guardada en", CARPETA_FIGURAS / "expresion_por_grado.png")
