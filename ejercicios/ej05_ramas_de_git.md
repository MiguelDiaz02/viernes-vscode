# Ejercicio 5 · Una rama para probar sin miedo

Quieres probar una normalización distinta (TPM en lugar de CPM) sin tocar lo que funciona.

1. Abajo a la izquierda, clic en el nombre de la rama → **Create new branch** → `tpm`.
2. Modifica `scripts/03_normalizar.py` para que use una normalización distinta (basta con
   cambiar el nombre del archivo de salida y agregar una línea de comentario; el punto es el flujo).
3. Panel de Git: mira el diff, haz commit en la rama `tpm`.
4. Cambia de vuelta a `main` desde el mismo sitio. Abre el script: tu cambio no está.
   Vuelve a `tpm`: está.
5. Abre **Source Control Graph** en el panel de Git y mira cómo se bifurcan las dos ramas.
6. Opcional: desde `main`, paleta de comandos → **Git: Merge Branch** → `tpm`.

Si tienes remoto, publica la rama con **Publish Branch** y mírala en GitHub.

---

Solución: `soluciones/ej05_ramas_de_git.md`. Se publica en el repositorio después de la clase.
