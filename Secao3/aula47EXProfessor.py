"""SOLUÇÃO DO PROFESSOR"""
import os
palavra_secreta = 'perfurme' # PREFIRO USAR CONSTANTE
letra_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta: # VAI ARMAZENAR AS LETRAS DIGITADAS CORRETAMENTE, MAS ARMAZENA INÚMEROS DADOS REPETIDOS
        letra_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta: # IMPRESSÃO DAS LETRAS ACERTADAS, MAS A CADA LOOP DO WHILE ELA SE APAGA
        if letra_secreta in letra_acertadas:
            palavra_formada +=letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada:',palavra_formada)

    if palavra_formada == palavra_secreta: # ACERTOU A PALAVRA COMPLETA
        os.system('cls') # LIMPAR O TERMINAL
        print('\nVOCÊ GANHOU, PARABÉNS!!')
        print(f'A palavra era: {palavra_secreta}')
        print(f'Tentativas: {tentativas}')
        letra_acertadas = ''
        tentativas = 0