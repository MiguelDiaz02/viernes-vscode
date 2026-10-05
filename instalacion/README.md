# Instalación del entorno

Esto se hace **una sola vez**, antes de la clase. Tarda entre 5 y 10 minutos.
Al final vas a tener un entorno de Python llamado `viernes-vscode` con todo lo necesario,
y un kernel con el mismo nombre para usar notebooks.

> **Hazlo antes del 30 de octubre.** Si algo falla, escríbeme con una captura de pantalla
> del error y lo resolvemos antes de la sesión. Instalar durante la clase es la forma más
> segura de perderse la primera media hora.

## Elige tu ruta

| Tu situación | Ruta | Tiempo |
| --- | --- | --- |
| No sé si tengo conda, o nunca he instalado Python | **A · Miniforge** (recomendada) | 10 min |
| Ya tengo Anaconda, Miniconda o Miniforge | **A · solo los pasos 2 a 5** | 5 min |
| Ya tengo Python y prefiero pip | **B · venv** | 5 min |
| No puedo instalar nada en mi computadora | **C · Codespaces** (en el navegador) | 2 min |

¿No sabes si tienes conda? Abre una terminal (ver abajo) y escribe `conda --version`.
Si responde con un número, ya lo tienes. Si dice «no se reconoce» o «command not found», no.

### Cómo abrir una terminal

