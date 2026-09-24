# Cria conexão com o banco de dados. Aqui Declaro URL, engine e Session Local. Resumindo é a comunicação com o DB

from sqlalchemy import create_engine # SQLalchemy faz a tradução do DB para o python
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Vai rodar separado do nosso FastAPI. Vão se comunicar por endpoint

DATABASE_URL = "postgresql://postgres:postgres@localhost/escola"

#Sem essa linha, nada poderia se comunicar com o Postgres
engine = create_engine(DATABASE_URL) # Motor do banco de dados. Vai comunicar o DB com o FastAPI.
SessionLocal = sessionmaker(bind=engine) # Cria conexão temporária com o banco de dados

Base = declarative_base() # Serve para criar nossas entidades