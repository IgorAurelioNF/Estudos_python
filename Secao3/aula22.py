# Operadores Lógicos
# and (e) or (ou) not (não)
# OR - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# Se qualquer valor for considerado TRUE, a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu):  0 0.0 '' False 
# Também existe o tipo None que é usado para respresentar UM NÃO VALOR (INEXISTENTE)

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')
# # if (condição):
# senha_permitida = '123456'
# if (entrada == 'E' or entrada == 'e' or entrada == 'Entrar') and senha_digitada == senha_permitida:
#     print('Entrar')
# else: 
#     print('Sair')

# Avaliação de curto circuito
print(True or False)

senha = 0 or False or 0 or 'abc' or True
print(senha)

# "if" simples
senha2 = input('Senha: ') or 'Sem senha'
print(senha2)