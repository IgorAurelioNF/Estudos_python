"""
Desenvolva um login com usuário professor e senha Python2026. O sistema deve distinguir usuário inexistente, 
senha incorreta e autenticação bem-sucedida. Não permita acesso com apenas parte do nome ou da senha.
Teste também com os dois campos vazios.
"""

# BANCO DE DADOS
USER0001 = 'professor'
SENHA0001 = 'Python2026'

# Variaveis None
campo_vazio_user = None
campo_vazio_password = None
user_inexistente = None
password_incorreta = None

while True:
    usuario_digitado = input(f'{'Usuario: ': >9}')
    senha_digitada = input(f'{'Senha: ': >9}')

#   VALIDADOR DE CAMPO VAZIO
    if not usuario_digitado:
        campo_vazio_user = 1
    if not senha_digitada:
        campo_vazio_password = 1

#   VALIDADOR DE USUARIO OU SENHA ERRADA
    if usuario_digitado != USER0001:
        user_inexistente = 1
    if senha_digitada != SENHA0001:
        password_incorreta = 1

#   RESPOSTA FINAL
    if usuario_digitado == USER0001 and senha_digitada == SENHA0001:
        print('Autentificação bem-sucedida.')
        break
    elif campo_vazio_user == 1 or campo_vazio_password == 1:
        if campo_vazio_user == 1:
            print('Usuário não digitado.')
        if campo_vazio_password == 1:
            print('Senha não digitado.')
        print('\n')
        continue
    elif user_inexistente == 1 or password_incorreta == 1:
        if user_inexistente == 1:
            print('Usuário inexistente.')
        if password_incorreta == 1:
            print('Senha incorreta.')
        print('\n')
        continue
    else:
        print('ERRO!')