valor = int(input('Digite o valor do seu salário:'))
aumento10 = valor * 10/100 + valor
aumento15 = valor * 15/100 + valor
if valor <= 1250:
    print('O seu salário com aumento de 15% vai de {} para R${:.2f}'.format(valor, aumento15))
if valor > 1250:
    print('O seu salário com aumento de 10% vai de {} para R${:.2f}'.format(valor, aumento10))
