# Define as entidades da nossa aplicação

from sqlalchemy import \
    Column, Integer, String, ForeignKey
from database import Base

class Estudante(Base): # Importa a base para mapear uma classe no banco de dados. É como se fosse o molde
    __tablename__ = 'estudantes' # Criamos uma tabela
    id = Column( # Criamos uma coluna com esses dados.
        Integer,
        primary_key=True,
        index=True # O index faz com que crie automaticamente
        )
    nome = Column(
        String(100), # Define o tamanho da String
        nullable=False # Significa que não pode ser um valor nullo
        )
    age = Column(
        Integer
    )

class Matricula(Base):
    __tablename__ = 'matriculas'
    id = Column(
        Integer,
        primary_key=True,
        index=True
        )
    student_id = Column(
        Integer,
        ForeignKey('estudantes.id')
        )
    nome_disciplina = Column(
        String(100),
        nullable=False
    )
