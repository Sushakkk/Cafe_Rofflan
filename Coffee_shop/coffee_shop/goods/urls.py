from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('search/', views.catalog, name='search'),
    # path('<slug:category_slug>/<int:page>/', views.catalog, name='index'),
    path('dish/<slug:dish_slug>/', views.dish, name='dish'),
]
