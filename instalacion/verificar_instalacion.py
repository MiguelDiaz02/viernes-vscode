"""Comprueba que el entorno de la clase está listo.

Uso, desde la carpeta del repositorio y con el entorno activado:

    python instalacion/verificar_instalacion.py

Si todas las líneas dicen [OK], ya estás listo para la clase.
"""

import importlib
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
problemas = []


def ok(texto):
    print(f"  [OK]    {texto}")


def falta(texto, solucion):
    print(f"  [FALTA] {texto}")
    print(f"          -> {solucion}")
    problemas.append(texto)


def aviso(texto):
    print(f"  [AVISO] {texto}")


print("\nComprobando la instalación para la clase de VS Code\n")

# 1. Versión de Python
v = sys.version_info
if v >= (3, 10):
    ok(f"Python {v.major}.{v.minor}.{v.micro}")
else:
    falta(
        f"Python {v.major}.{v.minor} es muy viejo (se necesita 3.10 o más)",
        "activa el entorno: conda activate viernes-vscode",
    )

# 2. ¿Es el entorno de la clase?
print(f"          usando: {sys.executable}")
if "viernes-vscode" not in sys.executable and ".venv" not in sys.executable:
    aviso(
        "este Python no parece ser el entorno 'viernes-vscode'. "
        "Si algo de abajo falla, ejecuta primero: conda activate viernes-vscode"
    )

# 3. Paquetes
paquetes = [
    ("pandas", (2, 2)),
    ("numpy", None),
    ("matplotlib", (3, 9)),
    ("ipykernel", None),
]
for nombre, minimo in paquetes:
    try:
        modulo = importlib.import_module(nombre)
        version = getattr(modulo, "__version__", "?")
        if minimo:
            partes = tuple(int(p) for p in version.split(".")[:2] if p.isdigit())
            if partes and partes < minimo:
                falta(
                    f"{nombre} {version} (se necesita {'.'.join(map(str, minimo))} o más)",
                    f"conda install -c conda-forge '{nombre}>={'.'.join(map(str, minimo))}'",
                )
                continue
        ok(f"{nombre} {version}")
    except ImportError:
        falta(
            f"{nombre} no está instalado en este Python",
            "conda env create -f instalacion/environment.yml  (o revisa que el entorno esté activado)",
        )

# 4. Ruff (opcional)
if shutil.which("ruff"):
    ok("ruff disponible (formateador)")
else:
    aviso("ruff no está instalado. No es indispensable para la clase.")

# 5. Datos de la clase
for archivo in ["data/metadatos_muestras.csv", "data/conteos.tsv"]:
    if (RAIZ / archivo).exists():
        ok(f"{archivo} encontrado")
    else:
        falta(
            f"{archivo} no existe",
            "ejecuta este script desde dentro de la carpeta viernes-vscode completa",
        )

# 6. Kernel registrado para notebooks
try:
    from jupyter_client.kernelspec import KernelSpecManager

    kernels = KernelSpecManager().find_kernel_specs()
    if "viernes-vscode" in kernels:
        ok("kernel 'Python (viernes-vscode)' registrado para notebooks")
    else:
        aviso(
            "el kernel no está registrado con nombre propio. VS Code igual lo encuentra, "
            "pero para verlo con nombre claro ejecuta:\n"
            '          python -m ipykernel install --user --name viernes-vscode '
            '--display-name "Python (viernes-vscode)"'
        )
except ImportError:
    pass

# Resumen
print()
if problemas:
    print(f"Hay {len(problemas)} cosa(s) por resolver. Sigue las flechas -> de arriba.")
    print("Si te atoras, revisa la sección 'Problemas comunes' en instalacion/README.md\n")
    sys.exit(1)
else:
    print("Todo listo. Nos vemos en la clase.\n")
