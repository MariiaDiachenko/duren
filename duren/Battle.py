from duren.Card import Card

class Battle:
    attack = []
    defense = []

    def __init__(self):
        self.attack = []
        self.defense = []

    def can_put_card(self, card: Card, attacker: bool, atut:str)->bool:

        all = self.attack + self.defense
        if all == []:
            return True

        if attacker:
            """Atakujący może zucić atut"""
            if card.color == atut:
                return True
            """albo karty jakiegokolwiek numeru co są już w battle"""
            for num in (card.num for card in all):
                if card.num == num:
                    return True
        else:
            """Obrońca broni sie wyższą kartą w kolorze"""
            attack_card = self.attack[-1]
            if attack_card.color == card.color and attack_card.num < card.num:
                return True
            """Albo atutem"""
            if card.color == atut:
                """Chyba że broni się przed atutem, wtedy musi mieć większy atut"""
                if attack_card.color == atut and attack_card.num > card.num:
                    return False
                return True


        return False

    def put_card(self, card: Card,  is_attacker):
        if is_attacker:
            self.attack.append(card)
        else:
            self.defense.append(card)

    def clear(self):
        self.attack = []
        self.defense = []
