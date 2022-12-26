import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from cerberus import Validator
from game.service import Game

schema = {'x': {'type': 'integer', 'min': 1, "max": 10, 'required': True},
          'y': {'type': 'integer', 'min': 1, "max": 10, 'required': True}}
v = Validator()


@csrf_exempt
def create_dinosaur(request):
    if not request.method == 'POST':
        return JsonResponse({"status": False, "message": "your http method is incorrect"}, status=400)
    data = json.loads(request.body)
    x = data.get("x")
    y = data.get("y")
    if not v.validate(data, schema):
        return JsonResponse({"status": False, "message": "your input params not valid"}, status=400)
    status, result = Game.create_dinosaurs(x=x, y=y)
    if not result:
        return JsonResponse({"status": False, "message": result}, status=400)
    return JsonResponse({"status": False, "message": result}, status=200)


@csrf_exempt
def create_robot(request):
    if not request.method == 'POST':
        return JsonResponse({"status": False, "message": "your http method is incorrect"}, status=400)
    data = json.loads(request.body)
    x = data.get("x")
    y = data.get("y")
    if not v.validate(data, schema):
        return JsonResponse({"status": False, "message": "your input params not valid"}, status=400)
    status, result = Game.create_robot(x=x, y=y)
    if not result:
        return JsonResponse({"status": False, "message": result}, status=400)
    return JsonResponse({"status": False, "message": result}, status=200)


@csrf_exempt
def move_robot(request):
    if not request.method == 'POST':
        return JsonResponse({"status": False, "message": "your http method is incorrect"}, status=400)
    data = json.loads(request.body)
    schema = {'direction': {'type': 'string', 'required': True}}
    direction = data.get("direction")
    if not v.validate(data, schema):
        return JsonResponse({"status": False, "message": "your input params not valid"}, status=400)
    status, result = Game.robot_move(direction)
    if not result:
        return JsonResponse({"status": False, "message": result}, status=400)
    return JsonResponse({"status": True, "message": result}, status=200)
