# Considere valor = 1589.7564. Sem alterar o valor armazenado na variável, mostre-o com duas casas decimais, uma casa decimal,
#  três casas decimais e alinhado à direita em um campo de 15 caracteres. Use apenas f-strings.

valor = 1589.7564

print(f'{valor=} com DUAS casas decimais: {valor:.2f}')
print(f'{valor=} com UMA casa decimal: {valor:.1f}')
print(f'{valor=} com TRÊS casas decimais: {valor: >15.3f}')
