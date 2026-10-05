"""Explorar los metadatos de las muestras.

Primer contacto con el experimento: cuántas muestras hay,
de qué condición, y qué tan sucia está la tabla.
"""

# %%
import pandas as pd

from utils import limpiar_condicion, ruta_datos

# %%
meta = pd.read_csv(ruta_datos("metadatos_muestras.csv"))
print(f"{meta.shape[0]} filas, {meta.shape[1]} columnas")
print(meta.head())

# %%
# Muestras por condición. Ojo: la columna viene con mayúsculas mezcladas.
meta["condicion"] = limpiar_condicion(meta["condicion"])
print(meta["condicion"].value_counts())

# %%
# ¿Hay identificadores repetidos?
duplicados = meta[meta["sample_id"].duplicated(keep=False)]
print(f"Duplicados encontrados: {len(duplicados)}")
print(duplicados)

# %%
# Distribución de RIN por condición
meta["rin"] = pd.to_numeric(meta["rin"], errors="coerce")
print(meta.groupby("condicion")["rin"].describe())

# %%
ax = meta.groupby("condicion")["lecturas_millones"].mean().plot.bar(
    title="Lecturas promedio por condición (millones)"
)
ax.set_xlabel("")
