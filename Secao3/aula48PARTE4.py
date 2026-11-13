"""
Listas em python
Tipo list - Mutável (Matrix) (LISTA DE COISAS)
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - índices e fatiamento
Métodos úteis: 
    append: Adiciona um item ao final
    insert: Adiciona um item no índice escolhido
    pop: Remove do final ou do índice escolhido
    del: apaga um índice
    clear: limpa a lista
    extend: estende a lista
    +: concatena listas
Create Read Update   Delete ---> (C.R.U.D)
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(f'UNIÃO LISTA C(A+B): {lista_c}')

lista_a.extend(lista_b) # MÉTODO QUE NÃO RETORNA NADA, MEXE DIRETAMENTE NA LISTA A
print(f'LISTA A ESTENDIDA: {lista_a}')