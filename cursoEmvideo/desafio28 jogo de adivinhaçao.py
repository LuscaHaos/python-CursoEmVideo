import random
print('Pensando em um número...')
n = int(input('Adivinhe o número que máquina pensou!'))
maquina = random.randint(1, 5)
if n == maquina:
    print('Você acertou!')
else:
    print('Você errou!')
print('A máquina escolheu: {}'.format(maquina))









