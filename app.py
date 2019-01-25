import pytest
from flask import Flask, render_template, request
from duren.Game import *

app = Flask(__name__)
duren = Game()

@app.route('/')
def hot_seats():
    #todo remove after debug
    # duren.cards = []

    return render_template('game.jinja2')

@app.route('/ajax_duren', methods = ['POST'])
def ajax_duren():
    json = request.get_json()
    cmd = json.get('cmd', '')
    data = json.get('data', {})

    print(cmd)
    if cmd == 'put_card':
        duren.put_card(data)
    elif cmd == 'take':
        duren.take()
    elif cmd == 'pass':
        duren.pass_attack()
    elif cmd == 'computer':
        duren.reset()
        duren.vs_computer = False if duren.vs_computer == True else True
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
