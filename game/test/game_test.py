import pytest
from game.models import Robot, Dinosaurs
from game.service import Game


class TestGame:
    def test_create_robot_model(self):
        assert Robot.objects.all().count() == 0

    def test_create_dinosaurs_model(self):
        assert Dinosaurs.objects.all().count() == 0

    def test_create_robot_pass(self):
        x, y = 10, 1
        statusResponse, message = Game.create_robot(x, y)
        assert statusResponse
        assert message == "create robot successfully"

    def test_create_robot_fail(self):
        x, y = 10, "1"
        statusResponse, message = Game.create_robot(x, y)
        assert not statusResponse
        assert message == "your x,y parameter must be integer"

    def test_create_dinosaur_pass(self):
        x, y = 10, 1
        statusResponse, message = Game.create_dinosaurs(x, y)
        assert statusResponse
        assert message == "create dinosaur successfully"

    def test_create_dinosaur_fail(self):
        x, y = 10, "1"
        statusResponse, message = Game.create_dinosaurs(x, y)
        assert not statusResponse
        assert message == "your x,y parameter must be integer"
