dia = int(input('Quantos dias alugou o carro?'))
km = float(input('Quantos km andou com o carro?'))
total = (dia * 60) + (km * 0.15)
print('Total: R${:.2f}'.format(total))


