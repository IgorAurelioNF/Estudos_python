# Solicite três medidas. Um triângulo válido precisa ter todos os lados positivos e a soma de quaisquer dois lados maior que o terceiro. 
# Verifique essas condições. Se for válido, classifique como equilátero (três lados iguais), isósceles (exatamente dois iguais) ou escaleno (todos diferentes).

# PEDIDO DAS MEDIDAS
medida1 = float(input('Informe a medida do LADO 1: '))
medida2 = float(input('Informe a medida do LADO 2: '))
medida3 = float(input('Informe a medida do LADO 3: '))

# TESTE DE TRIÂNGULO
if (medida1 > 0 and medida2 > 0 and medida3 > 0) and ((medida3 + medida1) > medida2) and ((medida2 + medida1)> medida3) and ((medida2 + medida3) > medida1):
    if medida1 == medida2 and medida3 == medida1:
        print(f'Triângulo EQUILÁTERO, todos os lados são IGUAS.')
    elif (medida1 == medida2 and medida3 != medida1) or (medida2 == medida3 and medida2 != medida1) or (medida3 == medida1 and medida3 != medida2):
        print(f'Triângulo ISÓCELES, tem DOIS lado iguais e UM diferente.')
    else: 
        print(f'Triângulo ESCALENO, todos os lados são DIFERENTES.')
else:
    print(f'Não passou no teste do triângulo.')