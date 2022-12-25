from django.urls import path

from game import apis

urlpatterns = [
    path('create_dinosaur/', apis.create_dinosaur),
    path('create_robot/', apis.create_robot),
    path('move_robot/', apis.move_robot),
]
