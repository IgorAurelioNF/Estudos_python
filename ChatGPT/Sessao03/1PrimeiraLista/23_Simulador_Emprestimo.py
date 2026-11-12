# Um banco fictício aprova uma solicitação quando o cliente tem pelo menos 21 anos, recebe R$ 2.500,00 ou mais e não possui 
# restrição financeira. Solicite idade, salário e se possui restrição ('S' ou 'N'). Informe se a solicitação foi aprovada. 
# Não é necessário calcular juros.

# Menu de Perguntas
print(f'{'BANCO CHATGPT':-^30}')
idade_usuario = int(input('\nQual sua IDADE? '))
salario_usuario = float(input('Quanto você recebe de SALÁRIO? '))
restricao_usuario = input('Possui restrição? [Sim] ou [Não]? ')

# limites Banco
b_idade_min = 21
b_salario_min = 2500.00
b_restricao = 'Ss'

# Validação
if (idade_usuario >= b_idade_min) and (salario_usuario >= b_salario_min) and ((restricao_usuario [0])  in 'Nn'):
    print(f'\nSolicitação APROVADA')
else:
    print(f'\nSolicitação NÃO APROVADA')