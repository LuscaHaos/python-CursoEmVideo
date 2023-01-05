import random
g1 = str(input('Gerador de ordem de apresentação do trabalho aleatória''\nPrimeiro grupo:'))
g2 = str(input('Segundo grupo:'))
g3 = str(input('Terceiro grupo:'))
g4 = str(input('Quarto grupo:'))
lista = [g1, g2, g3, g4]
random.shuffle(lista)
print('A ordem é:')
print(lista)
