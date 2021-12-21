from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from datetime import datetime

from .helper import *
from .models import Game, Player, Move


def index(request):
    return render(request, 'play/index.html')



def singleplayer(request):
    if 'current_game_id' not in request.session:
        return start_singleplayer(request)
    else:
        game = get_object_or_404(Game, pk=request.session['current_game_id'])
        player = get_object_or_404(Player, pk=request.session['current_player_id'])
        high_score, hs_name = get_high_score_and_hs_name()
        try:
            move = player.move_set.all().last()
        except:
            move = None
        x_coord, y_coord = get_current_coordinates(player)
        data = {
            'location_x': x_coord,
            'location_y': y_coord,
            'moves_remaining': player.num_moves_remaining,
            'high_score': high_score,
            'hs_name': hs_name,
            'score': len(player.move_set.all()),
            'game': game,
            'player': player,
            'move': move,
        }
        return render(request, 'play/singleplayer.html', data)

def start_singleplayer(request):

    new_singleplayer_game = Game(creation_datetime = timezone.now())
    new_singleplayer_game.save()
    request.session['current_game_id'] = new_singleplayer_game.pk

    new_player_name = "Player1"
    if 'player_name' in request.session:
        new_player_name = request.session['player_name']
    new_player = Player(player_name=new_player_name, game=new_singleplayer_game)
    new_player.num_moves_remaining = 5
    new_player.save()

    
    request.session['current_player_id'] = new_player.pk

    """
    request.session['player_x_coord'] = 2
    request.session['player_y_coord'] = 2
    request.session['moves_remaining'] = 5
    """

    return HttpResponseRedirect(reverse('singleplayer'))

def submit_name(request):
    player = get_object_or_404(Player, pk=request.session['current_player_id'])
    player.player_name = request.POST['new_player_name']
    player.save()
    request.session['player_name'] = request.POST['new_player_name']
    return HttpResponseRedirect(reverse('singleplayer'))

def random_move(request):
    player = get_object_or_404(Player, pk=request.session['current_player_id'])
    execute_random_move(player)
    return HttpResponseRedirect(reverse('singleplayer'))

def center_return(request):
    player = get_object_or_404(Player, pk=request.session['current_player_id'])
    execute_center_return(player)
    return HttpResponseRedirect(reverse('singleplayer'))


def rules(request):
    return render(request, 'play/rulespage.html')



