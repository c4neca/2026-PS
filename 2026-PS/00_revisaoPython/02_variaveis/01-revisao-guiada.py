#================================================
# SISTEMA DE APROVAÇÃO DE ALUNO
#================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 04 - Revisão: Variáveis, Tipos e Controle de Fluxo
# Autor      : Ana Vitória Schactae Brandão
# Data       : 24 de Fevereiro de 2026
# Repositório: https://github.com/c4neca/2026-PS
#================================================

# ==== DADOS DA TURMA ====
# Uma lista de dicionários: cada dicionário representa um aluno 

turma = [
    {"nome": "Ana",     "nota1": 8.0,  "nota2": 7.5},
    {"nome": "Bruno",   "nota1": 4.5,  "nota2": 5.0},
    {"nome": "Clara",   "nota1": 2.0,  "nota2": 3.5},
]

print("=== Resultado da Turma ===")
print()

# O 'for' percorre cada aluno da lista automaticamente
for aluno in turma:
    nome  = aluno["nome"]
    nota1 = aluno["nota1"]
    nota2 = aluno["nota2"]
    media = (nota1 + nota2) / 2

    if media >= 6.0:
        situacao = "✅ Aprovado"
    elif media >= 4.0:
        situacao = "⚠️ Recuperação"
    else:
        situacao = "❌ Reprovado"
    
    print(f"Aluno   : {nome}")
    print(f"Média   : {media:.2f}")
    print(f"Situação: {situacao}")
    print("-" * 30)

# ==== PROCESSAR NOVOS ALUNOS ====

continuar = "s"

while continuar == "s":
    print("\nDeseja processar outro aluno? (s/n)")
    continuar = input().lower()

    if continuar == "s":
        # Entrada de dados
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a nota 1 (0 a 10): "))
        nota2 = float(input("Digite a nota 2 (0 a 10): "))

        # Cálculo da média
        media = (nota1 + nota2) / 2

        # ==== DECISÃO ====
        if media >= 6.0:
            situacao = "✅ Aprovado"
        elif media >= 4.0:
            situacao = "⚠️ Recuperação"
        else:
            situacao = "❌ Reprovado"

        # Saída de dados
        print(f"\nAluno   : {nome}")
        print(f"Média   : {media:.2f}")
        print(f"Situação: {situacao}")
        print("-" * 40)