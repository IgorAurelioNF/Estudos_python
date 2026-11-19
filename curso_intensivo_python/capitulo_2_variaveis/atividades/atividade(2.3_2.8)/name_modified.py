#ATIVIDADE 2.4
name_user = input('Digite seu nome: ')
name_user = name_user.strip()

name_upper = f'Seu nome em caixa alta: {name_user.upper()}'
name_lower = f'Seu nome em minúsculo: {name_user.lower()}'
name_title = f'Seu nome com as Primeiras letras em maiúsculas: {name_user.title()}'

print('='*45)
print(f'Nome Padrão: {name_user}')
print(name_upper)
print(name_lower)
print(name_title)