# Define os endpoints

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine

# Cria as tabela no PostgreSQL caso não exista
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post(
        '/estudantes/',
        response_model=schemas.EstudanteResponse # Usamos o schemas para dizer qual tipo de dado deve chegar
        )
def create_student(
    student: schemas.EstudanteCreate, # Define qual o formato o parâmetro student deve ter
    db: Session = Depends(get_db)): # Abre a sessão com o banco de dados, envia e fecha conexão

    # Usa dado do navegador. o model_dump é pra converter HTTP em dicionário
    db_student = models.Estudante(**student.model_dump()) # O normal é Estudante(nome='Eduardo', idade=18)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

                        # Modelo de resposta recebe uma lista (que é a do chemas)
@app.get('/estudantes/', response_model= List[schemas.EstudanteResponse])
def read_students(db: Session = Depends(get_db)):

    # Como se fosse SQL. O alchemy traduz. Pega o db, BUSQUE nos (parâmetros) todas as ocorrências
    students = db.query(models.Estudante).all()
    return students