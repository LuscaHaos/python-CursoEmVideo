ano = int(input('Digite o ano em que nasceu:'))
calculo = (2021 - ano)
if calculo <= 9:
    print('Você tem {} anos.'.format(calculo))
    print('Classificação: MIRIM')

elif calculo <= 14:
    print('Você tem {} anos.'.format(calculo))
    print('Classificação: INFANTIL')

elif calculo <= 19:
    print('Você tem {} anos.'.format(calculo))
    print('Classificação: JÚNIOR')

elif calculo <= 25:
    print('Você tem {} anos.'.format(calculo))
    print('Classificação: SÊNIOR')

else:
    print('Você tem {} anos.'.format(calculo))
    print('Classificação: MASTER')