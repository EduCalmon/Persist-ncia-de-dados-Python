import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute( # SELECT seve para consultar. * serve para consultar tudo. FROM escolhe de onde quero consultar
    """
        SELECT * FROM estudantes
    """
)

conn.commit()

estudantes = cursor.fetchall() # Salva tudo dentro do select na variável estudantes

for estudante in estudantes:
    print(estudante)
    
conn.close()