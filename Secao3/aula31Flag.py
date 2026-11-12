"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not - é ou não é (tipo, valor, identidade)
"""

condicao = False 
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None) # Passou_no_if é None? True
print(passou_no_if, passou_no_if is not None) # Passou_no_if não é None? False

# OOOOOOUUUUUUU

if passou_no_if is None:
    print('\nNão passou no if')
else:
    print('\nPassou no if')