frase = str(input('Digite a frase:')).strip().upper()
print('A letra A aparece {}'.format(frase.count('A')))
print('A primeira letra "a" está na posiçao {}'.format(frase.find('A')+1))
print('A última letra "a" está na posição:{}'.format(frase.rfind('A')+1 - frase.count(' ')))
#obs: uso de +1 para não contar com a posição 0, e - frase.count(' ') para não contar com espaços.
