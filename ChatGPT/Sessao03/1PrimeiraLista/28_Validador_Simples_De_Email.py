# Solicite um endereço de e-mail e verifique se não está vazio e se contém os caracteres '@' e '.'. 
# Se atender a essas três condições, exiba "Formato básico aceito"; caso contrário, exiba "Formato inválido". 
# Essa é apenas uma verificação simplificada, não uma validação completa de e-mails.

email_digitado = input('Digite um E-mail para ver se é válido: ')

# VALIDADOR
if (' ' not in email_digitado) and ('@' in email_digitado) and ('.' in email_digitado):
    print(f'Formato básico aceito.')
else:
    print('Formato inválido.')