frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

frase = 'abcddefeee'

# print(frase.count('Python'))
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = 0

i = 0 #contador
while i < len(frase):
    letra_atual = frase[i] #ITERAÇÃO DE STRING / Salvando a Letra da ITERAÇÃO

    if letra_atual == ' ': # Não contabilizar os espaços
        i += i
        continue
    qtd_atual = frase.count(letra_atual) # PEGANDO A QUANTIDADE DE LETRA ATUAL DA ITERAÇÃO TEM

    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_que_apareceu_mais_vezes = letra_atual
    # print(letra_atual, quantas_vezes_letra_apareceu_atual)
    i += 1

print(f'A letra que apareceu mais vezes foi '
      f'"{letra_que_apareceu_mais_vezes}" que apareceu '
      f'{qtd_apareceu_mais_vezes}x')