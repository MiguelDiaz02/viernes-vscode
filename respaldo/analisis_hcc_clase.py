"""Expresión génica en hepatocarcinoma (TCGA-LIHC) por grado del tumor. Versión corta de la clase.

Ejecútalo desde la RAÍZ de la carpeta del proyecto (la que contiene scripts/):
    python scripts/analisis_hcc.py
"""

# ------------------------------------------------------------
# 1. Bibliotecas
# ------------------------------------------------------------
import os  # os: sirve para crear carpetas
import pandas as pd  # pandas: trabaja con tablas (pd es su apodo)
import matplotlib.pyplot as plt  # matplotlib: dibuja figuras (plt es su apodo)

# ------------------------------------------------------------
# 2. Carpetas del proyecto
# ------------------------------------------------------------
os.makedirs("data", exist_ok=True)  # crea la carpeta de los datos
os.makedirs("results/tablas", exist_ok=True)  # crea la carpeta de las tablas de resultados
os.makedirs("results/figuras", exist_ok=True)  # crea la carpeta de las figuras

# ------------------------------------------------------------
# 3. Descargar los datos
# ------------------------------------------------------------
url = "https://raw.githubusercontent.com/MiguelDiaz02/viernes-vscode/main/data/hcc_tabla.csv"  # dirección del archivo
datos = pd.read_csv(url)  # pandas lee el archivo y lo guarda en la variable datos
datos.to_csv("data/hcc_tabla.csv", index=False)  # guarda una copia en la carpeta data

# ------------------------------------------------------------
# 4. Conocer la tabla
# ------------------------------------------------------------
print(datos.shape)  # (filas, columnas): debe dar (371, 9)
print(datos.head())  # las primeras 5 filas
print(datos["grado"].value_counts())  # cuántos pacientes hay en cada grado (G1 es el más parecido al hígado sano)

# ------------------------------------------------------------
# 5. Datos faltantes
# ------------------------------------------------------------
print(datos.isna().sum())  # cuántos valores vacíos hay en cada columna
datos = datos.dropna(subset=["grado"])  # quita los pacientes que no tienen grado
print(datos.shape)  # ahora debe dar (366, 9)

# ------------------------------------------------------------
# 6. Promedio de cada gen por grado
# ------------------------------------------------------------
genes = ["AFP", "CA9", "TOP2A", "ALB", "GAPDH"]  # lista con los genes que vamos a comparar
resumen = datos.groupby("grado")[genes].mean()  # promedio de cada gen en cada grado
print(resumen.round(2))  # muestra la tabla con 2 decimales
resumen.round(2).to_csv("results/tablas/resumen_por_grado.csv")  # guarda la tabla en results/tablas

# ------------------------------------------------------------
# 7. Figura
# ------------------------------------------------------------
resumen.plot(kind="bar", rot=0, figsize=(8, 4))  # barras: una por gen, agrupadas por grado
plt.title("Expresión promedio por grado tumoral (TCGA-LIHC)")  # título de la figura
plt.ylabel("log2(expresión + 1)")  # nombre del eje vertical
plt.legend(title="gen", bbox_to_anchor=(1.02, 1), loc="upper left")  # leyenda fuera de la figura, a la derecha
plt.savefig("results/figuras/expresion_por_grado.png", dpi=150, bbox_inches="tight")  # guarda la imagen
plt.close()  # cierra la figura; ábrela desde el Explorador (results/figuras)
