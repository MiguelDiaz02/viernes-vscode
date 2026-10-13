# Mis primeros pasos con conda

Instalar Python y crear el entorno de la clase desde cero. Para **Windows, macOS y Linux** (Ubuntu, Linux Mint y similares).

Tiempo: de 15 a 25 minutos, casi todo esperando. **Una sola vez.** Hazlo antes del 30 de octubre.

Si nunca has usado la terminal, lee primero la **Parte 0** de [Mis primeros pasos en GitHub](../primeros-pasos-github/README.md#parte-0--la-terminal-en-5-minutos). Son 5 minutos y explica cómo abrirla y cómo pegar comandos.

---

## ¿Qué vamos a hacer?

Un análisis de datos depende de la versión exacta de Python y de sus paquetes (pandas, numpy, matplotlib). Si tú tienes una versión y yo otra, el mismo código funciona en una computadora y falla en la otra.

Un **entorno de conda** es una caja cerrada con las versiones exactas. **Miniforge** es el programa que crea esas cajas. La caja de esta clase se llama `viernes-vscode`.

Son cinco pasos:

1. Instalar Miniforge
2. Entrar a la carpeta del repositorio
3. Crear el entorno
4. Comprobar que quedó bien
5. Usarlo en VS Code

**Necesitas:** conexión a internet, unos 3 GB libres en disco y haber descargado el repositorio (Parte 3 de la guía de GitHub). **No necesitas** permisos de administrador.

**¿Ya tienes Anaconda, Miniconda o Miniforge?** Escribe `conda --version` en la terminal. Si responde con un número, salta al [Paso 2](#paso-2--entrar-a-la-carpeta-del-repositorio).

### Qué terminal usar

| Sistema | Terminal |
| --- | --- |
| **Windows** | **Miniforge Prompt** (aparece en el menú Inicio *después* de instalar Miniforge). No uses PowerShell para los comandos de conda. |
| **macOS** | Terminal |
| **Linux** | Terminal (Ctrl + Alt + T) |

---

## Paso 1 · Instalar Miniforge

<details>
<summary><b>Windows</b></summary>

1. Descarga el instalador: [Miniforge3-Windows-x86_64.exe](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) (unos 100 MB).
2. Haz doble clic en el archivo. Si Windows muestra *«Windows protegió tu PC»*, pulsa **Más información → Ejecutar de todas formas**. Si más adelante el instalador no te deja instalar en `C:\miniforge3`, vuelve a abrirlo con **clic derecho → Ejecutar como administrador**.
3. En el instalador:
   - **Next** → **I Agree**.
   - *Install for:* deja **Just Me**.
   - *Destination Folder:* borra lo que aparece y escribe `C:\miniforge3`. Una ruta corta, sin acentos ni espacios, evita varios problemas de Windows. Si el instalador no te deja usar esa ruta, ciérralo y ábrelo otra vez con **clic derecho → Ejecutar como administrador**.
   - *Advanced Installation Options:* deja marcada **solo** *Create shortcuts* (es la que crea el «Miniforge Prompt» en el menú Inicio). **No marques** *Add installation to my PATH* (el propio instalador dice que no se recomienda) ni *Register Miniforge3 as my default Python*: este último haría que VS Code y otros programas usen ese Python, que es demasiado nuevo para esta clase. *Clear the package cache* da igual; déjala como viene.
   - **Install**, espera unos minutos, **Next** y **Finish**.
4. Abre el menú Inicio, escribe **Miniforge Prompt** y ábrelo. Es una ventana negra. **Usa siempre esta ventana para los comandos de conda.**

Comprueba:

```bash
conda --version
```

**Debes ver:** `conda` seguido de un número, por ejemplo `conda 26.7.2`.

</details>

<details>
<summary><b>macOS</b></summary>

Abre Terminal y pega estas tres líneas, **una por una**. Funcionan igual en Macs con chip Apple (M1 a M4) y en Macs Intel: el comando detecta cuál tienes.

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
```

Descarga el instalador a tu carpeta personal (unos 100 MB). **Debes ver** una barra de progreso que llega a 100%.

```bash
bash "Miniforge3-$(uname)-$(uname -m).sh" -b
```

Lo instala en `~/miniforge3` y acepta la licencia (de código abierto). Tarda uno o dos minutos. **Debes ver** que termina con `installation finished.`

```bash
~/miniforge3/bin/conda init --all
```

Le enseña a tu terminal a usar conda. **Debes ver** varias líneas que dicen `modified` o `no change`.

Ahora **cierra la terminal por completo (Cmd + Q) y ábrela de nuevo.** Esto es indispensable.

**Debes ver** `(base)` al principio de la línea de la terminal. Comprueba:

```bash
conda --version
```

**Debes ver:** `conda` seguido de un número.

Cuando quieras, borra el instalador: `rm Miniforge3-*.sh`

</details>

<details>
<summary><b>Linux (Ubuntu, Linux Mint, Debian)</b></summary>

Abre la terminal (Ctrl + Alt + T) y pega estas tres líneas, **una por una**. Pega con **Ctrl + Shift + V**.

```bash
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
```

Descarga el instalador (unos 100 MB). **Debes ver** una barra que llega a 100%. Si dice `wget: command not found`, instálalo con `sudo apt install -y wget` y repite.

```bash
bash "Miniforge3-$(uname)-$(uname -m).sh" -b
```

Lo instala en `~/miniforge3` y acepta la licencia (de código abierto). Tarda uno o dos minutos. **Debes ver** que termina con `installation finished.`

```bash
~/miniforge3/bin/conda init --all
```

Le enseña a tu terminal a usar conda. **Debes ver** varias líneas que dicen `modified` o `no change`.

Ahora **cierra la terminal por completo y ábrela de nuevo.** Esto es indispensable.

**Debes ver** `(base)` al principio de la línea de la terminal. Comprueba:

```bash
conda --version
```

**Debes ver:** `conda` seguido de un número.

Cuando quieras, borra el instalador: `rm Miniforge3-*.sh`

</details>

---

## Paso 2 · Entrar a la carpeta del repositorio

Todos los comandos siguientes se ejecutan **desde dentro de la carpeta del repositorio**.

**Windows** (Miniforge Prompt):

```bash
cd clases\viernes-vscode
```

**macOS y Linux:**

```bash
cd clases/viernes-vscode
```

Si descargaste el repositorio como ZIP, la carpeta se llama `viernes-vscode-main` y puede estar en *Descargas*. Entra a donde esté.

Comprueba que estás en el lugar correcto: escribe `dir` (Windows) o `ls` (macOS y Linux). **Debes ver** la carpeta `primeros-pasos-conda`, entre otras.

En el Miniforge Prompt de Windows no existen `ls` ni `pwd`. La carpeta en la que estás aparece escrita antes del signo `>`; también puedes escribir `cd` solo para verla.

Si la carpeta está en otra unidad (por ejemplo `D:`), usa `cd /d "ruta"`. Para copiar la ruta: Shift + clic derecho sobre la carpeta en el Explorador → *Copiar como ruta*, y pégala después de `cd /d `.

---

## Paso 3 · Crear el entorno

**Solo en Windows, antes de crear el entorno** (una sola línea, para todos):

```bash
conda config --add envs_dirs C:\Users\Public\conda-envs
```

Le dice a conda que guarde el entorno en una carpeta sin acentos ni espacios. Si tu nombre de usuario tiene acentos, ñ o espacios (por ejemplo `Miguel Díaz`), sin este paso el entorno se crea pero falla al activarlo. Si no los tiene, no estorba. Hazlo todos, así no tienes que adivinar. No imprime nada: es normal.

Ahora sí, en todos los sistemas:

```bash
conda env create -f primeros-pasos-conda/environment.yml
```

Esto descarga e instala Python, pandas, numpy, matplotlib y otros paquetes. Tarda de 2 a 10 minutos según tu internet. Puede parecer que se quedó congelado en *Solving environment*: **es normal, espera.**

Durante la instalación puede aparecer un aviso largo que empieza con `WARNING conda.conda_pypi... Did you know?`. Es solo informativo: ignóralo.

**Debes ver**, al final, algo como:

```
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate viernes-vscode
```

Actívalo:

```bash
conda activate viernes-vscode
```

**Debes ver** que el inicio de la línea cambia de `(base)` a `(viernes-vscode)`. Así sabes que estás dentro de la caja.

**En Windows**, esa línea no debe ir acompañada de ningún `ERROR: Activation script ... failed`. Si sale, ve a [Problemas comunes](#problemas-comunes).

**En Windows**, comprueba además dónde quedó el entorno:

```bash
conda env list
```

**Debes ver** una línea `viernes-vscode` con la ruta `C:\Users\Public\conda-envs\viernes-vscode`. Si la ruta está dentro de tu carpeta de usuario (por ejemplo `C:\Users\...\.conda\envs`), te saltaste el comando de arriba: ve a [Problemas comunes](#problemas-comunes).

Registra el entorno para usarlo en notebooks:

```bash
python -m ipykernel install --user --name viernes-vscode --display-name "Python (viernes-vscode)"
```

**Debes ver:** `Installed kernelspec viernes-vscode in ...`

---

## Paso 4 · Comprobar que todo quedó bien

```bash
python primeros-pasos-conda/verificar_instalacion.py
```

**Debes ver** una lista con `[OK]` en cada línea y, al final:

```
Todo listo. Nos vemos en la clase.
```

Si aparece algún `[FALTA]`, justo debajo hay una flecha `->` con lo que debes hacer. Si no se resuelve, mándale a Miguel una captura de pantalla de **todo** el resultado.

Un `[AVISO]` no es un problema; solo te informa algo.

---

## Paso 5 · Usarlo en VS Code

1. Abre VS Code → **Archivo → Abrir carpeta** (en macOS: **File → Open Folder**) → elige `clases/viernes-vscode`.
2. Si aparece un aviso abajo a la derecha con **extensiones recomendadas**, pulsa **Instalar**.
3. Abre cualquier archivo `.py` dentro de `scripts/`. Abajo a la derecha, en la barra de estado, haz clic en la versión de Python y elige **viernes-vscode**.
4. En un notebook (`.ipynb`), arriba a la derecha pulsa **Select Kernel** y elige **Python (viernes-vscode)**.

**Importante:**

- Si VS Code ofrece **descargar otro Python** o **instalar Docker**, di que no. No hace falta.
- Si no aparece `viernes-vscode` en la lista, cierra y abre VS Code. Si sigue sin aparecer, mira [Problemas comunes](#problemas-comunes).

---

## Cada vez que uses el entorno

Abre la terminal (en Windows, **Miniforge Prompt**) y escribe:

```bash
conda activate viernes-vscode
```

Para salir de la caja:

```bash
conda deactivate
```

Para ver todos tus entornos:

```bash
conda env list
```

---

## Si no puedes instalar nada: Codespaces

<details>
<summary><b>GitHub Codespaces: VS Code en el navegador, con todo ya instalado</b></summary>

Para quien no puede instalar programas en su computadora, o como rescate el día de la clase. Necesitas una cuenta de GitHub; las cuentas personales incluyen horas gratuitas cada mes.

1. Entra a [github.com/MiguelDiaz02/viernes-vscode](https://github.com/MiguelDiaz02/viernes-vscode).
2. Botón verde **Code** → pestaña **Codespaces** → **Create codespace on main**.
3. Espera un par de minutos. Se abre VS Code en el navegador con Python, los paquetes, las extensiones y el kernel ya instalados.

Todo lo de la clase funciona igual ahí. Al terminar, borra el codespace desde [github.com/codespaces](https://github.com/codespaces) para no gastar horas gratuitas.

</details>

---

## Problemas comunes

| Qué ves | Qué pasó | Qué hacer |
| --- | --- | --- |
| `conda` no se reconoce como comando (**Windows**) | Estás en PowerShell o en el Símbolo del sistema normal | Abre **Miniforge Prompt** desde el menú Inicio |
| `conda: command not found` (**macOS, Linux**) | La terminal se abrió antes de instalar, o falta `conda init` | Cierra **toda** la terminal y abre otra. Si sigue: `~/miniforge3/bin/conda init --all` y abre otra terminal |
| `EnvironmentFileNotFound`, `No such file` o `File not found` | No estás en la carpeta del repositorio | Usa `cd` (Paso 2) y confirma con `dir` o `ls` que ves `primeros-pasos-conda` |
| `prefix already exists` | Ya habías creado el entorno | Actívalo: `conda activate viernes-vscode`. Para empezar de cero: `conda env remove -n viernes-vscode` y repite el Paso 3 |
| Se queda en *Solving environment* más de 15 minutos, o `CondaHTTPError`, `SSLError`, `ProxyError` | Internet lento, o una red con firewall (escuela, laboratorio) | Prueba con otra red o con los datos del celular. Como salida, usa Codespaces |
| `No space left on device` | Disco lleno | Libera unos 3 GB y repite |
| **Windows:** al activar el entorno sale `ERROR: Activation script ... libxml2-split_activate.bat failed`, la ruta tiene caracteres raros (como `D¦+az`) o `python` no se reconoce justo después | El entorno quedó dentro de tu carpeta de usuario, que tiene acentos, ñ o espacios | Cierra el Miniforge Prompt y abre uno nuevo. Luego: `conda env remove -n viernes-vscode -y`, `conda config --add envs_dirs C:\Users\Public\conda-envs` y repite el Paso 3 desde `conda env create` |
| `ModuleNotFoundError: No module named 'pandas'` al correr un script | VS Code está usando otro Python | Barra inferior derecha → elige `viernes-vscode` |
| `viernes-vscode` no aparece en VS Code | VS Code todavía no lo detecta | Cierra y abre VS Code. Si sigue: **Ctrl + Shift + P** → *Python: Select Interpreter* → *Enter interpreter path* y pega la ruta de abajo |
| El kernel del notebook se cae («The Kernel crashed») | Entorno creado con una versión vieja de esta guía, que instalaba Qt | Recréalo (ver abajo) |
| El verificador marca `[FALTA]` en `matplotlib` o en el backend Qt | Mismo caso | Recréalo (ver abajo) |
| El kernel se cae justo al graficar y el verificador marca `[FALTA]` en «álgebra lineal» (**Windows**) | Una librería matemática (MKL) del entorno es incompatible con otra | Con el entorno activado: `conda install -n viernes-vscode "libblas=*=*openblas"` (responde `y`), reinicia el kernel en VS Code (botón **Restart**) y corre el verificador otra vez |
| Cualquier otra cosa | | Mándale a g5diazcamposmiguel@gmail.com una captura de pantalla de la terminal completa |

**Rutas del intérprete** (para el caso de *Enter interpreter path*). En macOS y Linux cambia `tu_usuario`:

| Sistema | Ruta |
| --- | --- |
| Windows | `C:\Users\Public\conda-envs\viernes-vscode\python.exe` |
| macOS | `/Users/tu_usuario/miniforge3/envs/viernes-vscode/bin/python` |
| Linux | `/home/tu_usuario/miniforge3/envs/viernes-vscode/bin/python` |

**Recrear el entorno desde cero** (2 minutos), desde la carpeta del repositorio:

```bash
conda deactivate
conda env remove -n viernes-vscode
conda env create -f primeros-pasos-conda/environment.yml
conda activate viernes-vscode
python -m ipykernel install --user --name viernes-vscode --display-name "Python (viernes-vscode)"
python primeros-pasos-conda/verificar_instalacion.py
```

Luego cierra y abre VS Code.

---

## Cuando termine el curso: desinstalar

Si ya no quieres el entorno (los comandos van en este orden):

```bash
conda activate viernes-vscode
jupyter kernelspec remove viernes-vscode -f
conda deactivate
conda env remove -n viernes-vscode
```

Si además quieres quitar Miniforge:

- **Windows:** *Configuración → Aplicaciones* → busca *Miniforge3* → **Desinstalar**.
- **macOS y Linux:** `conda init --reverse --all`, luego `rm -rf ~/miniforge3`, y abre otra terminal.

---

## Lista final: ¿quedó todo?

- [ ] `conda --version` responde con un número
- [ ] `conda activate viernes-vscode` hace que aparezca `(viernes-vscode)`
- [ ] `python primeros-pasos-conda/verificar_instalacion.py` termina con **Todo listo**
- [ ] En VS Code, un archivo `.py` de `scripts/` muestra **viernes-vscode** abajo a la derecha
