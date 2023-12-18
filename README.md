### Despliegue de una app básica en Flask con Docker

Dividiendo las tareas del siguiente proyecto por dificultad y estado del proceso en Jira llevaremos a cabo el despliegue de una aplicación básica con Flask (python3) y Docker. Haciendo un seguimiento del proyecto mediante GitHub (repositorio: https://github.com/estherrc2408/despliegue-docker-flask.git)

1. Para ver el proceso de creación del proyecto tenemos los pasos tanto en Jira como en el archivo del repositorio 'pasos.md'
```
https://mestherrc.atlassian.net/jira/software/projects/PE/boards/2
```

2. Accedemos a la carpeta donde queremos guardar el proyecto de forma local y descargamos el repositorio usando los siguientes comandos por terminal:
```bash
git clone https://github.com/estherrc2408/despliegue-docker-flask.git
cd despliegue-docker-flask
```

3. Creamos la imagen y contenedor a partir del dockerfile
Imagen:
```bash
docker build -t flaskapp:latest .
```
Contenedor:
```bash
docker run -p 4000:4000 flaskapp:latest
```

4. Accedemos a la web creada desde la siguiente URL:
```
http://localhost:4000/users
```

5. *En caso de querer parar el contenedor y borrar contenedor e imagen*:
*Parar contenedor:*
```bash
docker stop flaskapp
```
*Borrar contenedor (sustituyendo flaskapp por su CONTAINER ID):*
```bash
docker rm flaskapp
```
*Borrar imagen:*
```bash
docker rmi flaskapp
```

