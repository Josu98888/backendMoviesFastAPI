from fastapi import FastAPI; # Se importa FastAPI para crear una aplicación web
from db.database import Base, engine; # Se importa el motor de base de datos desde el módulo database y Base para definir los modelos de datos
from routers.movies import routerMovie; # Se importa el enrutador de películas desde el módulo routers.movies
from routers.users import routerUser; # Se importa el enrutador de usuarios desde el módulo routers.users

# Se crea una instancia de FastAPI
app = FastAPI(
    title = 'Api con FastAPI',
    description = 'Esto es una api con FastAPI',
);  

app.include_router(routerMovie) # Se incluye el enrutador de películas en la aplicación FastAPI
app.include_router(routerUser) # Se incluye el enrutador de usuarios en la aplicación FastAPI

 # Crea todas las tablas definidas en los modelos de datos en la base de datos utilizando el motor de base de datos
Base.metadata.create_all(bind=engine) 

@app.get('/', tags=['Home'])  # Se define una ruta para la raíz del sitio web
def read_root():  # Se define una ruta raíz
    return {"message": "Hello, World!"} # Se devuelve un mensaje JSON al acceder a la ruta raíz

