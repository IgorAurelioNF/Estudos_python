# Crie um programa que peça nome, idade e altura. Exiba tudo em uma frase usando f-string, 
# apresentando a altura com duas casas decimais. Acrescente uma informação indicando se a pessoa é maior de idade.
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))

frase = f'Olá, {nome}, você tem {altura:.2f} metros de altura.'

if idade >= 18:
    print(f'{frase} Você é maior de idade, tem {idade} de idade')
else:
    print(f'{frase} Você é menor de idade, falta {18 - idade} para ser maior de idade.')