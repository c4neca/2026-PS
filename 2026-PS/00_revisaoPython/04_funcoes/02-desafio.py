#================================================
# SISTEMA DE APROVAÇÃO DE ALUNO
#================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 06 - Revisão: Funções, Parâmetros, Retorno e Escopo
# Autor      : Ana Vitória Schactae Brandão
# Data       : 09/03/2026
# Repositório: https://github.com/c4neca/2026-PS
#================================================


# =================================================
# FUNÇÃO: calcular_media
# recebe duas notas e mostra a média
# =================================================
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2   # calcula a média das duas notas
    return media                  # retorna o valor da média


# =================================================
# FUNÇÃO: verificar_situacao
# recebe a média e mostra a situação do aluno
# =================================================
def verificar_situacao(media):

    # se média maior ou igual a 6 == aprovado
    if media >= 6.0:
        return "✅ Aprovado"

    # se média entre 4 e 5.9 == recuperação
    elif media >= 4.0:
        return "⚠️ Recuperação"

    # caso contrário == reprovado
    else:
        return "❌ Reprovado"


# =================================================
# FUNÇÃO: solicitar_notas
# pede as notas e valida se estão entre 0 e 10
# =================================================
def solicitar_notas(nome_aluno):

    print(f"\nDigite as notas de {nome_aluno}")

    # pede a primeira nota
    nota1 = float(input("Digite a nota 1 (0 a 10): "))

    # valida a nota
    while nota1 < 0 or nota1 > 10:
        print("Nota inválida. Digite um valor entre 0 e 10.")
        nota1 = float(input("Digite a nota 1 novamente: "))

    # pede a segunda nota
    nota2 = float(input("Digite a nota 2 (0 a 10): "))

    # valida a nota
    while nota2 < 0 or nota2 > 10:
        print("Nota inválida. Digite um valor entre 0 e 10.")
        nota2 = float(input("Digite a nota 2 novamente: "))

    # retorna as duas notas validadas
    return nota1, nota2


# =================================================
# FUNÇÃO: gerar_relatorio
# recebe os dados e mostra o resultado formatado
# =================================================
def gerar_relatorio(nome, media, situacao):

    print(f"Aluno   : {nome}")        # mostra o nome do aluno
    print(f"Média   : {media:.2f}")   # mostra a média com duas casas
    print(f"Situação: {situacao}")    # mostra a situação
    print("-" * 30)                  # linha separadora



# =================================================
# ==== DADOS DA TURMA ====
# lista de dicionários representando alunos
# =================================================

turma = [
    {"nome": "Ana",     "nota1": 8.0,  "nota2": 7.5},
    {"nome": "Bruno",   "nota1": 4.5,  "nota2": 5.0},
    {"nome": "Clara",   "nota1": 2.0,  "nota2": 3.5},
]

print("=== Resultado da Turma ===")
print()


# =================================================
# percorre automaticamente cada aluno da lista
# =================================================
for aluno in turma:

    nome  = aluno["nome"]   # pega o nome do aluno
    nota1 = aluno["nota1"]  # pega a primeira nota
    nota2 = aluno["nota2"]  # pega a segunda nota

    # chama a função que calcula a média
    media = calcular_media(nota1, nota2)

    # chama a função que verifica a situação
    situacao = verificar_situacao(media)

    # chama a função que retorna o relatório
    gerar_relatorio(nome, media, situacao)



# =================================================
# ==== PROCESSAR NOVOS ALUNOS ====
# =================================================

continuar = "s"   # variável de controle do loop


# loop que permite cadastrar novos alunos
while continuar == "s":

    print("\nDeseja processar outro aluno? (s/n)")
    continuar = input().lower()   # lê a resposta e transforma em minúsculo


    if continuar == "s":

        # pede o nome do aluno
        nome = input("Digite o nome do aluno: ")

        # chama a função que solicita e valida as notas
        nota1, nota2 = solicitar_notas(nome)

        # calcula a média
        media = calcular_media(nota1, nota2)

        # verifica a situação
        situacao = verificar_situacao(media)

        # mostra o relatório
        gerar_relatorio(nome, media, situacao)