'use strict'
const gameUrl = '/ajax_duren'
const imgUrl = '/static/cards_images/'

$(document).ready(function(){
    durenAjax( {'cmd':'init'});
    addMenuFunctions();
});

function addMenuFunctions(){
    $('#JS-reset').click(function() {
        durenAjax({'cmd':'reset'});
    });
    $('#JS-computer').click(function() {
        durenAjax({'cmd':'computer'});
    });
    $('#JS-take').click(function() {
       durenAjax({'cmd':'take'});
    });
    $('#JS-pass').click(function() {
       durenAjax({'cmd':'pass'});
    });
}

function durenAjax(json){
      $.ajax({
      url: gameUrl,
      type: 'POST',
      dataType:'json',
      contentType: 'application/json',
      data:JSON.stringify(json),
      success: function(result){
        renderGame(result);
    },
      error: function(err, s , exception){
          console.log(exception);
      }
  });

}

function renderGame(result){
    $('#JS-cardsLeft').html('cards left: ' + result.cardsLeft);
    $('#JS-atut').html('atut: ' + result.atut);
    initPlayers(result);
    initBattle(result);
    handleWin(result.duren);
    displayComp(result.vs_computer);
}

function displayComp(comp) {
    if(comp){
        $('#JS-displayComp').html('you play vs computer');
    } else {
        $('#JS-displayComp').html('');
    }
}

function handleWin(duren){
    if(duren != 0){
        let side = duren == 1? 'Bottom' : 'Top';
        $('#JS-win')
            .html('END.'+ side +' player is duren')
            .css('display', 'flex');
    } else {
        $('#JS-win')
            .html('')
            .css('display', 'none');
    }
}

function initBattle(result){
    let defenser = result.attacker == 1? 2 : 1;

    let attackCards = makeCards(result.battle.attack, true);
    $('#JS-battle__p' + result.attacker).html(attackCards);

    let defenseCards = makeCards(result.battle.defense, true);
    $('#JS-battle__p' + defenser).html(defenseCards);
}

function initPlayers(result){
    for(let key in result.players){
      let player = result.players[key]
        initPlayer(player, result.turn);
    }
}

function initPlayer(player, turn){
    // todo remove after deubg
    console.log(player.id);
    let thisPlayerTurn = player.id === turn ? true : false;
    let cards = makeCards(player.cards, true);//thisPlayerTurn);

    $('#JS-p' + player.id).html(cards);

    if (thisPlayerTurn === true) {
        addFunctionToCards(player.cards);
    }
}

function addFunctionToCards(cards){
    for(var key in cards){
        let card = cards[key]
        $('#JS-card_' + card.id).click(function(){
            putCard(card.id);
        });
    }
}

function putCard(id){
    durenAjax({'cmd':'put_card', 'data':id});
}

function makeCards(cards, show){
    let out = '';
    for(var key in cards){
        let card = cards[key]
        out += makeCard(card, show);
    }
    return out;
}

function makeCard(card, show){
    let img = show === true ? card.img : 'back.png';
    return '<div id="JS-card_' + card.id +'" class="card"><div class="card__img"><img src="/static/cards_images/'+ img +'" alt=""></div></div>';
}