"""while/else nunca utilizado"""
string = 'Valor Qualquer'

i = 0
while i < len(string):
    letra = string[i]

    print(letra)
    i += i
else:
    print('O else foi executado.')
print('Fora do while. ')