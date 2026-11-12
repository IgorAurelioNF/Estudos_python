"""
Desenvolva um login com usuário professor e senha Python2026. O sistema deve distinguir usuário inexistente, 
senha incorreta e autenticação bem-sucedida. Não permita acesso com apenas parte do nome ou da senha.
Teste também com os dois campos vazios.
"""

# CÓDIGO MAIS INCHUTO E MENOR

# BANCO DE DADOS
USER0001 = 'professor'
SENHA0001 = 'Python2026'

while True:
    usuario_digitado = input(f'{'Usuario: ': >9}')
    senha_digitada = input(f'{'Senha: ': >9}')

#   VALIDADOR DE CAMPO VAZIO
    if not usuario_digitado:
        print('Usuário não digitado.')
    if not senha_digitada:
        print('Senha não digitado.')

#   VALIDADOR DE USUARIO OU SENHA ERRADA
    if len(usuario_digitado) > 0 and usuario_digitado != USER0001:
        print('Usuário inexistente.')
    if len(senha_digitada) > 0 and senha_digitada != SENHA0001:
        print('Senha incorreta.')

#   RESPOSTA FINAL
    if usuario_digitado == USER0001 and senha_digitada == SENHA0001:
        print('Autentificação bem-sucedida.')
        break
    else:
        print(f'{'-' * 25}')
        continue