import random
from duren.Card import *
from duren.Player import *

class Game:
    colors = ['♠', '♣', '♦', '♥']
    numbers = [6, 7, 8, 9, 10, 11, 12, 13, 14]
    cards = []
    players = []
    battle = {
        'atak': [],
        'obrona': []
    }

    """One of colors"""
    atut = ''

    """Player id"""
    turn = 0

    """Player id"""
    winner = 0

    def __init__(self):
        self.cards = self.make_cards()
        self.players = self.make_players()
        self.atut = self.pick_atut()

        self.give_cards()

        self.turn = self.set_initial_turn()

    def set_initial_turn(self):
        """Gracz z najmniejszą wartością karty coloru atutu zaczyna, a jeśli nikt nie ma atutu to pierwszy lepszy"""
        starting_id = self.players[0].id
        minimal_for_players = []
        for player in self.players:
            in_atut = player.get_cards_in_atut(self.atut)
            if in_atut:
                minimal_for_player = min(in_atut, key = lambda card: card.num)
                minimal_for_players.append((player, minimal_for_player))

        if minimal_for_players:
            starting_id = min(minimal_for_players, key= lambda x: x[1].num)[0].id

        return starting_id

    def give_cards(self):
        player_num = 0
        for player_num in range(len(self.players)):
            cards = []
            for i in range(6):
                cards.append(self.cards.pop())
            self.players[player_num].cards = cards

    def pick_random_card(self)->Card:
        random.choice(range(len(self.cards)))

    def make_players(self, quantity = 2)->list:
        return [Player(x) for x in range(1, quantity+1)]

    def make_cards(self)->list:
        cards = [Card(num, col) for num in self.numbers for col in self.colors]
        random.shuffle(cards)
        return cards

    def pick_atut(self):
        return random.choice(self.colors)
