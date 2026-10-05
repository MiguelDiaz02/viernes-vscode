"""Graficar la expresión de genes de respuesta a hipoxia."""

import pandas as pd

from utils import limpiar_condicion, log_cpm, ruta_datos, ruta_resultados

conteos = pd.read_csv(ruta_datos("conteos.tsv"), sep="\t", index_col=0)
normalizado = log_cpm(conteos)

meta = pd.read_csv(ruta_datos("metadatos_muestras.csv")).drop_duplicates("sample_id")
meta["condition"] = limpiar_condicion(meta["condition"])
orden = ["normoxia", "hipoxia_6h", "hipoxia_24h"]

genes = ["VEGFA", "CA9", "SLC2A1", "BNIP3", "ALB", "GAPDH"]

fig, axes = plt.subplots(2, 3, figsize=(10, 6))
for gen, ax in zip(genes, axes.flat):
    datos = [
        normalizado.loc[gen, meta.loc[meta["condition"] == c, "sample_id"]].values
        for c in orden
    ]
    ax.boxplot(datos, tick_labels=["normoxia", "6 h", "24 h"])
    ax.set_title(gen)
    ax.set_ylabel("log2(CPM + 1)")

fig.suptitle("Respuesta a hipoxia en HepG2")
fig.tight_layout()
salida = ruta_resultados("expresion_hipoxia.png")
fig.savefig(salida, dpi=150)
print(f"Figura guardada en {salida}")
