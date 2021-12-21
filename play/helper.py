import random

from django.shortcuts import get_object_or_404

from .models import Game, Player, Move


def execute_center_return(player):
    moves_remaining_before_turn = player.num_moves_remaining
    if moves_remaining_before_turn < 1:
        return 1
    
    player.num_moves_remaining = moves_remaining_before_turn - 1
    player.save()

    new_move = Move(
        player=player,
        x_coord = 2,
        y_coord = 2,
        new_coordinates_text = "2_2",
        did_player_choose_move = True,
        )
    new_move.save()

    return 0

def execute_random_move(player):
    try:
        latest_move = player.move_set.last()
        x = latest_move.x_coord
        y = latest_move.y_coord
    except:
        x = 2
        y = 2

    if (x==1 or x==3) and (y==1 or y==3):
        did_player_start_in_corner=True
    else:
        did_player_start_in_corner=False
    
    match random.choice([0,1,2,3]):
        case 0:
            x-=1
        case 1:
            x+=1
        case 2:
            y-=1
        case 3:
            y+=1

    if 1<=x<=3 and 1<=y<=3:
        if did_player_start_in_corner == True:
            player.num_moves_remaining += 1
    else:
        player.num_moves_remaining = 0

    player.save()

    new_move = Move(
        player=player,
        x_coord = x,
        y_coord = y,
        new_coordinates_text = "%d_%d" % (x, y) ,
        did_player_choose_move = False ,
        )
    new_move.save()

    return
    
def get_high_score_and_hs_name():

    hs = 0
    hs_name = "NA"
    for player in Player.objects.all():
        score = len(player.move_set.all())
        if score > hs:
            hs = score
            hs_name = player.player_name
    return hs, hs_name

def get_current_coordinates(player):
    try:
        latest_move = player.move_set.last()
        return latest_move.x_coord, latest_move.y_coord
    except:
        return 2, 2




