
from django.contrib import messages
from django.forms import ValidationError
from django.shortcuts import redirect, render
from baskets.templatetags.baskets_tags import user_baskets
# Create your views here.
from baskets.models import Baskets
from orders.models import Order, OrderItem
from orders.forms import CreateOrderForm
from django.db import transaction
from django.contrib.auth.decorators import login_required
# import logging

# logging.getLogger('django')
@login_required
def create_order(request):
    
    if request.method == "POST":
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    basket_items = Baskets.objects.filter(user=user)

                    if basket_items.exists():
                        order = Order.objects.create(
                            user=user,
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )

                        for basket_item in basket_items:
                            dish=basket_item.dish
                            name=basket_item.dish.name
                            price=basket_item.dish.sell_price()
                            quantity=basket_item.quantity
                    
                            if dish.quantity < quantity:
                                raise ValidationError( f'Недостаточное количество товара {name} на складе. В наличии - {dish.quantity}' )

                            OrderItem.objects.create(
                                    order=order,
                                    dish=dish,
                                    name=name,
                                    price=price,
                                    quantity=quantity,
                            )
                            dish.quantity -= quantity
                            dish.save()
                
                        basket_items.delete()
                        messages.success(request, "Заказ оформлен!")
                        return redirect("users:profile")


            except ValidationError as e:
                error_e=str(e)
                messages.success(request, error_e)
                return redirect('users:users-basket')

    else:
        initial = {
            'first_name' : request.user.first_name,
            'last_name': request.user.last_name,
            'phone' : request.user.phone,
        }
        # logging.debug(f'Имя:{request.user.first_name}  Фамилия:{request.user.last_name} телефон:{request.user.phone}  объект:{request.user}')
        form = CreateOrderForm(initial=initial)
    context={
        'title': 'Home - Оформление заказа',
        'form': form,
    }
    user_baskets(context, request)
    return render(request, "orders/create_order.html", context)