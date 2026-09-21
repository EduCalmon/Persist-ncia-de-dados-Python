import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute(
    """
        INSERT INTO disciplinas (estudante_id, nome_disciplina) \
        VALUES (?,?)
    """,
    ("1", "Matemática")
) # VALUES (?,?) é uma forma segura de inserir os valores no banco de dados

conn.commit()
conn.close()