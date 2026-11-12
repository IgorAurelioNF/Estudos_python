# Uma pessoa pode participar de uma competição se tiver entre 16 e 30 anos, inclusive, e possuir autorização ('S'). 
# Crie um programa que solicite a idade e a autorização e mostre se a participação foi permitida. Aceite tanto 'S' quanto 's'.

idade = int(input('Qual a sua idade? '))
confirmacao = input('Deseja participar [S] ou [N]? ')

if (idade >= 16 and idade <= 30) and (confirmacao [0]) in 'Ss':
    print(f'Você está apito a participar da competição, tem idade e confirmou a participação.')
elif not (idade >= 16 and idade <= 30) and not ((confirmacao [0]) in 'Ss'):
    print(f'Você não tem nem idade e nem confirmou a presença.')
elif not ((confirmacao [0]) in 'Ss'):
    print(f'Você tem idade, mas não confirmou a presença.')
else:
    print(f'Você não tem idade para participar.')