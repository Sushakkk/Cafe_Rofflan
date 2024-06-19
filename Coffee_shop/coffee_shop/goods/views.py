from django.shortcuts import render

from goods.models import Dishes


def catalog(request):
    
    goods = Dishes.objects.all()
    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    
    return render(request, 'goods/catalog.html', context)


def dish(request, dish_slug):
    
    dish = Dishes.objects.get(slug=dish_slug)
    
    context = {
        'dish': dish
    }
    
    
    return render(request, 'goods/dish.html', context)