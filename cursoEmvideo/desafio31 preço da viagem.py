km = int(input('Distancia em km:'))
valor1 = km * 0.50
valor2 = km * 0.45
if km <= 200:
    print('O valor da viagem é: R${}'.format(valor1))
else:
    print('O valor da vigame é: R${}'.format(valor2))
