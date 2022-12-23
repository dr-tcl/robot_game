from django.shortcuts import render
from service import Game
# Create your views here.

g=Game()
print(g._get_dinosaurs_location())
print(Game.BOARD_MAP_SIZE)