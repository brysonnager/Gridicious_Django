from django.db import models

class Game(models.Model):
    creation_datetime = models.DateTimeField('Date Created')



class Player(models.Model):
    player_name = models.CharField(max_length=15)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    num_moves_remaining = models.IntegerField()

    def __str__(self):
        return self.player_name.title()
    
class Move(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    new_coordinates_text = models.CharField(max_length=3)
    did_player_choose_move = models.BooleanField()

    x_coord = models.IntegerField(default=2)
    y_coord = models.IntegerField(default=2)


    def __str__(self):
        if self.did_player_choose_move:
            return "P %d_%d" % (self.x_coord, self.y_coord)
        else:
            return "R %d_%d" % (self.x_coord, self.y_coord)

