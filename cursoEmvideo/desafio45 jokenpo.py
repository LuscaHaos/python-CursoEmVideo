while True:
    import random
    from time import sleep

    print('[0] PEDRA')
    print('[1] PAPEL')
    print('[2] TESOURA')

    escolha = int(input('Qual sua escolha?'))
    maquina = random.randint(0, 2)

    print('JO')
    sleep(0.8)
    print('KEN')
    sleep(0.8)
    print('PO!!!')
    sleep(0.5)

    print('-=' * 20)
    if escolha == 0:
        print('Você escolheu: PEDRA')
        if maquina == 0:
            print('Maquina: PEDRA')
            print('\033[33mEMPATE!!!')
        elif maquina == 1:
            print('Maquina: PAPEL')
            print('\033[31mVOCÊ PERDEU!!!')
        elif maquina == 2:
            print('Maquina: TESOURA')
            print('\033[32mVOCÊ GANHOU!!!')

    elif escolha == 1:
        print('Você escolheu: PAPEL')
        if maquina == 0:
            print('Maquina: PEDRA')
            print('\033[32mVOCÊ GANHOU!!!')
        elif maquina == 1:
            print('Maquina: PAPEL')
            print('\033[33mEMPATE!!!')
        elif maquina == 2:
            print('Maquina: TESOURA')
            print('\033[31mVOCÊ PERDEU!!!')

    elif escolha == 2:
        print('Você escolheu: TESOURA')
        if maquina == 0:
            print('Maquina: PEDRA')
            print('\033[31mVOCÊ PERDEU!!!')
        elif maquina == 1:
            print('Maquina: PAPEL')
            print('\033[32mVOCÊ GANHOU!!!')
        elif maquina == 2:
            print('Maquina: TESOURA')
            print('\033[33mEMPATE!!!')
    print('\033[m-=' * 20)
    print('[1]Jogar novamente')
    novamente = int(input(':'))
else:
    print('Escolha inválida!! Tente novamente.')
