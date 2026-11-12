# Peça o valor de uma compra. A loja concede 15% de desconto para compras a partir de R$ 200,00,
#  inclusive. Para valores inferiores, o desconto é de 5%. Exiba o preço original, o valor descontado e o total a pagar.

valor_compra = float(input('Digite o valor da compra: '))

# DESCONTO
if valor_compra >= 200.00:
    print(f'\nVocê ganhou um desconto de 15%.', 
          f'\n{' COMPRA E DESCONTO ':-^50}',
          f'\nValor sem desconto R${valor_compra:.2f}. \nValor do desconto: {valor_compra*0.15:.2f}',
          f'\n{' Valor FINAL ':-^50}',
          f'\nValor Final com desconto: R${valor_compra-(valor_compra*0.15):.2f}')
else:
    print(f'\nVocê ganhou um desconto de 5%.', 
        f'\n{' COMPRA E DESCONTO ':-^50}',
        f'\nValor sem desconto R${valor_compra:.2f}. \nValor do desconto: {valor_compra*0.05:.2f}',
        f'\n{' Valor FINAL ':-^50}',
        f'\nValor Final com desconto: R${valor_compra-(valor_compra*0.05):.2f}')