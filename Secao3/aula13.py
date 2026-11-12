#Exercício IMC Aula 30
nome = 'Ígor Aurélio'
altura = 1.80
peso = 105.20
imc = peso / (altura * altura)

#f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso:.2f} quilos e seu IMC é:'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)