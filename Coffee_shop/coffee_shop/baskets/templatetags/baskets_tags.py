from django import template

from baskets.models import Baskets

register = template.Library()


@register.simple_tag(takes_context=True)
def user_baskets(context, request):
    if request.user.is_authenticated:
        user_baskets = Baskets.objects.filter(user=request.user)
        total_quantity = sum(basket.quantity for basket in user_baskets)
        total_price = round(sum(basket.dish.price*basket.quantity for basket in user_baskets),2)

        context['user_baskets'] = user_baskets
        context['total_quantity'] = total_quantity
        context['total_price'] = total_price
        return ''
