# JOGO DA FORCA

tentativas = 0
PALAVRA_SECRETA = 'Michelle'.upper() #Palavra do game
palavra_oculta ='*'*len(PALAVRA_SECRETA)
letras_testadas =''

print(f'{'JOGO DA FORCA':=^30}')
print(f'A palavra tem {len(palavra_oculta)} letras.')
while True:
    print('-'*25, 'TENTATIVA:',tentativas+1)
    user_letra = input('Digite  uma Letra: ').upper() # LETRA DIGITADA

    if user_letra in palavra_oculta: # TESTE SE A JÁ FOI DIGITADA E ACERTADA
        print(f'Você já acertou essa letra {user_letra}.')
        print(f'Palavra formada: {palavra_oculta}')
        continue

    if len(user_letra) > 1: # VALIDADOR DE MAIS DE 1 DIGITO E CAMPO VAZIO
        print(f'Digite apenas uma letra. TENTE NOVAMENTE.')
        continue
    elif not user_letra:
        print('Campo vazio, digite uma letra. TENTE NOVAMENTE.')
        continue

    if not user_letra in PALAVRA_SECRETA: # ARMAZEM DE LETRAS TESTADAS
        if not letras_testadas:
            pass
        elif user_letra in letras_testadas:
            print(f'LETRA {user_letra} JÁ TESTADA. TESTADAS: {letras_testadas}-')
            print(f'Palavra formada: {palavra_oculta}')
            continue

        letras_testadas += '-' + user_letra
        print(f'ERROU! LETRAS TESTADAS: {letras_testadas}-')
        print(f'Palavra formada: {palavra_oculta}')
        tentativas +=1
        continue
        
    palavra_temp = '' # RESET
    for letra_por_letra in PALAVRA_SECRETA: # VERIFICAR SE A LETRA DIGITADA ESTÁ PRESENTE NA PALAVRA_SECRETA
        if user_letra == letra_por_letra:
            palavra_temp += user_letra
        else:
            palavra_temp += '*'

    stage2 = ''#RESET
    for i in range(len(PALAVRA_SECRETA)):# VERIFICAR A POSIÇÃO DA LETRA ACERTADA E UNIR COM A TENTATIVA ANTERIOR
        if palavra_oculta[i] == palavra_temp[i]:
            stage2 += '*'
        else:
            stage2 += PALAVRA_SECRETA[i]

    palavra_oculta = stage2 
    tentativas +=1
    if palavra_oculta == PALAVRA_SECRETA:
        break

    print(f'Palavra formada: {palavra_oculta}')
    continue

print('\nVOCÊ GANHOU, PARABÉNS!!')
print(f'A palavra era: {PALAVRA_SECRETA}')
print(f'Tentativas: {tentativas}')