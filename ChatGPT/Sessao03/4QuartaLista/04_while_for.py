texto = 'Eu amo Python'

i = 0
print('WHILE:')
while i < len(texto):
    if texto[i] == ' ':
        i += 1
        continue

    print(texto[i])
    i += 1

print('\nFOR:')
for letra in texto:
    if letra == ' ':
        continue
    print(letra)