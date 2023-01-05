print('[M] para masculino')
print('[F] para feminino')
sexo = str(input('Digite seu sexo[M/F]:')).strip().upper()
m = 'M'
f = 'F'
while sexo != 'M' and sexo != 'F':
    sexo = str(input("""\033[31mDigite novamente!!\033[m
Digite seu nome[M/F]:""")).strip().upper()
print('\033[32mAnotado.\033[m')