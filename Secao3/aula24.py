# Operadores in e note in
# IN - entre (está entre)
# NOT IN - não entre (não está entre)
# Strings são interáveis 
# 0 1 2 3 4 5
# O t á v i o
# -6-5-4-3-2-1

nome = 'Otávio'

# print(nome[2])
# print(nome[-4])

print('á' in nome)
print('z' in nome)
print(20 * '-')
print('á' not in nome)
print('z' not in nome)

print(20 * '-')

nome_digitado = input('Digite seu NOME: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome_digitado:
    print(f'\n{encontrar} está em {nome_digitado}')
else:
    print(f'\n{encontrar} não está em {nome_digitado}')