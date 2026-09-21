import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute(
    """
        INSERT INTO estudantes (nome, idade) \
        VALUES (?,?)
    """,
    ("Ronaldo", 15)
) # VALUES (?,?) é uma forma segura de inserir os valores no banco de dados

conn.commit()
conn.close()