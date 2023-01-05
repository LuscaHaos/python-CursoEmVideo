n = int(input('Digite um número:'))
primo = 0
for c in range(2, n):
    if n % c == 0:
        print("Múltiplo de: {}".format(c))
        primo += 1
if primo == 0:
    print("É primo!")
else:
    print('Não é primo!')

