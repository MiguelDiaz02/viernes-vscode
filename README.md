# viernes-vscode

Material de la clase **VS Code desde cero** para el grupo Viernes de Bioinformática.
30 de octubre de 2026 · Miguel Ángel Díaz Campos · Laboratorio de Fallas Medulares,
Instituto de Investigaciones Biomédicas, UNAM.

En la clase escribimos **un script de Python en vivo**, desde la primera línea, con datos reales de
hepatocarcinoma (TCGA-LIHC): importamos bibliotecas, descargamos los datos, escribimos funciones y
guardamos una tabla y una figura. Mientras tanto vemos el autocompletado, la búsqueda y el
depurador, y al final Git y GitHub. El proyecto de la clase se crea **desde cero**, en una carpeta
vacía. Aquí está el análisis terminado como respaldo y un segundo proyecto, con errores a
propósito, para practicar después.

Funciona en **Windows, macOS y Linux**.

---

## Empieza aquí

Prepararte toma alrededor de una hora, **una sola vez**, y debe hacerse **antes de la clase**.
Cada paso tiene su guía, escrita para quien nunca ha usado la terminal.

| Paso | Qué haces | Guía |
| --- | --- | --- |
| 1 | Instalar VS Code y crear tu cuenta de GitHub | **[INSTALACION_VISUAL_STUDIO_CODE.pdf](INSTALACION_VISUAL_STUDIO_CODE.pdf)** (VS Code) + los pasos en [primeros-pasos-github](primeros-pasos-github/README.md#antes-de-empezar) (cuenta de GitHub) |
| 2 | Instalar Git y aprender lo básico de la terminal. Para la clase solo hacen falta las partes 1 y 2; descargar este repositorio es opcional | **[primeros-pasos-github](primeros-pasos-github/README.md)** |
| 3 | Instalar Python y crear el entorno de la clase | **[primeros-pasos-conda](primeros-pasos-conda/README.md)** |
| 4 | Elegir dónde vas a trabajar: una carpeta `clases` con ruta corta, sin acentos ni espacios (por ejemplo `C:\clases` o `~/clases`). En la clase creamos juntos la carpeta del proyecto. Necesitas internet: el script descarga los datos | — |

Al terminar el paso 3, este comando debe decir **Todo listo**:

```bash
python primeros-pasos-conda/verificar_instalacion.py
```

¿Algo no funciona? Cada guía tiene una tabla de **Problemas comunes**. Si no sale, escribe a
g5diazcamposmiguel@gmail.com con una captura de pantalla de todo lo que ves.

---

## Qué hay en cada carpeta

| Carpeta o archivo | Qué contiene |
| --- | --- |
| [`INSTALACION_VISUAL_STUDIO_CODE.pdf`](INSTALACION_VISUAL_STUDIO_CODE.pdf) | Guía ilustrada, paso a paso, para instalar VS Code en Windows, macOS y Linux |
| [`primeros-pasos-github/`](primeros-pasos-github/README.md) | Guía de la terminal, Git y GitHub, para Windows, macOS y Linux |
| [`primeros-pasos-conda/`](primeros-pasos-conda/README.md) | Guía de instalación de Python y del entorno, más los archivos del entorno y el verificador |
| [`data/`](data/README.md) | Los datos de la clase (`hcc_expresion.csv`, `hcc_clinicos.csv`): expresión de 12 genes en 371 tumores de hepatocarcinoma, de TCGA. El script de la clase los descarga de aquí. También los datos inventados de la práctica en casa |
| `respaldo/` | El análisis terminado de la clase, como script (`.py`) y como cuaderno (`.ipynb`), por si te pierdes |
| `scripts/` | Práctica en casa: cuatro scripts numerados. Cada uno tiene un error pequeño |
| `notebooks/` | Práctica en casa: un notebook de exploración, para comparar con los scripts |
| [`ejercicios/`](ejercicios/) | Cinco ejercicios para después de la clase. Las soluciones se publican aquí cuando termina la clase |
| `.vscode/` | Configuración del proyecto para VS Code. No hace falta tocarla |
| `.devcontainer/` | Solo para GitHub Codespaces. Si usas tu computadora, ignóralo |

## Para practicar después: los cuatro errores

Los scripts de `scripts/` tienen cada uno un error pequeño, del tipo que aparece todos los días.
Son para practicar **después de la clase**: encuentra el error con lo que viste (mensaje de error,
depurador, buscar) y arréglalo.

Los arreglos no se hacen sobre `main`, sino en una rama propia (abajo a la izquierda, clic en
`main` → **Create new branch** → `clase-en-vivo`). Así `main` conserva los errores para que
cualquiera pueda repetirlo, y tus commits se quedan en tu computadora.

---

## Después de la clase

### Los ejercicios

En [`ejercicios/`](ejercicios/), en orden. Cubren lo que no cupo en la clase. Cada uno nombra el archivo que debes crear:

1. Limpiar los metadatos con pandas
2. Limpiar los mismos metadatos solo con el editor y expresiones regulares
3. Convertir un script en celdas ejecutables
4. Usar el depurador en lugar de `print`
5. Crear una rama de Git para probar sin miedo

### Guardar tu trabajo con Git

Cada cambio que hagas se puede guardar en el historial desde el panel de control de
versiones de VS Code (Ctrl+Shift+G): escribe un mensaje y pulsa **Commit**. Todo queda en
tu computadora. **No pulses Sync Changes**: tu copia apunta al repositorio de la clase y no
tienes permiso para subir ahí. Para tener tu propia copia en GitHub, ver la
[Parte 6 de la guía de GitHub](primeros-pasos-github/README.md#parte-6--opcional-tu-propia-copia-en-github).

---

## Licencia

MIT. Úsalo, adáptalo, da tu propia versión de la clase.
