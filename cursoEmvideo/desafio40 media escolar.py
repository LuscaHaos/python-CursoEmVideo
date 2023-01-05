nota1 = float(input('Digite a media 1:'))
nota2 = float(input('Digite a media 2:'))
media = (nota1 + nota2) / 2
print('Sua média é {:.1f}'.format(media))
if media < 5:
    print('REPROVADO!!')

elif media >= 7:
    print('APROVADO!!')

else:
    print('RECUPERAÇÃO!!')

