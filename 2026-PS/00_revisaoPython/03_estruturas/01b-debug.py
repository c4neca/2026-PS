# Arquivo: 01b-debug.py
# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!

catalogo = [
    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "disponivel": True},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "disponivel": False},
    {"titulo": "Python Fluente", "autor": "Luciano Ramalho", "disponivel": True},
]

# 1. O índice 3 não existe, pois a lista tem posições 0, 1 e 2.
print("Primeiro livro:", catalogo[2]["titulo"])

print("\nLivros disponíveis:")

for livro in catalogo:
# 2. A condição está verificando == False, mas está pedindo livros disponíveis (True).
    if livro["disponivel"] == True:
        print(f"  {livro['titulo']}")

total = len(catalogo)
print(f"\nTotal de livros: {total}")

# 3. Faltou .items() para percorrer chave e valor.
for chave, valor in catalogo[0].items():
    print(f"  {chave}: {valor}")

# 4. A chave está escrita com letra maiúscula mas foi definida em minúsculo
primeiro_autor = catalogo[0]["autor"]

print("\nAutor do primeiro livro:", primeiro_autor)