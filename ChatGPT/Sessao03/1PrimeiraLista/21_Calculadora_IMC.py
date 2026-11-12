# Refaça o exercício de IMC do seu curso, mas agora solicite nome, peso e altura pelo input(). 
# Calcule o IMC e mostre o resultado com duas casas decimais. Se a altura for menor ou igual a zero, exiba uma mensagem de erro em vez de realizar a divisão.

# Nome
nome_digitado = input('Informe seu primeiro nome: ')
sobrenome = input('Informe seu SOBRENOME: ')
nome_sobrenome = f'{nome_digitado + ' ' + sobrenome}'

# PESO
peso_digitado = float(input('Qual seu PESO? '))

# Altura
altura_digitada = float(input('Qual sua ALTURA? '))

if (peso_digitado <= 0):
    print(f'Peso informado é menor ou igual a zero. Valor inválido')
elif (altura_digitada <= 0):
    print(f'Altura informado é menor ou igual a zero. Valor inválido')
else:
    imc = peso_digitado / (altura_digitada**2)
    print(f'{nome_sobrenome}, seu IMC é de {imc:.2f}')