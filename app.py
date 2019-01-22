from flask import Flask
from duren.Game import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    duren = Game()

    # for_tests(duren = duren)

    return 'Hello World!'


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