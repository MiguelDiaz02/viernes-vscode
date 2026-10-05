"""Funciones compartidas por los scripts de la clase."""

from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def ruta_datos(nombre: str) -> Path:
    """Devuelve la ruta a un archivo dentro de data/, relativa al repositorio.

    Funciona igual en tu laptop, en el servidor y en un contenedor,
    porque se calcula a partir de dónde está este archivo.
    """
    return RAIZ / "data" / nombre


def ruta_resultados(nombre: str) -> Path:
    """Devuelve la ruta a un archivo dentro de results/, creando la carpeta si no existe."""
    carpeta = RAIZ / "results"
    carpeta.mkdir(exist_ok=True)
    return carpeta / nombre


def limpiar_condicion(serie):
    """Normaliza la columna condition: minúsculas y sin espacios sobrantes."""
    return serie.str.strip().str.lower()


def log_cpm(conteos):
    """Conteos por millón en escala log2(CPM + 1), a partir de una matriz genes x muestras."""
    import numpy as np

    cpm = conteos / conteos.sum(axis=0) * 1e6
    return np.log2(cpm + 1)
