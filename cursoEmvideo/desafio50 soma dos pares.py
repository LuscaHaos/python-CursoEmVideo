cont = 0
soma = 0
for s in range(1, 7):
    n = int(input('Digite o {}ª número:'.format(s)))
    if n % 2 == 0:
        cont += 1
        soma += n
print('A soma dos {} números pares é: {}'.format(cont, soma))