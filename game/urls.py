from django.urls import path

from game import apis, views

urlpatterns = [
    path('create_dinosaur/', apis.create_dinosaur),
    path('create_robot/', apis.create_robot),
    path('move_robot/', apis.move_robot),
    path('show_game/', views.show_game, name="show_game"),
    path('submit_robot_form/', views.robot_form, name="submit_robot_form"),
    path('submit_dinosaur_form/', views.dinosaur_form, name="submit_dinosaur_form"),
]
