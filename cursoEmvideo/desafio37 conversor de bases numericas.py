n = int(input('Digite um número inteiro:'))
print('[1] Converter em binário:')
print('[2] Converter em octal:')
print('[3] Converter em hexadecimal')
opçao = int(input('Escolha um opção:'))
binario = bin(n)
octal = oct(n)
hexa = hex(n)
if opçao == 1:
    print('{}'.format(binario)[2:])

elif opçao == 2:
    print('{}'.format(octal)[2:])

elif opçao == 3:
    print('{}'.format(hexa)[2:])

else:
    print('Opção inválida! Tente novamente.')


