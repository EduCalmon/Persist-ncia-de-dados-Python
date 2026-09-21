import sqlite3

def conectar_banco():
    conn = sqlite3.connect('loja.db')
    return conn

def criar_tabela_produto():
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            preco INTEGER
            )
        """
    )
    conn.commit()
    conn.close()

def inserir_produto(nome, preco):
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute(
        """
            INSERT INTO produtos (nome, preco)
            VALUES (?,?)
        """,(nome, preco)
    )

    conn.commit()
    conn.close()

def listar_produtos():
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT * FROM produtos
        """
    )

    produtos = cursor.fetchall()

    for produto in produtos:
        print(produto)

    conn.close()