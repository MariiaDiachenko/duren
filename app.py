from flask import Flask, render_template
from duren.Game import *

app = Flask(__name__)


@app.route('/')
def hot_seats():
    duren = Game()
    card = duren.players[0].cards[0]
    # for_tests(duren = duren)

    return render_template('game.jinja2', card = card)


if __name__ == '__main__':
    app.run()

def for_tests(**ins):
    # cards = ins['duren'].cards
    print('ok')
    players = ins['duren'].players
    out = ''
    for player in players:
        for x in range(len(player.cards)):
            out = f'assert players[{x}].__dict__ == {player.cards[x].__dict__} '
            print(out)
        print('\n')