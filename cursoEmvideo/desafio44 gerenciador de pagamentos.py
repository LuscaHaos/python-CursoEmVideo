preço = float(input('Preço das compras (R$):'))
print('[1] à vista dinheiro/cheque: 10% de desconto')
print('[2] à vista no cartão: 5% de desconto')
print('[3] em até 2x no cartão: preço normal')
print('[4] 3x ou mais no cartão: 20% de juros')
forma = float(input('Escolha a forma de pagamento.'))
desconto10 = preço - preço * 10/100
desconto5 = preço - preço * 5/100
juros20 = preço + preço * 20/100
if forma == 1:
    print('O valor vai de: {} para {}'.format(preço, desconto10))
elif forma == 2:
    print('O valor vai de: {} para {}'.format(preço, desconto5))
elif forma == 4:
    print('O valor vai de: {} para {}'.format(preço, juros20))
else:
    print('Total: {}'.format(preço))
