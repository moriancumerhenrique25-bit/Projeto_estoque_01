"""
V 1.1
Desenvolvido em Sorocaba - SP
Cliente Mercado 
Dsenvolvedores:
Enzo Soares Matias 
Henrique M.S Felipe
Hudson  L. Ferreira
Gabriel terci
Pedro Poiato

Desenvolvemos um sistema de controle de estoque voltado para as necessidades de um mercado, incorporando as seguintes funções:
- Tela de login
- Menu estoque
- Lista de produtos
- Adicionar produtos
- Remover produtos
- Realizar venda
- Fechar Sistema

Tela de uso
===== MENU ESTOQUE =====
1 - Listar produtos
2 - Adicionar produto
3 - Remover produto
4 - Realizar venda
5 - Relatório de vendas
6- voltar para menu
7 - Sair
Escolha uma opção:

"""

# BLOCO 1 - LISTAS DE PRODUTOS
produto = {
    1: {"nome": "morango", "quantidade": 20, "valor": 15, "kilo": 150},
    2: {"nome": "manga", "quantidade": 15, "valor": 10, "kilo": 5},
    3: {"nome": "limao", "quantidade": 30, "valor": 5, "kilo": 3},
    4: {"nome": "maracuja", "quantidade": 50, "valor": 10, "kilo": 6},
    5: {"nome": "kiwi", "quantidade": 20, "valor": 20, "kilo": 10},
    6: {"nome": "abacate", "quantidade": 40, "valor": 12, "kilo": 10},
    7: {"nome": "abacaxi", "quantidade": 30, "valor": 35, "kilo": 10},
    8: {"nome": "mamao", "quantidade": 20, "valor": 10, "kilo": 20},
    9: {"nome": "laranja", "quantidade": 60, "valor": 10, "kilo": 30},
    10: {"nome": "ameixa", "quantidade": 10, "valor": 15, "kilo": 6},
}

# BLOCO 2 - DEF CUSTO
def somar(kilo,quantidade):
  custo = kilo * quantidade
  return custo

#BLOCO 3 - DEF LISTAR PRODUTOS
def listar_prod():
    for id_prod, info in produto.items():
        print(f"{id_prod}: {info['nome']} - Qtd: {info['quantidade']}")
    print()

# BLOCO 4 - TELA DE LOGIN
usuario = input("Usuário: ")
senha = input("Senha: ")
ativo = True

# BLOCO 5 - AUTENTIFICAÇÃO DE USUÃRIO COM IF
if usuario == "admin" and senha == "123" and ativo:
    print("Bem-vindo ao sistema!")

    #BLOCO 6 - TELA MENU DE ESTOQUE COM WHILE
    while True:
        print("===== MENU ESTOQUE =====")
        print("1 - Listar produtos")
        print("2 - Adicionar produto")
        print("3 - Remover produto")   
        print("4 - Realizar venda")
        print("5 - Relatório de vendas")
        print("6- voltar para menu")
        print("7 - Sair")
        opcao = input("Escolha uma opção: ")

        # OPÇÃO 1 - LISTAR PRODUTOS IF
        if opcao == "1":
            listar_prod()

        # OPÇÃO 2 - ADICIONAR PRODUTOS COM ELIF
        elif opcao == "2":
            print("\n=== Adicionar Produto ==...")
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            valor = float(input("Valor: "))
            kilo = float(input("Peso (kg): "))

            novo_id = max(produto.keys()) + 1
            produto[novo_id] = {
                "nome": nome,
                "quantidade": quantidade,
                "valor": valor,
                "kilo": kilo
            }

            print(f"Produto '{nome}' adicionado com sucesso!\n")

        # OPÇÃO 3 - REMOVER PRODUTOS ELIF/IF/DEL/ELSE
        elif opcao == "3":
            id_remover = int(input("ID do produto a remover: "))
            if id_remover in produto:
                del produto[id_remover]
                print("Produto removido!\n")
            else:
                print("ID não encontrado.\n")

        # OPÇÃO 4 - VENDA DE PRODUTOS ELIF/IF/ELSE
        elif opcao == "4":
            print("\n=== Realizar Venda ===")
            id_venda = int(input("Informe o ID do produto: "))
            if id_venda in produto:
                qtd_venda = int(input("Quantidade a vender: "))
                if qtd_venda <= produto[id_venda]["quantidade"]:
                    produto[id_venda]["quantidade"] -= qtd_venda
                    print(f"Venda realizada: {qtd_venda} unidade(s) de '{produto[id_venda]['nome']}'\n")
                else:
                    print("Estoque insuficiente.\n")
            else:
                print("ID do produto não encontrado.\n")

            # OPÇÃO 5 - LISTA DE VENDAS REALIZADAS
        elif opcao == "5":
             print(somar(produto[1]["kilo"],produto[1]["valor"]))
             print(somar(produto[2]["kilo"],produto[2]["valor"]))
             print(somar(produto[3]["kilo"],produto[3]["valor"]))
             print(somar(produto[4]["kilo"],produto[4]["valor"]))
             print(somar(produto[5]["kilo"],produto[5]["valor"]))
             print(somar(produto[6]["kilo"],produto[6]["valor"]))
             print(somar(produto[7]["kilo"],produto[7]["valor"]))
             print(somar(produto[8]["kilo"],produto[8]["valor"]))
             print(somar(produto[9]["kilo"],produto[9]["valor"]))
             print(somar(produto[10]["kilo"],produto[10]["valor"]))
            
        # BLOCO 7 - SAIR DO SISTEMA
        elif opcao == "6":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!\n")
else:
    print("Falha\xa0no\xa0login.")
