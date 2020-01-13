def verification():

    if choose1 > choose2:
        print('O número maior é' ' ' + choose1)
    if choose1 < choose2:
        print('O número maior é' ' ' + choose2)
    if choose1 == choose2:
        print('Os números são equivalentes, não existe um maior!')


choose1 = input('Escolha sua opção: ')
choose2 = input('Escolha sua opção: ')
verification()