from PyQt5 import QtWidgets
from db.cmd_sql import connection, select_all
from cmd.CmdPlayer import Player
from cmd.CmdGame import Game
from tabulate import tabulate


options = [1, 2, 0]
connection()


def view_winners():
    w = select_all()
    print(tabulate(w, headers=["Played 1", "Player 2", "Winner", "Score"], tablefmt="psql"))


def play():
    option = 1

    while option != 0:
        print('- ' * 50)
        print('[1] Play Command Line Game')
        print('[2] Play User Interface Game')
        print('[7] View Winners')
        print('[8]')
        print('[9] Rules')
        print('[0] Exit')

        try:
            option = int(input('Choose an option? '))

            """ cmd game """
            if option == 1:
                p1 = Player('Ivy')
                p2 = Player('Ema')

                g1 = Game(p1, p2)
                g1.start()

            """ gui game """
            if option == 2:
                print('[2]')

            """ cmd line winners"""
            if option == 7:
                view_winners()

            """ rules """
            if option == 9:
                print('Rules')
                print('Calc: attack - enemy defense + element = total')

            if option not in options:
                print('[Value not Found]')

        except ValueError as ve:
            print(f'[Error]: Invalid Character, {ve}')
        except KeyError as ke:
            print(f'[Error]: Invalid Character, {ke}')


if __name__ == "__main__":
    play()
