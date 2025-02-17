from django.shortcuts import render, get_object_or_404, redirect
from .models import Game

def game_list(request):
    games = Game.objects.all()
    return render(request, 'shop/game_list.html', {'games': games})
