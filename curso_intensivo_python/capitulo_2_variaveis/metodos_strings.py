message_one = 'A primeira palavra é sempre maiúscula'.title()
print(f'Método 1 - {message_one}')

message_two = 'Todas as letras em minúsculas'.lower()
print(f'\nMétodo 2 -{message_two}')

message_three = 'Todas as letras maiúsculas'.upper()
print(f'\nMétodo 3 - {message_three}\n')

message_four = 'Tabulação: \n\tPython \n\tGit \n\tGitHub \n\tSQL'
print(fr'Tabulação \t - {message_four}')

message_five = ' Tira o espaço da esquerda '.lstrip()
print(f'\nMétodo 4 -  -{message_five}-')

message_six = ' Tira o espaço da direita '.rstrip()
print(f'\nMétodo 5 - -{message_six}-')

message_seven = ' Tira o espaço dos dois '.strip()
print(f'\nMétodo 6 - -{message_seven}-')

message_eight = 'www.https://Google.com.br'
simple_url = message_eight.removeprefix('www.https://')
print(f'Método 7 - Tirar partes do texto: {simple_url}')