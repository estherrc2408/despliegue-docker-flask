1. crear entorno virtual dentro de la carpeta proyecto. Instalamos pip(biblioteca de módulos):
```bash
python -m pip install --upgrade pip
python -m venv venv
```
*NOTA:Virtualenv es una herramienta usada para crear un entorno Python aislado. Este entorno tiene sus propios directorios de instalación que no comparten bibliotecas con otros entornos virtualenv o las bibliotecas instaladas globalmente en el servidor.*

2. crear carpeta src donde irá el cuerpo de la aplicación

3. activamos el entorno virtual de python
```bash
cd venv
cd Scripts
.\activate.bat
```

4. creamos app.py con el código que queramos programar para la creación de la página con Flask, importando bibliotecas y haciendo un script.

5. Creamos el archivo requirements.txt con las versiones de cada biblioteca usada por nuestro programa
```bash
pip freeze > requirementstxt
```

6. Creamos el archivo Dockerfile, desde donde automatizaremos la creación de la página con Flask.

7. Creamos la imagen a partir del directorio actual poniendo por terminal:
```bash
docker build -t flaskapp:latest .
```