- **Windows:** después de instalar Miniforge, busca **Miniforge Prompt** en el menú Inicio. Usa esa, no la de Windows normal.
- **macOS:** Cmd+Espacio, escribe **Terminal**, Enter.
- **Linux:** Ctrl+Alt+T en la mayoría de las distribuciones.
- **Dentro de VS Code:** Ctrl+ñ (o Ctrl+`). Sirve para todo lo de abajo una vez que conda está instalado.

---

## Ruta A · Miniforge y conda (recomendada)

### 1. Instalar Miniforge

Miniforge es conda ya configurado con conda-forge, el canal que usa casi toda la
comunidad de bioinformática. Si ya tienes Anaconda o Miniconda, **salta al paso 2**.

**Windows:** descarga el instalador `Miniforge3-Windows-x86_64.exe` desde
[github.com/conda-forge/miniforge](https://github.com/conda-forge/miniforge#download)
y ejecútalo. Acepta las opciones por defecto.

**macOS y Linux:** copia y pega en la terminal:

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```

Responde `yes` a todo. Al final **cierra la terminal y abre una nueva** para que reconozca `conda`.

### 2. Ir a la carpeta del repositorio

Si clonaste o descomprimiste el repositorio en Descargas:

```bash
cd ~/Downloads/viernes-vscode
```

En Windows:

```bash
cd %USERPROFILE%\Downloads\viernes-vscode
```

> Si lo descargaste como ZIP desde GitHub, la carpeta se llama `viernes-vscode-main`.
> Ajusta el nombre en el comando.

Para confirmar que estás en el lugar correcto, escribe `ls` (o `dir` en Windows):
deberías ver `README.md`, `data`, `scripts` e `instalacion`.

### 3. Crear el entorno

```bash
conda env create -f instalacion/environment.yml
```

Va a descargar paquetes durante unos minutos. Cuando termine, actívalo:

```bash
conda activate viernes-vscode
```

El inicio de la línea de la terminal ahora dice `(viernes-vscode)`. Así sabes que está activo.

### 4. Registrar el kernel para notebooks

```bash
python -m ipykernel install --user --name viernes-vscode --display-name "Python (viernes-vscode)"
```

VS Code encuentra el entorno aunque no hagas esto, pero así aparece con un nombre claro en
el selector de kernel de los notebooks, y también funciona en Jupyter fuera de VS Code.

### 5. Comprobar

```bash
python instalacion/verificar_instalacion.py
```

Si la última línea dice **Todo listo**, terminaste. Si aparece algún `[FALTA]`,
sigue la flecha que viene debajo.

---

## Ruta B · venv y pip (si ya tienes Python)

Necesitas Python 3.10 o más reciente. Compruébalo con `python --version`
(en macOS y Linux puede ser `python3 --version`).

Desde la carpeta del repositorio:

**macOS y Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r instalacion/requirements.txt
python -m ipykernel install --user --name viernes-vscode --display-name "Python (viernes-vscode)"
python instalacion/verificar_instalacion.py
```

**Windows (símbolo del sistema):**

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r instalacion\requirements.txt
python -m ipykernel install --user --name viernes-vscode --display-name "Python (viernes-vscode)"
python instalacion\verificar_instalacion.py
```

La carpeta `.venv` queda dentro del repositorio y Git la ignora. VS Code la detecta sola.

---

## Ruta C · GitHub Codespaces (sin instalar nada)

Para quien no puede instalar programas en su computadora, o para rescatarse si algo
falla el día de la clase. Necesitas una cuenta de GitHub; las cuentas personales
incluyen horas gratuitas cada mes.

1. Entra a [github.com/MiguelDiaz02/viernes-vscode](https://github.com/MiguelDiaz02/viernes-vscode).
2. Botón verde **Code** → pestaña **Codespaces** → **Create codespace on main**.
3. Espera un par de minutos. Se abre VS Code en el navegador con Python, los paquetes,
   las extensiones y el kernel ya instalados.

Todo lo de la clase funciona igual ahí, salvo la conexión por SSH a un servidor.
Cuando termines, borra el codespace desde [github.com/codespaces](https://github.com/codespaces)
para no gastar horas.

---

## Usar el entorno en VS Code

1. Abre la carpeta del repositorio: **Archivo → Abrir carpeta** → `viernes-vscode`.
2. Si aparece un aviso de **extensiones recomendadas** abajo a la derecha, pulsa **Instalar**.
3. Abre cualquier archivo `.py` de `scripts/`.
4. Abajo a la derecha, en la barra de estado, haz clic en la versión de Python y elige
   **viernes-vscode** (o `.venv` si usaste la ruta B).
5. En los notebooks (`.ipynb`), arriba a la derecha, **Select Kernel** → **Python (viernes-vscode)**.

---

## Problemas comunes

**`conda` no se reconoce como un comando.**
En Windows, usa **Miniforge Prompt**, no la terminal normal. En macOS y Linux, cierra
y vuelve a abrir la terminal después de instalar. Si sigue sin funcionar:
`~/miniforge3/bin/conda init` y abre otra terminal.

**`EnvironmentFileNotFound` o «No such file».**
No estás en la carpeta del repositorio. Usa `cd` para entrar a `viernes-vscode` y
confirma con `ls` (o `dir`) que ves la carpeta `instalacion`.

**El entorno ya existe** (`prefix already exists`).
Ya lo creaste antes. Actívalo con `conda activate viernes-vscode` y sigue al paso 4.
Si quieres empezar de cero: `conda env remove -n viernes-vscode` y repite el paso 3.

**`ModuleNotFoundError: No module named 'pandas'` al correr un script en VS Code.**
VS Code está usando otro Python. Mira abajo a la derecha y elige `viernes-vscode`.
Es el error más común de la clase, y lo vamos a ver en vivo.

**PowerShell dice que la ejecución de scripts está deshabilitada** (ruta B en Windows).
Usa el **símbolo del sistema** (cmd) en lugar de PowerShell, o ejecuta una vez:
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

**El kernel no aparece en el notebook.**
Repite el paso 4 con el entorno activado y reinicia VS Code.

**La instalación se queda congelada mucho tiempo.**
Una red lenta puede tardar más de 10 minutos. Si pasan 20, cancela con Ctrl+C y prueba
la ruta B, que descarga menos.

---

## Al terminar el curso

Para borrar todo lo que instalaste:

```bash
conda activate viernes-vscode
jupyter kernelspec remove viernes-vscode
conda deactivate
conda env remove -n viernes-vscode
```

En ese orden: el primer comando vive dentro del entorno, así que hay que quitar el kernel
antes de borrar el entorno. En la ruta B, quita el kernel igual y luego borra la carpeta `.venv`.
