"""Normalizar conteos a CPM (conteos por millón) y guardar el resultado."""

import pandas as pd

from utils import log_cpm, ruta_resultados

conteos = pd.read_csv(
    "/home/miguel/proyectos/viernes-vscode/data/conteos.tsv",
    sep="\t",
    index_col=0,
)

normalizado = log_cpm(conteos)

salida = ruta_resultados("conteos_cpm.tsv")
normalizado.round(3).to_csv(salida, sep="\t")
print(f"Guardado en {salida}")
print(normalizado.iloc[:5, :4])
