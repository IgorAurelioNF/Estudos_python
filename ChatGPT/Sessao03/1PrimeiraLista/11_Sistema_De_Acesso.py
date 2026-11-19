# Crie um sistema com usuário admin e senha python123. Solicite ambos e permita a entrada somente quando as duas informações
# estiverem corretas. Se o usuário estiver correto, mas a senha errada, exiba uma mensagem específica.
#  Caso contrário, informe que o usuário não foi encontrado.
usuario = 'admin'
senha = 'python123'

print(F'{'LOGIN':-^30}')
digite_usuario = input(' USUÁRIO: ')
digite_senha = input(' SENHA: ')
# ERRO!!! if digite_usuario in usuario and digite_senha in senha:
if digite_usuario == usuario and digite_senha == senha:
    print(f'ENTRADA permitida!')
elif digite_usuario == usuario and digite_senha not in senha:
    print(f'USUÁRIO CORRETO. SENHA INVÁLIDA.')
else: 
    print(f'USUÁRIO não encontrado.')