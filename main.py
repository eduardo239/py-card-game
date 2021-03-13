from PyQt5 import QtWidgets
from db.cmd_sql import connection
from cmd.CmdPlayer import Player
from cmd.CmdGame import Game

options = [1, 2, 0]

connection()

#

p1 = Player('Ivy')
p2 = Player('Ema')

g1 = Game(p1, p2)
g1.start()


def play():
    option = 1

    while option != 0:
        print('- ' * 50)
        print('[1] Play Command Line Game')
        print('[2] Play User Interface Game')
        print('[0] Exit')

        try:
            option = int(input('Choose an option? '))

            """ cmd game """
            if option == 1:
                print('[1]')

            """ gui game """
            if option == 2:
                print('[2]')

            if option not in options:
                print('[Value not Found]')

        except ValueError as ve:
            print(f'[Error]: Invalid Character, {ve}')
        except KeyError as ke:
            print(f'[Error]: Invalid Character, {ke}')


if __name__ == "__main__":
    play()
