def pedir_senha():
    return input('Senha: ')


def numero_carateres(senha):
    i = len(senha)
    if i >= 8:
        print(f'Numero de caracteres: {i}\n')
        return True
    else:
        print(f'Não é valido está senha: {senha}')
        return False


def maiusculos(senha):
    maiuscula = 0
    for i in senha:
        if i.isupper():
            maiuscula += 1
    print(f'Maiusculos: {maiuscula}')


def minusculas(senha):
    minusculas = 0
    for i in senha:
        if i.islower():
            minusculas += 1
    print(f'Minusculas: {minusculas}')


def numbers(senha):
    number = 0
    for i in senha:
        if i.isnumeric():
            number += 1
    print(f'Numeros: {number}')


def symbol(senha):
    sym = 0
    for i in senha:
        if not i.isalnum():
            sym += 1
    print(f'Simbolos: {sym}\n')