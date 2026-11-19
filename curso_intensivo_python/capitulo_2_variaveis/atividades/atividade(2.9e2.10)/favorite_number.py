number_user = float(input('Digite seu número favorito: '))

if '.0' in f'{number_user:.1f}':
    print(f'Seu número favorito é: {number_user:.0f}')
else:
    print(f'Seu número favorito é: {number_user}')