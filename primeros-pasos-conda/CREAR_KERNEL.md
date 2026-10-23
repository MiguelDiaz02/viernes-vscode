# Crear el entorno y el kernel de Python para la clase

Esta guía deja listo, **desde la terminal**, el entorno de Python y el *kernel* que usan los notebooks (`.ipynb`) de la clase. Se hace **una sola vez** y toma de 10 a 15 minutos.

| Tu sistema | Qué usas | Dónde |
| --- | --- | --- |
| **Windows** | Entorno virtual (`venv`), sin conda | [Ruta Windows](#ruta-windows--entorno-virtual-venv) |
| **macOS y Linux** | Entorno de **conda** llamado `viernes-vscode` | [Ruta macOS y Linux](#ruta-macos-y-linux--conda) |

> **¿Por qué Windows va por otro camino?** En algunas computadoras con Windows, el entorno de conda no puede cargar matplotlib: Windows bloquea un archivo de Pillow (*«Una directiva de Control de aplicaciones bloqueó este archivo»*). Con `venv` no pasa. En macOS y Linux no existe ese bloqueo.

### Qué es un kernel

Un notebook es solo un archivo con celdas. Quien **ejecuta** esas celdas es el *kernel*: un programa de Python que corre por detrás, ligado a un Python en particular, con sus propias bibliotecas (pandas, matplotlib…). Por eso VS Code te pide **elegir un kernel** al abrir un notebook. Esta guía lo crea.

### Qué terminal usar

| Sistema | Terminal |
| --- | --- |
| **Windows** | **PowerShell**. Lo más fácil: en VS Code, menú **Terminal → Nueva terminal** |
| **macOS** | Terminal (o la terminal de VS Code) |
| **Linux** | Terminal (Ctrl + Alt + T) o la terminal de VS Code |

Para pegar un comando: en Windows, clic derecho dentro de la terminal; en macOS, Cmd + V; en Linux, Ctrl + Shift + V. Después, Enter.

---

## Ruta Windows · Entorno virtual (venv)

Un *entorno virtual* es una carpeta con su propio Python y sus propias bibliotecas, aislada del resto de tu computadora. No necesitas permisos de administrador.

### W1 · Tener Python

Comprueba si ya lo tienes:

```powershell
py --version
```

Necesitas **Python 3.10 a 3.13** (recomendado **3.12**). Si responde un número en ese rango, pasa a W2. Si dice que no se reconoce el comando, o la versión es más vieja, o es 3.14 o más nueva, instálalo:

1. Descarga el instalador de **python.org → Downloads → Python 3.12** (Windows installer, 64-bit) y ábrelo.
2. En la **primera pantalla marca la casilla «Add python.exe to PATH»** y pulsa *Install Now*.
3. Cierra la terminal, abre otra y vuelve a correr `py --version`.

### W2 · Entrar a tu carpeta de clases

Usa una carpeta **con ruta corta, sin acentos ni espacios**, por ejemplo `C:\clases`. Créala si no existe y entra a ella:

```powershell
mkdir C:\clases
cd C:\clases
```

Si ya tienes el repositorio descargado, puede estar dentro de esa carpeta (`clases\viernes-vscode`). El entorno se crea **en `clases`**, no dentro del repositorio.

### W3 · Crear el entorno virtual

```powershell
py -m venv .venv
```

Tarda unos segundos y **no imprime nada**. Crea una carpeta oculta llamada `.venv`.

> Si usaste conda antes, ejecuta `conda deactivate` (las veces necesarias hasta que desaparezca `(base)` del inicio de la línea) **antes** de este paso.

### W4 · Activar el entorno

```powershell
.\.venv\Scripts\Activate.ps1
```

Al inicio de la línea debe aparecer **`(.venv)`**. Si no aparece, el entorno no está activo: no sigas.

Si sale *«la ejecución de scripts está deshabilitada en este sistema»*, ejecuta esto **una sola vez**, responde `S` si pregunta, y repite el comando de activación:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

(En el Símbolo del sistema `cmd` la activación es `.venv\Scripts\activate`.)

> **Cada vez que abras una terminal nueva** tendrás que activar el entorno otra vez (este mismo paso). La terminal de VS Code lo hace sola cuando ya elegiste el intérprete (más abajo, «Elegirlo en VS Code»).

### W5 · Instalar las bibliotecas

Con `(.venv)` visible:

```powershell
python -m pip install --upgrade pip
python -m pip install ipykernel pandas matplotlib
```

Tarda uno o dos minutos. `pandas` trae `numpy` por su cuenta. Con el entorno activado `python` ya apunta al del entorno: **no** uses `py` desde aquí.

### W6 · Crear el kernel

```powershell
python -m ipykernel install --user --name viernes-vscode --display-name "Python (viernes-vscode)"
```

**Debes ver:** `Installed kernelspec viernes-vscode in ...`

Si ya existía un kernel con ese nombre (por ejemplo, creado antes con conda), este comando lo reemplaza y ahora apuntará a tu `.venv`.

Sigue en [Comprobar que quedó bien](#comprobar-que-quedó-bien).

---

## Ruta macOS y Linux · Conda

### M1 · Tener el entorno de conda

Esta ruta usa el entorno **`viernes-vscode`** que se crea con la guía [Mis primeros pasos con conda](README.md) (instala Miniforge y crea el entorno). Si todavía no lo tienes, haz esa guía primero y vuelve aquí.

### M2 · Activar el entorno

```bash
conda activate viernes-vscode
```

Al inicio de la línea debe aparecer **`(viernes-vscode)`**. Si no aparece, el entorno no está activo y lo que sigue no sirve.

### M3 · Comprobar que `ipykernel` está instalado

```bash
python -c "import ipykernel; print('ipykernel', ipykernel.__version__)"
```

- Si imprime `ipykernel` y un número: sigue a M4.
- Si dice `ModuleNotFoundError`: instálalo y repite la comprobación.

```bash
conda install -y ipykernel
```

### M4 · Crear el kernel

```bash
python -m ipykernel install --user --name viernes-vscode --display-name "Python (viernes-vscode)"
```

**Debes ver:** `Installed kernelspec viernes-vscode in ...`

---

## Qué significa el comando del kernel

Es el mismo en las dos rutas:

| Parte | Para qué sirve |
| --- | --- |
| `python -m ipykernel install` | Pide a **este** Python (el del entorno activo) que se registre como kernel |
| `--user` | Lo registra solo para tu usuario; no necesita permisos de administrador |
| `--name viernes-vscode` | Nombre interno, sin espacios ni acentos |
| `--display-name "Python (viernes-vscode)"` | El nombre que verás en VS Code |

---

## Comprobar que quedó bien

Con el entorno activado (`(.venv)` en Windows, `(viernes-vscode)` en macOS y Linux):

```bash
python -c "import pandas, matplotlib; print('pandas', pandas.__version__, '| matplotlib', matplotlib.__version__)"
python -c "import sys; print(sys.executable)"
jupyter kernelspec list
```

Debes ver:

- una línea con las dos versiones, **sin errores**;
- una ruta que contenga **`.venv`** (Windows) o **`viernes-vscode`** (macOS y Linux);
- una línea con **`viernes-vscode`** en la lista de kernels.

Si descargaste el repositorio, el verificador revisa todo junto. Desde la carpeta del repositorio:

```bash
python primeros-pasos-conda/verificar_instalacion.py
```

Debe terminar con **Todo listo**.

---

## Elegirlo en VS Code

**Para notebooks (`.ipynb`):**

1. Abre un archivo `.ipynb`.
2. Arriba a la derecha, clic en **Select Kernel**.
3. Elige **Jupyter Kernel…** y después **Python (viernes-vscode)**.
4. Si no aparece: pulsa el botón de refrescar (↻) de esa lista. Si sigue sin aparecer, **Ctrl + Shift + P** (macOS: Cmd + Shift + P), escribe `Reload Window` y pulsa Enter.

**Para scripts (`.py`) y el depurador (F5):**

1. **Ctrl + Shift + P** (macOS: Cmd + Shift + P) → escribe `Python: Select Interpreter`.
2. En la lista, elige el que dice **`.venv`** (Windows) o **`viernes-vscode`** (macOS y Linux).
3. **Solo si no aparece:** elige **Enter interpreter path… → Find…** y señala:

| Sistema | Ruta |
| --- | --- |
| Windows | `C:\clases\.venv\Scripts\python.exe` |
| macOS y Linux | `~/miniforge3/envs/viernes-vscode/bin/python` |

Abajo a la derecha de VS Code debe verse la versión de Python junto al nombre del entorno.

### Prueba final en un notebook

En la primera celda, escribe y ejecuta con **Shift + Enter**:

```python
import sys
print(sys.executable)
```

La ruta debe contener **`.venv`** (Windows) o **`viernes-vscode`** (macOS y Linux). Después:

```python
import pandas as pd
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.show()
```

Debe aparecer una línea dentro del notebook, sin ventanas extra y sin que el kernel se cierre.

---

## Problemas comunes

| Qué ves | Causa probable | Qué hacer |
| --- | --- | --- |
| `ModuleNotFoundError: No module named 'ipykernel'` (o `pandas`, `matplotlib`) | Lo ejecutaste fuera del entorno, o falta instalar | Activa el entorno y repite el paso de instalación |
| No aparece `(.venv)` / `(viernes-vscode)` al inicio de la línea | El entorno no está activo | Windows: repite W4 desde `C:\clases`. macOS y Linux: repite M2 |
| El kernel no aparece en **Select Kernel** | VS Code no ha vuelto a leer la lista | Botón ↻ de la lista, o `Reload Window`. Comprueba con `jupyter kernelspec list` que existe |
| Aparece, pero `sys.executable` es de otro Python | Creaste el kernel con otro entorno activo | Bórralo (ver abajo), activa el entorno correcto y repite el paso de crear el kernel |
| **Windows:** `py` o `python` no se reconoce | Python no está instalado, o no se marcó *Add python.exe to PATH* | Instálalo de python.org (W1), marca la casilla y abre una terminal **nueva** |
| **Windows:** `python` abre la Microsoft Store | La tienda intercepta el comando | Usa `py` en W3, o instala Python de python.org |
| **Windows**, PowerShell: *«la ejecución de scripts está deshabilitada»* | PowerShell bloquea `Activate.ps1` | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y repite W4. O usa `cmd` |
| **Windows:** el nombre de usuario tiene acento o espacio (por ejemplo `Miguel Díaz`) y falla el registro | Rutas con caracteres especiales | Usa `--sys-prefix` en lugar de `--user` en W6, y mantén el entorno en `C:\clases` |
| **Windows:** `ImportError: DLL load failed ... Una directiva de Control de aplicaciones bloqueó este archivo` | Windows bloquea un archivo (Smart App Control o política de tu institución) | Si estás usando conda, sal de él (`conda deactivate`) y usa la ruta Windows de esta guía. Si falla también en `.venv`, usa **Codespaces** |
| **Windows:** el kernel se cierra («The Kernel crashed») al importar pandas o graficar | Entorno mezclado con otras instalaciones | Borra y recrea el entorno (ver abajo) |
| **Linux:** `conda: command not found` | La terminal se abrió antes de instalar conda | Cierra **toda** la terminal y abre otra; si sigue, mira la guía de conda |
| **macOS y Linux:** el kernel se cierra («The Kernel crashed») | Entorno creado con una versión vieja de la guía | Recrea el entorno con `conda env remove -n viernes-vscode -y` y `conda env create -f primeros-pasos-conda/environment.yml` |

### Borrar el kernel y empezar de nuevo

```bash
jupyter kernelspec remove viernes-vscode -f
```

Quita solo el registro del kernel; no borra el entorno ni tus archivos. Para recrear **todo** desde cero:

- **Windows:** `deactivate`, luego `Remove-Item -Recurse -Force .venv` (desde `C:\clases`) y repite W3 a W6.
- **macOS y Linux:** `conda deactivate`, luego `conda env remove -n viernes-vscode -y` y repite la guía de conda y M2 a M4.

---

## Lista de verificación

- [ ] Veo `(.venv)` (Windows) o `(viernes-vscode)` (macOS y Linux) al inicio de la línea
- [ ] `python -c "import pandas, matplotlib"` no da error
- [ ] El comando de crear el kernel respondió `Installed kernelspec viernes-vscode`
- [ ] `jupyter kernelspec list` muestra `viernes-vscode`
- [ ] En VS Code, **Select Kernel** muestra **Python (viernes-vscode)**
- [ ] La prueba final imprime una ruta con `.venv` o `viernes-vscode`, y el gráfico aparece sin cerrarse el kernel
