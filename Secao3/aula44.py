"""
For + range
range -> range(start, stop, step)
"""

numeros = range(0, 10, 1) # Início, Fim, Passos

for numero in numeros:
    print(numero)
print('='*20)
numeros = range(10, 0, -1)
for numero in numeros:
    print(numero)