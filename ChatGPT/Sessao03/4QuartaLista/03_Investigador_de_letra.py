"""
Peça uma frase e conte quantas vezes aparecem as letras a e A, somadas.
Exiba também o número total de caracteres, incluindo espaços. Se a frase estiver vazia, apresente uma mensagem adequada.
Você deverá utilizar for para percorrer a frase, if para testar cada caractere e += para atualizar o contador. Não use .count().
Dica: você já fez algo semelhante com while. Desta vez, não precisa acessar a string por índice.
"""

# VARIAVEIS NULAS
resultado_a = '' # FRASE FINAL QTD 'aA'
azinho_azao = 0 # CONTADOR DE 'aA'
tam_frase = 0
resultado_tam_frase = ''

# PROGRAMA
frase_user = input('Digite uma frase: ')
for letra in frase_user: # Verificador de 'aA'
    if letra in 'aA':
        azinho_azao += 1
        resultado_a = f'Número de vezes que aparece a letra "a" e "A" é: {azinho_azao}'

tam_frase = len(frase_user)
if  not tam_frase: # Informacao do tamanho da frase
    resultado_tam_frase = f'Não foi digitado nenhuma frase.'
else:
    resultado_tam_frase = f'A frase apresenta um total de {tam_frase} caracteres.'

# RESULTADO
print(resultado_a)
print(resultado_tam_frase)