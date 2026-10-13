# viernes-vscode

Material de la clase **VS Code desde cero** para el grupo Viernes de Bioinformática.
30 de octubre de 2026 · Miguel Ángel Díaz Campos · Laboratorio de Fallas Medulares,
Instituto de Investigaciones Biomédicas, UNAM.

Es un proyecto pequeño, con datos inventados, hecho para aprender el editor.
**Los scripts tienen errores a propósito.** Arreglarlos es parte de la clase.

Funciona en **Windows, macOS y Linux**.

---

## Empieza aquí

Prepararte toma alrededor de una hora, **una sola vez**, y debe hacerse **antes de la clase**.
Cada paso tiene su guía, escrita para quien nunca ha usado la terminal.

| Paso | Qué haces | Guía |
| --- | --- | --- |
| 1 | Instalar VS Code y crear tu cuenta de GitHub | La guía ilustrada que te compartió Miguel |
| 2 | Instalar Git, descargar este repositorio y aprender lo básico de la terminal | **[primeros-pasos-github](primeros-pasos-github/README.md)** |
| 3 | Instalar Python y crear el entorno de la clase | **[primeros-pasos-conda](primeros-pasos-conda/README.md)** |
| 4 | Abrir la carpeta en VS Code | Última sección de la guía del paso 3 |

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
| [`primeros-pasos-github/`](primeros-pasos-github/README.md) | Guía de la terminal, Git y GitHub, para Windows, macOS y Linux |
| [`primeros-pasos-conda/`](primeros-pasos-conda/README.md) | Guía de instalación de Python y del entorno, más los archivos del entorno y el verificador |
| [`data/`](data/README.md) | Un experimento inventado: células HepG2 en hipoxia. Metadatos sucios a propósito y una matriz de conteos |
| `scripts/` | Cuatro scripts numerados. Cada uno tiene un error pequeño |
| `notebooks/` | Un notebook de exploración, para comparar con los scripts |
| [`ejercicios/`](ejercicios/) | Cinco ejercicios para después de la clase. Las soluciones se publican aquí cuando termina la clase |
| `.vscode/` | Configuración del proyecto para VS Code. No hace falta tocarla |
| `.devcontainer/` | Solo para GitHub Codespaces. Si usas tu computadora, ignóralo |

## Los cuatro errores

Cada script tiene un error pequeño, del tipo que aparece todos los días. Los arreglamos juntos en
la clase, uno por uno, y cada arreglo es un commit de Git. **No los arregles antes**: vale la pena
ver el error aparecer.

Los arreglos no se hacen sobre `main`, sino en una rama propia llamada `clase-en-vivo`
(**la creamos juntos en la clase**; si quieres adelantarte, abajo a la izquierda, clic en `main` →
**Create new branch** → `clase-en-vivo`). Así `main` conserva los errores para que cualquiera
pueda repetir la clase, y tus commits se quedan en tu computadora.

---

## Después de la clase

### Los ejercicios

En [`ejercicios/`](ejercicios/), en orden. Cubren lo que no cupo en 45 minutos. Cada uno nombra el archivo que debes crear:

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
