"""
Solicite três lados e determine se podem formar um triângulo, verificando todas as desigualdades necessárias e se 
todos os lados são positivos.
Classifique os válidos como equilátero, isósceles ou escaleno. Faça testes com 
(3, 3, 3), (5, 5, 8), (3, 4, 5), (1, 2, 10) e (2, 2, 4).
"""
# Variaveis None
lado1 = ''
lado2 = ''
lado3 = ''
flado1 = 0
flado2 = 0
flado3 = 0
triangulo_valido = 0

while True:
    lado1 = input('Digite o valor do primeiro lado: ')
    lado2 = input('Digite o valor do segundo lado: ')
    lado3 = input('Digite o valor do terceiro lado: ')
# CONVERSAO
    try:
        flado1 = float(lado1)
        if flado1 <0:
            print('Primeiro lado é negativo. TENTE NOVAMENTE.')
            continue
        elif flado1 == 0:
            print('Primeiro lado é zero. TENTE NOVAMENTE.')
            print(f'{'-'*30}')
            continue

        flado2 = float(lado2)
        if flado2 < 0:
            print('Segundo lado é negativo. TENTE NOVAMENTE.')
            print(f'{'-'*30}')
            continue
        elif flado2 == 0:
            print('Segundo lado é zero. TENTE NOVAMENTE.')
            print(f'{'-'*30}')
            continue

        flado3 = float(lado3)
        if flado3 < 0:
            print('Terceiro lado é negativo. TENTE NOVAMENTE.')
            print(f'{'-'*30}')
            continue
        elif flado3 == 0:
            print('Terceiro lado é zero. TENTE NOVAMENTE.')
            print(f'{'-'*30}')
            continue
    except:
        print('ERRO! Um dos lados tem valor incompatível. TENTE NOVAMENTE.')
        print(f'{'-'*30}')
        continue

# VALIDAÇÃO DO TRIÂNGULO
    if (flado1 + flado2 > flado3) and (flado1 + flado3 > flado2) and (flado2 + flado3 > flado1):
        triangulo_valido = 1
    else:
        triangulo_valido = 0
        
# CLASSIFICACAO DO TRIANGULO
    equilatero = (flado1 == flado2) and (flado3 == flado1)
    isoceles = (flado1 == flado2 and flado1 != flado3) or (flado1 == flado3 and flado1 != flado2) or (flado2 == flado3 and flado2 != flado1)
    escaleno = (flado1 != flado2) and (flado1 != flado3) and (flado2 != flado3)

    if triangulo_valido == 0:
        print('Triângulo invalido para Classificalo.TENTE NOVAMENTE.')
        print(f'{'-'*30}')
        continue
    else:
        if equilatero:
            print(f'Triângulo EQUILÁTERO, todos os lados são IGUAS.')
        elif isoceles:
            print(f'Triângulo ISÓCELES, tem DOIS lado iguais e UM diferente.')
        elif escaleno:
            print(f'Triângulo ESCALENO, todos os lados são DIFERENTES.')
        else:
            print('!ERRO!Não deveria passar por aqui.')
        break