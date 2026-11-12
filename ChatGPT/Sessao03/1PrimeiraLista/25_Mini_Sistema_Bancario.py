# Crie um programa com saldo inicial de R$ 1.000,00. Pergunte se a pessoa deseja depositar ('D'), sacar ('S') ou consultar saldo ('C'). 
# No depósito, solicite um valor positivo e atualize o saldo; no saque, não permita valores maiores que o saldo nem valores menores ou iguais a zero. 
# Exiba uma mensagem para operações inválidas. O programa deve executar apenas uma operação por vez.

# Saldo Inicial
saldo_inicial = 1000.00

# Menu Usuario
escolha_usuario = input('O que você deseja? [S]acar? [D]epositar? [C]onsultar saldo? \nDigite sua escolha:')

# Escolhas do banco
b_depositar_alternativa = 'Dd'
b_sacar_alternativa = 'Ss'
b_consultar = 'Cc'

if (escolha_usuario [0]) in b_depositar_alternativa:
    print(f'{'-'*40}')
    deposito_usuario = float(input('Valor a depositar: R$'))
    if deposito_usuario > 0:
        print(f'Saldo atual: R${deposito_usuario+saldo_inicial:.2f}')
    else:
        print('Valor negativo. Depósito NEGADO')
elif (escolha_usuario [0]) in b_sacar_alternativa:
    print(f'{'-'*40}')
    sacar_usuario = float(input('Digite um valor a SACAR: '))
    if (sacar_usuario > saldo_inicial) or sacar_usuario <= 0:
        print(f'Valor acima do saldo, ou menor ou igual a zero')
    else:
        print(f'Valor retirado: R${sacar_usuario:.2f}. Saldo ATUAL: R${saldo_inicial-sacar_usuario:.2f}')
elif (escolha_usuario [0]) in b_consultar:
    print(f'Saldo ATUAL: R${saldo_inicial:.2f}')
else:
    print(f'ERRO! Solicitação inválida ou não digitado.')