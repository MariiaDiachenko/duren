class Card():
    color = ''
    num = 0
    sign = ''
    img = ''

    def __init__(self, num, color):
        self.num = num
        self.color = color
        self.sign = self.set_sign()

    def set_sign(self):
        translate = ['6', '7', '8', '9', '10', 'J', 'Q', 'K','T']
        if 0 == self.num: return ''
        else: return translate[self.num - 6]
