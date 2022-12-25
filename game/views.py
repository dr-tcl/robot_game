from django.shortcuts import render
# from service import Game


# Create your views here.

def show_game(request):
    return render(request, "base.html", context={})
