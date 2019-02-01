import random
from duren.Card import *
from duren.Player import *
from duren.Battle import *
import json

class Game:
    colors = ['♠', '♣', '♦', '♥']
    numbers = [6, 7, 8, 9, 10, 11, 12, 13, 14]
    cards = []
    players = []

    battle = None

    vs_computer = False

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
        self.duren = 0

        self.give_cards()

        self.turn = self.set_initial_turn()
        self.attacker = self.turn
        self.battle = Battle()

    def put_card(self, card_id: int):
        if self.duren != 0:
            return

        player = self.get_player_by_id(self.turn)
        index = player.find_card_by_id(card_id)
        card = player.cards[index]

        is_attacker = player.id == self.attacker

        if self.battle.can_put_card(card, is_attacker, self.atut):
            card = player.cards.pop(index)
            self.battle.put_card(card, is_attacker)
            self.handle_win()
            self.change_turn()

            if self.vs_computer:
                self.computer_move()

    def computer_move(self):
        if self.duren != 0:
            return

        player = self.get_player_by_id(self.turn)
        is_attacker = player.id == self.attacker
        puttable_cards = sorted(self.battle.get_puttable_cards(player.cards, is_attacker, self.atut), key=lambda x: x.num)

        if puttable_cards == []:
            if is_attacker:
                self.battle.clear()
                self.pour_players_cards()

                self.change_turn()
                self.attacker = self.turn
                return
            else:
                self.take()
                self.computer_move()
                return
        else:
            not_atut_cards = sorted([card for card in puttable_cards if card.color != self.atut], key=lambda x: x.num)
            if not_atut_cards != []:
                index = player.find_card_by_id(not_atut_cards[0].id)
                card = player.cards.pop(index)
                self.battle.put_card(card, is_attacker)
            else:
                index = player.find_card_by_id(puttable_cards[0].id)
                card = player.cards.pop(index)
                self.battle.put_card(card, is_attacker)

            self.handle_win()
            self.change_turn()

    def take(self):
        if self.turn != self.attacker and self.duren == 0:
            index = self.find_player_by_id(self.turn)
            self.players[index].cards += self.battle.get_all()
            self.battle.clear()
            self.pour_players_cards()

            self.attacker = self.turn

    def pass_attack(self):
        if self.turn == self.attacker and self.duren == 0:
            self.battle.clear()
            self.pour_players_cards()

            self.change_turn()
            self.attacker = self.turn

            if self.vs_computer:
                self.computer_move()

    def reset(self):
        self.__init__()
        self.duren = 0

    def handle_win(self):
        for player in self.players:
            if player.cards == []:
                self.duren = [player.id for player in self.players if len(player.cards)][0]

    def pour_players_cards(self):
        """atakujący dobiera pierwszy a potem obrońca"""
        self.pour_for_player_by_id(self.attacker)
        for player in self.players:
            if player.id != self.attacker:
                self.pour_for_player_by_id(player.id)

    def pour_for_player_by_id(self, id):
        index = self.find_player_by_id(id)

        while len(self.players[index].cards) < 6 and len(self.cards) != 0:
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
                           'attacker':self.attacker, 'duren':self.duren, 'battle': self.battle, 'duren':self.duren, 'vs_computer':self.vs_computer}, default = lambda x: x.__dict__)

    def change_turn(self):
        self.turn = [player for player in self.players if player.id != self.turn][0].id

    def set_mode(self, mode):
        if mode in self.modes:
            self.mode = mode
        else:
            raise AssertionError('Invalid mode')
