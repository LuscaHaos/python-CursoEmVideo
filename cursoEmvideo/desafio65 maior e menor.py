opcao = 'S'
soma = 0
cont = 0
maior = 0
menor = 0
while opcao in 'Ss':
    n = int(input('Digite um número:'))
    cont += 1
    soma += n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opcao = str(input('Quer continuar? [S/N]:')).upper().strip()
media = soma / cont
print('A média é {:.1f}'.format(media))
print('O maior é {} e o menor é {}'.format(maior, menor))



