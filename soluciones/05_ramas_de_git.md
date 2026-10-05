# Solución del ejercicio 5

No hay código que entregar; el resultado es el historial. Si lo hiciste bien,
`git log --oneline --graph --all` en la terminal muestra algo como:

```
* a1b2c3d (tpm) Prueba normalización TPM
* 9f8e7d6 (HEAD -> main) Agrega import faltante
* ...
```

Y el Source Control Graph del panel de Git dibuja lo mismo.

Dos cosas que suelen confundir:

- Al cambiar de rama con archivos sin guardar, VS Code avisa. Guarda o descarta antes.
- `Publish Branch` sube solo la rama actual. Para subir `tpm`, párate en ella primero.
