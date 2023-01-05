n = str(input('Digite seu nome:')).strip().title()
pnome = n.split()
print('O seu primeiro nome é: {}'.format(pnome[0]))
print('O seu último nome é: {}'.format(pnome[len(pnome)-1]))
