"""
Solicite um número inteiro e informe se ele é múltiplo somente de 3, somente de 5, de ambos ou de nenhum deles.
Para esta atividade, trate o número zero em uma categoria própria: "Você digitou zero".
Teste com 3, 5, 15, 17, 30 e 0. Cada entrada deve produzir apenas uma classificação.
"""

while True:
    numero_digitado = input('Digite um número para saber se é múltipo de 3 e 5: ')

    try:
        numero_float = float(numero_digitado)
    except:
        print('!ERRO! DIGITE UM NÚMERO!\n')
        continue

    if numero_float == 0:
        print('Você digitou zero.')
        break
    elif (numero_float % 3 == 0) and (numero_float % 5 == 0):
        print(f'O {numero_float} é múltiplo de 3 e 5.')
        break
    elif numero_float % 3 == 0:
        print(f'O {numero_float} é múltiplo só de 3.')
        break
    elif numero_float % 5 == 0:
        print(f'O {numero_float} é múltiplo só de 5.')
        break
    else:
        print(f'O {numero_float} não é múltiplo de nenhum dos dois.')
        break