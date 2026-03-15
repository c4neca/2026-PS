# debug_teste/01b-debug.py
# ATENÇAO: 4 erros propositais. Encontre e corrija todos!
# Rode de dentro de 05_modulos/: python debug_teste/01b-debug.py

# ERRO 1: módulo não utilizado no código

from conversores import celsius_para_kelvin, km_para_milhas # ERRO 2: módulo não utilizado (ou inexistente)
from utils.formatador import formatar_resultado # ERRO 3: romatar_resultado está recebendo um argumento extra

resultado = celsius_para_kelvin(25)
print(f"25°C em K: {resultado}")

print(formatar_resultado("teste", 100, "km", 62.1, "mi"))

print(f"50 km = {km_para_milhas(50):.2f} mi")

# ERRO 4: importação desnecessária, módulo algo pode causar erro