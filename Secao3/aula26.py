"""
Formatração básica de Strings
s - string
d - int
f - float
.<número de dígitos>f
x e x - hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal | + ou - 
Ex.: 0>-100,.1f
Conversion flags - !r !s !a | PUXA OUTROS MÉTODOS
"""

variavel = 'ABC'
# PADDING
print(f'{variavel}.')
print(f'{variavel: >10}.') # ESQUERDA
print(f'{variavel: <10}.') # DIREITA
print(f'{variavel:-^10}.') # CENTRO

print(f'\n', 30 * '-', f'\n', sep='')
# FORMATAÇÃO DE NÚMEROS
print(f'{1000.4548937587478379:0>+10,.1f}')
# FORMATAÇÃO DE HEXADECIMAL
print(f'O hexadecimal de 1500 é {1500:08X}')

print(f'{variavel!r}')