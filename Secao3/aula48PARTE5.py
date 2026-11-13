"""
CUIDADOS com dados MUTÁVEIS
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória  (mutável)
"""
lista_a = ['Igor', 'Michelle', 4, 5]
lista_b = lista_a.copy()

lista_a.append('TE AMO!')

print(f'LISTA_A: {lista_a}')
print(f'LISTA_B: {lista_b}')