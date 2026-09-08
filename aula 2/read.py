#Para ler o que tem dentro de um arquívo
with open('texto.txt', 'r') as f:
    conteudo = f.read()
    
print(conteudo)