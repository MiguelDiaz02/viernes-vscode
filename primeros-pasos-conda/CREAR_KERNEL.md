# Crear el kernel de Python para los notebooks

Esta guía deja listo, **desde la terminal**, el *kernel* que usan los notebooks (`.ipynb`) de la clase. Funciona en **Windows, macOS y Linux**. Se hace **una sola vez** y toma unos 5 minutos.

---

## ¿Qué es un kernel?

Un notebook es solo un archivo con celdas. Quien **ejecuta** esas celdas es el *kernel*: un programa de Python que corre por detrás. Cada kernel está ligado a un Python en particular, con sus propias bibliotecas (pandas, matplotlib…).

Por eso, antes de correr un notebook, VS Code te pide **elegir un kernel**. Si tu computadora no tiene uno con las bibliotecas de la clase, esta guía lo crea.

---

## Elige tu camino

| Si… | Camino |
| --- | --- |
| Ya hiciste la guía [Mis primeros pasos con conda](README.md) y tienes el entorno `viernes-vscode` | **Camino A** (2 minutos) |
| No usas conda y tienes Python instalado (de python.org, Homebrew, `apt`…) | **Camino B** (5 minutos) |

Los dos terminan igual: un kernel llamado **Python (viernes-vscode)** que aparece en VS Code.

### Qué terminal usar

| Sistema | Terminal |
| --- | --- |
| **Windows**, Camino A | **Miniforge Prompt** (menú Inicio). No uses PowerShell para los comandos de conda. |
| **Windows**, Camino B | **Símbolo del sistema** (`cmd`) o **Git Bash**. PowerShell funciona, pero a veces bloquea la activación (ver *Problemas comunes*). |
| **macOS** | Terminal |
| **Linux** | Terminal (Ctrl + Alt + T) |

Para pegar un comando: en Windows, clic derecho dentro de la terminal (o Ctrl + Shift + V en Git Bash); en macOS, Cmd + V; en Linux, Ctrl + Shift + V. Después, Enter.

---

## Camino A · Con conda

### A1. Activar el entorno

```bash
conda activate viernes-vscode
```

Al inicio de la línea debe aparecer **`(viernes-vscode)`**. Si no aparece, el entorno no está activo y lo que sigue no sirve.

### A2. Comprobar que `ipykernel` está instalado

```bash
python -c "import ipykernel; print('ipykernel', ipykernel.__version__)"
```

- Si imprime `ipykernel` y un número: sigue al paso A3.
- Si dice `ModuleNotFoundError`: instálalo y repite la comprobación.

```bash
conda install -y ipykernel
```

### A3. Crear el kernel

```bash
python -m ipykernel install --user --name viernes-vscode --display-name "Python (viernes-vscode)"
```

**Debes ver:** `Installed kernelspec viernes-vscode in ...`

Qué significa cada parte, por si quieres adaptarlo:

| Parte | Para qué sirve |
| --- | --- |
| `python -m ipykernel install` | Pide a **este** Python (el del entorno activo) que se registre como kernel |
| `--user` | Lo registra solo para tu usuario; no necesita permisos de administrador |
| `--name viernes-vscode` | Nombre interno, sin espacios ni acentos |
| `--display-name "Python (viernes-vscode)"` | El nombre que verás en VS Code |

