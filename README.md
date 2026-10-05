# viernes-vscode

[![verificar fallas](https://github.com/MiguelDiaz02/viernes-vscode/actions/workflows/verificar-fallas.yml/badge.svg)](https://github.com/MiguelDiaz02/viernes-vscode/actions/workflows/verificar-fallas.yml)

Material de la clase **VS Code desde cero** para el grupo Viernes de Bioinformática.
30 de octubre de 2026 · Miguel Ángel Díaz Campos · Laboratorio de Fallas Medulares,
Instituto de Investigaciones Biomédicas, UNAM.

Es un proyecto pequeño, con datos inventados, hecho para aprender el editor.
**Los scripts tienen errores a propósito.** Arreglarlos es parte de la clase.

---

## ¿Primera vez en GitHub?

Un **repositorio** es una carpeta con archivos y con el historial de todos sus cambios.
Esta página es la portada de esa carpeta. No necesitas cuenta de GitHub para descargarla.

Todo lo que está en recuadros gris como este se puede copiar y pegar tal cual:

```bash
echo "así se ven los comandos"
```

Pasa el ratón por encima del recuadro y aparece un botón para copiarlo.

---

## Para la clase: cuatro pasos

### Paso 1 · Descargar el repositorio

Elige **una** de las dos opciones.

**Opción fácil, sin Git:** arriba en esta página, botón verde **Code** → **Download ZIP**.
Descomprime el archivo. La carpeta se llama `viernes-vscode-main`.

**Opción con Git** (recomendada, porque en la clase vamos a usar Git):
abre una terminal y pega:

```bash
git clone https://github.com/MiguelDiaz02/viernes-vscode.git
cd viernes-vscode
```

¿No tienes Git? Compruébalo con `git --version`. Si no responde con un número, instálalo
desde [git-scm.com](https://git-scm.com/downloads) o usa la opción fácil.

### Paso 2 · Instalar el entorno de Python

Todo lo necesario está en la carpeta [`instalacion/`](instalacion/README.md), con
instrucciones paso a paso para Windows, macOS y Linux. La versión corta, si ya tienes conda:

```bash
conda env create -f instalacion/environment.yml
conda activate viernes-vscode
python -m ipykernel install --user --name viernes-vscode --display-name "Python (viernes-vscode)"
```

**Hazlo antes del día de la clase.** Tarda de 5 a 10 minutos.

### Paso 3 · Comprobar que todo funciona

Con el entorno activado y desde la carpeta del repositorio:

```bash
python instalacion/verificar_instalacion.py
```

Si la última línea dice **Todo listo**, ya estás. Si no, cada problema viene con su solución.

### Paso 4 · Abrir en VS Code

En VS Code: **Archivo → Abrir carpeta** → elige `viernes-vscode`.
Abre la carpeta completa, no un archivo suelto. Es la regla número uno de la clase.

Si VS Code ofrece instalar **extensiones recomendadas** (aviso abajo a la derecha), acepta.

Nada más. El resto lo hacemos juntos.

---

## Qué hay en cada carpeta

| Carpeta o archivo | Qué contiene |
| --- | --- |
| [`data/`](data/README.md) | Un experimento inventado: células HepG2 en hipoxia. Metadatos sucios a propósito y una matriz de conteos |
| `scripts/` | Cuatro scripts numerados. Cada uno tiene un error pequeño |
| `notebooks/` | Un notebook de exploración, para comparar con los scripts |
| [`ejercicios/`](ejercicios/) | Cinco ejercicios para después de la clase |
| `soluciones/` | Las soluciones. Intenta primero |
| [`instalacion/`](instalacion/README.md) | Entorno de conda, requirements de pip y el verificador |
| `.vscode/` | Configuración del proyecto para VS Code. No hace falta tocarla |
| `.devcontainer/` | Entorno listo para GitHub Codespaces o Docker |

## Los cuatro errores

Cada script falla por algo pequeño, del tipo que aparece todos los días.
Se arregla en menos de un minuto y cada arreglo es un commit de Git.

| Script | Qué hace | Por qué falla |
| --- | --- | --- |
| `01_explorar_metadatos.py` | Resume las muestras | Un nombre de columna mal escrito |
| `02_cargar_conteos.py` | Carga la matriz de conteos | Lee un archivo con tabuladores como si tuviera comas |
| `03_normalizar.py` | Calcula log2(CPM + 1) | Usa una ruta que solo existía en otra computadora |
| `04_grafico_expresion.py` | Grafica genes de hipoxia | Le falta una línea de `import` |

No los arregles antes de la clase. Vale la pena ver el error aparecer.

---

## Después de la clase

### Los ejercicios

En [`ejercicios/`](ejercicios/), en orden. Cubren lo que no cupo en 45 minutos:

1. Limpiar los metadatos con pandas
2. Limpiar los mismos metadatos solo con el editor y expresiones regulares
3. Convertir un script en celdas ejecutables
4. Usar el depurador en lugar de `print`
5. Crear una rama de Git para probar sin miedo

### Guardar tu trabajo con Git

Si descargaste con `git clone`, cada cambio que hagas se puede guardar en el historial
desde el panel de control de versiones de VS Code (Ctrl+Shift+G): escribe un mensaje y
pulsa **Commit**. Todo queda en tu computadora; no necesitas cuenta.

### Tener tu propia copia en GitHub

Con cuenta de GitHub, botón **Fork** arriba a la derecha de esta página. Crea una copia
del repositorio en tu cuenta, donde puedes subir tus cambios. Luego clona **tu** copia:

```bash
git clone https://github.com/TU_USUARIO/viernes-vscode.git
```

Cambia `TU_USUARIO` por tu nombre de usuario de GitHub.

---

## Problemas frecuentes

**`git` o `conda` no se reconoce como comando.** No está instalado, o la terminal se
abrió antes de instalarlo. Cierra la terminal, abre otra, y revisa
[`instalacion/README.md`](instalacion/README.md).

**`ModuleNotFoundError` al correr un script.** VS Code está usando otro Python.
Abajo a la derecha, en la barra de estado, haz clic en la versión de Python y elige
`viernes-vscode`.

**No puedo instalar nada en mi computadora.** Usa GitHub Codespaces: botón **Code** →
**Codespaces** → **Create codespace on main**. Abre VS Code en el navegador con todo
instalado. Detalles en [`instalacion/README.md`](instalacion/README.md#ruta-c--github-codespaces-sin-instalar-nada).

**Algo más.** Escríbeme a g5diazcamposmiguel@gmail.com con una captura del error.

---

## Para quien da la clase

- [`ERRATAS.md`](ERRATAS.md) dice dónde está cada error y cómo se corrige.
- [`PUBLICAR.md`](PUBLICAR.md) explica cómo subir el repositorio a GitHub, con y sin cuenta.
- Un flujo de GitHub Actions comprueba en cada cambio que los cuatro errores siguen ahí y
  que las soluciones funcionan. Si el distintivo de arriba está en rojo, alguien corrigió
  un script y lo subió a `main`.

## Licencia

MIT. Úsalo, adáptalo, da tu propia versión de la clase.
