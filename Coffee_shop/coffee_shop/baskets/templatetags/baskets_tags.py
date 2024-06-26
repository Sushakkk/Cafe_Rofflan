from django import template

from baskets.models import Baskets
from baskets.utils import get_user_baskets
register = template.Library()


@register.simple_tag(takes_context=True)
def user_baskets(context, request):
    user_baskets = get_user_baskets(request)
    total_quantity = sum(basket.quantity for basket in user_baskets)
    total_price = round(sum(basket.dish.price*basket.quantity for basket in user_baskets),2)

    context['user_baskets'] = user_baskets
    context['total_quantity'] = total_quantity
    context['total_price'] = total_price
    return ''
