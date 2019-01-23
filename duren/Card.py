class Card():
    id = 0
    color = ''
    num = 0
    img = ''

    def __init__(self, num, color):
        self.num = num
        self.color = color
        self.img = self.set_img()

    def set_img(self):
        suffix = ''
        if self.color == '♣':
            suffix = 'C'
        elif self.color == '♦':
            suffix = 'D'
        elif self.color == '♥':
            suffix = 'H'
        else:
            suffix = 'S'

        translate = [ x.format(suffix = suffix) for x in ['6{suffix}.png', '7{suffix}.png', '8{suffix}.png', '9{suffix}.png', 'X{suffix}.png', 'J{suffix}.png', 'K{suffix}.png', 'Q{suffix}.png', 'A{suffix}.png']]

        if 0 == self.num: return ''
        else: return translate[self.num - 6]
