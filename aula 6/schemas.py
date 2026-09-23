# Schemas é responsável por validação dos dados

from pydantic import BaseModel

class EstudanteBase(BaseModel): # Garantimos que o que vem no campo nome e idade é str e int
    nome: str
    idade: int

class EstudanteCreate(EstudanteBase): # Recebe os mesmos parâmetros da Base
    pass

class EstudanteResponse(EstudanteBase): # Como os dados serão devolvidos na aplicação.
    id: int
    class Config:
        from_attributes = True # Isso é do Pydantic. Permite ler diretamente os atributos no banco de dados

class MatriculaBase(BaseModel):
    estudante_id: int
    nome_disciplina: str

class MatriculaCreate(MatriculaBase):
    pass

class MatriculaResponse(MatriculaBase):
    id: int
    class Config:
        from_attributes=True
        