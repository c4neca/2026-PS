#================================================
# SISTEMA DE CONTROLE DE ESTOQUE
#================================================
# Disciplina : Programação de Sistemas (PS)
# Aula : 04 - Revisão: Variáveis, Tipos e Controle de Fluxo
# Autor : Ana Vitória Schactae Brandão
# Data : 26 de Fevereiro de 2026
# Descrição : Programa que controla o estoque de produtos
# e classifica conforme a quantidade disponível.
#
# Critérios:
# - Crítico -> menos de 5 unidades
# - Adequado -> entre 5 e 20 unidades
# - Excesso -> mais de 20 unidades
#================================================


#================================================
# ==== LISTA INICIAL DE PRODUTOS ====
#================================================

estoque = [ #Armazena os três produtos em uma lista
{"nome": "Teclado", "quantidade": 3},
{"nome": "Mouse", "quantidade": 12},
{"nome": "Monitor", "quantidade": 30},
]


#================================================
# ==== RELATÓRIO DO ESTOQUE ====
#================================================

print("\n=== RELATÓRIO DE ESTOQUE ===\n")

# Contadores para o resumo geral
contador_critico = 0
contador_adequado = 0
contador_excesso = 0

for produto in estoque:
# Traz o relatório do estoque baseado nos critérios
    nome = produto["nome"]
    quantidade = produto["quantidade"]

    if quantidade < 5:
        situacao = "Crítico"
        contador_critico += 1
    elif 5 <= quantidade <= 20:
        situacao = "Adequado"
        contador_adequado += 1
    else:
        situacao = "Excesso"
        contador_excesso += 1

# Mostra nome, quantidade e situação
    print(f"Produto : {nome}")
    print(f"Quantidade: {quantidade}")
    print(f"Situação : {situacao}")
    print("-" * 35)


#================================================
# ==== RESUMO GERAL DO ESTOQUE ====
#================================================

print("\n=== RESUMO GERAL ===")
print(f"Crítico  : {contador_critico}")
print(f"Adequado : {contador_adequado}")
print(f"Excesso  : {contador_excesso}")


#================================================
# ==== CONSULTAR PRODUTO ESPECÍFICO ====
#================================================

while True:
    print("\nDeseja consultar um produto pelo nome? (s/n)")
    consulta = input().lower()

    if consulta == "n":
        break

    nome_busca = input("Digite o nome do produto: ").lower()
    encontrado = False

    for produto in estoque:
        if produto["nome"].lower() == nome_busca:
            quantidade = produto["quantidade"]

            if quantidade < 5:
                situacao = "Crítico"
            elif quantidade <= 20:
                situacao = "Adequado"
            else:
                situacao = "Excesso"

            print(f"\nProduto : {produto['nome']}")
            print(f"Quantidade: {quantidade}")
            print(f"Situação : {situacao}")
            encontrado = True
            break

    if not encontrado:
        print("Produto não encontrado no estoque.")


#================================================
# ==== ADICIONAR NOVOS PRODUTOS ====
#================================================

continuar = "s"

while continuar == "s": #Se o cliente quiser, adiciona um novo produto a lista
    print("\nDeseja adicionar um novo produto? (s/n)")
    continuar = input().lower() #transforma a entrada em minúsculo para padrozinação

    if continuar == "s": 
        nome = input("Digite o nome do produto: ") #Se o cliente desejar, cadastrar produto pelo nome

# ==== VALIDAÇÃO DA QUANTIDADE ====
        while True:
            try:
                quantidade = int(input("Digite a quantidade em estoque: "))

                if quantidade < 0: # Valida se a quantidade é um número maior que zero
                    print("A quantidade não pode ser negativa.")
                else:
                    break

            except ValueError: #é um número inteiro
                print("Entrada inválida. Digite apenas números inteiros.")

        estoque.append({"nome": nome, "quantidade": quantidade}) #cadastra o produto na lista
        print("Produto adicionado com sucesso!")


#================================================
# ==== PRODUTO COM MENOR ESTOQUE ====
#================================================

# Baseando-se no primeiro valor, compara e mostra qual o produto com menor estoque
menor_quantidade = estoque[0]["quantidade"]
produto_critico = estoque[0]["nome"]

for produto in estoque:
    if produto["quantidade"] < menor_quantidade:
        menor_quantidade = produto["quantidade"]
        produto_critico = produto["nome"]

print("\n=== PRODUTO COM MENOR ESTOQUE ===")
print(f"Produto : {produto_critico}")
print(f"Quantidade: {menor_quantidade}")