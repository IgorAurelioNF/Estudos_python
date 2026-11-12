"""
Desenvolva um programa que solicite uma palavra e apresente:
- A palavra original e sua versão invertida.
- A quantidade total de caracteres.
- O primeiro e o último caractere.
- Quantas vezes aparecem as letras a ou A.
- Se ela é um palíndromo, desconsiderando maiúsculas e minúsculas.
Regras: utilize while e índices para contar as ocorrências de a ou A. Não use for, .count() ou listas. Não permita que uma entrada vazia provoque erro.

EXEMPLO DE RESULTADO
Palavra: arara
Invertida: arara
Quantidade: 5
Primeira letra: a
Última letra: a
Ocorrências de A: 3
É palíndromo: Sim
"""
palavra_valida = None # FLAG
# VARIAVEIS s/ CONTADOR
invertida_palavra = ''
quantidade_letra = None
primeira_letra = None
ultima_letra = None
palindromo = None
# VARIAVEIS c/ CONTADOR
ocorrencia_letra_a = 0
contador_ocorrencia = 0


while True:
    palavra_user = input('Digite uma palavra para fazer uma investigação: ')

# Validador de palavra com espaço ou vazia
    if ' ' in palavra_user:
        print('ERRO! A palavra não pode apresentar espaço')
        continue
    elif not palavra_user:
        print('ERRO! Campo vazio, digite uma palavra!')
        continue
    else:
        palavra_valida = True

    if palavra_valida is True:
        invertida_palavra = palavra_user[::-1]
        quantidade_letra = len(palavra_user)
        primeira_letra = palavra_user[0]
        ultima_letra = palavra_user[-1]

        while contador_ocorrencia < quantidade_letra:
            if palavra_user[contador_ocorrencia] in 'aA':
                ocorrencia_letra_a += 1
            contador_ocorrencia += 1

        if (palavra_user.lower()) == (invertida_palavra.lower()):
            palindromo = 'Sim'
        else:
            palindromo = 'Não'
        break
    else:
        print('NÃO ERA PRA CHEGAR AQUI.')
        continue
    
        
print(f'Palavra: {palavra_user}')
print(f'Invertida: {invertida_palavra}')
print(f'Quantidade: {quantidade_letra}')
print(f'Primeira letra: {primeira_letra}')
print(f'Última letra: {ultima_letra}')
print(f'Ocorrência de A: {ocorrencia_letra_a}')
print(f'Palíndromo: {palindromo}')