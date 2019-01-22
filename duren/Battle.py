from duren.Card import Card

class Battle:
    attack = []
    defense = []

    def attack_with_card(self, card: Card):
        self.attack.append(card)
