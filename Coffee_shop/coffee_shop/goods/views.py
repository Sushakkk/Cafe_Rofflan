from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from goods.models import Dishes
from goods.utils import q_search

def catalog(request, category_slug=None):
    
    
    
    page = request.GET.get('page', 1)

    query = request.GET.get('q', None)
    
    

    if category_slug == "all":
        goods = Dishes.objects.all()
    elif query:
        goods = q_search(query)
    else: goods = Dishes.objects.filter(category__slug=category_slug)
   
   
   
    # сколько на страницу карточек 
    paginator = Paginator(goods,1)
    current_page=paginator.page(page)
    
    
   
    context = {
        "title": "Home - Каталог",
        "goods":  current_page, #отображаем первую страницу 
        "slug_url" : category_slug
    }
    
    return render(request, 'goods/catalog.html', context)

def dish(request, dish_slug):
    dish = get_object_or_404(Dishes, slug=dish_slug)
    
    context = {
        'dish': dish
    }
    
    return render(request, 'goods/dish.html', context)






