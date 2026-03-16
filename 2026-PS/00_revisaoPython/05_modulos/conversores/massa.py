# ================================================
# CONVERSÕES DE MASSA
# ================================================

def kg_para_libras(kg):
    """Converte quilogramas para libras."""
    return kg * 2.20462


def kg_para_gramas(kg):
    """Converte quilogramas para gramas."""
    return kg * 1000


# Teste do módulo
if __name__ == "__main__":
    valor = 10
    print("Testando conversões de massa")
    print("kg -> lb:", kg_para_libras(valor))
    print("kg -> g :", kg_para_gramas(valor))