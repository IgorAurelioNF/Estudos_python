"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_inteiro = input('Digite um número INTEIRO: ')

if '.' in numero_inteiro:
    print('O núemro não é inteiro')
else:
    try:
        if int(numero_inteiro) % 2 == 0:
            print(f'{numero_inteiro} é PAR!')
        else:
            print(f'{numero_inteiro} é ÍMPAR!')
    except:
        numero_inteiro = input('Digite um número INTEIRO não Letra: ')
        if int(numero_inteiro) % 2 == 0:
            print(f'{numero_inteiro} é PAR!')
        else:
            print(f'{numero_inteiro} é ÍMPAR!')

# PROFESSOR
# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'Ímpar' # Já declarar o valor, mas pode ser mudado

#     if par_impar: # Se par_impar for TRUE
#         par_impar_texto = 'Par' # Executa esse código, Se não permanece 'Ímpar'
#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro.')
















"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horas = input('Que HORAS são? ')

if int(horas) >= 0 and int(horas) <= 11:
    print('Bom dia!')
elif int(horas) >= 12 and int(horas) <= 17:
    print('Boa tarde!')
elif int(horas) >= 18 and int(horas) <= 23:
    print('Boa Noite!')
else:
    print('Você digitou a hora errada!')

# PROFESSOR

# hora_entrada = input('Que HORAS São?')

# try:
#     hora_int = int(hora_entrada)

#     if hora_int >= 0 and hora_int <= 11:
#         print('Bom dia!')
#     elif hora_int >= 12 and hora_int <= 17:
#         print('Boa tarde!')
#     elif hora_int >= 18 and hora_int <= 23:
#         print('Boa Noite!')
#     else:
#         print('Você digitou a hora errada!')
# except:
#     print('Por favor, digite apenas números inteiros.')

















"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu Primeiro nome: ')

if len(nome) <= 4 and len(nome) >= 1:
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <=6:
    print("Seu nome é normal")
elif len(nome) > 6:
    print("Seu nome é muito grande")
else:
    print('Você não digitou nada')

# PROFESSOR

# nome_entrada = input('Digite seu nome: ')
# tamanho_nome = len(nome_entrada)

# if tamanho_nome > 1: #Validação do tamanho do nome, não pode ter só um digito
#     if tamanho_nome <=4:
#         print('Seu nome é curto')
#     elif tamanho_nome >=6 and tamanho_nome <= 6:
#         print("Seu nome é normal")
#     else:
#         print("Seu nome é muito grande")
# else:
#     print('Digite mais de uma letra.')