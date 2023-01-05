print('[1] para ver números impares de 0 a 50')
print('[2] para ver números pares de 0 a 50')
escolha = int(input('Escolha uma opção:'))
if escolha == 2:
    for p in range(0, 51, 2):
        print(p, end=', ')
elif escolha == 1:
    for i in range(1, 51, 2):
        print(i, end=', ')
else:
    print('Escolha inválida. Tente novamente.')