idade = int(input('Digite sua idade:'))
if idade == 18:
    print('Momento exato de se alistar:')

elif idade > 18:
    print('Já passou o momento de se alistar:')
    print('Passou:', idade - 18, 'ano(s)')

elif idade < 18:
    print('Não chegou o momento de se alistar:')
    print('Falta:', 18 - idade, 'ano(s)')

