# ================================================
# SISTEMA DE BIBLIOTECA
#=================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 05 - Revisão: Estruturas de Dados
# Autor      : Ana Vitória Schactae Brandão
# Data       : 26/02/2026
# Repositório: https://github.com/c4neca/2026-PS.git
#=================================================


# ================================================
# LISTAS: CONCEITO BÁSICO
# ================================================

# Criando uma lista com alguns títulos de livros
titulos = [
    "O Programador Pragmático",
    "Código Limpo",
    "Entendendo Algoritmos",
]

# Acessando elementos da lista usando índice
# lembrando que em Python o índice começa em 0
print("Primeiro livro:", titulos[0])
print("Último livro  :", titulos[-1])  # índice -1 pega o último elemento
print("Total de livros:", len(titulos))  # len() mostra o tamanho da lista


# ================================================
# OPERAÇÕES NA LISTA
# ================================================

print("\n--- Operações na lista ---")

# Adicionando um novo título no final da lista
titulos.append("Python Fluente")
print("Após append:", titulos)

# Verificando se um título existe na lista
busca = "Código Limpo"
if busca in titulos:
    print(f'"{busca}" está no catálogo.')
else:
    print(f'"{busca}" não encontrado.')

# Ordenando a lista em ordem alfabética
titulos.sort()
print("Lista ordenada:", titulos)

# Removendo um item específico da lista
titulos.remove("Entendendo Algoritmos")
print("Após remove:", titulos)


# ================================================
# DICIONÁRIOS: CONCEITO BÁSICO
# ================================================

# Criando um dicionário que representa um livro
# cada informação é armazenada em uma chave
livro = {
    "titulo": "O Programador Pragmático",
    "autor": "Andrew Hunt",
    "ano": 1999,
    "disponivel": True,
}

# Acessando valores do dicionário pelas chaves
print("Titulo :", livro["titulo"])
print("Autor  :", livro["autor"])
print("Ano    :", livro["ano"])

# Exibindo o status do livro usando operador condicional
print("Status :", "Disponível" if livro["disponivel"] else "Emprestado")


# ================================================
# MODIFICANDO E CONSULTANDO DICIONÁRIOS
# ================================================

# Alterando o valor da chave "disponivel"
# simulando que o livro foi emprestado
livro["disponivel"] = False

# .get() permite acessar uma chave sem gerar erro
# caso ela não exista no dicionário
print("Páginas:", livro.get("paginas", "Não informado"))

# Outro exemplo de uso do .get()
editora = livro.get("editora", "Não informa")
print("Editora:", editora)


# ================================================
# CATÁLOGO: LISTA DE DICIONÁRIOS
# ================================================

# Cria um catálogo com vários livros
catalogo = [
    {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt", "ano": 1999, "disponivel": True},
    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "ano": 2008, "disponivel": True},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "ano": 2017, "disponivel": False},
]

print("\n=== Catálogo da Biblioteca ===")
print()

# Percorre todos os livros do catálogo
for livro in catalogo:
    status = "Disponível" if livro["disponivel"] else "Emprestado"
    print(f'     {livro["titulo"]} ({livro["ano"]})')
    print(f'     Autor: {livro["autor"]} | {status}')
    print("  " + "-" * 40)


# ================================================
# CONSULTAS E FILTROS
# ================================================

print("\n=== Livros disponíveis ===")

# Mostrando apenas os livros que estão disponíveis
for livro in catalogo:
    if livro["disponivel"]:
        print(f'    {livro["titulo"]}')

print("\n=== Busca por titulo ===")

# Usuário digita parte do título que deseja buscar
busca = input("Digite o título (ou parte): ").lower()
encontrado = False

# Percorre o catálogo procurando o termo digitado
for livro in catalogo:
    if busca in livro["titulo"].lower():
        print(f'  Encontrado: {livro["titulo"]} - {livro["autor"]}')
        encontrado = True

# Caso nenhum livro seja encontrado
if not encontrado:
    print("  Nenhum livro encontrado com esse termo.")


# ================================================
# ATRIBUTOS DO PRIMEIRO LIVRO
# ================================================

print("\n=== Atributos do primeiro livro ===")

# .items() retorna chave e valor do dicionário
for chave, valor in catalogo[0].items():
    print(f"   {chave}: {valor}")


# ================================================
# CADASTRO DE NOVO LIVRO
# ================================================

print("\n=== Cadastro de novo livro ===")

# Usuário informa os dados do novo livro
titulo = input("Título do livro: ")
autor = input("Autor do livro: ")
ano = int(input("Ano de publicação: "))

# Criando um novo dicionário com os dados informados
novo_livro = {
    "titulo": titulo,
    "autor": autor,
    "ano": ano,
    "disponivel": True
}

# Adicionando o novo livro ao catálogo
catalogo.append(novo_livro)

print("\n=== Catálogo atualizado ===")

# Exibindo novamente o catálogo com o novo livro
for livro in catalogo:
    status = "Disponível" if livro["disponivel"] else "Emprestado"
    print(f'     {livro["titulo"]} ({livro["ano"]})')
    print(f'     Autor: {livro["autor"]} | {status}')
    print("  " + "-" * 40)


# ================================================
# BUSCA POR AUTOR
# ================================================

print("\n=== Busca por autor ===")

# Usuário digita o nome do autor ou parte dele
busca_autor = input("Digite o autor (ou parte do nome): ").lower()
encontrado = False

# Procura todos os livros daquele autor
for livro in catalogo:
    if busca_autor in livro["autor"].lower():
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f'  {livro["titulo"]} - {livro["autor"]} | {status}')
        encontrado = True

# Caso nenhum livro seja encontrado
if not encontrado:
    print("  Nenhum livro encontrado desse autor.")


# ================================================
# REGISTRO DE EMPRÉSTIMO / DEVOLUÇÃO
# ================================================

print("\n=== Registro de empréstimo / devolução ===")

# Entrada para determinar o título do livro
titulo_busca = input("Digite o título do livro: ").lower()
encontrado = False

# Procura o livro e altera o status se disponível ou não 
for livro in catalogo:
    if titulo_busca in livro["titulo"].lower():

        # alterna o valor de True e False
        livro["disponivel"] = not livro["disponivel"]

        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f'  Status atualizado: {livro["titulo"]} agora está {status}')
        encontrado = True

# Caso o título não exista no catálogo
if not encontrado:
    print("  Livro não encontrado no catálogo.")


# ================================================
# RELATÓRIO FINAL
# ================================================

print("\n=== Relatório final ===")

# Calcula totais
total = len(catalogo)
disponiveis = 0
emprestados = 0

# Conta os livros disponíveis e emprestados
for livro in catalogo:
    if livro["disponivel"]:
        disponiveis += 1
    else:
        emprestados += 1

print("Total de livros :", total)
print("Disponíveis     :", disponiveis)
print("Emprestados     :", emprestados)

print("\nLivros emprestados:")

# Lista os livros que estão emprestados
for livro in catalogo:
    if not livro["disponivel"]:
        print(" -", livro["titulo"])