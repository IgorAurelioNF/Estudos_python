texto = 'Python'

i= 0
tamanho_str = len(texto)

# COMO FAZ NO LAÇO WHILE
while i < tamanho_str: # Não sabe quando acaba e o número de repetições
    print(texto[i])
    i += 1
print('FORA DO WHILE\n')


# FOR PARA SITUAÇÕES QUE A PESSOA TÁ MAIS CIENTE E SABE O NÚMERO DE REPETIÇÕES
# Mais usado em variáveis
novo_texto = ''                          #INTERAÇÃO
for letra in texto:  #(PARA CADA(for)) (LETRA(letra)) (EM(in)) (INTERÁVEL(texto))
    novo_texto += f'*{letra}'
    print(letra + '+')
print(novo_texto + '*')