# Define as entidades da nossa aplicação

from sqlalchemy import \
    Column, Integer, String, ForeignKey
from database import Base # Traz a classe base criada no arquívo anterior. Conecta as classes na Engine

class Estudante(Base): # Importa a base para mapear uma classe no banco de dados. É como se fosse o molde
    __tablename__ = 'estudantes' # Nomeamos a tabela. Sem isso da erro na hora de criar
    id = Column( # Criamos uma coluna com esses dados.
        Integer,
        primary_key=True, # Toda entidade mapeada precisa ter uma chave primária. É obrigatório
        index=True # O index faz com que crie automaticamente
        )
    nome = Column(
        String(100), # Define o tamanho da String
        nullable=False # Significa que não pode ser um valor nullo
        )
    idade = Column(
        'age',
        Integer
    )

class Matricula(Base):
    __tablename__ = 'matriculas'
    id = Column(
        Integer,
        primary_key=True,
        index=True
        )
    estudante_id = Column(
        Integer,
        ForeignKey('estudantes.id'), # Usa um dado de outra classe
        name='student_id'
        )
    nome_disciplina = Column(
        String(100),
        nullable=False
    )
