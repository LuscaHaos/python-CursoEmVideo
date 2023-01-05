peso = float(input('Seu peso:'))
altura = float(input('Sua altura:'))
imc = peso / altura**2
print('Seu imc é : {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobre peso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
