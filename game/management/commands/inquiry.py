from game.service import Game
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(Game.BOARD_MAP_SIZE)
        g = Game()
        # print(g._get_dinosaurs_location())
        # print(g._check_location_in_board_size(g._get_dinosaurs_location()[0]))
        f1 = g.create_dinosaurs(9,1)
        f2 = g.create_dinosaurs(10,1)
        f3 = g.create_dinosaurs(11,1)
        f4 = g.create_robot(11,1)
        f5 = g.create_robot(10,1)
        f6 = g.create_robot(8,1)
        print(f1)
        print(f2)
        print(f3)
        print(f4)
        print(f5)
        print(f6)


