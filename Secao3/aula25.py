"""
Interpolação básica de strings
s - strings
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)

print('Bem-Vindo, %s' % nome)
print(variavel)

print('\n' \
'O hexadecimal de %d é %04x' % (15, 15))