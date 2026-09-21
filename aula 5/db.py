import sqlite3

def conectar():
    conn = sqlite3.connect('escola5.db')
    return conn

def criar_tabela_estudante():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS estudantes(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER
            )
        """
    )
    conn.commit()
    conn.close()

def criar_tabela_matricula():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS matriculas(
            id INTEGER PRIMARY KEY,
            nome_disciplina TEXT,
            estudante_id INTEGER,
            FOREIGN KEY (estudante_id) REFERENCES estudantes(id)

            )
        """
    )
    conn.commit()
    conn.close()

def criar_estudante(nome, idade):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO estudantes (nome, idade)
        VALUES (?, ?)
        """,
        (nome, idade)
    )

    conn.commit()
    conn.close()

def listar_estudantes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
    """
        SELECT * FROM estudantes
    """
    )

    conn.commit()

    estudantes = cursor.fetchall()

    for estudante in estudantes:
        print(estudante)
        
    conn.close()

def criar_matricula(nome_disciplina, estudante_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO matriculas (nome_disciplina, estudante_id)
        VALUES (?, ?)
        """, (nome_disciplina, estudante_id)
        
    )

    conn.commit()
    conn.close()

def listar_matriculas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
    """
        SELECT * FROM matriculas
    """
    )
    conn.commit()

    matriculas = cursor.fetchall()

    for matricula in matriculas:
        print(matricula)
        
    conn.close()

def listar_matriculas_join():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT matriculas.id, estudantes.nome, matriculas.nome_disciplina
        FROM matriculas
        JOIN estudantes
            ON matriculas.estudante_id = estudantes.id
        """
    )

    matriculas = cursor.fetchall()

    for matricula in matriculas:
        print(matricula)

    conn.close()