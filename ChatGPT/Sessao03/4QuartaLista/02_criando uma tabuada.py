"""
Solicite um número inteiro e exiba sua tabuada de multiplicação, começando em 1 e terminando em 10.
Utilize obrigatoriamente for, range() e f-strings.
EXEMPLO COM O NÚMERO 3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
...
3 x 10 = 30
"""
int_num_user = None # CONVERSOR INT
print(f'{'TABUADA DE MULTIPLICAÇÃO':=^49}')
while True:
    number_user = input('Digite um número INTEIRO para mostrar a tabuada: ')

    try: # CONVERSOR & VALIDADOR
        int_num_user = int(number_user)
    except:
        print(f'{'='*47}')
        print('ERRO! Valor digitado inválido. TENTE NOVAMENTE.')
        print(f'{'='*47}')
        continue

    print('x'*14)
    for num in range(1,11): # TABUADA
        print(f'{int_num_user:>2} x {num:>2} = {int_num_user * num}')

    print('x'*14)
    user_continue = input('Continuar? [s]im ou [n]ão? ').lower().startswith('s')
    if user_continue:
        print('\n')
        continue
    else:
        print('Obrigado por testar a Tabuada de multiplição')
        break