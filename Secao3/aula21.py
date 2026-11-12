# Operadores Lógicos
# and (e) or (ou) not (não)
# AND - Todas as condições precisam ser TRUE
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor FALSO
# São considerados falsy (que vc já viu):  0 0.0 '' False 
# Também existe o tipo None que é usado para respresentar UM NÃO VALOR (INEXISTENTE)

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

# if (condição):
senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else: 
    print('Sair')

# Avaliação de curto circuito
print('\n',True and False and True, sep='')
print(True and 0.0 and True) # Retorna o valor da condição Falsy