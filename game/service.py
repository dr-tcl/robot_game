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

    def create_dinosaurs(self, x, y):
        loc = (x, y)
        if self._check_location_in_board_size(loc):
            Dinosaurs.objects.get_or_create(width=x, height=y)
            return True
        else:
            return False

    def create_robot(self, x, y):
        loc = (x, y)
        robot = Robot.objects.first()
        if robot:
            return False
        if loc not in self._get_dinosaurs_location() \
                and self._check_location_in_board_size(loc):
            robot = Robot.objects.create(width=x, height=y)
            self._kill_dinosaurs(robot)
            return True
        else:
            return False

    @staticmethod
    def _kill_dinosaurs(robot: Robot):
        Dinosaurs.objects.filter(Q(width=robot.width, height__in=[robot.height + 1, robot.height - 1]) |
                                 Q(height=robot.height, width__in=[robot.width + 1, robot.width - 1])).update(
            is_live=False)

    def robot_move(self, direction):
        robot = Robot.objects.first()
        if robot is None:
            return False

        if direction.lower() == "up":
            robot.height += 1
        elif direction.lower() == "down":
            robot.height -= 1
        elif direction.lower() == "right":
            robot.width += 1
        elif direction.lower() == "left":
            robot.width -= 1
        else:
            # input direction is incorrect
            return False

        loc = (robot.width, robot.height)
        if self._check_location_in_board_size(loc):
            robot.save()
            self._kill_dinosaurs(robot)
            return True
        return False
