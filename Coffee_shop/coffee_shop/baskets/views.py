from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from goods.models import Dishes
from baskets.models import Baskets
from users.models import User
from baskets.utils import get_user_baskets

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
    
    else:
        baskets = Baskets.objects.filter(session_key=request.session.session_key, dish=dish )

        if baskets.exists():
            basket = baskets.first()
            if basket:
                basket.quantity += 1
                basket.save()
        else:
            Baskets.objects.create(session_key=request.session.session_key, dish=dish, quantity=1)
    
    user_baskets = get_user_baskets(request)
    total_quantity = sum(basket.quantity for basket in user_baskets)
    total_price = round(sum(basket.dish.price*basket.quantity for basket in user_baskets),2)
    basket_items_html = render_to_string(
    "baskets/includes/included_basket.html", {"user_baskets": user_baskets, 'total_quantity': total_quantity,'total_price': total_price},  request=request
    )
    response_data = {
        "message": "Товар добавлен в корзину",
        "basket_items_html": basket_items_html,
    }
    return JsonResponse(response_data)


def basket_change(request):
    basket_id = request.POST.get("basket_id")
    quantity = request.POST.get("quantity")

    basket = Baskets.objects.get(id=basket_id)
    basket.quantity = quantity
    basket.save()
    updated_quantity = basket.quantity

    user_baskets = get_user_baskets(request)
    total_quantity = sum(basket.quantity for basket in user_baskets)
    total_price = round(sum(basket.dish.price*basket.quantity for basket in user_baskets),2)
    basket_items_html = render_to_string(
    "baskets/includes/included_basket.html", {"user_baskets": user_baskets, 'total_quantity': total_quantity,'total_price': total_price},  request=request
    )

    response_data = {
        "message": "Количество товара изменено",
        "basket_items_html": basket_items_html,
        "quantity": updated_quantity,
    }

    return JsonResponse(response_data)


# def basket_remove(request, basket_id):  # basket_id
#     basket = Baskets.objects.get(id=basket_id)
#     basket.delete()

#     return redirect(request.META['HTTP_REFERER'])

def basket_remove(request):
    
    basket_id = request.POST.get('basket_id')
    basket = Baskets.objects.get(id=basket_id)
    quantity_deleted = basket.quantity 
    basket.delete()

    user_baskets = get_user_baskets(request)
    total_quantity = sum(basket.quantity for basket in user_baskets)
    total_price = round(sum(basket.dish.price*basket.quantity for basket in user_baskets),2)
    basket_items_html = render_to_string(
    "baskets/includes/included_basket.html", {"user_baskets": user_baskets, 'total_quantity': total_quantity,'total_price': total_price},  request=request
    )

    response_data = {
        "message": "Товар удален",
        "basket_items_html": basket_items_html,
        "quantity_deleted": quantity_deleted,
    }

    return JsonResponse(response_data)