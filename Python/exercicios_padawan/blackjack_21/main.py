import random
from exercicios_padawan.blackjack_21.classes.blackjack21 import *
from exercicios_padawan.blackjack_21.services.somethings import *

black_jack = BlackJack()

continuar = True

while continuar:
    carta = black_jack.pegar_carta()

    print(f'\nSua carta:: "{carta}"!!!')

    print(f"Suas cartas são {black_jack.cartas_jogador}")
    print(f"Score em conjunto: {black_jack.soma_jogador}")

    if black_jack.alcancou_21():
        print('Você ganhou!')
    else:
        print('Você perdeu!')
        proxima()

print(f"Seu Score {black_jack.soma_jogador} pontos !!!")
