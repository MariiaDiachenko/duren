import random
from duren.Card import *
from duren.Player import *
from duren.Battle import *
import json

class Game:
    colors = ['♠', '♣', '♦', '♥']
    numbers = [6, 7, 8, 9, 10, 11, 12, 13, 14]
    modes = ['hot_seats', 'computer']
    cards = []
    players = []

    battle = None

    mode = ''

    """One of colors"""
    atut = ''

    """Player id"""
    turn = 0

    """Player id"""
    attacker = 0

    """Player id"""
    duren = 0

    def __init__(self):
        self.cards = self.make_cards()
        self.players = self.make_players()
        self.atut = self.pick_atut()

        self.give_cards()

        self.turn = self.set_initial_turn()
        self.attacker = self.turn
        self.battle = Battle()

    #todo przetestować, rozne put card jesli player atakuje albo sie broni?
    """User Interface"""
    def put_card(self, card_id: int):
        player = self.get_player_by_id(self.turn)
        index = player.find_card_by_id(card_id)
        card = player.cards[index]

        is_attacker = player.id == self.attacker

        if self.battle.can_put_card(card, is_attacker, self.atut):
            card = player.cards.pop(index)
            self.battle.put_card(card, is_attacker)
            self.change_turn()

        #todo sprawdzanie: atak odparty? wygrana? też w zależności od tego czy gracz jest atakujacym czy nie

        #todo dobieranie kart do playerów

    def take(self):
        if self.turn != self.attacker:
            index = self.find_player_by_id(self.turn)
            self.players[index].cards.append(self.battle.attack[-1])
            self.battle.clear()
            self.pour_players_cards()

            self.change_turn()
            self.attacker = self.turn

    def pass_attack(self):
        self.battle.clear()
        self.pour_players_cards()

        self.change_turn()
        self.attacker = self.turn

    def reset(self):
        self.__init__()

    """User Interface END"""

    #todo atakujący dobiera pierwszy a potem obrońca
    def pour_players_cards(self):
        self.pour_for_player_by_id(self.attacker)
        for player in self.players:
            if player.id != self.attacker:
                self.pour_for_player_by_id(player.id)

    def pour_for_player_by_id(self, id):
        index = self.find_player_by_id(id)

        while len(self.players[index].cards) != 6:
            if len(self.cards) == 0: return
            card = self.cards.pop()
            self.players[index].cards.append(card)

    def find_player_by_id(self, id):
        for i in range(len(self.players)):
            player = self.players[i]
            if player.id == id:
                return i

        raise AssertionError('Invalid id')

    def get_player_by_id(self, id: int):
        player = [player for player in self.players if player.id == id][0]
        if not player: raise AssertionError('Invalid id')
        return player

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
        for i in range(len(cards)):
            id = i+1
            cards[i].id = id
        random.shuffle(cards)
        return cards

    def pick_atut(self):
        return random.choice(self.colors)

    def make_response(self):
        return json.dumps({'players':self.players, 'atut':self.atut, 'cardsLeft':len(self.cards), 'turn':self.turn,
                           'attacker':self.attacker, 'duren':self.duren, 'battle': self.battle}, default = lambda x: x.__dict__)

    def change_turn(self):
        self.turn = [player for player in self.players if player.id != self.turn][0].id

    def set_mode(self, mode):
        if mode in self.modes:
            self.mode = mode
        else:
            raise AssertionError('Invalid mode')
