# Proyecto "Book" FastAPI

Este proyecto se encuentra basado en un [curso de FastAPI]() donde aplico lo aprendido en este proyecto. Dentro de este proyecto podrás ver:

1. FastAPI.

2. Pydantic.

3. Pixi (manejador de dependencias del proyecto).

4. Manejo de errores.

## Pre-Requisitos

Se recomienda tener instalado Pixi para poder correr el proyecto, en caso contrario te dejaré un requirements para que puedas realizar la instalación de las dependencias por tu cuenta.

Para instalar dependencias del proyecto usando Pixi, haremos lo siguiente:

```bash
pixi install
```

## Ejecutar proyecto
En caso de que no te encuentres utilizando *Pixi* y hayas instalado las dependencias del proyecto. Te recomiendo utilizar el siguiente comando para inicializar el servidor:

```bash
uvicorn main:app
```

Si quieres ver la documentación de las diferentes APIs debes acceder a la siguiente ruta:

```
http://127.0.0.1:8000/docs
```

En caso contrario para ejecutar la app con *Pixi*:

```bash
pixi run dev
```
