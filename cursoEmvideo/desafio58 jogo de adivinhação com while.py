import random
print('Pensando em um número...')
n = int(input('Adivinhe o número que a máquina pensou de 1 a 10!'))
maquina = random.randint(1, 10)
print('A máquina escolheu: {}'.format(maquina))
contjogadas = 0

if n > 10:
    print('\033[33mDigite um número de 1 a 10!!!\033[m')

while n != maquina:
    contjogadas += 1
    maquina = random.randint(1, 10)
    n = int(input("""\033[31mVocê errou, tente novamente!\033[m
Adivinhe o número que máquina pensou!"""))
    print('A máquina escolheu: {}'.format(maquina))

print('\033[32mVocê acertou!!\033[m')
print('A máquina escolheu: {}'.format(maquina))
print('Você jogou {} vezes até acertar.'.format(contjogadas))

