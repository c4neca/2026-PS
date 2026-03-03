# Arquivo: 01b-debug.py
# ATENÇÃO: Este código contém 4 erros propositais. Encontre e corrija todos!

# Arquivo: 01b-debug.py
# ATENÇÃO: Este código contém 4 erros propositais. Encontre e corrija todos!

nome = input("Digite o nome do aluno: ") # CORREÇAO 1: SyntaxError "imput" escrito incorretamente
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2  # CORREÇÃO 2: adicionei parênteses para calcular a média corretamente

if media >= 6.0:
    situacao = "Aprovado"
elif media >= 4.0:
    situacao = "Recuperação"
else:  # CORREÇÃO 3: corrigi a indentação do else (estava desalinhado)
    situacao = "Reprovado"

print(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}") # CORREÇAO 4: SyntaxError "pront" escrito incorretamente