"""Solución del ejercicio 4: diferencia hipoxia_24h - normoxia por gen."""

import pandas as pd

from utils import limpiar_condicion, log_cpm, ruta_datos

conteos = pd.read_csv(ruta_datos("conteos.tsv"), sep="\t", index_col=0)
normalizado = log_cpm(conteos)

meta = pd.read_csv(ruta_datos("metadatos_muestras.csv")).drop_duplicates("sample_id")
meta["condition"] = limpiar_condicion(meta["condition"])

# Punto de interrupción sugerido: la línea siguiente. Inspecciona `promedios` en el panel de variables.
promedios = normalizado.T.groupby(meta.set_index("sample_id")["condition"]).mean().T

log2fc = (promedios["hipoxia_24h"] - promedios["normoxia"]).sort_values(ascending=False)
print("Suben más:")
print(log2fc.head(5).round(2))
print("\nBajan más:")
print(log2fc.tail(5).round(2))
