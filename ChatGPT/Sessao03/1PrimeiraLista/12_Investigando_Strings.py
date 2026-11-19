# Peça um nome e um caractere que a pessoa deseja procurar. Informe se o caractere aparece no nome. 
# Depois, mostre o primeiro e o último caractere do nome usando índices. Considere que o nome digitado não será vazio.

# Perguntas
while True: 
    nome_procurado = input('Digite um nome para ser procurado: ').strip()
    caractere_procurado = input('Informe um caracter para ser procurado: ')

    if not nome_procurado:
        print('Você não digitou nada. TENTE NOVAMENTE.')
        print('\n')
        continue

    if caractere_procurado in nome_procurado:
        print(f'Sim, {caractere_procurado} tem no nome {nome_procurado}')
        print(f'Primeira letra: {nome_procurado [0]} | Última letra: {nome_procurado [-1]}')
        break
    else:
        print(f'Não, {caractere_procurado} não tem no nome {nome_procurado}')
        print(f'Primeira letra: {nome_procurado [0]} | Última letra: {nome_procurado [-1]}')
        break