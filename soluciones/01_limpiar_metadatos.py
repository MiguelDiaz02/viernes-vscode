"""Solución del ejercicio 1: limpiar los metadatos."""

# %%
import pandas as pd

from utils import limpiar_condicion, ruta_datos

# %%
meta = pd.read_csv(ruta_datos("metadatos_muestras.csv"))

# %%
meta["condition"] = limpiar_condicion(meta["condition"])
meta = meta.drop_duplicates("sample_id").reset_index(drop=True)

# %%
# Dos formatos de fecha: ISO y DD/MM/AAAA. to_datetime con format="mixed" resuelve ambos.
meta["fecha_extraccion"] = pd.to_datetime(
    meta["fecha_extraccion"], format="mixed", dayfirst=True
).dt.strftime("%Y-%m-%d")

# %%
meta["rin"] = pd.to_numeric(meta["rin"], errors="coerce")
meta["lecturas_millones"] = pd.to_numeric(meta["lecturas_millones"], errors="coerce")
meta["operador"] = meta["operador"].str.strip()

# %%
print(meta["condition"].value_counts())
meta.to_csv(ruta_datos("metadatos_limpios.csv"), index=False)
print("Guardado en data/metadatos_limpios.csv")
