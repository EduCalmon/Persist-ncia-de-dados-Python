from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/") # Conecta no Data base
db = client["escola"]
estudantes = db["estudantes"]

estudantes.insert_one({"nome": "Stefani", "idade": 20})

for estudante in estudantes.find():
    print(estudante)