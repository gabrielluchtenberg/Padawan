from math import atan2, degrees


def get_number(x, y):
    numeros = [11, 8, 16, 7, 19, 3, 17, 2, 15, 10, 6, 13, 4, 18, 1, 20, 5, 12, 9, 14]
    cordenada = degrees(atan2(y, x)) + 180 + 9
    if cordenada > 360:
        return 11
    return numeros[int(cordenada // 18)]


def get_score(x, y):
    diametros = (x ** 2 + y ** 2) ** 0.5 * 2

    if diametros > 340:
        return "X"

    if diametros <= 12.7:
        return "DB"

    if diametros <= 31.8:
        return "SB"

    if diametros <= 198:
        jogada = ""

    elif diametros <= 214:
        jogada = "T"

    elif diametros <= 324:
        jogada = ""

    else:
        jogada = "D"

    return jogada + str(get_number(x, y))
