# Peça dois números e informe qual é maior ou se são iguais. Depois, acrescente uma mensagem indicando se ambos são positivos, 
# ambos são negativos ou se não pertencem ao mesmo grupo. Considere zero como nem positivo nem negativo.
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

# Coersão de valores (int e float)
if '.' in numero_1:
    numero_1_convercao = float(numero_1)
else:
    numero_1_convercao = int(numero_1)

if '.' in numero_2:
    numero_2_convercao = float(numero_2)
else:
    numero_2_convercao = int(numero_2)

# Qual é maior
if numero_1_convercao > numero_2_convercao:
    print(f'{numero_1_convercao} é maior que {numero_2_convercao}')
elif numero_2_convercao > numero_1_convercao:
    print(f'{numero_2_convercao} é maior que {numero_1_convercao}')
else:
    print(f'Os dois são IGUAIS. {numero_1_convercao} e {numero_2_convercao}')

# Ambos são positivos e negativos? E descarte do número zero
    
if (numero_1_convercao != 0 and numero_2_convercao != 0) and (numero_1_convercao > 0 and numero_2_convercao > 0) :
    print(f'Os dois são POSITIVOS')
elif (numero_1_convercao != 0 and numero_2_convercao != 0) and (numero_1_convercao < 0 and numero_2_convercao < 0):
    print(f'Os dois são NEGATIVOS')
else:
    if numero_1_convercao == 0 and numero_2_convercao == 0:
        print(f'Ambos são zeros, logo ZERO é um número VAZIO')
    elif numero_1_convercao == 0:
        if numero_2_convercao > 0:
            print(f'O {numero_2_convercao} é POSITIVO  o outro é {numero_1_convercao}')
        else:
            print(f'O {numero_2_convercao} é NEGATIVO o outro é {numero_1_convercao}')
    elif numero_2_convercao == 0:
        if numero_1_convercao > 0:
            print(f'O {numero_1_convercao} é POSITIVO  o outro é {numero_2_convercao}')
        else:
            print(f'O {numero_1_convercao} é NEGATIVO o outro é {numero_2_convercao}')
    else:
        print(f'Os dois NÃO pertencem ao mesmo grupo. O sinal de positividade são diferentes')