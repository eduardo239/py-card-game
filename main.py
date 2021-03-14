from PyQt5 import QtWidgets
from db.cmd_sql import connection, select_all
from cmd.CmdPlayer import Player
from cmd.CmdGame import Game
from ui import GuiGame
from tabulate import tabulate


options = [1, 2, 7, 8, 9, 0]
connection()


def view_winners():
    w = select_all()
    print(tabulate(w, headers=["Played 1", "Player 2", "Winner", "Score"], tablefmt="psql"))


def view_winners_gui():
    print('nothing here')


def play():
    option = 1

    while option != 0:
        print('- ' * 50)
        print('[1] Play Command Line')
        print('[2] Play Graphical User Game')
        print('[7] View Winners (Command Line)')
        print('[8] View Winners (Graphical User Interface)')
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

                import sys
                app = QtWidgets.QApplication(sys.argv)
                MainWindow = QtWidgets.QMainWindow()
                ui = GuiGame.Ui_MainWindow()
                ui.setupUi(MainWindow)
                MainWindow.show()
                sys.exit(app.exec_())

            """ cmd line winners"""
            if option == 7:
                view_winners()

            """ cmd line winners"""
            if option == 8:
                view_winners_gui()

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
