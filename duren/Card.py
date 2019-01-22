class Card():
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

        translate = [f'6{suffix}.png', f'7{suffix}.png', f'8{suffix}.png', f'9{suffix}.png', f'X{suffix}.png', f'J{suffix}.png', f'K{suffix}.png', f'Q{suffix}.png', f'A{suffix}.png']

        if 0 == self.num: return ''
        else: return translate[self.num - 6]
