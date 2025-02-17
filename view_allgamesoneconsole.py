def console_games(request, platform):
    games = Game.objects.filter(platform=platform)
    return render(request, 'shop/console_games.html', {'games': games, 'platform': platform})
