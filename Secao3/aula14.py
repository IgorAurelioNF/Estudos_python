a = 'AAA'
b = 'BBB'
c = 1.1
string = 'a={} b={} c{terceiro:.2f}'

formato_sem_variavel_ordem = 'a={} b={} c={:.2f}'.format(a, b, c)
formato_sem_variavel_indice = 'b={1} a={0} c={2:.2f}'.format(a, b, c)
formato_sem_variavel_parametro_nominal = 'a={nome1} c={nome3:.2f} b={nome2} b+a={nome2}+{nome1}'.format(nome1=a, nome2=b, nome3=c)

formato_com_variavel_mix = string.format(a, b, terceiro=c)


print('Método format(ordem):', formato_sem_variavel_ordem)
print('\nMétodo format(Índice):', formato_sem_variavel_indice)
print('\nMétodo format(Parâmetro Nominal):', formato_sem_variavel_parametro_nominal)
print('\nMétodo format(Mix com Variável):', formato_com_variavel_mix)