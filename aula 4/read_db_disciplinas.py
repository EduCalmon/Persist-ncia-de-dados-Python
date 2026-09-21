import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute( # SELECT seve para consultar. * serve para consultar tudo. FROM escolhe de onde quero consultar
    """
        SELECT * FROM disciplinas
    """
)

conn.commit()

disciplinas = cursor.fetchall() # Salva tudo dentro do select na variável estudantes

for disciplina in disciplinas:
    print(disciplina)
    
conn.close()