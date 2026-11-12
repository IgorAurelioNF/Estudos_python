"""
Crie um programa que exiba continuamente o seguinte menu:
========== MENU ==========
[1] Somar dois números
[2] Comparar dois números
[3] Verificar par ou ímpar
[4] Sair
==========================

As operações devem seguir estas regras:
1. Na opção 1, solicitar dois números e exibir a soma.
2. Na opção 2, solicitar dois números e identificar o maior ou informar que são iguais.
3. Na opção 3, solicitar um número inteiro e informar se é par ou ímpar.
4. Na opção 4, encerrar o programa e exibir uma mensagem de despedida.
Exigências: utilizar while, if/elif/else, f-strings e try/except. Entradas inválidas não devem encerrar o programa nem produzir resultados incorretos. 
Após cada operação, o menu deve reaparecer.
"""
# conversao 
conversao_escolha = None
conversao_adicao_numero1 = None
conversao_adicao_numero2 = None
conversao_comparacao_num1 = None
conversao_comparacao_num2 = None
conversao_jokepoo_num = None
while True:
    print(f'{'MENU':=^26}')
    print(f'[1] Somar dois números')
    print(f'[2] COmparar dois números')
    print(f'[3] Verificar par ou ímpar')
    print(f'[4] Sair')
    print(f'{'='*26}')
    escolha_user = input('INFORME: ')

    try:
        conversao_escolha = int(escolha_user)
    except:
        print('Não tem essa opção. TENTE NOVAMENTE.')
        continue
#   ADIÇÃO
    while conversao_escolha == 1:
        print(f'{'ADIÇÃO':=^26}')
        numero1_adicao = input('Digite o primeiro número: ')
        numero2_adicao = input('Digite o segundo número: ')

        try:
            conversao_adicao_numero1 = int(numero1_adicao)
            conversao_adicao_numero2 = int(numero2_adicao)
        except:
            print('Número incomum. TENTE NOVAMENTE.')
            continue
        print(f'{'='*26}')
        print(f'{conversao_adicao_numero1} + {conversao_adicao_numero2} = {conversao_adicao_numero1 + conversao_adicao_numero2}')
        break
#   COMPARAÇAO MAIOR/ MENOR/ IGUAL
    while conversao_escolha == 2:
        print(f'{'COMPARAÇÃO':=^26}')
        num1_comparar = input('Digite o primeiro Núemro: ')
        num2_comparar = input('Digite o seguundo Núemro: ')

        try: 
            conversao_comparacao_num1 = int(num1_comparar)
            conversao_comparacao_num2 = int(num2_comparar)
        except:
            print('Número incomum. TENTE NOVAMENTE.')
            continue

        if conversao_comparacao_num1 == conversao_comparacao_num2:
            print(f'{'='*26}')
            print(f'{conversao_comparacao_num1} e {conversao_comparacao_num2} são IGUAIS.')
        elif conversao_comparacao_num1 > conversao_comparacao_num2:
            print(f'{'='*26}')
            print(f'{conversao_comparacao_num1} e MAIOR que {conversao_comparacao_num2}.')
        else:
            print(f'{'='*26}')
            print(f'{conversao_comparacao_num1} e MENOR que {conversao_comparacao_num2}.')
        break
#   ÍMPAR OU PAR
    while conversao_escolha == 3:
        print(f'{'ÍMPAR OU PAR':=^26}')
        num1_jokepoo = input('Digite um número: ')

        try:
            conversao_jokepoo_num = int(num1_jokepoo)
        except:
            print('Número incomum. TENTE NOVAMENTE.')
            continue

        if conversao_jokepoo_num % 2 == 0:
            print(f'{'='*26}')
            print(f'{conversao_jokepoo_num} é PAR!')
        else:
            print(f'{'='*26}')
            print(f'{conversao_jokepoo_num} é ÍMPAR!')
        break
#   SAIDA DO SISTEMA
    if conversao_escolha == 4:
        print(f'{'='*26}')
        print(f'Tchau! Até a próxima!')
        break
    else:
        print(f'{'='*26}')
        print('Voltando ao MENU...')
        print(f'{'='*26}')
        continue