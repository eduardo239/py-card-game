from Player import Player
from Game import Game
import time

from colorama import Fore, Back, Style
from colorama import init

init()

from termcolor import colored, cprint
import sys
from helpers import *

# https://pypi.org/project/termcolor/

time.sleep(1)

msg_error('Atenção!')
msg_black_on_red('THE GAME!')


def start_message():
    print('Jogo começando em..')
    # time.sleep(1)
    # print('3')
    # time.sleep(1)
    # print('2')
    # time.sleep(1)
    print('1')
    time.sleep(1)


option = 1
while option != 0:
    print('- ' * 50)
    print('[1] Jogar')
    print('[0] Sair')
    option = int(input('Qual a opção escolhida? '))

    if option == 1:

        print('Jogando..')
        p1 = Player('John')
        p1.deck = p1.get_cards()

        p2 = Player('Jane')
        p2.deck = p2.get_cards()

        g1 = Game([p1, p2])
        play = True

        start_message()
        while play:
            try:
                print(f'cartas: {p1.deck}')
                print(f'cartas: {p2.deck}')
                msg_grey_on_yellow('[p1] Carta a ser jogada [1-5]: ')
                j1_p1 = int(input())
                msg_grey_on_cyan('[p2] Carta a ser jogada [1-5]: ')
                j1_p2 = int(input())

                # 0 erro
                if j1_p1 in range(1, 6) or j1_p2 in range(1, 6):
                    p1_played_cards, p2_played_cards = g1.get_played_cards()
                    ja_jogada = p1_played_cards[j1_p1 - 1]
                    ja_jogada2 = p2_played_cards[j1_p2 - 1]

                    if ja_jogada or ja_jogada2:
                        msg_error('Carta já jogada.')
                    else:
                        g1.match(j1_p1, j1_p2)
                        msg_black_on_red(p1_played_cards)
                        msg_black_on_red(p2_played_cards)
                else:
                    msg_error('Valor fora do alcance')

                # jogar mais ?
                if p1.score == 3 or p2.score == 3:
                    play = False
            except IndexError:
                msg_error('Valor fora de alcance.')
            except ValueError:
                msg_error('Valor inválido.')

        p1.score = 0
        p2.score = 0

print('- ' * 50)
