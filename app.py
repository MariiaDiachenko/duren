import pytest
from flask import Flask, render_template, request
from duren.Game import *
from duren.tests.fixtures import *
import json

app = Flask(__name__)
duren = Game()

@app.route('/')
def hot_seats():
    card = duren.players[0].cards[0]
    # for_tests(duren = duren)

    return render_template('game.jinja2', card = card)

@app.route('/ajax_duren', methods = ['POST'])
def ajax_duren():
    json = request.get_json()
    cmd = json.get('cmd', '')
    data = json.get('data', {})

    if not duren.mode:
        duren.mode = 'hot_seats'

    print(cmd)
    if cmd == 'put_card':
        duren.put_card(data)
    elif cmd == 'take':
        duren.take()
    elif cmd == 'pass':
        duren.pass_attack()
    elif cmd == 'reset':
        duren.reset()

    return duren.make_response()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5012, debug=True)

# def for_tests(**ins):
#     # cards = ins['duren'].cards
#     print('ok')
#     players = ins['duren'].players
#     out = ''
#     for player in players:
#         for x in range(len(player.cards)):
#             out = f'assert players[{x}].__dict__ == {player.cards[x].__dict__} '
#             print(out)
#         print('\n')
