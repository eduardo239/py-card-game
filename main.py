from Cards import Card
from Player import Player
from Game import Game

print('- '*50)
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

        print('/\\'*20)
        print(f'Jogos: player 1 venceu {p1.win} vezes, e perdeu {p1.lose}')
        print(f'Jogos: player 2 venceu {p2.win} vezes, e perdeu {p2.lose}')
        print('/\\'*20)
        while play:
            print('Primeira jogada:')
            try:
                j1_p1 = int(input('[p1] Carta a ser jogada [1-5]: '))
                j1_p2 = int(input('[p2] Carta a ser jogada [1-5]: '))

                g1.match(j1_p1, j1_p2)
                # jogar mais ?
                if p1.score >= 5 or p2.score >= 5:
                    play = False
            except IndexError:
                print('Valor fora de alcance.')
            except ValueError:
                print('Caracter inválido.')

        p1.score = 0
        p2.score = 0

print('- '*50)
print('- '*50)
print('- '*50)
