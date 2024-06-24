from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('search/', views.catalog, name='search'),
    # path('<slug:category_slug>/<int:page>/', views.catalog, name='index'),
    path('dish/<slug:dish_slug>/', views.dish, name='dish'),

    # path('menu/', views.menu, name='menu'),
    # path('', views.menu, name='menu'),
    # path('<slug:category_slug>/', views.menu, name='index'),
    # path('search/', views.menu, name='search'),
]
