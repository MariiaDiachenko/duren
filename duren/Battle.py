class Battle:
    attacker_id = 0
    defender_id = 0

    attack = []
    defense = []

    def __init__(self, attacker_id:int, defender_id: int):
        self.attacker_id = attacker_id
        self.defender_id = defender_id
