"""
Listas em python
Tipo list - Mutável (Matrix) (LISTA DE COISAS)
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update   Delete ---> (C.R.U.D)
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [10,20,30,40]
#numero = lista[2] # ACESSA UM VALOR DA LISTA E ALOCANDO A UMA VARIÁVEL
del lista[2] # DELETA O VALOR DA LISTA. EVITAR AO MÁXIMO DELETAR ALGO NA LISTA, POIS PODE ATRAPALHAR NO PROCESSAMENTO
# DE PREFERÊNCIA TIRAR UM VALOR NO FINAL DA LISTA
print('Valor 30 deletado:',lista)

lista.append(50)# ESSA FUNÇÃO VAI ADICIONAR VALORES NOVOS AO FINAL DA LISTA
lista.append(60)# NÃO REQUER TANTO PROCESSAMENTO
lista.append(70)
print('ADD NOVOS VALORES:',lista)

lista.pop()# VAI REMOVER O ÚLTIMO ELEMENTO
print('REMOVEU O ÚLTIMO ELEMENTO:',lista) 
ultimo_valor = lista.pop() # USAR UMA VARIÁVEL PARA APAGAR E ARMAZENAR ELA
print('REMOVEU OUTRO ÚLTIMO VALOR:', ultimo_valor)
primeiro_valor = lista.pop(0) # REMOVER POR ÍNDICE
print('REMOVEU O PRIMEIRO VALOR:', primeiro_valor, 'LISTA ATUALIZADA:', lista)