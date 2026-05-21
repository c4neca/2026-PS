"""
hotel_droids.py - Aula 23 (Programação de Sistemas, 2026)
Sistema de Hotel para Droids.
"""

import pickle


class Droid:
    def __init__(self, nome, tipo, serie, idade, peso, nome_do_dono, telefone, manutencao):
        self.nome = nome
        self.tipo = tipo
        self.serie = serie
        self.idade = idade
        self.peso = peso
        self.nome_do_dono = nome_do_dono
        self.telefone = telefone
        self.manutencao = manutencao
        self.hospedado = False

    def exibir(self):
        print(f"Nome           : {self.nome}")
        print(f"Tipo           : {self.tipo}")
        print(f"Série          : {self.serie}")
        print(f"Idade          : {self.idade}")
        print(f"Peso           : {self.peso} kg")
        print(f"Dono           : {self.nome_do_dono}")
        print(f"Telefone       : {self.telefone}")

        print(
            f"Hospedado      : "
            f"{'Sim' if self.hospedado else 'Não'}"
        )
        print(
            f"Manutenção OK  : "
            f"{'Sim' if self.manutencao else 'Não'}"
        )
        print(f"Diária         : "
              f"R$ {self.calcular_diaria():.2f}")
    def para_linha_txt(self):
        return (
            f"{self.nome};"
            f"{self.tipo};"
            f"{self.serie};"
            f"{self.idade};"
            f"{self.peso};"
            f"{self.nome_do_dono};"
            f"{self.telefone};"
            f"{self.manutencao};"
            f"{self.hospedado}"
        )
    def calcular_diaria(self):
        if self.idade <= 10:
            return 50
        elif self.idade <= 60:
            return 60
        elif self.idade <= 100:
            return 75
        elif self.idade > 1000:
            return 200
        else:
            return 150
    def registrar_entrada(self):
        if not self.manutencao:
            print(
                f"{self.nome} não pode entrar."
                "\nManutenção pendente."
            )
            return
        self.hospedado = True
        print(f"{self.nome} entrou no hotel.")
    def registrar_saida(self):
        if not self.hospedado:
            print(f"{self.nome} não está hospedado.")
            return
        self.hospedado = False
        print(f"{self.nome} saiu do hotel.")
    def atualizar_peso(self, novo_peso):
        self.peso = float(novo_peso)
        print(
            f"Peso de {self.nome} atualizado "
            f"para {self.peso} kg."
        )
# --------------------------------------------------
# SALVAR TXT
# --------------------------------------------------
def salvar_em_txt(droids, caminho):

    with open(caminho, "w", encoding="utf-8") as arquivo:

        for d in droids:
            arquivo.write(d.para_linha_txt() + "\n")

    print(f"{len(droids)} droid(s) salvo(s) em {caminho}")
# --------------------------------------------------
# CARREGAR TXT
# --------------------------------------------------
def carregar_de_txt(caminho):
    droids = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(";")
                if len(partes) >= 9:
                    droid = Droid(
                        partes[0],
                        partes[1],
                        partes[2],
                        int(partes[3]),
                        float(partes[4]),
                        partes[5],
                        partes[6],
                        partes[7] == "True"
                    )
                    droid.hospedado = (
                        partes[8] == "True"
                    )
                    droids.append(droid)
    except FileNotFoundError:
        print(
            f"Arquivo {caminho} ainda não existe."
        )
    return droids
# --------------------------------------------------
# SALVAR BINÁRIO
# --------------------------------------------------
def salvar_em_binario(droids, caminho):
    with open(caminho, "wb") as arquivo:
        pickle.dump(droids, arquivo)
    print(f"{len(droids)} droid(s) salvo(s) em {caminho}")
# --------------------------------------------------
# CARREGAR BINÁRIO
# --------------------------------------------------
def carregar_de_binario(caminho):
    try:
        with open(caminho, "rb") as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        print(
            f"Arquivo {caminho} ainda não existe."
        )
        return []
