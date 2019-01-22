class Player():
    id = 0
    player_actions = []
    cards = []

    def __init__(self, id):
        self.id = id

    def get_cards_in_atut(self, atut: str)->list:
        return [card for card in self.cards if card.color == atut]
