import sqlite3

conn = sqlite3.connect('escola.db') # Conecto à um banco de dados (se não tiver ele cria).

cursor = conn.cursor()

cursor.execute( # Aqui colocamos 3 aspas para passar o comando puro de SQL
    """
        CREATE TABLE IF NOT EXISTS estudantes(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER
        )
    """
)
# Aqui tem o Foreing key, que pega uma chave de outra tabela
cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS disciplinas(
            id INTEGER PRIMARY KEY,
            nome_disciplina TEXT,
            estudante_id INTEGER,
            FOREIGN KEY (estudante_id)\
                REFERENCES estudantes(id)
        )
    """ 
)

conn.commit() # Confirma as mudan;as no banco de dados
conn.close() # Fecha o banco de dados