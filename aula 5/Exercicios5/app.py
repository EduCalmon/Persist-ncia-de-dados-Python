from db_loja import criar_tabela_produto, inserir_produto, listar_produtos

while (True):
    print("\n1.Criar Tabela de Produto\n 2.Inserir produto\n 3.Listar produto\n 4.Sair")
    entrada = int(input("Digite a execução: "))

    if entrada == 4:
        print("Obrigado por usar o programa!")
        break

    elif entrada == 1:
        criar_tabela_produto()
        print("Tabela criada!")

    elif entrada == 2:
        produto_nome = input("Digite o nome do produto: ")
        produto_preco = int(input("Digite o Preço do produto: "))
        inserir_produto(produto_nome,produto_preco)
        print("Produto criado!")

    elif entrada == 3:
        listar_produtos()
        print("Produtos listados!")

    else:
        print("Digite uma opção válida!")