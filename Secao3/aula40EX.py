""" Calculadora com while"""
#   VALIDADOR DE NÚMEROS/ CONVERSOR
numeros_validos = None
coversao_num1 = 0
coversao_num2 = 0

while True:
#   QUESTIONÁRIO AO USUÁRIO
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o SEGUNDO número: ')
#   CONVERSOR
    try:
        coversao_num1 = float(numero_1)
        coversao_num2 = float(numero_2)
        numeros_validos = True
    except:
        print(f'\nERRO! Números não podem ser convertidos! TENTE DE NOVO')
        numeros_validos = None
        continue

    operador_aritimetico = input('\nQual operação executar?\n' \
    'Multiplicação[*] - Divisão[/] - Adição[+] - Subtração[-]\n' \
    'Informe sua Escolha: ')

#   VALIDADOR DE SINAIS E QUANTIDADE
    operadores_permitidos = '+-/*'
    if operador_aritimetico not in operadores_permitidos:
        print('Operador inválido.')
        continue
    if len(operador_aritimetico) > 1:
        print('Digite apenas um OPERADOR.')
        continue

    if operador_aritimetico == '*':
        multiplicacao = (f'\nOPERAÇÃO: {coversao_num1} x {coversao_num2} = {coversao_num1 * coversao_num2}\n')
        print(f'{multiplicacao}')
    elif operador_aritimetico == '/':
        divisao = (f'\nOPERAÇÃO: {coversao_num1} / {coversao_num2} = {coversao_num1 / coversao_num2}\n')
        print(f'{divisao}')
    elif operador_aritimetico == '+':
        adicao = (f'\nOPERAÇÃO: {coversao_num1} + {coversao_num2} = {coversao_num1 + coversao_num2}\n')
        print(f'{adicao}')
    elif operador_aritimetico == '-':
        subtracao = (f'\nOPERAÇÃO: {coversao_num1} - {coversao_num2} = {coversao_num1 - coversao_num2}\n')
        print(f'{subtracao}')
    else:
        print('Como chegou aqui?')

    repetir = input('Quer continuar? [s]im ou [n]ao? ').lower().startswith('s') # lower()-> tudo pequeno          startswitch()
    if repetir:
        continue
    else:
        break
