from django.contrib import admin

from .models import Game, Player, Move

admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Move)
