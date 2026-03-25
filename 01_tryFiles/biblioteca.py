"""
Sistema de Biblioteca - v2

Autor: Ana Vitória Schactae Brandão
Descrição:
Sistema de gerenciamento de biblioteca com persistência em arquivo .txt.

Formato do arquivo:
titulo|autor|disponivel
"""

# Centralizar o nome evita erros de digitação em todo o código
ARQUIVO = "01_tryFiles/biblioteca.txt"

SEPARADOR = "|"  # separa campos em cada linha do .txt


def carregar_catalogo():
        """Lê o .txt e reconstrói a lista de dicionários."""

        catalogo = []

        try:
                # 'r' = leitura | encoding='utf-8' garante acentos corretos
                with open(ARQUIVO, "r", encoding="utf-8") as f:

                        for linha in f:
                                linha = linha.strip()

                                if not linha:            # ignora linhas vazias
                                        continue

                                partes = linha.split(SEPARADOR)

                                if len(partes) != 3:     # linha malformada → pula
                                        continue

                                titulo, autor, disponivel_str = partes

                                catalogo.append({
                                        "titulo": titulo,
                                        "autor": autor,
                                        # string "True" → booleano True
                                        "disponivel": disponivel_str == "True"
                                })

        except FileNotFoundError:
                pass    # primeira execução: arquivo ainda não existe — tudo bem

        return catalogo


def salvar_catalogo(catalogo):
        """Grava toda a lista no arquivo .txt."""

        try:
                # 'w' = write: cria se não existir, sobrescreve se existir
                with open(ARQUIVO, "w", encoding="utf-8") as f:

                        for livro in catalogo:
                                linha = f"{livro['titulo']}{SEPARADOR}{livro['autor']}{SEPARADOR}{livro['disponivel']}\n"
                                f.write(linha)

                print(f"💾 Catálogo salvo em '{ARQUIVO}'.")

        except IOError as e:
                # IOError: disco cheio, permissão negada, etc.
                print(f"❌ Erro ao salvar: {e}")


def listar_livros(catalogo):
        print("\n--- Catálogo de Livros ---")
        if not catalogo:
                print(" O catálogo está vazio.")
                return
        for i, livro in enumerate(catalogo, 1):
                status = " Disponível" if livro["disponivel"] else " Emprestado"
                print(f"{i}. {livro['titulo']} - {livro['autor']} [{status}]")


def adicionar_livro(catalogo):
        print("\n--- Adicionar Novo Livro ---")
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()

        catalogo.append({
                "titulo": titulo,
                "autor": autor,
                "disponivel": True
        })

        salvar_catalogo(catalogo)

        print(f" Livro '{titulo}' adicionado!")


def buscar_livro(catalogo):
        print("\n--- Buscar Livro ---")
        termo = input("Digite o título para busca: ").lower()

        encontrados = [l for l in catalogo if termo in l["titulo"].lower()]

        if encontrados:
                for l in encontrados:
                        print(f" Encontrado: {l['titulo']} - {l['autor']}")
        else:
                print(" Nenhum livro encontrado.")


def registrar_emprestimo(catalogo):
        listar_livros(catalogo)
        if not catalogo: return
        try:
                indice = int(input("\nNúmero do livro para empréstimo: ")) - 1
                if catalogo[indice]["disponivel"]:
                        catalogo[indice]["disponivel"] = False
                        salvar_catalogo(catalogo)
                        print(f" Empréstimo de '{catalogo[indice]['titulo']}' realizado!")
                else:
                        print(" Este livro já está emprestado.")
        except (ValueError, IndexError):
                print(" Opção inválida.")


def devolver_livro(catalogo):
        listar_livros(catalogo)
        if not catalogo: return
        try:
                indice = int(input("\nNúmero do livro para devolução: ")) - 1
                if not catalogo[indice]["disponivel"]:
                        catalogo[indice]["disponivel"] = True
                        salvar_catalogo(catalogo)
                        print(f" Livro '{catalogo[indice]['titulo']}' devolvido!")
                else:
                        print(" O livro já está disponível.")
        except (ValueError, IndexError):
                print(" Opção inválida.")


    # ESTRUTURA EXATA DA SUA IMAGEM
def menu():
        print("\n SISTEMA DE BIBLIOTECA - v2 (com arquivo)")

        catalogo = carregar_catalogo()

        opcoes = {
                "1": ("Listar livros",        listar_livros),
                "2": ("Adicionar livro",      adicionar_livro),
                "3": ("Buscar livro",         buscar_livro),
                "4": ("Registrar empréstimo", registrar_emprestimo),
                "5": ("Devolver livro",       devolver_livro),
                "0": ("Sair",                 None),
        }

        while True:
                print("\n Opções:")
                for chave, (descricao, _) in opcoes.items():
                        print(f" [{chave}] {descricao}")

                try:
                        escolha = input("\n Sua escolha: ").strip()
                        if escolha not in opcoes:
                                raise ValueError(f"Opção '{escolha}' inválida.")

                except ValueError as e:
                        print(f" {e}")
                        continue

                else:
                        if escolha == "0":
                                print("\n Até logo!")
                                break

                        _, funcao = opcoes[escolha]
                        funcao(catalogo)


if __name__ == "__main__":
        menu()
