import math
from math import sin, cos, tan
n = int(input('Digite o valor:'))
seno = sin(math.radians(n))
cosseno = cos(math.radians(n))
tangente = tan(math.radians(n))
print('O seno vale: {:.2f}'.format(seno))
print('O cosseno vale: {:.2f}'.format(cosseno))
print('A tangente é: {:.2f}'.format(tangente))
