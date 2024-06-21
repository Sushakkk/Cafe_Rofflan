from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('order_dish/', views.order_dish, name='order_dish'),
]