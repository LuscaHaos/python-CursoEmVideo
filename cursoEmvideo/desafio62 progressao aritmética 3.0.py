n1 = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
termo = n1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}, '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quais termos você quer mostrar a mais?'))



