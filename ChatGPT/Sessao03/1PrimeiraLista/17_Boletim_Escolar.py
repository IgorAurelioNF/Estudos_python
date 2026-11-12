# Solicite três notas, calcule a média e classifique o resultado: média de 7 a 10, aprovado; de 5 até menos de 7, 
# recuperação; abaixo de 5, reprovado. Exiba a média com duas casas decimais. Considere notas válidas entre 0 e 10.
print(f'\n{'MÉDIA E CLASSIFICAÇÃO DE NOTAS': ^40}')
print(f'{'='*40}')

nota1 = float(input('Nota da PRIMEIRA prova: '))
nota2 = float(input('Nota da SEGUNDA prova: '))
nota3 = float(input('Nota da TERCEIRA prova: '))
media = 0

if (nota1 >= 0 and nota1 <= 10) and (nota2 >= 0 and nota2 <= 10) and (nota3 >= 0 and nota3 <= 10):
    media = (nota1 + nota2 + nota3) / 3
else:
    print(f'Você digitou uma nota menor que 0 ou maior que 10. TENTE NOVAMENTE!')

if media >= 7 and media <=10:
    print(f'{'-'*40}')
    print(f'Aluno APROVADO. Média = {media:.2f}')
elif media >= 5 and media < 7:
    print(f'{'-'*40}')
    print(f'Aluno em RECUPERAÇÃO. Média = {media:.2f}')
else: 
    print(f'{'-'*40}')
    print(f'Aluno REPROVADO. Média = {media:.2f}')