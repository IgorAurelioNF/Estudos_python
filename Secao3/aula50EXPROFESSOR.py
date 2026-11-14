"""
Exercício 
Exiba os índices da lista
0 Liz
1 Michelle
2 Igor
3 Ianny
"""
lista = ['Liz', 'Michelle', 'Igor', 'Ianny']
lista.append('Levi')
indices = range(len(lista))# PEGANDO O TAMANHO DA LISTA PARA ENUMERAR 

for nome in lista: # PUXANDO A LISTA POR UM NOME DE CADA VEZ
    print(f'PULL LISTA POR NOME:{nome}')

for i in indices: # PUXANDO A LISTA POR ÍNDICES
    print(f'{i} - {lista[i]}')