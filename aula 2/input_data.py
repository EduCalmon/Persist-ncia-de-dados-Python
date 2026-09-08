nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

with open('input-usuário.txt', 'a') as f: # O 'a' serve para adicionar no arquivo, pois sem isso voce escreve por cima
    f.write(f'Nome? {nome}\nIdade? {idade}')