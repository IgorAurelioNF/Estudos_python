# INFORMAÇÕES DO CLIENTE
nome_cliente = input('Digite seu nome: ')
idade_cliente = int(input('Digite sua idade: '))
pipoca_cliente = input('Deseja adicinar pipoca? [S]im ou [N]ão: ')

# VALIDADOR DE IDADE
if idade_cliente >= 0 and idade_cliente <=11:
    valor_ingresso = 12.00
elif idade_cliente >= 12 and idade_cliente <=59:
    valor_ingresso = 25.00
elif idade_cliente >=60:
    valor_ingresso = 15.00
else:
    valor_ingresso = 0
    print(f'Idade Inválida.')

if (pipoca_cliente [0]) in 'Ss':
    valor_pipoca = 10.00
    print(f'Adicional de pipoca')
else:
    valor_pipoca = 0.00
    print(f'Sem adicional de pipoca')

if valor_ingresso > 0:
    print(f'\n{'CINEMA':-^28}',
        f'\nCliente: {nome_cliente}',
        f'\nIdade: {idade_cliente} anos',
        f'\nIngresso: R${valor_ingresso:.2f}',
        f'\nPipoca: R${valor_pipoca:.2f}',
        f'\nTotal: R${valor_pipoca+valor_ingresso:.2f}',
        f'\n{'-'*28}')
else:
    print(f'INGRESSO INVÁLIDO')