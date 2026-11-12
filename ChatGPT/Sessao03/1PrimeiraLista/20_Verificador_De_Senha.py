# Solicite uma senha e verifique se ela está vazia usando not. Se estiver, informe que nenhuma senha foi digitada. 
# Caso exista uma senha, verifique se ela contém o caractere '@'. Exiba mensagens diferentes para cada situação.

senha = input('Digite uma SENHA: ')

if not senha:
    print(f'Senha vazia. Nenhuma senha digitada.')
elif '@' in senha:
    print(f'A senha contém o caracter "@".')
else:
    print(f'A senha não é vazia e nem contém o caracter "@".')