import pytest
from duren.Game import Game

def test_make_cards():
    duren = Game()
    cards = duren.cards
    for card in cards:
        assert card.id
        assert card.color
        assert card.num
        assert card.img
    """stan kart po rozdaniu dla domyślnie 2 graczy"""
    assert 24 == len(duren.cards)
    for player in duren.players:
        assert 6 == len(player.cards)

    assert duren.atut != ''
    assert duren.turn != 0
    assert duren.attacker != 0

    assert duren.battle != None

