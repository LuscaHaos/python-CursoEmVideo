from datetime import date
atual = date.today().year
cont1 = 0
cont2 = 0
for data in range(1, 8):
    data = int(input('{}ª data:'.format(data)))
    maiord = atual - data
    if maiord >= 18:
        cont1 = cont1 + 1
    else:
        cont2 += 1
print('{} pessoas são maiores de idade e {} pessoas são menores de idade.'.format(cont1, cont2), end=' ')
