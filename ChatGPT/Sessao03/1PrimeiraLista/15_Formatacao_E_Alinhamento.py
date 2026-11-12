# Utilizando texto = 'PYTHON', exiba a palavra centralizada em 20 posições preenchidas com -, alinhada à direita em 20 posições preenchidas com. 
# e alinhada à esquerda em 20 posições preenchidas com *. Use os recursos de f-strings apresentados na aula 26.

texto = 'PYTHON'
txt_centralizado = f'{texto:-^20}'
txt_direita = f'{texto:.>20}'
txt_esquerda = f'{texto:*<20}'
print(f'{txt_centralizado}')
print(f'{txt_direita}')
print(f'{txt_esquerda}')