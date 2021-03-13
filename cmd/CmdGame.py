import time
import random
from db.cmd_sql import insert_result
from tabulate import tabulate
from termcolor import cprint
from pyfiglet import Figlet
# f = Figlet(font='doom')
f = Figlet(font='standard')

# colors
print_error = lambda x: cprint(x, 'red', attrs=['bold'])
print_grey_on_yellow2 = lambda x: cprint(x, 'grey', 'on_yellow', end=' ')
print_grey_on_yellow = lambda x: cprint(x, 'grey', 'on_yellow')
print_yellow_on_grey2 = lambda x: cprint(x, 'yellow', 'on_grey', end=' ')
print_yellow_on_grey = lambda x: cprint(x, 'yellow', 'on_grey')
print_cyan = lambda x: cprint(x, 'cyan', attrs=['bold'])
print_warning2 = lambda x: cprint(x, 'yellow', end=' ')
print_warning = lambda x: cprint(x, 'yellow')
print_info2 = lambda x: cprint(x, 'blue', end=' ')
print_info = lambda x: cprint(x, 'blue')
print_green2 = lambda x: cprint(x, 'green', end=' ')
print_green = lambda x: cprint(x, 'green')
print_win = lambda x: cprint(x, 'yellow')

# welcome message
print_error(f.renderText('the card game!'))


class Game:
    def __init__(self, player1, player2):
        super().__init__()
        self.player1 = player1
        self.player2 = player2
        self.played_cards_1 = [False, False, False, False, False]
        self.played_cards_2 = [False, False, False, False, False]
        self.score_p1 = 0
        self.score_p2 = 0
        self.deck_1 = self.player1.get_deck()
        self.deck_2 = self.player2.get_deck()
        self.play = True
        self.winner = ''

    def start(self):
        # game count
        counter = 1
        while self.play:
            try:
                print_info2('- ' * 18)
                print_info2(f'GAME NUMBER {counter}/5')
                print_info('- ' * 18)

                # p1 and p2 deck
                p1 = self.deck_1
                p2 = self.deck_2
                print(p1)
                # print(p2)

                # receives the value entered from the players
                print_grey_on_yellow2('Select 1 card: [player 1]:')
                p1_pick = int(input())
                print_grey_on_yellow2('Select 1 card: [player 2]:')
                p2_pick = int(input())

                # call method pick
                self.pick(p1_pick, p2_pick)

                # show score and played cards table
                table = [["SCORE", self.score_p1, self.score_p2]]
                played_cards = [["Player 1", self.played_cards_1], ["Player 2", self.played_cards_2]]
                print_warning(tabulate(table, headers=["Player 1", "Player 2"], tablefmt="psql"))
                print(tabulate(played_cards, headers=["Played Cards"], tablefmt="psql"))

                counter += 1
            except ValueError:
                print_error('Incorrect Value')
            except IndexError:
                print_error('Value out of range. [1-5]')

    def pick(self, p1_pick, p2_pick):
        # check if the card has already been played
        if self.played_cards_1[p1_pick - 1] or self.played_cards_2[p2_pick - 1]:
            return print_error('Card already played!')
        else:

            # set true for card played
            self.played_cards_1[p1_pick - 1] = True
            self.played_cards_2[p2_pick - 1] = True

            # p1 stats
            p1_atk = int(self.deck_1[p1_pick - 1][0])
            p1_def = int(self.deck_1[p1_pick - 1][1])
            p1_elm = self.deck_1[p1_pick - 1][2]

            # p2 stats
            p2_atk = int(self.deck_2[p2_pick - 1][0])
            p2_def = int(self.deck_2[p2_pick - 1][1])
            p2_elm = self.deck_2[p2_pick - 1][2]

            p1_total = {
                'attack': p1_atk,
                'defense': p1_def,
                'element': p1_elm
            }
            p2_total = {
                'attack': p2_atk,
                'defense': p2_def,
                'element': p2_elm
            }

            # call the method
            self.match(p1_total, p2_total)

    def element(self, p1_el, p2_el):
        # check element advantage
        if p1_el == 'fire' and p2_el == 'ice' or \
                p1_el == 'ice' and p2_el == 'water' or \
                p1_el == 'water' and p2_el == 'fire':
            return 'p1'
        elif p2_el == 'fire' and p1_el == 'ice' or \
                p2_el == 'ice' and p1_el == 'water' or \
                p2_el == 'water' and p1_el == 'fire':
            return 'p2'
        else:
            return 0

    def match(self, p1_attack, p2_attack):
        a1 = p1_attack['attack']
        a2 = p2_attack['attack']
        d1 = p1_attack['defense']
        d2 = p2_attack['defense']
        e1 = p1_attack['element']
        e2 = p2_attack['element']
        f1 = 0
        f2 = 0
        # decide which element wins
        adv = self.element(e1, e2)
        f1 += random.randint(2, 5) if adv == 'p1' else 0
        f2 += random.randint(2, 5) if adv == 'p2' else 0

        # total players stats
        p1_sum = a1 - d2 + f1
        p2_sum = a2 - d1 + f2

        # show table stats
        table = [[a1, d2, e1, f1, p1_sum], [a2, d1, e2, f2, p2_sum]]
        print(tabulate(table, headers=["+ Attack", "- Enemy Def.", "> Element", "+ Elm. Points", "= Total"],
                       tablefmt="psql"))

        # show winner message
        if p1_sum > p2_sum:
            print_cyan(f'| P1 WINNER')
            self.score_p1 += 1
        elif p2_sum > p1_sum:
            print_cyan(f'| P2 WINNER')
            self.score_p2 += 1
        else:
            print_cyan('| DRAW')
            self.score_p1 += 1
            self.score_p2 += 1

        # check if the game is over
        if self.score_p1 == 3 or self.score_p2 == 3:
            self.play = False
            time.sleep(1)
            print_win(f.renderText('Player'))
            time.sleep(1)

            if self.score_p1 == 3 and self.score_p2 == 3:
                print_win(f.renderText('DRAW'))
                # set winner
                self.winner = 'Draw'
            elif self.score_p1 == 3:
                print_win(f.renderText(self.player1.name))
                # set winner
                self.winner = self.player1.name
            elif self.score_p2 == 3:
                print_win(f.renderText(self.player2.name))
                # set winner
                self.winner = self.player2.name
            time.sleep(1)
            print_win(f.renderText('Won'))
            time.sleep(1)

            # save on db
            score = f'{self.score_p1} x {self.score_p2}'
            data = {
                'player_1': self.player1.name,
                'player_2': self.player2.name,
                'winner': self.winner,
                'final_score': score
            }
            insert_result(data)
