def basket_view(request):
    basket_items = BasketItem.objects.all()
    total_price = sum(item.game.price * item.quantity for item in basket_items)
    return render(request, 'shop/basket.html', {'basket_items': basket_items, 'total_price': total_price})
