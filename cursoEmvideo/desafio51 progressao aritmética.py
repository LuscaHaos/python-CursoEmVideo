n1 = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão:'))
t10 = n1 + (10 - 1) * r
for pa in list(range(n1, t10 + n1, r)):
    print('{}'.format(pa), end=', ')
print('FIM.')
