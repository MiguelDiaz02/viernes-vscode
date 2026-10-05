"""Solución del ejercicio 3: 02_cargar_conteos.py con celdas y genes más variables."""

# %%
import pandas as pd

from utils import ruta_datos

# %%
conteos = pd.read_csv(ruta_datos("conteos.tsv"), sep="\t", index_col=0)
print(f"{conteos.shape[0]} genes x {conteos.shape[1]} muestras")

# %%
meta = pd.read_csv(ruta_datos("metadatos_muestras.csv")).drop_duplicates("sample_id")
assert set(meta["sample_id"]) == set(conteos.columns), "Metadatos y conteos no cuadran"

# %%
cv = conteos.std(axis=1) / conteos.mean(axis=1)
top = cv.sort_values(ascending=False).head(10)
print(top.round(2))

# %%
ax = top.sort_values().plot.barh(title="Diez genes más variables (CV)")
ax.set_xlabel("Coeficiente de variación")

# El script con celdas vive en Git sin salidas pesadas y se puede importar como módulo.
# El notebook guarda las figuras junto al código y es mejor para contar una historia.
