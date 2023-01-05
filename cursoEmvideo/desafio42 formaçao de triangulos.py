l1 = float(input('Medida do primeiro lado:'))
l2 = float(input('Medida do segundo lado:'))
l3 = float(input('Medida do terceiro lado:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('O segmento pode formar um triângulo.', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não é possível formar um triângulo.')