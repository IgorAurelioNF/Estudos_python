"""
Iterável -> str, range e etc (___iter___)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
texto0 = 'Luiz' # ITERÁVEL
iterator0 = iter(texto0) # OU .__iter__() ITERATOR(INTERADOR)
print(texto0)
print(iterator0)
print(texto0.__next__() ) #OU next(texto)

##########################

texto = 'Luiz' # ITERÁVEL
iterator = iter(texto) # ITERATOR
# EM while
while True:
    try: 
        letra = next(iterator) # NEXT
        print(letra) # ITER
    except StopIteration: # Quando der esse erro, o while vai parar
        break
# EM for
for letra in texto:
    print(letra)