from pymongo import MongoClient

con = MongoClient("mongodb://localhost:27017/") # Conecta no Data base
db = con.get_database("Alura") # Conecta no banco de dados específico
colecao = db.get_collection("Contato") # Conecta na coleção

# nome = input("Digite seu nome: ")
# telefone = int(input("Digite seu telefone: "))

# dados = {
#     "Nome": nome,
#     "Telefone": telefone
#     }
# colecao.insert_one(dados)

contatos = list(colecao.find()) # printo todos os contatos do banco de dados
print(contatos)

contatos = list(colecao.find({"Nome": "Eduardo"})) # Pesquiso um específico
print(contatos)

colecao.update_one({"Nome": "Eduardo"}, {"$set": {"Idade:":19}}) # Altero a idade

colecao.delete_one({"Nome": "Rodolfo"}) # Exclui