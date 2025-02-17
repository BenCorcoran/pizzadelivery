def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'shop/game_detail.html', {'game': game})
