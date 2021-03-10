from PyQt5 import QtWidgets

from Player import Player
from Game import Game
from db import *
from messages import *
import os

from ui import Game


connection()


def start_message():
    print('Loading...')
    # time.sleep(0.3)
    # print('...3')
    # time.sleep(1.1)
    # print('...2')
    # time.sleep(0.6)
    # print('...1')
    # time.sleep(0.2)


start_message()


msg_error('Attention !')
msg_start('The Game !')

option = 1

while option != 0:
    print('- ' * 50)
    print('[1] Play')
    print('[2] Play GUI')
    print('[9] Rules')
    print('[0] Exit')
    option = int(input('Choose an option? '))
    # verify
    os.system('cls' if os.name == 'nt' else 'clear')

    if option == 1:
        player_1_name = input('Player 1 Name:')
        p1 = Player(player_1_name)
        p1.deck = p1.get_cards()

        player_2_name = input('Player 2 Name:')
        p2 = Player(player_2_name)
        p2.deck = p2.get_cards()

        g1 = Game([p1, p2])
        play = True

        while play:
            try:
                print(f'Cards {p1.name}: {p1.deck}')
                print(f'Cards {p2.name}: {p2.deck}')
                msg_grey_on_yellow('[p1] Available Cards [1-5]: ')
                j1_p1 = int(input())
                msg_grey_on_cyan('[p2] Available Cards [1-5]: ')
                j1_p2 = int(input())

                if j1_p1 == 0 or j1_p2 == 0:
                    msg_status('Game Over')
                    play = False

                if j1_p1 in range(1, 6) or j1_p2 in range(1, 6):
                    p1_played_cards, p2_played_cards = g1.get_played_cards()
                    already_played1 = p1_played_cards[j1_p1 - 1]
                    already_played2 = p2_played_cards[j1_p2 - 1]

                    if already_played1 or already_played2:
                        msg_error('Cards Already Played.')
                    else:
                        g1.match(j1_p1, j1_p2)
                        msg_grey_on_white(p1_played_cards)
                        msg_grey_on_white(p2_played_cards)
                        # verify
                        os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    msg_error('Incorrect Value.')

                # play more fix
                if p1.score == 3 or p2.score == 3:
                    play = False
            except IndexError:
                msg_error('Incorrect Value')
            except ValueError:
                msg_error('Incorrect Value.')

        more = input('Play more? y/n: ')
        if more == 'n' or more == 'N':
            play = False

        p1.score = 0
        p2.score = 0

    if option == 2:
        if __name__ == "__main__":
            import sys

            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Game.Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())

    if option == 9:
        print('RULE:')
        print('Rule: p1_atk - p2_def + p1_elm')
        print('Rule: p1_elm + 2 if fire > nature')
        print('Rule: p1_elm + 2 if nature > water')
        print('Rule: p1_elm + 2 if water > fire')
