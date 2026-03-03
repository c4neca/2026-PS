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
# ==== ADICIONAR NOVOS PRODUTOS ====
#================================================

continuar = "s"

while continuar == "s": #Se o cliente quiser, adiciona um novo produto a lista
    print("\nDeseja adicionar um novo produto? (s/n)")
    continuar = input().lower() #transforma a entrada em minúsculo para padrozinação

    if continuar == "s": 
        nome = input("Digite o nome do produto: ") #Se o cliente desejar, cadastrar produto peo nome

# ==== VALIDAÇÃO DA QUANTIDADE ====
        while True:
            try:
                quantidade = int(input("Digite a quantidade em estoque: "))

                if quantidade < 0: # Valida se a quantidade é um número maior que zero
                    print("⚠️ A quantidade não pode ser negativa.")
                else:
                    break

            except ValueError: #e um número inteiro
                print("⚠️ Entrada inválida. Digite apenas números inteiros.")

estoque.append({"nome": nome, "quantidade": quantidade}) #cadastra o produto na lista
print("✅ Produto adicionado com sucesso!")


#================================================
# ==== RELATÓRIO FINAL DO ESTOQUE ====
#================================================

print("\n=== RELATÓRIO DE ESTOQUE ===\n")

for produto in estoque:
# Traz o relatório do estoque baseado nos critérios
    nome = produto["nome"]
    quantidade = produto["quantidade"]

    if quantidade < 5:
        situacao = "Crítico"
    elif 5 <= quantidade <= 20:
        situacao = "Adequado"
    else:
        situacao = "Excesso"

# Mostra nome, quantidade e situação
print(f"Produto : {nome}")
print(f"Quantidade: {quantidade}")
print(f"Situação : {situacao}")
print("-" * 35)


#================================================
# ==== PRODUTO COM MENOR ESTOQUE ====
#================================================

# Baseando-se no primeiro valor, compara qual o produto com menor estoque
menor_quantidade = estoque[0]["quantidade"]
produto_critico = estoque[0]["nome"]

for produto in estoque:
    if produto["quantidade"] < menor_quantidade:
        menor_quantidade = produto["quantidade"]
        produto_critico = produto["nome"]

        print("\n=== PRODUTO COM MENOR ESTOQUE ===")
        print(f"Produto : {produto_critico}")
        print(f"Quantidade: {menor_quantidade}")