# --------------------------------------------------
# CADASTRAR
# --------------------------------------------------
def cadastrar(droids):
    print("\n--- Novo Droid ---")
    nome = input("Nome           : ")
    tipo = input("Tipo           : ")
    serie = input("Série          : ")
    idade = int(input("Idade          : "))
    peso = float(input("Peso (kg)      : "))
    nome_do_dono = input("Nome do dono   : ")
    telefone = input("Telefone       : ")
    manutencao = (
        input("Manutenção OK? (S/N): ").upper() == "S"
    )
    droids.append(
        Droid(nome, tipo, serie, idade, peso, nome_do_dono, telefone, manutencao)
    )

    print("Droid cadastrado.")
# --------------------------------------------------
# LISTAR
# --------------------------------------------------
def listar(droids):
    if not droids:
        print("\n(hotel vazio)")
        return
    print(f"\n--- Hotel ({len(droids)} droids) ---")
    for i, d in enumerate(droids, start=1):
        print(f"\n[{i}]")
        d.exibir()
# --------------------------------------------------
# REMOVER
# --------------------------------------------------
def remover(droids):
    listar(droids)
    if not droids:
        return
    try:
        indice = int(
            input("\nN° do droid a remover: ")
        ) - 1
        if 0 <= indice < len(droids):
            removido = droids.pop(indice)
            print(
                f"Droid '{removido.nome}' removido."
            )
        else:
            print("Índice inválido.")
    except ValueError:
        print("Digite um número válido.")
# --------------------------------------------------
# CHECK-IN
# --------------------------------------------------
def checkin(droids):
    listar(droids)
    if not droids:
        return
    try:
        indice = int(
            input("\nN° do droid para check-in: ")
        ) - 1
        if 0 <= indice < len(droids):
            droids[indice].registrar_entrada()
        else:
            print("Índice inválido.")
    except ValueError:
        print("Digite um número válido.")
# --------------------------------------------------
# CHECK-OUT
# --------------------------------------------------
def checkout(droids):
    listar(droids)
    if not droids:
        return
    try:
        indice = int(
            input("\nN° do droid para check-out: ")
        ) - 1
        if 0 <= indice < len(droids):
            droids[indice].registrar_saida()
        else:
            print("Índice inválido.")
    except ValueError:
        print("Digite um número válido.")
# --------------------------------------------------
# ATUALIZAR PESO
# --------------------------------------------------
def atualizar_peso(droids):
    listar(droids)
    if not droids:
        return
    try:
        indice = int(
            input("\nN° do droid: ")
        ) - 1
        if 0 <= indice < len(droids):
            novo_peso = float(
                input("Novo peso: ")
            )
            droids[indice].atualizar_peso(
                novo_peso
            )
        else:
            print("Índice inválido.")
    except ValueError:
        print("Digite um valor válido.")
# --------------------------------------------------
# MENU
# -------------------------------------------------
def menu():
    droids = carregar_de_binario("droids.bin")
    while True:
        print("\n========== HOTEL ==========")
        print("1 - Cadastrar droid")
        print("2 - Listar droids")
        print("3 - Remover droid")
        print("4 - Check-in")
        print("5 - Check-out")
        print("6 - Atualizar peso")
        print("7 - Salvar em .txt")
        print("8 - Salvar em binário")
        print("0 - Sair")
        opcao = input("Opção: ")
        if opcao == "1":
            cadastrar(droids)
        elif opcao == "2":
            listar(droids)
        elif opcao == "3":
            remover(droids)
        elif opcao == "4":
            checkin(droids)
        elif opcao == "5":
            checkout(droids)
        elif opcao == "6":
            atualizar_peso(droids)
        elif opcao == "7":
            salvar_em_txt(
                droids,
                "droids.txt"
            )
        elif opcao == "8":
            salvar_em_binario(
                droids,
                "droids.bin"
            )
        elif opcao == "0":
            salvar_em_binario(
                droids,
                "droids.bin"
            )
            print("Até logo!")
            break
        else:
            print("Opção inválida.")
if __name__ == "__main__":
    menu()