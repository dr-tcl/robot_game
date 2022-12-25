import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from game.service import Game

@csrf_exempt
def create_dinosaur(request):
    if not request.method == 'POST':
        return JsonResponse({"status": False, "message": "your http method is incorrect"}, status=400)
    data = json.loads(request.body)
    x = data.get("x")
    y = data.get("y")
    if (x or y) is None:
        return JsonResponse({"status": False, "message": "x, y is required"}, status=400)
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
    if (x or y) is None:
        return JsonResponse({"status": False, "message": "x, y is required"}, status=400)
    status, result = Game.create_robot(x=x, y=y)
    if not result:
        return JsonResponse({"status": False, "message": result}, status=400)
    return JsonResponse({"status": False, "message": result}, status=200)

@csrf_exempt
def move_robot(request):
    if not request.method == 'POST':
        return JsonResponse({"status": False, "message": "your http method is incorrect"}, status=400)
    data = json.loads(request.body)
    direction = data.get("direction")
    if direction is None:
        return JsonResponse({"status": False, "message": "direction is required"}, status=400)
    status, result = Game.robot_move(direction)
    if not result:
        return JsonResponse({"status": False, "message": result}, status=400)
    return JsonResponse({"status": False, "message": result}, status=200)
