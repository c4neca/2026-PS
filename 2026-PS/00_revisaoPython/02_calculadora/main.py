#================================================
# Calculadora
#================================================
# Disciplina : Programação de Sistemas (PS)
# Autor : Ana Vitória Schactae Brandão
# Data : 28 de Maio de 2026
# Descrição : Programa de calculadora 
#================================================
#SOMA
# MENU
def menu():
    while True:
        print("\n======== CALCULADORA =========")
        print("1 - Soma")
        print("2 - Subtração")
        print("3- Divisão")
        print("4 - Multiplicação")
        print("5 - Sair da calculadora")
        
        opcao = int()
        if opcao == "5":
            break

        if opcao != (1, 2, 3, 4):
            print("Opção inválida! Tente novamente")
            continue
        
        try:
            A = int("Digite um valor A: ")
            B = int("Digite um valor B: ")
        except ValueError:
            print("Valor inválido")

        if opcao == 1:
            print("A soma é igual a: ", A + B)
        elif opcao == 2:
            if A > B:
                print("A subtração é igual a: ", A - B)
            else:
                print("A subtração é igual a: ", B - A)
        elif opcao == 3:
            print("A multiplicação é igual a: ", A*B)
        elif opcao == 4:
            print("A divisao é igual a: ", A/B)
    
menu()


