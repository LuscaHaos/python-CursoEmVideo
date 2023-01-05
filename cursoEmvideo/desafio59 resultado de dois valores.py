n1 = int(input('Digite o primeiro valor.'))
n2 = int(input('Digite o segundo valor.'))
escolha = 0

while n1 and n2 / 1 and escolha != 5:
    print('-=' * 20)
    print('[1] Soma')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] \033[32mNovos números\033[m')
    print('[5] \033[31mSaior do programa\033[m')
    print('-=' * 20)

    escolha = int(input('Escolha:'))

    if escolha == 1:
        soma = n1 + n2
        print('O resultado de {} + {} é {}'.format(n1, n2, soma))

    elif escolha == 2: 
        multiplica = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, multiplica))

    elif escolha == 3:
        if n1 > n2:
            print(n1, 'é o maior.')
        else:
            print(n2, 'é o menor.')
    elif escolha == 4:
        print('Informe os números novamente.')
        int(input('Digite o primeiro valor:'))
        int(input('Digite o segundo valor'))
    else:
        print('\033[33m!!!Opção inválida, tente novamente.\033[m')
