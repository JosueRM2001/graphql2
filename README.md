# GraphQL
Este es un proyecto que fue desarrollado con Python en una arquitectura GraphQL.

## Descripción
Este proyecto muestra una página en la cual dará la bienvenida con un mensaje y mostrara una tabla. 
Es un programa sencillo para mostrar cómo funciona un programa en el lenguaje de programación con un estilo de arquitectura.

## Tecnologías Utilizadas
**Contiene lo Siguiente**
- Python(version mas actual)
- Docker
- fastapi
- uvicorn
- strawberry-graphql
- httpie

## Requerimientos para el Desarrollo
- **Docker Desktop** (si lo quieres correr en un contenedor)
- **Visual Studio Code** (opcional, pero recomendado)
- **Python**(requerido y recomendado)
- **La extensión Python para Visual Studio Code** (para mejorar el soporte y el resaltado de sintaxis).
- **GitHub Desktop** (si quieres clonar y usar el proyecto)
  
  ```bash
  https://www.docker.com/products/docker-desktop/
  ```
  
- **Docker hub** (si quieres clonar y usar el proyecto)
  
  ```bash
  https://hub.docker.com/layers/erickjrm/programgraphql/latest/images/sha256-1ce12e0bbf8197ee7606698418e93b402ea288c5febf07abe72b5dc9b5580460?context=repo
  ```

## Intruciciones para ejecutar el proyecto
## Pasos para ejecutar
- **Paso #1**
  **Clonar este repositorio**
Si aún no ha clonado el repositorio, puede hacerlo con el siguiente link:

 ```bash
https://github.com/JosueRM2001/graphql2.git
 ```
- **Paso #2**
  **Construya la imagen de Docker**

Ejecuta el siguiente comando, que generará la imagen:

```bash
docker pull erickjrm/programgraphql:latest
```

**Paso #3**
**Ejecute el contenedor Docker:**

Luego ejecuta el siguiente comando, que genera el contenedor y el puerto.

```bash

docker run -d -p 8080:80 --name graphql erickjrm/programgraphql:latest
```

**Paso #4**

Abre Docker Desktop para ver si la imagen se creó correctamente y envíala a ejecutar para verla.

**Paso #5**

**Accede a la aplicación**: Si está ejecutándose, puedes acceder a la aplicación navegando a la

siguiente url en tu navegador web:

```bash
http://localhost:8080
```
