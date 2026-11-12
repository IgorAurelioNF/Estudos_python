# VARIAVEIS NULOS
cont_par = 0
cont_impar = 0
multiplo3e5 = 0
soma_numeros = 0

print(f'{'ANALISADOR DE NÚMEROS':=^42}')
while True:    
    num_user = input('Digite um número INTEIRO entre 1 e 20: ')

    if not num_user: # VALIDADOR CAMPO VAZIO
        print(f'Campo vazio, digite algo.')
        print('-'*42)
        continue

    try: # VALIDADOR FLOAT
        if num_user:
            conversor_num = float(num_user)
        #INFORMAÇÕES DO FLOAT
        tamanho_float = len(str(conversor_num)) # TAMANHO DA STR
        penultima_str = tamanho_float - 2 # POSIÇÃO DA PENÚLTIMA LETRA
        str_float = str(conversor_num) # CONVERSÃO PARA STR

        comparador_float = str_float[penultima_str:tamanho_float] # ÚLTIMOS DOIS DIGITOS

        if '.0' == comparador_float:
            pass
        else:
            print('Você digitou um float. TENTE NOVAMENTE')
            print('-'*42)
            continue
    except ValueError:
        print(f'Você digitou um texto. TENTE NOVAMENTE.')
        print('-'*42)
        continue

    
    try:
        conversor_num = int(num_user)

    except ValueError:
        print('Digite um número inteiro válido.')
        continue


    if conversor_num >= 1 and conversor_num <=20: # VALIDADOR DE REGRA
        pass
    elif conversor_num < 1:
        print(f' O {conversor_num} é menor que 1, não está na rega. TENTE NOVAMENTE.')
        print('-'*42)
        continue
    else:
        print(f' O {conversor_num} é maior que 20, não está na rega. TENTE NOVAMENTE.')
        print('-'*42)
        continue

# NÚMERO VALIDADO
    print(f'{'='*42}\n')
    for numero in range(1, (conversor_num+1)):
        if numero % 2 == 0: #CONTADOR DE NÚMERO PAR E ÍMPAR
            cont_par +=1
            txt_analisador = f'{numero:<2} {'- Par ':<8}'
        else:
            cont_impar +=1
            txt_analisador = f'{numero:<2} {'- Ímpar ':<8}'

        if numero %  3 == 0 and numero % 5 == 0:
            multiplo3e5 +=1
            txt_analisador += '| É múltiplo de 3 e 5.'
        elif numero % 3 == 0:
            txt_analisador += '| Múltiplo de 3.'
        elif numero % 5 == 0:
            txt_analisador += '| Múltiplo de 5.'
        else:
            txt_analisador += '| Não é múltiplo de 3 nem 5.'
        print(txt_analisador)
        soma_numeros += numero
# ANALISADOS AGORA A TABELA
    print(f'\n{'RELATÓRIO':=^30}')
    print(f'Soma dos números: {soma_numeros}')
    print(f'Quantidade de pares: {cont_par}')
    print(f'Quantidade de ímpares: {cont_impar}')
    print(f'Múltiplos de 3 e 5: {multiplo3e5}')
    print(f'{'='*30}\n')

# TENTAR NOVAMENTE
    continuar = input('Deseja sair do programa? [s]im ou [n]ão? ').lower().startswith('s')
    if continuar:
        print('ADEUS! até a próxima!')
        break
    else:
        print(f'\n{'ANALISADOR DE NÚMEROS':=^42}')
            #ZERAR OS CONTADORES
        cont_par = 0
        cont_impar = 0
        multiplo3e5 = 0
        soma_numeros = 0
        continue