Sigue en [Comprobar que quedó bien](#comprobar-que-quedó-bien).

---

## Camino B · Sin conda (entorno virtual)

Un *entorno virtual* es una carpeta con su propio Python y sus propias bibliotecas, aislada del resto de tu computadora. Viene con Python, no necesitas instalar nada extra (en Linux, a veces sí: ver *Problemas comunes*).

### B1. Revisar que tienes Python

| Sistema | Comando |
| --- | --- |
| Windows | `python --version` |
| macOS y Linux | `python3 --version` |

Debe responder `Python 3.10` o más nuevo. Si en Windows dice que `python` no se reconoce, prueba `py --version`; si funciona, usa `py` en lugar de `python` solo en el comando de B3.

### B2. Entrar a la carpeta de trabajo

Elige una carpeta **con ruta corta, sin acentos ni espacios** (por ejemplo `C:\clases` en Windows, `~/clases` en macOS y Linux) y entra a ella:

```bash
cd ~/clases           # macOS y Linux
cd C:\clases          # Windows (cmd)
cd /c/clases          # Windows (Git Bash)
```

Si la carpeta no existe, créala antes: `mkdir clases`.

### B3. Crear el entorno virtual

| Sistema | Comando |
| --- | --- |
| Windows | `python -m venv .venv` |
| macOS y Linux | `python3 -m venv .venv` |

Tarda unos segundos y no imprime nada. Crea una carpeta oculta llamada `.venv`.

### B4. Activarlo

| Sistema y terminal | Comando |
| --- | --- |
| Windows, Símbolo del sistema (`cmd`) | `.venv\Scripts\activate` |
| Windows, PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows, Git Bash | `source .venv/Scripts/activate` |
| macOS y Linux | `source .venv/bin/activate` |

Al inicio de la línea debe aparecer **`(.venv)`**. Si no aparece, no se activó: sigue sin continuar.

### B5. Instalar las bibliotecas

```bash
python -m pip install --upgrade pip
python -m pip install ipykernel pandas matplotlib
```

Tarda uno o dos minutos. `pandas` trae `numpy` por su cuenta. Estas versiones de `pip` no dependen de Qt ni de bibliotecas que choquen entre sí.

> En macOS y Linux, con el entorno activado, `python` ya apunta al del entorno: **no** uses `python3` desde aquí.

### B6. Crear el kernel

```bash
python -m ipykernel install --user --name viernes-vscode --display-name "Python (viernes-vscode)"
```

**Debes ver:** `Installed kernelspec viernes-vscode in ...`

---

## Comprobar que quedó bien

Con el entorno activado (el `(viernes-vscode)` o `(.venv)` al inicio de la línea):

```bash
jupyter kernelspec list
```

Debes ver una línea con **`viernes-vscode`** y una ruta.

### Usarlo en VS Code

1. Abre un archivo `.ipynb`.
2. Arriba a la derecha, clic en **Select Kernel**.
3. Elige **Jupyter Kernel…** y después **Python (viernes-vscode)**.
4. Si no aparece: pulsa el botón de refrescar (↻) de esa lista. Si sigue sin aparecer, **Ctrl + Shift + P** (macOS: Cmd + Shift + P), escribe `Reload Window` y pulsa Enter.

> **Atajo:** VS Code también muestra los entornos que tiene `ipykernel` instalado en **Select Kernel → Python Environments…**, sin necesidad de haber ejecutado el paso del kernel. Si te aparece ahí `viernes-vscode` o `.venv`, puedes elegirlo directamente.

### Prueba final

En la primera celda del notebook, escribe y ejecuta con **Shift + Enter**:

```python
import sys
print(sys.executable)
```

La ruta debe contener **`viernes-vscode`** (Camino A) o **`.venv`** (Camino B). Después, para comprobar que no se cae al graficar:

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
| `ModuleNotFoundError: No module named 'ipykernel'` | Lo ejecutaste fuera del entorno, o falta instalarlo | Activa el entorno (el `(viernes-vscode)` o `(.venv)` debe verse) y repite el paso de instalación |
| El kernel no aparece en **Select Kernel** | VS Code no ha vuelto a leer la lista | Botón ↻ de la lista, o `Reload Window`. Comprueba con `jupyter kernelspec list` que existe |
| Aparece, pero la ruta de `sys.executable` es de otro Python | Lo creaste con otro entorno activo | Bórralo (ver abajo), activa el entorno correcto y repite el paso de crear el kernel |
| Windows, PowerShell: *«la ejecución de scripts está deshabilitada en este sistema»* | PowerShell bloquea `Activate.ps1` | Usa el **Símbolo del sistema** o **Git Bash** (comandos de B4), que no tienen ese bloqueo |
| Windows: `python` no se reconoce, o abre la Microsoft Store | Python no está en el PATH, o la tienda intercepta el comando | Prueba `py` en lugar de `python`. Si tampoco, instala Python desde python.org marcando **Add python.exe to PATH** |
| Windows: el nombre de usuario tiene acento o espacio (por ejemplo `Miguel Díaz`) y falla el registro | Rutas con caracteres especiales | Usa `--sys-prefix` en lugar de `--user` (el kernel se guarda dentro del entorno), o crea el entorno en una ruta corta como `C:\clases` |
| Linux: `The virtual environment was not created successfully because ensurepip is not available` | Falta el paquete de entornos virtuales | `sudo apt install python3-venv` (Ubuntu, Linux Mint, Debian) y repite B3 |
| macOS: `command not found: python` | En macOS el comando se llama `python3` | Usa `python3` solo para el comando de B3. Con el entorno activado, `python` ya funciona |
| macOS/Linux: `error: externally-managed-environment` | Estás instalando con el Python del sistema, no con el entorno | Activa el entorno (B4) y repite; el `(.venv)` debe verse |
| **Windows + conda:** el kernel se cierra («The Kernel crashed») al importar pandas o graficar | Un motor matemático (MKL) incompatible con otra biblioteca | Con el entorno activado: `conda install -n viernes-vscode "libblas=*=*openblas"`, reinicia el kernel con **Restart**. Si no funciona, usa el **Camino B** |

### Borrar el kernel y empezar de nuevo

```bash
jupyter kernelspec remove viernes-vscode -f
```

Después repite el paso de crear el kernel con el entorno correcto activado. Esto **no** borra el entorno ni tus archivos: solo quita el registro del kernel.

---

## Lista de verificación

- [ ] Veo `(viernes-vscode)` o `(.venv)` al inicio de la línea de la terminal
- [ ] `python -c "import ipykernel"` no da error
- [ ] El comando de crear el kernel respondió `Installed kernelspec viernes-vscode`
- [ ] `jupyter kernelspec list` muestra `viernes-vscode`
- [ ] En VS Code, **Select Kernel** muestra **Python (viernes-vscode)**
- [ ] La prueba final imprime una ruta con `viernes-vscode` o `.venv`, y el gráfico aparece sin cerrarse el kernel
