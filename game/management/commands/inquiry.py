from game.service import Game
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(Game.BOARD_MAP_SIZE)
        g = Game()
        print(g._get_dinosaurs_location())
        print(g._check_location_in_board_size(g._get_dinosaurs_location()[0]))


