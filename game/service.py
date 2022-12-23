from django.db.models import Q

from game.models import Robot, Dinosaurs


class Game:
    BOARD_MAP_SIZE = (10, 10)

    @staticmethod
    def _get_dinosaurs_location():
        dinosaurs = Dinosaurs.objects.filter(is_live=True)
        return [(i.width, i.height) for i in dinosaurs]
    
    @classmethod
    def _check_location_in_board_size(cls, loc: tuple):
        mapX, mapY = cls.BOARD_MAP_SIZE
        locX, locY = loc

        return locX <= mapX and locY <= mapY

    def create_robot(self, x, y):
        loc = (x, y)
        if loc not in self._get_dinosaurs_location() \
                and self._check_location_in_board_size(loc):
            Robot.objects.create(width=x, height=y)
            return True
        else:
            return False

    @staticmethod
    def _kill_dinosaurs(robot: Robot):
        Dinosaurs.objects.filter(Q(width=robot.width) | Q(height=robot.height)).update(is_live=False)

    def robot_move(self, direction):
        robot = Robot.objects.first()
        #check in map
        if robot is None:
            return False

        if direction.lower() is "up":
            robot.update(height=robot.height + 1)
        elif direction.lower() is "down":
            robot.update(height=robot.height - 1)
        elif direction.lower() is "right":
            robot.update(width=robot.width + 1)
        elif direction.lower() is "left":
            robot.update(width=robot.width - 1)
        else:
            return False

        self._kill_dinosaurs(robot)