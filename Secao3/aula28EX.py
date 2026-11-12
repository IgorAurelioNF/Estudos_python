"""
Exercício 
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade foram digitados:
    EXIBA:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do se nome é {letra}
        A última letra do seu nome é {letra}
se nada for digitado em nome ou idade:
    exiba: "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contém ESPAÇO.')
    else:
        print(f'Seu nome NÃO contém espaço.')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ÚLTIMA letra do seu nome é {nome[-1]}')
else:
    print(f'Desculpe, você deixou campos vazios.')