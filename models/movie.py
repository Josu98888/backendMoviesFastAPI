from db.database import Base # Importa la clase Base desde el módulo database
from sqlalchemy import Column, Integer, String # Importa Column, Integer y String desde SQLAlchemy para definir columnas en la base de datos


# Define el modelo de datos para la tabla "movies" en la base de datos utilizando SQLAlchemy
class Movie(Base):
    __tablename__ = 'movies'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True, index=True)  # Columna de ID, clave primaria y con índice
    title = Column(String, nullable=False)  # Columna de título, no puede ser nula
    director = Column(String, nullable=False)  # Columna de director, no puede ser nula
