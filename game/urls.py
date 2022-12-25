from django.urls import path

from game import apis, views


urlpatterns = [
    path('create_dinosaur/', apis.create_dinosaur),
    path('create_robot/', apis.create_robot),
    path('create_robot/', apis.create_robot),
    path('show_game/', views.show_game),
]
