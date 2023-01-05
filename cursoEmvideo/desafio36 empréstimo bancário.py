valor = float(input('Qual valor da casa?'))
salario = float(input('Qual seu salário?'))
anos = int(input('Quantos anos você vai pagar?'))

valormensal = (valor / (12 * anos))

print('O valor mensal a pagar é: R${:.2f}'.format(valormensal))

if valormensal <= (salario * (30/100)):
    print('Empréstimo aprovado!')
elif valormensal > (salario * (30/100)):
    print('Empréstimo negado!')


