"""
Listas em python
Tipo list - Mutável (Matrix) (LISTA DE COISAS)
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234 índices+
#        -54321 índices-
string = 'ABCDE'  # 5 caracteres (len)
lista_funcao = list() # FUNÇÃO PARA CONVERTER ALGO EM LISTA
lista_vazia = [] # CRIADA A LISTA VAZIA

#print(bool(lista_vazia)) # FALSE
#print(lista_vazia, type(lista_vazia)) #<class 'list'>

#        0     1       2             3    4
lista = [123, True, 'Ígor Aurélio', 1.2, []]
#       -5    -4      -3            -2   -1

print(lista) # IMPRIMIR A LISTA COMPLETA
print('-'*40)

print(lista[2], type(lista[2])) # IMPRIMIR UM ELEMENTO DA LISTA ESPECÍFICO
print('-'*40)

lista[-3] = 'Michelle' # MUDANDO/RECEBENDO VALOR DA LISTA 
print(lista[-3].upper()) # PODE USAR FUNÇÃO EM UM ELEMENTO DA LISTA
print('-'*40)

print(lista) # IMPRIMINDO A LISTA ALTERADA