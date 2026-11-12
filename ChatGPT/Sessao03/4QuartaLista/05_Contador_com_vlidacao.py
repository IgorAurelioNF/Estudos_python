"""Crie um programa que peça um número inteiro de 1 a 10.

Se o usuário digitar uma entrada inválida, o programa deverá solicitar outra usando while e try/except.

Quando receber um número válido, utilize for e range() para exibir a contagem de 1 até esse número, inclusive.

Ao final, mostre também a soma de todos os números exibidos.

Exemplo: para a entrada 4, a contagem será 1, 2, 3, 4 e a soma será 10."""
# ARMAZEM DE VARIAVEL
int_n_u = None
soma = 0
num_limite = ''
while True:
    num_user = input('Digite um número de 1 a 10: ')
    try:
        int_n_u = int(num_user)
        if int_n_u >= 1 and int_n_u <= 10:
            pass
        else:
            print(f'O número {int_n_u} não está na regra.')
            int_n_u + '2'
    except:
        print('Valor digitado inválido. TENTE NOVAMENTE.\n')
        continue
    
    for cont in range(1,int_n_u+1):
        num_limite += f'{cont} '
        soma += cont
    break

print(f'Resultado: {num_limite}')
print(f'Soma dos números: {soma}')