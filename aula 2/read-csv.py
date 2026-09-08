import csv

with open('dados.csv', newline='') as f: # tem que usar newline=
    leitor = csv.reader(f) # função csv para ler o arquivo csv
    for linha in leitor:
        print(linha)