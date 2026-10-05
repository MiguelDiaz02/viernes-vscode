"""Cargar la matriz de conteos y revisar que cuadre con los metadatos."""

import pandas as pd

from utils import ruta_datos

conteos = pd.read_csv(ruta_datos("conteos.tsv"), sep=",", index_col=0)
print(f"{conteos.shape[0]} genes x {conteos.shape[1]} muestras")

meta = pd.read_csv(ruta_datos("metadatos_muestras.csv")).drop_duplicates("sample_id")
faltan = set(meta["sample_id"]) - set(conteos.columns)
sobran = set(conteos.columns) - set(meta["sample_id"])

if faltan or sobran:
    raise SystemExit(f"No cuadran: faltan {faltan}, sobran {sobran}")

print("Metadatos y conteos cuadran.")
print(conteos.describe().T[["mean", "min", "max"]].head())
