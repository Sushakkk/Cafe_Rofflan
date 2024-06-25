from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from goods.models import Dishes
from baskets.models import Baskets
from users.models import User


def basket_add(request):
    dish_id = request.POST.get("dish_id")

    dish = Dishes.objects.get(id=dish_id)
    if request.user.is_authenticated:
        baskets = Baskets.objects.filter(user=request.user, dish=dish)

        if baskets.exists():
            basket = baskets.first()
            if basket:
                basket.quantity += 1
                basket.save()
        else:
            Baskets.objects.create(user=request.user, dish=dish, quantity=1)
    user_basket = Baskets.objects.filter(user=request.user)
    basket_items_html = render_to_string(
        "baskets/includes/included_basket.html", {"baskets": user_basket}, request=request
    )
    response_data = {
        "message": "Товар добавлен в корзину",
        "basket_items_html": basket_items_html,
    }
    return JsonResponse(response_data)


def basket_change(request, dish_slug):
    return render('includes/included_basket.html')


def basket_remove(request):  # basket_id
    # basket = Baskets.objects.get(id=basket_id)
    # basket.delete()

    return redirect(request.META['HTTP_REFERER'])
