'''
================================================================
# ARQUIVO   : pet.py
# DISCIPLINA: Programação de Sistemas (2026-2)
# AULA      : Aula 20 -- Por que POO?
# AUTOR     : Ana Vitória Schactae Brandão
# Conceitos : Classe, objeto, atributos, métodos, encapsulamento
# Atividade : Classe Pet
================================================================
'''
from time import sleep 
class Droid: # Agrupa os dados de um pet do sistema de hotel nessa classe
    def __init__(self, nome, tipo, serie, idade, peso, nome_do_dono, telefone, manutencao,  diaria):
        self.nome = nome
        self.tipo = tipo
        self.serie = serie
        self.idade = idade
        self.peso = peso
        self.nome_do_dono = nome_do_dono
        self.telefone = telefone
        self.hospedado = False
        self.manutencao = manutencao
        self.diaria = diaria
    def exibir_dados(self):
        print("\n=== Dados do Pet ===")
        print(f"Nome: {self.nome}")
        sleep(0.5)
        print(f"Tipo: {self.tipo}")
        sleep(0.5)
        print(f"Série: {self.serie}")
        sleep(0.5)
        print(f"Idade: {self.idade}")
        sleep(0.5)
        print(f"Peso: {self.peso}kg")
        sleep(0.5)
        print(f"Nome do dono: {self.nome_do_dono}")
        sleep(0.5)
        print(f"Telefone de contato: {self.telefone}")
        sleep(0.5)
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")
        sleep(0.5)
        print(f"Manutenção: {'Sim' if self.manutencao else 'Não'}")
        sleep(0.5)
        print(f"Diária: R${self.diaria:.2f}")
        sleep(0.5)
        
    def registrar_entrada(self):
        if self.manutencao == True:
            self.hospedado = True
            print(f"{self.nome} entrou no hotel.")

    def registrar_saida(self):
        if not self.hospedado:
            print(f"AVISO: Não é possível registrar saída. {self.nome} não está hospedado!")
            return
        self.hospedado = False
        print(f"{self.nome} saiu do hotel.")

    def calcular_diaria(self):
        if self.idade <= 10:
            return 50
        elif self.idade <= 60:
            return 60
        elif self.idade <=100:
            return 75
        elif self.idade > 1000:
            return 200
        else:
            return 150

    def verificar_manutencao(self):
        if self.manutencao == True:
            print(f"{self.nome} está com a manutenção em dia.")
        else:
            print(f"{self.nome} não está com a manutenção em dia.")
    
    def atualizar_peso(self, novo_peso):
        self.peso = novo_peso
        print(f"O peso de {self.nome} foi atualizado para {self.peso}kg")
    
    def emitir_resumo(self):
        valor_diaria = self.calcular_diaria()
        print(f"Resumo de {self.nome}: {self.tipo}, {self.serie}, {self.idade} anos, {self.peso}kg, {self.nome_do_dono}, {self.telefone}, Diária: R${valor_diaria:.2f}, Vacinação: {'Sim' if self.manutencao else 'Não'}")

    '''
    # =================================================================================
    # TESTES DA CLASSE
    # =================================================================================
    # Depois de completar a classe, crie pelo menos 3 objetos Pet.
    #
    # Exemplo:
    # droid1 = Droid("R2-D2", "Astromecânico", "Série R2", 66, 32.0, True)
    # droid2 = Droid("C-3PO", "Protocolo", "Série 3PO", 112, 77.0, False)
    # droid3 = Droid("BB-8", "Astromecânico", "Série BB", 5, 20.0, True)

    # Atenção:
    # Se você adicionou novos parâmetros no __init__, será necessário informar esses dados na criação do objeto.
    # =================================================================================
    '''
droid1 = Droid("R2-D2", "Astromecânico", "Série R2", 66, 32.0, "Padme", 999887777, True, 60.0)
droid2 = Droid("C-3PO", "Protocolo", "Série 3PO", 112, 77.0, "Anakin", 999776666, False, 75.0)
droid3 = Droid("BB-8", "Astromecânico", "Série BB", 5, 20.0, "Poe", 999667777, True, 50.0)
droid4 = Droid("Huyang", "Arquitetura", "Série Mk I", 25000, 55.0, "Ahsoka", 999554444, True, 200.0)
meus_droids = [droid1, droid2, droid3, droid4]

for droid in meus_droids:
    droid.exibir_dados()
    sleep(1)
    droid.verificar_manutencao()
    sleep(1)
    droid.registrar_entrada()
    sleep(1)
    print("\n=== Resumo ===")
    droid.emitir_resumo()
    print("===============")
    
    
print("\n Atualizando peso...\n")

droid1.atualizar_peso(30.0)
droid2.atualizar_peso(26.4)
droid3.atualizar_peso(22.0)
droid4.atualizar_peso(60.0)
