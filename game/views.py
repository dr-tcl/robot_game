from django.shortcuts import render, redirect
from django.urls import reverse

from .form import RobotFormItem
from .service import Game


def show_game(request):
    data = Game.show_game_map()
    form1 = RobotFormItem(request.POST or None)
    form2 = RobotFormItem(request.POST or None)
    return render(request, "base.html", context={"form1": form1, "form2": form2, "data": data})


def robot_form(request):
    form = RobotFormItem(request.POST or None)
    if form.is_valid():
        x = form.cleaned_data.get("x")
        y = form.cleaned_data.get("y")
        re = Game.create_robot(x, y)
        print(re)
        return redirect(reverse("show_game"))

    return redirect(reverse("show_game"))


def dinosaur_form(request):
    form = RobotFormItem(request.POST or None)
    if form.is_valid():
        x = form.cleaned_data.get("x")
        y = form.cleaned_data.get("y")
        re = Game.create_dinosaurs(x, y)
        print(re)
        return redirect(reverse("show_game"))

    return redirect(reverse("show_game"))
