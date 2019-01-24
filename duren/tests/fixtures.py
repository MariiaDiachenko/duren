import pytest
from duren.Game import *

# '♠', '♣', '♦', '♥']
@pytest.fixture
def case_1():
    duren = Game()

    p2_cards_data =[
        (12,'♣','QC.png'),
        (12, '♥', 'QH.png'),
        (11, '♦', 'JD.png'),
        (6, '♥', '6H.png'),
        (9, '♠', '9S.png'),
        (13, '♣', 'KC.png'),
    ]

    p1_cards = [
        (9, '♣', '9C.png'),
        (14, '♦', 'AD.png'),
        (8, '♠', '8S.png'),
        (8, '♦', '8D.png'),
        (13, '♠', 'KS.png'),
        (7, '♥', '7H.png'),
    ]

    duren.turn = 2
    duren.attacker = 2
    duren.atut = '♥'
    duren.players[0] = Player(1)
    duren.players[1] = Player(2)

    id = 0
    duren.players[0].cards = make_cards_from(p1_cards)
    duren.players[1].cards = make_cards_from(p2_cards_data)

    return duren

def make_cards_from(cards_data):
    cards = [Card(num, color) for num, color, img in cards_data]
    for card in cards:
        card.id = make_cards_from.id
        id += 1
        print(id)
