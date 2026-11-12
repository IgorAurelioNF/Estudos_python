"""
Repetições
while (enquanto)
Executa um ação enquanto uma condição for verdadera
Loop infinito -> Quando um código não tem fim
"""

contador = 0 

while contador <= 100:
    contador += 1

    if contador == 6:
        print(f'Não vou mostrar o {contador}.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break

print('\nLAÇO DE REPETIÇÃO FINALIZADO!')