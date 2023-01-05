n1 = input('Digite um valor:')
n2 = input('Digite o segundo valor:')
n3 = input('Digite o terceiro valor:')
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))




