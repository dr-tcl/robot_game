from game.service import Game
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(Game.BOARD_MAP_SIZE)
        g = Game()
        print(g.show_game_map())


