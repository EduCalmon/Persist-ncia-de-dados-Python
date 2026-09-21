import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute( # SELECT seve para consultar. * serve para consultar tudo. FROM escolhe de onde quero consultar. Aqui pude escolher os parâmetros
    """
        SELECT * FROM estudantes WHERE id = 1
    """
)

conn.commit()

estudante = cursor.fetchall() # Salva tudo dentro do select na variável estudantes
print(estudante)

cursor.execute( # Crio uma consulta conjunta entre as duas tabelas
    """
        SELECT estudantes.nome, disciplinas.nome_disciplina FROM disciplinas JOIN estudantes ON disciplinas.estudante_id
    """
)

estudante_join = cursor.fetchall()
print(estudante_join)

conn.close()