n1 = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
termo = n1
c = 0
while c <= 10:
    print('{}, '.format(termo), end='')
    termo += razao
    c += 1
