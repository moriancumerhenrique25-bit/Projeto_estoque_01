"""
V 1.1
Desenvolvido em Sorocaba - SP
Cliente Mercado 
Dsenvolvedores:
Enzo Soares Matias 
Henrique M.S Felipe
Hudson ferreira

Desenvolvemos um sistema de controle de estoque voltado para as necessidades de um mercado, incorporando as seguintes funções:
- Tela de login
- Menu estoque
- Lista de produtos
- Adicionar produtos
- Remover produtos
- Realizar venda
- Fechar Sistema

"""


#IMPORTA CLASSE DO ARQUIVO SISTEMA.PY NA MESMA PASTA
from sistema import Sistema

# BLOCO 1 - INSTÂNCIA DA CLASSE E VARIÁVEIS
sistema = Sistema()
produto = sistema.produto
somar = sistema.somar
ativo = sistema.ativo

# BLOCO 2 - VARIÁVEL PARA CONTROLAR O PRÓXIMO ID
prox_id = max(produto.keys()) + 1

# BLOCO 3 - TELA DE LOGIN
usuario = input("Usuário: ")
senha = input("Senha: ")

# BLOCO 4 - AUTENTICAÇÃO DE USUÁRIO
if usuario == "admin" and senha == "123" and ativo:
    print("Bem-vindo ao sistema!\n")

    # BLOCO 5 - TELA MENU DE ESTOQUE COM WHILE
    while True:
        print("===== MENU ESTOQUE =====")
        print("1 - Listar produtos")
        print("2 - Adicionar produto")
        print("3 - Remover produto")
        print("4 - Realizar venda")
        print("5 - Relatório de vendas")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        # OPÇÃO 1 - LISTAR PRODUTOS
        if opcao == "1":
            for id_prod, info in produto.items():
                print(f"{id_prod}: {info['nome']} - Qtd: {info['quantidade']}")
            print()

        # OPÇÃO 2 - ADICIONAR PRODUTOS
        elif opcao == "2":
            print("\n=== Adicionar Produto ===")
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            valor = float(input("Valor: "))
            kilo = float(input("Peso (kg): "))

            produto[prox_id] = {
                "nome": nome,
                "quantidade": quantidade,
                "valor": valor,
                "kilo": kilo
            }
            print(f"Produto '{nome}' adicionado com sucesso!\n")
            prox_id += 1  # incrementa para o próximo produto

        # OPÇÃO 3 - REMOVER PRODUTOS
        elif opcao == "3":
            id_remover = int(input("ID do produto a remover: "))
            if id_remover in produto:
                del produto[id_remover]
                print("Produto removido!\n")
            else:
                print("ID não encontrado.\n")

        # OPÇÃO 4 - VENDA DE PRODUTOS
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

        # OPÇÃO 5 - RELATÓRIO DE VENDAS
        elif opcao == "5":
            print("\n=== Relatório de Vendas (Custo por produto) ===")
            for i in sorted(produto.keys()):
                p = produto[i]
                print(f"{i} - {p['nome']}: {somar(p['kilo'], p['valor'])}")
            print()

        # BLOCO 6 - SAIR DO SISTEMA
        elif opcao == "6":
            print("Saindo do sistema...\n")
            break

        else:
            print("Opção inválida!\n")

# BLOCO 7 - LOGIN INVÁLIDO
else:
    print("Falha no login.")