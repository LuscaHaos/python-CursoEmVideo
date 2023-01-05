l1 = float(input('Valor do primeiro lado:'))
l2 = float(input('Valor do segundo lado:'))
l3 = float(input('Valor do terceiro lado:'))
if l2 + l3 > l1 and l1 + l2 > l3 and l1 + l3 > l2:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo')
#"""esse programa ve se os tres lados podem formar um triângulo com a seguinte regra:
# Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das
# medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas."""




