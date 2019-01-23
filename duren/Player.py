class Player():
    id = 0
    cards = []
    attacker = False

    def __init__(self, id):
        self.id = id

    def get_cards_in_atut(self, atut: str)->list:
        return [card for card in self.cards if card.color == atut]

    def find_card_by_id(self, id):
        for i in range(len(self.cards)):
            if self.cards[i].id == id:
                return i
        raise AssertionError('Card with that id not in player cards')
