nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print('Seu nome completo possui {} letras:'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome possui {} letras:'.format(nome.find(' ')))