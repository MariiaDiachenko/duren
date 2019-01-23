from duren.Card import Card

class Battle:
    attack = []
    defense = []

    def __init__(self):
        self.attack = []
        self.defense = []

    #todo
    def attack_defended(self):
        pass

    def can_put_card(self, card: Card, attacker: bool, atut:str):
        if card.color == atut:
            return True

        all = self.attack + self.defense
        if all == []:
            return True

        if attacker:
            """Atakujący może zucić karty jakiegokolwiek numeru co są już w battle"""
            for num in (card.num for card in all):
                if card.num == num:
                    return True
        else:
            """Obrońca broni sie tylko kartą w kolorze"""
            if self.attack[-1].color == card.color:
                return True

        return False

    def put_card(self, card: Card,  is_attacker):
        if is_attacker:
            self.attack.append(card)
        else:
            self.defense.append(card)
