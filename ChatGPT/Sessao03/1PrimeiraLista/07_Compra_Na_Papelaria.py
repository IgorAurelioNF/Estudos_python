# Solicite o nome de um produto, seu preço unitário e a quantidade comprada. 
# Calcule o total e exiba um pequeno recibo usando f-strings com valores monetários de duas casas decimais.

produto_nome = input('Digite o nome do produto: ')
preco_unitario = float(input('Preço unitário: '))
quantidade = int(input('Quantidade comprada: '))
none = ...
total_compra = preco_unitario * quantidade

print(f'{30 * '-'}',
      f'\n| {produto_nome: <27}|',
      f'\n| Quantidade: {quantidade: <15}|',
      f'\n| Preço Un.: R${round(preco_unitario,2): <14.2f}|',
      f'\n|{28 * '-'}|',
      f'\n| Total: {total_compra: <20.2f}|',
      f'\n{30 * '-'}')