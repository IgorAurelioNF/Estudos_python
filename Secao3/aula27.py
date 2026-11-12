"""
Fatiamento de Strings
 0123456789 (positivo)
 Olá Mundo
-987654321 (negativo)
Fatiamento [i:f:p] [::] -> [inicio : final : passos]
Obs.: a função len retorna a qtd de caracteres da str
"""

variavel = 'Olá Mundo'
print(variavel[4:]) # Mundo
print(variavel[4:8]) # Mund
print(variavel[0:5]) # Olá M
print(variavel[-9:-2]) # Olá Mun

# len()

print(len(variavel)) # 9 elementos
print(variavel[0:9:2]) # OáMno
print(variavel[::-1]) # odnuM álO == [-1:-10:-1]