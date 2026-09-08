import csv

#escrever uma planilha
with open('dados.csv', 'w') as f:
    escritor = csv.writer(f) # crio um escritor csv
    escritor.writerow(['Nome', 'Idade']) # Cria linha
    escritor.writerow(['Ana', '32'])