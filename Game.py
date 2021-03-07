from time import sleep


class Game:
    def __init__(self, players):
        self.player1 = players[0]
        self.player2 = players[1]

    def match(self, j_p1, j_p2):

        print(self.player1.deck)
        print(self.player2.deck)

        p1_card_selected = self.player1.deck[j_p1 - 1]
        p2_card_selected = self.player2.deck[j_p2 - 1]
        p1_attack = p1_card_selected[1]
        p2_attack = p2_card_selected[1]
        p1_defense = p1_card_selected[2]
        p2_defense = p2_card_selected[2]
        print(f'p1 atk {p1_attack}, p1 def {p1_defense}')
        print(f'p2 atk {p2_attack}, p2 def {p2_defense}')

        p1_atk = p1_attack - p2_defense
        p2_atk = p2_attack - p1_defense

        if p1_atk > p2_atk:
            self.player1.score += 1
            if self.player1.score == 5:
                sleep(1)
                print(' .-. ' * 10)
                sleep(1)
                print('Fim de jogo')
                sleep(1)
                print(' .-. ' * 10)
                sleep(1)
                print(f'Jogador {self.player2.name} venceu')
                sleep(1)
                self.player1.win += 1
                self.player2.lose += 1
        elif p2_atk > p1_atk:
            self.player2.score += 1
            if self.player2.score == 5:
                sleep(1)
                print(' .-. ' * 10)
                sleep(1)
                print('Fim de jogo')
                sleep(1)
                print(' .-. ' * 10)
                sleep(1)
                print(f'Jogador {self.player2.name} venceu')
                sleep(1)
                self.player2.win += 1
                self.player1.lose += 1
        else:
            print('Draw')
            self.player1.score += 1
            self.player2.score += 1

        print('- ' * 20)
        print(f'PLAYER {self.player1.name}: {self.player1.score}'
              f' x PLAYER {self.player2.name}: {self.player2.score}')
        print('- ' * 20)

