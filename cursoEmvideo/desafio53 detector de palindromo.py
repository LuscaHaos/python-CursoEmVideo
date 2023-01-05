frase = str(input('Digite uma palavra:')).strip()
palavras = frase.split()
junto = ''.join(palavras)
inversa = ''
print('O inverso de {} é {}'.format(junto, inversa ))
for letra in range(len(junto)-1, -1, -1):
    inversa += junto[letra]
if inversa == junto:
    print('É um palindromo.')
else:
    print('Não é uma palindromo.')

