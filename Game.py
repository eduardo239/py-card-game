from time import sleep
from helpers import *


class Game:
    def __init__(self, players):
        self.player1 = players[0]
        self.player2 = players[1]
        self.played_cards_1 = [False, False, False, False, False]
        self.played_cards_2 = [False, False, False, False, False]

    def match(self, j_p1, j_p2):
        p1_at = self.player1.deck[j_p1 - 1][1]
        p2_at = self.player2.deck[j_p2 - 1][1]
        p1_df = self.player1.deck[j_p1 - 1][2]
        p2_df = self.player2.deck[j_p2 - 1][2]

        self.played_cards_1[j_p1 - 1] = True
        self.played_cards_2[j_p2 - 1] = True

        p1_atk = p1_at - p2_df
        p2_atk = p2_at - p1_df

        print(f'player 1 ATK {p1_at}, p2 DEFENSE {p2_df} == {p1_atk}')
        print(f'player 2 ATK {p2_at}, p1 DEFENSE {p1_df} == {p2_atk}')

        if p1_atk > p2_atk:
            msg_success('Player 1 Venceu essa luta')
            self.player1.score += 1
            if self.player1.score == 3:
                self.win_message(self.player1.name)
                self.player1.win += 1
                self.player2.lose += 1
        elif p2_atk > p1_atk:
            msg_success('Player 2 Venceu essa luta')
            self.player2.score += 1
            if self.player2.score == 3:
                self.win_message(self.player2.name)
                self.player2.win += 1
                self.player1.lose += 1
        else:
            print('Draw')
            self.player1.score += 1
            self.player2.score += 1
            if self.player2.score == 3:
                self.win_message(self.player2.name)
                self.player2.win += 1
                self.player1.lose += 1
            if self.player1.score == 3:
                self.win_message(self.player1.name)
                self.player1.win += 1
                self.player2.lose += 1

        print('- ' * 20)
        print(f'PLAYER {self.player1.name}: {self.player1.score}'
              f' x PLAYER {self.player2.name}: {self.player2.score}')
        print('- ' * 20)

    def get_played_cards(self):
        return self.played_cards_1, self.played_cards_2

    def win_message(self, player):
        sleep(1)
        print(' .-. ' * 10)
        sleep(1)
        print('Fim de jogo')
        sleep(1)
        print(' .-. ' * 10)
        sleep(1)
        msg_success(f'Jogador {player} venceu')
        sleep(1)
        print(f'Placar FINAL: {self.player1.score} x {self.player2.score}')
        sleep(1)
