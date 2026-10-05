# Publicar el repositorio

## Ruta A: con cuenta de GitHub

Desde VS Code, sin terminal:

1. Abre la carpeta en VS Code.
2. Panel de control de versiones (Ctrl+Shift+G). Si la carpeta no es un repositorio todavía, pulsa **Initialize Repository**.
3. Prepara todos los archivos con el **+** junto a «Changes», escribe `Commit inicial` y pulsa **Commit**.
4. Pulsa **Publish Branch**. VS Code te pide iniciar sesión en GitHub la primera vez.
5. Elige público o privado y el nombre `viernes-vscode`. Listo, ya está en línea.

Desde la terminal, si prefieres:

```bash
git init
git add .
git commit -m "Commit inicial"
gh repo create MiguelDiaz02/viernes-vscode --public --source=. --push
```

(`gh` es la CLI de GitHub; sin ella, crea el repo vacío en github.com y sigue las
instrucciones que aparecen: `git remote add origin https://github.com/MiguelDiaz02/viernes-vscode.git` y `git push -u origin main`.)

## Ruta B: sin cuenta de GitHub

Git funciona completo en tu máquina, sin remoto:

```bash
git init
git add .
git commit -m "Commit inicial"
```

Con eso ya tienes historial, vista de diferencias y ramas dentro de VS Code.
Cuando tengas cuenta, el botón **Publish Branch** del panel de Git sube todo tal cual.

## Para dar la clase

Ten el repositorio en su estado inicial, con **un solo commit** y las fallas intactas.
Clónalo en tu laptop y en el servidor. Si vas a hacer push en vivo, prueba el push
el mismo día desde las dos máquinas.
