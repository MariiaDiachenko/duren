'use strict'
const gameUrl = '/ajax_duren'
const imgUrl = '/static/cards_images/'

$(document).ready(function(){
    durenAjax( {'cmd':'init'}, function(result){
        renderGame(result);
    });
});

function durenAjax(json, success){
      $.ajax({
      url: gameUrl,
      type: 'POST',
      dataType:'json',
      contentType: 'application/json',
      data:JSON.stringify(json),
      success:success,
      error: function(err, s , exception){
          console.log(exception);
      }
  });

}

function renderGame(result){
    $('#JS-cardsLeft').html('cards left: ' + result.cardsLeft);
    $('#JS-atut').html('atut: ' + result.atut);

    for(let key in result.players){
      let player = result.players[key]
      initPlayer(player, result.turn);
    }


    console.log(result);
}

//todo addFunctionToCard i zmiany na serwerze i tyle
function initPlayer(player, turn){
    let cards = '';
    let thisPlayerTurn = player.id === turn ? true : false;
    for(var key in player.cards){
        let card = player.cards[key]
        cards += makeCard(card, thisPlayerTurn);
    }
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

// #todo send ajax request
function putCard(id){
    durenAjax({'cmd':'put_card', 'data':id}, function(result){
        renderGame(result);
    });
}

function makeCard(card, show){
    let img = show === true ? card.img : 'back.png';
    return '<div id="JS-card_' + card.id +'" class="card"><div class="card__img"><img src="/static/cards_images/'+ img +'" alt=""></div></div>';
}