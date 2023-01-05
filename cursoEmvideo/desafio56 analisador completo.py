idadecont = 0
mulhercont = 0
hmaisvelho = 0
nomevelho = 0
nomevelho = ''

for p in range(1, 5):
    print('----- {}ª pessoa -----'.format(p))
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [F/M]:')).strip().upper()

    #a media de idade do grupo
    if p > 0:
        idadecont += idade
        media = idadecont / 4

    #verifica o homem mais velho
    if p == 1 and sexo in 'Mn':
        hmaisvelho = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > hmaisvelho:
        hmaisvelho = idade
        nomevelho = nome

    #conta quantas mulheres tem menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        mulhercont += 1

print('\033[;44mA média de idade do grupo é:', media)
print('\033[;44mO homem mais velho tem {:.0f} e se chama {}!\033[m'.format(hmaisvelho, nomevelho))
print('\033[;44mTotal de {} mulher(s) tem menos de 20 anos.\033[m'.format(mulhercont))
print('\033[m')



