import json

with open('Dados Eduardo.json', 'r') as f:
    dados_lidos = json.load(f) # Aui vou ler o que tem no arquívo json
    print(dados_lidos)