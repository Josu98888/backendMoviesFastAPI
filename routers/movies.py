from fastapi import FastAPI, Path,HTTPException, Query, APIRouter; #fASTAPI  aplicación web, Body para manejar los datos del cuerpo de las solicitudes HTTP y Path para manejar los parámetros de la ruta
from pydantic import BaseModel, Field;  # Se importa BaseModel para definir modelos de datos que se utilizarán en las solicitudes y respuestas
from typing import Optional; # Se importa Optional para definir campos opcionales en los modelos de datos
from fastapi.responses import JSONResponse; # Se importa JSONResponse para devolver respuestas JSON personalizadas
from fastapi.security import HTTPBearer; # Se importa HTTPBearer para manejar la autenticación basada en tokens Bearer
from db.database import Base, Session; # Se importan las clases Base, Session y engine desde el módulo database para interactuar con la base de datos
from models.movie import Movie as  ModelMovie; # Se importa el modelo Movie desde el módulo movie para definir la estructura de las películas en la base de datos
from fastapi.encoders import jsonable_encoder; # Se importa jsonable_encoder para convertir objetos de Pydantic a JSON serializable

# josu
routerMovie = APIRouter() #Se crea una instancia de APIRouter para manejar las rutas relacionadas con las películas

# Clase para manejar la autenticación Bearer con JWT
class BearerJWT(HTTPBearer):
    async def __call__(self, request): # Se define el método __call__ para manejar la autenticación
        auth = await super().__call__(request) # Se llama al método __call__ de la clase base HTTPBearer para obtener el token de autenticación
        data = validatedToken(auth.credentials) # Se valida y decodifica el token utilizando la función validatedToken
        if data['email'] != 'josu@test.com' :
            raise HTTPException(status_code=403, detail='Credenciales inválidas')


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default= 'titulo', min_length=3, max_length=15)
    director: str = Field(default= 'director', min_length=3, max_length=15)


# Se define una ruta para obtener una lista de películas 
@routerMovie.get('/movies', tags=['Movie'])  
def getMovies():
    db = Session()  # Crea una sesión de base de datos
    movies = db.query(ModelMovie).all()  # Obtiene todas las películas de la base de datos
    return JSONResponse(content= jsonable_encoder(movies)) # Se devuelve una lista de películas con un mensaje y un código de estado 200

 
# Se define una ruta para obtener una película por su ID
@routerMovie.get('/movies/{id}', tags=['Movie'] )
def getMovie(id:int = Path(ge= 1)):
    db = Session()  # Crea una sesión de base de datos
    movie = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    if not movie:
        return JSONResponse(content={"message": "Movie not found"},status_code=404 )  # Si no se encuentra la película, se devuelve un mensaje de error con un código de estado 404
    return JSONResponse(content= jsonable_encoder(movie))  # Se devuelve la película encontrada con un código de estado 200


# Se define una ruta para buscar por titulo una peliculla
@routerMovie.get('/movies/', tags=['Movie'])
def getMoviesByTitle (title:str = Query(min_length=1, max_length=100) ):
    db = Session()  # Crea una sesión de base de datos
    movies = db.query(ModelMovie).filter(ModelMovie.title == title).all()
    return JSONResponse(content= jsonable_encoder(movies), status_code= 200)  # Se devuelve una lista de películas que coinciden con el título proporcionado con un código de estado 200;

# Se define una ruta para crear una nueva pelicula
@routerMovie.post('/movies', tags=['Movie'])
def createMovie(movie: Movie):
    db = Session()  # Crea una sesión de base de datos
    newMovie = ModelMovie(**movie.model_dump())
    db.add(newMovie)
    db.commit()
    return JSONResponse(content= {"message": "Movie created successfully", "movie": movie.model_dump()});  # Se devuelve un mensaje de éxito y la película creada con un código de estado 201

# Se define una ruta para actualizar una película por su ID
@routerMovie.put('/movies/{id}', tags=['Movie'])
def updateMovie(movie: Movie, id:int):
    db = Session() # Crea una sesión de base de datos
    movieUpdate = db.query(ModelMovie).filter(ModelMovie.id == id).first() # Busca la película por su ID
    if not movieUpdate:
            return JSONResponse(content = {'message': 'Movie not fount'}, status_code = 404)
    movieUpdate.title = movie.title
    movieUpdate.director = movie.director
    db.commit()  # Guarda los cambios en la base de datos
    db.refresh(movieUpdate)  # Actualiza la película en la base de datos
    return JSONResponse(content= {"message": "Movie updated successfully", "movieUpdated": jsonable_encoder(movieUpdate)});

# Se define una ruta para eliminar una película por su ID
@routerMovie.delete('/movies/{id}', tags=['Movie'])
def deleteMovie(id: int):
    db = Session()  # crea una sesión de base de datos
    movieDeleted = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    if not movieDeleted :
            return JSONResponse(content= {'message': 'Movie not found'}, status_code=404);
    db.delete(movieDeleted) # Elimina la película de la base de datos
    db.commit() # Se guarda los cambios en la base de datos
    return JSONResponse(content= {"message": "Movie deleted successfully", "movieDeleted": jsonable_encoder(movieDeleted)});
