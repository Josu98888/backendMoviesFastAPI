import os; #Se importa el módulo os para interactuar con el sistema operativo.
from sqlalchemy import create_engine; #Se importa create_engine desde SQLAlchemy para crear una conexión a la base de datos.
from sqlalchemy.orm.session import sessionmaker; #Se importa sessionmaker para crear sesiones de base de datos.
from sqlalchemy.ext.declarative import declarative_base; #Se importa declarative_base para definir modelos de base de datos.


sqlite = 'movies.sqlite' # Nombre del archivo de la base de datos SQLite
baseDir = os.path.dirname(os.path.abspath(__file__)) # Obtiene el directorio base del archivo actual
databaseUrl = f'sqlite:///{os.path.join(baseDir, sqlite)}' # Construye la URL de la base de datos SQLite

engine = create_engine(databaseUrl, echo=True) # Crea un motor de base de datos SQLite

Session = sessionmaker(bind=engine) # Crea una clase de sesión vinculada al motor de base de datos

Base = declarative_base() # Crea una clase base para los modelos de base de datos