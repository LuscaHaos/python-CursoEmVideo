n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um numero [999 para parar]:'))
    cont += 1
    soma += n
print('Você digitou {} numeros.'.format(cont - 1))
print('A soma entre ele é {}.'.format(soma - 999))
    
