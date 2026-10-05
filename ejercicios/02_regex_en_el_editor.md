# Ejercicio 2 · Lo mismo, pero sin Python

Haz la limpieza del ejercicio 1 directamente en el editor, sobre una copia del CSV.

1. Copia `data/metadatos_muestras.csv` como `data/metadatos_editor.csv` (clic derecho en el explorador → Copiar, Pegar).
2. Con Ctrl+H y el modo de expresiones regulares (botón `.*`), convierte las fechas
   `DD/MM/AAAA` a `AAAA-MM-DD`. Necesitas tres grupos de captura y reordenarlos en el reemplazo.
3. Con Ctrl+Shift+L, normaliza los valores de `condition`.
4. Borra la fila duplicada a mano.
5. Compara los dos archivos: selecciona ambos en el explorador, clic derecho → **Compare Selected**.

Pregunta para pensar: ¿cuándo conviene esto y cuándo conviene el script del ejercicio 1?
(Pista: ¿qué pasa cuando llega el segundo lote de muestras?)
