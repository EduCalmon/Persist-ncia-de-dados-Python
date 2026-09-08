import json

dados = {'Nome': 'Eduardo', 'Idade': '18', 'Endereço': 'Rua a'}

with open('Dados Eduardo.json', 'w') as f:
    json.dump(dados, f) # crio um arquivo json
    
