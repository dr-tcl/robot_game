from django.db.models import Q

from game.models import Robot, Dinosaurs


class Game:
    BOARD_MAP_SIZE = (10, 10)

    @staticmethod
    def _get_dinosaurs_location():
        dinosaurs = Dinosaurs.objects.filter()
        return [(i.width, i.height) for i in dinosaurs]

    @classmethod
    def _check_location_in_board_size(cls, loc: tuple):
        mapX, mapY = cls.BOARD_MAP_SIZE
        locX, locY = loc

        return locX <= mapX and locY <= mapY

    @classmethod
    def create_dinosaurs(cls, x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            return False, "your x,y parameter must be integer"
        loc = (x, y)
        if cls._check_location_in_board_size(loc):
            Dinosaurs.objects.get_or_create(width=x, height=y)
            return True, "create dinosaur successfully"
        else:
            return False, "dinosaur location is not in map size"

    @classmethod
    def create_robot(cls, x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            return False, "your x,y parameter must be integer"
        loc = (x, y)
        robot = Robot.objects.first()
        if robot:
            return False, "you create robot before"
        if loc not in cls._get_dinosaurs_location() \
                and cls._check_location_in_board_size(loc):
            robot = Robot.objects.create(width=x, height=y)
            cls._kill_dinosaurs(robot)
            return True, "create robot successfully"
        else:
            return False, "robot location is not in map size or on dinosaurs location"

    @staticmethod
    def _kill_dinosaurs(robot: Robot):
        Dinosaurs.objects.filter(Q(width=robot.width, height__in=[robot.height + 1, robot.height - 1]) |
                                 Q(height=robot.height, width__in=[robot.width + 1, robot.width - 1])).update(
            is_live=False)

    @classmethod
    def robot_move(cls, direction):
        robot = Robot.objects.first()
        if robot is None:
            return False, "you haven't created robot"

        if direction.lower() == "up":
            robot.height += 1
        elif direction.lower() == "down":
            robot.height -= 1
        elif direction.lower() == "right":
            robot.width += 1
        elif direction.lower() == "left":
            robot.width -= 1
        else:
            return False, "input direction is incorrect"

        loc = (robot.width, robot.height)
        if loc in cls._get_dinosaurs_location():
            return False, f"{direction} cell of robot get by dinosaur before"
        if cls._check_location_in_board_size(loc):
            robot.save()
            cls._kill_dinosaurs(robot)
            return True, f"robot moved {direction} successfully"
        return False, "robot cant move to out of board size"

    def show_game_map(self):
        robot = Robot.objects.first()
        dinosaurs = Dinosaurs.objects.all()
        map = [[None for i in range(self.BOARD_MAP_SIZE[1])] for i in range(self.BOARD_MAP_SIZE[0])]
        if robot:
            map[robot.height].insert(robot.width, "R")
        for dinosaur in dinosaurs:
            map[dinosaur.height].insert(dinosaur.width, "D")
        return map
