"""
Interando strings com while
"""
# Nome USUARIO
nome = input('Digite seu nome para editar ele: ')

# Contexto
tamanho_nome = len(nome) # Quantidade de caracteres
contador_nome = 0 # contador
novo_nome_editado ='' # inicio

while contador_nome == 0:
    novo_nome_editado += '*'

    while (contador_nome < tamanho_nome):

        letra_por_letra = f'{nome[contador_nome]}*' # armazena o valor do caracter
        novo_nome_editado +=letra_por_letra # armazena cada caracter editado
        contador_nome +=1 # contador para pular em cada variável

print(f'Nome editado: {novo_nome_editado}') # Nome completo editado