from fastapi import FastAPI, APIRouter; #fASTAPI  aplicación web, Body para manejar los datos del cuerpo de las solicitudes HTTP y Path para manejar los parámetros de la ruta
from pydantic import BaseModel;  # Se importa BaseModel para definir modelos de datos que se utilizarán en las solicitudes y respuestas
from JWT import createToken; #Se importan las funciones createToken y validatedToken desde el módulo JWT


routerUser = APIRouter() #Se crea una instancia de APIRouter para manejar las rutas relacionadas con las películas


class User(BaseModel): 
    id:str
    name:str
    email: str
    password:str

# Rutas de User
@routerUser.post('/login', tags=['User'])
def login(user:User):
    token:str = createToken(data = user.model_dump()) 
    print (token)
    return token