# Mis primeros pasos en GitHub

La terminal, Git y GitHub desde cero. Para **Windows, macOS y Linux** (Ubuntu, Linux Mint y similares).

Tiempo: de 20 a 30 minutos, **una sola vez**. Hazlo antes del 30 de octubre.

No necesitas saber nada. Solo copiar, pegar y comparar lo que ves con lo que dice esta guía.

---

## Antes de empezar

Necesitas dos cosas que se explican en la **guía ilustrada** que te compartió Miguel:

1. **VS Code** instalado. Si no lo tienes: [code.visualstudio.com](https://code.visualstudio.com/).
2. Una **cuenta de GitHub** (gratis). Si no la tienes: [github.com/signup](https://github.com/signup).

La cuenta es opcional para seguir la clase. Sin cuenta puedes hacer todo menos subir tus cambios a internet.

**Cómo leer esta guía**

- Los recuadros grises son **comandos**. Se copian y se pegan tal cual, sin cambiar nada.
- Debajo de cada comando dice **Debes ver** lo que tiene que aparecer. Si lo ves, sigue. Si no, ve a [Problemas comunes](#problemas-comunes).
- Donde hay una versión para cada sistema operativo, **abre solo la tuya**.
- Equivocarte no rompe nada. Lo peor que puede pasar es que un comando diga que falló, y se repite.

---

## Parte 0 · La terminal en 5 minutos

### ¿Qué es?

Una ventana donde le das órdenes a tu computadora escribiendo texto, en lugar de hacer clic. VS Code trae una, pero para estos primeros pasos usamos la del sistema.

### Cómo abrirla

| Sistema | Cómo |
| --- | --- |
| **Windows** | Presiona la tecla **Windows**, escribe `PowerShell` y presiona Enter. Se abre una ventana azul. |
| **macOS** | Presiona **Cmd + Espacio**, escribe `Terminal` y presiona Enter. |
| **Linux** (Ubuntu, Mint) | Presiona **Ctrl + Alt + T**. Si no funciona: abre el menú de aplicaciones y busca **Terminal**. |

### Cómo ejecutar un comando

1. Copia el comando de esta guía.
2. Pégalo en la terminal:
   - **Windows:** clic derecho dentro de la ventana, o **Ctrl + V**.
   - **macOS:** **Cmd + V**.
   - **Linux:** **Ctrl + Shift + V**. Ojo: aquí **no** es Ctrl + V.
3. Presiona **Enter**. Nada ocurre hasta que presionas Enter.

El texto que aparece antes del cursor (por ejemplo `PS C:\Users\ana>` o `ana@laptop:~$`) se llama *prompt*. Es de la terminal. **No lo copies ni lo escribas.**

### Los cinco comandos que vas a necesitar

| Qué quieres | Windows (PowerShell) | macOS y Linux |
| --- | --- | --- |
| Saber en qué carpeta estás | `pwd` | `pwd` |
| Ver qué hay en esa carpeta | `dir` | `ls` |
| Entrar a una carpeta | `cd nombre` | `cd nombre` |
| Salir a la carpeta anterior | `cd ..` | `cd ..` |
| Crear una carpeta | `mkdir nombre` | `mkdir nombre` |

> **Ojo con el Miniforge Prompt.** Más adelante usarás una ventana llamada *Miniforge Prompt*. Es el Símbolo del sistema de Windows (cmd), no PowerShell. Ahí `ls` y `pwd` **no existen**: usa `dir` para ver qué hay y `cd` (solo, sin nada más) para saber en qué carpeta estás. `mkdir`, `cd nombre` y `cd ..` funcionan igual.

### Cuatro trucos que te ahorran la mitad de los errores

- La tecla **Tab** completa los nombres. Escribe `cd cla`, presiona Tab y aparece `clases`.
- La **flecha hacia arriba** trae el último comando.
- **Ctrl + C** cancela lo que esté corriendo.
- Cuando escribas una contraseña en la terminal (Linux y macOS), **no se ve nada**, ni asteriscos. Es normal. Escríbela completa y presiona Enter.

---

## Parte 1 · Instalar Git

**Git** es el programa que guarda el historial de cambios de un proyecto. **GitHub** es la página web donde se guardan esos proyectos. Primero instalamos Git.

### ¿Ya lo tienes?

Pega esto en la terminal:

```bash
git --version
```

Si ves algo como `git version 2.43.0` (cualquier número), **ya lo tienes: salta a la Parte 2**.

Si dice que no se reconoce o que no se encuentra, instálalo:

<details>
<summary><b>Windows</b></summary>

**Opción A (la más fácil).** En PowerShell:

```bash
winget install --id Git.Git -e --source winget --accept-package-agreements --accept-source-agreements
```

Espera a que termine. **Cierra PowerShell y ábrelo de nuevo.**

Si dice que `winget` no se reconoce, usa la opción B.

**Opción B (instalador).**

1. Entra a [git-scm.com/downloads](https://git-scm.com/downloads) y descarga la versión para Windows (Git for Windows Setup).
2. Abre el archivo descargado. Si Windows pregunta si permites cambios, di que sí.
3. Presiona **Next** en todas las pantallas. Solo una importa: en *Choosing the default editor used by Git*, elige **Visual Studio Code** si aparece en la lista. Así evitas que Git abra un editor llamado Vim, que es muy difícil de cerrar.
4. Al terminar, **cierra PowerShell y ábrelo de nuevo**.

</details>

<details>
<summary><b>macOS</b></summary>

Pega en Terminal:

```bash
git --version
```

Si Git no está, macOS abre una ventana que ofrece instalar las **herramientas de línea de comandos**. Pulsa **Instalar**, acepta la licencia y espera de 5 a 15 minutos.

Si la ventana no aparece, pega:

```bash
xcode-select --install
```

Cuando termine, cierra la terminal, ábrela de nuevo y repite `git --version`.

</details>

<details>
<summary><b>Linux (Ubuntu, Linux Mint, Debian)</b></summary>

```bash
sudo apt update
sudo apt install -y git
```

`sudo` significa «hazlo como administrador» y te pide tu contraseña. Recuerda: al escribirla no se ve nada. Escríbela y presiona Enter.

Otras distribuciones: Fedora `sudo dnf install -y git`, Arch `sudo pacman -S git`.

</details>

### Comprueba

```bash
git --version
```

**Debes ver:** `git version` seguido de un número.

---

## Parte 2 · Decirle a Git quién eres

Git firma cada cambio que guardas con tu nombre y tu correo. Sin esto, tu primer *commit* (guardado de cambios) falla con el mensaje `Please tell me who you are` o `Author identity unknown`.

Se hace **una sola vez** en cada computadora. Pega estos tres comandos, uno por uno, **cambiando solo el texto entre comillas**:

```bash
git config --global user.name "Tu Nombre Completo"
git config --global user.email "tu_correo@ejemplo.com"
git config --global init.defaultBranch main
```

- Conserva las comillas.
- Usa el **mismo correo con el que creaste tu cuenta de GitHub**. Así tus cambios aparecen ligados a tu perfil.
- Si no quieres mostrar tu correo, en GitHub ve a *Settings → Emails*, activa *Keep my email addresses private* y usa el correo `...@users.noreply.github.com` que te muestra ahí.

### Comprueba

```bash
git config --global --list
```

**Debes ver** líneas con tu nombre y tu correo:

```
user.name=Tu Nombre Completo
user.email=tu_correo@ejemplo.com
init.defaultbranch=main
```

Si aparece una lista larga que termina en `(END)` o con dos puntos `:`, presiona **q** para salir.

---

## Parte 3 · Descargar el repositorio de la clase

Un **repositorio** es una carpeta de proyecto con todo su historial. **Clonar** es copiarlo completo a tu computadora. Para clonar un repositorio público **no necesitas cuenta ni contraseña**.

Pega estos cuatro comandos, uno por uno. Son **iguales en Windows, macOS y Linux**:

```bash
mkdir clases
cd clases
git clone https://github.com/MiguelDiaz02/viernes-vscode.git
cd viernes-vscode
```

Qué hace cada uno:

1. `mkdir clases` crea una carpeta llamada `clases` dentro de tu carpeta personal. Si responde que ya existe, ignóralo.
2. `cd clases` entra en ella.
3. `git clone ...` descarga el repositorio.
4. `cd viernes-vscode` entra a la carpeta descargada.

**Debes ver**, durante la descarga, algo como:

```
Cloning into 'viernes-vscode'...
...
Receiving objects: 100% ...
```

### Comprueba

```bash
git status
```

**Debes ver:**

```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

Esto significa: «estás en la rama principal y no has cambiado nada». Ahora mira qué hay dentro:

- Windows: `dir`
- macOS y Linux: `ls`

**Debes ver** carpetas como `data`, `scripts`, `notebooks`, `primeros-pasos-conda` y el archivo `README.md`.

### ¿Dónde quedó la carpeta?

| Sistema | Ruta |
| --- | --- |
| Windows | `C:\Users\tu_usuario\clases\viernes-vscode` |
| macOS | `/Users/tu_usuario/clases/viernes-vscode` |
| Linux | `/home/tu_usuario/clases/viernes-vscode` |

Está a propósito fuera de *Documentos*: en Windows, esa carpeta suele sincronizarse con OneDrive, que causa problemas con proyectos de programación.

### Alternativa sin Git: descargar el ZIP

Si Git no quiere instalarse, en la página del repositorio pulsa el botón verde **Code → Download ZIP** y descomprímelo dentro de `clases`. La carpeta se llamará `viernes-vscode-main`. Funciona para todo lo de la clase **excepto** la parte de guardar cambios con Git.

### Abrir en VS Code

Con la terminal dentro de `viernes-vscode`:

```bash
code .
```

El punto significa «esta carpeta». Si dice que `code` no se reconoce, abre VS Code y ve a **Archivo → Abrir carpeta** (en macOS: **File → Open Folder**) y elige `clases/viernes-vscode`.

**Regla número uno de la clase:** en VS Code se abren **carpetas**, no archivos sueltos.

---

## Parte 4 · Práctica de Git (5 minutos, recomendada)

Sirve para comprobar que Git quedó bien configurado **antes** de la clase. Trabajas en una rama de práctica que no afecta nada.

Con la terminal dentro de `viernes-vscode`:

```bash
git switch -c practica
```

**Debes ver:** `Switched to a new branch 'practica'`.

Ahora, en VS Code: **Archivo → Nuevo archivo de texto**, escribe tu nombre y guárdalo como `hola.txt` dentro de la carpeta `viernes-vscode`.

De vuelta en la terminal:

```bash
git status
```

**Debes ver** `hola.txt` en rojo, en una lista llamada *Untracked files*. Git lo ve, pero todavía no lo está guardando.

```bash
git add hola.txt
git commit -m "Mi primer commit"
```

**Debes ver** algo como `1 file changed, 1 insertion(+)`.

```bash
git log --oneline
```

**Debes ver** tu commit, `Mi primer commit`, al principio de la lista. Si la lista termina en `(END)` o `:`, presiona **q**.

Para volver a como estaba:

```bash
git switch main
```

El archivo `hola.txt` **desaparece** de la carpeta: vive solo en la rama `practica`. Así funcionan las ramas, y lo vamos a ver con calma en la clase. Para borrar la práctica por completo:

```bash
git branch -D practica
```

**Llega a la clase con tu copia en la rama `main`** (comprueba con `git branch`: la rama con `*` debe ser `main`). En la clase crearemos juntos otra rama, `clase-en-vivo`, y los arreglos de los scripts van ahí.

Si tu `git commit` falló con `Please tell me who you are`, vuelve a la Parte 2.

---

## Parte 5 · Regla de la clase: Commit sí, Sync no

En la clase vas a guardar cambios con el panel de Git de VS Code. Para eso:

- **Commit** (guardar cambios en tu computadora): **sí, todos los que quieras.**
- **Sync Changes**, **Push** o **Publish** (subir a internet): **no lo presiones.**

Tu copia apunta al repositorio de Miguel y no tienes permiso para escribir en él, así que subir da error (`403` o `Permission denied`). El error es inofensivo: tus commits siguen en tu computadora. Si quieres subir tus cambios a tu propia cuenta, está la Parte 6.

---

## Parte 6 · Opcional: tu propia copia en GitHub

Solo si ya tienes cuenta y quieres subir tu trabajo.

1. Entra a [github.com/MiguelDiaz02/viernes-vscode](https://github.com/MiguelDiaz02/viernes-vscode) con tu cuenta.
2. Pulsa **Fork** (arriba a la derecha) y luego **Create fork**. Eso crea una copia tuya en `github.com/TU_USUARIO/viernes-vscode`.
3. En la terminal, dentro de tu carpeta `viernes-vscode`, apunta tu copia local a tu fork. Cambia `TU_USUARIO` por tu usuario de GitHub:

```bash
git remote set-url origin https://github.com/TU_USUARIO/viernes-vscode.git
git remote -v
```

**Debes ver** tu usuario en las dos líneas que aparecen.

4. Para subir los cambios, usa VS Code: panel de Git (**Ctrl + Shift + G**, en macOS **Cmd + Shift + G**) → **Sync Changes** (o *Publish Branch*). La primera vez VS Code dice que quiere iniciar sesión con GitHub: pulsa **Permitir**, se abre el navegador, pulsa **Authorize**. Es lo más sencillo en los tres sistemas.

---

## Glosario de 30 segundos

| Palabra | Significa |
| --- | --- |
| **Terminal** | Ventana donde das órdenes escribiendo |
| **Git** | Programa que guarda el historial de un proyecto |
| **GitHub** | Sitio web donde se guardan proyectos de Git |
| **Repositorio** | Carpeta de proyecto con todo su historial |
| **Clonar** | Copiar un repositorio de internet a tu computadora |
| **Commit** | Una «foto» de tu proyecto con un mensaje que dice qué cambió |
| **Rama (branch)** | Línea de historial paralela para probar sin riesgo. La principal se llama `main` |
| **Push / Sync** | Subir tus commits a internet |
| **Fork** | Tu propia copia de un repositorio ajeno, en tu cuenta de GitHub |

---

## Problemas comunes

| Qué ves | Qué pasó | Qué hacer |
| --- | --- | --- |
| `git` no se reconoce como comando (Windows) | La terminal se abrió antes de instalar Git | Cierra PowerShell, ábrelo de nuevo y repite. Si sigue, reinstala con la opción B |
| Aparece una ventana pidiendo instalar herramientas (macOS) | Es la instalación normal de Git | Pulsa **Instalar** y espera |
| `xcrun: error: invalid active developer path` (macOS) | Una actualización del sistema borró las herramientas | Pega `xcode-select --install` |
| `Please tell me who you are` o `Author identity unknown` | Falta la Parte 2 | Haz la Parte 2 y repite el commit |
| `destination path 'viernes-vscode' already exists` | Ya lo habías clonado | Entra con `cd viernes-vscode`; no hace falta clonar otra vez |
| `Could not resolve host: github.com` o se queda colgado | Sin internet, o una red con firewall (escuela, laboratorio) | Prueba otra red o los datos del celular. Como salida, usa el ZIP |
| La pantalla se llena de texto y abajo hay `(END)` o `:` | Es un visor de texto de la terminal | Presiona **q** |
| Se abre una pantalla rara con `~` en cada línea (Vim) | Git abrió un editor para el mensaje del commit | Presiona **Esc**, escribe `:q!` y Enter. Luego repite el commit con `-m "mensaje"` |
| Ctrl + V no pega (Linux) | En la terminal de Linux el atajo es otro | **Ctrl + Shift + V** |
| `sudo: apt: command not found` | Tu distribución no usa `apt` | Fedora: `sudo dnf install -y git`. Arch: `sudo pacman -S git` |
| `winget` no se reconoce (Windows) | Tu Windows es anterior a Windows 10 versión 1809 o no lo trae | Usa la opción B (instalador) |
| `Permission denied` o `403` al subir cambios | Estás subiendo al repositorio de Miguel | Es normal: ver Parte 5 |
| Todo lo demás | | Escribe a g5diazcamposmiguel@gmail.com con una captura de pantalla de la terminal completa |

---

## Lista final: ¿quedó todo?

- [ ] `git --version` responde con un número
- [ ] `git config --global --list` muestra tu nombre y tu correo
- [ ] La carpeta `clases/viernes-vscode` existe y `git status` dice *working tree clean*
- [ ] Lograste hacer un commit de práctica (Parte 4), o al menos no te marcó error

Siguiente paso: **[Mis primeros pasos con conda](../primeros-pasos-conda/README.md)**.
