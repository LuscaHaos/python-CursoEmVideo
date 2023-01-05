from datetime import date
ano = int(input('Vou ver se o seu ano é bissexto. Digite o ano ou digite 0 para ver o ano atual.'))
if ano == 0:
    ano = date.today().year
    print('{}'.format(ano))
if ano % 4 == 0 and ano % 400 == 0 and ano % 100 != 0:
    print('Bissexto')
else:
    print('Não bissexto')



