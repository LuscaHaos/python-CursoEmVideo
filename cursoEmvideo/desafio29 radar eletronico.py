
km = int(input('Velocidade do carro:'))
valormulta = (km - 80) * 7
if km > 80:
    print('Você foi multado!')
    print('O valor da multa é: R${}'.format(valormulta))
