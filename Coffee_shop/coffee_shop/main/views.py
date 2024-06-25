from django.shortcuts import render
from django.http import HttpResponse
from baskets.templatetags.baskets_tags import user_baskets

from goods.models import Categories


# Create your views here.


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': "Магазин мебели HOME",
    }
    user_baskets(context, request)
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': "О нас",
        'text_on_page': "Текст о том почему этот магазин такой классный, и какой хороший товар."
    }
    user_baskets(context, request)
    return render(request, 'main/about.html', context)
