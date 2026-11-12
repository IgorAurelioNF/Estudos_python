# Solicite um número inteiro e informe se ele é par ou ímpar. Depois, verifique se ele é múltiplo de 3 e de 5 simultaneamente.
numero = int(input('Digite um número INTEIRO: '))

if numero % 2 == 0:
    print(f'{numero} é PAR')
else:
    print(f'{numero} é ÍMPAR')

# QUERIA SIMULTANEAMENTE
# if numero % 3 == 0:
#     print(f'{numero} é mútiplo de 3')
#     if numero % 5 == 0:
#         print(f'{numero} é mútiplo de 5')
#     else:
#         print(f'{numero} não é mútiplo de 5')
# elif numero % 5 == 0:
#     print(f'{numero} é mútiplo de 5')
#     if numero % 3 == 0:
#         print(f'{numero} é mútiplo de 3')
#     else:
#         print(f'{numero} não é mútiplo de 3')

# CORRETO
if (numero % 3 == 0) and (numero % 5 == 0):
    print(f'{numero} é múltiplo de 3 e 5 simultaneamente.')
else:
    print(f'{numero} não múltiplo de 3 e 5.')