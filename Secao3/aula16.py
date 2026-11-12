# if/ elif      / else
# se/ se não se / se não
login = input('Você quer "entrar" ou "sair"? ')

if login == 'entrar':
    print('Você entrou no sistema!')
elif login == 'sair':
    print('Você saiu no sistema.')
else:
    print('ERRO! Você não digitou nem "entrar" e nem "sair".')