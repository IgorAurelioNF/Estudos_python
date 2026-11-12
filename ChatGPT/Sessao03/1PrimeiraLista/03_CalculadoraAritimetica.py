# Solicite dois números inteiros e mostre a soma, subtração, multiplicação, divisão comum, divisão inteira, potência e resto da divisão. 
# Considere que o segundo número será diferente de zero.
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

if numero_2 != 0:
    print(f'{numero_1} + {numero_2} = {numero_1 +  numero_2}') # SOMA
    print(f'{numero_1} - {numero_2} = {numero_1 -  numero_2}') # SUBTRAÇÃO
    print(f'{numero_1} * {numero_2} = {numero_1 *  numero_2}') # MULTIPLICAÇÃO
    print(f'{numero_1} / {numero_2} = {numero_1 /  numero_2}') # DIVISÃO COMUM
    print(f'{numero_1} // {numero_2} = {numero_1 //  numero_2}') # DIVISÃO INTEIRA
    print(f'{numero_1} ** {numero_2} = {numero_1 ** numero_2}') # POTENCIAÇÃO
    print(f'{numero_1} % {numero_2} = {numero_1 % numero_2}') # DIVISÃO POR RESTO
else:
    print(f'O segundo número é zero: {numero_2=}, não será possível fazer os cálculos')