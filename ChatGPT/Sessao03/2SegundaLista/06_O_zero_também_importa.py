"""
Solicite dois números inteiros e classifique cada um como positivo, negativo ou zero. Depois, informe se ambos são positivos, 
ambos são negativos ou se não pertencem ao mesmo grupo.
Explique, em um comentário no código, por que bool(0) ser False não significa que zero seja um número negativo.
"""
# VARIÁVVEIS NONE
rank_num1 = None
float_num1 = 0
rank_num2 = None
float_num2 = 0

# CONSTANTES E VALOR
NUM_POSITIVO = '[POSITIVO]'
NUM_NEGATIVO = '[NEGATIVO]'
NUM_ZERO = '[ZERO]'

while True:
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')

# VALIDADOR NÚMERO 1
    try:
        float_num1 = float(numero_1)
        if float_num1 > 0:
            rank_num1 = NUM_POSITIVO
        elif float_num1 < 0:
            rank_num1 = NUM_NEGATIVO
        else:
            rank_num1 = NUM_ZERO
    except:
        print('!ERRO! Primeiro Número não é um número. Tente Novamente. \n')
        continue

# VALIDADOR NÚMERO 2
    try:
        float_num2 = float(numero_2)
        if float_num2 > 0:
            rank_num2 = NUM_POSITIVO
        elif float_num2 < 0:
            rank_num2 = NUM_NEGATIVO
        else:
            rank_num2 = NUM_ZERO
    except:
        print('!ERRO! Segundo Número não é um número. Tente Novamente. \n')
        continue

    if (rank_num1 == NUM_ZERO) and (rank_num2 == NUM_ZERO):
        print(f'{numero_1} é {rank_num1}. {numero_2} é {rank_num2}.')
        print(f'Ambos são {NUM_ZERO}.')
    elif (rank_num1 == NUM_POSITIVO) and (rank_num2 == NUM_POSITIVO):
        print(f'{numero_1} é {rank_num1}. {numero_2} é {rank_num2}.')
        print(f'Ambos são {NUM_POSITIVO}.')
    elif (rank_num1 == NUM_NEGATIVO) and (rank_num2 == NUM_NEGATIVO):
        print(f'{numero_1} é {rank_num1}. {numero_2} é {rank_num2}.')
        print(f'Ambos são {NUM_NEGATIVO}.')
    else:
        print(f'{numero_1} é {rank_num1}. {numero_2} é {rank_num2}.')
        print('Ambos não pertencem ao mesmo grupo.')
    break

# o 0 tem valor False, por isso não recebe o valor negativo