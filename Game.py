from time import sleep

from db import insert_result
from messages import *
from tabulate import tabulate

FINAL_SCORE = 3
ELEMENT_ATTACK = 2


class Game:
    def __init__(self, players):
        self.player1 = players[0]
        self.player2 = players[1]
        self.played_cards_1 = [False, False, False, False, False]
        self.played_cards_2 = [False, False, False, False, False]
        self.final_score = ''
        self.winner = ''
        self.loser = ''

    def match(self, j_p1, j_p2):
        p1_el = self.player1.deck[j_p1 - 1][0]
        p2_el = self.player2.deck[j_p2 - 1][0]
        p1_at = self.player1.deck[j_p1 - 1][1]
        p2_at = self.player2.deck[j_p2 - 1][1]
        p1_df = self.player1.deck[j_p1 - 1][2]
        p2_df = self.player2.deck[j_p2 - 1][2]

        self.played_cards_1[j_p1 - 1] = True
        self.played_cards_2[j_p2 - 1] = True

        p1_atk = p1_at - p2_df
        p2_atk = p2_at - p1_df

        p1_element = 0
        p2_element = 0

        # self.el_win(p1_el, p2_el)

        if p1_el == 'fire' and p2_el == 'nature':
            p1_atk += 2
            p1_element = ELEMENT_ATTACK
        elif p1_el == 'nature' and p2_el == 'water':
            p1_atk += 2
            p1_element = ELEMENT_ATTACK
        elif p1_el == 'water' and p2_el == 'fire':
            p1_atk += 2
            p1_element = ELEMENT_ATTACK

        if p2_el == 'fire' and p1_el == 'nature':
            p2_atk += 2
            p2_element = ELEMENT_ATTACK
        elif p2_el == 'nature' and p1_el == 'water':
            p2_atk += 2
            p2_element = ELEMENT_ATTACK
        elif p2_el == 'water' and p1_el == 'fire':
            p2_atk += 2
            p2_element = ELEMENT_ATTACK

        data = {
            'p1_name': self.player1.name,
            'p2_name': self.player2.name,
            'p1_fight': p1_atk,
            'p2_fight': p2_atk,
            'p1_atk': p1_at,
            'p2_atk': p2_at,
            'p1_def': p1_df,
            'p2_def': p2_df,
            'p1_elm': p1_el,
            'p2_elm': p2_el,
            'p1_elm_adv': p1_element,
            'p2_elm_adv': p2_element,
        }

        self.battle_message(data)

        if p1_atk > p2_atk:
            msg_status('Player 1 won this fight.')
            self.player1.score += 1
            if self.player1.score == FINAL_SCORE:
                self.win_message(self.player1.name)

        elif p2_atk > p1_atk:
            msg_status('Player 2 won this fight.')
            self.player2.score += 1
            if self.player2.score == FINAL_SCORE:
                self.win_message(self.player2.name)

        else:
            msg_status('Draw !')
            self.player1.score += 1
            self.player2.score += 1

            if self.player1.score == FINAL_SCORE:
                self.win_message(self.player1.name)

            if self.player2.score == FINAL_SCORE:
                self.win_message(self.player2.name)

        print('- ' * 20)
        print(f'PLAYER {self.player1.name}: {self.player1.score}'
              f' x PLAYER {self.player2.name}: {self.player2.score}')
        print('- ' * 20)

    def get_played_cards(self):
        return self.played_cards_1, self.played_cards_2

    def win_message(self, player):
        self.winner = player
        self.final_score = f'{self.player1.score} x {self.player2.score}'
        sleep(0.75)
        print(' .-. ' * 10)
        sleep(0.75)
        msg_success('Game Over')
        sleep(0.75)
        print(' .-. ' * 10)
        sleep(0.75)
        msg_win(f'{player} WON!')
        sleep(0.75)
        msg_success(f'Final Score: {self.player1.score} x {self.player2.score}')
        sleep(0.75)

        data = {
            'player_1': self.player1.name,
            'player_2': self.player2.name,
            'winner': self.winner,
            'final_score': self.final_score
        }
        insert_result(data)

    def if_win(self, player):
        pass

    def el_win(self, p1_el, p2_el):
        pass

    def battle_message(self, data):
        print(tabulate([["Name", "Attack", "Defense", "Element", "Element Adv.", "Result"],

                        [data["p1_name"], data["p1_atk"], data["p1_def"], data["p1_elm"],
                         data["p1_elm_adv"] if data["p1_elm"] else 0, data["p1_fight"]],

                        [data["p2_name"], data["p2_atk"], data["p2_def"], data["p2_elm"],
                         data["p2_elm_adv"] if data["p2_elm"] else 0, data["p2_fight"]]],

                       headers="firstrow", tablefmt="psql"))
